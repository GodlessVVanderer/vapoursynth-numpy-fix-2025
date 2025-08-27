# VapourSynth NumPy Fix - GTX 1650/1660 Frame Interpolation 
### 🎯 Fix "numpy.core.multiarray failed to import" error (NumPy 1.26.4 solution)

> **THE PROBLEM:** NumPy 2.0 breaks VapourSynth. This installer fixes it by using NumPy 1.26.4.

## ⚠️ MASSIVE DOWNLOAD WARNING
**The full installer downloads:**
- PyTorch with CUDA 11.8: **~2-3 GB** 
- Other dependencies: **~500 MB**
- **TOTAL: ~3.5GB OF DOWNLOADS**

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
This runs in seconds and verifies your setup WITHOUT downloading 3.5GB!

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

## 📊 Performance Benchmarks (with SVP4 + PotPlayer)

| Resolution | Target FPS | GPU Usage | Status |
|------------|------------|-----------|---------|
| 1080p | 60fps | 40% | Perfect |
| 1080p | 120fps | 70% | Smooth |
| 4K | 60fps | 90% | Works |
| Anime | 144fps | 60% | Great |

## 🔧 PotPlayer + SVP4 Setup (Tested Working)

1. Start SVP4 Manager
2. Open PotPlayer
3. Press **F5** → **Video** → **VapourSynth** (NOT AviSynth!)
4. Enable VapourSynth
5. Load your VapourSynth script if needed:
   - Go to VapourSynth settings
   - Browse to your `.vpy` script location
   - Or let SVP4 auto-detect PotPlayer
6. SVP4 tray icon shows "Active" when playing video

**Note:** Other players may work but PotPlayer is confirmed and easy to setup.

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
| AviSynth mode | VapourSynth mode | Direct integration |
| `pip install --upgrade` | Use exact versions | Prevents breaking updates |

## 🆘 Troubleshooting

### If you accidentally updated NumPy:
```bash
pip uninstall numpy -y
pip install numpy==1.26.4
```

### Black screen in PotPlayer:
- Check SVP4 Manager is running
- Verify F5 → Video → **VapourSynth** is selected (NOT AviSynth)
- Check if VapourSynth script path is set correctly

### Poor performance on laptop:
- Force NVIDIA GPU in Windows Graphics Settings
- Add PotPlayer.exe → High Performance

## 🤝 Contributing

Found an improvement? Please share! This configuration took weeks to figure out through trial and error.

## 📜 License

MIT - Use freely, help others!

---

**Remember:** You DON'T need an RTX 4090 for frame interpolation. A GTX 1650 Mobile works great with the right setup!