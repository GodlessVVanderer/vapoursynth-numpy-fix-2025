#!/usr/bin/env python3
"""
VapourSynth + SVP4 Community Installer
Automatically sets up the working environment with proper versions
"""

import os
import sys
import subprocess
import platform
import json
import urllib.request
from pathlib import Path
import venv
import shutil

class VapourSynthInstaller:
    def __init__(self):
        self.home = Path.home()
        self.install_dir = self.home / "VapourSynth_Environment"
        self.issues_found = []
        self.fixes_applied = []
        
    def check_system(self):
        """Check system compatibility"""
        print("🔍 Checking system requirements...")
        
        # Check OS
        if platform.system() != "Windows":
            print("⚠️  This installer is designed for Windows")
            return False
            
        # Check Python version
        py_version = sys.version_info
        print(f"Python: {py_version.major}.{py_version.minor}.{py_version.micro}")
        
        if py_version.major != 3 or py_version.minor < 10:
            self.issues_found.append("Python 3.10+ required")
            return False
            
        # Check for NVIDIA GPU
        try:
            result = subprocess.run(['nvidia-smi'], capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ NVIDIA GPU detected")
            else:
                print("⚠️  No NVIDIA GPU detected - CPU mode only")
        except:
            print("⚠️  nvidia-smi not found - GPU acceleration may not work")
            
        return True
    
    def create_virtual_environment(self):
        """Create isolated Python environment"""
        print(f"\n📦 Creating virtual environment at {self.install_dir}")
        
        if self.install_dir.exists():
            response = input("Environment exists. Recreate? (y/n): ")
            if response.lower() == 'y':
                shutil.rmtree(self.install_dir)
            else:
                return False
                
        # Create venv
        venv.create(self.install_dir, with_pip=True)
        
        # Get paths
        if platform.system() == "Windows":
            self.python_exe = self.install_dir / "Scripts" / "python.exe"
            self.pip_exe = self.install_dir / "Scripts" / "pip.exe"
        else:
            self.python_exe = self.install_dir / "bin" / "python"
            self.pip_exe = self.install_dir / "bin" / "pip"
            
        print("✅ Virtual environment created")
        return True
    
    def install_packages(self):
        """Install exact working versions"""
        print("\n📥 Installing packages with correct versions...")
        
        packages = [
            ("numpy", "1.26.4", "Critical: Must be 1.26.4, NOT 2.0!"),
            ("torch", "2.7.0+cu118", "CUDA 11.8 build for compatibility"),
            ("vapoursynth", "72", "R72 is the stable version"),
        ]
        
        # Upgrade pip first
        subprocess.run([str(self.pip_exe), "install", "--upgrade", "pip"], 
                      capture_output=True)
        
        for package, version, note in packages:
            print(f"\nInstalling {package}=={version}")
            print(f"  ℹ️  {note}")
            
            if package == "torch":
                # Special handling for PyTorch with CUDA
                cmd = [
                    str(self.pip_exe), "install", 
                    f"torch=={version}", "torchvision", "torchaudio",
                    "--index-url", "https://download.pytorch.org/whl/cu118"
                ]
            else:
                cmd = [str(self.pip_exe), "install", f"{package}=={version}"]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"  ✅ {package} installed successfully")
                self.fixes_applied.append(f"Installed {package} {version}")
            else:
                print(f"  ❌ Failed to install {package}")
                print(f"  Error: {result.stderr}")
                self.issues_found.append(f"Failed to install {package}")
    
    def check_installations(self):
        """Verify SVP4 and PotPlayer are installed"""
        print("\n🔍 Checking required applications...")
        
        # Check SVP4
        svp4_paths = [
            Path(r"C:\Program Files (x86)\SVP 4\SVPManager.exe"),
            Path(r"C:\Program Files\SVP 4\SVPManager.exe")
        ]
        
        self.svp4_path = None
        for path in svp4_paths:
            if path.exists():
                self.svp4_path = path
                print(f"✅ SVP4 found: {path}")
                break
        
        if not self.svp4_path:
            print("❌ SVP4 not found")
            print("  Download from: https://www.svp-team.com/")
            self.issues_found.append("SVP4 not installed")
        
        # Check PotPlayer
        potplayer_paths = [
            Path(r"C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe"),
            Path(r"C:\Program Files (x86)\DAUM\PotPlayer\PotPlayerMini64.exe")
        ]
        
        self.potplayer_path = None
        for path in potplayer_paths:
            if path.exists():
                self.potplayer_path = path
                print(f"✅ PotPlayer found: {path}")
                break
                
        if not self.potplayer_path:
            print("⚠️  PotPlayer not found (optional)")
            print("  Download from: https://potplayer.daum.net/")
    
    def create_launcher(self):
        """Create convenient launcher script"""
        print("\n🚀 Creating launcher script...")
        
        launcher_path = self.home / "Desktop" / "Launch_VapourSynth_SVP4.bat"
        
        launcher_content = f"""@echo off
echo ============================================
echo VapourSynth + SVP4 Launcher (Fixed Versions)
echo ============================================
echo.
echo Using virtual environment with:
echo - Python 3.12 compatible
echo - NumPy 1.26.4 (NOT 2.0!)
echo - VapourSynth R72
echo - CUDA 11.8 support
echo.

rem Activate virtual environment
call "{self.install_dir}\\Scripts\\activate.bat"

rem Set environment variables
set PYTHONPATH={self.install_dir}\\Lib\\site-packages
set VAPOURSYNTH_PATH={self.install_dir}\\Lib\\site-packages

rem Start SVP4 if found
if exist "{self.svp4_path}" (
    echo Starting SVP4 Manager...
    start "" "{self.svp4_path}"
    timeout /t 5 /nobreak >nul
)

rem Start PotPlayer if found  
if exist "{self.potplayer_path}" (
    echo Starting PotPlayer...
    start "" "{self.potplayer_path}"
    echo.
    echo ✅ Remember: In PotPlayer press F5 → Video → VapourSynth → Enable
)

echo.
echo ✅ Environment ready! Your setup uses the WORKING versions.
echo.
pause
"""
        
        with open(launcher_path, 'w') as f:
            f.write(launcher_content)
            
        print(f"✅ Launcher created: {launcher_path}")
        self.fixes_applied.append("Created desktop launcher")
    
    def create_test_script(self):
        """Create script to verify the installation"""
        print("\n🧪 Creating test script...")
        
        test_script = self.install_dir / "test_setup.py"
        
        test_content = '''#!/usr/bin/env python
"""Test VapourSynth installation"""

import sys
print(f"Python: {sys.version}")

try:
    import numpy as np
    print(f"✅ NumPy: {np.__version__}", end="")
    if np.__version__.startswith("2."):
        print(" ❌ ERROR: NumPy 2.0 will break VapourSynth!")
    elif np.__version__.startswith("1.26"):
        print(" ✅ Correct version!")
    else:
        print(" ⚠️  Unexpected version")
except ImportError as e:
    print(f"❌ NumPy import failed: {e}")

try:
    import torch
    print(f"✅ PyTorch: {torch.__version__}")
    if torch.cuda.is_available():
        print(f"✅ CUDA available: {torch.cuda.get_device_name(0)}")
    else:
        print("⚠️  CUDA not available")
except ImportError:
    print("⚠️  PyTorch not installed (optional)")

try:
    import vapoursynth as vs
    core = vs.core
    print(f"✅ VapourSynth: {core.version()}")
    
    # Test basic functionality
    clip = core.std.BlankClip()
    print("✅ VapourSynth core is functional")
except ImportError as e:
    print(f"❌ VapourSynth import failed: {e}")
except Exception as e:
    print(f"❌ VapourSynth core error: {e}")

print("\\n" + "="*50)
print("Test complete! Check for any ❌ errors above.")
'''
        
        with open(test_script, 'w') as f:
            f.write(test_content)
            
        print(f"✅ Test script created: {test_script}")
        
        # Run the test
        print("\n🧪 Running test...")
        result = subprocess.run([str(self.python_exe), str(test_script)], 
                              capture_output=True, text=True)
        print(result.stdout)
        
        if result.returncode != 0:
            print(f"⚠️  Test errors: {result.stderr}")
    
    def run(self):
        """Main installation process"""
        print("="*60)
        print("VapourSynth + SVP4 Community Installer")
        print("Fixing NumPy 2.0 compatibility issues")
        print("="*60)
        
        if not self.check_system():
            print("\n❌ System requirements not met")
            return False
        
        if not self.create_virtual_environment():
            print("\n❌ Failed to create environment")
            return False
            
        self.install_packages()
        self.check_installations()
        self.create_launcher()
        self.create_test_script()
        
        print("\n" + "="*60)
        print("✅ INSTALLATION COMPLETE!")
        print("="*60)
        print("\nNext steps:")
        print("1. Run Launch_VapourSynth_SVP4.bat from your desktop")
        print("2. In PotPlayer: F5 → Video → VapourSynth → Enable")
        print("3. Check SVP4 tray icon shows 'Active'")
        
        return True

if __name__ == "__main__":
    installer = VapourSynthInstaller()
    success = installer.run()
    
    input("\nPress Enter to exit...")
    sys.exit(0 if success else 1)
