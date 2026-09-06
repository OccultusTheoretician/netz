#!/usr/bin/env python3
"""legende.py - instruments.html: every instrument defined from its own
source, every served record indexed. Reads instruments_map.json (blurb,
optional module); module docstring first line prints as the source line.
The records section is computed from docs/ so no served artifact can be
orphaned while this page exists. Idempotent full regeneration."""
import ast, json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
DOCS = HERE / "docs"
_SKIP = {".nojekyll","CNAME",".gitignore","robots.txt","sitemap.xml"}
PAGE_EXT = (".ots",".png",".ico",".svg",".css",".js",".html",".xml",".txt",
            ".jpg",".jpeg",".webp",".woff",".woff2")
def esc(s):
    return (s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;"))
def docline(mod):
    p = HERE / mod
    if not p.exists(): return None
    try:
        d = ast.get_docstring(ast.parse(p.read_text(encoding="utf-8",errors="replace")))
        return d.strip().splitlines()[0].strip() if d else None
    except Exception: return None
def main():
    man = json.loads((HERE/"nav_manifest.json").read_text(encoding="utf-8-sig"))
    imap = json.loads((HERE/"instruments_map.json").read_text(encoding="utf-8-sig"))
    o = []
    o.append('<!doctype html><html lang="en"><head><meta charset="utf-8">')
    o.append('<meta name="viewport" content="width=device-width,initial-scale=1">')
    o.append('<title>Instruments &mdash; The Prescient Desk</title>')
    o.append('<link rel="canonical" href="https://retroprescientaudit.com/instruments.html">')
    o.append('<meta name="description" content="Every instrument on the desk, defined from its own source; every served record, indexed.">')
    o.append('<meta property="og:image" content="https://retroprescientaudit.com/og_nebelkraehe.png">')
    o.append('<link rel="stylesheet" href="fonts/fonts.css">')
    o.append('<style>:root{--bg:#0c0e11;--fg:#d6d3cb;--dim:#8b8b85;--brass:#e9e7e2;--line:#26292f}')
    o.append('*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.65 "IBM Plex Sans",sans-serif}')
    o.append('.wrap{max-width:900px;margin:0 auto;padding:0 1.25rem}header{padding:3rem 0 1.2rem}')
    o.append('h1{font-size:1.9rem;margin:.2rem 0}.kicker{font:600 .72rem "IBM Plex Mono",monospace;letter-spacing:.22em;color:var(--brass);text-transform:uppercase}')
    o.append('.dek{color:var(--dim);max-width:46rem}section{border-top:1px solid var(--line);padding:1.8rem 0}')
    o.append('h2{font:600 .8rem "IBM Plex Mono",monospace;letter-spacing:.18em;text-transform:uppercase;color:var(--brass);margin:0 0 .8rem}')
    o.append('table{border-collapse:collapse;width:100%}td{padding:.42rem .6rem .42rem 0;vertical-align:top;border-top:1px solid var(--line)}')
    o.append('td.n{white-space:nowrap;font:600 .72rem "IBM Plex Mono",monospace;letter-spacing:.08em;text-transform:uppercase}')
    o.append('a{color:#c9c7c1;text-decoration:none}a:hover{color:#fff}')
    o.append('.src{display:block;font:400 .66rem "IBM Plex Mono",monospace;color:#6a6a64;margin-top:.15rem}')
    o.append('ul{margin:.2rem 0;padding-left:1.1rem}li{margin:.3rem 0}</style></head>')
    o.append('<body data-kk30-legend="1"><header><div class="wrap">')
    o.append('<div class="kicker">Legend</div><h1>Instruments</h1>')
    o.append('<p class="dek">Every instrument on the desk, defined from its own source. Definitions come from each tool&#39;s docstring or its page&#39;s own description &mdash; never hand-copied twice.</p>')
    o.append('</div></header>')
    for g in man.get("groups", []):
        o.append('<section><div class="wrap"><h2>' + esc(g["label"]) + '</h2><table>')
        for ln in g.get("links", []):
            spec = imap.get(ln["href"], {})
            blurb = spec.get("blurb", "")
            mod = spec.get("module")
            srcline = docline(mod) if mod else None
            src = ('<span class="src">' + esc(mod) + (' &mdash; ' + esc(srcline) if srcline else '') + '</span>') if mod else ''
            o.append('<tr><td class="n"><a href="' + ln["href"] + '">' + esc(ln["text"]) + '</a></td>'
                     '<td>' + esc(blurb) + src + '</td></tr>')
        o.append('</table></div></section>')
    # LEGENDETRACKED-2026-09-06: a served document is a file git tracks under docs/;
    # untracked or ignored files cannot be served by Pages and are not listed.
    import subprocess as _sp
    try:
        _tracked = set(Path(x).name for x in _sp.run(
            ["git", "ls-files", "--", "docs"], capture_output=True, text=True, timeout=30, cwd=str(HERE)
        ).stdout.split("\n") if x.strip() and Path(x).parent.name == "docs")
    except Exception:
        _tracked = None   # no git: fall back to the disk walk, printed
    if _tracked is None:
        print("legende: git unavailable - listing served documents from disk")
    arts = sorted(p.name for p in DOCS.iterdir() if p.is_file()
                  and p.name not in _SKIP and not p.name.lower().endswith(PAGE_EXT)
                  and (_tracked is None or p.name in _tracked))
    o.append('<section><div class="wrap"><h2>Served records</h2>')
    o.append('<p class="dek">Machine and document records served beside the pages. Indexed here so no published artifact is reachable from nowhere.</p><ul>')
    for a in arts:
        kind = "machine record" if a.endswith(".json") else "served document"
        o.append('<li><a href="' + a + '">' + esc(a) + '</a> <span class="src">' + kind + '</span></li>')
    o.append('</ul></div></section>')
    o.append('<footer><div class="wrap" style="padding:1.4rem 0 3rem;color:#8b8b85;font-size:.82rem">Generated by legende.py from instruments_map.json and module docstrings.</div></footer>')
    o.append('</body></html>')
    (DOCS/"instruments.html").write_text("\n".join(o) + "\n", encoding="utf-8")
    print("legende: instruments.html written -", len(arts), "record(s) indexed")
if __name__ == "__main__":
    main()
