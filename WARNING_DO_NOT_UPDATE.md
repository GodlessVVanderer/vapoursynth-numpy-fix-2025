# ⚠️ CRITICAL WARNING - DO NOT UPDATE ⚠️

## NEVER UPDATE THESE PACKAGES OR YOUR SETUP WILL BREAK!

### ❌ DO NOT UPDATE:
- **NumPy** - MUST stay at 1.26.4 (NumPy 2.0 BREAKS VapourSynth!)
- **VapourSynth** - MUST stay at R72 (R73+ has compatibility issues)
- **PyTorch** - MUST stay at 2.7.0+cu118 (CUDA 12.x builds cause conflicts)

### ❌ NEVER RUN:
```bash
# THESE COMMANDS WILL BREAK YOUR SETUP:
pip install --upgrade numpy          # THIS WILL INSTALL 2.0 AND BREAK EVERYTHING
pip install --upgrade vapoursynth    # THIS WILL BREAK SVP4 INTEGRATION
pip install -U numpy                 # SAME AS ABOVE - WILL BREAK
pip update                           # WILL UPDATE EVERYTHING AND BREAK IT
```

### ✅ SAFE COMMANDS:
```bash
# Only use exact version installs:
pip install numpy==1.26.4
pip install vapoursynth==72
pip install torch==2.7.0+cu118 --index-url https://download.pytorch.org/whl/cu118
```

## WHY THIS MATTERS:

**NumPy 2.0 fundamentally changed their C API** which VapourSynth relies on. Until VapourSynth updates their bindings (which hasn't happened as of August 2025), NumPy 2.0 will cause:
- `ImportError: numpy.core.multiarray failed to import`
- `VapourSynth has no attribute 'core'`
- Complete failure of frame interpolation

## IF YOU ACCIDENTALLY UPDATE:

1. Uninstall everything:
```bash
pip uninstall numpy vapoursynth torch -y
```

2. Reinstall with correct versions:
```bash
pip install numpy==1.26.4
pip install vapoursynth==72
pip install torch==2.7.0+cu118 --index-url https://download.pytorch.org/whl/cu118
```

## FOR PACKAGE MANAGERS:

If using conda, poetry, or other package managers, PIN the versions:

**requirements.txt:**
```
numpy==1.26.4
vapoursynth==72
torch==2.7.0+cu118
```

**pyproject.toml:**
```toml
[tool.poetry.dependencies]
numpy = "==1.26.4"
vapoursynth = "==72"
torch = {version = "==2.7.0+cu118", source = "pytorch"}
```

## AUTO-UPDATE PROTECTION:

Disable auto-updates in your IDE:
- **VSCode:** Set `"python.terminal.activateEnvironment": false`
- **PyCharm:** Uncheck "Auto-update packages"
- **pip:** Never use `--upgrade` without specifying exact versions

---

# 🛑 REMEMBER: The moment NumPy updates to 2.0, EVERYTHING BREAKS!

This setup works ONLY because we're using NumPy 1.26.4. This is NOT a Python 3.12 issue - it's a NumPy 2.0 incompatibility with VapourSynth's C bindings.