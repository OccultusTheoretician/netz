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


# MAPWIDE-2026-09-15: the row's window when the resolution says "within the window" and no dates:
# the two dates in the resolution, else the statement's, else the row's own issue date and deadline.
def _row_window(e: dict, t: str):
    b = re.search(r"between\s+" + DATE + r"\s+and\s+" + DATE, t, re.I)
    if b and b.group(1) <= b.group(2):
        return (b.group(1), b.group(2)), None
    w = sorted(set(re.findall(DATE, t)))
    if len(w) >= 2:
        return (w[0], w[-1]), "window taken as the earliest and latest dates in the resolution"
    sw = sorted(set(re.findall(DATE, e.get("statement", "") or "")))
    if len(sw) >= 2:
        return (sw[0], sw[-1]), "window taken from the statement's dates"
    di, dl = str(e.get("date_issued", ""))[:10], str(e.get("deadline", ""))[:10]
    if re.match(r"\d{4}-\d{2}-\d{2}", di) and re.match(r"\d{4}-\d{2}-\d{2}", dl) and di <= dl:
        return (di, dl), "window taken from the row's issue date and deadline (the resolution says 'the window')"
    return None, None


# MAPWIDE-2026-09-15: bounding boxes (minlat, maxlat, minlon, maxlon), coarse by design; a proposal from this
# path says so and carries LOW confidence. Add a region only with its box.
USGS_REGIONS = {
    "Japan": (24.0, 46.0, 122.0, 146.0), "New Zealand": (-47.5, -34.0, 166.0, 179.0),
    "Chile": (-56.0, -17.0, -76.0, -66.0), "Indonesia": (-11.0, 6.0, 95.0, 141.0),
    "Turkey": (36.0, 42.0, 26.0, 45.0), "Mexico": (14.0, 33.0, -118.0, -86.0),
    "California": (32.5, 42.0, -124.5, -114.0), "Alaska": (51.0, 72.0, -170.0, -130.0),
    "Taiwan": (21.5, 25.5, 119.5, 122.5), "Philippines": (4.5, 21.0, 116.0, 127.0),
    "Italy": (36.0, 47.5, 6.0, 19.0), "Greece": (34.5, 42.0, 19.0, 30.0),
    "Iran": (25.0, 40.0, 44.0, 64.0), "Pakistan": (23.5, 37.0, 60.5, 77.5),
    "Nepal": (26.0, 31.0, 80.0, 89.0), "Peru": (-18.5, 0.0, -81.5, -68.5),
    "Papua New Guinea": (-12.0, 0.0, 140.0, 156.0), "Pacific Northwest": (42.0, 49.5, -125.0, -116.5),
    "Vanuatu": (-20.5, -13.0, 166.0, 170.5), "Tonga": (-23.0, -15.0, -177.0, -173.0),
    "Kamchatka": (50.0, 62.0, 155.0, 165.0), "Myanmar": (9.5, 28.5, 92.0, 101.5),
    "Afghanistan": (29.4, 38.5, 60.5, 75.0),
}

# MAPWIDE-2026-09-15: a candidate name, cleaned: trailing punctuation off, the arms' suffixes
# ("Certighost-related", "Check Point-vendor", "Tencent-app") off, stop-words out, nothing under three
# characters unless it carries a digit (n8n), nothing that is plainly a phrase.
def _kev_norm(nm):
    nm = " ".join(x.strip(".,;:()\"'") for x in str(nm).split())
    nm = re.sub(r"-(?:related|vendor|app|based|family|branded)$", "", nm)
    toks = [x for x in nm.split() if x not in KEV_STOP]
    nm = " ".join(toks).strip()
    if not nm or nm in KEV_STOP or len(nm) > 40 or " the " in nm or " or " in nm:
        return None
    if len(nm) < 3 and not re.search(r"\d", nm):
        return None
    if re.fullmatch(r"[A-Z]{2,5}", nm) or re.fullmatch(r"[A-Z]\.[A-Z]\.?", nm):
        return None
    if "XXXX" in nm or nm in KEV_GENERIC_SINGLE:
        return None
    return nm


