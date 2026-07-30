#!/usr/bin/env python3
"""
wire_baseline.py — NETZ War Desk · Gap 2: the neutral baseline.

THE GAP THIS CLOSES

    tg_grade confirms an event when hostile BELLIGERENTS agree. That is a real
    method and it survives the obvious attack — three Kremlin-aligned outlets
    are one voice, and the grader counts sides, not labels.

    It does not survive a subtler one. Belligerents can be correlated without
    being coordinated: both sides amplify the same framing because both have
    reason to, and nothing in the corpus can tell that apart from two
    independent observations of one event. A claim can clear Grade B with two
    genuinely hostile sides and still have no neutral confirmation anywhere.

    So this adds a third tier that is not a belligerent: GDELT, a global index
    of news coverage with tone and theme extraction, free and queryable. The
    measurement is the DIVERGENCE — what the sides are saying, minus what the
    wire record carries.

        CONFIRMED      belligerent claim + wire coverage of the same anchor
        WIRE-SILENT    belligerent claim, no wire coverage in the window
        WIRE-ONLY      wire coverage the watched channels never mentioned

    WIRE-SILENT is the interesting column. Heavy belligerent framing with no
    neutral pickup is either propaganda preparing ground, or a real event the
    wires have not reached yet, or a watched-set artifact. It is not evidence of
    falsity. What it is, reliably, is a claim that has not been corroborated
    outside the belligerent set — and printing that count next to the grades is
    the honest thing this desk was missing.

WHAT THIS IS NOT

    Not a truth oracle. GDELT indexes coverage, not facts; a wire can be wrong
    and often is early. Absence of coverage is absence of coverage. WIRE-ONLY
    rows are equally a finding about the CHANNEL REGISTRY — a zone the watched
    set does not cover — and are printed as such rather than as a scoop.

    GDELT's own known limits ride every row: coverage skews Anglophone and
    online-indexed, its geocoding is automated and errs, and its 15-minute
    update cadence means a very recent event legitimately shows as wire-silent.

NETWORK POSTURE

    Commit-time only, from the operator's machine. The served pages never call
    out — site_audit enforces that and the property is an asset. This writes a
    JSON artifact that the pages read like any other tile.

USE
    python wire_baseline.py --events forecasts/tg_events_YYYY-MM-DD_HHMM.json
    python wire_baseline.py --latest
    python wire_baseline.py --latest --hours 48
    python wire_baseline.py --selftest        parse fixtures, no network
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
FORECASTS = HERE / "forecasts"
DOCS = HERE / "docs"

GDELT_DOC = "https://api.gdeltproject.org/api/v2/doc/doc"
UA = "netz-wire-baseline/1.0 (+https://retroprescientaudit.com)"


def newest(pattern):
    hits = sorted(FORECASTS.glob(pattern))
    return hits[-1] if hits else None


def parse_ts(v):
    if not v:
        return None
    s = str(v).replace("Z", "+00:00")
    try:
        d = datetime.fromisoformat(s)
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


# DEFECTS, 2026-07-30, all four measured on the first live run:
#   1. 45 queries fired for 19 unique terms — anchors repeat across events
#      (tehran x4, blockade x4, crimea x4) and every duplicate was re-queried.
#   2. No delay between queries. GDELT throttles at roughly one query per five
#      seconds; 45 back-to-back requests earned HTTP 429 and then SSL handshake
#      timeouts as the throttling escalated.
#   3. No retry. A 429 was terminal for that term.
#   4. An event where one term answered and another 429'd was classified
#      CONFIRMED while still printing the error — a partially measured event
#      reported as a clean confirmation. That is the stated-versus-operational
#      gap in miniature, in the tool that exists to measure it.
_CACHE = {}
_LAST_CALL = [0.0]


def _throttle(min_gap):
    wait = min_gap - (time.monotonic() - _LAST_CALL[0])
    if wait > 0:
        time.sleep(wait)
    _LAST_CALL[0] = time.monotonic()


def gdelt_cached(term, start, end, min_gap=5.0, retries=2, timeout=30):
    """One network call per distinct (term, window), throttled and retried."""
    key = (term.lower(), start.strftime("%Y%m%d%H%M"), end.strftime("%Y%m%d%H%M"))
    if key in _CACHE:
        return _CACHE[key]
    delay = min_gap
    for attempt in range(retries + 1):
        _throttle(min_gap)
        arts, err = gdelt_query(term, start, end, timeout=timeout)
        if err and ("429" in err or "timed out" in err.lower()
                    or "handshake" in err.lower()):
            if attempt < retries:
                delay *= 2
                print(f"    throttled on '{term}' ({err}) — backing off "
                      f"{delay:.0f}s", file=sys.stderr)
                time.sleep(delay)
                continue
        _CACHE[key] = (arts, err)
        return arts, err
    _CACHE[key] = (None, "throttled after retries")
    return _CACHE[key]


def gdelt_query(term, start, end, timeout=30, maxrecords=75):
    """One GDELT DOC 2.0 query. Returns (articles, error_or_None).

    Never raises on a network problem: an unreachable wire index must read as
    'not measured', never as 'no coverage'. Those are different facts and
    conflating them would invent a finding.
    """
    q = {
        "query": f'"{term}" sourcelang:english',
        "mode": "artlist",
        "format": "json",
        "maxrecords": str(maxrecords),
        "startdatetime": start.strftime("%Y%m%d%H%M%S"),
        "enddatetime": end.strftime("%Y%m%d%H%M%S"),
        "sort": "datedesc",
    }
    url = GDELT_DOC + "?" + urllib.parse.urlencode(q)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code}"
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"
    return parse_gdelt(raw)


def parse_gdelt(raw):
    """GDELT returns JSON, but on rate-limit or malformed query it returns
    prose with a 200. Parsing must survive that rather than crash a run."""
    raw = (raw or "").strip()
    if not raw:
        return None, "empty response"
    if not raw.startswith("{"):
        return None, "non-JSON response: " + raw[:120].replace("\n", " ")
    try:
        d = json.loads(raw)
    except json.JSONDecodeError as e:
        return None, f"JSON decode failed: {e}"
    arts = d.get("articles")
    if arts is None:
        return [], None          # a valid empty result is not an error
    out = []
    for a in arts:
        if not isinstance(a, dict):
            continue
        out.append({
            "title": (a.get("title") or "")[:200],
            "domain": a.get("domain") or "",
            "url": a.get("url") or "",
            "seendate": a.get("seendate") or "",
            "language": a.get("language") or "",
        })
    return out, None


def anchors_of(ev):
    a = ev.get("anchor") or []
    a = a if isinstance(a, list) else [a]
    terms = [str(x) for x in a if x]
    for v in (ev.get("anchor_aliases") or []):
        if v:
            terms.append(str(v))
    seen, out = set(), []
    for t in terms:
        k = t.lower().strip()
        if k and k not in seen:
            seen.add(k)
            out.append(t)
    return out


GRADE_ORDER = {"A": 0, "B": 1, "C": 2, "F": 3}


def classify(n_articles, n_ok, n_failed):
    """n_ok / n_failed count TERMS, not articles.

    A term that never got an answer cannot contribute silence. So:
      no term answered            -> NOT-MEASURED (we did not ask successfully)
      some answered, some failed  -> PARTIAL-* (say which, never launder it)
      all answered                -> CONFIRMED / WIRE-SILENT
    """
    if n_ok == 0:
        return "NOT-MEASURED"
    if n_failed:
        return "PARTIAL-CONFIRMED" if n_articles > 0 else "PARTIAL-SILENT"
    return "CONFIRMED" if n_articles > 0 else "WIRE-SILENT"


def selftest():
    """Parsing is verified against fixtures because the live index is not
    reachable from every environment, and a parser that has only ever been
    tried against one live response is untested."""
    cases = [
        ("well-formed with articles",
         json.dumps({"articles": [
             {"title": "Strike reported near Kherson", "domain": "reuters.com",
              "url": "https://reuters.com/x", "seendate": "20260727T101500Z",
              "language": "English"}]}),
         1, None),
        ("well-formed empty", json.dumps({"articles": []}), 0, None),
        ("valid JSON, no articles key", json.dumps({"status": "ok"}), 0, None),
        ("rate-limit prose with HTTP 200",
         "Your query rate is too high. Please wait.", None, "non-JSON"),
        ("empty body", "", None, "empty"),
        ("truncated JSON", '{"articles": [{"title": "x"', None, "decode"),
    ]
    ok = True
    for name, raw, want_n, want_err in cases:
        arts, err = parse_gdelt(raw)
        if want_err:
            good = err is not None and want_err.lower() in err.lower()
        else:
            good = err is None and len(arts) == want_n
        print(f"  {'PASS' if good else 'FAIL'}  {name}"
              + ("" if good else f"  → arts={arts} err={err}"))
        ok = ok and good
    # classification must never turn an error into a finding
    checks = [
        (classify(0, 2, 0), "WIRE-SILENT"),
        (classify(3, 2, 0), "CONFIRMED"),
        (classify(0, 0, 2), "NOT-MEASURED"),
        (classify(10, 1, 1), "PARTIAL-CONFIRMED"),
        (classify(0, 1, 1), "PARTIAL-SILENT"),
    ]
    for got, want in checks:
        good = got == want
        print(f"  {'PASS' if good else 'FAIL'}  classify → {got} (want {want})")
        ok = ok and good
    print("\n  An unreachable index reads NOT-MEASURED, never WIRE-SILENT — "
          "absence of\n  measurement and absence of coverage are different "
          "facts. An event where one\n  term answered and another did not "
          "reads PARTIAL, never CONFIRMED.")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description="Gap 2: neutral wire baseline")
    ap.add_argument("--events")
    ap.add_argument("--latest", action="store_true")
    ap.add_argument("--hours", type=int, default=36,
                    help="wire window around each event's first_seen")
    ap.add_argument("--min-grade", default="B", choices=list("ABCF"))
    ap.add_argument("--min-gap", type=float, default=5.0,
                    help="seconds between network calls; GDELT throttles at "
                         "roughly one query per five seconds")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    if a.selftest:
        print("wire_baseline parser selftest — no network")
        return selftest()

    ev_path = Path(a.events) if a.events else (
        newest("tg_events_*.json") if a.latest else None)
    if not ev_path or not ev_path.exists():
        print("Need --events or --latest.", file=sys.stderr)
        return 1
    events = json.loads(ev_path.read_text(encoding="utf-8")).get("events", [])
    floor = GRADE_ORDER[a.min_grade]
    graded = [e for e in events
              if GRADE_ORDER.get(str(e.get("grade", "F"))[0], 3) <= floor]
    print(f"events: {ev_path.name} · {len(graded)} at grade {a.min_grade} "
          f"or better", file=sys.stderr)

    rows, errors = [], 0
    for ev in graded:
        terms = anchors_of(ev)
        first = parse_ts(ev.get("first_seen")) or datetime.now(timezone.utc)
        start = first - timedelta(hours=2)
        end = first + timedelta(hours=a.hours)
        hits, err, per_term = [], None, {}
        if a.dry_run:
            print(f"  would query {terms} "
                  f"{start:%Y-%m-%d %H:%M}Z → {end:%Y-%m-%d %H:%M}Z")
            continue
        n_ok = n_failed = 0
        for t in terms[:3]:
            arts, e = gdelt_cached(t, start, end, min_gap=a.min_gap)
            if e or arts is None:
                err = e or "no result"
                n_failed += 1
                continue
            n_ok += 1
            per_term[t] = len(arts)
            hits.extend(arts)
        # dedupe by url
        seen, uniq = set(), []
        for h in hits:
            if h["url"] and h["url"] not in seen:
                seen.add(h["url"])
                uniq.append(h)
        state = classify(len(uniq), n_ok, n_failed)
        if state == "NOT-MEASURED":
            errors += 1
        rows.append({
            "anchor": terms,
            "zone": ev.get("zone"),
            "grade": ev.get("grade"),
            "sides": ev.get("sides"),
            "first_seen": ev.get("first_seen"),
            "wire_window_hours": a.hours,
            "wire_state": state,
            "wire_articles": len(uniq),
            "per_term_counts": per_term,
            "terms_answered": n_ok,
            "terms_failed": n_failed,
            "error": err,
            "domains": sorted({h["domain"] for h in uniq if h["domain"]})[:12],
            "sample": uniq[:4],
        })
        print(f"  {state:12} {','.join(terms)[:28]:28} "
              f"{len(uniq):3} article(s)"
              + (f"  [{err}]" if err else ""), file=sys.stderr)

    if a.dry_run:
        return 0

    conf = sum(1 for r in rows if r["wire_state"] == "CONFIRMED")
    silent = sum(1 for r in rows if r["wire_state"] == "WIRE-SILENT")
    partial = sum(1 for r in rows if r["wire_state"].startswith("PARTIAL"))
    payload = {
        "schema": "wire_baseline/v1",
        "generated": datetime.now(timezone.utc).isoformat(),
        "events_source": ev_path.name,
        "wire_index": "GDELT DOC 2.0, sourcelang:english",
        "window_hours": a.hours,
        "summary": {"events": len(rows), "confirmed": conf,
                    "wire_silent": silent, "partial": partial,
                    "not_measured": errors,
                    "unique_queries": len(_CACHE),
                    "wire_silent_share": round(silent / len(rows), 4)
                    if rows else None},
        "limits": ("GDELT indexes COVERAGE, not facts. Absence of coverage is "
                   "absence of coverage: a very recent event legitimately reads "
                   "wire-silent, coverage skews Anglophone and online-indexed, "
                   "and an unreachable index reads NOT-MEASURED rather than "
                   "silent. WIRE-SILENT means uncorroborated outside the "
                   "belligerent set — never false."),
        "events": rows,
    }
    (DOCS / "wire_baseline.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nWIRE BASELINE · {conf} confirmed · {silent} wire-silent · "
          f"{partial} partial · {errors} not measured · "
          f"{len(_CACHE)} unique queries", file=sys.stderr)
    print(f"  → {DOCS / 'wire_baseline.json'}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
