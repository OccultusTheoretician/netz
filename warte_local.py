#!/usr/bin/env python3
"""warte_local.py - Kalibrierwarte Section 16: the reads of the local succession.

H6 on the successor (16.3), H7a, H7b and H7c (16.5) and H8 (16.6), under the
quality checks of 16.8, the corrected gate of 16.7 and the selection companion
of 16.12 (b). It imports warte_report.py (the Section 13 pin) and warte_frame.py
(the 15.5 pin) and redefines nothing in either: every percentile, interval
rounding, floor, bin, seed and resample count, and the H6 test, are theirs.
This file adds the day scope of 16.8, the statistics Section 16 defines and
their read points.

Fixed in advance (registration 16.13):
  - A packet day is the UTC date of a row's date_issued and of a run line's ts.
  - Rows in scope: cohort bbdc7791, date_issued on or after 2026-10-04 (16.7).
    Every sealed row counts whatever its later status; voids are counted beside.
  - Day checks run over every local run of the day: (g) the stock and twin runs
    read one packet (one register digest) and carry equal prompt_tokens; (g')
    each framed arm's prompt_tokens minus its plain arm's equals the reference
    fixed by the overlap (the modal difference over 2026-10-05..2026-10-25);
    (h) every run's response_model equals its arm's registered key; (i) one gate
    digest; (j) no reasoning output. (k) is per statistic: every arm the
    statistic needs sealed at least one row in scope that day; a day failing
    only (k) stays in H7c (iv).
  - Read points come from the record, not from the run date: H7a reads on the
    21st in-scope day, over the 21 days up to it; H7b on the first in-scope day
    by which 21 in-scope days exist and each arm has 30 conflict and 30 other
    rows in scope; H8 over the in-scope overlap days once the overlap has ended;
    H7c on the first date by which both arms have 50 resolved rows in the
    cohort (by resolved_date), over the population up to that date. A read run
    later returns the same figures.
  - Intervals: bootstrap 95%, the estimator's 2,000 resamples, seed 26
    (random.Random, as the estimator draws), percentile with linear
    interpolation and four-decimal rounding (W.ci95); packet days resampled
    with replacement (all of an arm's rows on a drawn day), except H7c (iii),
    which resamples resolved rows within each arm independently. A resample on
    which a statistic is undefined is skipped and counted.
  - The 16.12 (b) companion: the same statistic on every generated row,
    accepted and rejected, over the read's in-scope days on which every arm it
    needs carries the generated record; printed, never read as a test.

  python warte_local.py                 counts, and every read that is due
  python warte_local.py --counts-only   counts and scope only; no statistic is computed
  python warte_local.py --write         also write forecasts/warte_local_<UTC date>.json
  python warte_local.py --json          also print the report JSON (first line exactly "{")
  python warte_local.py --self-hash     print this file's LF-normalised SHA-256 and exit

Exit 0 counts or reads; 2 usage or refused input.
"""
import argparse
import bisect
import hashlib
import json
import random
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import warte_report as W  # the Section 13 pin; nothing in it is redefined here
import warte_frame as F   # the 15.5 pin; its arm report and H6 test are used unchanged

INSTRUMENT = "warte_local/1.0"
STOCK = "lmstudio/qwen36"
TWIN = "lmstudio/qwen36-abliterated"
SFRAME = "lmstudio/qwen36-realist"
IPLAIN = "lmstudio/auto"
IFRAME = "lmstudio/realist"
ARMS = (STOCK, TWIN, SFRAME, IPLAIN, IFRAME)
PAIRS = ((STOCK, SFRAME), (IPLAIN, IFRAME))          # (plain, framed), one model each
COHORT = "bbdc7791"
GATE_FROM = "2026-10-04"                             # 16.7, commit c1abde0
FIRST_DAY = "2026-10-05"                             # 16.12 (a)
OVERLAP = ("2026-10-05", "2026-10-25")               # 16.12 (a)
FRAME_POP = "442300f131b11b7c"                       # 15.4, the realist frame in force
DOMAINS_SHA = "1896f80732811642388c2f5d9a0328661c179ebe59398606c07c331b13ed81ba"  # 16.5
CONFLICT = ("military", "crime-security")
H7_DAYS = 21
H7B_ROWS = 30


