#!/usr/bin/env python3
"""
fontlocal.py — pull the site's webfonts local. Step 1 of 2.

Run from C:\\netz. Writes ONLY into docs\\fonts\\. Touches nothing else.

WHY
    Eleven pages request fonts from fonts.googleapis.com, which means every
    visitor's IP address is sent to Google on page load before any content
    renders. A 2022 Munich regional court decision (LG München I, 3 O 17493/20)
    found that arrangement violated GDPR because the visitor cannot consent to a
    transfer that happens as a side effect of loading the page.

    That is a live issue on a site about to be pointed at a regulator, and it is
    on pages that argue for verifiable disclosure. It is also entirely avoidable:
    all five families are under the SIL Open Font License, which permits
    self-hosting and redistribution.

    Two of the eleven use @import rather than <link>, which is worse — @import
    blocks rendering AND still calls Google.

WHAT THIS DOES
    1. Asks Google for each stylesheet the site currently requests, with a modern
       browser User-Agent so the woff2 variants come back rather than the legacy
       formats served to old agents.
    2. Downloads every font file referenced, into docs\\fonts\\.
    3. Writes docs\\fonts\\fonts.css with the same @font-face rules, src rewritten
       to local paths, unicode-range preserved so subsetting still works.
    4. Writes docs\\fonts\\NOTICE.txt recording provenance and the licence.

    It does NOT edit any page, brand.css, or netz.py. That is step 2, and it runs
    only after this one is verified — stripping the remote calls before the local
    files are present would leave the site rendering in fallback until fixed.

SUBSETS
    latin, latin-ext, cyrillic and cyrillic-ext are kept. Cyrillic matters: the
    war desk and Ohrwurm render Russian source phrases, and dropping it would
    show tofu boxes on exactly the material that proves the instrument works.
    Greek and Vietnamese are dropped — nothing on the site uses them.

RUN
    cd C:\\netz
    python fontlocal.py
    python fontlocal.py --check        (re-verify without downloading)
"""
import argparse, re, sys, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
FONTDIR = HERE / "docs" / "fonts"

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

# Exactly what the eleven pages ask for today, deduplicated by family+weight.
SHEETS = [
    # generated pages (netz.py render_html) — note Mono 700 and Spectral
    "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700"
    "&family=IBM+Plex+Sans:wght@400;500;600"
    "&family=Spectral:ital,wght@0,500;0,600;1,400&display=swap",
    # index.html and kraehes_kalls.html
    "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,400"
    "&family=IBM+Plex+Mono:wght@400;500;600"
    "&family=IBM+Plex+Sans:wght@400;500;600&display=swap",
    # standards.html wants Sans 300
    "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600"
    "&family=IBM+Plex+Mono:wght@400;500&display=swap",
    # the compendium
    "https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&display=swap",
]

