@echo off
REM LANE 2 STEP 1 — fresh NETZ run, then write the Fable packet only (no Qwen forecast).
python C:\netz\netz.py
python C:\netz\kkr.py --packet-only
echo.
echo  ============================================================
echo   PACKET READY. Upload the newest file from:
echo       C:\netz\forecasts\kkr_packet_[today].md
echo   into your Claude project, then say: "run the projections"
echo  ============================================================
echo.
start "" C:\netz\forecasts
pause
