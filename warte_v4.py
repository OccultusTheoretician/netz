#!/usr/bin/env python3
r"""
warte_v4.py - Kalibrierwarte registered report v4, the instrument (v4 Section 8).

Reads ledger.json and arms.json only. Imports warte_report.py and redefines none of its
estimators, floors or constants: Brier, bins, seats, determinations, percentile intervals
(2,000 resamples, seed 26, linear interpolation) are warte_report's. What is new here is
v4's: the population (rows of the arms in scope sealed at or after the adoption commit),
the pair (an arm row and its control/trailing mirror sealed in the same run), the pair as
the bootstrap unit for V1, V3 and check (e'), and checks (a)-(g).

Reading decisions taken in building, each stated in the pinning amendment (v4 Section 12):
  population  sealed_at >= ADOPTION_UTC (committer time of the adoption commit a257f2c),
              rubric hash in the named cohort; a population row with no rubric hash fails (b)
  pair        mirror = the control/trailing row whose control_basis.control_for is the arm
              row's id, control_basis.mirror_of equal to the arm's tag, same source_packet,
              seal times within warte_report.SAME_RUN_MINUTES; anything else is a gap (a)
  read set    operator/cold rows carrying the operator's hand seat are out (counted, (c));
              operator/cold rows without a recorded passing cold order are out (listed, (g))
  stage       counted on resolved pairs in the read set: checkpoint 50, interim 30 (noise
              line, not a result), otherwise counts only; checks run at the checkpoint
  V2          v3's H1 rule on the arm's resolved rows in the read set (rows, not pairs)

Report-only by default; --write writes forecasts/warte_v4_<date>.json through runguard.
Exit 0 read, 2 refused, 3 a check failed and a read halted.
"""
import argparse
import hashlib
import json
import random
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import warte_report as W  # noqa: E402

INSTRUMENT = "warte_v4/1.1"
REGISTRATION = "docs/KALIBRIERWARTE_REGISTERED_REPORT_v4.md"
ADOPTION_COMMIT = "a257f2c879dad31ba0c4b6a2a3e8917dba705129"
ADOPTION_UTC = "2026-10-27T19:55:42+00:00"
DEFAULT_COHORT = "bbdc7791"
TRAILING = "control/trailing"
FRONTIER_V4 = ("manual/fable-5.1/unattested", "manual/opus-5.5/unattested", "manual/fable-5.2/unattested")
COLD = "operator/cold"
ADVISED = "operator/advised"
SCOPE = FRONTIER_V4 + (COLD, ADVISED)
PRIORS = {  # v4 Section 7, the registrant's, 2026-10-27
    "manual/fable-5.1/unattested": {"V1": "yes", "V2": "no"},
    "manual/opus-5.5/unattested": {"V1": "yes", "V2": "no"},
    "manual/fable-5.2/unattested": {"V1": "not stated", "V2": "not stated"},
    COLD: {"V1": "no", "V2": "yes"},
    ADVISED: {"V1": "not stated", "V2": "not stated"},
}
NOT_SAME_CLAIMS = ("each forecaster is measured against its own climatology on its own claims; "
                   "this is not a same-claims test")


def ts(x):
    try:
        d = datetime.fromisoformat(str(x).replace("Z", "+00:00"))
    except Exception:
        return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


def y_of(r):
    return 1.0 if r["status"] == "hit" else 0.0


def p_of(r):
    return float(r.get("probability", 0)) / 100.0


def pair_d(pairs):
    """Mean over pairs of (arm squared error) - (mirror squared error)."""
    if not pairs:
        return None
    return sum((pa - ya) ** 2 - (pc - yc) ** 2 for pa, ya, pc, yc in pairs) / len(pairs)


def ctl_gap(pairs):
    """Control's mean priced probability minus its realized hit frequency, over pairs."""
    if not pairs:
        return None
    n = len(pairs)
    return sum(pc for _, _, pc, _ in pairs) / n - sum(yc for _, _, _, yc in pairs) / n