# MAPWIDE-2026-09-15: words a capitalised run in a KEV resolution is not a vendor or product.
KEV_STOP = set("""CISA KEV Known Exploited Vulnerabilities Vulnerability Catalog JSON CVE CVEs RCE TRUE FALSE YES NO True False Yes No
The A An If Any Otherwise Resolved Resolves Resolution Entry Entries Vendor Product VendorProject Field Date Added
January February March April May June July August September October November December
Monday Tuesday Wednesday Thursday Friday Saturday Sunday US U.S. United States Public This That With Between And Or
Late Early Mid New Two One Three Four Five Six Seven Eight Nine Ten At In On By For From To Of As Unknown
Server Status Count Wild Adjudicated News Hacker Center Management Engine Protection Software Open Source Secure Cloud
Zero Day Flaws Pre-existing Kyiv BleepingComputer Advisory Chain Exploitation Catalog Feed Page Report Window""".split())
# MAPWIDE-2026-09-15: single generic tokens a substring match would hit on half the catalog.
KEV_GENERIC_SINGLE = set("Server Engine Center Management Gateway Client Agent Manager Console Portal Service Services Platform Suite Tools".split())


def map_row(e: dict):
    """Return (resolver_name, params) or (None, why_unmapped)."""
    t = " ".join((e.get("resolution") or "").split())
    tl = t.lower()

    if re.search(r"kev catalog|known exploited", tl):
        # MAPWIDE-2026-09-15: the names the arms write, in the forms they write them.
        window, wnote = _row_window(e, t)
        if re.search(r"other than|excluding|additional|second entry|a second", tl):
            return None, "KEV-shaped but the predicate excludes named entries or counts a second one - operator adjudication"
        cnt = re.search(r"(\d+)\s+or more entries|at least\s+(\d+)\s+entries", tl)
        if cnt and window:
            return "kev", {"vendor": "(count)", "vendors": [], "min_count": int(cnt.group(1) or cnt.group(2)),
                           "window": window, "_note": wnote}
        names = []
        m = re.search(r"(?:vendorproject or product matching|matching)\s+"
                      r"([A-Za-z0-9._ -]+?)(?:\s+and\b|,|\.)", t, re.I)
        if m and len(m.group(1)) <= 40 and " the " not in m.group(1):
            names.append(m.group(1).strip())
        # a lowercase product named outright ("naming n8n", "names n8n")
        for mm in re.finditer(r"\b(?:naming|names|named)\s+([a-z0-9][A-Za-z0-9._-]*)", t):
            nm = mm.group(1).strip().rstrip(",.")
            if nm not in KEV_STOP and nm not in names:
                names.append(nm)
        # capitalised runs of one to three tokens (a token may carry digits or hyphens: N-able, N-central, TP-Link)
        for mm in re.finditer(r"\b([A-Z][A-Za-z0-9._-]*(?:\s+[A-Z][A-Za-z0-9._-]*){0,2})\b", t):
            nm = mm.group(1).strip().rstrip(",.")
            toks = [x for x in nm.split() if x not in KEV_STOP]
            nm = " ".join(toks)
            if nm and nm not in names and not re.fullmatch(r"[A-Z]{2,5}", nm):
                names.append(nm)
        clean = []
        for nm in names:
            nm = _kev_norm(nm)
            if nm and nm not in clean:
                clean.append(nm)
        if clean and window:
            return "kev", {"vendor": clean[0], "vendors": clean, "window": window, "_note": wnote}
        return None, "KEV-shaped but vendor/window not extractable"

    if "fdsn" in tl or "usgs" in tl or "earthquake" in tl:
        # MAPWIDE-2026-09-15: a compound predicate the feed cannot see stays unmapped.
        if re.search(r"death|fatalit|casualt|killed|injur|damage|tsunami|collapse|displac|depth", tl):
            return None, "USGS-shaped but the predicate needs deaths, casualties, damage, depth or a tsunami - not checked by the feed read"
        r = re.search(r"radius\s+(\d+)\s*km", tl)
        mg = re.search(r"minmagnitude\s+(\d+(?:\.\d+)?)|magnitude\s+(?:of\s+)?(\d+(?:\.\d+)?)", tl)
        w = re.findall(DATE, t)
        lat = re.search(r"latitude[= ]([\-\d.]+)", tl)
        lon = re.search(r"longitude[= ]([\-\d.]+)", tl)
        if r and mg and len(w) >= 2:
            p = {"radius_km": int(r.group(1)),
                 "min_mag": float(mg.group(1) or mg.group(2)),
                 "window": (w[-2], w[-1]),
                 "lat": float(lat.group(1)) if lat else 32.69,
                 "lon": float(lon.group(1)) if lon else 130.66}
            note = None if lat else ("epicentre coordinates not in text - "
                                     "using Uto 2026-07-28 (32.69, 130.66); "
                                     "confirm before trusting")
            return "usgs", {**p, "_note": note}
        if mg and re.search(r"within\s+\d+\s*km|\d+\s*km of", tl) and not (lat and lon):
            return None, "USGS-shaped radius predicate without epicentre coordinates - not extractable"
        if mg:
            region = None
            best = None
            for name, box in USGS_REGIONS.items():
                pos = re.search(r"\b" + re.escape(name.lower()) + r"\b", tl)
                if pos and (best is None or pos.start() < best):
                    best, region = pos.start(), (name, box)
            window, wnote = _row_window(e, t)
            if region and window:
                name, box = region
                note = ("region '%s' as a bounding box (lat %s..%s, lon %s..%s): a box is not a border - "
                        "confirm the epicentre's country before ruling" % (name, box[0], box[1], box[2], box[3]))
                return "usgs", {"bbox": box, "region": name,
                                "min_mag": float(mg.group(1) or mg.group(2)),
                                "window": window, "_note": (note + ("; " + wnote if wnote else ""))}
        return None, "USGS-shaped but radius/magnitude/window not extractable"

    if "bc_10year" in tl or re.search(r"bc_\d+year", tl) or ("treasury" in tl and "yield" in tl):
        # MAPWIDE-2026-09-15: tenor, threshold phrasing and direction.
        ten = re.search(r"bc_(\d+)year", tl) or re.search(r"\b(2|5|10|30)-year\b", tl)
        tenor = ten.group(1) if ten else None
        th = None
        direction = None
        for pat, d in ((r"(?:at or above|>=|reaches|reach|hits|touches|at least)\s*(\d+(?:\.\d+)?)\s*(?:percent|%)?(?:\s+or\s+(?:higher|above|more))?", ">="),
                       (r"(\d+(?:\.\d+)?)\s*(?:percent|%)\s+or\s+(?:higher|above|more)", ">="),
                       (r"(?:above|exceeds|exceeding|over|greater than|higher than|>)\s*(\d+(?:\.\d+)?)", ">"),
                       (r"(?:at or below|<=|falls to|fall to|declines to|drops to)\s*(\d+(?:\.\d+)?)\s*(?:percent|%)?(?:\s+or\s+(?:lower|below|less))?", "<="),
                       (r"(\d+(?:\.\d+)?)\s*(?:percent|%)\s+or\s+(?:lower|below|less)", "<="),
                       (r"(?:below|under|less than|lower than|<)\s*(\d+(?:\.\d+)?)", "<")):
            mm = re.search(pat, tl)
            if mm:
                th, direction = float(mm.group(1)), d
                break
        window, wnote = _row_window(e, t)
        if th is not None and window and tenor in ("2", "5", "10", "30"):
            return "treasury10y", {"threshold": th, "window": window, "tenor": tenor,
                                   "direction": direction, "_note": wnote}
        if th is not None and window and tenor:
            return None, "Treasury-shaped but the %s-year tenor is not a field this resolver reads" % tenor
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
        # KK28-TOOLWORK unpark: the KK23 guard's own removal condition is
        # met — resolve_gdacs reads the alert level STRUCTURALLY since KK21k
        # (namespaced element, then title-prefix, refusing body-text
        # inference, which was the 2026-08-04 false positive's channel).
        # First-run discipline still applies: smoke before trusting —
        #     python mechanical_adjudicator.py --smoke --keep-raw
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
