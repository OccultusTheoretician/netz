@echo off
REM lookup.bat - thin wrapper over desk_lookup.py. No logic lives here.
REM
REM   lookup treasury --date 2026-07-29
REM   lookup treasury --from 2026-07-01 --to 2026-07-29 --above 4.80
REM   lookup kev --cve CVE-2026-16812
REM   lookup kev --since 2026-07-27 --verbose
REM   lookup kev --match fastjson,gitlab
REM   lookup quake --from 2026-08-02 --to 2027-01-15 --minmag 4.5 --lat 36.19 --lon -101.19
REM
REM Writes nothing. Resolves nothing. Prints a published value and the query
REM that produced it, so the operator adjudicates against evidence a stranger
REM can re-fetch.
REM
REM Sources are keyless by rule. No API key belongs in this repo - publish.bat
REM runs git add -A, and every source in report_config.json is keyless, which
REM is why that file can sit tracked in public.

if "%~1"=="" goto usage
python "%~dp0desk_lookup.py" %*
goto :eof

:usage
echo.
echo   lookup ^<treasury^|kev^|quake^> [options]
echo.
echo   treasury  US Treasury daily par yield curve, 10-year
echo             --date YYYY-MM-DD ^| --from ^<d^> --to ^<d^> [--above 4.80]
echo             NOTE: posts after the close. A same-day query before ~18:00Z
echo             returns nothing yet. Wait, do not resolve.
echo.
echo   kev       CISA Known Exploited Vulnerabilities catalog
echo             --cve CVE-YYYY-NNNNN ^| --since ^<d^> --until ^<d^> --match a,b
echo             NOTE: dateAdded is what makes a windowed claim resolvable.
echo             Presence in the catalog is not a hit if it predates the window.
echo.
echo   quake     USGS FDSN event query
echo             --from ^<d^> --to ^<d^> --minmag N [--lat --lon --radius]
echo             [--minlat --maxlat --minlon --maxlon]
echo             NOTE: USGS carries no fatality field. A row requiring a death
echo             toll is only partly served here.
echo.
echo   NOT AVAILABLE, and why:
echo     stooq   blocked by a JavaScript bot challenge. Index and oil
echo             settlements have no keyless source - S^&P, Nasdaq, Brent and
echo             WTI rows stay hand-adjudicated.
echo     EFFIS   JavaScript app, not an API.
echo     HHS     JSF page, not machine-queryable.
echo     FRED    needs an API key.
echo.
