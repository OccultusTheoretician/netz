#!/usr/bin/env python3
"""warte_report.py - KALIBRIERWARTE REGISTERED REPORT. The estimators.

Implements Section 7 of docs/KALIBRIERWARTE_REGISTERED_REPORT_v3.md on top
of warte.py's figures, unchanged: Brier, base rate, climatological floor,
skill and the ten-decile reliability table are computed exactly as warte.py
computes them (same bins, same floors, same era bucketing from arms.json).
This file adds what the registration reserved for it:

  bootstrap percentile intervals, 95%, 2,000 resamples of the arm's
  resolved rows (unit = row, with replacement), seed 26: Brier, skill,
  each decile's observed frequency, and the keyless-minus-keyed Brier
  difference (from the same resamples);
  the adjudication-seat re-cut: operator / jury, searched seat adopted /
  jury, divergence - read from the row's own audit record;
  voids out of every denominator and counted beside it;
  corrected determinations: current value used, superseded value kept,
  the count of corrected rows in scope printed;
  quality checks (a)-(f), outcome-neutral, all evaluated before any
  hypothesis is read; a failure prints and halts the read;
  H1-H5 at an arm's first checkpoint only (50 resolved within one cohort).

Read-only against ledger.json, arms.json, cite_integrity_latest.json.
Report-only by default: every figure prints. --write writes
forecasts/warte_report_<date>.json through runguard. No number reaches a
page that is not in that file.

Floors are law, not options. Under 50 resolved within the cohort an arm
gets counts (and, from 30, an interim read with the noise line that is
not a result of this registration). There is no flag that lowers them.

Seat derivation (the registration names three seats; the ledger records
them in the row's audit dict): no audit record -> operator (hand-ruled);
audit.mode == blind-jury and basis == claude -> jury, searched seat
adopted; audit.mode == blind-jury and any other basis -> jury, divergence
(the operator ruled where the seats diverged or the searched seat was
AMBIGUOUS). Rows carrying the 2026-08-01 single-auditor record (an
'auditor' key, no 'mode') are a fourth class, auditor-single, printed as
outside the registration's three; all of them are cohort 0.

Mirror pairing for check (a): control_basis.control_for when present
(baserate.py writes it only when pairing from the ledger); otherwise the
control row that shares resolution, deadline and source_packet with the
arm row (the --pair path composes before ids exist). A mirror sealed more
than SAME_RUN_MINUTES after its arm row is a late mirror, listed. Check (a)
binds frontier rows by the registration's own text; for a local or control
arm it prints coverage and does not gate the read.

Self-hash: --self-hash prints this file's SHA-256 over LF-normalised bytes
(the desk-wide served-bytes convention) and over the raw bytes. The
LF-normalised digest is the one the registration pins.
"""
import argparse
import hashlib
import json
import math
import random
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
INSTRUMENT = "warte_report/1.0"
REGISTRATION = "docs/KALIBRIERWARTE_REGISTERED_REPORT_v3.md"

# warte.py, verbatim
N_FLOOR_ARM = 10
N_FLOOR_BIN = 5
BINS = [(0, 10), (10, 20), (20, 30), (30, 40), (40, 50),
        (50, 60), (60, 70), (70, 80), (80, 90), (90, 101)]

# registration, Sections 7 and 8
BOOT_N = 2000
BOOT_SEED = 26
CHECKPOINT = 50
INTERIM = 30
H3_FLOOR = 20
H5_FLOOR = 30
TOP_BINS = ("70-80", "80-90", "90-100")
SAME_RUN_MINUTES = 360

FRONTIER = {"manual/fable-5/unattested", "manual/opus-5/unattested",
            "manual/sonnet-5/unattested"}
CONTROL = "control/baserate"
MARKET = "control/market-implied"
CAPABILITY_OUT = {"operator/human", "kfk/halflife", "fogsim/scenario"}
DEFAULT_COHORT = "4ea5ab8f"
MARKET_DOMAINS = {"market", "markets", "economic", "economy", "finance",
                  "financial", "commodity", "commodities", "crypto"}


def lf_sha256(path):
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def bin_label(lo, hi):
    return "%d-%d" % (lo, hi - 1 if hi == 101 else hi)


def bin_of(p100):
    for lo, hi in BINS:
        if lo <= p100 < hi:
            return bin_label(lo, hi)
    return None


def pct(vals, q):
    """Percentile with linear interpolation between order statistics."""
    s = sorted(vals)
    if not s:
        return None
    k = (len(s) - 1) * q
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return s[int(k)]
    return s[f] + (s[c] - s[f]) * (k - f)


