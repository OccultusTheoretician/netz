@echo off
REM ============================================================
REM  ingest.bat - manual-lane ingest, arm-aware.
REM  Replaces fable_ingest.bat, which hardcoded fable_projections.json
REM  and passed no --arm, so every manual lane landed as manual/fable.
REM  That is DEFECT D, fixed in kkr.py in KK9 and reintroduced by the wrapper.
REM
REM  Usage:
REM     ingest.bat <projections.json> <arm-tag>
REM  Example:
REM     ingest.bat opus5_projections_2026-07-27.json manual/opus-5
REM ============================================================
setlocal

if "%~1"=="" goto :usage
if "%~2"=="" goto :usage
if not exist "%~1" (
  echo ingest: file not found: %~1
  echo         downloads do not always arrive - check Downloads before re-deriving.
  exit /b 1
)

REM resolve the packet this arm forecast against, for --packet provenance
set "PACKET="
for /f "delims=" %%P in ('dir /b /o-d "%~dp0forecasts\kkr_packet_2026-*.md" 2^>nul') do (
  if not defined PACKET set "PACKET=%%P"
)
if not defined PACKET (
  for /f "delims=" %%P in ('dir /b /o-d "%~dp0kkr_packet_2026-*.md" 2^>nul') do (
    if not defined PACKET set "PACKET=%%P"
  )
)
if not defined PACKET (
  echo ingest: no dated kkr_packet found. Pass provenance by hand:
  echo         python kkr.py --ingest "%~1" --arm %~2 --packet ^<packet-name^>
  exit /b 1
)

echo ingest: file   %~1
echo ingest: arm    %~2
echo ingest: packet %PACKET%
echo.

python "%~dp0kkr.py" --ingest "%~1" --arm %~2 --packet "%PACKET%"
if errorlevel 1 (
  echo.
  echo ingest: kkr.py returned an error - nothing was published. Ledger unchanged.
  exit /b 1
)

echo.
echo ingest: per-arm counts now --
python -c "import json;from collections import Counter;print(Counter(p.get('model','(none)') for p in json.load(open(r'%~dp0ledger.json'))['projections']))"
echo.
echo ingest: review KKR_latest.html, then run: python desk.py ship
exit /b 0

:usage
echo.
echo   usage: ingest.bat ^<projections.json^> ^<arm-tag^>
echo.
echo   arm tags in use:
echo      manual/opus-5      frontier model, operator-elicited, retrieval off
echo      manual/fable-5     frontier model, operator-elicited, retrieval off
echo      manual/sonnet-5    frontier model, operator-elicited, retrieval off
echo      operator/human     his own calls
echo.
echo   a Brier belongs to one forecaster. Do not reuse a tag across models.
echo.
exit /b 2
