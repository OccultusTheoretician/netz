#!/usr/bin/env python3
"""patch_fixes_kk16b.py — two fixes, report-only by default, --apply writes.

[QWEN] The control arm produced nothing for two days from two defects the
manual arms don't share:
  1. bare military DTG tokens (311502Z JUL 26) inside the citations array break
     json.loads before any salvage runs — they are now quoted at normalize time
     and the citations coercion drops non-integer tokens instead of discarding
     the whole entry;
  2. the truncation salvage cut at the last '}' — which lands inside a quoted
     string whenever the token limit hits mid-value. A raw_decode object walk
     now recovers every COMPLETE projection first; the rfind cut remains as the
     fallback;
  3. kkr_raw_last.txt was written only on total parse failure — a partially
     salvaged run left no audit copy. The raw now writes unconditionally before
     parsing.

[XLATE] Root cause of the standing audit finding: md_inline has no backtick
rule at all, and kkr.py injected literal <code translate="no"> HTML into the
packet markdown — which html.escape then flattened into visible &lt;code&gt;
text with no real element for the shield to live on. The renderer now turns
`backticks` into <code translate="no"> (escaping stays on, so model-authored
markdown still cannot inject HTML), kkr.py goes back to backticks, and the
already-shipped pages plus both forecasts mirror twins are stamped with the
correctly rendered element so the finding clears now, not at the next packet.
"""
import argparse
from pathlib import Path

ROOT = Path(".").resolve()

EDITS = [
    # ---------------- QWEN ----------------
    ("kkr.py",
     b"        txt = txt.replace(a, b)\n    return txt",
     b"        txt = txt.replace(a, b)\n"
     b"    # bare military DTG tokens (e.g. 311502Z JUL 26) inside arrays corrupt\n"
     b"    # the JSON; quote them so the parse survives and the citation coercion\n"
     b"    # drops them as non-integers instead of killing the run\n"
     b"    txt = re.sub(r'(?<=[\\[,\\s])(\\d{6}Z[ \\t]+[A-Z]{3}[ \\t]+\\d{2})(?=[\\s,\\]}])',\n"
     b"                 r'\"\\1\"', txt)\n"
     b"    return txt",
     b"bare military DTG tokens",
     "qwen: DTG tokens quoted at normalize"),
    ("kkr.py",
     b'        # SALVAGE a truncated array (model hit its token limit mid-object):\n'
     b'        # keep everything up to the last complete "}", then close the bracket.\n'
     b'        last = blob.rfind("}")',
     b'        # SALVAGE, two stages. Stage 1: walk complete objects with raw_decode\n'
     b'        # truncation- and mid-string-safe; a cut inside a quoted value\n'
     b'        # cannot fake an object boundary the way rfind("}") can.\n'
     b'        _dec, _objs, _i = json.JSONDecoder(), [], blob.find("{")\n'
     b'        while 0 <= _i < len(blob):\n'
     b'            try:\n'
     b'                _o, _j = _dec.raw_decode(blob, _i)\n'
     b'            except json.JSONDecodeError:\n'
     b'                break\n'
     b'            if isinstance(_o, dict):\n'
     b'                _objs.append(_o)\n'
     b'            _i = blob.find("{", _j)\n'
     b'        if _objs:\n'
     b'            arr = _objs\n'
     b'            print(f"SALVAGE: recovered {len(_objs)} complete projections "\n'
     b'                  f"from damaged output", file=sys.stderr)\n'
     b'    if arr is None:\n'
     b'        # Stage 2 (fallback): cut at the last complete "}", close the bracket.\n'
     b'        last = blob.rfind("}")',
     b"Stage 1: walk complete objects",
     "qwen: raw_decode object-walk salvage"),
    ("kkr.py",
     b'"citations": [int(c) for c in p.get("citations", [])]}',
     b'"citations": [int(c) for c in p.get("citations", [])\n'
     b'                                   if str(c).strip().lstrip("-").isdigit()]}',
     b'if str(c).strip().lstrip("-").isdigit()',
     "qwen: citations coercion drops non-integer tokens, keeps the entry"),
    ("kkr.py",
     b"    projs = parse_projections(raw)",
     b'    (OUT / "kkr_raw_last.txt").write_text(raw, encoding="utf-8")  # audit copy, unconditional\n'
     b"    projs = parse_projections(raw)",
     b"audit copy, unconditional",
     "qwen: raw saved before parsing, every run"),
    # ---------------- XLATE ----------------
    ("netz.py",
     b"    t = html.escape(text, quote=False)\n",
     b"    t = html.escape(text, quote=False)\n"
     b"    t = re.sub(r\"`([^`]+)`\", r'<code translate=\"no\">\\1</code>', t)\n",
     b"<code translate=\"no\">\\1</code>",
     "xlate: md_inline backtick rule, shielded code element (escape stays on)"),
    ("kkr.py",
     b'<code translate=\\"no\\">python kkr.py --resolve</code>',
     b'`python kkr.py --resolve`',
     b'--resolve`). ',
     "xlate: packet md uses backticks; the renderer owns the element"),
    ("kkr.py",
     b'    m = re.search(r"\\[.*\\]", txt, re.S)\n'
     b'    if not m:\n'
     b'        return []\n'
     b'    blob = m.group(0)',
     b'    m = re.search(r"\\[.*\\]", txt, re.S)\n'
     b'    if m:\n'
     b'        blob = m.group(0)\n'
     b'    else:\n'
     b'        j0 = txt.find("[")\n'
     b'        if j0 == -1:\n'
     b'            return []\n'
     b'        blob = txt[j0:]  # no closing ] survived - salvage territory',
     b'salvage territory',
     "qwen: blob extraction degrades instead of dying when no ] survived"),
    ("kkr.py",
     b'        _dec, _objs, _i = json.JSONDecoder(), [], blob.find("{")',
     b'        _src = txt[txt.find("["):]  # walk the FULL text - the blob regex\n'
     b'        # cuts at the last ], which is usually the final object\'s citations\n'
     b'        _dec, _objs, _i = json.JSONDecoder(), [], _src.find("{")',
     b'walk the FULL text',
     "qwen: salvage walks the untruncated source"),
    ("kkr.py",
     b'                _o, _j = _dec.raw_decode(blob, _i)',
     b'                _o, _j = _dec.raw_decode(_src, _i)',
     b'raw_decode(_src, _i)',
     "qwen: walk decodes from source"),
    ("kkr.py",
     b'            _i = blob.find("{", _j)',
     b'            _i = _src.find("{", _j)',
     b'_src.find("{", _j)',
     "qwen: walk advances on source"),
]