def ci95(vals):
    if not vals:
        return None
    return [round(pct(vals, 0.025), 4), round(pct(vals, 0.975), 4)]


def r3(x):
    return None if x is None else round(x, 3)


def seat_of(row):
    a = row.get("audit") or {}
    if not a:
        return "operator"
    if a.get("mode") == "blind-jury":
        return ("jury-searched-adopted" if a.get("basis") == "claude"
                else "jury-divergence")
    if "auditor" in a:
        return "auditor-single"
    return None


def det_of(row):
    d = str(row.get("keyed_keyless", "")).strip().lower()
    return d if d in ("keyed", "keyless") else "keyed-by-rule"


def point(rs):
    """warte.py's tile figures, unchanged."""
    n = len(rs)
    if n == 0:
        return {"resolved": 0}
    hits = sum(1 for r in rs if r["status"] == "hit")
    ps = [float(r.get("probability", 0)) / 100.0 for r in rs]
    ys = [1.0 if r["status"] == "hit" else 0.0 for r in rs]
    brier = sum((a - b) ** 2 for a, b in zip(ps, ys)) / n
    base = hits / n
    clim = base * (1 - base)
    skill = None if clim == 0 else 1.0 - brier / clim
    bins = []
    for lo, hi in BINS:
        sub = [(a, b) for a, b in zip(ps, ys) if lo <= a * 100 < hi]
        if not sub:
            continue
        bn = len(sub)
        bins.append({"bin": bin_label(lo, hi), "n": bn,
                     "mean_p": round(sum(a for a, _ in sub) / bn, 3),
                     "obs": (round(sum(b for _, b in sub) / bn, 3)
                             if bn >= N_FLOOR_BIN else None),
                     "note": None if bn >= N_FLOOR_BIN else "n<%d" % N_FLOOR_BIN})
    return {"resolved": n, "hits": hits, "misses": n - hits,
            "brier": round(brier, 3), "base_rate": round(base, 3),
            "climatological": round(clim, 3),
            "skill": (round(skill, 3) if skill is not None and n >= N_FLOOR_ARM
                      else None),
            "skill_unfloored": r3(skill),
            "n_floor": (None if n >= N_FLOOR_ARM else
                        "insufficient n (%d<%d) - printed, not hidden" % (n, N_FLOOR_ARM)),
            "bins": bins}


def bootstrap(rs, seed=BOOT_SEED, reps=BOOT_N):
    """Percentile bootstrap over the arm's resolved rows, unit = row.

    Returns intervals for Brier, skill, each decile's observed frequency
    (over the resamples in which the decile is non-empty; that count is
    printed) and the keyless-minus-keyed Brier difference (over the
    resamples in which both splits are non-empty).
    """
    n = len(rs)
    if n == 0:
        return {}
    rng = random.Random(seed)
    pre = [(float(r.get("probability", 0)) / 100.0,
            1.0 if r["status"] == "hit" else 0.0,
            bin_of(float(r.get("probability", 0))),
            det_of(r)) for r in rs]
    briers, skills, diffs = [], [], []
    binobs = defaultdict(list)
    for _ in range(reps):
        idx = [rng.randrange(n) for _ in range(n)]
        s = [pre[i] for i in idx]
        b = sum((p - y) ** 2 for p, y, _, _ in s) / n
        base = sum(y for _, y, _, _ in s) / n
        clim = base * (1 - base)
        briers.append(b)
        if clim > 0:
            skills.append(1.0 - b / clim)
        acc = defaultdict(lambda: [0.0, 0])
        for p, y, lab, _ in s:
            acc[lab][0] += y
            acc[lab][1] += 1
        for lab, (sy, sn) in acc.items():
            binobs[lab].append(sy / sn)
        kd = [(p, y) for p, y, _, d in s if d == "keyed" or d == "keyed-by-rule"]
        kl = [(p, y) for p, y, _, d in s if d == "keyless"]
        if kd and kl:
            bk = sum((p - y) ** 2 for p, y in kd) / len(kd)
            bl = sum((p - y) ** 2 for p, y in kl) / len(kl)
            diffs.append(bl - bk)
    out = {"reps": reps, "seed": seed, "unit": "row",
           "brier_ci95": ci95(briers),
           "skill_ci95": ci95(skills), "skill_resamples": len(skills),
           "bins": {lab: {"ci95": ci95(v), "resamples_nonempty": len(v)}
                    for lab, v in binobs.items()},
           "keyless_minus_keyed_brier_ci95": ci95(diffs),
           "diff_resamples": len(diffs)}
    return out