def boot_pairs(pairs, fn, seed=W.BOOT_SEED, reps=W.BOOT_N):
    """Percentile bootstrap, unit = pair: each arm row travels with its mirror."""
    n = len(pairs)
    if n == 0:
        return None
    rng = random.Random(seed)
    vals = []
    for _ in range(reps):
        vals.append(fn([pairs[rng.randrange(n)] for _ in range(n)]))
    return W.ci95(vals)


def boot_v3(pa, pb, seed=W.BOOT_SEED, reps=W.BOOT_N):
    """Operator's V1 difference minus a frontier arm's; both arms' pairs resampled
    independently inside each resample (v4 Section 7, V3)."""
    rng = random.Random(seed)
    na, nb = len(pa), len(pb)
    vals = []
    for _ in range(reps):
        a = [pa[rng.randrange(na)] for _ in range(na)]
        b = [pb[rng.randrange(nb)] for _ in range(nb)]
        vals.append(pair_d(a) - pair_d(b))
    return W.ci95(vals)


def v2_top(rs):
    """v3's H1 rule (v3 Section 6, warte_report.hypotheses) on v4's read set."""
    m = W.point(rs)
    b = W.bootstrap(rs)
    clear = [x for x in m.get("bins", []) if x["bin"] in W.TOP_BINS and x["n"] >= W.N_FLOOR_BIN]
    per = []
    for x in clear:
        ci = b["bins"].get(x["bin"], {}).get("ci95")
        over = ci is not None and ci[1] < x["mean_p"]
        per.append({"bin": x["bin"], "n": x["n"], "mean_p": x["mean_p"], "obs": x["obs"],
                    "obs_ci95": ci, "overconfident": over})
    k = sum(1 for p in per if p["overconfident"])
    return {"rows": len(rs), "bins_clearing_floor": len(clear), "overconfident_bins": k,
            "per_bin": per,
            "result": ("UNTESTABLE - fewer than two top bins clear the bin floor" if len(clear) < 2
                       else "SUPPORTED" if k >= 2 else "FALSIFIED")}


def build(rows, reg, coh_full):
    """Population, mirrors, pairs and exclusions per arm in scope."""
    cut = ts(ADOPTION_UTC)
    by_id = {r["id"]: r for r in rows}
    mirrors = {}
    for c in rows:
        if c.get("model") != TRAILING:
            continue
        f = (c.get("control_basis") or {}).get("control_for")
        if f:
            mirrors.setdefault(f, []).append(c)
    out = {}
    for tag in SCOPE:
        mine = [r for r in rows if r.get("model") == tag]
        no_seal = [r["id"] for r in mine if ts(r.get("sealed_at")) is None]
        pop = [r for r in mine if ts(r.get("sealed_at")) is not None and ts(r["sealed_at"]) >= cut]
        unhashed = [r["id"] for r in pop if not r.get("rubric_hash")]
        other = Counter(str(r["rubric_hash"])[:8] for r in pop
                        if r.get("rubric_hash") and r["rubric_hash"] != coh_full)
        pop = [r for r in pop if r.get("rubric_hash") == coh_full]
        recs, gaps = [], []
        for r in pop:
            cands = mirrors.get(r["id"]) or []
            why, c = None, None
            if not cands:
                why = "no mirror"
            elif len(cands) > 1:
                why = "%d mirrors" % len(cands)
            else:
                c = cands[0]
                cb = c.get("control_basis") or {}
                gap = abs((ts(c.get("sealed_at")) - ts(r["sealed_at"])).total_seconds()) / 60.0 \
                    if ts(c.get("sealed_at")) else None
                if cb.get("mirror_of") != tag:
                    why = "mirror_of %s" % cb.get("mirror_of")
                elif c.get("source_packet") != r.get("source_packet"):
                    why = "other packet"
                elif gap is None or gap > W.SAME_RUN_MINUTES:
                    why = "not same run (gap %s min)" % (None if gap is None else round(gap, 1))
                elif c.get("rubric_hash") != coh_full:
                    why = "mirror outside cohort"
            if why:
                gaps.append({"id": r["id"], "why": why})
                c = None
            recs.append((r, c))
        hand, order_out = [], []
        read = []
        for r, c in recs:
            if tag == COLD:
                if W.seat_of(r) == "operator" and r["status"] in ("hit", "miss"):
                    hand.append(r["id"])
                    continue
                co = r.get("cold_order") or {}
                if co.get("ok") is not True:
                    order_out.append({"id": r["id"], "why": "order not recorded" if not co else "arrived after a frontier file"})
                    continue
            read.append((r, c))
        out[tag] = {"registered": tag in reg, "status": (reg.get(tag) or {}).get("status"),
                    "rows_all": len(mine), "no_seal_time": no_seal, "population": len(pop) + len(unhashed) + sum(other.values()),
                    "in_cohort": len(pop), "unhashed": unhashed, "other_cohorts": dict(other),
                    "recs": recs, "gaps": gaps, "hand_seat_out": hand, "cold_order_out": order_out,
                    "read": read}
    return out


