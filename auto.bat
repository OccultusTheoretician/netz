@echo off
:: KK30-LMS-PREFLIGHT - raise the inference engine before the chain assumes it
call lms server start >nul 2>&1
set LMSTRIES=0
:lmswait
curl -s -o NUL http://127.0.0.1:1234/v1/models && goto lmsready
set /a LMSTRIES+=1
if %LMSTRIES% GEQ 30 (
  echo [preflight] LM Studio server not answering on 1234 after ~60s - elicitation will fail loud
  goto lmsdone
)
ping -n 3 127.0.0.1 >nul
goto lmswait
:lmsready
lms ps 2>nul | findstr /C:"qwen/qwen3-30b-a3b-2507" >nul || call lms load qwen/qwen3-30b-a3b-2507 -y
:lmsdone
:: end KK30-LMS-PREFLIGHT
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
REM FRAMEARM-2026-09-03: second local arm - same model, same rubric, a hashed
REM realist frame preamble; own packet; rows carry frame/frame_hash. LM Studio
REM down = packet written, ledger unchanged, printed. Fail-open under :run.
call :run "frame arm realist (local)"  python kkr.py --provider lmstudio --frame realist
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
REM KFKSWEEP-2026-09-02: the claim-decay face is a function of the board and
REM today's date; it regenerates here nightly so it can never again be the
REM stalest tile on its own site. validate is the structural and provenance
REM audit, printed, fail-open. Neither line moves the board's own as_of: that
REM moves only on applied observations (add, link, enrich --apply, promote),
REM and the weekly "KFK data" row keeps grading that commitment honestly.
call :run "kfk validate"               python KriegForeKaster.py validate
call :run "kfk freshness face"         python KriegForeKaster.py freshness
call :run "dialektik meter"            python dialektik_meter.py --run
call :run "kfk enrich (batch 15)"      python kfk_enrich.py --batch --limit 15
call :run "archiv fetch (resume)"      python archiv.py fetch --vault D:\vault
call :run "failure-condition drafts"   python fc_pass.py --draft
call :run "adjudicator proposals"      python mechanical_adjudicator.py --due --keep-raw
call :run "conformance"                call conformance.bat
call :run "surface audit"              python site_audit.py --section all
REM KK27F-WIRE: the two audit instruments run nightly, ahead of
REM the health board so their outputs exist when health grades
REM them. Urteil first - it reads jury files the adjudicator
REM stages may have written earlier in this same chain.
REM KK27H-FOGLIVE: the Warte was the last instrument serving a
REM live page by hand only. A page that freezes when someone
REM forgets is not an instrument.
REM KK27J-STALE: the register recomputes from a live verifier run
REM instead of being typed; the spine restates its real
REM source-field age instead of its file date.
call :run "conformance register"       python register_build.py
call :run "spine freshness census"     python spine_stamp.py
call :run "calibration observatory"    python warte.py
call :run "verdict grounding"          python urteil.py
call :run "completeness audit"         python luecke.py
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
