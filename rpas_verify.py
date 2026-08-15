#!/usr/bin/env python3
"""
rpas_verify.py — a third-party conformance verifier for RPAS-26 forecast ledgers.

The sibling of knp_verify.py, pointed at the other commitment surface. It knows
nothing about any particular desk. Point it at any kkr-ledger JSON, anywhere,
and it recomputes every per-entry seal and every publishable figure from the
file alone, reporting conformance with RPAS paragraph citations and exiting
non-zero on a MUST failure.

It is the honest form of "the figures are recomputable." That sentence is only
true while somebody other than the desk can actually run the recomputation.

    python rpas_verify.py <ledger>                      structure, seals, figures
    python rpas_verify.py <ledger> --previous <older>   append-only across time
    python rpas_verify.py --selftest                    construction vectors
    python rpas_verify.py <ledger> --json               machine-readable result

<ledger> may be a path or an https URL.

THE SEAL CONSTRUCTION (RPAS 4.02g, as deployed by candidate_desk.py / kkr.py):
    SHA-256 over the UTF-8 bytes of
        json.dumps({k: entry.get(k) for k in FIELDS}, sort_keys=True,
                   ensure_ascii=False)
    with FIELDS = (statement, resolution, deadline, probability,
                   failure_condition, keyed_keyless, keyed_keyless_rationale,
                   date_issued)
    Missing fields serialize as null. Key order is irrelevant by construction
    (sort_keys); two implementations agree byte-for-byte or one is wrong.

SEALED-STATE RETRY (KK29-SEALCLASS, rpas_verify/1.1): rows are commonly
sealed before their keyed/keyless determination exists (RPAS 1.04/4.03).
On a recompute mismatch this verifier retries with keyed_keyless and
keyed_keyless_rationale forced to null. A match there proves the sealed
state - the determination was absent at seal and written later, which is
the workflow the standard directs, not an edit to sealed material. Such
rows are counted and disclosed as an INFO note under 4.03; only rows
failing BOTH recomputations are 5.06 must-failures.

Entries issued before 2026-07-30 are unsealed by history; the ledger's own
disclosure prints that finding (RPAS 6.04) and this verifier reads it. Entries
issued on or after that date without a seal are a MUST failure. Scores obey the
fifty-entry gate (5.02), travel with their miss counts (5.03), and are never
pooled across arms — a Brier belongs to one forecaster.

Standard library only. No network required except to fetch an https ledger.
"""

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen, Request

FIELDS = ("statement", "resolution", "deadline", "probability",
          "failure_condition", "keyed_keyless", "keyed_keyless_rationale",
          "date_issued")
SEAL_CUTOVER = "2026-07-30"
STATUSES = {"open", "hit", "miss", "void"}
RESOLVED = {"hit", "miss"}
HEX64 = re.compile(r"^[0-9a-f]{64}$")

findings = []          # (level, cite, message)  level in MUST | SHOULD | INFO


def rec(level, cite, msg):
    findings.append((level, cite, msg))


def load(src):
    if str(src).startswith(("http://", "https://")):
        req = Request(str(src), headers={"User-Agent": "rpas_verify/1.1"})
        with urlopen(req, timeout=30) as r:
            raw = r.read().decode("utf-8")
    else:
        raw = Path(src).read_text(encoding="utf-8-sig")
    return json.loads(raw)


