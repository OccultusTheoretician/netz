#!/usr/bin/env python3
"""
mechanical_adjudicator.py — blind adjudication's mechanical half.

Maps each open row's resolution basis (machine-written, regular prose) onto a
resolver in resolvers.py, extracts the predicate's parameters by pattern,
fetches the named instrument, and PROPOSES a verdict with a hashed evidence
record. It writes nothing to the ledger — `kkr --resolve` remains the only
resolution path — and it never sees the arm or the probability while judging,
which is what makes the adjudication blind by construction.

    python mechanical_adjudicator.py --coverage      map every open row, fetch nothing
    python mechanical_adjudicator.py --due           fetch + propose for past-deadline rows
    python mechanical_adjudicator.py --row KKR-...   one row
    python mechanical_adjudicator.py --due --keep-raw    also keep raw response bytes

First-run discipline: every resolver is SCHEMA-UNVERIFIED until it has parsed
its live endpoint once from this desk. Run --due and read the INDETERMINATEs
before trusting anything; a resolver that cannot find exactly what it expects
proposes nothing.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import resolvers

HERE = Path(__file__).resolve().parent
DATE = r"(\d{4}-\d{2}-\d{2})"


def map_row(e: dict):
    """Return (resolver_name, params) or (None, why_unmapped)."""
    t = " ".join((e.get("resolution") or "").split())
    tl = t.lower()

    if re.search(r"kev catalog|known exploited", tl):
        m = re.search(r"(?:vendorproject or product matching|matching)\s+"
                      r"([A-Za-z0-9._ -]+?)(?:\s+and\b|,|\.)", t, re.I)
        w = re.findall(DATE, t)
        if len(w) < 2:
            w = re.findall(DATE, e.get("statement", ""))
        if m and len(w) >= 2:
            return "kev", {"vendor": m.group(1).strip(),
                           "window": (w[-2], w[-1])}
        return None, "KEV-shaped but vendor/window not extractable"

    if "fdsn" in tl or "usgs" in tl:
        r = re.search(r"radius\s+(\d+)\s*km", tl)
        mg = re.search(r"minmagnitude\s+(\d+(?:\.\d+)?)|magnitude\s+(\d+(?:\.\d+)?)", tl)
        w = re.findall(DATE, t)
        lat = re.search(r"latitude[= ]([\-\d.]+)", tl)
        lon = re.search(r"longitude[= ]([\-\d.]+)", tl)
        if r and mg and len(w) >= 2:
            p = {"radius_km": int(r.group(1)),
                 "min_mag": float(mg.group(1) or mg.group(2)),
                 "window": (w[-2], w[-1]),
                 "lat": float(lat.group(1)) if lat else 32.69,
                 "lon": float(lon.group(1)) if lon else 130.66}
            note = None if lat else ("epicentre coordinates not in text — " 
                                     "using Uto 2026-07-28 (32.69, 130.66); "
                                     "confirm before trusting")
            return "usgs", {**p, "_note": note}
        return None, "USGS-shaped but radius/magnitude/window not extractable"

    if "bc_10year" in tl or ("treasury" in tl and "yield" in tl):
        th = re.search(r"(?:at or above|>=)\s*(\d+(?:\.\d+)?)", tl)
        w = re.findall(DATE, t)
        stmt_w = re.findall(DATE, e.get("statement", ""))
        window = (w[-2], w[-1]) if len(w) >= 2 else (
            (stmt_w[-2], stmt_w[-1]) if len(stmt_w) >= 2 else None)
        if th and window:
            return "treasury10y", {"threshold": float(th.group(1)),
                                   "window": window}
        return None, "Treasury-shaped but threshold/window not extractable"

    if "ecb data portal" in tl or "ecb" in tl and "series" in tl:
        s = re.search(r"series\s+([A-Z0-9._]+)", t)
        w = re.findall(DATE, t + " " + e.get("statement", ""))
        if s and len(w) >= 2:
            fs = s.group(1)
            if "/" not in fs:
                fs = fs.split(".", 1)
                fs = f"{fs[0]}/{fs[1]}"
            return "ecb", {"flow_series": fs,
                           "baseline_date": min(w), "compare_date": max(w),
                           "predicate": "unchanged"}
        return None, "ECB-shaped but series/dates not extractable"

    if "federal register" in tl:
        w = re.findall(DATE, t + " " + e.get("statement", ""))
        term = "Iranian" if "iranian" in tl or "iran" in tl else None
        ags = []
        if "treasury" in tl:
            ags.append("treasury-department")
        if "state" in tl:
            ags.append("state-department")
        if term and len(w) >= 2:
            return "fedreg", {"term": term, "agencies": ags or
                              ["treasury-department"],
                              "window": (min(w), max(w))}
        return None, "FedReg-shaped but term/window not extractable"

    if "gdacs" in tl:
        # KK23 guard (doctrine from jury_log entry one, generalised): a
        # resolver with a known false-positive class abstains on any predicate
        # containing its failure token until the matcher is fixed. The gdacs
        # matcher substring-matches flattened item text and returned YES on a
        # Green alert against a red predicate (smoke 2026-08-04) -- the
        # dangerous direction. Every mappable gdacs row carries a level token,
        # so this guard parks the whole resolver on operator adjudication.
        # REMOVE only when the matcher parses the alert-level FIELD and a
        # Green-vs-red smoke returns NO.
        _tok = re.search(r"\b(green|orange|red)\b", tl)
        if _tok:
            return None, (f"gdacs ABSTAIN (KK23 guard): predicate contains "
                          f"alert-level token '{_tok.group(1)}' and the "
                          f"matcher has a documented false-positive on alert "
                          f"levels (smoke 2026-08-04: YES on Green against a "
                          f"red predicate) -- operator adjudication until the "
                          f"matcher parses the alert-level field")
        lvl = re.search(r"alertlevel\s+(\w+)|(\bred\b|\borange\b)", tl)
        cty = re.search(r"country\s+(\w+)|\bin\s+([A-Z]\w+)", t)
        w = re.findall(DATE, t)
        if lvl and cty:
            return "gdacs", {"alertlevel": (lvl.group(1) or lvl.group(2)),
                             "country": (cty.group(1) or cty.group(2)),
                             "window": (w[-2], w[-1]) if len(w) >= 2 else None}
        return None, "GDACS-shaped but level/country not extractable"

    for tag, why in (("ice brent", "official ICE settlement series is "
                      "licensed — the standing probe governs"),
                     ("nymex", "official NYMEX settlement is licensed — "
                      "the standing probe governs"),
                     ("s&p 500", "official index settlement is licensed — "
                      "the standing probe governs"),
                     ("nasdaq", "official index settlement is licensed — "
                      "the standing probe governs")):
        if tag in tl:
            return None, why
    return None, "resolution basis is a statement/press-release shape — a " \
                 "search problem, not a feed read; operator adjudication"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--coverage", action="store_true")
    ap.add_argument("--due", action="store_true")
    ap.add_argument("--row")
    ap.add_argument("--keep-raw", action="store_true")
    ap.add_argument("--smoke", action="store_true",
                    help="one row per resolver, regardless of deadline, forced "
                         "probe. Verifies all six parsers against their live "
                         "endpoints in one command. Writes probe records that "
                         "cannot be mistaken for resolving evidence.")
    a = ap.parse_args()

    rows = json.loads((HERE / "ledger.json").read_text(
        encoding="utf-8"))["projections"]
    open_rows = [e for e in rows if e.get("status") == "open"]
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    if a.smoke:
        seen, picked = set(), []
        for e in open_rows:
            name, params = map_row(e)
            if name and name not in seen:
                seen.add(name)
                picked.append((name, params, e))
        if not picked:
            print("no mappable open rows — nothing to smoke")
            return 1
        print(f"\nPARSER SMOKE TEST — {len(picked)} resolver(s), forced probe")
        print("-" * 66)
        print("These fetches prove the parsers read their endpoints. They are")
        print("NOT adjudications: every record is written with probe=true and")
        print("carries a line saying it must not be cited in a resolution.\n")
        bad = 0
        for name, params, e in picked:
            resolvers.set_row_context(deadline=e.get("deadline"), probe=True)
            try:
                meta = resolvers.REGISTRY[name](e["id"], params,
                                                keep_raw=a.keep_raw)
                v = meta.get("verdict_if_resolved_now",
                             meta.get("verdict_proposed", "?"))
                mark = "ok  " if v != "INDETERMINATE" else "IND "
                if v == "INDETERMINATE":
                    bad += 1
                print(f"  {mark} {name:<12} {e['id']:<18} {v:<14} "
                      f"{str(meta.get('detail',''))[:44]}")
            except Exception as ex:
                bad += 1
                print(f"  FAIL {name:<12} {e['id']:<18} {type(ex).__name__}: "
                      f"{str(ex)[:44]}")
            finally:
                resolvers.set_row_context()
        print(f"\n  {len(picked) - bad} of {len(picked)} parser(s) returned a "
              f"determinate read. An INDETERMINATE is the resolver refusing to "
              f"guess, which is correct behaviour and still a parser that "
              f"cannot yet be trusted.")
        return 0

    if a.coverage or not (a.due or a.row):
        mapped = {}
        unmapped = {}
        for e in open_rows:
            name, p = map_row(e)
            if name:
                mapped.setdefault(name, []).append(e["id"])
            else:
                unmapped.setdefault(p, []).append(e["id"])
        print(f"\nMECHANICAL COVERAGE — {len(open_rows)} open rows, {today}")
        print("-" * 66)
        n_m = sum(len(v) for v in mapped.values())
        for k in sorted(mapped):
            print(f"  {k:12s} {len(mapped[k]):3d}  {', '.join(mapped[k][:5])}"
                  + (" …" if len(mapped[k]) > 5 else ""))
        print(f"  {'':12s} ---")
        print(f"  mappable     {n_m:3d} of {len(open_rows)} "
              f"({100*n_m/len(open_rows):.0f}%)")
        print(f"\n  UNMAPPED, by reason (printed, because the gap is the "
              f"finding):")
        for why in sorted(unmapped, key=lambda w: -len(unmapped[w])):
            print(f"    {len(unmapped[why]):3d} · {why}")
        print(f"\n  A resolver proposes; it never resolves. `kkr --resolve` "
              f"is the only resolution path.")
        return 0

    targets = []
    if a.row:
        targets = [e for e in open_rows if e.get("id") == a.row]
        if not targets:
            print(f"no open row {a.row}", file=sys.stderr)
            return 1
    elif a.due:
        targets = [e for e in open_rows
                   # KK21i: was <=, which adjudicated rows deadlined TODAY.
                   # kkr --resolve uses <, and the settling-margin rule (KK19)
                   # is the reason: third-party confirmation does not exist on
                   # the morning the resolver walks the row.
                   if str(e.get("deadline", "9999")) < today]
        if not targets:
            print("nothing past deadline")
            return 0

    print(f"\nMECHANICAL PROPOSALS — {len(targets)} row(s), evidence to "
          f"evidence/")
    print("-" * 66)
    for e in targets:
        name, p = map_row(e)
        if not name:
            print(f"  {e['id']}: UNMAPPED — {p}")
            continue
        note = p.pop("_note", None)
        try:
            resolvers.set_row_context(deadline=e.get("deadline"), probe=False)
            meta = resolvers.REGISTRY[name](e["id"], p, keep_raw=a.keep_raw)
            resolvers.set_row_context()
        except Exception as ex:
            print(f"  {e['id']}: FETCH FAILED ({name}) — {ex}. No evidence "
                  f"written, nothing proposed.")
            continue
        print(f"  {e['id']}: {meta['verdict_proposed']} · {name} · "
              f"{meta['detail'][:100]}")
        print(f"      evidence sha256 {meta['sha256_raw'][:16]}… · "
              f"{meta['fetched_at']}")
        if note:
            print(f"      NOTE: {note}")
    print(f"\n  Confirm any proposal yourself, then resolve via "
          f"`python kkr.py --resolve`, citing the evidence file in the "
          f"row's audit note.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
