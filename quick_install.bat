@echo off
echo ============================================
echo VapourSynth + SVP4 Quick Install
echo Fixing NumPy 2.0 Compatibility Issues
echo ============================================
echo.
echo Installing the WORKING versions...
echo.

echo Installing NumPy 1.26.4 (NOT 2.0!)...
pip install numpy==1.26.4

echo.
echo Installing PyTorch with CUDA 11.8...
pip install torch==2.7.0+cu118 --index-url https://download.pytorch.org/whl/cu118

echo.
echo Installing VapourSynth R72...
pip install vapoursynth

echo.
echo ============================================
echo Installation Complete!
echo ============================================
echo.
echo Next steps:
echo 1. Start SVP4 Manager
echo 2. Open PotPlayer
echo 3. Press F5 - Video - VapourSynth - Enable
echo 4. Play any video!
echo.
echo Remember: Use VapourSynth mode, NOT AviSynth!
echo.
pause
