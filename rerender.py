#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Re-render every md-backed page under the current netz.py template.
Run from C:\\netz after dropping in a patched netz.py. Then publish.bat."""
import pathlib, shutil
from netz import render_html

reports = sorted(pathlib.Path("reports").glob("battle_report_*.md"))
for md in reports:
    stamp = md.stem.replace("battle_report_", "")
    md.with_suffix(".html").write_text(
        render_html(md.read_text(encoding="utf-8"), f"The Prescient Desk \u2014 Report {stamp}"),
        encoding="utf-8")
print(f"reports re-rendered: {len(reports)}")
if reports:
    shutil.copy(reports[-1].with_suffix(".html"), "reports/latest.html")
    print(f"latest.html <- {reports[-1].stem}")

kkrs = sorted(pathlib.Path("forecasts").glob("KKR_2026-*.md"))
for md in kkrs:
    stamp = md.stem.replace("KKR_", "")
    md.with_suffix(".html").write_text(
        render_html(md.read_text(encoding="utf-8"), f"KKR {stamp}"), encoding="utf-8")
print(f"KKR pages re-rendered: {len(kkrs)}")
if kkrs:
    shutil.copy(kkrs[-1].with_suffix(".html"), "forecasts/KKR_latest.html")
    print(f"KKR_latest.html <- {kkrs[-1].stem}")

led = pathlib.Path("forecasts/LEDGER.md")
if led.exists():
    pathlib.Path("forecasts/ledger.html").write_text(
        render_html(led.read_text(encoding="utf-8"), "KKR Ledger"), encoding="utf-8")
    print("ledger.html re-rendered")
print("done — run publish.bat to review and push")
