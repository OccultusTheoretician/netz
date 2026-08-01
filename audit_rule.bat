@echo off
REM STEP 2 — auditor recommends, YOU rule. Nothing is written without your key.
if not exist C:\netz\audit_verdicts.json (
  echo  audit_verdicts.json not found in C:\netz\ — save the auditor's JSON there first.
  pause
  exit /b
)
set AUD=%~1
if "%AUD%"=="" set AUD=claude
python C:\netz\kkr.py --audit-ingest C:\netz\audit_verdicts.json --auditor %AUD%
pause
