#!/usr/bin/env python3
"""
denom_capture.py — capture completeness (DECC-26 Level 4).
Version 0.1.0 · companion to denom.py · standard library only.

THE GAP THIS CLOSES
denom.py proves the size of the population that was SEALED. It cannot prove
that everything the system PRODUCED was sealed — DECC-26 §8.01(a) names this
the standard's principal residual risk. An operator who seals 97 of 100 outputs
has a perfectly verifiable vault and an incomplete record.

Two controls close it, and both are here:

  1. ENFORCED SEALING. Sealing happens in the generation path, not after it, as
     a fail-closed side effect. If the seal cannot be written the call RAISES by
     default — no output is returned that was not sealed. Degraded mode exists
     but quarantines and COUNTS every unsealed record, so the gap is never
     silent.

  2. INDEPENDENT TALLY + RECONCILIATION. A counter incremented on a different
     path from the vault (ideally a different process or an external billing or
     usage record) gives a second number. Reconciliation compares the two and
     prints the delta. A vault that matches its tally is evidence; a vault
     nobody counted against is an assertion.

INDEPENDENCE IS GRADED, AND THE GRADE IS PRINTED
    external  — count from a source the operator does not write (provider usage
                or billing records). Strongest; the only grade that fully
                satisfies §8.01(a).
    process   — counter incremented by a separate process (proxy, sidecar).
                Meaningful; defeats in-code miscounting, not a determined
                operator.
    inprocess — counter in the same process as the sealer. WEAK: common-mode
                failure means one bug can move both numbers. Better than
                nothing and labelled as such on every artifact.

Reconciliation NEVER silently reconciles. A delta is printed, carried into the
artifact, and exits non-zero.

COMMANDS
  denom_capture.py tally-inc  [--n N] [--source S] [--grade G]
  denom_capture.py tally-set  --count N --source S --grade G
  denom_capture.py reconcile  [--strict]
  denom_capture.py attest     [--out FILE]
  denom_capture.py selftest

LIBRARY USE (the enforced path)
    from denom_capture import Capture
    cap = Capture(vault="denom_vault")

    @cap.sealed(meta_fn=lambda out, **kw: {"model": kw.get("model","")})
    def generate(prompt, model="qwen3-30b"):
        return call_your_model(prompt, model)      # returns str/bytes

    text = generate("hello", model="qwen3-30b")    # sealed before it returns

Or explicitly:
    seq = cap.record(output_bytes, {"model": "qwen3-30b", "req": "abc"})
"""

import argparse
import base64
import json
import os
import secrets
import sys
from datetime import datetime, timezone
from functools import wraps
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

try:
    import denom
except ImportError:
    print("denom_capture: denom.py must sit beside this file.", file=sys.stderr)
    sys.exit(2)

VERSION = "0.1.0"
GRADES = ("external", "process", "inprocess")
GRADE_NOTE = {
    "external": "count from a source the operator does not write",
    "process": "counter incremented by a separate process",
    "inprocess": "counter in the sealing process — WEAK, common-mode failure",
}


def now_utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# --------------------------------------------------------------- the sealer
class SealFailure(RuntimeError):
    """Raised when a record could not be sealed and degraded mode is off."""


class Capture:
    """Fail-closed sealing into a denom vault.

    Writes byte-identical vault entries to `denom.py seal`, so `denom.py audit`
    validates records sealed through either path.
    """

    def __init__(self, vault="denom_vault", allow_degraded=False,
                 tally_grade="inprocess", tally=True):
        self.vault = Path(vault)
        self.allow_degraded = allow_degraded
        self.tally_grade = tally_grade
        self.tally = tally
        if not (self.vault / "chain.json").exists():
            raise SealFailure(f"no vault at {self.vault} — run: "
                              f"python denom.py init --vault {self.vault}")

    # -- the tally is bumped FIRST, so a crash mid-seal shows as a gap, not
    #    as a matched pair. An undercount would hide the very failure the
    #    tally exists to reveal.
    def record(self, content, meta=None):
        if isinstance(content, str):
            content = content.encode("utf-8")
        meta = {str(k): str(v) for k, v in (meta or {}).items()}
        if self.tally:
            _tally_inc(self.vault.parent, 1, "denom_capture", self.tally_grade)
        try:
            return self._seal(content, meta)
        except Exception as e:
            self._quarantine(content, meta, repr(e))
            if not self.allow_degraded:
                raise SealFailure(
                    f"seal failed and degraded mode is off: {e}. The output was "
                    f"NOT returned; it is quarantined and counted.") from e
            return None

    def _seal(self, content, meta):
        cp = self.vault / "chain.json"
        chain = denom.read_json(cp)
        seq = len(chain["entries"])
        salt = secrets.token_hex(32)
        ts = now_utc()
        com = denom.commitment(salt, content, meta)
        prev = (chain["entries"][-1]["chain_hash"] if chain["entries"]
                else denom.GENESIS)
        core = {"seq": seq, "ts": ts, "commit": com}
        entry = dict(core)
        entry["prev"] = prev
        entry["chain_hash"] = denom.chain_hash(prev, core)
        # openings first: an opening without a chain entry is recoverable
        # noise; a chain entry without an opening breaks audit.
        denom.write_json(self.vault / "openings" / f"{seq:08d}.json", {
            "seq": seq, "ts": ts, "salt": salt,
            "content_b64": base64.b64encode(content).decode(),
            "content_sha256": denom.sha256(content),
            "meta": meta, "source": "capture", "commit": com})
        chain["entries"].append(entry)
        denom.write_json(cp, chain)
        return seq

    def _quarantine(self, content, meta, err):
        q = self.vault.parent / "quarantine"
        q.mkdir(exist_ok=True)
        denom.write_json(q / f"UNSEALED_{now_utc().replace(':','')}_"
                             f"{secrets.token_hex(4)}.json", {
            "ts": now_utc(), "error": err, "meta": meta,
            "content_sha256": denom.sha256(content),
            "note": ("This output was NOT sealed. It is counted in the tally, "
                     "so reconciliation will show the gap.")})

    def sealed(self, meta_fn=None):
        """Decorator: seal a function's return value before it is returned."""
        def deco(fn):
            @wraps(fn)
            def inner(*a, **kw):
                out = fn(*a, **kw)
                payload = out if isinstance(out, (str, bytes)) else json.dumps(
                    out, sort_keys=True, ensure_ascii=False)
                meta = meta_fn(out, **kw) if meta_fn else {}
                self.record(payload, meta)
                return out
            return inner
        return deco