def arm_report(tag, A, confirmatory):
    read = A["read"]
    arm_rows = [r for r, _ in read]
    paired = [(r, c) for r, c in read if c is not None]
    both = [(r, c) for r, c in paired if r["status"] in ("hit", "miss") and c["status"] in ("hit", "miss")]
    void_pair = [(r, c) for r, c in paired if r["status"] == "void" or c["status"] == "void"]
    pairs = [(p_of(r), y_of(r), p_of(c), y_of(c)) for r, c in both]
    differ = sum(1 for r, c in both if r["status"] != c["status"])
    n = len(pairs)
    stage = ("checkpoint" if confirmatory and n >= W.CHECKPOINT else
             "interim" if n >= W.INTERIM else "counts-only")
    e = {"arm": tag, "registered": A["registered"], "registry_status": A["status"],
         "rows_all_time": A["rows_all"], "population": A["population"], "in_cohort": A["in_cohort"],
         "open": sum(1 for r in arm_rows if r["status"] == "open"),
         "resolved_rows": sum(1 for r in arm_rows if r["status"] in ("hit", "miss")),
         "void_rows": sum(1 for r in arm_rows if r["status"] == "void"),
         "pairs_formed": len(paired), "pairs_resolved": n, "pairs_out_void": len(void_pair),
         "pairs_outcome_differs": differ, "gaps": A["gaps"],
         "hand_seat_out": A["hand_seat_out"], "cold_order_out": A["cold_order_out"],
         "stage": stage, "priors": PRIORS.get(tag)}
    print("")
    print("== %s == population %d (in cohort %d) - read %d - open %d - pairs %d formed, %d resolved, %d out by void - stage %s" % (
        tag, e["population"], e["in_cohort"], len(read), e["open"], len(paired), n, len(void_pair), stage))
    if A["no_seal_time"]:
        print("   rows with no seal time (outside every population): %d" % len(A["no_seal_time"]))
    if A["other_cohorts"]:
        print("   population rows in another cohort, outside this read: %s" % A["other_cohorts"])
    if A["gaps"]:
        print("   pairing gaps: %d - %s" % (len(A["gaps"]), "; ".join("%s %s" % (g["id"], g["why"]) for g in A["gaps"][:6])))
    if A["hand_seat_out"]:
        print("   operator hand seat, out of every confirmatory read (v4 Section 5): %d" % len(A["hand_seat_out"]))
    if A["cold_order_out"]:
        print("   cold order not shown, out (check g): %d - %s" % (len(A["cold_order_out"]), ", ".join(x["id"] for x in A["cold_order_out"][:6])))
    if differ:
        print("   pairs whose arm and mirror outcomes differ: %d (a finding about the pairing)" % differ)
    if stage == "counts-only":
        e["note"] = "under %d resolved pairs - counts only" % W.INTERIM
        print("   " + e["note"])
        return e, False
    d = pair_d(pairs)
    dci = boot_pairs(pairs, pair_d)
    e["V1_point"] = {"d": W.r3(d), "d_ci95": dci,
                     "arm_brier": W.r3(sum((pa - ya) ** 2 for pa, ya, _, _ in pairs) / n),
                     "mirror_brier": W.r3(sum((pc - yc) ** 2 for _, _, pc, yc in pairs) / n)}
    noise = ("under 30 resolved pairs, this is noise" if n < 30 else
             "n=%d pairs - floors are conventions, not power; a null is absence of evidence" % n)
    print("   arm Brier %s - mirror Brier %s - difference %s ci95 %s (unit pair) - %s" % (
        e["V1_point"]["arm_brier"], e["V1_point"]["mirror_brier"], e["V1_point"]["d"], dci, noise))
    if stage == "interim":
        e["note"] = "interim read at %d pairs - printed with the noise line - NOT a result of this registration (Section 9)" % n
        print("   " + e["note"])
        return e, False
    # checkpoint: quality checks (Section 8), all before any hypothesis
    q = {}
    q["a_pairing"] = {"rows": len(A["recs"]), "same_run": len(A["recs"]) - len(A["gaps"]),
                      "gaps": A["gaps"], "result": "PASS" if not A["gaps"] else "FAIL"}
    seatless = [r["id"] for r in arm_rows if r["status"] in ("hit", "miss") and W.seat_of(r) is None]
    seatless += [c["id"] for _, c in both if W.seat_of(c) is None]
    q["c_seats"] = {"seats": dict(Counter(W.seat_of(r) for r in arm_rows if r["status"] in ("hit", "miss"))),
                    "seatless": seatless, "operator_hand_out": len(A["hand_seat_out"]),
                    "result": "PASS" if not seatless else "FAIL"}
    q["b_rubric"] = {"in_cohort": A["in_cohort"], "unhashed": A["unhashed"],
                     "result": "PASS" if not A["unhashed"] else "FAIL"}
    dets = Counter(W.det_of(r) for r in arm_rows if r["status"] in ("hit", "miss"))
    q["d_determinations"] = {"keyed": dets["keyed"], "keyless": dets["keyless"],
                             "keyed_by_rule": dets["keyed-by-rule"], "result": "PASS",
                             "note": "rows resolved without a determination are keyed by rule and counted"}
    g = ctl_gap(pairs)
    gci = boot_pairs(pairs, ctl_gap)
    q["e_prime_control_calibration"] = {
        "mean_priced": W.r3(sum(pc for _, _, pc, _ in pairs) / n),
        "realized": W.r3(sum(yc for _, _, _, yc in pairs) / n), "gap": W.r3(g), "gap_ci95": gci,
        "result": "PASS" if gci and gci[0] <= 0 <= gci[1] else "FAIL",
        "note": "a trailing rate can lag an arm whose hit rate moves; a failure prints as that"}
    q["f_void_rate"] = {"void_rows": e["void_rows"], "pairs_out_void": len(void_pair),
                        "void_rate": W.r3(len(void_pair) / max(1, len(paired)))}
    q["g_cold_order"] = ({"result": "PASS" if not A["cold_order_out"] else "ROWS OUT",
                          "out": A["cold_order_out"],
                          "note": "rows failing it are out of the read, listed; the check does not halt"}
                         if tag == COLD else {"result": "n/a - not operator/cold"})
    fails = [k for k in ("a_pairing", "b_rubric", "c_seats", "e_prime_control_calibration")
             if q[k]["result"] == "FAIL"]
    q["all_pass"] = not fails
    e["quality"] = q
    print("   -- quality checks (Section 8) --")
    print("   (a) pairing %s - %d rows, %d same-run, %d gaps" % (q["a_pairing"]["result"], q["a_pairing"]["rows"], q["a_pairing"]["same_run"], len(A["gaps"])))
    print("   (b) rubric %s - %d in cohort, %d unhashed" % (q["b_rubric"]["result"], A["in_cohort"], len(A["unhashed"])))
    print("   (c) seats %s - %s - hand seat out %d" % (q["c_seats"]["result"], q["c_seats"]["seats"], len(A["hand_seat_out"])))
    print("   (d) determinations %s - keyed %d, keyless %d, keyed-by-rule %d" % ("PASS", dets["keyed"], dets["keyless"], dets["keyed-by-rule"]))
    qe = q["e_prime_control_calibration"]
    print("   (e') control calibration %s - priced %s, realized %s, gap %s ci95 %s" % (qe["result"], qe["mean_priced"], qe["realized"], qe["gap"], gci))
    print("   (f) void rate %s - %d pairs out by void of %d formed" % (q["f_void_rate"]["void_rate"], len(void_pair), len(paired)))
    print("   (g) cold order %s" % q["g_cold_order"]["result"])
    if fails:
        e["hypotheses"] = None
        e["note"] = "READ HALTED - %s failed; no hypothesis read for this arm (Section 8; the halt stands)" % ", ".join(fails)
        print("   " + e["note"])
        return e, True
    h = {}
    h["V1_paired_skill"] = {"pairs": n, "d": W.r3(d), "d_ci95": dci, "prior": PRIORS[tag]["V1"],
                            "result": ("SUPPORTED - arm Brier below its mirrors', interval excludes zero"
                                       if d < 0 and dci and dci[1] < 0 else
                                       "NOT SUPPORTED - the interval reaches zero")}
    h["V2_overconfidence_top"] = dict(v2_top([r for r in arm_rows if r["status"] in ("hit", "miss")]),
                                      prior=PRIORS[tag]["V2"])
    e["hypotheses"] = h
    e["_pairs"] = pairs
    print("   -- hypotheses at first checkpoint (%d pairs, Section 7) --" % n)
    print("   V1 %s - d %s ci95 %s - prior %s" % (h["V1_paired_skill"]["result"], h["V1_paired_skill"]["d"], dci, PRIORS[tag]["V1"]))
    v2 = h["V2_overconfidence_top"]
    print("   V2 %s - %d/%d top bins overconfident over %d rows - prior %s" % (v2["result"], v2["overconfident_bins"], v2["bins_clearing_floor"], v2["rows"], v2["prior"]))
    for p in v2["per_bin"]:
        print("       %s n %d mean p %.3f obs %s ci95 %s -> %s" % (p["bin"], p["n"], p["mean_p"], p["obs"], p["obs_ci95"], "overconfident" if p["overconfident"] else "not"))
    return e, False