KEEP_SUBSETS = {"latin", "latin-ext", "cyrillic", "cyrillic-ext"}
FACE_RE = re.compile(r"/\*\s*([a-z0-9-]+)\s*\*/\s*(@font-face\s*\{.*?\})", re.S)
URL_RE = re.compile(r"url\((https://[^)]+)\)")
FAM_RE = re.compile(r"font-family:\s*'([^']+)'")
WGT_RE = re.compile(r"font-weight:\s*(\d+)")
STY_RE = re.compile(r"font-style:\s*(\w+)")


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=45).read()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="report state, download nothing")
    a = ap.parse_args()

    if a.check:
        if not FONTDIR.exists():
            print("docs\\fonts does not exist — run without --check first."); return 1
        files = sorted(FONTDIR.glob("*.woff2"))
        css = FONTDIR / "fonts.css"
        print(f"docs\\fonts: {len(files)} woff2 · fonts.css {'present' if css.exists() else 'MISSING'}")
        if css.exists():
            text = css.read_text(encoding="utf-8")
            print(f"  @font-face rules: {text.count('@font-face')}")
            missing = [m for m in re.findall(r'url\("?([^")]+)"?\)', text)
                       if not (FONTDIR / Path(m).name).exists()]
            print(f"  rules pointing at a missing file: {len(missing)}")
            for m in missing[:5]:
                print(f"    {m}")
            fams = sorted(set(re.findall(r"font-family:\s*'([^']+)'", text)))
            print(f"  families: {', '.join(fams)}")
        return 0

    FONTDIR.mkdir(parents=True, exist_ok=True)
    seen, out_rules, downloaded, skipped = set(), [], 0, 0

    for sheet in SHEETS:
        print(f"fetching stylesheet …")
        try:
            css = get(sheet).decode("utf-8")
        except Exception as e:
            print(f"  FAIL — could not fetch: {e}")
            return 1

        for subset, block in FACE_RE.findall(css):
            if subset not in KEEP_SUBSETS:
                skipped += 1
                continue
            fam = (FAM_RE.search(block) or [None, "unknown"])[1]
            wgt = (WGT_RE.search(block) or [None, "400"])[1]
            sty = (STY_RE.search(block) or [None, "normal"])[1]
            m = URL_RE.search(block)
            if not m:
                continue
            remote = m.group(1)
            name = f"{fam.replace(' ', '')}-{wgt}{'i' if sty == 'italic' else ''}-{subset}.woff2"
            key = (fam, wgt, sty, subset)
            if key in seen:
                continue
            seen.add(key)

            dest = FONTDIR / name
            if not dest.exists():
                try:
                    dest.write_bytes(get(remote))
                    downloaded += 1
                    print(f"  + {name}")
                except Exception as e:
                    print(f"  ! {name}: {e}")
                    continue
            out_rules.append(URL_RE.sub(f'url("{name}")', block))

    if not out_rules:
        print("nothing collected — aborting without writing fonts.css"); return 1

    header = (
        "/* fonts.css — generated by fontlocal.py. Do not hand-edit; regenerate.\n"
        " *\n"
        " * Self-hosted so that loading a page does not transmit the visitor's IP\n"
        " * address to a third party before any content renders. All families here\n"
        " * are SIL Open Font License; see NOTICE.txt in this directory.\n"
        " *\n"
        " * unicode-range is preserved from the upstream rules, so a browser still\n"
        " * fetches only the subsets a page actually needs.\n"
        " */\n\n")
    (FONTDIR / "fonts.css").write_text(header + "\n\n".join(out_rules) + "\n", encoding="utf-8")

    (FONTDIR / "NOTICE.txt").write_text(
        "Fonts in this directory are self-hosted copies.\n\n"
        "Families: IBM Plex Mono, IBM Plex Sans, Spectral, Cormorant Garamond, Cinzel.\n"
        "All are licensed under the SIL Open Font License, Version 1.1, which permits\n"
        "redistribution and self-hosting provided this notice accompanies them.\n\n"
        "Retrieved from Google Fonts via fontlocal.py. Subsets retained: latin,\n"
        "latin-ext, cyrillic, cyrillic-ext. Greek and Vietnamese were not retained.\n\n"
        "Self-hosted rather than requested from fonts.googleapis.com so that loading\n"
        "a page on this site does not transmit a visitor's IP address to a third\n"
        "party as a side effect of rendering.\n\n"
        "The full OFL text should be placed alongside this file as OFL.txt.\n",
        encoding="utf-8")

    print(f"\nok — {downloaded} file(s) downloaded, {len(out_rules)} @font-face rule(s) written")
    print(f"     {skipped} rule(s) skipped as unused subsets")
    print(f"     -> {FONTDIR / 'fonts.css'}")
    print(f"     -> {FONTDIR / 'NOTICE.txt'}")
    print("\n  Add the OFL text as docs\\fonts\\OFL.txt — the licence requires it travel")
    print("  with the fonts. It is one file, same for all five families.")
    print("\n  next:  python fontlocal.py --check")
    print("         then Claude writes step 2, which strips the remote calls.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
