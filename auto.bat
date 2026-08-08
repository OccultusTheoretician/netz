@echo off
REM ============================================================
REM  auto.bat - THE UNATTENDED MORNING (KK26).
REM
REM  What the 9:00 task runs. Everything mechanical; nothing that
REM  needs the operator. Judgment stays manual by design:
REM    fc_pass --apply        (the review stop caught the 19-row class)
REM    kkr.py --resolve       (adjudication is signed by the operator)
REM    kkr.py --mine          (the operator/human arm)
REM    ohrwurm_call.py        (a sealed forecast is a projection)
REM    kfk_promote / kfk_walk --apply
REM    publish.bat            (until the CVE-token guard ships)
REM
REM  COLLISION: daily.bat owns the latch (state\desk_<date>.ran).
REM  If the operator ran `go` first, stage 1 here no-ops; if this
REM  ran first, `go` skips the war desk and continues at stage 2.
REM  Every stage is fail-open: a failure is logged to the morning
REM  file and the chain continues. A missed stage prints as missed.
REM ============================================================
setlocal enabledelayedexpansion
cd /d C:\netz
REM KK28D-UTF8: under the scheduler there is no console and Python 3.14
REM defaults redirected stdout to cp1252 — a Cyrillic phrase or em-dash
REM mid-print killed ohrwurm_candidates live (2026-08-07). UTF-8 for every
REM child Python; the stage logs and MORNING file become clean UTF-8 too.
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
for /f %%d in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd"') do set TODAY=%%d
if not exist state mkdir state
if not exist state\log_%TODAY% mkdir state\log_%TODAY%
set MORNING=state\MORNING_%TODAY%.md
echo # MORNING %TODAY% — unattended run>%MORNING%
echo.>>%MORNING%

REM KK28B-AUTOLATCH: the latch is daily.bat's, stage-scoped. The old
REM whole-run exit here skipped the entire mechanical tail on every
REM operator-first day (proven live 2026-08-07: MORNING file, one line,
REM nothing ran). Stage 1 no-ops inside daily.bat; the chain continues.
if exist state\desk_%TODAY%.ran (
  echo latch: desk_%TODAY%.ran present — stage 1 will no-op inside daily.bat; chain continues.>>%MORNING%
)

call :run "war-desk + collation + forecast (daily.bat)" call daily.bat
call :run "ohrwurm propagation"        python ohrwurm.py --latest
call :run "ohrwurm velocity"           python ohrwurm_velocity.py --latest
call :run "ohrwurm event-phrase join"  python ohrwurm_link.py --latest
call :run "ohrwurm register append"    python ohrwurm_log.py
call :run "dialektik feed iran"        python dialektik_feed.py --zone iran
call :run "dialektik feed ru-ua"       python dialektik_feed.py --zone russia_ukraine
REM KK33-PIPELINE: the three formerly-manual instruments, now nightly. All
REM fail-open per stage, print INDETERMINATE on a bad read, touch no sealed row.
call :run "kfk sightings"              python kfk_sightings.py
call :run "kfk overlay"                python kfk_map.py
call :run "dialektik meter"            python dialektik_meter.py --run
call :run "kfk enrich (batch 15)"      python kfk_enrich.py --batch --limit 15
call :run "archiv fetch (resume)"      python archiv.py fetch --vault D:\vault
call :run "failure-condition drafts"   python fc_pass.py --draft
call :run "adjudicator proposals"      python mechanical_adjudicator.py --due --keep-raw
call :run "conformance"                call conformance.bat
call :run "surface audit"              python site_audit.py --section all
call :run "health board"               python health.py

echo.>>%MORNING%
echo ## Ohrwurm crossing candidates (calls are yours to fire)>>%MORNING%
python ohrwurm_candidates.py >> %MORNING% 2>&1

echo.>>%MORNING%
echo ## What needs you>>%MORNING%
python whatnow.py >> %MORNING% 2>&1

echo.
echo ===== unattended run complete — read %MORNING% =====
type %MORNING%
exit /b 0

:run
set LABEL=%~1
set STAGELOG=state\log_%TODAY%\%LABEL: =_%.log
shift
set CMD=%1
:build
shift
if "%~1"=="" goto exec
set CMD=%CMD% %1
goto build
:exec
%CMD% > "%STAGELOG%" 2>&1
REM KK28C-RUNLABELS: parse-time %%LABEL%% inside these blocks broke on the
REM three paren-bearing stage labels the first time the chain ever ran.
REM Delayed expansion (!VAR!) expands after the block is parsed.
if errorlevel 1 (
  echo [FAIL] !LABEL!  — see !STAGELOG!>>%MORNING%
  echo [FAIL] !LABEL!
) else (
  echo [OK]   !LABEL!>>%MORNING%
  echo [OK]   !LABEL!
)
exit /b 0
