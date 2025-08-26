# VapourSynth + SVP4 Working Setup (2025)

## The NumPy 2.0 Problem SOLVED

**THE ISSUE:** NumPy 2.0 breaks VapourSynth Python bindings. It's NOT a Python 3.12 problem!

## One-Click Installer

1. Download `install.bat`
2. Right-click → Run as Administrator
3. Follow the prompts
4. Done!

## Manual Install (if needed)

```bash
pip install numpy==1.26.4
pip install torch==2.7.0+cu118 --index-url https://download.pytorch.org/whl/cu118
pip install vapoursynth
```

## Working Configuration

| Component | Version | Critical |
|-----------|---------|----------|
| Python | 3.12.8 | ✅ Works |
| NumPy | 1.26.4 | ⚠️ NOT 2.0 |
| PyTorch | 2.7.0+cu118 | CUDA 11.8 |
| VapourSynth | R72 | Stable |

## PotPlayer Setup

1. Start SVP4 Manager
2. Open PotPlayer
3. Press F5 → Video → **VapourSynth** (NOT AviSynth!)
4. Enable VapourSynth
5. Play video - SVP4 should show "Active"

## Performance (GTX 1650 Mobile)

- 1080p → 60fps: 40% GPU
- 1080p → 120fps: 70% GPU
- 4K → 60fps: 90% GPU
- Anime → 144fps: 60% GPU

## Laptop GPU Fix

Force NVIDIA GPU:
- Windows Settings → Graphics → PotPlayer → High Performance
- NVIDIA Control Panel → PotPlayer → NVIDIA GPU

## Troubleshooting

Run the version checker:
```bash
python check_versions.py
```

Should show:
- NumPy 1.26.4 ✅
- CUDA Available ✅
- VapourSynth R72 ✅

## Downloads

- [Python 3.12](https://python.org)
- [SVP4](https://www.svp-team.com)
- [PotPlayer](https://potplayer.daum.net)
- [VapourSynth R72](https://github.com/vapoursynth/vapoursynth/releases)