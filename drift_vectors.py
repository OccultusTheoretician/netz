#!/usr/bin/env python3
"""drift_vectors.py - DRIFT-26 Chapter 13: the known-answer vectors.

Six fixtures, each a synthetic record (ledger.json + arms.json) built deterministically
from a fixed seed, run through the desk's OWN estimator (warte_report.py, the file the
registration pins) so that the expected report is the desk's output, not this script's
arithmetic. A conforming implementation reproduces every figure and every check verdict.

  (i)   clean      an arm at the floor; every check passes; H1/H2/H3 read; no version pair (H4 untestable)
  (ii)  drift      a version pair whose 70-80 and 80-90 deciles differ by more than the wider interval
  (ii-b) nodrift   a version pair whose deciles agree within the intervals
  (iii) ctlfail    the base-rate control priced far from the outcome rate; check (e) fails; the read halts
  (iv)  mirrorgap  one frontier row with no same-run control; check (a) lists it; the read halts
  (v)   corrected  a corrected determination: superseded value carried, correction counted
  (vi)  voids      voids counted out of denominators and beside them

Usage:
  python drift_vectors.py build  --estimator path/to/warte_report.py --out DRIFT_26_VECTORS
  python drift_vectors.py verify --estimator path/to/warte_report.py --vectors DRIFT_26_VECTORS

build writes, per fixture: ledger.json, arms.json, expected.json (the estimator's report with
volatile fields removed), expected_exit.txt. It also writes index.json with the estimator's
LF-SHA-256 and every fixture's ledger hash. verify rebuilds nothing: it runs the given estimator
over each stored fixture and diffs against expected.json field by field, reporting every
divergence. Exit 0 on full agreement.
"""
import argparse
import hashlib
import json
import os
import random
import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

SEED = 26
RUBRIC = hashlib.sha256(b"DRIFT-26 fixture rubric\n").hexdigest()          # the cohort hash
PACKET = "kkr_packet_2026-01-15_1500.md"
T0 = datetime(2026, 1, 15, 15, 0, tzinfo=timezone.utc)
ARMS = {"A": "manual/fable-5/unattested", "B": "manual/fable-5.1/unattested", "C": "control/baserate"}
VOLATILE = ("generated", "self_sha256", "self_sha256_raw", "written", "path", "ledger_as_of")


def arms_json():
    return {"arms": [
        {"tag": ARMS["A"], "lane": "manual", "model": "claude-fable-5", "access": "unattested", "status": "active"},
        {"tag": ARMS["B"], "lane": "manual", "model": "claude-fable-5-1", "access": "unattested", "status": "active"},
        {"tag": ARMS["C"], "lane": "control", "model": "climatological", "access": "n-a", "status": "active"},
    ]}


