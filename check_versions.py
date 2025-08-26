#!/usr/bin/env python
"""Check if all versions are correct for VapourSynth + SVP4"""

import sys

print("="*50)
print("VapourSynth Version Checker")
print("="*50)

errors = []

# Check Python
print(f"\nPython: {sys.version}")
if sys.version_info.major == 3 and sys.version_info.minor == 12:
    print("  ✅ Python 3.12 - Correct!")
else:
    print(f"  ⚠️ Python {sys.version_info.major}.{sys.version_info.minor}")

# Check NumPy
try:
    import numpy as np
    print(f"\nNumPy: {np.__version__}")
    if np.__version__.startswith("2."):
        print("  ❌ ERROR: NumPy 2.0 breaks VapourSynth!")
        errors.append("NumPy 2.0")
    elif np.__version__.startswith("1.26"):
        print("  ✅ NumPy 1.26 - Perfect!")
    else:
        print(f"  ⚠️ Unexpected version")
except ImportError:
    print("❌ NumPy not installed")
    errors.append("NumPy missing")

# Check PyTorch
try:
    import torch
    print(f"\nPyTorch: {torch.__version__}")
    if "+cu118" in torch.__version__:
        print("  ✅ CUDA 11.8 build")
    else:
        print("  ⚠️ Not CUDA 11.8 build")
    
    if torch.cuda.is_available():
        print(f"  ✅ CUDA available: {torch.cuda.get_device_name(0)}")
    else:
        print("  ⚠️ CUDA not detected")
except ImportError:
    print("⚠️ PyTorch not installed")

# Check VapourSynth
try:
    import vapoursynth as vs
    print(f"\nVapourSynth: {vs.core.version()}")
    print("  ✅ VapourSynth working")
except ImportError:
    print("❌ VapourSynth not installed")
    errors.append("VapourSynth missing")

print("\n" + "="*50)
if errors:
    print("❌ ERRORS FOUND:")
    for error in errors:
        print(f"  - {error}")
    print("\nFix with: pip install numpy==1.26.4")
else:
    print("✅ ALL VERSIONS CORRECT!")
    print("\nSetup PotPlayer:")
    print("1. Start SVP4 Manager")
    print("2. In PotPlayer: F5 → Video → VapourSynth → Enable")
print("="*50)