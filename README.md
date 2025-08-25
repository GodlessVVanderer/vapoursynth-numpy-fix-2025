# VapourSynth + SVP4 Frame Interpolation Setup Guide

> 🎬 **Transform any video to smooth 60/120/144 FPS on modest hardware**
> 
> **THE KEY FIX:** NumPy 2.0 breaks VapourSynth - Use 1.26.4! Python 3.12 works fine!

## 🚀 Quick Start (If you just want it working NOW)

```bash
pip install numpy==1.26.4
pip install torch==2.7.0+cu118 --index-url https://download.pytorch.org/whl/cu118
pip install vapoursynth
```

Then in PotPlayer: **F5 → Video → VapourSynth** (NOT AviSynth!) → Enable

## ✅ Verified Working Configuration (August 2025)

| Component | Version | Critical Notes |
|-----------|---------|----------------|
| **Python** | 3.12.8 | Yes, 3.12 WORKS! (ignore outdated guides) |
| **NumPy** | 1.26.4 | ⚠️ MUST be 1.26.4, NOT 2.0! |
| **PyTorch** | 2.7.0+cu118 | CUDA 11.8 build only |
| **VapourSynth** | R72 | Don't use R73+ |
| **CUDA** | 11.8 | Better compatibility than 12.x |

## 💻 Tested Hardware

This setup is confirmed working on:
- **GPU:** NVIDIA GTX 1650 Mobile (4GB VRAM)
- **CPU:** AMD Ryzen 7 4800HS (8-core)
- **RAM:** 16GB DDR4
- **OS:** Windows 10/11

### Performance You Can Expect:
- **1080p → 60fps:** 40% GPU usage
- **1080p → 120fps:** 70% GPU usage
- **4K → 60fps:** 90% GPU usage (but works!)
- **Anime → 144fps:** 60% GPU usage

## 🎯 The Key Discovery

**The Python 3.12 Myth:** Everyone claims Python 3.12 doesn't work with VapourSynth. This is FALSE! The real problem is NumPy 2.0, which breaks VapourSynth's Python bindings. Use NumPy 1.26.4 and Python 3.12 works perfectly.

## ❌ Common Mistakes to Avoid

| Wrong | Right | Why |
|-------|-------|-----|
| NumPy 2.0 | NumPy 1.26.4 | v2.0 breaks VapourSynth bindings |
| VapourSynth R73 | VapourSynth R72 | R73 has compatibility issues |
| CUDA 12.x | CUDA 11.8 | PyTorch stability |
| AviSynth mode | VapourSynth mode | Direct integration |
| Python 3.11 | Python 3.12 | 3.12 works perfectly! |

## 📦 Complete Installation Guide

### Step 1: Install Python 3.12
Download from python.org - **Version 3.12.x** (NOT 3.11, NOT 3.13)
- ✅ Add Python to PATH
- ✅ Install for all users

### Step 2: Install VapourSynth R72
Download VapourSynth-R72.exe from GitHub releases
- Default installation
- It will auto-detect Python

### Step 3: Install EXACT Package Versions
```bash
# CRITICAL: Must be these exact versions!
pip install numpy==1.26.4
pip install torch==2.7.0+cu118 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install vapoursynth
```

### Step 4: Install SVP4
1. Download from svp-team.com
2. Install with default settings
3. It will auto-detect VapourSynth

### Step 5: Configure PotPlayer
1. Start **SVP4 Manager** (runs in system tray)
2. Open **PotPlayer 64-bit**
3. Press **F5** → **Video** → **VapourSynth** ← THIS IS CRITICAL!
4. Check **"Enable VapourSynth"**
5. Play any video - SVP4 tray shows "Active"

## 🔧 For Laptop Users (Dual GPU)

### Force NVIDIA GPU:
```
Windows Settings → System → Display → Graphics
Add PotPlayer.exe → High Performance

NVIDIA Control Panel → Manage 3D Settings
Add PotPlayer → Select NVIDIA processor
```

## 🔍 Troubleshooting

### "Module 'vapoursynth' not found"
```bash
pip uninstall vapoursynth
pip install vapoursynth==72
```

### "NumPy version conflict"
```bash
pip uninstall numpy
pip install numpy==1.26.4 --force-reinstall
```

### Black screen in PotPlayer
1. Check SVP4 Manager is running
2. Verify: F5 → Video → **VapourSynth** is selected
3. NOT AviSynth mode!

### Poor performance on laptop
- Confirm NVIDIA GPU is being used (not Intel/AMD)
- Set Windows to High Performance mode
- Disable battery saving

## 📈 Results

- Smooth frame interpolation on a GTX 1650 Mobile
- Stable for weeks with no crashes
- 1080p anime to 144fps with 60% GPU usage
- Even 4K to 60fps is possible (though GPU-intensive)

## 🤝 Contributing

Found an improvement? Please open an issue or PR! This configuration took weeks to figure out through trial and error. The community needs more documented working setups.

## 📁 Files in This Repo

- `quick_install.bat` - One-click installer for the correct versions
- `test_versions.py` - Script to verify your setup
- `FORUM_POST.md` - Ready-to-post forum solution
- `REDDIT_POST.md` - Reddit-formatted post

## ⚠️ Important Notes

- SVP4 requires a license (free version available)
- VapourSynth is open source
- This guide assumes Windows 10/11
- Tested August 2025

---

**Remember:** You DON'T need an RTX 4090 for frame interpolation. A GTX 1650 Mobile works great with the right setup!

## Help Spread the Word

If this helped you, please:
- ⭐ Star this repo
- Share on forums/Reddit
- Report if it works with your hardware
- Contribute any improvements

Together we can save others from weeks of troubleshooting!