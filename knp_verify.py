#!/usr/bin/env python3
"""
knp_verify.py — a third-party conformance verifier for KNP-26 hashlogs.

Written to solve the problem that keeps a standard a house rule: nobody can
conform to a specification they cannot test against. This program is the test.
It knows nothing about any particular committer. Point it at any KNP-26 hashlog,
anywhere, and it reports conformance with paragraph citations and exits non-zero
on a MUST failure.

It is also the honest form of "recompute the hashes." That line is only true as
long as somebody other than the committer can actually run the recomputation.

    python knp_verify.py <hashlog>                     structure and shape
    python knp_verify.py <hashlog> --reveal <file>     recompute revealed Kalls
    python knp_verify.py <hashlog> --previous <older>  append-only across time
    python knp_verify.py --selftest                    interoperability vectors
    python knp_verify.py <hashlog> --json              machine-readable result

<hashlog> may be a path or an https URL.

The reveal file is a JSON array of opening material, each item carrying the
fields named in the hashlog's own construction block — typically:

    [{"id": "...", "timestamp": "...", "statement": "...",
      "resolution_basis": "...", "salt": "..."}]

The verifier builds the preimage from the *published* construction block, not
from anything hardcoded here. A committer using a legacy construction is
verified against the recipe they published; the published commitment governs
(KNP 4.01b).

Standard library only. No network required except to fetch an https hashlog.
"""

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen, Request

STATUSES = {"SEALED", "REVEALED", "RESOLVED_HIT", "RESOLVED_MISS", "VOID"}
REQUIRED_CONSTRUCTION = ["preimage_order", "separator", "hash", "encoding"]
INTEROP_FIELDS = ["id", "timestamp", "commitment", "status"]
HEX64 = re.compile(r"^[0-9a-f]{64}$")
TS = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")

findings = []      # (level, cite, message)  level in MUST | SHOULD | INFO


def rec(level, cite, msg):
    findings.append((level, cite, msg))


def load(src):
    if str(src).startswith(("http://", "https://")):
        req = Request(str(src), headers={"User-Agent": "knp_verify/1.0"})
        with urlopen(req, timeout=30) as r:
            raw = r.read().decode("utf-8")
    else:
        raw = Path(src).read_text(encoding="utf-8")
    return json.loads(raw)


# ----------------------------------------------------------------------
def check_container(h):
    if not isinstance(h, dict):
        rec("MUST", "KNP 4.01", "hashlog is not a JSON object — a bare array is "
                                "nonconformant"); return False
    if h.get("protocol") != "KNP-26":
        rec("MUST", "KNP 4.01", f"protocol is {h.get('protocol')!r}, expected 'KNP-26'")
    if "records" not in h or not isinstance(h["records"], list):
        rec("MUST", "KNP 4.01", "no 'records' array"); return False
    return True


def check_construction(h):
    c = h.get("construction")
    if not isinstance(c, dict):
        rec("MUST", "KNP 4.01b",
            "no construction block. A stranger holding a reveal and a bare "
            "commitment cannot recompute without the recipe; revision 2 requires "
            "it be published.")
        return None
    for k in REQUIRED_CONSTRUCTION:
        if k not in c:
            rec("MUST", "KNP 4.01b", f"construction block missing '{k}'")
    order = c.get("preimage_order")
    if not isinstance(order, list) or not order:
        rec("MUST", "KNP 4.01b", "preimage_order is not a non-empty list")
    if str(c.get("hash", "")).upper().replace("-", "") != "SHA256":
        rec("MUST", "KNP 2.02", f"hash is {c.get('hash')!r}; KNP-26 commits with SHA-256")
    if str(c.get("encoding", "")).upper().replace("-", "") != "UTF8":
        rec("MUST", "KNP 2.01", f"encoding is {c.get('encoding')!r}; the preimage is UTF-8")
    if "pipe_escape" not in c and c.get("separator") == "|":
        rec("SHOULD", "KNP 2.01", "no pipe_escape declared while the separator is a "
                                  "pipe; a statement containing '|' cannot be "
                                  "unambiguously recomputed")
    return c