def split_metrics(rs, defective):
    out = {}
    for lab in ("keyed", "keyless"):
        sub = [r for r in rs if det_of(r) == lab]
        m = point(sub)
        m["defect_ids"] = sorted(defective & {r["id"] for r in sub})
        out[lab] = m
    out["keyed_by_rule"] = sum(1 for r in rs if det_of(r) == "keyed-by-rule")
    if out["keyed"]["resolved"] and out["keyless"]["resolved"]:
        out["keyless_minus_keyed_brier"] = round(
            out["keyless"]["brier"] - out["keyed"]["brier"], 3)
    return out


def seat_cut(rs):
    out = {}
    for lab in ("operator", "jury-searched-adopted", "jury-divergence",
                "auditor-single"):
        sub = [r for r in rs if seat_of(r) == lab]
        m = point(sub)
        if m["resolved"] >= N_FLOOR_ARM:
            b = bootstrap(sub)
            m["brier_ci95"] = b["brier_ci95"]
            m["skill_ci95"] = b["skill_ci95"]
        out[lab] = m
    out["unclassified"] = sum(1 for r in rs if seat_of(r) is None)
    return out


def mirrors_for(arm_rows, controls):
    """Pair each arm row with its control mirror. Returns per-row records."""
    by_for = {}
    for c in controls:
        f = (c.get("control_basis") or {}).get("control_for")
        if f:
            by_for.setdefault(f, []).append(c)
    by_key = defaultdict(list)
    for c in controls:
        by_key[(c.get("resolution"), c.get("deadline"),
                c.get("source_packet"))].append(c)
    recs = []
    for r in arm_rows:
        cands = by_for.get(r["id"]) or by_key.get(
            (r.get("resolution"), r.get("deadline"), r.get("source_packet"))) or []
        if not cands:
            recs.append({"id": r["id"], "mirror": None, "gap_min": None,
                         "class": "no-mirror"})
            continue
        c = cands[0]
        gap = None
        try:
            a = datetime.fromisoformat(str(r.get("sealed_at")))
            b = datetime.fromisoformat(str(c.get("sealed_at")))
            gap = round(abs((b - a).total_seconds()) / 60.0, 1)
        except Exception:
            pass
        cls = ("same-run" if gap is not None and gap <= SAME_RUN_MINUTES
               else "late-mirror" if gap is not None else "gap-unknown")
        recs.append({"id": r["id"], "mirror": c["id"], "gap_min": gap,
                     "class": cls,
                     "pairing": "control_for" if r["id"] in by_for else "key"})
    return recs


