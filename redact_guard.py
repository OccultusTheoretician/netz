#!/usr/bin/env python3
"""redact_guard.py -- GUARDREDACT-2026-09-01 (v2, GUARDGATE-2026-09-01 adds --arm)

Redact configured identity terms from named files, in place, using
identity_guard's own salted hashes and token grammar. The term is never
printed, logged or written by this program; files come back with each hit
replaced by [withheld] and a dated note appended, and are re-scanned before
the program says so.

WHY. The guard refuses to publish a file carrying a configured term, and
that is correct. Generated served surfaces (the battle report and its renders)
pull third-party news and model prose every day, so they will carry such a
term some days. The remedy for a served record is redaction in the current
tree with a dated note (KK24 disposition), never a history rewrite and never a
narrower guard. This is that remedy as a tool, and redact_text() is what the
report writer imports to do it at write time.

    python redact_guard.py FILE [FILE ...]          redact in place, note dated today
    python redact_guard.py --check FILE [FILE ...]  report counts only, write nothing
    python redact_guard.py --arm FILE [FILE ...]    arm files: redact in place, move the
                                                    original to originals/ (gitignored,
                                                    local custody), append a derivative
                                                    entry to anchor_log.json chaining to
                                                    the original's sha

Exit 0 when every named file is clean after the pass; 1 otherwise.
"""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import identity_guard as IG  # noqa: E402  (h, load, TOKEN)

MASK = "[withheld]"


def _sets():
    d = IG.load()
    return set(d.get("terms", [])), set(d.get("bigrams", []))


def redact_line(line: str, terms: set, bigs: set) -> tuple[str, int]:
    """Replace every configured token (and both halves of a configured bigram)
    in one line. Returns (new_line, hits)."""
    spans = [(m.start(), m.end(), m.group(0).lower()) for m in IG.TOKEN.finditer(line)]
    kill = set()
    for i, (_s, _e, tok) in enumerate(spans):
        if IG.h(tok) in terms:
            kill.add(i)
    for i in range(len(spans) - 1):
        if IG.h(f"{spans[i][2]} {spans[i + 1][2]}") in bigs:
            kill.add(i); kill.add(i + 1)
    if not kill:
        return line, 0
    out = line
    for i in sorted(kill, reverse=True):
        s, e, _ = spans[i]
        out = out[:s] + MASK + out[e:]
    return out, len(kill)


def redact_text(text: str, terms=None, bigs=None) -> tuple[str, int]:
    """Redact a whole text. Line endings are preserved."""
    if terms is None or bigs is None:
        terms, bigs = _sets()
    total = 0
    parts = text.splitlines(keepends=True)
    for i, ln in enumerate(parts):
        body = ln.rstrip("\r\n"); tail = ln[len(body):]
        new, n = redact_line(body, terms, bigs)
        if n:
            parts[i] = new + tail; total += n
    return "".join(parts), total


