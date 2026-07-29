@echo off
call lms server start

REM war desk: must run AFTER lms server start and BEFORE netz.py
python C:\netz\tg_fetch.py
python C:\netz\tg_translate.py --latest
python C:\netz\tg_cluster.py --latest
python C:\netz\tg_grade.py --latest

python C:\netz\netz.py
python C:\netz\kkr.py