STAMP_OLD = b'&lt;code translate="no"&gt;python kkr.py --resolve&lt;/code&gt;'
STAMP_NEW = b'<code translate="no">python kkr.py --resolve</code>'


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    for path, old, new, mark, note in EDITS:
        p = ROOT / path
        if not p.exists():
            print(f"MISS  {path} - file absent - {note}"); continue
        b = p.read_bytes()
        if mark in b:
            print(f"OK    {path} - already applied - {note}"); continue
        if old in b:
            if a.apply: p.write_bytes(b.replace(old, new, 1))
            print(f"{'FIX  ' if a.apply else 'WOULD'} {path} - {note}"); continue
        print(f"MISS  {path} - target not found - {note}")
    # stamp the already-shipped pages, twins symmetric
    for f in ("docs/kkr.html", "forecasts/KKR_latest.html",
              "docs/ledger.html", "forecasts/ledger.html", "docs/report.html"):
        p = ROOT / f
        if not p.exists():
            continue
        b = p.read_bytes()
        n = b.count(STAMP_OLD)
        if not n:
            print(f"OK    {f} - no escaped span present")
            continue
        if a.apply:
            p.write_bytes(b.replace(STAMP_OLD, STAMP_NEW))
        print(f"{'FIX  ' if a.apply else 'WOULD'} {f} - escaped code span rendered real x{n}")
    if not a.apply:
        print("report only - rerun with --apply to write")


if __name__ == "__main__":
    main()
