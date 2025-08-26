@echo off
echo Simple VapourSynth + SVP4 Installer
echo ====================================
echo.
echo This will install the EXACT working versions:
echo - NumPy 1.26.4 (NOT 2.0!)
echo - PyTorch with CUDA 11.8
echo - VapourSynth
echo.
pause

echo.
echo Uninstalling old versions...
pip uninstall -y numpy vapoursynth torch torchvision torchaudio

echo.
echo Installing NumPy 1.26.4...
pip install numpy==1.26.4

echo.
echo Installing PyTorch with CUDA 11.8...
pip install torch==2.7.0+cu118 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

echo.
echo Installing VapourSynth...
pip install vapoursynth

echo.
echo ====================================
echo DONE! Now configure PotPlayer:
echo 1. Press F5
echo 2. Go to Video tab
echo 3. Select VapourSynth (NOT AviSynth!)
echo 4. Enable VapourSynth
echo ====================================
echo.
pause