def main():
    ap = argparse.ArgumentParser(description="Kalibrierwarte registered report v4 - the instrument (Section 8)")
    ap.add_argument("--cohort", default=DEFAULT_COHORT, help="rubric-hash prefix (default %s)" % DEFAULT_COHORT)
    ap.add_argument("--write", action="store_true", help="write forecasts/warte_v4_<date>.json")
    ap.add_argument("--self-hash", action="store_true", help="print this file's SHA-256 and exit")
    ap.add_argument("--json", action="store_true", help="also print the report JSON to stdout")
    a = ap.parse_args()

    me = Path(__file__).resolve()
    self_lf = W.lf_sha256(me)
    self_raw = hashlib.sha256(me.read_bytes()).hexdigest()
    if a.self_hash:
        print("warte_v4.py sha256 LF-normalised %s" % self_lf)
        print("warte_v4.py sha256 raw bytes     %s" % self_raw)
        return 0
    led = json.loads((HERE / "ledger.json").read_text(encoding="utf-8"))
    rows = led["projections"]
    reg = {x["tag"]: x for x in json.loads((HERE / "arms.json").read_text(encoding="utf-8-sig"))["arms"]}
    coh = a.cohort.strip()
    fulls = sorted({r["rubric_hash"] for r in rows if r.get("rubric_hash") and coh
                    and str(r["rubric_hash"]).startswith(coh)})
    if len(fulls) != 1:
        print("REFUSE - prefix %r matches %d rubric hashes" % (coh, len(fulls)))
        return 2
    coh_full = fulls[0]
    regp = HERE / REGISTRATION
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    report = {"_meta": {"generated": now, "instrument": INSTRUMENT, "registration": REGISTRATION,
                        "registration_sha16_lf": W.lf_sha256(regp)[:16] if regp.exists() else None,
                        "self_sha256_lf": self_lf, "self_sha256_raw": self_raw,
                        "warte_report_sha16_lf": W.lf_sha256(Path(W.__file__))[:16],
                        "adoption": {"commit": ADOPTION_COMMIT, "utc": ADOPTION_UTC},
                        "ledger_as_of": led.get("as_of"), "ledger_rows": len(rows),
                        "cohort": {"prefix": coh, "hash": coh_full},
                        "bootstrap": {"reps": W.BOOT_N, "seed": W.BOOT_SEED, "unit": "pair (V1, V3, e'); row (V2)",
                                      "interval": "percentile 2.5-97.5, linear interpolation"},
                        "floors": {"checkpoint_pairs": W.CHECKPOINT, "interim_pairs": W.INTERIM,
                                   "bin": W.N_FLOOR_BIN, "same_run_minutes": W.SAME_RUN_MINUTES},
                        "doctrine": "no pooled score exists; a Brier belongs to one forecaster; "
                                    "nothing is claimed below the floors; misses printed at full size"},
              "arms": {}, "V3": []}
    print("WARTE v4 - %s - cohort %s - ledger %d rows as of %s" % (INSTRUMENT, coh_full[:16], len(rows), led.get("as_of")))
    print("registration %s (LF-sha16 %s) - self %s - warte_report %s" % (
        REGISTRATION, report["_meta"]["registration_sha16_lf"], self_lf[:16], report["_meta"]["warte_report_sha16_lf"]))
    print("population: sealed at or after %s (adoption %s)" % (ADOPTION_UTC, ADOPTION_COMMIT[:7]))
    B = build(rows, reg, coh_full)
    halted = False
    done = {}
    for tag in SCOPE:
        e, h = arm_report(tag, B[tag], True)
        halted |= h
        done[tag] = e
    for tag in SCOPE:
        report["arms"][tag] = {k: v for k, v in done[tag].items() if k != "_pairs"}
    oc = done[COLD]
    for f in FRONTIER_V4:
        fe = done[f]
        rec = {"operator": COLD, "frontier": f, "two_sided": True, "note": NOT_SAME_CLAIMS}
        if oc.get("hypotheses") and fe.get("hypotheses"):
            dd = oc["hypotheses"]["V1_paired_skill"]["d"] - fe["hypotheses"]["V1_paired_skill"]["d"]
            ci = boot_v3(oc["_pairs"], fe["_pairs"])
            rec.update({"diff": W.r3(dd), "diff_ci95": ci,
                        "result": ("DIFFERENCE - interval excludes zero" if ci and (ci[1] < 0 or ci[0] > 0)
                                   else "NO DIFFERENCE DETECTED - interval covers zero")})
        else:
            rec["result"] = "WAITS - V3 needs both arms read at their first checkpoints"
        report["V3"].append(rec)
        print("")
        print("V3 %s vs %s: %s%s - %s" % (COLD, f, rec["result"],
                                         (" diff %s ci95 %s" % (rec["diff"], rec["diff_ci95"])) if "diff" in rec else "", NOT_SAME_CLAIMS))
    if a.write:
        txt = json.dumps(report, indent=1, ensure_ascii=True) + "\n"
        outp = HERE / "forecasts" / ("warte_v4_%s.json" % now[:10])
        outp.parent.mkdir(exist_ok=True)
        from runguard import write_run_artifact
        written = write_run_artifact(outp, txt, tag="warte_v4")
        print("")
        print("WARTE v4 - written %s (sha256 LF %s)" % (written, W.lf_sha256(Path(written))[:16]))
    else:
        print("")
        print("WARTE v4 - report-only; --write writes forecasts/warte_v4_%s.json" % now[:10])
    if a.json:
        print(json.dumps(report, indent=1, ensure_ascii=True))
    return 3 if halted else 0


if __name__ == "__main__":
    sys.exit(main())
