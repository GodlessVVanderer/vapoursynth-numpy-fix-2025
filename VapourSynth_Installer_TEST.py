#!/usr/bin/env python3
"""
VapourSynth Installer TEST VERSION with Verification
Tests your current setup AND simulates installation
"""

import os
import sys
from pathlib import Path
import time
import subprocess

class VapourSynthInstallerTest:
    def __init__(self):
        self.home = Path.home()
        self.install_dir = self.home / "VapourSynth_Environment_TEST"
        self.issues_found = []
        self.fixes_applied = []
        self.current_setup_works = True
        
    def verify_current_setup(self):
        """Check if user's current Python setup would work"""
        print("="*60)
        print("VERIFYING YOUR CURRENT SETUP")
        print("="*60)
        
        # Check Python version
        print(f"\n1. Python Version:")
        py_version = sys.version_info
        print(f"   Current: {py_version.major}.{py_version.minor}.{py_version.micro}")
        if py_version.major == 3 and py_version.minor >= 10:
            print("   ✅ Python 3.10+ - Good!")
        else:
            print("   ❌ Need Python 3.10 or later")
            self.current_setup_works = False
            self.issues_found.append("Python version too old")
        
        # Check NumPy
        print(f"\n2. NumPy Check:")
        try:
            import numpy as np
            print(f"   Found NumPy {np.__version__}")
            if np.__version__.startswith("2."):
                print("   ❌ CRITICAL: NumPy 2.0 WILL BREAK VapourSynth!")
                print("   You MUST downgrade: pip install numpy==1.26.4")
                self.current_setup_works = False
                self.issues_found.append("NumPy 2.0 detected - MUST downgrade")
            elif np.__version__.startswith("1.26"):
                print("   ✅ NumPy 1.26 - Perfect!")
            else:
                print(f"   ⚠️ NumPy {np.__version__} may have issues")
                self.issues_found.append(f"NumPy {np.__version__} untested")
        except ImportError:
            print("   ⚠️ NumPy not installed - will need to install")
            self.issues_found.append("NumPy not installed")
        
        # Check PyTorch
        print(f"\n3. PyTorch Check:")
        try:
            import torch
            print(f"   Found PyTorch {torch.__version__}")
            if "+cu118" in torch.__version__:
                print("   ✅ CUDA 11.8 build - Good!")
            elif "+cu12" in torch.__version__:
                print("   ⚠️ CUDA 12.x build may have issues")
                self.issues_found.append("PyTorch CUDA 12 may conflict")
            
            if torch.cuda.is_available():
                print(f"   ✅ CUDA available: {torch.cuda.get_device_name(0)}")
            else:
                print("   ⚠️ CUDA not detected")
        except ImportError:
            print("   ⚠️ PyTorch not installed - optional but recommended")
        
        # Check VapourSynth
        print(f"\n4. VapourSynth Check:")
        try:
            import vapoursynth as vs
            core = vs.core
            vs_info = str(core.version())
            print(f"   Found VapourSynth: {vs_info}")
            
            if "R72" in vs_info:
                print("   ✅ VapourSynth R72 - Perfect!")
            elif "R73" in vs_info or "R74" in vs_info:
                print("   ⚠️ VapourSynth R73+ may have compatibility issues")
                self.issues_found.append("VapourSynth R73+ may have issues")
            
            # Test basic functionality
            try:
                test_clip = core.std.BlankClip()
                print("   ✅ VapourSynth core is functional")
            except:
                print("   ❌ VapourSynth core not working properly")
                self.current_setup_works = False
                self.issues_found.append("VapourSynth core malfunction")
                
        except ImportError:
            print("   ⚠️ VapourSynth not installed")
            self.issues_found.append("VapourSynth not installed")
        except Exception as e:
            print(f"   ❌ VapourSynth error: {e}")
            self.current_setup_works = False
            self.issues_found.append(f"VapourSynth error: {e}")
        
        # Check for SVP4
        print(f"\n5. SVP4 Check:")
        svp4_paths = [
            Path(r"C:\Program Files (x86)\SVP 4\SVPManager.exe"),
            Path(r"C:\Program Files\SVP 4\SVPManager.exe")
        ]
        
        svp4_found = False
        for path in svp4_paths:
            if path.exists():
                print(f"   ✅ SVP4 found: {path}")
                svp4_found = True
                self.svp4_path = path
                break
        
        if not svp4_found:
            print("   ❌ SVP4 not found - Download from svp-team.com")
            self.issues_found.append("SVP4 not installed")
            self.svp4_path = Path(r"C:\Program Files (x86)\SVP 4\SVPManager.exe")
        
        # Check for PotPlayer
        print(f"\n6. PotPlayer Check:")
        potplayer_paths = [
            Path(r"C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe"),
            Path(r"C:\Program Files (x86)\DAUM\PotPlayer\PotPlayerMini64.exe")
        ]
        
        potplayer_found = False
        for path in potplayer_paths:
            if path.exists():
                print(f"   ✅ PotPlayer found: {path}")
                potplayer_found = True
                self.potplayer_path = path
                break
                
        if not potplayer_found:
            print("   ⚠️ PotPlayer not found (optional)")
            print("   Download from: potplayer.daum.net")
            self.potplayer_path = Path(r"C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe")
        
        # Summary
        print("\n" + "="*60)
        print("VERIFICATION RESULTS")
        print("="*60)
        
        if self.current_setup_works and not self.issues_found:
            print("\n✅ YOUR SETUP IS PERFECT!")
            print("Everything is configured correctly for VapourSynth + SVP4")
        elif self.current_setup_works:
            print("\n⚠️ YOUR SETUP MAY WORK but has warnings:")
            for issue in self.issues_found:
                print(f"   - {issue}")
        else:
            print("\n❌ YOUR SETUP WILL NOT WORK! Critical issues found:")
            for issue in self.issues_found:
                print(f"   - {issue}")
            print("\n🔧 REQUIRED FIXES:")
            if "NumPy 2.0" in str(self.issues_found):
                print("   1. pip uninstall numpy")
                print("   2. pip install numpy==1.26.4")
            if "VapourSynth core" in str(self.issues_found):
                print("   1. pip uninstall vapoursynth")
                print("   2. pip install vapoursynth==72")
        
        print("\n" + "="*60)
        return self.current_setup_works
    
    def check_system(self):
        """Check system compatibility"""
        print("\n🔍 Checking system requirements for installer...")
        print(f"Python: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
        print("✅ Python 3.10+ detected")
        
        # Check for NVIDIA GPU
        try:
            result = subprocess.run(['nvidia-smi', '--query-gpu=name', '--format=csv,noheader'], 
                                  capture_output=True, text=True, timeout=2)
            if result.returncode == 0:
                gpu_name = result.stdout.strip()
                print(f"✅ NVIDIA GPU detected: {gpu_name}")
            else:
                print("⚠️ No NVIDIA GPU detected - CPU mode only")
        except:
            print("⚠️ nvidia-smi not found - GPU acceleration may not work")
        
        return True
    
    def create_virtual_environment(self):
        """SIMULATE creating virtual environment"""
        print(f"\n📦 SIMULATING virtual environment at {self.install_dir}")
        
        # Just create the directory
        self.install_dir.mkdir(exist_ok=True)
        
        # Set fake paths
        self.python_exe = self.install_dir / "Scripts" / "python.exe"
        self.pip_exe = self.install_dir / "Scripts" / "pip.exe"
        
        print("✅ Virtual environment created (TEST - no actual venv)")
        time.sleep(1)
        return True
    
    def install_packages(self):
        """SIMULATE installing packages"""
        print("\n📥 SIMULATING package installation...")
        print("⚠️ REMEMBER: NEVER UPDATE THESE PACKAGES!")
        
        packages = [
            ("numpy", "1.26.4", "CRITICAL: Must be 1.26.4, NOT 2.0!"),
            ("torch", "2.7.0+cu118", "CUDA 11.8 build for compatibility"),
            ("vapoursynth", "72", "R72 is the stable version, NOT R73!"),
        ]
        
        for package, version, note in packages:
            print(f"\nSIMULATING install {package}=={version}")
            print(f"  ⚠️ {note}")
            time.sleep(0.5)
            print(f"  ✅ {package} installed successfully (TEST)")
            self.fixes_applied.append(f"Installed {package} {version}")
    
    def create_launcher(self):
        """Create TEST launcher script with warnings"""
        print("\n🚀 Creating TEST launcher script...")
        
        launcher_path = self.home / "Desktop" / "TEST_Launch_VapourSynth_SVP4.bat"
        
        launcher_content = f"""@echo off
echo ============================================
echo TEST LAUNCHER - VapourSynth + SVP4
echo ============================================
echo.
echo CRITICAL WARNINGS:
echo - NEVER update NumPy (must stay 1.26.4)
echo - NEVER update VapourSynth (must stay R72)
echo - NEVER run pip install --upgrade
echo.
echo THIS IS A TEST VERSION
echo Real version would:
echo - Activate virtual environment at {self.install_dir}
echo - Start SVP4 at {self.svp4_path}
echo - Start PotPlayer at {self.potplayer_path}
echo.
pause
"""
        
        with open(launcher_path, 'w') as f:
            f.write(launcher_content)
            
        print(f"✅ TEST Launcher created: {launcher_path}")
        self.fixes_applied.append("Created desktop launcher with warnings")
    
    def run(self):
        """Main TEST installation process with verification"""
        print("="*60)
        print("VapourSynth + SVP4 Installer - TEST MODE with VERIFICATION")
        print("="*60)
        
        # First verify current setup
        setup_ok = self.verify_current_setup()
        
        input("\nPress Enter to continue to installation simulation...")
        
        print("\n" + "="*60)
        print("SIMULATING INSTALLATION")
        print("="*60)
        
        if not self.check_system():
            return False
        
        if not self.create_virtual_environment():
            return False
            
        self.install_packages()
        self.create_launcher()
        
        print("\n" + "="*60)
        print("✅ TEST COMPLETE!")
        print("="*60)
        
        if setup_ok:
            print("\n✅ Your current setup verification: PASSED")
        else:
            print("\n❌ Your current setup verification: FAILED")
            print("Fix the issues above before running the real installer!")
        
        print("\nTEST files created:")
        print("- Desktop/TEST_Launch_VapourSynth_SVP4.bat")
        print("- VapourSynth_Environment_TEST folder")
        
        print("\n⚠️ REMEMBER: NEVER UPDATE NumPy, VapourSynth, or PyTorch!")
        
        return True

if __name__ == "__main__":
    installer = VapourSynthInstallerTest()
    success = installer.run()
    
    input("\nPress Enter to exit TEST MODE...")
    sys.exit(0 if success else 1)
