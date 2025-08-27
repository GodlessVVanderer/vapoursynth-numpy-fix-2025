# VapourSynth NumPy 2.0 Fix (Works with ANY Video Player)
### 🎯 Fix for "numpy.core.multiarray failed to import" error on older GPUs

> **THE SOLUTION:** It's not Python 3.12 that's broken - it's NumPy 2.0! This fixes VapourSynth for frame interpolation, video processing, and works with SVP4, mpv, MPC-HC, PotPlayer, or any player.

## ⚠️ MASSIVE DOWNLOAD WARNING
**The full installer downloads:**
- PyTorch with CUDA 11.8: **~2-3 GB** 
- NVIDIA CUDA Toolkit (if needed): **~2-8 GB**
- Other dependencies: **~500 MB**
- **TOTAL: Up to 11GB if you need full CUDA!**

**TIP:** Run `VapourSynth_Installer_TEST.py` FIRST - it verifies everything WITHOUT downloading gigabytes!

## ⚠️ CRITICAL WARNING
**DO NOT UPDATE THESE PACKAGES OR EVERYTHING BREAKS:**
- NumPy MUST stay at **1.26.4** (NumPy 2.0 breaks VapourSynth!)
- VapourSynth MUST stay at **R72** (R73+ has issues)
- PyTorch MUST stay at **2.7.0+cu118** (CUDA 12.x causes conflicts)

## 🚀 Quick Start

### Option 1: Test First (Recommended - NO DOWNLOADS!)
```bash
python VapourSynth_Installer_TEST.py
```
This runs in seconds and verifies your setup WITHOUT downloading gigabytes!

### Option 2: Direct Install (WARNING: 3.5GB DOWNLOAD)
```bash
pip install numpy==1.26.4
pip install torch==2.7.0+cu118 --index-url https://download.pytorch.org/whl/cu118  # THIS IS 3GB!
pip install vapoursynth==72
```

### Option 3: Full Installer (WARNING: 3.5GB DOWNLOAD)
```bash
python VapourSynth_Installer.py
```
Creates a complete virtual environment but downloads 3.5GB of packages!

## ✅ What This Fixes

- VapourSynth frame interpolation with **any video player**
- Works with SVP4, mpv, MPC-HC, PotPlayer
- Video processing scripts and filters
- AI upscaling tools that use VapourSynth
- ANY software that depends on VapourSynth + NumPy

## ✅ Verified Working Configuration

| Component | Version | Critical Notes |
|-----------|---------|----------------|
| **Python** | 3.12.8 | Yes, 3.12 WORKS! |
| **NumPy** | 1.26.4 | ⚠️ NOT 2.0! |
| **PyTorch** | 2.7.0+cu118 | CUDA 11.8 only (3GB download!) |
| **VapourSynth** | R72 | Not R73+ |
| **CUDA** | 11.8 | Better compatibility |

## 💻 Tested Hardware

- **GPU:** NVIDIA GTX 1650 Mobile (4GB VRAM)
- **CPU:** AMD Ryzen 7 4800HS (8-core)
- **Performance:** 1080p@60fps uses only 40% GPU!

## 📊 Performance Benchmarks

| Resolution | Target FPS | GPU Usage | Status |
|------------|------------|-----------|---------|
| 1080p | 60fps | 40% | Perfect |
| 1080p | 120fps | 70% | Smooth |
| 4K | 60fps | 90% | Works |
| Anime | 144fps | 60% | Great |

## 🔧 Example: PotPlayer + SVP4 Configuration

1. Start SVP4 Manager (if using SVP4)
2. Open PotPlayer
3. Press **F5 → Video → VapourSynth** (NOT AviSynth!)
4. Enable VapourSynth
5. SVP4 tray icon shows "Active"

**Note:** This fix works with ANY player that uses VapourSynth, not just PotPlayer!

## 🎯 The Key Discovery

**Everyone says Python 3.12 doesn't work with VapourSynth - THEY'RE WRONG!**

The real problem is NumPy 2.0 which changed their C API. VapourSynth hasn't updated their bindings yet (as of August 2025), so NumPy 2.0 causes:
- `ImportError: numpy.core.multiarray failed to import`
- `VapourSynth has no attribute 'core'`
- Complete failure of frame interpolation

## 📁 Repository Contents

- `VapourSynth_Installer.py` - Full installer with virtual environment (DOWNLOADS 3.5GB!)
- `VapourSynth_Installer_TEST.py` - Test version with verification (NO DOWNLOADS!)

## ❌ Common Mistakes to Avoid

| Wrong | Right | Why |
|-------|-------|-----|
| NumPy 2.0 | NumPy 1.26.4 | v2.0 breaks VapourSynth bindings |
| VapourSynth R73 | VapourSynth R72 | R73 has compatibility issues |
| CUDA 12.x | CUDA 11.8 | PyTorch stability |
| `pip install --upgrade` | Use exact versions | Prevents breaking updates |

## 🆘 Troubleshooting

### If you accidentally updated NumPy:
```bash
pip uninstall numpy -y
pip install numpy==1.26.4
```

### VapourSynth not working in your player:
- Each player has different settings (F5 in PotPlayer, preferences in mpv, etc.)
- Make sure VapourSynth mode is enabled, not AviSynth

### Poor performance on laptop:
- Force NVIDIA GPU in Windows Graphics Settings
- Add your video player → High Performance

## 🤝 Contributing

Found an improvement? Please share! This configuration took weeks to figure out through trial and error.

## 📜 License

MIT - Use freely, help others!

---

**Remember:** You DON'T need an RTX 4090 for video processing. A GTX 1650 Mobile works great with the right setup!