def lf_sha(p: Path):
    return hashlib.sha256(p.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


class Builder:
    def __init__(self, seed=SEED):
        self.rng = random.Random(seed)
        self.rows = []
        self.n = 0

    def _id(self):
        self.n += 1
        return "DRIFT-%04d" % self.n

    def arm_row(self, arm, prob, hit, minute, seat="jury-claude", det="keyed", domain="political",
                void=False, superseded=None, mirror=True, mirror_prob=None, mirror_gap_min=3):
        sealed = T0 + timedelta(minutes=minute)
        rid = self._id()
        row = {"id": rid, "model": arm, "statement": "fixture claim %s" % rid, "domain": domain,
               "probability": int(prob), "resolution": "fixture resolution %s" % rid,
               "failure_condition": "fixture failure %s" % rid, "deadline": "2026-02-15",
               "citations": [1], "source_packet": PACKET, "source_report": "battle_report_2026-01-15_1500.md",
               "date_issued": "2026-01-15", "sealed_at": sealed.isoformat(),
               "rubric_hash": RUBRIC, "status": "void" if void else ("hit" if hit else "miss"),
               "resolved_date": "2026-02-16", "keyed_keyless": det,
               "keyed_keyless_dated": "2026-02-16", "keyed_keyless_rationale": "fixture"}
        if seat == "jury-claude":
            row["audit"] = {"mode": "blind-jury", "basis": "claude", "verdicts": {"claude": row["status"].upper(), "qwen": row["status"].upper()}}
        elif seat == "jury-divergent":
            row["audit"] = {"mode": "blind-jury", "basis": "operator", "verdicts": {"claude": "HIT", "qwen": "MISS"}}
        if superseded:
            row["keyed_keyless_superseded"] = superseded
            row["keyed_keyless_corrected"] = "2026-02-20"
        self.rows.append(row)
        if mirror:
            cid = self._id()
            self.rows.append({"id": cid, "model": ARMS["C"], "is_control": True,
                              "statement": row["statement"], "domain": domain,
                              "probability": int(mirror_prob if mirror_prob is not None else 36),
                              "resolution": row["resolution"], "failure_condition": row["failure_condition"],
                              "deadline": row["deadline"], "citations": [1], "source_packet": PACKET,
                              "source_report": row["source_report"], "date_issued": "2026-01-15",
                              "sealed_at": (sealed + timedelta(minutes=mirror_gap_min)).isoformat(),
                              "rubric_hash": RUBRIC, "status": row["status"], "resolved_date": row["resolved_date"],
                              "control_basis": {"arm": ARMS["C"], "rule": "climatological", "rate": 0.36,
                                                "n": 100, "basis": "global", "control_for": rid}})
        return row

    def ledger(self):
        return {"as_of": "2026-02-21T00:00:00Z", "schema": "kkr-ledger/1.1", "projections": self.rows}


def deciles_plan(rng, hits_per_bin):
    """(prob, hit) rows: 20 per bin, with EXACT hit counts per bin so the realized base rate is an
    exact integer percent (a control priced at that percent then has skill exactly zero on the full
    set, and check (e) is not decided by rounding)."""
    plan = []
    for (lo, hi), hits in hits_per_bin.items():
        outcomes = [True] * hits + [False] * (20 - hits)
        rng.shuffle(outcomes)
        for h in outcomes:
            plan.append((rng.randint(lo, hi - 1), h))
    rng.shuffle(plan)
    return plan


BINS6 = [(20, 30), (30, 40), (40, 50), (60, 70), (70, 80), (80, 90)]
HITS_A = dict(zip(BINS6, [5, 7, 9, 13, 15, 17]))        # 66 of 120 -> 0.55 exactly
HITS_B_SAME = dict(HITS_A)
HITS_B_DRIFT = dict(zip(BINS6, [15, 17, 9, 13, 5, 7]))  # same total 66; top and bottom deciles swapped
CTL_PRICE = 55


def build_fixture(name, out: Path, estimator: Path):
    rng = random.Random(SEED)
    b = Builder()
    planA = deciles_plan(rng, HITS_A)
    for i, (p, h) in enumerate(planA):
        det = "keyless" if i % 12 in (0, 3, 5, 7, 9) else "keyed"
        seat = "jury-claude" if i % 7 else ("operator" if i % 14 else "jury-divergent")
        kw = {}
        if name == "mirrorgap" and i == 17:
            kw["mirror_gap_min"] = 7 * 60      # a late mirror: sealed seven hours after its arm row
        if name == "corrected" and i in (4, 21):
            kw["superseded"] = "keyless" if det == "keyed" else "keyed"
        b.arm_row(ARMS["A"], p, h, minute=i, seat=seat, det=det,
                  domain="economics/markets" if i % 5 == 0 else "political",
                  mirror_prob=(12 if name == "ctlfail" else CTL_PRICE), **kw)
    if name == "voids":
        for i in range(3):
            b.arm_row(ARMS["A"], 55, True, minute=300 + i, void=True, mirror_prob=CTL_PRICE)
    if name in ("drift", "nodrift"):
        planB = deciles_plan(random.Random(SEED + 1), HITS_B_DRIFT if name == "drift" else HITS_B_SAME)
        for i, (p, h) in enumerate(planB):
            det = "keyless" if i % 12 in (1, 4, 6, 8, 10) else "keyed"
            b.arm_row(ARMS["B"], p, h, minute=400 + i, seat="jury-claude", det=det, mirror_prob=CTL_PRICE)
    fx = out / name
    if fx.exists():
        shutil.rmtree(fx)
    fx.mkdir(parents=True)
    (fx / "ledger.json").write_text(json.dumps(b.ledger(), indent=1) + "\n", encoding="utf-8")
    (fx / "arms.json").write_text(json.dumps(arms_json(), indent=1) + "\n", encoding="utf-8")
    (fx / "cite_integrity_latest.json").write_text('{"rows": []}\n', encoding="utf-8")
    (fx / "docs").mkdir()
    (fx / "docs" / "KALIBRIERWARTE_REGISTERED_REPORT_v3.md").write_text("fixture registration placeholder\n", encoding="utf-8")
    return fx


def run_estimator(estimator: Path, fx: Path):
    fx = fx.resolve()
    local = fx / "warte_report.py"
    shutil.copyfile(estimator, local)
    env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")
    r = subprocess.run([sys.executable, str(local), "--cohort", RUBRIC[:8], "--json"], cwd=str(fx),
                       capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=600, env=env)
    local.unlink()
    out = r.stdout
    # the report JSON is printed as a block whose first line is exactly "{"; the human
    # face above it contains dict reprs, so anchor on the line, not the first brace
    lines = out.split("\n")
    rep = None
    for i, line in enumerate(lines):
        if line.strip() == "{":
            try:
                rep = json.loads("\n".join(lines[i:]))
                break
            except json.JSONDecodeError:
                continue
    return r.returncode, rep, out


def scrub(o):
    if isinstance(o, dict):
        return {k: scrub(v) for k, v in o.items() if k not in VOLATILE}
    if isinstance(o, list):
        return [scrub(x) for x in o]
    return o


def diff(a, b, path=""):
    out = []
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b:
                out.append("%s.%s: %s" % (path, k, "missing in expected" if k not in a else "missing in actual"))
            else:
                out.extend(diff(a[k], b[k], path + "." + k))
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            out.append("%s: length %d vs %d" % (path, len(a), len(b)))
        for i, (x, y) in enumerate(zip(a, b)):
            out.extend(diff(x, y, "%s[%d]" % (path, i)))
    elif a != b:
        out.append("%s: expected %r, actual %r" % (path, a, b))
    return out


FIXTURES = ["clean", "drift", "nodrift", "ctlfail", "mirrorgap", "corrected", "voids"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["build", "verify"])
    ap.add_argument("--estimator", required=True)
    ap.add_argument("--out", default="DRIFT_26_VECTORS")
    ap.add_argument("--vectors", default="DRIFT_26_VECTORS")
    a = ap.parse_args()
    est = Path(a.estimator).resolve()
    if a.cmd == "build":
        out = Path(a.out)
        out.mkdir(parents=True, exist_ok=True)
        index = {"standard": "DRIFT-26 rev0 (draft)", "estimator_lf_sha256": lf_sha(est), "seed": SEED,
                 "rubric_hash": RUBRIC, "fixtures": {}}
        for name in FIXTURES:
            fx = build_fixture(name, out, est)
            rc, rep, raw = run_estimator(est, fx)
            (fx / "expected.json").write_text(json.dumps(scrub(rep), indent=1, sort_keys=True) + "\n", encoding="utf-8")
            (fx / "expected_exit.txt").write_text("%d\n" % rc, encoding="utf-8")
            (fx / "estimator_stdout.txt").write_text(raw, encoding="utf-8")
            index["fixtures"][name] = {"ledger_lf_sha256": lf_sha(fx / "ledger.json"), "exit": rc,
                                       "rows": len(json.loads((fx / "ledger.json").read_text())["projections"])}
            print("%-10s exit %d  rows %3d  %s" % (name, rc, index["fixtures"][name]["rows"], summary(rep)))
        (out / "index.json").write_text(json.dumps(index, indent=1) + "\n", encoding="utf-8")
        print("index -> %s" % (out / "index.json"))
        return 0
    vec = Path(a.vectors)
    bad = 0
    for name in FIXTURES:
        fx = vec / name
        if not fx.exists():
            print("%-10s MISSING" % name); bad += 1; continue
        rc, rep, raw = run_estimator(est, fx)
        exp = json.loads((fx / "expected.json").read_text(encoding="utf-8"))
        exp_rc = int((fx / "expected_exit.txt").read_text().strip())
        d = diff(exp, scrub(rep))
        ok = (rc == exp_rc) and not d
        print("%-10s %s  exit %d (expected %d)  %d divergence(s)" % (name, "PASS" if ok else "FAIL", rc, exp_rc, len(d)))
        for line in d[:8]:
            print("      " + line)
        bad += 0 if ok else 1
    print("DRIFT-26 vectors: %d of %d fixtures reproduce" % (len(FIXTURES) - bad, len(FIXTURES)))
    return 1 if bad else 0


def summary(rep):
    if not rep:
        return "(no report parsed)"
    try:
        arms = rep.get("arms", {})
        a = next((v for k, v in arms.items() if k.startswith(ARMS["A"])), {})
        q = a.get("quality", {})
        halted = a.get("halted") or rep.get("_meta", {}).get("halted")
        checks = ",".join(k[0] for k, v in q.items() if isinstance(v, dict) and v.get("pass") is False)
        h = a.get("hypotheses") or {}
        comps = (h.get("H4_version_drift") or {}).get("comparators") or []
        h4s = (comps[0].get("result") or "-")[:40] if comps else ("halted" if a.get("note") else "-")
        return "resolved %s | failed checks: %s | H4: %s" % (a.get("resolved", a.get("n")), checks or "none", h4s)
    except Exception as ex:
        return "(summary error %s)" % ex


if __name__ == "__main__":
    sys.exit(main())
