@echo off
REM seal.bat - one sealed entry, end to end: veil entry -> conformance -> commit -> push -> external clock.
cd /d C:\netz
python candidate_desk.py --new --ledger ledger.json
if errorlevel 1 ( echo seal: entry NOT sealed ^& pause ^& exit /b 1 )
call conformance.bat --force
git add ledger.json
git commit -m "ledger: entry sealed under RPAS-26"
git push
echo.
echo  EXTERNAL CLOCK (RPAS 4.05): run syndicate.bat to post the seal hash to Bluesky.
pause
