#!/usr/bin/env python
"""
VapourSynth + SVP4 Version Compatibility Checker
Run this to verify all versions are correct
"""

import sys
import subprocess

def check_version():
    print("=" * 60)
    print("VapourSynth + SVP4 Version Compatibility Checker")
    print("=" * 60)
    
    errors = []
    warnings = []
    
    # Check Python version
    python_version = sys.version_info
    print(f"\n✓ Python: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version.major == 3 and python_version.minor == 12:
        print("  ✓ Python 3.12 - Correct version!")
    else:
        warnings.append(f"  ⚠ Python {python_version.major}.{python_version.minor} - Should be 3.12")
    
    # Check NumPy
    try:
        import numpy as np
        numpy_version = np.__version__
        print(f"\n✓ NumPy: {numpy_version}")
        
        if numpy_version.startswith("1.26"):
            print("  ✓ NumPy 1.26 - Perfect! (NOT 2.0)")
        elif numpy_version.startswith("2."):
            errors.append("  ✗ NumPy 2.0+ WILL BREAK VapourSynth! Downgrade to 1.26.4")
            print("  Fix: pip install numpy==1.26.4")
        else:
            warnings.append(f"  ⚠ NumPy {numpy_version} - Should be 1.26.4")
    except ImportError:
        errors.append("✗ NumPy not installed")
    
    # Check PyTorch and CUDA
    try:
        import torch
        torch_version = torch.__version__
        cuda_available = torch.cuda.is_available()
        
        print(f"\n✓ PyTorch: {torch_version}")
        
        if "+cu118" in torch_version:
            print("  ✓ CUDA 11.8 build - Correct!")
        elif "+cu121" in torch_version or "+cu122" in torch_version:
            errors.append("  ✗ CUDA 12.x build - Compatibility issues!")
            print("  Fix: pip install torch==2.7.0+cu118 --index-url https://download.pytorch.org/whl/cu118")
        
        if cuda_available:
            print(f"  ✓ CUDA is available: {torch.cuda.get_device_name(0)}")
            print(f"  ✓ CUDA version: {torch.version.cuda}")
        else:
            warnings.append("  ⚠ CUDA not detected")
    except ImportError:
        warnings.append("⚠ PyTorch not installed (optional for basic use)")
    
    # Check VapourSynth
    try:
        import vapoursynth as vs
        core = vs.core
        vs_version = core.version()
        
        print(f"\n✓ VapourSynth: {vs_version}")
        
        if "R72" in str(vs_version):
            print("  ✓ VapourSynth R72 - Correct version!")
        elif "R73" in str(vs_version) or "R74" in str(vs_version):
            errors.append("  ✗ VapourSynth R73+ has compatibility issues! Downgrade to R72")
        
        # Test core functionality
        try:
            test_clip = core.std.BlankClip()
            print("  ✓ VapourSynth core is functional")
        except:
            errors.append("  ✗ VapourSynth core not working properly")
            
    except ImportError:
        errors.append("✗ VapourSynth not installed or not in Python path")
    
    # Check for PotPlayer
    import os
    potplayer_paths = [
        r"C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe",
        r"C:\Program Files (x86)\DAUM\PotPlayer\PotPlayerMini64.exe"
    ]
    
    potplayer_found = False
    for path in potplayer_paths:
        if os.path.exists(path):
            print(f"\n✓ PotPlayer found: {path}")
            potplayer_found = True
            break
    
    if not potplayer_found:
        warnings.append("⚠ PotPlayer not found (optional)")
    
    # Check for SVP4
    svp4_paths = [
        r"C:\Program Files (x86)\SVP 4\SVPManager.exe",
        r"C:\Program Files\SVP 4\SVPManager.exe"
    ]
    
    svp4_found = False
    for path in svp4_paths:
        if os.path.exists(path):
            print(f"\n✓ SVP4 found: {path}")
            svp4_found = True
            break
    
    if not svp4_found:
        warnings.append("⚠ SVP4 not found (needed for automatic script management)")
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    if errors:
        print("\n❌ CRITICAL ISSUES (must fix):")
        for error in errors:
            print(error)
    
    if warnings:
        print("\n⚠️ WARNINGS (may need attention):")
        for warning in warnings:
            print(warning)
    
    if not errors and not warnings:
        print("\n✅ ALL VERSIONS CORRECT! Your setup should work perfectly!")
        print("\nTo use:")
        print("1. Start SVP4 Manager")
        print("2. Open PotPlayer")
        print("3. Press F5 → Video → VapourSynth → Enable")
        print("4. Play any video!")
    
    print("\n" + "=" * 60)
    
    # Return exit code
    return 0 if not errors else 1

if __name__ == "__main__":
    exit(check_version())
