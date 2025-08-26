@echo off
title VapourSynth + SVP4 Automated Installer
color 0A

echo ============================================
echo    VapourSynth + SVP4 Automated Installer
echo    For GTX 1650 Mobile and Similar GPUs
echo ============================================
echo.

:: Check for admin rights
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo This installer needs to run as Administrator.
    echo Right-click and select "Run as administrator"
    pause
    exit /b 1
)

echo [1/6] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python not found. Please install Python 3.12.x first
    echo Download from: https://python.org
    pause
    exit /b 1
)

echo [2/6] Creating backup of current packages...
pip freeze > backup_packages_%date:~-4,4%%date:~-10,2%%date:~-7,2%.txt 2>nul

echo [3/6] Uninstalling conflicting packages...
pip uninstall -y numpy vapoursynth torch torchvision torchaudio 2>nul

echo [4/6] Installing EXACT working versions...
echo Installing NumPy 1.26.4 (NOT 2.0!)...
pip install numpy==1.26.4
if %errorlevel% neq 0 (
    echo ERROR: Failed to install NumPy 1.26.4
    pause
    exit /b 1
)

echo [5/6] Installing PyTorch with CUDA 11.8...
pip install torch==2.7.0+cu118 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
if %errorlevel% neq 0 (
    echo ERROR: Failed to install PyTorch
    pause
    exit /b 1
)

echo [6/6] Installing VapourSynth...
pip install vapoursynth
if %errorlevel% neq 0 (
    echo ERROR: Failed to install VapourSynth
    pause
    exit /b 1
)

echo.
echo ============================================
echo    Creating Launcher and Config Files
echo ============================================
echo.

:: Create PotPlayer launcher
echo @echo off > "%USERPROFILE%\Desktop\Launch_SVP4_PotPlayer.bat"
echo echo Starting SVP4 + PotPlayer... >> "%USERPROFILE%\Desktop\Launch_SVP4_PotPlayer.bat"
echo start "" "C:\Program Files (x86)\SVP 4\SVPManager.exe" >> "%USERPROFILE%\Desktop\Launch_SVP4_PotPlayer.bat"
echo timeout /t 5 /nobreak ^>nul >> "%USERPROFILE%\Desktop\Launch_SVP4_PotPlayer.bat"
echo taskkill /f /im PotPlayerMini64.exe 2^>nul >> "%USERPROFILE%\Desktop\Launch_SVP4_PotPlayer.bat"
echo timeout /t 2 /nobreak ^>nul >> "%USERPROFILE%\Desktop\Launch_SVP4_PotPlayer.bat"
echo start "" "C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe" >> "%USERPROFILE%\Desktop\Launch_SVP4_PotPlayer.bat"

:: Create version checker
echo Creating version checker...
(
echo import sys, numpy, torch, vapoursynth
echo print(f"Python: {sys.version}"^)
echo print(f"NumPy: {numpy.__version__}"^)
echo print(f"PyTorch: {torch.__version__}"^)
echo print(f"CUDA Available: {torch.cuda.is_available()}"^)
echo print(f"VapourSynth: {vapoursynth.core.version()}"^)
echo if numpy.__version__.startswith("2."^):
echo     print("ERROR: NumPy 2.0 detected! This will break VapourSynth!"^)
echo else:
echo     print("SUCCESS: All versions correct!"^)
) > "%USERPROFILE%\Desktop\check_versions.py"

echo.
echo ============================================
echo          INSTALLATION COMPLETE!
echo ============================================
echo.
echo IMPORTANT SETUP STEPS:
echo.
echo 1. Launch file created on Desktop: Launch_SVP4_PotPlayer.bat
echo.
echo 2. In PotPlayer, press F5 and configure:
echo    - Go to Video tab
echo    - Select VapourSynth (NOT AviSynth!)
echo    - Check "Enable VapourSynth"
echo.
echo 3. For laptop users with dual GPU:
echo    - Windows Settings - Graphics
echo    - Add PotPlayer - High Performance
echo    - NVIDIA Control Panel - Set PotPlayer to use NVIDIA
echo.
echo 4. Test your setup:
echo    - Run check_versions.py on Desktop
echo    - Should show "SUCCESS: All versions correct!"
echo.
echo Your installed versions:
python -c "import numpy; print(f'NumPy: {numpy.__version__}')"
python -c "import torch; print(f'PyTorch: {torch.__version__}')"
python -c "import vapoursynth; print(f'VapourSynth: {vapoursynth.core.version()}')"
echo.
pause