def process_arm(path, log_path=None, originals_dir=None, _redact=None):
    """GUARDGATE-2026-09-01: identity policy for arm files.

    Redacts the file in place; the ORIGINAL bytes move to originals/ (gitignored,
    local custody, AU-C 230 retention); anchor_log.json gains a derivative entry
    whose sha256 is the redacted bytes and whose derived_from is the original's
    sha256 - the sha arrive.py anchored when the file landed. The A1 lane follows
    that chain and its disclosure names the original's receipt as covering the
    original bytes. Returns (hits, derivative_sha_or_None)."""
    import hashlib
    import json as _json
    from datetime import datetime, timezone
    p = Path(path)
    raw = p.read_bytes()
    text = raw.decode("utf-8", errors="surrogateescape")
    rt = _redact or redact_text
    new, n = rt(text)
    if n == 0:
        print(f"  {p.name}: clean; nothing moved")
        return 0, None
    osha = hashlib.sha256(raw).hexdigest()
    od = Path(originals_dir) if originals_dir else HERE / "originals"
    od.mkdir(exist_ok=True)
    dest = od / p.name
    if dest.exists():
        dest = od / (p.name + "." + osha[:8])
    dest.write_bytes(raw)
    p.write_bytes(new.encode("utf-8", errors="surrogateescape"))
    nsha = hashlib.sha256(p.read_bytes()).hexdigest()
    lp = Path(log_path) if log_path else HERE / "anchor_log.json"
    try:
        log = _json.loads(lp.read_text(encoding="utf-8")) if lp.exists() else []
        if not isinstance(log, list):
            raise ValueError("anchor log is not a list")
    except Exception:
        print(f"  {p.name}: anchor log unreadable - redaction done, DERIVATIVE ENTRY NOT WRITTEN; fix the log")
        return n, None
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if not any(isinstance(e, dict) and e.get("sha256") == osha for e in log):
        log.append({"file": dest.name, "sha256": osha, "bytes": len(raw),
                    "arrived_utc": now, "receipt": None,
                    "stamp_state": "unstamped (entered custody at redaction; not swept on landing)"})
    log.append({"file": p.name, "sha256": nsha, "bytes": p.stat().st_size,
                "arrived_utc": now, "derived_from": osha, "receipt": None,
                "stamp_state": "derivative",
                "note": ("identity-policy redaction; original bytes in local custody "
                         "(originals/); the original's receipt covers the original digest")})
    lp.write_text(_json.dumps(log, indent=1, ensure_ascii=True) + "\n", encoding="utf-8")
    print(f"  {p.name}: {n} token(s) withheld; original -> {dest} (sha {osha[:16]}); "
          f"derivative sha {nsha[:16]} logged")
    return n, nsha


def _note(path: Path, n: int, when: str) -> str:
    if path.suffix.lower() in (".html", ".htm"):
        return f"\n<!-- identity policy: {n} token(s) withheld on {when}; the term list is hashed and never printed -->\n"
    return f"\n\n*identity policy: {n} token(s) withheld on {when}; the term list is hashed and never printed.*\n"


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check = "--check" in sys.argv
    arm = "--arm" in sys.argv
    if not args:
        print(__doc__); return 2
    terms, bigs = _sets()
    if not terms and not bigs:
        print("redact_guard: no terms configured; nothing to do"); return 0
    when = date.today().isoformat()
    dirty = 0
    if arm:
        for a in args:
            p = Path(a)
            if not p.exists():
                print(f"  {a}: not found"); dirty += 1; continue
            _n, _sha = process_arm(p)
            _again, left = redact_text(p.read_text(encoding="utf-8", errors="surrogateescape"), terms, bigs)
            if left:
                print(f"  {a}: RE-SCAN NOT CLEAN ({left} left)"); dirty += 1
            if _n and _sha is None:
                dirty += 1
        return 1 if dirty else 0
    for a in args:
        p = Path(a)
        if not p.exists():
            print(f"  {a}: not found"); dirty += 1; continue
        raw = p.read_bytes()
        text = raw.decode("utf-8", errors="surrogateescape")
        new, n = redact_text(text, terms, bigs)
        if check or n == 0:
            print(f"  {a}: {n} hit(s)" + ("" if n == 0 else " (not written, --check)"))
            dirty += (n > 0)
            continue
        note = _note(p, n, when)
        if p.suffix.lower() in (".html", ".htm") and "</body>" in new:
            new = new.replace("</body>", note + "</body>", 1)
        else:
            new = new + note
        p.write_bytes(new.encode("utf-8", errors="surrogateescape"))
        _again, left = redact_text(p.read_text(encoding="utf-8", errors="surrogateescape"), terms, bigs)
        print(f"  {a}: {n} token(s) withheld; re-scan {'clean' if left == 0 else f'{left} left'}")
        dirty += (left > 0)
    return 1 if dirty else 0


if __name__ == "__main__":
    sys.exit(main())
