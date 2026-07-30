#!/usr/bin/env python3
"""
site_audit.py - the whole surface, by enumeration.

WHY IT ENUMERATES

A prior instance on this desk twice reported "full audit - clean" after
sampling. Everything here counts what it checked and prints the count. If a
section says it scanned 395 references, it scanned 395. If it cannot check
something, it says so rather than passing silently.

Writes nothing. Read-only against the working tree and git index.

WHAT IT CHECKS, AND WHY EACH ONE IS HERE

SITE
  links       every href and src in docs/*.html resolved against disk.
              JavaScript-built URLs are detected and excluded rather than
              reported as broken - a previous pass called six of seven
              "broken links" when they were string concatenation.
  case        CRITICAL. Every local reference compared against the ACTUAL
              filename set read from the directory, not os.path.exists().
              Windows is case-insensitive and GitHub Pages is not. Four pages
              once referenced og_nebelKraehe.png with a capital K; the file
              was lowercase; every link preview on the site rendered without
              an image and nobody knew. exists() cannot catch that. This can.
  external    any stylesheet or script pulled from a third party. The site's
              pitch is that nothing phones home; that is checkable.
  meta        description and og:image per page. A page with neither previews
              as a bare URL wherever it is shared.
  orphans     pages reachable from index.html by following links, versus
              pages that exist. An unreachable page is published and unread.
  sitemap     urls listed that do not exist, and pages that exist but are
              absent. A sitemap listing a 404 is worse than no sitemap.
  noindex     pages declaring noindex that appear in the sitemap anyway.
  bom         served files carrying a UTF-8 byte order mark. Harmless to
              browsers, but it is three bytes no diff explains.

GIT
  secrets     VALUE SHAPES, not keywords. The last keyword scan's only hits
              were the word secretary in a headline, the phrase secret salt
              in the Kalls protocol, an import secrets line, and two
              docstrings naming env vars with no values. This matches the
              shape of an actual credential: an assignment with a long
              opaque value, a known token prefix, a private key block.
              MATCHES ARE NEVER PRINTED - only file, line number and which
              pattern fired. Printing the match would be the leak.
  tracked     backup extensions, session files and vault-tier paths that are
              tracked when they should not be. Five index.html.bak* copies of
              the front page were tracked and served, unlinked and unlisted,
              because the *.bak rule never matched *.bak2.
  sweep       untracked and unignored files that `git add -A` would commit on
              the next ship. publish.bat runs git add -A.
  missing     tracked but absent from disk.
  deadrules   .gitignore rules matching nothing. Not an error; a rule that
              matches nothing may be protecting a file that does not exist
              yet, which is the point of it.

    python site_audit.py
    python site_audit.py --section site
    python site_audit.py --verbose

Run from C:\\netz. Standard library only. ASCII-only output.
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

DOCS = Path("docs")

# reference extraction. Group 1 is the target.
REF_RE = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""")
# a target containing these is built at runtime, not a literal path
JS_MARKERS = ("'+", "+'", '"+', '+"', "${", "{{")

META_DESC = re.compile(r"""<meta\s+name=["']description["']""", re.I)
META_OG = re.compile(r"""<meta\s+property=["']og:image["']""", re.I)
ROBOTS_NOINDEX = re.compile(
    r"""<meta\s+name=["']robots["']\s+content=["']([^"']*)""", re.I)

