@echo off
REM Forecast-only: run the model against the EXISTING latest report.
REM No refetch, no collation - use when LM was off during the daily run.
python C:\netz\kkr.py
start "" C:\netz\forecasts\KKR_latest.html
pause
