@echo off
REM LANE 2 STEP 2 — ingest the JSON Claude returned (saved as fable_projections.json).
if not exist C:\netz\fable_projections.json (
  echo  fable_projections.json not found in C:\netz\
  echo  Save Claude's JSON block to that filename first, then rerun.
  pause
  exit /b
)
python C:\netz\kkr.py --ingest C:\netz\fable_projections.json
start "" C:\netz\forecasts\KKR_latest.html
echo.
echo  Ingested and scored under the manual/fable lane.
echo  Review KKR_latest.html, then publish.bat when ready.
pause