def quality(bucket, tag, scope_rows, all_rows_bucket, cohort_full, controls,
            control_rows_cohort, control_rows_all):
    q = {}
    res = [r for r in scope_rows if r["status"] in ("hit", "miss")]
    voids = [r for r in scope_rows if r["status"] == "void"]
    # (a) mirror completeness
    recs = mirrors_for(res, controls)
    cls = Counter(x["class"] for x in recs)
    binding = tag in FRONTIER
    listed = [x for x in recs if x["class"] != "same-run"]
    q["a_mirror_completeness"] = {
        "binding": binding,
        "rows_checked": len(recs), "same_run": cls.get("same-run", 0),
        "late_mirror": cls.get("late-mirror", 0),
        "no_mirror": cls.get("no-mirror", 0),
        "gap_unknown": cls.get("gap-unknown", 0),
        "same_run_minutes": SAME_RUN_MINUTES,
        "listed": listed,
        "result": ("PASS" if not binding or not listed else "FAIL"),
        "note": ("binds frontier rows (Section 7a); the local arm's coverage is printed, not gated"
                 if not binding else "every frontier row in scope needs a same-run mirror; gaps listed")}
    # (b) rubric coverage
    bad = [r["id"] for r in scope_rows if r.get("rubric_hash") != cohort_full]
    q["b_rubric_coverage"] = {"rows": len(scope_rows), "carrying_cohort_hash":
                              len(scope_rows) - len(bad), "off_hash": bad,
                              "result": "PASS" if not bad else "FAIL"}
    # (c) seat recorded
    seats = Counter(seat_of(r) or "UNCLASSIFIED" for r in res)
    q["c_seat_recorded"] = {"resolved": len(res), "seats": dict(seats),
                            "outside_registration": seats.get("auditor-single", 0),
                            "result": "PASS" if not seats.get("UNCLASSIFIED") else "FAIL"}
    # (d) determination coverage
    dets = Counter(det_of(r) for r in res)
    q["d_determination_coverage"] = {"resolved": len(res), "keyed": dets.get("keyed", 0),
                                     "keyless": dets.get("keyless", 0),
                                     "keyed_by_rule": dets.get("keyed-by-rule", 0),
                                     "result": "PASS"}
    # (e) control/baserate skill against its own base rate
    def ctl(rows):
        m = point(rows)
        if m["resolved"] == 0:
            return {"resolved": 0, "result": "UNTESTABLE"}
        b = bootstrap(rows)
        lo, hi = b["skill_ci95"] if b["skill_ci95"] else (None, None)
        inc = (lo is not None and lo <= 0.0 <= hi)
        return {"resolved": m["resolved"], "hits": m["hits"],
                "brier": m["brier"], "base_rate": m["base_rate"],
                "climatological": m["climatological"],
                "skill": m["skill_unfloored"], "skill_ci95": b["skill_ci95"],
                "under_arm_floor": m["resolved"] < N_FLOOR_ARM,
                "result": "PASS" if inc else "FAIL"}
    e_c = ctl(control_rows_cohort)
    e_all = ctl(control_rows_all)
    e_all["label"] = "exploratory - all cohorts pooled, the face's figure"
    q["e_control_skill_zero"] = {"within_cohort": e_c, "all_time_exploratory": e_all,
                                 "result": e_c["result"] if e_c["result"] != "UNTESTABLE" else "FAIL",
                                 "note": ("by construction the interval includes zero; a departure is a defect in the control"
                                          if e_c["result"] == "PASS" else
                                          "departure - the control's reference class is not the control's own base rate; prints as a defect")}
    # (f) void rate
    tot = len(res) + len(voids)
    q["f_void_rate"] = {"resolved": len(res), "voids": len(voids),
                        "void_rate": (round(len(voids) / tot, 3) if tot else None),
                        "result": "PASS"}
    q["all_pass"] = all(q[k]["result"] == "PASS" for k in
                        ("a_mirror_completeness", "b_rubric_coverage", "c_seat_recorded",
                         "d_determination_coverage", "e_control_skill_zero", "f_void_rate"))
    return q