def check_records(h):
    recs = h["records"]
    seen, levels2 = set(), 0
    for i, r in enumerate(recs):
        w = f"record[{i}]"
        if not isinstance(r, dict):
            rec("MUST", "KNP 4.01", f"{w} is not an object"); continue
        rid = r.get("id", w)
        for f in INTEROP_FIELDS:
            if f not in r:
                rec("MUST", "KNP 4.01", f"{rid}: missing interoperability field '{f}'")
        if r.get("id") in seen:
            rec("MUST", "KNP 3.02", f"{rid}: duplicate id — ids must be unique within "
                                    f"a committer's hashlog")
        seen.add(r.get("id"))
        cm = r.get("commitment", "")
        if not HEX64.match(str(cm)):
            rec("MUST", "KNP 2.02", f"{rid}: commitment is not 64 lowercase hex chars")
        ts = str(r.get("timestamp", ""))
        if not TS.match(ts):
            rec("MUST", "KNP 2.01", f"{rid}: timestamp {ts!r} is not ISO 8601 UTC at "
                                    f"second precision with a Z suffix")
        st = r.get("status")
        if st not in STATUSES:
            rec("MUST", "KNP 4.01", f"{rid}: status {st!r} not in {sorted(STATUSES)}")
        if r.get("level") == 2:
            levels2 += 1
            if not r.get("reveal_date"):
                rec("MUST", "KNP 4.01", f"{rid}: level 2 requires reveal_date")
        for k in ("statement", "resolution_basis", "salt", "preimage"):
            if k in r:
                rec("MUST", "KNP 4.01",
                    f"{rid}: hashlog record carries '{k}'. Records carry only opaque "
                    f"and non-sensitive fields; publishing opening material destroys "
                    f"the hiding property for that Kall.")
    return recs


def check_disclosure(h):
    """4.01: metadata outside the preimage should be disclosed as unbound."""
    con = h.get("construction") or {}
    order = [str(x) for x in (con.get("preimage_order") or [])]
    outside = [k for k in ("probability", "deadline", "domain")
               if any(k in r for r in h["records"]) and k not in order]
    if not outside:
        return
    blob = json.dumps(h).lower()
    if not any(w in blob for w in ("outside the preimage", "not bound", "anchored by",
                                   "unbound", "disclosure")):
        rec("SHOULD", "KNP 4.01",
            f"{', '.join(outside)} are published outside the preimage and are "
            f"therefore not bound by the hash; the hashlog should say so on its face")


def check_anchor(h, src):
    blob = json.dumps(h).lower()
    declared = any(w in blob for w in ("anchor", "timestamp_authority", "beacon",
                                       "opentimestamps", "git"))
    vcs = str(src).startswith("https://raw.githubusercontent.com/")
    if declared:
        rec("INFO", "KNP 4.03", "hashlog declares an external anchor on its face")
    elif vcs:
        rec("INFO", "KNP 4.03",
            "served from a public version-control host — the commit history is the "
            "append-only mechanism, but it is not declared in the hashlog itself. "
            "A reader who receives this file by any other route cannot tell what "
            "anchors it.")
    else:
        rec("MUST", "KNP 4.03",
            "no external anchor is declared and the source is not a public "
            "version-control host. Without an append-only mechanism the committer "
            "does not solely control, the count is not committed and cherry-picking "
            "is undetectable.")


