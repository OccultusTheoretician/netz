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

Revision 3 additions. A hashlog may publish a `construction_history` (KNP
4.01c): every construction ever used, keyed by version, with each record
naming its own via a `construction` field (absent = the log's earliest). A
reveal is recomputed under the construction its record names. `probability`
inside a preimage renders canonically as the integer percent (KNP 2.01b).
Across two snapshots, a change to a sealed record's `probability` or
`deadline` is a MUST failure identical in class to an altered commitment
(KNP 4.02) — restating a probability downward on a row heading toward a miss
is the cheap cheat, and this is where a stranger catches it. The external
anchor is tested structurally (KNP 4.03b): an object that resolves, not a
word that appears. The standing line is recomputed from the records and any
published line that disagrees fails (KNP 4.04).

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


def _validate_con(c, where):
    for k in REQUIRED_CONSTRUCTION:
        if k not in c:
            rec("MUST", "KNP 4.01b", f"{where} missing '{k}'")
    order = c.get("preimage_order")
    if not isinstance(order, list) or not order:
        rec("MUST", "KNP 4.01b", f"{where}: preimage_order is not a non-empty list")
    if str(c.get("hash", "")).upper().replace("-", "") != "SHA256":
        rec("MUST", "KNP 2.02", f"{where}: hash is {c.get('hash')!r}; KNP-26 commits "
                                f"with SHA-256")
    if str(c.get("encoding", "")).upper().replace("-", "") != "UTF8":
        rec("MUST", "KNP 2.01", f"{where}: encoding is {c.get('encoding')!r}; the "
                                f"preimage is UTF-8")
    if "pipe_escape" not in c and c.get("separator") == "|":
        rec("SHOULD", "KNP 2.01", f"{where}: no pipe_escape declared while the separator "
                                  f"is a pipe; a statement containing '|' cannot be "
                                  f"unambiguously recomputed")


def check_construction(h):
    """Returns (singular_construction, history_map). history_map is
    version -> construction and always contains at least the singular block."""
    c = h.get("construction")
    if not isinstance(c, dict):
        rec("MUST", "KNP 4.01b",
            "no construction block. A stranger holding a reveal and a bare "
            "commitment cannot recompute without the recipe; revision 2 requires "
            "it be published.")
        return None, {}
    _validate_con(c, "construction block")
    hist = {}
    hraw = h.get("construction_history")
    if hraw is not None:
        if not isinstance(hraw, list) or not all(isinstance(b, dict) for b in hraw):
            rec("MUST", "KNP 4.01c", "construction_history is not a list of objects")
            hraw = []
        for b in hraw:
            ver = b.get("version")
            if not ver:
                rec("MUST", "KNP 4.01c", "construction_history entry lacks a version")
                continue
            _validate_con(b, f"construction_history[{ver}]")
            hist[ver] = b
    default_ver = c.get("version") or (sorted(hist)[0] if hist else "knp-1")
    hist.setdefault(default_ver, c)
    # Every construction a record names must be published in the history.
    named = {str(r.get("construction")) for r in h.get("records", [])
             if isinstance(r, dict) and r.get("construction")}
    for ver in sorted(named - set(hist)):
        rec("MUST", "KNP 4.01c",
            f"records name construction {ver!r} but the hashlog publishes no such "
            f"entry in construction_history — those records cannot be recomputed "
            f"by a stranger")
    if len({v for v in named} | {default_ver}) > 1 and hraw is None:
        rec("MUST", "KNP 4.01c", "records are sealed under more than one construction "
                                 "but no construction_history is published")
    return c, hist


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
    """KNP 4.03b (rev. 3): the anchor is an object that resolves, not a word that
    appears. A hashlog stating 'we anchor by vibes' no longer passes."""
    a = h.get("anchor")
    vcs = str(src).startswith("https://raw.githubusercontent.com/")
    if not isinstance(a, dict):
        msg = ("no structured anchor object is published. Without an append-only "
               "mechanism the committer does not solely control, the count is not "
               "committed and cherry-picking is undetectable.")
        if vcs:
            msg += (" (Served from a public version-control host, which may in fact "
                    "anchor it — but a reader receiving this file by any other route "
                    "cannot tell, and prose is not a declaration.)")
        rec("MUST", "KNP 4.03b", msg)
        return
    mech = str(a.get("mechanism", "")).lower()
    if not mech:
        rec("MUST", "KNP 4.03b", "anchor object lacks a 'mechanism'")
        return
    resolvable = False
    if "version-control" in mech or "git" in mech:
        repo, hist = a.get("repository"), a.get("history")
        if not (isinstance(repo, str) and repo.startswith("https://")):
            rec("MUST", "KNP 4.03b", "version-control anchor lacks a resolvable "
                                     "'repository' URL")
        elif not (isinstance(hist, str) and hist.startswith("https://")):
            rec("MUST", "KNP 4.03b", "version-control anchor lacks a resolvable "
                                     "'history' URL — the history IS the anchor")
        else:
            resolvable = True
            rec("INFO", "KNP 4.03b", f"anchor resolves to version-control history: "
                                     f"{hist}")
    ts = a.get("rfc3161") or a.get("timestamp_token")
    if isinstance(ts, dict):
        tok, dig = ts.get("token"), str(ts.get("sha256", ""))
        if not tok or not HEX64.match(dig):
            rec("MUST", "KNP 4.03c", "timestamp anchor declared without a token "
                                     "location and a 64-hex covered digest")
        else:
            resolvable = True
            rec("INFO", "KNP 4.03c",
                f"RFC 3161 token declared over sha256 {dig[:16]}…; a reader verifies "
                f"with: openssl ts -verify -digest {dig} -sha256 -in {tok} "
                f"-CAfile <tsa-ca.pem>")
    elif "rfc3161" in mech or "timestamp" in mech:
        rec("MUST", "KNP 4.03c", "mechanism names a timestamping authority but no "
                                 "token object is published")
    if not resolvable and mech:
        rec("MUST", "KNP 4.03b",
            f"anchor mechanism {mech!r} publishes no pointer this verifier "
            f"recognizes as resolvable (version-control repository+history URLs, "
            f"or an rfc3161 token+digest object)")
    if "rfc3161" not in json.dumps(a).lower() and "timestamp_token" not in a:
        rec("SHOULD", "KNP 4.03c",
            "no external timestamp token is declared. Version-control history "
            "anchors the sequence; a timestamp token from an authority the "
            "committer cannot amend anchors existence. Hashlogs first published "
            "after revision 3 must carry one.")


def check_standing(h):
    """KNP 4.04 (rev. 3): the standing line is a derivation, not a self-report."""
    recs = [r for r in h.get("records", []) if isinstance(r, dict)]
    resolved = sum(1 for r in recs if str(r.get("status", "")).startswith("RESOLVED"))
    revealed = sum(1 for r in recs if r.get("status") == "REVEALED") + resolved
    line = f"{len(recs)} sealed · {revealed} revealed · {resolved} resolved"
    rec("INFO", "KNP 4.04", f"standing line, recomputed from the records: {line}")
    asserted = h.get("standing")
    if asserted is None:
        return
    nums = [int(n) for n in re.findall(r"\d+", str(asserted))][:3]
    if nums != [len(recs), revealed, resolved]:
        rec("MUST", "KNP 4.04",
            f"published standing line {asserted!r} disagrees with the recomputation "
            f"({line}) — the visible denominator is being asserted, not derived")


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
        for f in ("probability", "deadline"):
            if f in o and str(o.get(f)) != str(n.get(f)):
                rec("MUST", "KNP 4.02",
                    f"{rid}: {f} altered after sealing ({o.get(f)!r} -> {n.get(f)!r}). "
                    f"Deletion was never the efficient cheat — restating the {f} is, "
                    f"and it is a failure identical in class to an altered commitment.")
        if o.get("construction") != n.get("construction"):
            rec("MUST", "KNP 2.01b", f"{rid}: construction reassigned after sealing")
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
        if f == "probability":
            v = str(int(round(float(v))))     # KNP 2.01b: canonical integer percent
        else:
            v = str(v)
        if esc and sep in v and f != "salt":
            v = v.replace(sep, esc)
        parts.append(v)
    return sep.join(parts)


def check_reveals(h, con, hist, reveals):
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
        # KNP 2.01b/4.01c: recompute under the construction the sealed record names.
        ver = by_id[rid].get("construction") or item.get("construction")
        rcon = hist.get(ver, con) if ver else con
        if ver and ver not in hist:
            rec("MUST", "KNP 4.01c", f"{rid}: names construction {ver!r} which the "
                                     f"hashlog does not publish"); continue
        try:
            pre = build_preimage(item, rcon)
        except KeyError as e:
            rec("MUST", "KNP 2.01", f"{rid}: reveal missing preimage field {e}"); continue
        got = hashlib.sha256(pre.encode(rcon.get("encoding", "utf-8"))).hexdigest()
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

V2_CON = {"version": "knp-2",
          "preimage_order": ["id", "timestamp", "statement", "resolution_basis",
                             "probability", "deadline", "salt"],
          "separator": "|", "hash": "SHA-256", "encoding": "UTF-8",
          "pipe_escape": "\\u007C"}

V2_VECTORS = [
    {"name": "knp-2 baseline (probability and deadline bound)",
     "item": {"id": "KK-20260729-91", "timestamp": "2026-07-29T00:00:00Z",
              "statement": "A test statement.", "resolution_basis": "A test basis.",
              "probability": 35, "deadline": "2026-12-31",
              "salt": "00112233445566778899aabbccddeeff"}},
    {"name": "knp-2 canonical probability (35.0 and '35' hash identically to 35)",
     "item": {"id": "KK-20260729-92", "timestamp": "2026-07-29T00:00:00Z",
              "statement": "Canonicalization test.", "resolution_basis": "KNP 2.01b.",
              "probability": "35.0", "deadline": "2026-12-31",
              "salt": "ffeeddccbbaa99887766554433221100"}},
    {"name": "knp-2 pipe in statement (escaped)",
     "item": {"id": "KK-20260729-93", "timestamp": "2026-07-29T00:00:00Z",
              "statement": "Either A | or B will occur.",
              "resolution_basis": "Reported by two wire services.",
              "probability": 5, "deadline": "2030-07-25",
              "salt": "0123456789abcdef0123456789abcdef"}},
]


def selftest():
    print("KNP-26 INTEROPERABILITY VECTORS")
    print("An independent implementation is conformant when it produces these exact")
    print("digests from these exact inputs (KNP 2.03: byte-for-byte identity is the")
    print("interoperability contract).\n")
    print("construction knp-1 (KNP 2.01)\n")
    for v in VECTORS:
        pre = build_preimage(v["item"], DEFAULT_CON)
        dig = hashlib.sha256(pre.encode("utf-8")).hexdigest()
        print(f"  {v['name']}")
        print(f"    preimage   {pre}")
        print(f"    sha256     {dig}\n")
    print("construction knp-2 (KNP 2.01b — probability and deadline bound)\n")
    for v in V2_VECTORS:
        pre = build_preimage(v["item"], V2_CON)
        dig = hashlib.sha256(pre.encode("utf-8")).hexdigest()
        print(f"  {v['name']}")
        print(f"    preimage   {pre}")
        print(f"    sha256     {dig}\n")
    a = hashlib.sha256(build_preimage(V2_VECTORS[0]["item"], V2_CON)
                       .encode("utf-8")).hexdigest()
    b = hashlib.sha256(build_preimage(dict(V2_VECTORS[0]["item"], probability="35"),
                                      V2_CON).encode("utf-8")).hexdigest()
    print(f"  canonicalization invariant: int 35 == str '35' under knp-2: "
          f"{'PASS' if a == b else 'FAIL'}\n")
    return 0 if a == b else 1


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
            "verifier": "knp_verify/1.1"}, indent=2))
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
    con, hist = check_construction(h)
    recs = check_records(h)
    check_disclosure(h)
    check_anchor(h, a.hashlog)
    check_standing(h)
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
            check_reveals(h, con or DEFAULT_CON, hist, reveals)
        except Exception as e:
            rec("MUST", "KNM 3.04", f"reveal file unreadable: {e}")
    else:
        rec("INFO", "KNM 3.04", "no reveal supplied — structure checked, contents not "
                                "recomputed. A sealed record proves only that something "
                                "was committed.")
    return report(a.json, a.hashlog, len(recs))


if __name__ == "__main__":
    sys.exit(main())