def hypotheses(bucket, tag, m, b, sp, cohort_rows, buckets_in_cohort, reg):
    h = {}
    # H1
    clear = [x for x in m["bins"] if x["bin"] in TOP_BINS and x["n"] >= N_FLOOR_BIN]
    per = []
    for x in clear:
        ci = b["bins"].get(x["bin"], {}).get("ci95")
        over = ci is not None and ci[1] < x["mean_p"]
        per.append({"bin": x["bin"], "n": x["n"], "mean_p": x["mean_p"],
                    "obs": x["obs"], "obs_ci95": ci, "overconfident": over})
    k = sum(1 for p in per if p["overconfident"])
    h["H1_overconfidence_top"] = {
        "population": ("frontier" if tag in FRONTIER else
                       "outside H1's stated population (frontier); applied to the local arm, labelled"),
        "bins_clearing_floor": len(clear), "overconfident_bins": k, "per_bin": per,
        "result": ("UNTESTABLE - fewer than two top bins clear the bin floor" if len(clear) < 2
                   else "SUPPORTED" if k >= 2 else "FALSIFIED")}
    # H2
    lo = b["skill_ci95"][0] if b["skill_ci95"] else None
    h["H2_skill_positive"] = {
        "skill": m["skill"], "skill_ci95": b["skill_ci95"],
        "prior": ("no frontier arm clears at the first checkpoint" if tag in FRONTIER
                  else "none stated for the local arm (Section 11: informed by the faces)"),
        "result": ("SUPPORTED - skill positive, interval excludes zero"
                   if (m["skill"] is not None and m["skill"] > 0 and lo is not None and lo > 0)
                   else "NOT SUPPORTED - skill not positive with interval excluding zero")}
    # H3
    kd_n = sp["keyed"]["resolved"] + sp["keyed_by_rule"]  # keyed-by-rule rows are keyed by rule
    kl_n = sp["keyless"]["resolved"]
    d = sp.get("keyless_minus_keyed_brier")
    dci = b.get("keyless_minus_keyed_brier_ci95")
    if kd_n >= H3_FLOOR and kl_n >= H3_FLOOR:
        if d is not None and d > 0 and dci and dci[0] > 0:
            res = "SUPPORTED - keyless Brier exceeds keyed, interval excludes zero"
        elif d is not None and d <= 0:
            res = "FALSIFIED - keyless at or below keyed: finding against the instrument (determination not separating arithmetic from foresight)"
        else:
            res = "NOT SUPPORTED - difference positive but interval reaches zero"
    else:
        res = "UNTESTABLE - split floor %d per split not met (keyed %d, keyless %d)" % (H3_FLOOR, kd_n, kl_n)
    h["H3_keyless_harder"] = {"keyed_n": kd_n, "keyless_n": kl_n,
                              "keyed_brier": sp["keyed"].get("brier"),
                              "keyless_brier": sp["keyless"].get("brier"),
                              "keyless_minus_keyed_brier": d, "diff_ci95": dci,
                              "keyless_defective_citations": len(sp["keyless"].get("defect_ids", [])),
                              "result": res}
    # H4 - a version change is a new model string, same lane and access
    me = reg.get(tag, {})
    comps = []
    for other_bucket, other_rows in buckets_in_cohort.items():
        otag = other_bucket.split("[")[0]
        o = reg.get(otag, {})
        if otag == tag or not me or not o:
            continue
        if o.get("lane") == me.get("lane") and o.get("access") == me.get("access") \
                and o.get("model") != me.get("model"):
            ores = [r for r in other_rows if r["status"] in ("hit", "miss")]
            if not ores:
                comps.append({"arm": other_bucket, "resolved": 0, "result": "UNTESTABLE - no resolved rows"})
                continue
            om = point(ores)
            ob = bootstrap(ores)
            dec = []
            for x in m["bins"]:
                ox = next((y for y in om["bins"] if y["bin"] == x["bin"]), None)
                if not ox or x["n"] < N_FLOOR_BIN or ox["n"] < N_FLOOR_BIN:
                    continue
                ca = b["bins"].get(x["bin"], {}).get("ci95")
                cb = ob["bins"].get(x["bin"], {}).get("ci95")
                if not ca or not cb:
                    continue
                wider = max(ca[1] - ca[0], cb[1] - cb[0])
                dec.append({"bin": x["bin"], "obs_a": x["obs"], "obs_b": ox["obs"],
                            "abs_diff": round(abs(x["obs"] - ox["obs"]), 3),
                            "wider_ci_width": round(wider, 3),
                            "drift": abs(x["obs"] - ox["obs"]) > wider})
            comps.append({"arm": other_bucket, "resolved": len(ores), "deciles_both_clear": dec,
                          "result": ("UNTESTABLE - no decile clears the bin floor on both sides" if not dec
                                     else "SUPPORTED - drift in %d decile(s)" % sum(1 for z in dec if z["drift"])
                                     if any(z["drift"] for z in dec) else "FALSIFIED - no decile differs at that margin")})
    h["H4_version_drift"] = {"comparators": comps,
                             "result": ("UNTESTABLE - no successor or predecessor with a different model string seals under this hash"
                                        if not comps else "see comparators")}
    # H5 - market control
    mk = [r for r in cohort_rows if r["model"] == MARKET and r["status"] in ("hit", "miss")
          and str(r.get("domain", "")).lower() in MARKET_DOMAINS]
    h["H5_market_control"] = {"market_control_resolved_market_rows": len(mk),
                              "floor": H5_FLOOR,
                              "result": ("UNTESTABLE - %d of %d market-domain rows resolved on control/market-implied" % (len(mk), H5_FLOOR)
                                         if len(mk) < H5_FLOOR else "see comparison")}
    return h


def bucket_of(p, reg):
    tag = str(p.get("model", "?"))
    eras = reg.get(tag, {}).get("eras")
    bucket = tag
    if eras:
        d = str(p.get("date_issued") or "")
        for e in eras:
            if e.get("until") and d and d < e["until"]:
                bucket = tag + "[" + e["id"] + "]"
                break
            if e.get("from") and d and d >= e["from"]:
                bucket = tag + "[" + e["id"] + "]"
    return tag, bucket