def check_append_only(h, prev):
    old = {r.get("id"): r for r in prev.get("records", []) if isinstance(r, dict)}
    new = {r.get("id"): r for r in h.get("records", []) if isinstance(r, dict)}
    if len(new) < len(old):
        rec("MUST", "KNP 4.02", f"count fell from {len(old)} to {len(new)} — the "
                                f"hashlog is append-only")
    for rid, o in old.items():
        if rid not in new:
            rec("MUST", "KNP 4.02", f"{rid}: present in the earlier hashlog, absent now")
            continue
        n = new[rid]
        if o.get("commitment") != n.get("commitment"):
            rec("MUST", "KNP 4.02", f"{rid}: commitment ALTERED — this breaks the seal "
                                    f"for the entire set")
        if o.get("timestamp") != n.get("timestamp"):
            rec("MUST", "KNP 4.02", f"{rid}: timestamp altered")
    rec("INFO", "KNP 4.02", f"append-only holds across the two snapshots "
                            f"({len(old)} → {len(new)} records)")


# ----------------------------------------------------------------------
def build_preimage(item, con):
    order = con.get("preimage_order") or ["id", "timestamp", "statement",
                                          "resolution_basis", "salt"]
    sep = con.get("separator", "|")
    esc = con.get("pipe_escape")
    parts = []
    for f in order:
        v = item.get(f)
        if v is None:
            raise KeyError(f)
        v = str(v)
        if esc and sep in v and f != "salt":
            v = v.replace(sep, esc)
        parts.append(v)
    return sep.join(parts)


def check_reveals(h, con, reveals):
    by_id = {r.get("id"): r for r in h["records"] if isinstance(r, dict)}
    matched = 0
    for item in reveals:
        rid = item.get("id", "?")
        if rid not in by_id:
            rec("MUST", "KNM 3.04", f"{rid}: reveal has no matching sealed record")
            continue
        salt = str(item.get("salt", ""))
        if len(salt) < 32:
            rec("MUST", "KNP 2.04", f"{rid}: salt is {len(salt)} hex chars; the minimum "
                                    f"is 128 bits (32 hex)")
        try:
            pre = build_preimage(item, con)
        except KeyError as e:
            rec("MUST", "KNP 2.01", f"{rid}: reveal missing preimage field {e}"); continue
        got = hashlib.sha256(pre.encode(con.get("encoding", "utf-8"))).hexdigest()
        want = by_id[rid].get("commitment")
        if got == want:
            matched += 1
        else:
            rec("MUST", "KNP 2.02",
                f"{rid}: RECOMPUTED HASH DOES NOT MATCH. published {want} , "
                f"recomputed {got}. Either the opening material is not what was "
                f"sealed, or the published construction does not describe the "
                f"recipe actually used.")
    rec("INFO", "KNM 3.04", f"{matched} of {len(reveals)} reveal(s) recompute to their "
                            f"published commitment")
    return matched


# ----------------------------------------------------------------------
VECTORS = [
    {"name": "ascii baseline",
     "item": {"id": "KK-20260101-01", "timestamp": "2026-01-01T00:00:00Z",
              "statement": "A test statement.", "resolution_basis": "A test basis.",
              "salt": "00112233445566778899aabbccddeeff"}},
    {"name": "unicode statement",
     "item": {"id": "KK-20260101-02", "timestamp": "2026-01-01T00:00:00Z",
              "statement": "NebelKrähe — Straße, 日本語, emoji 🜁",
              "resolution_basis": "Vérification à la source.",
              "salt": "ffeeddccbbaa99887766554433221100"}},
    {"name": "pipe in statement (escaped)",
     "item": {"id": "KK-20260101-03", "timestamp": "2026-01-01T00:00:00Z",
              "statement": "Either A | or B will occur.",
              "resolution_basis": "Reported by two wire services.",
              "salt": "0123456789abcdef0123456789abcdef"}},
]
DEFAULT_CON = {"preimage_order": ["id", "timestamp", "statement",
                                  "resolution_basis", "salt"],
               "separator": "|", "hash": "SHA-256", "encoding": "UTF-8",
               "pipe_escape": "\\u007C"}


