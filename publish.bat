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
REM KK31-HEALTHPULL: integrate the remote's cron commits (spion, audits,
REM OTS anchors) BEFORE health.py measures surface ages. Four LATE/STALE
REM rows on 2026-08-17 were one defect: health ran against a tree that
REM had not pulled since the prior day, so every remote-dated surface
REM aged at the operator's last pull. The pre-push rebase below still
REM guards the review-pause race; this one guards the measurement.
git pull --rebase --autostash origin main
if errorlevel 1 (
  echo.
  echo  EARLY PULL FAILED - resolve the conflict, then rerun publish.bat.
  echo  Nothing rendered, nothing committed.
  pause
  exit /b 1
)
python health.py
REM KK28-TOOLWORK: navgen in no batch file was the NAVDRIFT root cause — the
REM daily-regenerated report face drifted from the manifest until a hand run.
REM packet_commit --write is the standing BEHIND reflex made permanent (both
REM are no-ops when current). Before add -A so their output rides this publish.
python navgen.py
python packet_commit.py --write
git add -A

REM KK24: the guard was never in the publish path - everything it caught
REM on 2026-08-06 was caught by a hand-run verify. Runs AFTER add -A so
REM newly staged files are inside the scan surface. WARNs pass; FAILs stop.
python desk.py verify
if errorlevel 1 (
  echo.
  echo  VERIFY FAILED - an invariant is broken. NOTHING committed, NOTHING pushed.
  echo  Read the FAIL line above; identity_guard findings are file:line only.
  pause
  exit /b 1
)

for /f "tokens=*" %%i in ('powershell -NoProfile -Command "(Get-Date).ToUniversalTime().ToString('yyyy-MM-dd_HHmm') + 'Z'"') do set STAMP=%%i
git commit -m "publish %STAMP%"

REM KK18: spion[bot] commits on a 6-hour cron, so the remote moves between
REM your runs. Without this rebase the push is rejected and you are left with
REM a local commit and an unpublished site. desk.py ship has always done this;
REM publish.bat did not.
echo.
echo  Rebasing onto the remote (spion may have pushed since your last run)...
git pull --rebase --autostash origin main
if errorlevel 1 (
  echo.
  echo  REBASE FAILED - conflict with the remote. NOTHING PUSHED.
  echo  Your commit is safe locally. Resolve, then: git rebase --continue ^&^& git push
  pause
  exit /b 1
)

git push
if errorlevel 1 (
  echo.
  echo  PUSH REJECTED even after rebase. Nothing lost - retry publish.bat.
  pause
  exit /b 1
)

REM KK31-BEACON: external clock (RPAS 4.05) fires on every publish, after the
REM push, so the posted sha256 and the public ledger.json agree the moment a
REM verifier checks. Non-fatal by design - a beacon outage never gates a
REM publish. Needs BSKY_HANDLE / BSKY_APP_PASSWORD set user-scope (setx).
python syndicate.py
if errorlevel 1 echo  BEACON: syndicate did not post - see the line above. Publish unaffected.

REM Confirm from the remote, not the console.
for /f "tokens=1" %%R in ('git ls-remote origin main') do set REMOTE=%%R
for /f "tokens=1" %%L in ('git rev-parse HEAD') do set LOCAL=%%L
if /I not "%REMOTE%"=="%LOCAL%" (
  echo.
  echo  PUSH DID NOT LAND - remote does not match local HEAD.
  pause
  exit /b 1
)
echo.
echo  Published and confirmed on the remote. Pages updates within ~a minute.
pause
