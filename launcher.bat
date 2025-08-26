@echo off
echo Starting SVP4 + PotPlayer...
start "" "C:\Program Files (x86)\SVP 4\SVPManager.exe"
timeout /t 5 /nobreak >nul
taskkill /f /im PotPlayerMini64.exe 2>nul
timeout /t 2 /nobreak >nul
start "" "C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe"
echo.
echo ✅ SVP4 + PotPlayer launched!
echo.
echo Remember: F5 → Video → VapourSynth → Enable
echo.
pause