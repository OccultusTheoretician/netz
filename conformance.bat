@echo off
REM conformance.bat - regen RPAS report on ledger change, sync served copies, stage for the publish gate.
cd /d C:\netz
set FORCE=0
if "%1"=="--force" set FORCE=1
for /f %%H in ('certutil -hashfile ledger.json SHA256 ^| findstr /r "^[0-9a-f]"') do set CUR=%%H
set LAST=
if exist .conformance_last set /p LAST=<.conformance_last
if "%CUR%"=="%LAST%" if "%FORCE%"=="0" ( echo conformance: ledger unchanged ^& goto sync )
python rpas_audit.py --ledger ledger.json --report REPORT_conformance.md
if errorlevel 1 ( echo conformance: AUDIT FAILED ^& exit /b 1 )
REM Stranger's verdicts, published as JSON for conformance.html to render.
REM No errorlevel gate: a NONCONFORMANT verdict publishes like any other finding.
python rpas_verify.py ledger.json --json > docs\rpas_verdict.json
python knp_verify.py docs\kalls_hashlog.json --json > docs\knp_verdict.json
echo %CUR%>.conformance_last
:sync
copy /Y REPORT_conformance.md docs\ >nul
copy /Y RPAS_FIRST_EDITION_2026_v1.md docs\ >nul
copy /Y LIAS_FIRST_EDITION_2026_v1.md docs\ >nul
copy /Y STANDARDS_MAPPING_RPA_2026-07-24.md docs\ >nul
git add docs\REPORT_conformance.md docs\RPAS_FIRST_EDITION_2026_v1.md docs\LIAS_FIRST_EDITION_2026_v1.md docs\STANDARDS_MAPPING_RPA_2026-07-24.md REPORT_conformance.md 2>nul
echo conformance: current, synced, staged
