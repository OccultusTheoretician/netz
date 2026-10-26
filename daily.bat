@echo off
REM KK26 latch: one desk run per local day, whoever fires first.
for /f %%d in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd"') do set NETZ_TODAY=%%d
if not exist C:\netz\state mkdir C:\netz\state
if exist C:\netz\state\desk_%NETZ_TODAY%.ran (
  echo daily: desk already ran %NETZ_TODAY% — skipping war desk/collation/forecast.
  exit /b 0
)
echo ran>C:\netz\state\desk_%NETZ_TODAY%.ran
call lms server start

REM war desk: must run AFTER lms server start and BEFORE netz.py
python C:\netz\tg_fetch.py
python C:\netz\tg_translate.py --latest
python C:\netz\tg_cluster.py --latest
python C:\netz\tg_grade.py --latest

python C:\netz\netz.py
REM RETIRE-1026: lmstudio/auto and lmstudio/realist retired 2026-10-26 (registration
REM 16.10). The desk run writes the packet and kkr_packet_latest.md only; the local
REM arms fire from local_arms.py after this file. The input side above stays on the
REM model arms.json registers for lmstudio/auto (INPUTBIND-1004, 16.9).
python C:\netz\kkr.py --packet-only
