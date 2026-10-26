@echo off
REM Forecast-only: run the model against the EXISTING latest report.
REM No refetch, no collation - use when LM was off during the daily run.
REM RETIRE-1026: lmstudio/auto retired 2026-10-26. The fallback fires the registered
REM local arms against the existing report instead, one model at a time. Use it only
REM when the chain's local arms did not fire today.
setlocal
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
python C:\netz\local_arms.py
start "" C:\netz\forecasts\KKR_latest.html
pause
