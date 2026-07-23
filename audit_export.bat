@echo off
REM STEP 1 — export past-deadline projections for independent audit.
python C:\netz\kkr.py --audit-export
echo.
echo  Give forecasts\audit_packet_[date].md to your auditor (Claude, Qwen, or other).
echo  Save their JSON reply as C:\netz\audit_verdicts.json, then run audit_rule.bat
start "" C:\netz\forecasts
pause