def seal_digest(e: dict) -> str:
    payload = json.dumps({k: e.get(k) for k in FIELDS},
                         sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


# ----------------------------------------------------------------------
def check_envelope(h):
    if not isinstance(h, dict):
        rec("MUST", "RPAS 6.03", "ledger is not a JSON object — a bare array "
                                 "cannot state what produced it or when")
        return None
    if not str(h.get("schema", "")).startswith("kkr-ledger/"):
        rec("MUST", "RPAS 6.03", f"schema is {h.get('schema')!r}; expected a "
                                 f"kkr-ledger/* envelope")
    for k in ("generator", "as_of"):
        if not h.get(k):
            rec("SHOULD", "RPAS 6.03", f"envelope lacks '{k}' — a file that cannot "
                                       f"state its own provenance is a file, not "
                                       f"evidence")
    rows = h.get("projections")
    if not isinstance(rows, list):
        rec("MUST", "RPAS 6.03", "no 'projections' array")
        return None
    return rows


def check_entries(rows):
    seen = set()
    for i, e in enumerate(rows):
        w = f"entry[{i}]"
        if not isinstance(e, dict):
            rec("MUST", "RPAS 6.03", f"{w} is not an object"); continue
        rid = e.get("id", w)
        if e.get("id") in seen:
            rec("MUST", "RPAS 4.01", f"{rid}: duplicate id — an amendment is a new, "
                                     f"cross-referenced entry, never a rewrite")
        seen.add(e.get("id"))
        st = e.get("status")
        if st not in STATUSES:
            rec("MUST", "RPAS 6.03", f"{rid}: status {st!r} not in {sorted(STATUSES)}")
        for f, cite in (("statement", "RPAS 4.02a"), ("resolution", "RPAS 4.02b"),
                        ("deadline", "RPAS 4.02c"), ("probability", "RPAS 4.02d")):
            if not str(e.get(f, "")).strip():
                rec("MUST", cite, f"{rid}: missing {f}")
        try:
            p = float(e.get("probability"))
            if not (0 < p < 100):
                rec("MUST", "RPAS 4.02d", f"{rid}: probability {p} is a certainty "
                                          f"claim, not a forecast")
        except (TypeError, ValueError):
            rec("MUST", "RPAS 4.02d", f"{rid}: probability {e.get('probability')!r} "
                                      f"is not numeric")
        if st in RESOLVED and not e.get("resolved_date"):
            rec("SHOULD", "RPAS 6.03", f"{rid}: resolved without a resolved_date — "
                                       f"a third party cannot place the adjudication "
                                       f"in time")


def check_failure_conditions(h, rows):
    """RPAS 4.02e/4.03, aggregated. Post-cutover: always MUST. Pre-cutover:
    conformant-as-disclosed when the ledger prints the finding (6.04)."""
    miss = [e for e in rows
            if not str(e.get("failure_condition", "")).strip()
            or str(e.get("failure_condition", ""))
            .strip().lower().startswith("unset")]
    if not miss:
        return
    post = [e.get("id","?") for e in miss
            if str(e.get("date_issued","")) >= SEAL_CUTOVER]
    pre = len(miss) - len(post)
    if post:
        rec("MUST", "RPAS 4.03", f"{len(post)} entr{'y' if len(post)==1 else 'ies'} "
            f"issued on or after {SEAL_CUTOVER} lack a failure condition and are "
            f"unfalsifiable as issued: {', '.join(post[:6])}")
    if pre:
        disclosed = "4.03" in str(h.get("disclosure","")) or                     "failure" in str(h.get("disclosure","")).lower()
        if disclosed:
            rec("INFO", "RPAS 6.04", f"{pre} pre-{SEAL_CUTOVER} entries lack a "
                f"failure condition and the ledger's own disclosure prints the "
                f"finding — conformant-as-disclosed; the 4.02f window to add one "
                f"before resolution stands open")
        else:
            rec("MUST", "RPAS 4.03", f"{pre} entries lack a failure condition and "
                f"the ledger does not say so on its face")


def check_keying(h, rows):
    """RPAS 4.02f: the keyed/keyless determination is decided before resolution.
    RPAS 4.03: made after resolution, the hit is KEYED by rule."""
    bad = [e for e in rows if e.get("status") in RESOLVED
           and str(e.get("keyed_keyless")) not in ("keyed", "keyless")]
    if not bad:
        return
    hits = sum(1 for e in bad if e.get("status") == "hit")
    disclosed = "4.02f" in str(h.get("disclosure","")) or \
                "keyed" in str(h.get("disclosure","")).lower()
    rec("INFO" if disclosed else "MUST", "RPAS 4.02f",
        f"{len(bad)} resolved entr{'y' if len(bad) == 1 else 'ies'} carry no "
        f"pre-resolution keyed/keyless determination. By RPAS 4.03 the "
        f"{hits} hit(s) among them are KEYED by rule and bear on no faculty "
        f"claim; scores over these entries are calibration arithmetic only. "
        + ("The ledger's own disclosure prints this finding — "
           "conformant-as-disclosed (6.04)." if disclosed else
           "The ledger does not print this finding on its face."))


def check_seals(h, rows):
    ok = mismatch = det_after = 0  # KK29-SEALCLASS
    unsealed_pre, unsealed_post = [], []
    for e in rows:
        s = e.get("seal_sha256")
        if not s:
            (unsealed_post if str(e.get("date_issued", "")) >= SEAL_CUTOVER
             else unsealed_pre).append(e.get("id", "?"))
            continue
        if not HEX64.match(str(s)):
            rec("MUST", "RPAS 4.02g", f"{e.get('id','?')}: seal is not 64 lowercase "
                                      f"hex chars"); continue
        if seal_digest(e) == s:
            ok += 1
            continue
        sealed_state = dict(e)  # KK29-SEALCLASS: test the sealed state
        sealed_state["keyed_keyless"] = None
        sealed_state["keyed_keyless_rationale"] = None
        if seal_digest(sealed_state) == s:
            det_after += 1
        else:
            mismatch += 1
            rec("MUST", "RPAS 5.06",
                f"{e.get('id','?')}: SEAL DOES NOT RECOMPUTE — a pre-registered "
                f"field was edited after sealing, or the construction diverged. "
                f"A retroactive edit to a sealed entry scores as a MISS where "
                f"recoverable and voids the span where not.")
    if unsealed_post:
        rec("MUST", "RPAS 4.02g",
            f"{len(unsealed_post)} entr{'y' if len(unsealed_post)==1 else 'ies'} "
            f"issued on or after {SEAL_CUTOVER} carry no seal: "
            f"{', '.join(unsealed_post[:6])}")
    if unsealed_pre:
        disclosed = "4.02g" in str(h.get("disclosure", "")) or \
                    "seal" in str(h.get("disclosure", "")).lower()
        if disclosed:
            rec("INFO", "RPAS 6.04",
                f"{len(unsealed_pre)} pre-{SEAL_CUTOVER} entries are unsealed and "
                f"the ledger's own disclosure prints the finding — "
                f"conformant-as-disclosed; those entries rest on the anchored "
                f"history (4.04/4.05), not on per-entry commitment")
        else:
            rec("SHOULD", "RPAS 6.04",
                f"{len(unsealed_pre)} entries are unsealed and the ledger does not "
                f"say so on its face — an undisclosed unsealed span is a scope "
                f"limitation the reader is left to discover")
    if det_after:  # KK29-SEALCLASS
        rec("INFO", "RPAS 4.03",
            f"{det_after} seal(s) recompute to their sealed state with the "
            f"keyed/keyless fields at their sealed nulls - the determination "
            f"was written after sealing, as 1.04/4.03 direct. No sealed field "
            f"was edited; the seal proves the determination was absent at "
            f"seal, and the post-seal determination rests on the anchored "
            f"history (4.04/4.05) and 5.07 supersession discipline, not on "
            f"the row seal.")
    if ok or mismatch or det_after:
        rec("INFO", "RPAS 4.02g", f"{ok} seal(s) recompute to their published "
                                  f"digest; {det_after} recompute to their "
                                  f"sealed state (determined after seal); "
                                  f"{mismatch} do not")


def check_anchor(h):
    a = h.get("anchor")
    if not isinstance(a, dict):
        rec("SHOULD", "RPAS 4.04",
            "no anchor is declared on the ledger's face. The commit history may "
            "in fact anchor it (4.04) and a beacon may clock it (4.05), but a "
            "reader receiving this file by any other route cannot tell.")
        return
    mech = str(a.get("mechanism", "")).lower()
    if ("version-control" in mech or "git" in mech) and \
            str(a.get("history", "")).startswith("https://"):
        rec("INFO", "RPAS 4.04", f"anchor resolves to version-control history: "
                                 f"{a['history']}")
    else:
        rec("SHOULD", "RPAS 4.04", "anchor object present but publishes no "
                                   "resolvable history pointer")


def brier_and_bins(res):
    if not res:
        return None, []
    sq = [((float(e["probability"]) / 100.0) -
           (1.0 if e["status"] == "hit" else 0.0)) ** 2 for e in res]
    bins = {}
    for e in res:
        b = min(int(float(e["probability"]) // 10), 9)
        hit = 1 if e["status"] == "hit" else 0
        n, h = bins.get(b, (0, 0))
        bins[b] = (n + 1, h + hit)
    rows = [(f"{b*10:02d}-{b*10+9:02d}%", n, h) for b, (n, h) in sorted(bins.items())]
    return sum(sq) / len(sq), rows


def check_figures(rows):
    """RPAS 5.02: no score before fifty entries — counts only. 5.03: the miss
    count travels with every score. Never pooled: a Brier belongs to one arm."""
    arms = {}
    for e in rows:
        arms.setdefault(e.get("model", "?"), []).append(e)
    total = len(rows)
    if total < 50:
        rec("INFO", "RPAS 5.02", f"ledger holds {total} entries — under the "
                                 f"fifty-entry gate, counts are the only "
                                 f"reportable figures")
    for arm in sorted(arms):
        es = arms[arm]
        res = [e for e in es if e.get("status") in RESOLVED]
        hits = sum(1 for e in res if e["status"] == "hit")
        void = sum(1 for e in es if e.get("status") == "void")
        line = (f"{arm}: issued {len(es)} · open "
                f"{sum(1 for e in es if e.get('status') == 'open')} · void {void} "
                f"· resolved {len(res)} · H/M {hits}/{len(res)-hits}")
        if total >= 50 and res:
            b, bins = brier_and_bins(res)
            line += f" · Brier {b:.4f}"
            if len(res) < 30:
                line += (f" — under thirty resolved this figure is noise, not "
                         f"evidence of anything")
        rec("INFO", "RPAS 5.03", line)
    rec("INFO", "RPAS 5.04", "no pooled score is computed by this verifier — "
                             "a Brier belongs to one forecaster; pooling launders "
                             "the weaker record into the stronger")


def check_append_only(h, prev):
    old = {e.get("id"): e for e in prev.get("projections", [])
           if isinstance(e, dict)}
    new = {e.get("id"): e for e in h.get("projections", [])
           if isinstance(e, dict)}
    if len(new) < len(old):
        rec("MUST", "RPAS 4.01", f"entry count fell from {len(old)} to {len(new)} "
                                 f"— nothing leaves the record")
    for rid, o in old.items():
        if rid not in new:
            rec("MUST", "RPAS 5.06", f"{rid}: present in the earlier ledger, absent "
                                     f"now — a silently dropped entry scores as a "
                                     f"MISS and voids the span where unrecoverable")
            continue
        n = new[rid]
        for f in FIELDS:
            # The 4.02f window, as the ledger's own disclosure grants it: a
            # failure condition, keyed/keyless determination, or its rationale
            # may be ADDED to a still-open entry (empty -> value). Changing an
            # existing value, or touching any other pre-registered field, is
            # the cheap cheat and fails.
            fillable = (f in ("keyed_keyless", "failure_condition",
                              "keyed_keyless_rationale")
                        and str(o.get(f) or "").strip() in ("", "None", "unset")
                        and o.get("status") == "open")
            if o.get(f) != n.get(f) and not fillable:
                rec("MUST", "RPAS 4.01", f"{rid}: pre-registered field '{f}' changed "
                                         f"after issue ({o.get(f)!r} -> {n.get(f)!r})")
        if o.get("seal_sha256") and o.get("seal_sha256") != n.get("seal_sha256"):
            rec("MUST", "RPAS 5.06", f"{rid}: seal ALTERED between snapshots")
        if o.get("status") in RESOLVED and n.get("status") != o.get("status"):
            rec("MUST", "RPAS 5.06", f"{rid}: resolved status changed "
                                     f"({o.get('status')} -> {n.get('status')}) — "
                                     f"resolutions do not reverse; a correction is "
                                     f"a new, cross-referenced entry")
    rec("INFO", "RPAS 4.01", f"append-only examined across the two snapshots "
                             f"({len(old)} → {len(new)} entries)")


# ----------------------------------------------------------------------
def selftest():
    print("RPAS-26 SEAL CONSTRUCTION VECTOR")
    print("An independent implementation is conformant when it produces this exact")
    print("digest from this exact entry (byte-for-byte identity over the sorted-JSON")
    print("payload is the interoperability contract).\n")
    v = {"statement": "A test entry.", "resolution": "A named public instrument.",
         "deadline": "2026-12-31", "probability": 35,
         "failure_condition": "The instrument reports otherwise.",
         "keyed_keyless": "keyless",
         "keyed_keyless_rationale": "No prior sufficient to deduce it.",
         "date_issued": "2026-07-30"}
    d = seal_digest(v)
    payload = json.dumps({k: v.get(k) for k in FIELDS}, sort_keys=True,
                         ensure_ascii=False)
    print(f"  payload  {payload}")
    print(f"  sha256   {d}\n")
    shuffled = dict(reversed(list(v.items())))
    same = seal_digest(shuffled) == d
    print(f"  key-order invariance (sort_keys): {'PASS' if same else 'FAIL'}")
    missing = dict(v); missing.pop("keyed_keyless_rationale")
    stable = HEX64.match(seal_digest(missing)) is not None
    print(f"  absent-field-serializes-as-null:  {'PASS' if stable else 'FAIL'}")
    u = dict(v, statement="NebelKrähe — Straße, 日本語.")
    raw = json.dumps({k: u.get(k) for k in FIELDS}, sort_keys=True,
                     ensure_ascii=False).encode("utf-8")
    esc = json.dumps({k: u.get(k) for k in FIELDS}, sort_keys=True,
                     ensure_ascii=True).encode("utf-8")
    pin = hashlib.sha256(raw).hexdigest() != hashlib.sha256(esc).hexdigest()
    print(f"  ensure_ascii=False is load-bearing: {'PASS' if pin else 'FAIL'}")
    print("  (an implementation that escapes non-ASCII will disagree with the desk")
    print("   on every unicode entry — this pin is what catches it)")
    return 0 if (same and stable and pin) else 1


def report(as_json, src, nrec):
    musts = [f for f in findings if f[0] == "MUST"]
    shoulds = [f for f in findings if f[0] == "SHOULD"]
    if as_json:
        print(json.dumps({
            "source": str(src), "entries": nrec,
            "conformant": not musts,
            "must_failures": [{"cite": c, "message": m} for _, c, m in musts],
            "should_departures": [{"cite": c, "message": m} for _, c, m in shoulds],
            "notes": [{"cite": c, "message": m} for l, c, m in findings if l == "INFO"],
            "verified_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "verifier": "rpas_verify/1.1"}, indent=2))
        return 1 if musts else 0
    print(f"\nRPAS-26 CONFORMANCE — {src}")
    print("-" * 66)
    print(f"  {nrec} entr{'y' if nrec == 1 else 'ies'}\n")
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
        print("  No unmodified conformance statement may be made (RPAS 2.02).")
    elif shoulds:
        print(f"  CONFORMANT with {len(shoulds)} documented should-departure(s).")
        print("  A modified conformance statement must name them (RPAS 2.03).")
    else:
        print("  CONFORMANT — all applicable must-requirements met.")
    print("\n  Conformance certifies process, never foresight (RPAS 1.06). Only the")
    print("  resolved, misfire-inclusive record converts a signature into a claim.\n")
    return 1 if musts else 0


def main():
    ap = argparse.ArgumentParser(description="Third-party RPAS-26 ledger verifier")
    ap.add_argument("ledger", nargs="?", help="path or https URL")
    ap.add_argument("--previous", help="an earlier snapshot, for the append-only check")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.ledger:
        ap.print_help(); return 0
    try:
        h = load(a.ledger)
    except Exception as e:
        print(f"FAIL — could not read {a.ledger}: {e}"); return 1
    rows = check_envelope(h)
    if rows is None:
        return report(a.json, a.ledger, 0)
    check_entries(rows)
    check_failure_conditions(h, rows)
    check_keying(h, rows)
    check_seals(h, rows)
    check_anchor(h)
    check_figures(rows)
    if a.previous:
        try:
            check_append_only(h, load(a.previous))
        except Exception as e:
            rec("INFO", "RPAS 4.01", f"previous snapshot unreadable: {e}")
    return report(a.json, a.ledger, len(rows))


if __name__ == "__main__":
    sys.exit(main())
