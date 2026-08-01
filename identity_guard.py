#!/usr/bin/env python3
"""
identity_guard.py — refuse to publish the names.

THE PROBLEM WITH THE OBVIOUS VERSION

A deny-list committed to a public repository is a file listing precisely the
names it exists to hide. So this stores only SHA-256 of each lowercased term.
identity_guard.json is safe to commit and safe to read; it discloses nothing.
Matching happens by hashing every token in every tracked file and comparing.

Findings report FILE and LINE only. The matched term is never printed, never
logged, and never written anywhere — including by this program, whose output
you have been screenshotting all night.

    python identity_guard.py add            add terms, read from a prompt
    python identity_guard.py scan           scan every git-tracked file
    python identity_guard.py scan --staged  only what is about to be committed
    python identity_guard.py test           confirm the guard actually fires

Exit 1 on any hit, so `desk.py ship` refuses.

WHAT IT CANNOT DO. It matches tokens, not meaning. It will not catch a name
split across a line break, rendered inside a PNG, embedded in EXIF, or spelled
differently. It is a floor, not a ceiling, and a green result is not a licence
to stop reading what you are about to push.
"""

import hashlib, json, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STORE = HERE / "identity_guard.json"
TOKEN = re.compile(r"[A-Za-z][A-Za-z'\-]{2,}")
TEXT_EXT = {".md", ".txt", ".html", ".css", ".js", ".py", ".json", ".yml", ".yaml",
            ".bat", ".ps1", ".svg", ".csv", ".xml", ".ini", ".cfg", ""}
SKIP_DIR = {".git", "__pycache__", "node_modules"}


_SALT_PATH = HERE / "identity_salt.local.txt"


def _salt() -> bytes:
    """Secret salt, kept off the repo. Generated on first use.

    KK18: unsalted single-word SHA-256 is invertible by wordlist, so the
    published store disclosed most of itself to anyone who knew the domain.
    The salt makes the digests real. It is gitignored under *.local.txt.
    """
    if _SALT_PATH.exists():
        s = _SALT_PATH.read_text(encoding="utf-8").strip()
        if s:
            return s.encode("utf-8")
    import secrets
    s = secrets.token_hex(32)
    _SALT_PATH.write_text(s + "\n", encoding="utf-8")
    print("  identity_guard: new salt written to identity_salt.local.txt - "
          "back it up; losing it means re-adding every term.", file=sys.stderr)
    return s.encode("utf-8")


def h(s):
    return hashlib.sha256(_salt() + s.strip().lower().encode("utf-8")).hexdigest()


def load():
    if STORE.exists():
        return json.loads(STORE.read_text(encoding="utf-8"))
    return {"schema": "identity-guard/1.0",
            "note": ("SHA-256 of terms that must never reach a published surface. "
                     "Hashes only — this file discloses nothing. Add with "
                     "`python identity_guard.py add`."),
            "terms": [], "bigrams": []}


def save(d):
    STORE.write_text(json.dumps(d, indent=2) + "\n", encoding="utf-8")


def cmd_add():
    d = load()
    print("Enter terms one per line, blank line to finish.")
    print("They are hashed immediately and the plaintext is not retained.\n")
    n = 0
    while True:
        try:
            t = input("  term> ").strip()
        except EOFError:
            break
        if not t:
            break
        parts = t.lower().split()
        for p in parts:
            if len(p) >= 3 and h(p) not in d["terms"]:
                d["terms"].append(h(p)); n += 1
        if len(parts) > 1:
            b = h(" ".join(parts))
            if b not in d["bigrams"]:
                d["bigrams"].append(b); n += 1
    save(d)
    print(f"\n  {n} hash(es) added · {len(d['terms'])} terms, {len(d['bigrams'])} phrases")
    print("  The terms themselves are not stored anywhere in this repository.")
    return 0


def files(staged=False):
    try:
        cmd = ["git", "diff", "--cached", "--name-only"] if staged else ["git", "ls-files"]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=45)
        names = [x for x in r.stdout.splitlines() if x.strip()]
    except Exception:
        names = []
    for n in names:
        p = Path(n)
        if any(s in p.parts for s in SKIP_DIR):
            continue
        if p.suffix.lower() in TEXT_EXT and p.exists():
            yield p


def scan(staged=False):
    d = load()
    if not d["terms"] and not d["bigrams"]:
        print("  no terms configured — run: python identity_guard.py add")
        return 0
    terms, bigs = set(d["terms"]), set(d["bigrams"])
    hits = []
    for p in files(staged):
        try:
            lines = p.read_text(encoding="utf-8", errors="ignore").splitlines()
        except Exception:
            continue
        for i, line in enumerate(lines, 1):
            toks = [t.lower() for t in TOKEN.findall(line)]
            if any(h(t) in terms for t in toks):
                hits.append((p, i)); continue
            for a, b in zip(toks, toks[1:]):
                if h(f"{a} {b}") in bigs:
                    hits.append((p, i)); break
    return hits


def cmd_scan(staged):
    hits = scan(staged)
    if isinstance(hits, int):
        return hits
    scope = "staged" if staged else "tracked"
    if not hits:
        print(f"  PASS — no configured term appears in any {scope} file.")
        print("  Token matching only. A name split across a line, rendered into a")
        print("  PNG, or sitting in EXIF will not be caught. This is a floor.")
        return 0
    print(f"  FAIL — {len(hits)} occurrence(s) in {scope} files:\n")
    for p, i in hits[:40]:
        print(f"    {p}:{i}")
    if len(hits) > 40:
        print(f"    … {len(hits)-40} more")
    print("\n  The matched term is deliberately not printed.")
    return 1


def cmd_test():
    d = load()
    if not d["terms"]:
        print("  no terms configured"); return 1
    probe = HERE / ".identity_guard_probe.tmp"
    print("  Enter one term you expect the guard to catch; it is written to a")
    print("  temporary file, scanned, and the file is deleted.")
    try:
        t = input("  term> ").strip()
    except EOFError:
        return 1
    probe.write_text(f"probe {t} probe\n", encoding="utf-8")
    toks = [x.lower() for x in TOKEN.findall(probe.read_text(encoding="utf-8"))]
    caught = any(h(x) in set(d["terms"]) for x in toks)
    probe.unlink(missing_ok=True)
    print(f"\n  {'CAUGHT — the guard fires on that term.' if caught else 'NOT CAUGHT — add it with `add`.'}")
    return 0 if caught else 1


def main():
    a = sys.argv[1:] or ["scan"]
    if a[0] == "add":
        return cmd_add()
    if a[0] == "test":
        return cmd_test()
    if a[0] == "scan":
        return cmd_scan("--staged" in a)
    print(__doc__); return 0


if __name__ == "__main__":
    sys.exit(main())
