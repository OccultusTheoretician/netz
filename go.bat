@echo off
REM ============================================================
REM  go.bat - THE ONE MORNING COMMAND.
REM
REM  Runs everything mechanical, then tells you the 0-3 things
REM  that actually need your judgment. You should not have to
REM  remember any other command.
REM
REM    go            normal morning
REM    go seal       same, and auto-apply drafted failure
REM                  conditions without the review stop
REM
REM  WHY THE REVIEW STOP EXISTS (default, no argument):
REM  failure-condition proposals are mechanical negations, but on
REM  2026-08-01 a new arm shape produced 19 proposals that named a
REM  VENUE where a CONDITION belongs. They would have sealed as
REM  non-empty and unfalsifiable - invisible on the face. The stop
REM  is 30 seconds of reading and it is the thing that caught it.
REM  `go seal` skips it. Use it on days nothing new ingested.
REM ============================================================
setlocal
cd /d C:\netz

echo.
echo ===== 1/5  war desk + collation + forecast =====
call daily.bat

echo.
echo ===== 2/5  failure conditions =====
python fc_pass.py --draft
if /I "%~1"=="seal" (
  python fc_pass.py --apply all
) else (
  echo.
  echo   Drafted. Read FC_REVIEW.md, then:  python fc_pass.py --apply all
  echo   ^(or re-run as `go seal` to skip this stop next time^)
)

echo.
echo ===== 3/5  conformance =====
call conformance.bat

echo.
echo ===== 4/5  surface audit =====
python site_audit.py --section all

echo.
echo ===== 5/5  what needs you =====
python whatnow.py

endlocal
