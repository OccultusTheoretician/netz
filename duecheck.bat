@echo off
REM duecheck.bat - show what is due, then run the lookups that can serve it.
REM
REM DELIBERATELY NOT AN AUTO-RESOLVER.
REM
REM It prints the queue and then prints the published values for the three
REM classes a keyless source can serve. It does not match rows to values, does
REM not propose verdicts, and does not touch the ledger. Resolution stays a
REM `python kkr.py --resolve` decision made by a human reading both outputs.
REM
REM The reason is not caution for its own sake. Of eight probed endpoints, two
REM returned HTML shells that a lazy content check scored as passing, one
REM returns real data for the wrong instrument, and one is behind a bot
REM challenge. A chain that wrote verdicts automatically would have put four
REM wrong resolutions on a permanent record before anyone noticed.
REM
REM   duecheck            the queue plus a 30-day window on each source
REM   duecheck 4.80       same, flagging 10-year closes above 4.80
REM
REM Run from C:\netz.

setlocal
set THRESH=%~1
if "%THRESH%"=="" set THRESH=4.80

echo.
echo ================================================================
echo   THE DUE QUEUE
echo ================================================================
python "%~dp0desk.py" due

echo.
echo ================================================================
echo   TREASURY - 10-year par yield, last 30 days
echo   serves the 10-year rows. Posts after the close.
echo ================================================================
for /f %%d in ('powershell -NoProfile -Command "(Get-Date).AddDays(-30).ToString('yyyy-MM-dd')"') do set FROM=%%d
for /f %%d in ('powershell -NoProfile -Command "(Get-Date).ToString('yyyy-MM-dd')"') do set TO=%%d
python "%~dp0desk_lookup.py" treasury --from %FROM% --to %TO% --above %THRESH%

echo.
echo ================================================================
echo   CISA KEV - additions in the last 30 days
echo   serves the "CISA adds X to KEV" rows. Check dateAdded against
echo   the row's window: presence alone is not a hit.
echo ================================================================
python "%~dp0desk_lookup.py" kev --since %FROM%

echo.
echo ================================================================
echo   USGS - M4.5+ worldwide, last 30 days
echo   narrow with --lat/--lon/--radius or a bbox per row.
echo   No fatality field: death-toll clauses need a separate source.
echo ================================================================
python "%~dp0desk_lookup.py" quake --from %FROM% --to %TO% --minmag 4.5

echo.
echo ================================================================
echo   NOT COVERED - hand-adjudicate these
echo     index and oil settlements  stooq is bot-challenged
echo     hectares burned            EFFIS is a JavaScript app
echo     HHS breach portal          JSF page, not queryable
echo     FOMC target upper bound    NY Fed serves EFFR, the realised
echo                                rate, which is a different number
echo ================================================================
echo.
echo   Nothing above resolved anything. To resolve:
echo     python kkr.py --resolve      (no flags, never --all)
echo.
endlocal