def main():
    ap = argparse.ArgumentParser(description="Kalibrierwarte registered report - estimators (Section 7)")
    ap.add_argument("--cohort", default=DEFAULT_COHORT,
                    help="rubric-hash prefix (default %s, cohort 1); 'none' = cohort 0, descriptive only" % DEFAULT_COHORT)
    ap.add_argument("--arm", action="append", default=[],
                    help="restrict to these arm buckets (repeatable); default every arm with rows in the cohort")
    ap.add_argument("--write", action="store_true", help="write forecasts/warte_report_<date>.json")
    ap.add_argument("--self-hash", action="store_true", help="print this file's SHA-256 and exit")
    ap.add_argument("--json", action="store_true", help="also print the report JSON to stdout")
    a = ap.parse_args()

    me = Path(__file__).resolve()
    self_lf = lf_sha256(me)
    self_raw = hashlib.sha256(me.read_bytes()).hexdigest()
    if a.self_hash:
        print("warte_report.py sha256 LF-normalised %s" % self_lf)
        print("warte_report.py sha256 raw bytes     %s" % self_raw)
        return 0

    led = json.loads((HERE / "ledger.json").read_text(encoding="utf-8"))
    rows = led["projections"]
    try:
        reg = {x["tag"]: x for x in json.loads(
            (HERE / "arms.json").read_text(encoding="utf-8-sig"))["arms"]}
    except Exception:
        reg = {}
    defective = set()
    try:
        ci = json.loads((HERE / "cite_integrity_latest.json").read_text(encoding="utf-8"))
        defective = {r["id"] for r in ci.get("rows", [])
                     if str(r.get("verdict", "")).upper() == "DEFECTIVE"}
    except Exception:
        pass
    regpath = HERE / REGISTRATION
    reg_sha = lf_sha256(regpath)[:16] if regpath.exists() else None

    coh = a.cohort.strip()
    if coh.lower() == "none":
        cohort_rows = [r for r in rows if not r.get("rubric_hash")]
        cohort_full = None
        label = "cohort 0 - no hash - descriptive only, excluded from confirmatory analysis"
        confirmatory = False
    elif not coh:
        print("REFUSE - empty cohort prefix; name a rubric-hash prefix or 'none'")
        return 2
    else:
        cohort_rows = [r for r in rows if r.get("rubric_hash")
                       and str(r["rubric_hash"]).startswith(coh)]
        fulls = sorted({r["rubric_hash"] for r in cohort_rows})
        if not fulls:
            print("REFUSE - prefix %s matches no rubric hash on the ledger" % coh)
            return 2
        if len(fulls) != 1:
            print("REFUSE - prefix %s matches %d rubric hashes: %s" % (coh, len(fulls), fulls))
            return 2
        cohort_full = fulls[0]
        label = "cohort %s" % cohort_full[:16]
        confirmatory = True

    buckets = defaultdict(list)
    for r in cohort_rows:
        _, bk = bucket_of(r, reg)
        buckets[bk].append(r)
    controls = [r for r in rows if r["model"] == CONTROL]
    ctl_cohort = [r for r in cohort_rows if r["model"] == CONTROL and r["status"] in ("hit", "miss")]
    ctl_all = [r for r in controls if r["status"] in ("hit", "miss")]

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    report = {"_meta": {"generated": now, "instrument": INSTRUMENT,
                        "registration": REGISTRATION, "registration_sha16_lf": reg_sha,
                        "self_sha256_lf": self_lf, "self_sha256_raw": self_raw,
                        "ledger_as_of": led.get("as_of"), "ledger_rows": len(rows),
                        "cohort": {"prefix": coh, "hash": cohort_full, "label": label,
                                   "rows": len(cohort_rows), "confirmatory": confirmatory},
                        "bootstrap": {"reps": BOOT_N, "seed": BOOT_SEED, "unit": "row",
                                      "interval": "percentile 2.5-97.5, linear interpolation"},
                        "floors": {"checkpoint": CHECKPOINT, "interim": INTERIM, "arm": N_FLOOR_ARM,
                                   "bin": N_FLOOR_BIN, "h3_split": H3_FLOOR, "h5_market": H5_FLOOR},
                        "doctrine": "no pooled score exists; a Brier belongs to one forecaster; "
                                    "nothing is claimed below the floors; misses printed at full size"},
              "arms": {}}

    print("WARTE REPORT - %s - %s - ledger %d rows as of %s" % (INSTRUMENT, label, len(rows), led.get("as_of")))
    print("registration %s (LF-sha16 %s) - self %s" % (REGISTRATION, reg_sha, self_lf[:16]))
    print("bootstrap: %d resamples, seed %d, unit row, percentile 2.5-97.5" % (BOOT_N, BOOT_SEED))
    halted = False
    order = sorted(buckets, key=lambda k: -len([r for r in buckets[k] if r["status"] in ("hit", "miss")]))
    for bk in order:
        if a.arm and bk not in a.arm:
            continue
        tag = bk.split("[")[0]
        brows = buckets[bk]
        res = [r for r in brows if r["status"] in ("hit", "miss")]
        voids = [r for r in brows if r["status"] == "void"]
        n = len(res)
        stage = ("checkpoint" if confirmatory and n >= CHECKPOINT else
                 "interim" if n >= INTERIM else "counts-only")
        if tag in CAPABILITY_OUT:
            stage = "counts-only"
        entry = {"arm": bk, "tag": tag, "issued": len(brows),
                 "open": sum(1 for r in brows if r["status"] == "open"),
                 "resolved": n, "hits": sum(1 for r in res if r["status"] == "hit"),
                 "misses": sum(1 for r in res if r["status"] == "miss"),
                 "voids": len(voids), "stage": stage,
                 "capability_claim": tag not in CAPABILITY_OUT,
                 "corrections": {"count": sum(1 for r in brows if r.get("keyed_keyless_superseded")),
                                 "rows": [{"id": r["id"], "superseded": r.get("keyed_keyless_superseded"),
                                           "current": r.get("keyed_keyless"),
                                           "dated": r.get("keyed_keyless_corrected")}
                                          for r in brows if r.get("keyed_keyless_superseded")]}}
        print("")
        print("== %s == issued %d - open %d - resolved %d (%d hit / %d miss) - void %d - stage %s" % (
            bk, entry["issued"], entry["open"], n, entry["hits"], entry["misses"], len(voids), stage))
        if entry["corrections"]["count"]:
            print("   corrected determinations in scope: %d (superseded value kept on each row)" % entry["corrections"]["count"])
        if stage == "counts-only":
            entry["note"] = ("out of scope for any capability claim" if tag in CAPABILITY_OUT
                             else "under %d resolved within the cohort - counts only" % INTERIM)
            print("   " + entry["note"])
            report["arms"][bk] = entry
            continue
        m = point(res)
        b = bootstrap(res)
        sp = split_metrics(res, defective)
        entry["metrics"] = m
        entry["bootstrap"] = b
        entry["split"] = sp
        entry["seats"] = seat_cut(res)
        noise = "under 30 resolved, this is noise" if n < 30 else "n=%d - floors are conventions, not power; a null is absence of evidence" % n
        print("   Brier %s [%s, %s] - base rate %s - climatological %s - skill %s [%s, %s] - %s" % (
            m["brier"], b["brier_ci95"][0], b["brier_ci95"][1], m["base_rate"], m["climatological"],
            m["skill"], (b["skill_ci95"] or [None, None])[0], (b["skill_ci95"] or [None, None])[1], noise))
        for x in m["bins"]:
            ci = b["bins"].get(x["bin"], {}).get("ci95")
            print("   bin %-6s n %3d  mean p %.3f  obs %s  ci95 %s" % (
                x["bin"], x["n"], x["mean_p"], x["obs"] if x["obs"] is not None else x["note"],
                ci if x["obs"] is not None else "-"))
        for lab in ("keyed", "keyless"):
            s = sp[lab]
            print("   %-8s n %3d  Brier %s  skill %s  %s" % (
                lab, s["resolved"], s.get("brier"), s.get("skill"),
                ("%d defective-citation row(s)" % len(s["defect_ids"]) if s.get("defect_ids") else "")))
        print("   keyed-by-rule (resolved without determination): %d - keyless-minus-keyed Brier %s ci95 %s" % (
            sp["keyed_by_rule"], sp.get("keyless_minus_keyed_brier"), b.get("keyless_minus_keyed_brier_ci95")))
        for lab, s in entry["seats"].items():
            if lab == "unclassified":
                continue
            if s["resolved"]:
                print("   seat %-22s n %3d  Brier %s  skill %s  brier_ci95 %s" % (
                    lab, s["resolved"], s.get("brier"), s.get("skill"), s.get("brier_ci95")))
        if stage == "interim":
            entry["note"] = "interim read at %d - printed with the noise line - NOT a result of this registration (Section 8)" % n
            print("   " + entry["note"])
            report["arms"][bk] = entry
            continue
        # checkpoint: quality checks, then hypotheses
        q = quality(bk, tag, brows, brows, cohort_full, controls, ctl_cohort, ctl_all)
        entry["quality"] = q
        print("   -- quality checks (Section 7) --")
        qa = q["a_mirror_completeness"]
        print("   (a) mirror completeness %s - %d checked: same-run %d, late %d, none %d%s - %s" % (
            qa["result"], qa["rows_checked"], qa["same_run"], qa["late_mirror"], qa["no_mirror"],
            (" (binding)" if qa["binding"] else " (not binding for this arm)"), qa["note"]))
        for x in qa["listed"][:12]:
            print("       %s -> %s (%s, gap %s min)" % (x["id"], x["mirror"], x["class"], x["gap_min"]))
        if len(qa["listed"]) > 12:
            print("       ... %d more listed in the report file" % (len(qa["listed"]) - 12))
        qb = q["b_rubric_coverage"]
        print("   (b) rubric coverage %s - %d/%d rows carry %s" % (qb["result"], qb["carrying_cohort_hash"], qb["rows"], (cohort_full or "")[:16]))
        qc = q["c_seat_recorded"]
        print("   (c) seat recorded %s - %s" % (qc["result"], qc["seats"]))
        qd = q["d_determination_coverage"]
        print("   (d) determination coverage %s - keyed %d, keyless %d, keyed-by-rule %d" % (qd["result"], qd["keyed"], qd["keyless"], qd["keyed_by_rule"]))
        qe = q["e_control_skill_zero"]
        ec = qe["within_cohort"]
        print("   (e) control/baserate skill vs own base rate %s - within cohort n %s: skill %s ci95 %s%s" % (
            qe["result"], ec.get("resolved"), ec.get("skill"), ec.get("skill_ci95"),
            " (control under the arm floor)" if ec.get("under_arm_floor") else ""))
        ea = qe["all_time_exploratory"]
        print("       exploratory, all cohorts pooled (the face): n %s skill %s ci95 %s -> %s" % (
            ea.get("resolved"), ea.get("skill"), ea.get("skill_ci95"), ea.get("result")))
        print("       " + qe["note"])
        qf = q["f_void_rate"]
        print("   (f) void rate - %d void beside %d resolved = %s" % (qf["voids"], qf["resolved"], qf["void_rate"]))
        if not q["all_pass"]:
            halted = True
            entry["hypotheses"] = None
            entry["note"] = "READ HALTED - a quality check failed; no hypothesis read for this arm (Section 7)"
            print("   " + entry["note"])
            report["arms"][bk] = entry
            continue
        h = hypotheses(bk, tag, m, b, sp, cohort_rows, buckets, reg)
        entry["hypotheses"] = h
        print("   -- hypotheses at first checkpoint (n=%d, Section 6) --" % n)
        h1 = h["H1_overconfidence_top"]
        print("   H1 %s - %d/%d top bins overconfident%s" % (
            h1["result"], h1["overconfident_bins"], h1["bins_clearing_floor"],
            "" if tag in FRONTIER else " - " + h1["population"]))
        for p in h1["per_bin"]:
            print("       %s n %d mean p %.3f obs %s ci95 %s -> %s" % (
                p["bin"], p["n"], p["mean_p"], p["obs"], p["obs_ci95"], "overconfident" if p["overconfident"] else "not"))
        h2 = h["H2_skill_positive"]
        print("   H2 %s - skill %s ci95 %s - prior: %s" % (h2["result"], h2["skill"], h2["skill_ci95"], h2["prior"]))
        h3 = h["H3_keyless_harder"]
        print("   H3 %s - keyed %d Brier %s / keyless %d Brier %s - diff %s ci95 %s - keyless defective citations %d" % (
            h3["result"], h3["keyed_n"], h3["keyed_brier"], h3["keyless_n"], h3["keyless_brier"],
            h3["keyless_minus_keyed_brier"], h3["diff_ci95"], h3["keyless_defective_citations"]))
        h4 = h["H4_version_drift"]
        print("   H4 %s" % h4["result"])
        for c in h4["comparators"]:
            print("       vs %s (n %d): %s" % (c["arm"], c["resolved"], c["result"]))
        print("   H5 %s" % h["H5_market_control"]["result"])
        report["arms"][bk] = entry

    written = None
    if a.write:
        txt = json.dumps(report, indent=1, ensure_ascii=True) + "\n"
        outp = HERE / "forecasts" / ("warte_report_%s.json" % now[:10])
        outp.parent.mkdir(exist_ok=True)
        try:
            sys.path.insert(0, str(HERE))
            from runguard import write_run_artifact
            written = write_run_artifact(outp, txt, tag="warte_report")
        except Exception:
            if outp.exists() and outp.read_text(encoding="utf-8") != txt:
                k = 2
                while outp.with_name("warte_report_%s_%d.json" % (now[:10], k)).exists():
                    k += 1
                outp = outp.with_name("warte_report_%s_%d.json" % (now[:10], k))
            outp.write_text(txt, encoding="utf-8")
            written = outp
        print("")
        print("WARTE REPORT - written %s (sha256 LF %s)" % (written, lf_sha256(Path(written))[:16]))
    else:
        print("")
        print("WARTE REPORT - report-only; --write writes forecasts/warte_report_%s.json" % now[:10])
    if a.json:
        print(json.dumps(report, indent=1, ensure_ascii=True))
    return 3 if halted else 0


if __name__ == "__main__":
    sys.exit(main())