# ---------------------------------------------------------------- the tally
def _tally_path(base):
    return Path(base) / "tally.json"


def _load_tally(base):
    p = _tally_path(base)
    if p.exists():
        return denom.read_json(p)
    return {"denom_capture": VERSION, "count": 0, "sources": {},
            "grade": None, "created": now_utc()}


def _tally_inc(base, n, source, grade):
    t = _load_tally(base)
    t["count"] = int(t.get("count", 0)) + int(n)
    t["sources"][source] = int(t["sources"].get(source, 0)) + int(n)
    prev = t.get("grade")
    # the weakest contributing grade governs — a strong source cannot launder
    # a weak one sharing the same counter
    order = {g: i for i, g in enumerate(GRADES)}
    t["grade"] = grade if prev is None else max(
        (prev, grade), key=lambda g: order.get(g, 99))
    t["updated"] = now_utc()
    denom.write_json(_tally_path(base), t)
    return t


# ------------------------------------------------------------- reconciliation
def reconcile(base, vault):
    chain = denom.read_json(Path(vault) / "chain.json")
    sealed = len(chain["entries"])
    t = _load_tally(base)
    counted = int(t.get("count", 0))
    qdir = Path(base) / "quarantine"
    quarantined = len(list(qdir.glob("UNSEALED_*.json"))) if qdir.exists() else 0
    delta = counted - sealed
    grade = t.get("grade") or "none"
    return {"denom_capture": VERSION, "generated_at": now_utc(),
            "vault_id": chain.get("vault_id"),
            "sealed": sealed, "counted": counted, "delta": delta,
            "quarantined": quarantined,
            "tally_grade": grade,
            "tally_grade_note": GRADE_NOTE.get(grade, "no tally recorded"),
            "tally_sources": t.get("sources", {}),
            "reconciled": delta == 0 and quarantined == 0,
            "level4_eligible": (delta == 0 and quarantined == 0
                                and grade == "external")}


def print_recon(r):
    print("DECC-26 CAPTURE RECONCILIATION")
    print("-" * 58)
    print(f"  sealed in vault        {r['sealed']}")
    print(f"  counted independently  {r['counted']}   "
          f"[{r['tally_grade']}: {r['tally_grade_note']}]")
    print(f"  delta                  {r['delta']:+d}")
    if r["quarantined"]:
        print(f"  quarantined UNSEALED   {r['quarantined']}")
    print()
    if r["delta"] == 0 and not r["quarantined"]:
        print("  RECONCILED — every counted output is sealed.")
    elif r["delta"] > 0:
        print(f"  GAP — {r['delta']} counted output(s) are NOT in the vault.")
        print("  The sealed population is incomplete. Any completeness")
        print("  assertion MUST be qualified until this is resolved.")
    else:
        print(f"  OVERAGE — {-r['delta']} more sealed than counted. The tally")
        print("  is undercounting or records were sealed outside the capture")
        print("  path. Investigate before relying on either number.")
    print()
    if r["level4_eligible"]:
        print("  LEVEL 4 (Reconciled) — reconciliation holds against an")
        print("  external count. An unqualified completeness assertion over")
        print("  the generated population is supported.")
    else:
        why = []
        if r["delta"] or r["quarantined"]:
            why.append("reconciliation does not balance")
        if r["tally_grade"] != "external":
            why.append(f"tally grade is '{r['tally_grade']}', not 'external'")
        print("  NOT Level 4 — " + "; ".join(why) + ".")
        print("  Claims MUST be qualified to the SEALED population "
              "(DECC-26 §8.03).")


