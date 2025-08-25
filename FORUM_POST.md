# SOLVED: VapourSynth + SVP4 Working on Laptop with GTX 1650 Mobile (August 2025)

## The Setup
Finally got VapourSynth + SVP4 working smoothly on my laptop after weeks of version conflicts!

### 💻 MY HARDWARE:
- **CPU:** AMD Ryzen 7 4800HS (8 cores, 16 threads)
- **GPU:** NVIDIA GeForce GTX 1650 Mobile (4GB)
- **iGPU:** AMD Radeon Graphics (integrated)
- **RAM:** 16GB DDR4
- **OS:** Windows 11

### ✅ WORKING SOFTWARE VERSIONS:
```
Python 3.12.8 (YES, 3.12 works perfectly!)
NumPy 1.26.4 (NOT 2.0 - this is critical!)
PyTorch 2.7.0+cu118 (CUDA 11.8 build)
VapourSynth R72 (not R73)
SVP4 Pro (latest)
PotPlayer 64-bit (latest)
NVIDIA Driver: 560.xx
```

## 🔑 KEY DISCOVERIES:

1. **Python 3.12 WORKS** - Ignore guides saying use 3.11
2. **NumPy 1.26.4 is MANDATORY** - NumPy 2.0 breaks VapourSynth bindings
3. **CUDA 11.8 over 12.x** - Works better with older mobile GPUs
4. **GTX 1650 Mobile handles it fine** - Smooth 60fps interpolation even on laptop GPU

## 📦 INSTALLATION COMMANDS:

```bash
# Install exact versions - order matters!
pip install numpy==1.26.4
pip install torch==2.7.0+cu118 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install vapoursynth
```

## ⚙️ POTPLAYER SETUP (This is crucial!):

1. Start **SVP4 Manager** first
2. Launch **PotPlayer 64-bit**
3. Press **F5 → Video → VapourSynth** ← NOT AviSynth!
4. Check **"Enable VapourSynth"**
5. SVP4 tray icon shows **"Active"** when playing

## 🎮 LAPTOP-SPECIFIC TIPS:

### For GTX 1650 Mobile:
- Make sure NVIDIA GPU is selected (not AMD iGPU)
- In NVIDIA Control Panel → Manage 3D Settings → PotPlayer → High-performance NVIDIA
- Windows Graphics Settings → PotPlayer → High Performance

### Power Settings:
- Set Windows to High Performance mode
- Disable GPU power saving in NVIDIA Control Panel
- Keep laptop plugged in for best performance

### What Performance to Expect:
- **1080p 24→60fps:** Smooth, ~40% GPU usage
- **1080p 24→120fps:** Works, ~70% GPU usage  
- **4K 24→60fps:** Possible but ~90% GPU usage
- **Anime (lower complexity):** Can do 144fps easily

## 🚫 COMMON MISTAKES TO AVOID:

1. **DON'T use NumPy 2.0** - Instant breakage
2. **DON'T use VapourSynth R73** - Compatibility issues
3. **DON'T use CUDA 12.x** - Conflicts with PyTorch
4. **DON'T enable AviSynth mode** - Use VapourSynth mode!
5. **DON'T let Windows use AMD iGPU** - Force NVIDIA

## ✨ RESULTS:

Getting smooth frame interpolation on a GTX 1650 Mobile! The key was finding the exact version combination that works. This setup has been stable for weeks with no crashes.

**Virtual Environment Location:** `C:\Users\[username]\vapoursynth_working`

Hope this saves someone else the weeks of troubleshooting I went through. The GTX 1650 Mobile is absolutely capable of real-time frame interpolation with the right setup!

---
*Tested on: ASUS ROG Zephyrus G14 (2020) with similar specs*