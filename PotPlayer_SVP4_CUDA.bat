@echo off
echo Starting SVP4 + PotPlayer with CUDA Support
echo ==========================================

rem Set environment for CUDA compatibility
set CUDA_VISIBLE_DEVICES=0
set AVISYNTH_MT_MODE=5

echo Starting SVP4 Manager...
start "" "C:\Program Files (x86)\SVP 4\SVPManager.exe"

rem Wait for SVP4 to initialize
timeout /t 5 /nobreak >nul

echo Killing any existing PotPlayer instances...
taskkill /f /im PotPlayerMini64.exe 2>nul

rem Wait for cleanup
timeout /t 2 /nobreak >nul

echo Starting PotPlayer with SVP4 + CUDA support...
start "" "C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe"

echo.
echo 🎬 SVP4 + PotPlayer launched with CUDA compatibility!
echo.
echo Configuration:
echo 1. SVP4 should auto-detect PotPlayer
echo 2. Frame interpolation will use GPU acceleration
echo 3. AV1 hardware decoding remains active
echo 4. Check SVP4 tray icon for status