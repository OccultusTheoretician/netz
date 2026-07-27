#!/usr/bin/env python3
"""
patch_spion_page.py — two corrections to docs/spion.html.

ONE — it is a dead end. The page has no navigation at all: every href on it is
either an in-page anchor, a data file, or generated at runtime. A reader who
arrives from a link has no way back to anything. (kraehes_kalls.html is fine;
an earlier audit of mine called it a dead end by grepping for index.html and
missing that it links root-relative. Correction noted here rather than quietly.)

TWO — it asserts something untrue about its own custody. The page says the watch
"commits under a machine identity. That is deliberate." The workflow sets
user.email to spion@users.noreply.github.com, which is the legacy GitHub noreply
form and resolves to a real third party's account. Until that line in
.github/workflows/spion.yml changes, every observation commit is attributed to
someone with no connection to this desk. On the page whose entire argument is
that a monitoring record kept on the operator's own machine is worth only his
word, a false sentence about custody is the worst one to leave standing.

This patch tells the truth about the current state and leaves a marker so the
sentence can be restored in full once the workflow is fixed.

  python patch_spion_page.py [repo-root]     default C:\\netz

Idempotent.
"""

import sys
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(r"C:\netz")
TARGET = ROOT / "docs" / "spion.html"

NAV = '''<nav id="sitenav">
  <a class="home" href="index.html"><img src="crow_mark.svg" alt="">NebelKr&auml;he</a>
  <span class="sp"></span>
  <a href="index.html">Home</a>
  <a href="standards.html">Standards</a>
  <a href="conformance.html">Conformance</a>
  <a href="register.html">Register</a>
  <a href="verify.html">Verify</a>
  <a href="nest.html">Nest</a>
  <a href="ledger.html">Ledger</a>
  <a href="kraehes_kalls.html">Kalls</a>
  <a href="KriegForeKaster.html">ForeKaster</a>
</nav>
'''

NAV_CSS = '''<style>
#sitenav{position:sticky;top:0;z-index:40;display:flex;align-items:center;gap:.15rem;
  flex-wrap:wrap;padding:.45rem .9rem;background:rgba(8,11,15,.82);
  backdrop-filter:blur(10px);border-bottom:1px solid var(--line,#242a31);
  font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.68rem;letter-spacing:.06em}
#sitenav a{color:var(--dim,#8b8d92);text-decoration:none;padding:.25rem .5rem;
  text-transform:uppercase}
#sitenav a:hover{color:var(--brass2,#dcb65e)}
#sitenav a.home{color:var(--fg,#d9d6cf);display:flex;align-items:center;gap:.45rem;
  text-transform:none;letter-spacing:.02em;font-size:.8rem}
#sitenav a.home img{height:17px;width:auto}
#sitenav .sp{flex:1 1 auto}
</style>
'''

OLD = ("The watch runs on infrastructure the desk does not control\n"
       "  and commits under a machine identity. That is deliberate.")

NEW = ("The watch runs on infrastructure the desk does not control.\n"
       "  <b>Correction, 2026-07-27:</b> this paragraph previously said it commits under a "
       "machine identity. It does not. The workflow declares a committer address in "
       "GitHub's legacy no-reply form, which resolves to the account of an unrelated "
       "third party, so every observation commit is currently attributed to someone with "
       "no connection to this desk. The commits are real and the timestamps are the "
       "runner's; only the attribution is wrong. It is being corrected in the workflow, "
       "and this notice stays until it is. The point the paragraph was making still "
       "holds, and now holds against its own author:")


def main():
    if not TARGET.exists():
        print(f"FAIL — no such file: {TARGET}")
        return 1
    s = orig = TARGET.read_text(encoding="utf-8")

    if "sitenav" in s and "Correction, 2026-07-27" in s:
        print("ALREADY PATCHED — nothing written.")
        return 0

    if "sitenav" not in s:
        if "</head>" in s:
            s = s.replace("</head>", NAV_CSS + "</head>", 1)
        else:
            s = NAV_CSS + s
        if "<body>" in s:
            s = s.replace("<body>", "<body>\n" + NAV, 1)
        else:
            s = NAV + s
        print("  added · site navigation")

    if OLD in s:
        s = s.replace(OLD, NEW, 1)
        print("  added · correction to the custody claim")
    elif "Correction, 2026-07-27" not in s:
        print("  WARN  · custody sentence not found in the expected form; "
              "the paragraph may have been edited. Nothing changed there.")

    if s == orig:
        print("Nothing to change.")
        return 0
    TARGET.write_text(s, encoding="utf-8")
    print(f"\npatched → {TARGET}")
    print("\nThe workflow itself is still wrong. In the browser, edit")
    print("  .github/workflows/spion.yml  line 49")
    print("  user.email \"spion@users.noreply.github.com\"")
    print("to an address that resolves to no GitHub account, e.g.")
    print("  spion@retroprescientaudit.com")
    print("then remove this notice from the page.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
