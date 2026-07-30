@echo off
REM ============================================================
REM  run_dialektik_calibration.bat - close the calibration loop
REM  in one action.
REM
REM  1. writes the five scored dyad files
REM  2. records each into dialektik_calibration.json
REM  3. runs the gate check and prints the verdict
REM
REM  Nothing here ships. The ledger is untouched. Re-runnable:
REM  re-recording a case overwrites its index, it does not stack.
REM ============================================================
setlocal
cd /d "%~dp0"

echo.
echo ============================================================
echo   STEP 1 of 3 - writing the scored calibration dyads
echo ============================================================
python build_dialektik_calibration.py
if errorlevel 1 goto :failed

echo.
echo ============================================================
echo   STEP 2 of 3 - recording each case into the calibration file
echo ============================================================
python dialektik.py record --dyad cal_germany_ussr.json    --case "Germany-USSR 1941-45"
if errorlevel 1 goto :failed
python dialektik.py record --dyad cal_iran_iraq.json       --case "Iran-Iraq 1980-88"
if errorlevel 1 goto :failed
python dialektik.py record --dyad cal_india_pakistan.json  --case "India-Pakistan Line of Control, standing"
if errorlevel 1 goto :failed
python dialektik.py record --dyad cal_koreas.json          --case "Koreas, armistice standing"
if errorlevel 1 goto :failed
python dialektik.py record --dyad cal_airline_options.json --case "Pre-9/11 airline options, September 2001"
if errorlevel 1 goto :failed

echo.
echo ============================================================
echo   STEP 3 of 3 - the gate
echo ============================================================
python dialektik.py check

echo.
echo ------------------------------------------------------------
echo   PASS  = the instrument separates cases everyone agrees on.
echo           It is usable on live dyads.
echo   FAIL  = the honest result is a published null. That is a
echo           finding, not a breakage - do not tune scores to
echo           make it pass.
echo ------------------------------------------------------------
echo.
echo   Nothing has shipped. Review, then ship when you choose.
echo.
goto :end

:failed
echo.
echo   STOPPED - a step returned an error. Nothing further ran.
echo   The calibration file is unchanged past the last good record.
echo.

:end
pause
