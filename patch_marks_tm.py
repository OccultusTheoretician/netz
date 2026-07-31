#!/usr/bin/env python3
"""
patch_marks_tm.py - novelty-gated trademark pass for the netz repo.
Run from C:\\netz. Python 3.10+. Stdlib only. UTF-8 throughout.

DISCIPLINE (matches the desk's own rules):
  * PROPOSED-first: default mode only REPORTS. Nothing is written without
    --apply, and --apply requires an explicit --files allowlist, because
    docs/*.html are render targets - marking a render that regeneration
    overwrites is exhaust. Find the template string in the generator (.py)
    and mark THAT.
  * First-use-per-file: a mark lands on the first occurrence in each file
    only. Littering every occurrence with (TM) is branding noise, not a claim.
  * Never stages, never commits, never touches .git. Staging is yours,
    named files only.

NOVELTY GATE (searches of 2026-07-30; sweep of KK14 handoff + fresh checks):
  MARKED   - swept, no collisions found:
             Retro-Prescient Audit, VoidSection, Kraehe's Nest, Kraehe's Kalls,
             DECC-26, denom (lowercase tool name - marked in prose refs only)
  REFUSED  - fails novelty or own prior ruling:
             FogSim        (FOGSim, Univ. of Cantabria network simulator
                            2014-2021; imais/fogsim fog simulator; iFogSim
                            family - direct software-class collisions)
             Ohrwurm       (his own IP ruling: descriptive under doctrine of
                            foreign equivalents - do not assert)
             Spion, Konsole (generic German nouns - descriptive)
             KKR           (acronym collision: Kohlberg Kravis Roberts;
                            'Kaos Kontrol Report' full phrase unswept - hold)
  UNSWEPT  - already shipped marked, never swept; counsel-hour item:
             The Prescient Desk

USAGE (mobile-simple)
  python patch_marks_tm.py                       # report: where names live
  python patch_marks_tm.py --apply --sources     # mark first-use in all .py/.md sources
  python patch_marks_tm.py --casing --apply --sources   # fix casing in all sources
  (--files a.py b.py still works for surgical runs; --sources never touches
   .html renders or anything under docs/)
"""
import argparse
import sys
from pathlib import Path

TM = "\u2122"

MARKED = [
    "Retro-Prescient Audit",
    "VoidSection",
    "Kr\u00e4he's Nest",
    "Kr\u00e4he's Kalls",
    "DECC-26",
]
REFUSED = {
    "FogSim": "software-class collision (FOGSim/Cantabria; imais/fogsim; iFogSim)",
    "Ohrwurm": "own ruling: descriptive, doctrine of foreign equivalents",
    "Spion": "generic German noun",
    "Konsole": "generic German noun",
    "KKR": "acronym collision (Kohlberg Kravis Roberts); full phrase unswept",
}
UNSWEPT = ["The Prescient Desk"]

BAD_CASING = "NebelKr\u00e4he"
GOOD_CASING = "Nebelkr\u00e4he"

SCAN_EXT = {".py", ".md", ".html", ".json", ".txt", ".yml", ".yaml"}
SKIP_DIRS = {".git", "node_modules", "__pycache__", "denom_vault", "quarantine"}


def tracked_files(root: Path):
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.suffix.lower() in SCAN_EXT \
                and not any(part in SKIP_DIRS for part in p.parts):
            yield p


def report(root: Path):
    print("MARK PASS REPORT (nothing written)")
    print("-" * 64)
    for name in MARKED:
        already = name + TM
        hits = []
        for p in tracked_files(root):
            try:
                t = p.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            bare = t.count(name) - t.count(already)
            if name in t:
                tag = "GENERATED?" if "docs" in p.parts and p.suffix == ".html" else ""
                hits.append((str(p.relative_to(root)), bare, t.count(already), tag))
        print(f"\n{name}  ->  {name}{TM}")
        if not hits:
            print("  (not found)")
        for rel, bare, marked, tag in hits:
            print(f"  {rel}: {bare} unmarked, {marked} marked  {tag}")
    print("\nREFUSED (do not mark):")
    for k, why in REFUSED.items():
        print(f"  {k}: {why}")
    print("\nUNSWEPT (shipped marked, never cleared - counsel-hour item):")
    for k in UNSWEPT:
        print(f"  {k}")
    print("\nApply with: --apply --files <generator .py / source .md files>")
    print("Marking docs/*.html directly is exhaust if a generator rewrites it.")


def mark_first_use(text: str, name: str) -> tuple[str, bool]:
    already = name + TM
    i = text.find(name)
    if i == -1:
        return text, False
    # if the very first occurrence is already marked, done
    if text[i:i + len(already)] == already:
        return text, False
    return text[:i] + already + text[i + len(name):], True


def source_files(root: Path):
    me = Path(__file__).resolve()
    for p in tracked_files(root):
        if p.suffix.lower() in {".py", ".md"} and "docs" not in p.parts \
                and p.resolve() != me:
            yield p


def apply_marks(root: Path, files):
    changed = 0
    for f in files:
        p = (root / f).resolve() if not isinstance(f, Path) else f
        if not p.exists():
            print(f"SKIP {f}: not found")
            continue
        try:
            t = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        edits = []
        for name in MARKED:
            t2, did = mark_first_use(t, name)
            if did:
                edits.append(name)
                t = t2
        rel = p.relative_to(root) if root in p.parents or p.parent == root else p
        if edits:
            p.write_text(t, encoding="utf-8")
            changed += 1
            print(f"MARKED {rel}: " + ", ".join(edits))
        else:
            print(f"NO-OP  {rel}: nothing unmarked at first use")
    print(f"\n{changed} file(s) written. Stage named files yourself; "
          f"regenerate renders; verify before ship.")


def casing(root: Path, do_apply: bool, files, sources=False):
    allow = None
    if sources:
        allow = {p.resolve() for p in source_files(root)}
    elif files:
        allow = {(root / f).resolve() for f in files}
    total = 0
    for p in tracked_files(root):
        if allow is not None and p.resolve() not in allow:
            continue
        try:
            t = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        n = t.count(BAD_CASING)
        if not n:
            continue
        total += n
        if do_apply and allow is not None:
            p.write_text(t.replace(BAD_CASING, GOOD_CASING), encoding="utf-8")
            print(f"FIXED {p.relative_to(root)}: {n} occurrence(s)")
        else:
            print(f"{p.relative_to(root)}: {n} x {BAD_CASING}")
    if not do_apply:
        print(f"\n{total} total. Fix sources with: --casing --apply --sources")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--files", nargs="+", default=[])
    ap.add_argument("--sources", action="store_true",
                    help="target all .py/.md sources (never docs/, never .html)")
    ap.add_argument("--casing", action="store_true")
    ap.add_argument("--root", default=".")
    a = ap.parse_args()
    root = Path(a.root).resolve()
    if a.casing:
        if a.apply and not (a.files or a.sources):
            sys.exit("refusing: --apply needs --sources or --files")
        casing(root, a.apply, a.files, a.sources)
        return
    if a.apply:
        if not (a.files or a.sources):
            sys.exit("refusing: --apply needs --sources or --files")
        targets = list(source_files(root)) if a.sources else a.files
        apply_marks(root, targets)
        return
    report(root)


if __name__ == "__main__":
    main()