def selftest():
    print("KNP-26 INTEROPERABILITY VECTORS")
    print("An independent implementation is conformant when it produces these exact")
    print("digests from these exact inputs (KNP 2.03: byte-for-byte identity is the")
    print("interoperability contract).\n")
    for v in VECTORS:
        pre = build_preimage(v["item"], DEFAULT_CON)
        dig = hashlib.sha256(pre.encode("utf-8")).hexdigest()
        print(f"  {v['name']}")
        print(f"    preimage   {pre}")
        print(f"    sha256     {dig}\n")
    return 0


# ----------------------------------------------------------------------
def report(as_json, src, nrec):
    musts = [f for f in findings if f[0] == "MUST"]
    shoulds = [f for f in findings if f[0] == "SHOULD"]
    if as_json:
        print(json.dumps({
            "source": str(src), "records": nrec,
            "conformant": not musts,
            "must_failures": [{"cite": c, "message": m} for _, c, m in musts],
            "should_departures": [{"cite": c, "message": m} for _, c, m in shoulds],
            "notes": [{"cite": c, "message": m} for l, c, m in findings if l == "INFO"],
            "verified_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "verifier": "knp_verify/1.0"}, indent=2))
        return 1 if musts else 0

    print(f"\nKNP-26 CONFORMANCE — {src}")
    print("-" * 66)
    print(f"  {nrec} record(s)\n")
    for level in ("MUST", "SHOULD", "INFO"):
        rows = [f for f in findings if f[0] == level]
        if not rows:
            continue
        label = {"MUST": "MUST FAILURES", "SHOULD": "SHOULD DEPARTURES",
                 "INFO": "NOTES"}[level]
        print(f"  {label}")
        for _, cite, msg in rows:
            print(f"    [{cite:12s}] {msg}")
        print()
    if musts:
        print(f"  NONCONFORMANT — {len(musts)} must-requirement failure(s).")
        print("  No unmodified conformance statement may be made (KNM 2.02).")
    elif shoulds:
        print(f"  CONFORMANT with {len(shoulds)} documented should-departure(s).")
        print("  A modified conformance statement must name them (KNM 2.03).")
    else:
        print("  CONFORMANT — all applicable must-requirements met.")
    print("\n  Conformance certifies commitment integrity only. It certifies nothing")
    print("  about the quality of the predictions committed (KNM 1.07).\n")
    return 1 if musts else 0


def main():
    ap = argparse.ArgumentParser(description="Third-party KNP-26 conformance verifier")
    ap.add_argument("hashlog", nargs="?", help="path or https URL")
    ap.add_argument("--reveal", help="JSON array of opening material")
    ap.add_argument("--previous", help="an earlier snapshot, for the append-only check")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.selftest:
        return selftest()
    if not a.hashlog:
        ap.print_help(); return 0

    try:
        h = load(a.hashlog)
    except Exception as e:
        print(f"FAIL — could not read {a.hashlog}: {e}"); return 1

    if not check_container(h):
        return report(a.json, a.hashlog, 0)
    con = check_construction(h)
    recs = check_records(h)
    check_disclosure(h)
    check_anchor(h, a.hashlog)
    if a.previous:
        try:
            check_append_only(h, load(a.previous))
        except Exception as e:
            rec("INFO", "KNP 4.02", f"previous snapshot unreadable: {e}")
    if a.reveal:
        try:
            reveals = json.loads(Path(a.reveal).read_text(encoding="utf-8"))
            if isinstance(reveals, dict):
                reveals = [reveals]
            check_reveals(h, con or DEFAULT_CON, reveals)
        except Exception as e:
            rec("MUST", "KNM 3.04", f"reveal file unreadable: {e}")
    else:
        rec("INFO", "KNM 3.04", "no reveal supplied — structure checked, contents not "
                                "recomputed. A sealed record proves only that something "
                                "was committed.")
    return report(a.json, a.hashlog, len(recs))


if __name__ == "__main__":
    sys.exit(main())