def lf_sha256(path):
    return hashlib.sha256(Path(path).read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def p01(x):
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v / 100.0


def mean(xs):
    return sum(xs) / len(xs)


def sharp(ps):
    return sum(abs(p - 0.5) for p in ps) / len(ps)


def r4(x):
    return None if x is None else round(x, 4)


def boot(units, stat):
    """Resample units with replacement: the estimator's seed, count, percentile and rounding."""
    n = len(units)
    if not n:
        return {"ci95": None, "resamples": 0, "skipped": 0, "reps": W.BOOT_N, "seed": W.BOOT_SEED}
    rng = random.Random(W.BOOT_SEED)
    vals, skipped = [], 0
    for _ in range(W.BOOT_N):
        draw = [units[rng.randrange(n)] for _ in range(n)]
        v = stat(draw)
        if v is None:
            skipped += 1
        else:
            vals.append(v)
    return {"ci95": W.ci95(vals), "resamples": len(vals), "skipped": skipped,
            "reps": W.BOOT_N, "seed": W.BOOT_SEED}


def excludes_zero(ci):
    return bool(ci) and (ci[0] > 0 or ci[1] < 0)


def auc(pairs):
    pos = [p for p, y in pairs if y == 1]
    neg = sorted(p for p, y in pairs if y == 0)
    if not pos or not neg:
        return None
    s = 0.0
    for p in pos:
        lo = bisect.bisect_left(neg, p)
        hi = bisect.bisect_right(neg, p)
        s += lo + 0.5 * (hi - lo)
    return s / (len(pos) * len(neg))


def murphy(pairs):
    n = len(pairs)
    if not n:
        return None
    obar = mean([y for _, y in pairs])
    rel = res = 0.0
    for lo, hi in W.BINS:
        sub = [(p, y) for p, y in pairs if lo <= p * 100 < hi]
        if not sub:
            continue
        nk = len(sub)
        pk = mean([p for p, _ in sub])
        ok = mean([y for _, y in sub])
        rel += nk * (pk - ok) ** 2
        res += nk * (ok - obar) ** 2
    return {"n": n, "brier": r4(mean([(p - y) ** 2 for p, y in pairs])), "reliability": r4(rel / n),
            "resolution": r4(res / n), "uncertainty": r4(obar * (1 - obar))}


def load():
    led, rows, reg, defective = F.load()
    dpath = HERE / "domains.json"
    if not dpath.exists() or lf_sha256(dpath) != DOMAINS_SHA:
        print("REFUSE - domains.json is not the file committed with Section 16 (%s); the conflict "
              "set is defined by that file" % (lf_sha256(dpath)[:16] if dpath.exists() else "absent"))
        sys.exit(2)
    aliases = json.loads(dpath.read_text(encoding="utf-8"))["aliases"]
    runs = []
    rp = HERE / "forecasts" / "local_runs.jsonl"
    for ln in rp.read_text(encoding="utf-8").splitlines():
        if ln.strip():
            runs.append(json.loads(ln))
    preg = json.loads((HERE / "docs" / "packet_register.json").read_text(encoding="utf-8"))
    digests = {e.get("packet"): e.get("sha256") for e in preg.get("entries", [])}
    return led, rows, reg, defective, aliases, runs, digests


def main():
    ap = argparse.ArgumentParser(description="Kalibrierwarte Section 16 - the local succession reads")
    ap.add_argument("--counts-only", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-hash", action="store_true")
    a = ap.parse_args()
    self_lf = lf_sha256(Path(__file__).resolve())
    if a.self_hash:
        print("warte_local.py sha256 LF-normalised %s" % self_lf)
        return 0
    if a.write and a.counts_only:
        print("REFUSE - --write records a read; run it without --counts-only")
        return 2

    led, rows, reg, defective, aliases, runs, digests = load()
    cohort_full, cohort_rows, label = F.resolve_cohort(rows, COHORT)
    now = datetime.now(timezone.utc)
    today = now.strftime("%Y-%m-%d")

    def klass(dom):
        return aliases.get(str(dom or "").strip().lower(), "unclassified")

    def is_conflict(dom):
        return klass(dom) in CONFLICT

    # ---- rows in scope (16.7) and runs, by packet day
    scope = [r for r in cohort_rows if r.get("model") in ARMS and str(r.get("date_issued") or "")[:10] >= GATE_FROM]
    sealed = defaultdict(list)                       # (arm, day) -> rows
    for r in scope:
        sealed[(r["model"], str(r["date_issued"])[:10])].append(r)
    runs_by_day = defaultdict(list)
    for x in runs:
        d = str(x.get("ts") or "")[:10]
        if d >= FIRST_DAY and x.get("arm") in ARMS:
            runs_by_day[d].append(x)

    def one_run(rs, arm):
        got = [x for x in rs if x.get("arm") == arm]
        return got[0] if len(got) == 1 else (None if not got else "dup")

    # ---- (g') reference: the modal framed-minus-plain difference over the overlap
    ref = {}
    for plain, framed in PAIRS:
        diffs = []
        for d in sorted(runs_by_day):
            if not (OVERLAP[0] <= d <= OVERLAP[1]):
                continue
            pa, fr = one_run(runs_by_day[d], plain), one_run(runs_by_day[d], framed)
            if isinstance(pa, dict) and isinstance(fr, dict) and pa.get("prompt_tokens") is not None \
                    and fr.get("prompt_tokens") is not None:
                diffs.append(fr["prompt_tokens"] - pa["prompt_tokens"])
        if diffs:
            c = Counter(diffs).most_common()
            ref[(plain, framed)] = c[0][0]
            if len(c) > 1 and c[0][1] == c[1][1]:
                ref[(plain, framed)] = None          # no single mode: (g') cannot be fixed, printed
        else:
            ref[(plain, framed)] = None

    def day_checks(d):
        rs = runs_by_day.get(d, [])
        fails = []
        gates = {str(x.get("gate")) for x in rs}
        if len(gates) > 1:
            fails.append("(i) %d gate digests" % len(gates))
        for x in rs:
            if x.get("think_block") or x.get("reasoning_content"):
                fails.append("(j) reasoning output, %s" % x.get("arm"))
            key = str(reg.get(x.get("arm"), {}).get("model") or "")
            if str(x.get("response_model")) != key:
                fails.append("(h) %s served %s, registered %s" % (x.get("arm"), x.get("response_model"), key))
        s, t = one_run(rs, STOCK), one_run(rs, TWIN)
        if s is not None or t is not None:
            if not isinstance(s, dict) or not isinstance(t, dict):
                fails.append("(g) stock or twin run missing or duplicated")
            else:
                ds, dt = digests.get(s.get("packet")), digests.get(t.get("packet"))
                if not ds or not dt:
                    fails.append("(g) packet not in the register")
                elif ds != dt:
                    fails.append("(g) two packet digests")
                if s.get("prompt_tokens") is None or s.get("prompt_tokens") != t.get("prompt_tokens"):
                    fails.append("(g) prompt_tokens %s vs %s" % (s.get("prompt_tokens"), t.get("prompt_tokens")))
        for plain, framed in PAIRS:
            pa, fr = one_run(rs, plain), one_run(rs, framed)
            if pa == "dup" or fr == "dup":
                fails.append("(g') duplicate run, %s or %s" % (plain, framed))
            elif isinstance(pa, dict) and isinstance(fr, dict):
                if ref[(plain, framed)] is None:
                    fails.append("(g') no reference difference for %s" % framed)
                elif None in (pa.get("prompt_tokens"), fr.get("prompt_tokens")) or \
                        fr["prompt_tokens"] - pa["prompt_tokens"] != ref[(plain, framed)]:
                    fails.append("(g') %s minus %s off the reference %s" % (framed, plain, ref[(plain, framed)]))
        return fails

    days_all = sorted({d for d in runs_by_day} | {d for (_, d) in sealed if d >= FIRST_DAY})
    checks = {d: day_checks(d) for d in days_all}

    def P(arm, d, part=None):
        out = []
        for r in sealed.get((arm, d), []):
            p = p01(r.get("probability"))
            if p is None:
                continue
            if part == "conflict" and not is_conflict(r.get("domain")):
                continue
            if part == "other" and is_conflict(r.get("domain")):
                continue
            out.append(p)
        return out

    def k_ok(d, arms):
        return all(P(x, d) for x in arms)

    D7 = [d for d in days_all if not checks[d] and k_ok(d, (STOCK, TWIN))]
    D8 = [d for d in days_all if OVERLAP[0] <= d <= OVERLAP[1] and not checks[d]
          and k_ok(d, (STOCK, SFRAME, IPLAIN, IFRAME))]

    gen = {}
    for d, rs in runs_by_day.items():
        for x in rs:
            g = x.get("generated")
            if isinstance(g, list) and str(x.get("rubric_hash") or "").startswith(COHORT[:8]):
                if (x["arm"], d) in gen:
                    gen[(x["arm"], d)] = None        # two runs: no single record for the day
                else:
                    gen[(x["arm"], d)] = [(p01(e.get("p")), e.get("domain")) for e in g]

    def G(arm, d, part=None):
        out = []
        for p, dom in (gen.get((arm, d)) or []):
            if p is None:
                continue
            if part == "conflict" and not is_conflict(dom):
                continue
            if part == "other" and is_conflict(dom):
                continue
            out.append(p)
        return out

    def carries(d, arms):
        return all(gen.get((x, d)) for x in arms)

    rep = {"instrument": INSTRUMENT, "self_sha256": self_lf,
           "estimator": "warte_report.py " + lf_sha256(HERE / "warte_report.py")[:16],
           "frame_instrument": "warte_frame.py " + lf_sha256(HERE / "warte_frame.py")[:16],
           "registration": W.REGISTRATION,
           "registration_lf_sha16": (lf_sha256(HERE / W.REGISTRATION)[:16] if (HERE / W.REGISTRATION).exists() else None),
           "generated": now.isoformat(), "ledger_as_of": led.get("as_of"), "cohort": cohort_full,
           "inputs": {"local_runs_lf_sha16": lf_sha256(HERE / "forecasts" / "local_runs.jsonl")[:16],
                      "packet_register_lf_sha16": lf_sha256(HERE / "docs" / "packet_register.json")[:16],
                      "domains_lf_sha16": DOMAINS_SHA[:16]},
           "counts_only": a.counts_only,
           "scope": {"gate_from": GATE_FROM, "first_day": FIRST_DAY, "overlap": list(OVERLAP),
                     "g_prime_reference": {"%s - %s" % (fr, pa): v for (pa, fr), v in ref.items()},
                     "days": {d: {"checks_failed": checks[d],
                                  "sealed": {x: len(sealed.get((x, d), [])) for x in ARMS},
                                  "in_H7": d in D7, "in_H8": d in D8} for d in days_all}}}

    print("WARTE LOCAL - %s - %s - ledger %d rows as of %s" % (INSTRUMENT, label, len(rows), led.get("as_of")))
    print("estimator %s, frame instrument %s (imported, unchanged) - self %s" % (
        rep["estimator"].split()[1], rep["frame_instrument"].split()[1], self_lf[:16]))
    print("rows in scope (cohort %s, sealed from %s): %s" % (COHORT, GATE_FROM, ", ".join(
        "%s %d (void %d)" % (x, sum(len(v) for (y, _), v in sealed.items() if y == x),
                            sum(1 for (y, _), v in sealed.items() if y == x for r in v if r.get("status") == "void"))
        for x in ARMS)))
    print("(g') reference: %s" % ", ".join("%s - %s = %s" % (fr, pa, ref[(pa, fr)]) for pa, fr in PAIRS))
    failed = [(d, checks[d]) for d in days_all if checks[d]]
    print("16.8 day checks: %d day(s) from %s, %d failing" % (len(days_all), FIRST_DAY, len(failed)))
    for d, f in failed:
        print("   %s  %s" % (d, "; ".join(f)))
    print("in-scope days: H7 %d (stock and twin both sealed), H8 %d of the overlap (all four sealed)" % (len(D7), len(D8)))

    # ---------------------------------------------------------------- H7a
    h = {"needs": [STOCK, TWIN], "in_scope_days": len(D7), "read_after_days": H7_DAYS}
    if len(D7) >= H7_DAYS:
        days = D7[:H7_DAYS]
        h["read_point"] = days[-1]
        h["days"] = days
        if a.counts_only:
            h["result"] = "DUE - read point %s reached; not computed (--counts-only)" % days[-1]
        else:
            units = [sharp(P(TWIN, d)) - sharp(P(STOCK, d)) for d in days]
            b = boot(units, mean)
            h.update({"statistic": "mean over days of twin day-sharpness minus stock day-sharpness",
                      "point": r4(mean(units)), "bootstrap": b,
                      "result": ("SUPPORTED - the interval lies above zero" if b["ci95"] and b["ci95"][0] > 0
                                 else "NOT SUPPORTED - the interval includes zero or lies below it")})
            cd = [d for d in days if carries(d, (STOCK, TWIN))]
            if cd:
                cu = [sharp(G(TWIN, d)) - sharp(G(STOCK, d)) for d in cd if G(TWIN, d) and G(STOCK, d)]
                h["companion_16_12b"] = ({"days": len(cu), "point": r4(mean(cu)), "bootstrap": boot(cu, mean),
                                          "note": "every generated row, accepted and rejected; printed, never read as a test"}
                                         if cu else {"days": 0})
    else:
        h["result"] = "COUNTS - %d of %d in-scope days" % (len(D7), H7_DAYS)
    rep["H7a_sharpness"] = h

    # ---------------------------------------------------------------- H7b
    def h7b_counts(days):
        return {x: {"conflict": sum(len(P(x, d, "conflict")) for d in days),
                    "other": sum(len(P(x, d, "other")) for d in days)} for x in (STOCK, TWIN)}
    hb = {"needs": [STOCK, TWIN], "conflict_classes": list(CONFLICT)}
    rp = None
    for i in range(H7_DAYS - 1, len(D7)):
        c = h7b_counts(D7[:i + 1])
        if all(c[x]["conflict"] >= H7B_ROWS and c[x]["other"] >= H7B_ROWS for x in (STOCK, TWIN)):
            rp = i
            break
    hb["counts_to_date"] = h7b_counts(D7)
    if rp is None:
        hb["result"] = "COUNTS - read needs %d in-scope days and %d conflict and %d other rows per arm" % (
            H7_DAYS, H7B_ROWS, H7B_ROWS)
    else:
        days = D7[:rp + 1]
        hb["read_point"] = days[-1]
        hb["days"] = days
        if a.counts_only:
            hb["result"] = "DUE - read point %s reached; not computed (--counts-only)" % days[-1]
        else:
            units = [(P(TWIN, d, "conflict"), P(TWIN, d, "other"), P(STOCK, d, "conflict"), P(STOCK, d, "other"))
                     for d in days]

            def st(draw):
                tc = [p for u in draw for p in u[0]]
                to = [p for u in draw for p in u[1]]
                sc = [p for u in draw for p in u[2]]
                so = [p for u in draw for p in u[3]]
                if not (tc and to and sc and so):
                    return None
                return (mean(tc) - mean(sc)) - (mean(to) - mean(so))
            b = boot(units, st)
            hb.update({"statistic": "Dc - Do: (twin minus stock mean p, conflict rows) minus (the same, other rows)",
                       "point": r4(st(units)), "bootstrap": b,
                       "result": ("SUPPORTED - the interval lies above zero" if b["ci95"] and b["ci95"][0] > 0
                                  else "NOT SUPPORTED - the interval includes zero or lies below it")})
            cd = [d for d in days if carries(d, (STOCK, TWIN))]
            cu = [(G(TWIN, d, "conflict"), G(TWIN, d, "other"), G(STOCK, d, "conflict"), G(STOCK, d, "other")) for d in cd]
            hb["companion_16_12b"] = ({"days": len(cu), "point": r4(st(cu)), "bootstrap": boot(cu, st),
                                       "note": "every generated row; printed, never read as a test"} if cu else {"days": 0})
    rep["H7b_domain"] = hb

    # ---------------------------------------------------------------- H8
    h8 = {"needs": [STOCK, SFRAME, IPLAIN, IFRAME], "in_scope_overlap_days": len(D8), "days": D8}
    if today <= OVERLAP[1]:
        h8["result"] = "COUNTS - one read at the end of the overlap (%s)" % OVERLAP[1]
    elif not D8:
        h8["result"] = "NO IN-SCOPE DAY - nothing to read"
    elif a.counts_only:
        h8["result"] = "DUE - the overlap has ended; not computed (--counts-only)"
    else:
        for key, fn, name in (("H8a_location", mean, "day mean p"), ("H8b_sharpness", sharp, "day mean |p - 0.5|")):
            units = [(fn(P(SFRAME, d)), fn(P(STOCK, d)), fn(P(IFRAME, d)), fn(P(IPLAIN, d))) for d in D8]
            dd = [(u[0] - u[1]) - (u[2] - u[3]) for u in units]
            fs = [u[0] - u[1] for u in units]
            fi = [u[2] - u[3] for u in units]
            out = {"A": name, "D_point": r4(mean(dd)), "D_bootstrap": boot(dd, mean),
                   "frame_effect_successor_point": r4(mean(fs)), "frame_effect_successor_bootstrap": boot(fs, mean),
                   "frame_effect_incumbent_point": r4(mean(fi)), "frame_effect_incumbent_bootstrap": boot(fi, mean)}
            out["result"] = ("interval excludes zero" if excludes_zero(out["D_bootstrap"]["ci95"])
                             else "interval includes zero")
            cd = [d for d in D8 if carries(d, (STOCK, SFRAME, IPLAIN, IFRAME))]
            cu = [(fn(G(SFRAME, d)) - fn(G(STOCK, d))) - (fn(G(IFRAME, d)) - fn(G(IPLAIN, d))) for d in cd
                  if all(G(x, d) for x in (STOCK, SFRAME, IPLAIN, IFRAME))]
            out["companion_16_12b"] = ({"days": len(cu), "point": r4(mean(cu)), "bootstrap": boot(cu, mean),
                                        "note": "every generated row; printed, never read as a test"} if cu else {"days": 0})
            h8[key] = out
        h8["result"] = "READ - two-sided; see H8a and H8b"
    rep["H8_frame_by_version"] = h8

    # ---------------------------------------------------------------- H7c
    resolved = {x: sorted(((str(r.get("resolved_date") or ""), r) for r in scope
                           if r.get("model") == x and r.get("status") in ("hit", "miss")),
                          key=lambda t: (t[0], str(t[1].get("id")))) for x in (STOCK, TWIN)}
    hc = {"needs": [STOCK, TWIN], "checkpoint": W.CHECKPOINT,
          "resolved_in_cohort": {x: len(resolved[x]) for x in (STOCK, TWIN)}}
    cp = None
    if all(len(resolved[x]) >= W.CHECKPOINT for x in (STOCK, TWIN)):
        cp = max(resolved[x][W.CHECKPOINT - 1][0] for x in (STOCK, TWIN))
    if cp is None:
        hc["result"] = "COUNTS - read at the first checkpoint of both arms (%d resolved each)" % W.CHECKPOINT
    elif a.counts_only:
        hc["read_point"] = cp
        hc["result"] = "DUE - checkpoint %s reached; not computed (--counts-only)" % cp
    else:
        hc["read_point"] = cp
        days = [d for d in D7 if d <= cp]
        in_days = set(days)
        pairs = {x: [(p01(r.get("probability")), 1 if r["status"] == "hit" else 0) for rd, r in resolved[x]
                     if rd <= cp and str(r.get("date_issued"))[:10] in in_days and p01(r.get("probability")) is not None]
                 for x in (STOCK, TWIN)}
        comp = {}
        u1 = [(len(P(TWIN, d, "conflict")), len(P(TWIN, d)), len(P(STOCK, d, "conflict")), len(P(STOCK, d))) for d in days]

        def s1(draw):
            nt, ns = sum(u[1] for u in draw), sum(u[3] for u in draw)
            if not nt or not ns:
                return None
            return sum(u[0] for u in draw) / nt - sum(u[2] for u in draw) / ns
        comp["i_conflict_share"] = {"point": r4(s1(u1)), "bootstrap": boot(u1, s1)}
        u2 = [(P(TWIN, d, "other"), P(STOCK, d, "other")) for d in days]

        def s2(draw):
            t = [p for u in draw for p in u[0]]
            s = [p for u in draw for p in u[1]]
            return (sharp(t) - sharp(s)) if t and s else None

        def s5(draw):
            t = [p for u in draw for p in u[0]]
            s = [p for u in draw for p in u[1]]
            return (mean(t) - mean(s)) if t and s else None
        comp["ii_sharpness_outside_conflict"] = {"point": r4(s2(u2)), "bootstrap": boot(u2, s2)}
        rng = random.Random(W.BOOT_SEED)
        vals, skipped = [], 0
        ps, pt = pairs[STOCK], pairs[TWIN]
        for _ in range(W.BOOT_N):
            ds = [ps[rng.randrange(len(ps))] for _ in range(len(ps))] if ps else []
            dt = [pt[rng.randrange(len(pt))] for _ in range(len(pt))] if pt else []
            x1, x2 = auc(dt), auc(ds)
            if x1 is None or x2 is None:
                skipped += 1
            else:
                vals.append(x1 - x2)
        a_t, a_s = auc(pt), auc(ps)
        comp["iii_discrimination_auc"] = {"point": r4(a_t - a_s) if a_t is not None and a_s is not None else None,
                                          "auc_twin": r4(a_t), "auc_stock": r4(a_s),
                                          "resolved": {"twin": len(pt), "stock": len(ps)},
                                          "bootstrap": {"ci95": W.ci95(vals), "resamples": len(vals), "skipped": skipped,
                                                        "reps": W.BOOT_N, "seed": W.BOOT_SEED, "unit": "row, within each arm"}}

        def rate(x):
            if not isinstance(x, dict):
                return None
            if x.get("parse_failed"):
                return 0.0
            acc, rej = x.get("accepted") or 0, x.get("rejected") or 0
            return (acc / (acc + rej)) if (acc + rej) else 0.0
        days4 = [d for d in days_all if d <= cp and not checks[d]]
        u4 = [(rate(one_run(runs_by_day.get(d, []), TWIN)), rate(one_run(runs_by_day.get(d, []), STOCK))) for d in days4]

        def s4(draw):
            t = [u[0] for u in draw if u[0] is not None]
            s = [u[1] for u in draw if u[1] is not None]
            return (mean(t) - mean(s)) if t and s else None
        comp["iv_gate_acceptance"] = {"point": r4(s4(u4)), "days": len(u4), "bootstrap": boot(u4, s4)}
        comp["v_location_outside_conflict"] = {"point": r4(s5(u2)), "bootstrap": boot(u2, s5)}
        hc["components_twin_minus_stock"] = comp
        hc["brier_decomposition_descriptive"] = {"twin": murphy(pt), "stock": murphy(ps)}
        ex = {k: excludes_zero(v["bootstrap"]["ci95"]) for k, v in comp.items()}
        readings = []
        b7 = rep["H7b_domain"].get("result", "")
        if b7.startswith("SUPPORTED") or (comp["i_conflict_share"]["bootstrap"]["ci95"]
                                         and comp["i_conflict_share"]["bootstrap"]["ci95"][0] > 0):
            readings.append("refusal effect")
        if (ex["ii_sharpness_outside_conflict"] or ex["v_location_outside_conflict"]) and \
                not ex["iii_discrimination_auc"] and not ex["iv_gate_acceptance"]:
            readings.append("disposition effect")
        c3 = comp["iii_discrimination_auc"]["bootstrap"]["ci95"]
        c4 = comp["iv_gate_acceptance"]["bootstrap"]["ci95"]
        if (c3 and c3[1] < 0) or (c4 and c4[1] < 0):
            readings.append("capability cost")
        hc["reading"] = readings or ["mixed - component by component: %s" % ", ".join(
            "%s %s" % (k, "excludes zero" if v else "includes zero") for k, v in ex.items())]
        hc["result"] = "READ at the first checkpoint of both arms"
    rep["H7c_reading"] = hc

    # ---------------------------------------------------------------- H6 on the successor (16.3)
    h6 = {"plain": STOCK, "frame": SFRAME, "frame_population": FRAME_POP}
    srows = [r for r in scope if r["model"] == STOCK]
    frows_all = [r for r in scope if r["model"] == SFRAME]
    frows = [r for r in frows_all if str(r.get("frame_hash") or "").startswith(FRAME_POP)]
    h6["pre_revision_or_other_hash"] = len(frows_all) - len(frows)
    h6["resolved"] = {STOCK: sum(1 for r in srows if r["status"] in ("hit", "miss")),
                      SFRAME: sum(1 for r in frows if r["status"] in ("hit", "miss"))}
    if a.counts_only:
        h6["result"] = "COUNTS - %s resolved %d, %s resolved %d (checkpoint %d each)" % (
            STOCK, h6["resolved"][STOCK], SFRAME, h6["resolved"][SFRAME], W.CHECKPOINT)
    else:
        controls = [r for r in rows if r["model"] == W.CONTROL]
        ctl_cohort = [r for r in cohort_rows if r["model"] == W.CONTROL and r["status"] in ("hit", "miss")]
        ctl_all = [r for r in controls if r["status"] in ("hit", "miss")]
        plain = F.arm_report(STOCK, STOCK, srows, cohort_full, controls, ctl_cohort, ctl_all, defective)
        frame = F.arm_report(SFRAME + "[" + FRAME_POP + "]", SFRAME, frows, cohort_full, controls, ctl_cohort, ctl_all, defective)
        h6["verdict"] = F.h6(plain, frame)
        h6["result"] = h6["verdict"]["result"]
        h6["quality_all_pass"] = {STOCK: plain["quality"].get("all_pass"), SFRAME: frame["quality"].get("all_pass")}
    rep["H6_successor"] = h6

    # ---------------------------------------------------------------- print
    def ci(b):
        return b.get("ci95") if b else None
    print("-- H7a sharpness (16.5) -- %s" % h["result"])
    if "point" in h:
        print("   read point %s over %d days: point %s ci95 %s (%d resamples, %d skipped)" % (
            h["read_point"], len(h["days"]), h["point"], ci(h["bootstrap"]), h["bootstrap"]["resamples"], h["bootstrap"]["skipped"]))
        c = h.get("companion_16_12b") or {}
        if c.get("days"):
            print("   companion (16.12 b, never read as a test): %d days, point %s ci95 %s" % (c["days"], c["point"], ci(c["bootstrap"])))
    print("-- H7b domain (16.5) -- %s" % hb["result"])
    print("   rows in scope to date: %s" % ", ".join("%s conflict %d other %d" % (x, v["conflict"], v["other"])
                                                    for x, v in hb["counts_to_date"].items()))
    if "point" in hb:
        print("   read point %s: point %s ci95 %s" % (hb["read_point"], hb["point"], ci(hb["bootstrap"])))
        c = hb.get("companion_16_12b") or {}
        if c.get("days"):
            print("   companion (16.12 b, never read as a test): %d days, point %s ci95 %s" % (c["days"], c["point"], ci(c["bootstrap"])))
    print("-- H8 frame by version (16.6) -- %s; %d in-scope overlap days" % (h8["result"], len(D8)))
    for key in ("H8a_location", "H8b_sharpness"):
        if key in h8:
            o = h8[key]
            print("   %s (%s): D %s ci95 %s - %s; frame effect successor %s %s, incumbent %s %s" % (
                key, o["A"], o["D_point"], ci(o["D_bootstrap"]), o["result"],
                o["frame_effect_successor_point"], ci(o["frame_effect_successor_bootstrap"]),
                o["frame_effect_incumbent_point"], ci(o["frame_effect_incumbent_bootstrap"])))
            c = o.get("companion_16_12b") or {}
            if c.get("days"):
                print("      companion (16.12 b, never read as a test): %d days, D %s ci95 %s" % (c["days"], c["point"], ci(c["bootstrap"])))
    print("-- H7c reading (16.5) -- %s; resolved in cohort: %s" % (hc["result"], ", ".join(
        "%s %d" % (x, n) for x, n in hc["resolved_in_cohort"].items())))
    if "components_twin_minus_stock" in hc:
        for k, v in hc["components_twin_minus_stock"].items():
            print("   %-32s %s ci95 %s" % (k, v["point"], ci(v["bootstrap"])))
        print("   reading: %s" % "; ".join(hc["reading"]))
    print("-- H6 on the successor (16.3) -- %s" % h6["result"])
    if a.write:
        out = HERE / "forecasts" / ("warte_local_%s.json" % today)
        out.write_text(json.dumps(rep, indent=1) + "\n", encoding="utf-8")
        print("WARTE LOCAL - written %s (sha256 LF %s)" % (out, lf_sha256(out)[:16]))
    if a.json:
        print(json.dumps(rep, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
