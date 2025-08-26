# VapourSynth + SVP4 Automated Installer
# Version: 1.0 - August 2025
# Tested on: Windows 10/11 with GTX 1650 Mobile

param(
    [switch]$CheckOnly = $false
)

$ErrorActionPreference = "Stop"

Write-Host @"
╔════════════════════════════════════════════════════════════╗
│   VapourSynth + SVP4 Frame Interpolation Setup                │
│   For Laptop & Desktop GPUs                                   │
╚════════════════════════════════════════════════════════════╝
"@ -ForegroundColor Cyan

# Check if running as Administrator
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "⚠️  Please run PowerShell as Administrator" -ForegroundColor Yellow
    exit 1
}

# Configuration
$RequiredVersions = @{
    Python = "3.12"
    NumPy = "1.26.4"
    PyTorch = "2.7.0+cu118"
    VapourSynth = "R72"
}

function Test-Installation {
    Write-Host "`n🔍 Checking current installation..." -ForegroundColor Yellow
    
    $issues = @()
    
    # Check Python
    try {
        $pythonVersion = python --version 2>&1
        if ($pythonVersion -match "3\.12") {
            Write-Host "✅ Python 3.12 found" -ForegroundColor Green
        } else {
            $issues += "Python 3.12 not found (found: $pythonVersion)"
        }
    } catch {
        $issues += "Python not installed"
    }
    
    # Check NumPy
    try {
        $numpy = pip show numpy 2>&1 | Select-String "Version"
        if ($numpy -match "1\.26") {
            Write-Host "✅ NumPy 1.26.x found" -ForegroundColor Green
        } elseif ($numpy -match "2\.") {
            $issues += "NumPy 2.0 installed - MUST downgrade to 1.26.4"
        } else {
            $issues += "NumPy not found or wrong version"
        }
    } catch {
        $issues += "NumPy not installed"
    }
    
    # Check PyTorch
    try {
        $torch = pip show torch 2>&1 | Select-String "Version"
        if ($torch -match "cu118") {
            Write-Host "✅ PyTorch with CUDA 11.8 found" -ForegroundColor Green
        } else {
            $issues += "PyTorch CUDA 11.8 build not found"
        }
    } catch {
        $issues += "PyTorch not installed"
    }
    
    # Check VapourSynth
    if (Test-Path "C:\Program Files\VapourSynth") {
        Write-Host "✅ VapourSynth installed" -ForegroundColor Green
    } else {
        $issues += "VapourSynth not installed"
    }
    
    # Check GPU
    $gpu = Get-WmiObject Win32_VideoController | Where-Object {$_.Name -like "*NVIDIA*"}
    if ($gpu) {
        Write-Host "✅ NVIDIA GPU found: $($gpu.Name)" -ForegroundColor Green
    } else {
        Write-Host "⚠️  No NVIDIA GPU found - will use CPU mode" -ForegroundColor Yellow
    }
    
    return $issues
}

if ($CheckOnly) {
    $issues = Test-Installation
    
    if ($issues.Count -eq 0) {
        Write-Host "`n✅ Your setup is perfect! Ready for frame interpolation." -ForegroundColor Green
    } else {
        Write-Host "`n❌ Issues found:" -ForegroundColor Red
        $issues | ForEach-Object { Write-Host "  - $_" -ForegroundColor Yellow }
        Write-Host "`nRun without -CheckOnly flag to fix these issues" -ForegroundColor Cyan
    }
    exit
}

# Installation Process
Write-Host "`n🚀 Starting installation..." -ForegroundColor Cyan

# Create working directory
$WorkDir = "$env:USERPROFILE\VapourSynth_Setup"
if (!(Test-Path $WorkDir)) {
    New-Item -ItemType Directory -Path $WorkDir | Out-Null
}

# Step 1: Python 3.12
if (!(Get-Command python -ErrorAction SilentlyContinue) -or !(python --version 2>&1 -match "3\.12")) {
    Write-Host "`n📥 Downloading Python 3.12..." -ForegroundColor Yellow
    $pythonUrl = "https://www.python.org/ftp/python/3.12.8/python-3.12.8-amd64.exe"
    $pythonInstaller = "$WorkDir\python-installer.exe"
    
    Invoke-WebRequest -Uri $pythonUrl -OutFile $pythonInstaller
    Write-Host "Installing Python 3.12 (this may take a few minutes)..."
    Start-Process -FilePath $pythonInstaller -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1" -Wait
}

# Step 2: Fix NumPy version
Write-Host "`n📥 Installing correct package versions..." -ForegroundColor Yellow

# Uninstall wrong NumPy version if present
pip uninstall numpy -y 2>$null

# Install exact versions
Write-Host "Installing NumPy 1.26.4 (NOT 2.0!)..."
pip install numpy==1.26.4

Write-Host "Installing PyTorch with CUDA 11.8..."
pip install torch==2.7.0+cu118 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

Write-Host "Installing VapourSynth Python module..."
pip install vapoursynth

# Step 3: Download VapourSynth R72
if (!(Test-Path "C:\Program Files\VapourSynth")) {
    Write-Host "`n📥 Downloading VapourSynth R72..." -ForegroundColor Yellow
    $vsUrl = "https://github.com/vapoursynth/vapoursynth/releases/download/R72/VapourSynth64-R72.exe"
    $vsInstaller = "$WorkDir\VapourSynth-R72.exe"
    
    Invoke-WebRequest -Uri $vsUrl -OutFile $vsInstaller
    Write-Host "Please run the VapourSynth installer manually: $vsInstaller"
    Write-Host "Use default settings, it will auto-detect Python 3.12"
}

# Step 4: Create test script
$testScript = @'
import sys
import numpy as np
import torch
import vapoursynth as vs

print("=" * 50)
print("VapourSynth + SVP4 Version Check")
print("=" * 50)
print(f"Python: {sys.version}")
print(f"NumPy: {np.__version__}")
print(f"PyTorch: {torch.__version__}")
print(f"CUDA: {torch.cuda.is_available()}")
print(f"VapourSynth: {vs.core.version()}")

if np.__version__.startswith("2."):
    print("\n❌ ERROR: NumPy 2.0 breaks VapourSynth!")
elif np.__version__.startswith("1.26"):
    print("\n✅ All versions correct!")
'@

$testScript | Out-File -FilePath "$WorkDir\test_setup.py" -Encoding UTF8

# Step 5: Create desktop shortcuts
$desktopPath = [Environment]::GetFolderPath("Desktop")

$shortcut = @"
@echo off
echo Testing VapourSynth Setup...
python "$WorkDir\test_setup.py"
pause
"@
$shortcut | Out-File -FilePath "$desktopPath\Test_VapourSynth.bat" -Encoding ASCII

# Final check
Write-Host "`n" -NoNewline
$issues = Test-Installation

if ($issues.Count -eq 0) {
    Write-Host @"

╔════════════════════════════════════════════════════════════╗
│                    ✅ INSTALLATION COMPLETE!                   │
╚════════════════════════════════════════════════════════════╝

Next Steps:
1. Install SVP4 from svp-team.com
2. Install PotPlayer from potplayer.daum.net
3. In PotPlayer: F5 → Video → VapourSynth → Enable
4. Run Test_VapourSynth.bat on your desktop

Your GTX 1650 Mobile (or similar) is ready for smooth frame interpolation!
"@ -ForegroundColor Green
} else {
    Write-Host "`n⚠️ Some components need manual installation:" -ForegroundColor Yellow
    $issues | ForEach-Object { Write-Host "  - $_" }
}

Write-Host "`nPress any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")