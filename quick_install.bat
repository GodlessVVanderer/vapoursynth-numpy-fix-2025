@echo off
echo VapourSynth Quick Install - Correct Versions
echo ============================================
echo.
echo Installing NumPy 1.26.4 (NOT 2.0!)
pip install numpy==1.26.4
echo.
echo Installing PyTorch with CUDA 11.8
pip install torch==2.7.0+cu118 --index-url https://download.pytorch.org/whl/cu118
echo.
echo Installing VapourSynth R72
pip install vapoursynth==72
echo.
echo Installation complete!
echo.
echo REMEMBER: NEVER run 'pip install --upgrade' on these packages!
pause