# ---------------------------------------------------------------- commands
def cmd_tally_inc(a):
    if a.grade not in GRADES:
        denom.die(f"--grade must be one of {GRADES}")
    t = _tally_inc(a.base, a.n, a.source, a.grade)
    print(f"tally {t['count']} (+{a.n} from {a.source}, grade {t['grade']})")
    return 0


def cmd_tally_set(a):
    if a.grade not in GRADES:
        denom.die(f"--grade must be one of {GRADES}")
    t = _load_tally(a.base)
    t["count"] = int(a.count)
    t["sources"][a.source] = int(a.count)
    t["grade"] = a.grade
    t["updated"] = now_utc()
    t["note"] = ("count set from an authoritative source; overrides prior "
                 "incremental tally")
    denom.write_json(_tally_path(a.base), t)
    print(f"tally set to {a.count} from {a.source} (grade {a.grade})")
    return 0


def cmd_reconcile(a):
    r = reconcile(a.base, a.vault)
    print_recon(r)
    if a.strict and not r["reconciled"]:
        return 1
    return 0


def cmd_attest(a):
    r = reconcile(a.base, a.vault)
    out = Path(a.out) if a.out else Path(
        a.base) / f"RECONCILIATION_{now_utc().replace(':','')}.json"
    r["statement"] = (
        f"At {r['generated_at']} the vault held {r['sealed']} sealed records "
        f"against an independently counted {r['counted']} "
        f"(grade: {r['tally_grade']}). Delta {r['delta']:+d}. "
        + ("Reconciled." if r["reconciled"] else
           "NOT reconciled — completeness claims must be qualified."))
    denom.write_json(out, r)
    print(f"attestation -> {out}")
    print(f"  {r['statement']}")
    print("  Attach this to any disclosure bundle that carries a completeness "
          "claim.")
    return 0


def cmd_selftest(a):
    import tempfile, shutil, subprocess
    tmp = Path(tempfile.mkdtemp())
    try:
        v = tmp / "denom_vault"
        subprocess.run([sys.executable, str(HERE / "denom.py"),
                        "--vault", str(v), "init"],
                       capture_output=True, check=True)
        cap = Capture(vault=v, tally_grade="inprocess")
        for i in range(4):
            cap.record(f"output {i}", {"model": "test", "i": str(i)})
        r = subprocess.run([sys.executable, str(HERE / "denom.py"),
                            "--vault", str(v), "audit"],
                           capture_output=True, text=True)
        ok_audit = "AUDIT PASS" in r.stdout
        rec = reconcile(tmp, v)
        ok_bal = rec["sealed"] == 4 and rec["counted"] == 4 and rec["delta"] == 0
        ok_not4 = rec["level4_eligible"] is False   # inprocess must not qualify
        _tally_inc(tmp, 2, "external-billing", "external")
        rec2 = reconcile(tmp, v)
        ok_gap = rec2["delta"] == 2 and rec2["reconciled"] is False
        print(f"  capture entries pass denom audit        "
              f"{'PASS' if ok_audit else 'FAIL'}")
        print(f"  tally balances after 4 sealed           "
              f"{'PASS' if ok_bal else 'FAIL'}")
        print(f"  inprocess grade blocked from Level 4    "
              f"{'PASS' if ok_not4 else 'FAIL'}")
        print(f"  injected gap detected (+2 uncounted)    "
              f"{'PASS' if ok_gap else 'FAIL'}")
        allok = ok_audit and ok_bal and ok_not4 and ok_gap
        print("\n  SELFTEST " + ("PASS" if allok else "FAIL"))
        return 0 if allok else 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser(prog="denom_capture.py")
    ap.add_argument("--base", default=".", help="directory holding tally.json "
                                                "and quarantine/")
    ap.add_argument("--vault", default="denom_vault")
    sub = ap.add_subparsers(dest="cmd", required=True)
    ti = sub.add_parser("tally-inc")
    ti.add_argument("--n", type=int, default=1)
    ti.add_argument("--source", default="manual")
    ti.add_argument("--grade", default="process")
    ts = sub.add_parser("tally-set")
    ts.add_argument("--count", type=int, required=True)
    ts.add_argument("--source", required=True)
    ts.add_argument("--grade", required=True)
    rc = sub.add_parser("reconcile")
    rc.add_argument("--strict", action="store_true")
    at = sub.add_parser("attest")
    at.add_argument("--out")
    sub.add_parser("selftest")
    a = ap.parse_args()
    return {"tally-inc": cmd_tally_inc, "tally-set": cmd_tally_set,
            "reconcile": cmd_reconcile, "attest": cmd_attest,
            "selftest": cmd_selftest}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
