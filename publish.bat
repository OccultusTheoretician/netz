@echo off
REM KKR publish gate — review, then commit + push. Ctrl+C at the pause aborts.
start "" C:\netz\reports\latest.html
if exist C:\netz\forecasts\KKR_latest.html start "" C:\netz\forecasts\KKR_latest.html
echo.
echo  Review both reports in the browser.
echo  Ctrl+C to ABORT publication. Any other key publishes.
echo.
pause
if not exist C:\netz\docs mkdir C:\netz\docs
copy /Y C:\netz\reports\latest.html C:\netz\docs\report.html >nul
if exist C:\netz\forecasts\ledger.html copy /Y C:\netz\forecasts\ledger.html C:\netz\docs\ledger.html >nul
if exist C:\netz\forecasts\KKR_latest.html copy /Y C:\netz\forecasts\KKR_latest.html C:\netz\docs\kkr.html >nul
copy /Y C:\netz\ledger.json C:\netz\docs\ledger.json >nul
cd /d C:\netz
git add -A
for /f "tokens=*" %%i in ('powershell -NoProfile -Command "(Get-Date).ToUniversalTime().ToString('yyyy-MM-dd_HHmm') + 'Z'"') do set STAMP=%%i
git commit -m "publish %STAMP%"
git push
echo.
echo  Published. Pages updates within ~a minute.
pause
