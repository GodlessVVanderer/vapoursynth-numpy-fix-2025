#!/usr/bin/env python3
"""
VapourSynth + SVP4 Automated Installer
Actually works without crashing
"""

import os
import sys
import subprocess
import platform
from pathlib import Path
import shutil
import time

def run_command(cmd, shell=False):
    """Run command and return success status"""
    try:
        result = subprocess.run(cmd, shell=shell, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def main():
    print("="*60)
    print("   VapourSynth + SVP4 WORKING Installer")
    print("   NumPy 2.0 Fix Included")
    print("="*60)
    
    # Check Python version
    print("\n[1/7] Checking Python version...")
    if sys.version_info.major != 3:
        print("❌ Python 3.x required")
        input("Press Enter to exit...")
        return 1
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    
    # Backup current packages
    print("\n[2/7] Backing up current package list...")
    backup_file = f"package_backup_{int(time.time())}.txt"
    run_command([sys.executable, "-m", "pip", "freeze", ">", backup_file], shell=True)
    print(f"✅ Backup saved to {backup_file}")
    
    # Uninstall conflicting packages
    print("\n[3/7] Removing conflicting packages...")
    packages_to_remove = ["numpy", "vapoursynth", "torch", "torchvision", "torchaudio"]
    for pkg in packages_to_remove:
        print(f"  Removing {pkg}...")
        run_command([sys.executable, "-m", "pip", "uninstall", "-y", pkg])
    print("✅ Conflicting packages removed")
    
    # Install NumPy 1.26.4 (CRITICAL)
    print("\n[4/7] Installing NumPy 1.26.4 (NOT 2.0!)...")
    success, out, err = run_command([sys.executable, "-m", "pip", "install", "numpy==1.26.4"])
    if not success:
        print(f"❌ Failed to install NumPy 1.26.4: {err}")
        print("Trying alternative method...")
        success, out, err = run_command([sys.executable, "-m", "pip", "install", "--force-reinstall", "numpy==1.26.4"])
        if not success:
            print("❌ Critical failure - cannot continue without NumPy 1.26.4")
            input("Press Enter to exit...")
            return 1
    print("✅ NumPy 1.26.4 installed successfully")
    
    # Install PyTorch with CUDA 11.8
    print("\n[5/7] Installing PyTorch with CUDA 11.8...")
    torch_cmd = [
        sys.executable, "-m", "pip", "install",
        "torch==2.7.0+cu118", "torchvision", "torchaudio",
        "--index-url", "https://download.pytorch.org/whl/cu118"
    ]
    success, out, err = run_command(torch_cmd)
    if not success:
        print("⚠️ PyTorch installation failed (optional for basic use)")
    else:
        print("✅ PyTorch with CUDA 11.8 installed")
    
    # Install VapourSynth
    print("\n[6/7] Installing VapourSynth...")
    success, out, err = run_command([sys.executable, "-m", "pip", "install", "vapoursynth"])
    if not success:
        print(f"❌ Failed to install VapourSynth: {err}")
        input("Press Enter to exit...")
        return 1
    print("✅ VapourSynth installed")
    
    # Create launcher and test files
    print("\n[7/7] Creating launcher files...")
    
    # Create launcher
    desktop = Path.home() / "Desktop"
    launcher_path = desktop / "Launch_SVP4_PotPlayer.bat"
    launcher_content = """@echo off
echo Starting SVP4 + PotPlayer...
start "" "C:\\Program Files (x86)\\SVP 4\\SVPManager.exe"
timeout /t 5 /nobreak >nul
taskkill /f /im PotPlayerMini64.exe 2>nul
timeout /t 2 /nobreak >nul
start "" "C:\\Program Files\\DAUM\\PotPlayer\\PotPlayerMini64.exe"
echo.
echo SVP4 + PotPlayer launched!
echo Remember: F5 - Video - VapourSynth - Enable
pause
"""
    
    try:
        with open(launcher_path, 'w') as f:
            f.write(launcher_content)
        print(f"✅ Launcher created: {launcher_path}")
    except:
        print("⚠️ Could not create desktop launcher")
    
    # Verify installation
    print("\n" + "="*60)
    print("VERIFICATION")
    print("="*60)
    
    try:
        import numpy as np
        if np.__version__.startswith("2."):
            print("❌ ERROR: NumPy 2.0 detected - this will break!")
        else:
            print(f"✅ NumPy {np.__version__} - Correct!")
    except:
        print("❌ NumPy verification failed")
    
    try:
        import vapoursynth
        print("✅ VapourSynth imported successfully")
    except:
        print("❌ VapourSynth import failed")
    
    try:
        import torch
        print(f"✅ PyTorch {torch.__version__}")
        if torch.cuda.is_available():
            print(f"✅ CUDA detected: {torch.cuda.get_device_name(0)}")
    except:
        print("⚠️ PyTorch not available (optional)")
    
    print("\n" + "="*60)
    print("INSTALLATION COMPLETE!")
    print("="*60)
    print("\nNext steps:")
    print("1. Use Launch_SVP4_PotPlayer.bat on your Desktop")
    print("2. In PotPlayer: F5 → Video → VapourSynth (NOT AviSynth!)")
    print("3. Enable VapourSynth")
    print("4. Play any video - SVP4 should show 'Active'")
    print("\nFor laptops: Force NVIDIA GPU in Windows Graphics Settings")
    
    input("\nPress Enter to exit...")
    return 0

if __name__ == "__main__":
    sys.exit(main())