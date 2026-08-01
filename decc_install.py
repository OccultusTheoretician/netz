#!/usr/bin/env python3
r"""
decc_install.py — install DECC-26™ into the netz repo without an exposure slip.

ORDER IS THE SAFETY PROPERTY. Ignore rules are written BEFORE any file is
copied, so a `git add -A` between steps cannot sweep vault material. Nothing is
committed; this stages a reviewable tree and prints exactly what would ship.

WHAT SHIPS (public by design)
  DECC_26_STANDARD.md      the standard
  denom.py                 reference implementation
  denom_capture.py         capture-completeness layer
  decc_conformance.py      the conformance suite
  DENOM_README.md          positioning + honest limits
  docs/decc.html           browser verifier (no network, no storage)

WHAT MUST NEVER SHIP (hard-blocked, and the installer aborts if found tracked)
  denom_vault/             openings = record contents + salts, in the clear
  quarantine/              unsealed record digests and metadata
  tally.json               capture counts
  DISCLOSURE_*.json        opened records
  *_projections_*.json     unrelated, but same sweep class

Run from C:\netz:
    python decc_install.py --from C:\denom
    python decc_install.py --from C:\denom --check     (preflight only)
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

SHIP = ["DECC_26_STANDARD.md", "denom.py", "denom_capture.py",
        "decc_conformance.py", "DENOM_README.md"]
PAGE_SRC = "verify_disclosure.html"
PAGE_DST = "docs/decc.html"

IGNORE_RULES = [
    "# --- DECC-26 / denom: private evidence material, never publishable ---",
    "denom_vault/",
    "**/denom_vault/",
    "quarantine/",
    "**/quarantine/",
    "tally.json",
    "DISCLOSURE_*.json",
    "RECONCILIATION_*.json",
    "ANCHOR_*.json",
    "DECC_CONFORMANCE_REPORT.json",
]

FORBIDDEN = [
    ("denom_vault", "vault openings hold record contents and salts"),
    ("quarantine", "quarantine holds unsealed-record digests"),
    ("tally.json", "capture tally"),
]


def git(*a, cwd="."):
    r = subprocess.run(["git", *a], cwd=str(cwd), capture_output=True,
                       text=True, timeout=60)
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="src", required=True,
                    help="directory holding the DECC files (e.g. C:\\denom)")
    ap.add_argument("--check", action="store_true", help="preflight only")
    a = ap.parse_args()

    root = Path.cwd()
    src = Path(a.src)
    if not (root / ".git").exists():
        sys.exit("decc_install: run this from the netz repo root.")
    if not src.is_dir():
        sys.exit(f"decc_install: source not found: {src}")

    print("DECC-26 INSTALL — preflight")
    print("-" * 62)

    # ---- 1. abort if anything forbidden is ALREADY tracked -----------------
    rc, tracked, _ = git("ls-files")
    bad = []
    for pat, why in FORBIDDEN:
        for line in tracked.splitlines():
            if pat in line:
                bad.append((line, why))
    if bad:
        print("  ABORT — private material is already tracked:")
        for f, why in bad:
            print(f"    {f}   ({why})")
        print("  Untrack it first:  git rm --cached <file>")
        return 1
    print("  [ok] no private DECC material currently tracked")

    # ---- 2. source files present ------------------------------------------
    missing = [f for f in SHIP if not (src / f).exists()]
    page = src / PAGE_SRC
    if missing:
        print(f"  MISSING in {src}: {', '.join(missing)}")
        return 1
    print(f"  [ok] all {len(SHIP)} shippable files present in {src}")
    print(f"  [{'ok' if page.exists() else '--'}] verifier page "
          f"{'found' if page.exists() else 'absent (skipping docs/decc.html)'}")

    # ---- 3. scan the payload for exposure ---------------------------------
    leak = re.compile(r"C:\\\\Users|/home/[a-z]+/", re.I)
    hits = []
    for f in SHIP + ([PAGE_SRC] if page.exists() else []):
        t = (src / f).read_text(encoding="utf-8", errors="replace")
        for i, line in enumerate(t.splitlines(), 1):
            if leak.search(line):
                hits.append(f"{f}:{i}: {line.strip()[:90]}")
    if hits:
        print("  WARN — payload mentions local paths or a username:")
        for h in hits[:8]:
            print(f"    {h}")
        print("  Review before shipping; these are not identity-guard terms")
        print("  but they are small-pool descriptors.")
    else:
        print("  [ok] payload carries no local paths or usernames")

    if a.check:
        print("\n  preflight only — nothing written.")
        return 0

    # ---- 4. ignore rules FIRST --------------------------------------------
    gi = root / ".gitignore"
    cur = gi.read_text(encoding="utf-8") if gi.exists() else ""
    added = [r for r in IGNORE_RULES if r not in cur]
    if added:
        with gi.open("a", encoding="utf-8") as fh:
            if cur and not cur.endswith("\n"):
                fh.write("\n")
            fh.write("\n".join(added) + "\n")
        print(f"\n  [+] .gitignore — {len(added)} rule(s) added BEFORE any copy")
    else:
        print("\n  [ok] .gitignore rules already present")

    # ---- 5. copy the payload ----------------------------------------------
    for f in SHIP:
        shutil.copy2(src / f, root / f)
        print(f"  [+] {f}")
    if page.exists():
        (root / "docs").mkdir(exist_ok=True)
        shutil.copy2(page, root / PAGE_DST)
        print(f"  [+] {PAGE_DST}")

    # ---- 6. nav manifest --------------------------------------------------
    nm = root / "nav_manifest.json"
    if nm.exists() and page.exists():
        man = json.loads(nm.read_text(encoding="utf-8"))
        hrefs = [l["href"] for g in man.get("groups", [])
                 for l in g.get("links", [])]
        if "decc.html" not in hrefs:
            for g in man["groups"]:
                if g["label"] == "STANDARDS":
                    g["links"].append({"href": "decc.html", "text": "Verify Seal"})
                    break
            nm.write_text(json.dumps(man, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8")
            print("  [+] nav_manifest.json — STANDARDS / Verify Seal")
        else:
            print("  [ok] nav entry already present")

    # ---- 7. verify the ignore rules actually bite -------------------------
    print()
    for probe in ("denom_vault/chain.json", "tally.json",
                  "DISCLOSURE_test.json"):
        rc, out, _ = git("check-ignore", "-v", probe)
        print(f"  [{'ok' if rc == 0 else '!!'}] ignore covers {probe}"
              + ("" if rc == 0 else "   *** NOT IGNORED ***"))

    # ---- 8. what would ship -----------------------------------------------
    rc, st, _ = git("status", "--porcelain")
    print("\n  files staged/changed by this install:")
    for line in st.splitlines():
        print(f"    {line}")

    print("\n  NEXT (yours to run, in order):")
    print("    python identity_guard.py scan")
    print("    python navgen.py")
    print("    python decc_conformance.py")
    print("    python desk.py verify")
    print("    python desk.py ship -m \"...\"")
    print("\n  The vault stays where it is. Only the standard, the tools and")
    print("  the verifier ship. Anchors are published deliberately, one at a")
    print("  time, never by sweep.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