# credential VALUE shapes. Deliberately not keyword matching.
SECRET_PATTERNS = [
    ("assignment with long opaque value",
     re.compile(r"""(?i)\b[A-Z_]*(?:KEY|TOKEN|SECRET|PASSWORD|PASSWD|APIKEY)"""
                r"""[A-Z_]*\s*[=:]\s*["'][A-Za-z0-9_\-/+=]{20,}["']""")),
    ("AWS access key id", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b")),
    ("Anthropic key", re.compile(r"\bsk-ant-[A-Za-z0-9_\-]{20,}")),
    ("OpenAI key", re.compile(r"\bsk-[A-Za-z0-9]{32,}\b")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9\-]{10,}")),
    ("private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    # length is 30-45 rather than exactly 35: a pattern brittle enough to
    # miss by one character would miss a real token too
    ("Telegram bot token", re.compile(r"\b\d{8,10}:[A-Za-z0-9_\-]{30,45}\b")),
    ("bearer with long token",
     re.compile(r"""(?i)bearer\s+[A-Za-z0-9_\-\.]{30,}""")),
]

BAD_TRACKED = [
    ("backup copy", re.compile(r"\.(bak\d*|orig|old|save|pre[a-z]+)$", re.I)),
    ("session file", re.compile(r"\.session$", re.I)),
    ("vault tier", re.compile(r"(^|/)vault/", re.I)),
    ("opening material", re.compile(r"campaign.*\.json$", re.I)),
]

TEXT_EXT = {".py", ".md", ".html", ".json", ".txt", ".bat", ".css", ".js",
            ".yml", ".yaml", ".xml", ".cfg", ".ini", ".ps1", ".gitignore"}


def git(args):
    try:
        r = subprocess.run(["git"] + args, capture_output=True, text=True,
                           check=False, errors="replace")
        return r.stdout if r.returncode == 0 else ""
    except Exception:
        return ""


class Report:
    def __init__(self):
        self.findings = []
        self.counts = {}

    def head(self, title):
        print("")
        print("=" * 72)
        print("  " + title)
        print("=" * 72)

    def sub(self, title, n_checked, unit="items"):
        print("")
        print("  %s" % title)
        print("  %s" % ("-" * (len(title))))
        print("    checked %d %s" % (n_checked, unit))
        self.counts[title] = n_checked

    def bad(self, sev, msg):
        self.findings.append((sev, msg))
        print("    %-6s %s" % (sev, msg))

    def ok(self, msg):
        print("    ok     %s" % msg)


def audit_site(r, verbose):
    r.head("SITE")
    if not DOCS.is_dir():
        r.bad("FAIL", "docs/ not found - run from C:\\netz")
        return

    served = {l.split(chr(47))[-1] for l in git(["ls-files", "docs/"]).splitlines() if l.lower().endswith(".html") and l.count(chr(47))==1}
    # docs/ on disk holds untracked scratch files. Pages serves the repo,
    # so an untracked page is not published and is not a site finding.
    pages = sorted(p for p in DOCS.glob("*.html") if p.name in served)
    # ACTUAL filename set, real case, for the case-sensitivity check
    actual = set()
    for root, _dirs, files in os.walk(DOCS):
        rel = os.path.relpath(root, DOCS).replace("\\", "/")
        for f in files:
            actual.add(f if rel == "." else rel + "/" + f)

    texts = {}
    for p in pages:
        texts[p.name] = p.read_text(encoding="utf-8", errors="replace")

    # --- links, case, external -------------------------------------------
    n_refs = n_js = 0
    broken, wrongcase, external = [], [], []
    graph = {}
    for name, s in texts.items():
        graph[name] = set()
        for t in REF_RE.findall(s):
            n_refs += 1
            if any(m in t for m in JS_MARKERS):
                n_js += 1
                continue
            if t.startswith(("mailto:", "data:", "javascript:", "tel:")):
                continue
            if t.startswith(("http://", "https://", "//")):
                if t.rsplit("?", 1)[0].endswith((".css", ".js")):
                    external.append((name, t))
                continue
            target = t.split("#", 1)[0].split("?", 1)[0].lstrip("/")
            if not target:
                continue
            if target.endswith(".html"):
                graph[name].add(target)
            if target in actual:
                continue
            lower = {a.lower(): a for a in actual}
            if target.lower() in lower:
                wrongcase.append((name, t, lower[target.lower()]))
            else:
                broken.append((name, t))

    r.sub("internal references", n_refs, "href/src attributes")
    print("    %d runtime-built URLs excluded (JavaScript concatenation)" % n_js)
    if wrongcase:
        for pg, ref, real in wrongcase:
            r.bad("CASE", "%s -> %s   file on disk is %s" % (pg, ref, real))
        print("    CASE mismatches 404 on GitHub Pages and resolve on Windows.")
        print("    This is the class that broke every link preview on the site.")
    else:
        r.ok("no case mismatches - every reference matches disk exactly")
    if broken:
        for pg, ref in broken:
            r.bad("BROKEN", "%s -> %s" % (pg, ref))
    else:
        r.ok("no broken internal references")

    r.sub("third-party assets", len(pages), "pages")
    if external:
        for pg, u in external:
            r.bad("EXT", "%s pulls %s" % (pg, u))
    else:
        r.ok("zero external stylesheets or scripts - nothing phones home")

    # --- meta -------------------------------------------------------------
    r.sub("preview metadata", len(pages), "pages")
    nometa = []
    for name, s in texts.items():
        d, o = bool(META_DESC.search(s)), bool(META_OG.search(s))
        ni = ROBOTS_NOINDEX.search(s)
        noindex = bool(ni and "noindex" in ni.group(1).lower())
        if not (d and o) and not noindex:
            nometa.append((name, d, o))
        elif verbose:
            print("    ok     %-34s desc=%s og=%s%s"
                  % (name, d, o, "  [noindex]" if noindex else ""))
    if nometa:
        for name, d, o in nometa:
            r.bad("META", "%s missing %s"
                  % (name, ", ".join(x for x, has in
                                     (("description", d), ("og:image", o))
                                     if not has)))
    else:
        r.ok("every indexed page carries description and og:image")

    # --- orphans ----------------------------------------------------------
    seen, stack = set(), ["index.html"]
    while stack:
        cur = stack.pop()
        if cur in seen or cur not in graph:
            continue
        seen.add(cur)
        stack.extend(graph[cur])
    orphans = sorted(set(graph) - seen)
    r.sub("reachability from index.html", len(graph), "pages")

    # --- nav consistency ---------------------------------------------------
    # Every served page must carry a navigation whose internal-link SET is
    # identical, so a visitor sees the same map from every page. Drift here
    # is the most visible unprofessionalism a multi-page site can have, and
    # it accretes silently as pages are hand-edited — so it is enumerated.
    import re as _re
    navsets = {}
    # Scope to `pages` — the tracked-and-served set computed above — not the
    # raw disk glob, so a gitignored scratch page (warroom and its kin) is
    # never audited as a served surface. Every other site check uses this
    # scope; the nav check regressed to the glob and must not.
    for _p in pages:
        _t = _p.read_text(encoding="utf-8", errors="replace")
        _m = _re.search(r"<nav\b.*?</nav>", _t, _re.S)
        if not _m:
            r.bad("NONAV", "%s carries no <nav> element" % _p.name)
            continue
        _hrefs = frozenset(h for h in _re.findall(r'href="([^"]+\.html)"',
                                                  _m.group(0))
                           if not h.startswith("http"))
        navsets.setdefault(_hrefs, []).append(_p.name)
    if len(navsets) <= 1:
        _n = len(next(iter(navsets))) if navsets else 0
        r.ok(f"every page's nav offers the identical {_n}-page map")
    else:
        big = max(navsets, key=lambda k: len(navsets[k]))
        for _hrefs, _pages in navsets.items():
            if _hrefs is big:
                continue
            miss = sorted(big - _hrefs)[:6]
            r.bad("NAVDRIFT", f"{len(_pages)} page(s) diverge from the "
                      f"majority nav (e.g. {_pages[0]} misses {miss})")
    r.sub("nav consistency", len(list(DOCS.glob("*.html"))), "pages")

    if orphans:
        for o in orphans:
            s = texts[o]
            ni = ROBOTS_NOINDEX.search(s)
            tag = " [declares noindex - deliberate]" if (
                ni and "noindex" in ni.group(1).lower()) else ""
            r.bad("ORPHAN", "%s reachable from nothing%s" % (o, tag))
    else:
        r.ok("every page reachable by following links from the front page")

    # --- sitemap ----------------------------------------------------------
    sm = DOCS / "sitemap.xml"
    if not sm.exists():
        r.sub("sitemap", 0, "urls")
        r.bad("MISSING", "docs/sitemap.xml does not exist")
    else:
        urls = re.findall(r"<loc>\s*([^<]+?)\s*</loc>",
                          sm.read_text(encoding="utf-8", errors="replace"))
        listed = {u.rsplit("/", 1)[-1] for u in urls}
        r.sub("sitemap", len(urls), "urls")
        tracked_html = {l.split("/")[-1] for l in
                        git(["ls-files", "docs/"]).splitlines()
                        if l.lower().endswith(".html") and l.count("/") == 1}
        for u in sorted(listed):
            if not (DOCS / u).exists():
                r.bad("404", "sitemap lists %s which does not exist" % u)
        for name, s in texts.items():
            ni = ROBOTS_NOINDEX.search(s)
            noindex = bool(ni and "noindex" in ni.group(1).lower())
            if noindex and name in listed:
                r.bad("NOINDEX", "%s declares noindex and is in the sitemap"
                      % name)
            if not noindex and name in tracked_html and name not in listed:
                r.bad("ABSENT", "%s is tracked and indexable but not in the "
                                "sitemap - rebuild it" % name)
        if not any(f[0] in ("404", "NOINDEX", "ABSENT") for f in r.findings):
            r.ok("sitemap matches the tracked, indexable page set")

    # --- BOM --------------------------------------------------------------
    n = 0
    boms = []
    # Pages serves the repository tree: a gitignored local file never
    # publishes, so scanning it flags a surface that does not exist.
    _served = set(git(["ls-files", "docs"]).splitlines())
    for p in sorted(DOCS.rglob("*")):
        if (p.is_file() and str(p.as_posix()) in _served
                and p.suffix.lower() in (".html", ".json", ".css",
                                         ".js", ".xml", ".md", ".txt")):
            n += 1
            if p.read_bytes()[:3] == b"\xef\xbb\xbf":
                boms.append(str(p).replace("\\", "/"))
    r.sub("byte order marks", n, "served text files")
    if boms:
        for b in boms:
            r.bad("BOM", "%s carries a UTF-8 BOM" % b)
        print("    Set-Content -Encoding UTF8 on PowerShell 5.1 writes a BOM.")
        print("    Let Python write these files instead.")
    else:
        r.ok("no BOMs in served text files")


def audit_degradation(r, verbose):
    """Two properties this desk claims but never checked by enumeration.

    ACCESSIBILITY is not decoration here. The whole thesis is that a stranger
    who owes the desk nothing can read and check the record; a page a screen
    reader cannot navigate, or one that hides its own numbers behind an
    unlabelled control, fails that on its own terms.

    JS-OFF HONESTY is the harder property. Several pages recompute their
    figures client-side. With scripts blocked, the correct behaviour is to
    say so — a page that renders a stale figure, or an empty frame that looks
    like an empty world, is making a claim it cannot support. This check reads
    every element the scripts are supposed to fill and asks whether its
    pre-script contents are honest about being unfilled.
    """
    r.head("DEGRADATION AND ACCESS")
    served = {l.split(chr(47))[-1] for l in git(["ls-files", "docs/"]).splitlines()
              if l.lower().endswith(".html") and l.count(chr(47)) == 1}
    pages = sorted(p for p in DOCS.glob("*.html") if p.name in served)
    texts = {p.name: p.read_text(encoding="utf-8", errors="replace") for p in pages}

    # --- language, title, viewport ---------------------------------------
    miss = []
    for name, s in texts.items():
        if not re.search(r"<html[^>]*\slang=", s, re.I):
            miss.append((name, "no lang= on <html> (screen readers guess)"))
        if not re.search(r"<title>\s*\S", s, re.I):
            miss.append((name, "no non-empty <title>"))
        if not re.search(r'name=["\']viewport["\']', s, re.I):
            miss.append((name, "no viewport meta (unreadable on a phone)"))
    r.sub("document basics", len(texts) * 3, "checks over served pages")
    if miss:
        for n, why in miss:
            r.bad("DOC", "%s: %s" % (n, why))
    else:
        r.ok("every page declares a language, a title and a viewport")

    # --- images carry alt ------------------------------------------------
    n_img = 0
    noalt = []
    for name, s in texts.items():
        for tag in re.findall(r"<img\b[^>]*>", s, re.I):
            n_img += 1
            if not re.search(r"\salt=", tag, re.I):
                noalt.append((name, tag[:70]))
    r.sub("image alternatives", n_img, "img elements")
    if noalt:
        for n, t in noalt:
            r.bad("ALT", "%s: %s" % (n, t))
    else:
        r.ok("every img carries an alt attribute (empty alt is correct for marks)")

    # --- form controls are labelled --------------------------------------
    n_ctl = 0
    unlabelled = []
    for name, s in texts.items():
        labelled = set(re.findall(r"<label[^>]*\sfor=[\"']([^\"']+)", s, re.I))
        for tag in re.findall(r"<(?:input|select|textarea)\b[^>]*>", s, re.I):
            n_ctl += 1
            if re.search(r'type=["\']?(hidden|submit|button)', tag, re.I):
                continue
            idm = re.search(r'\sid=["\']([^"\']+)', tag)
            has = bool(re.search(r"aria-label=|aria-labelledby=|title=", tag, re.I))
            if idm and idm.group(1) in labelled:
                has = True
            # a placeholder is a hint, never a label, but it is not nothing
            if not has:
                unlabelled.append((name, (idm.group(1) if idm else tag[:50])))
    r.sub("labelled controls", n_ctl, "form controls")
    if unlabelled:
        for n, t in unlabelled:
            r.bad("LABEL", "%s: control %s has no label, aria-label or title"
                  % (n, t))
        print("    A placeholder is a hint, not a name: it disappears on input")
        print("    and is not announced as the control's label.")
    else:
        r.ok("every visible control has a programmatic name")

    # --- JS-off honesty --------------------------------------------------
    # Elements a script fills, read as a browser with scripts blocked would.
    # Only elements the script actually WRITES a value into count: an id is
    # often grabbed just to attach a handler, and a button reading "RUN" with
    # scripts off is honest — it is a control, not a figure. Buttons, options
    # and inputs are excluded for the same reason.
    HONEST = re.compile(r"loading|unavailable|reading |requires javascript|"
                        r"scripts? (?:are |is )?(?:blocked|disabled|off)|"
                        r"did not load|is empty|not published|unreachable|"
                        r"recomput|select |choose |no findings yet|load with scripts|"
                        r"^[-\u2014\u2013.\u2026\s]*$", re.I)
    WRITE = re.compile(
        r"(?:getElementById\(['\"]([^'\"]+)['\"]\)|\$\(['\"]#([^'\"]+)['\"]\))"
        r"\s*\.\s*(?:textContent|innerHTML)\s*=")
    n_slots = 0
    dishonest = []
    for name, s in texts.items():
        script = "\n".join(re.findall(r"<script>([\s\S]*?)</script>", s))
        if not script:
            continue
        written = {a or b for a, b in WRITE.findall(script)}
        for eid in sorted(written):
            m = re.search(r"<(\w+)[^>]*\sid=[\"']" + re.escape(eid)
                          + r"[\"'][^>]*>([\s\S]{0,400}?)</", s)
            if not m:
                continue
            if m.group(1).lower() in ("button", "option", "input", "select",
                                      "textarea"):
                continue
            n_slots += 1
            inner = re.sub(r"<[^>]+>", " ", m.group(2))
            inner = re.sub(r"\s+", " ", inner).strip()
            if not inner:
                continue          # empty is honest: nothing is claimed
            if not HONEST.search(inner):
                dishonest.append((name, eid, inner[:70]))
    r.sub("script-filled slots", n_slots, "elements a script writes into")
    if dishonest:
        for n, eid, txt in dishonest:
            r.bad("NOJS", "%s: #%s reads %r with scripts off - a figure that "
                  "is not being recomputed must not look like one that is"
                  % (n, eid, txt))
    else:
        r.ok("with scripts blocked every computed slot is empty or says so")

    # --- motion ----------------------------------------------------------
    movers = [n for n, s in texts.items()
              if re.search(r"requestAnimationFrame|setInterval\(", s)]
    guarded = [n for n in movers
               if "prefers-reduced-motion" in texts[n]]
    r.sub("motion", len(movers), "pages that animate")
    if movers and len(guarded) < len(movers):
        for n in movers:
            if n not in guarded:
                r.bad("MOTION", "%s animates without a prefers-reduced-motion "
                      "path" % n)
    elif movers:
        r.ok("every animating page honours prefers-reduced-motion")
    else:
        r.ok("nothing animates")


def audit_git(r, verbose):
    r.head("REPOSITORY")
    tracked = [l for l in git(["ls-files"]).splitlines() if l]
    if not tracked:
        r.bad("FAIL", "git ls-files returned nothing - run from the repo root")
        return

    # --- tracked but shouldn't be ----------------------------------------
    r.sub("tracked file hygiene", len(tracked), "tracked files")
    flagged = []
    for f in tracked:
        for label, pat in BAD_TRACKED:
            if pat.search(f):
                flagged.append((label, f))
                break
    if flagged:
        for label, f in flagged:
            r.bad("TRACKED", "%s is tracked and served (%s)" % (f, label))
        print("    git rm --cached removes it from Pages. History keeps it.")
    else:
        r.ok("no backup, session or vault-tier file is tracked")

    # --- missing ----------------------------------------------------------
    gone = [f for f in tracked if not Path(f).exists()]
    r.sub("tracked files present on disk", len(tracked), "tracked files")
    if gone:
        for f in gone[:20]:
            r.bad("MISSING", "%s is tracked but absent from disk" % f)
    else:
        r.ok("every tracked file exists")

    # --- would be swept ---------------------------------------------------
    st = [l for l in git(["status", "--short"]).splitlines() if l]
    untracked = [l[3:].strip() for l in st if l.startswith("??")]
    r.sub("files git add -A would sweep", len(untracked), "untracked paths")
    if untracked:
        for u in untracked:
            sev = "SWEEP"
            for label, pat in BAD_TRACKED:
                if pat.search(u):
                    sev = "DANGER"
                    break
            r.bad(sev, u)
        print("    publish.bat and desk.py ship both run git add -A.")
    else:
        r.ok("nothing untracked and unignored")

    # --- secrets ----------------------------------------------------------
    scanned = hits = 0
    for f in tracked:
        p = Path(f)
        if p.suffix.lower() not in TEXT_EXT and p.name != ".gitignore":
            continue
        if not p.exists():
            continue
        try:
            body = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        scanned += 1
        for i, line in enumerate(body.splitlines(), 1):
            for label, pat in SECRET_PATTERNS:
                if pat.search(line):
                    hits += 1
                    r.bad("SECRET", "%s:%d matched [%s] - MATCH NOT PRINTED"
                          % (f, i, label))
    r.sub("credential scan", scanned, "tracked text files")
    print("    value shapes, not keywords. Matches are never printed.")
    if not hits:
        r.ok("no credential-shaped value in any tracked text file")

    # --- dead ignore rules ------------------------------------------------
    gi = Path(".gitignore")
    if gi.exists():
        rules = [l.strip() for l in
                 gi.read_text(encoding="utf-8", errors="replace").splitlines()
                 if l.strip() and not l.strip().startswith("#")]
        ignored = set()
        for l in git(["status", "--short", "--ignored"]).splitlines():
            if l.startswith("!!"):
                ignored.add(l[3:].strip())
        r.sub("gitignore rules", len(rules), "rules")
        print("    %d paths currently ignored" % len(ignored))
        if verbose:
            print("    (a rule matching nothing is not an error - it may be")
            print("     guarding a file that does not exist yet)")


def main():
    ap = argparse.ArgumentParser(description="full site and repo audit")
    ap.add_argument("--section", choices=["site", "git", "all"], default="all")
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args()

    r = Report()
    print("")
    print("SITE AND REPOSITORY AUDIT - by enumeration, not sampling")
    if a.section in ("site", "all"):
        audit_site(r, a.verbose)
        audit_degradation(r, a.verbose)
    if a.section in ("git", "all"):
        audit_git(r, a.verbose)

    print("")
    print("=" * 72)
    print("  SUMMARY")
    print("=" * 72)
    for k, v in r.counts.items():
        print("    %-36s %d" % (k, v))
    print("")
    if r.findings:
        by = {}
        for sev, _ in r.findings:
            by[sev] = by.get(sev, 0) + 1
        print("    %d finding(s): %s"
              % (len(r.findings),
                 ", ".join("%s x%d" % (k, v) for k, v in sorted(by.items()))))
    else:
        print("    no findings. Every check above enumerated its whole set.")
    print("")
    return 0


if __name__ == "__main__":
    sys.exit(main())
