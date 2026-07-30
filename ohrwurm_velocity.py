#!/usr/bin/env python3
"""
ohrwurm_velocity.py — NETZ War Desk · Module 4b: the propagation timeline.

    ohrwurm.py prints, for each phrase, a handful of scalars: when it first
    appeared, how many hours to the second channel, how many to cross a side.
    Those are the endpoints of a curve it never draws. A phrase that reached
    six channels across two sides in ninety minutes and one that limped to two
    channels over nine hours both reduce to "crossed" — and the difference
    between them is the entire signal.

    This module reconstructs the curve. For every phrase above the floor it
    emits the ORDERED sequence of first-uses — each (hours-since-origin,
    channel, side) — so the adoption can be plotted, and from that sequence it
    computes a spread VELOCITY: channels per hour over the active window, and
    the side-crossing latency as a fraction of the whole span. Fast cross-side
    adoption is the case worth watching: a framing that jumped the hostile
    boundary in under an hour is either an event both sides genuinely saw at
    once, or one side's line that the other picked up nearly instantly. The
    instrument dates it and rates its speed; it does not claim which.

WHY THIS IS NOT A TREND YET

    Velocity here is measured WITHIN a single pull. "Acceleration" — whether
    cross-side adoption is getting faster week over week — needs two dated pulls
    whose windows do not overlap, and the two pulls on hand (07-28 and 07-30)
    both cover the same 24h of 07-27 reporting, so a real trend cannot be
    computed and this module does not fake one. The comparison slot is built and
    dormant: point --prior at an earlier ohrwurm_velocity tile from a
    non-overlapping window and the delta fires. Until then, every figure is a
    snapshot, and the face says so.

    It reuses ohrwurm's own tokeniser, stoplist and n-gram widths by importing
    it — re-implementing them here would let the page and the module measure
    two different things.

USE
    python ohrwurm_velocity.py --latest
    python ohrwurm_velocity.py --file forecasts/tg_translated_2026-07-30_0512.json
    python ohrwurm_velocity.py --latest --prior forecasts/ohrwurm_velocity_PRIOR.json
    python ohrwurm_velocity.py --latest --dry-run
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
FORECASTS = HERE / "forecasts"
DOCS = HERE / "docs"


def load_ohrwurm():
    spec = importlib.util.spec_from_file_location("ow", HERE / "ohrwurm.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def parse_ts(v):
    if not v:
        return None
    s = str(v).replace("Z", "+00:00")
    try:
        d = datetime.fromisoformat(s)
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


def newest(pattern):
    hits = sorted(FORECASTS.glob(pattern))
    return hits[-1] if hits else None


def maximal(rows):
    """One phrase seen at two n-gram widths is one phrase. Keep the widest of
    any pair where the shorter is a substring and the timelines match."""
    rows = sorted(rows, key=lambda r: len(r["phrase"]), reverse=True)
    kept = []
    for r in rows:
        p = " " + r["phrase"] + " "
        if not any(p in (" " + k["phrase"] + " ")
                   and k["reports"] == r["reports"] for k in kept):
            kept.append(r)
    return kept


def build(ow, msgs, fmap, min_reports, min_channels, gram_lo, gram_hi):
    # phrase -> [(ts, channel, side, zone)]
    seen = defaultdict(list)
    for m in msgs:
        if not isinstance(m, dict):
            continue
        raw = m.get(fmap["text"]) if fmap["text"] else None
        ts = parse_ts(m.get(fmap["ts"])) if fmap["ts"] else None
        ch = str(m.get(fmap["channel"], "unknown")) if fmap["channel"] else "unknown"
        raw_side = m.get(fmap["side"]) if fmap["side"] else None
        sd = ow.side_of(raw_side) if raw_side else "?"
        zn = str(m.get(fmap["zone"], "?")) if fmap["zone"] else "?"
        if not raw or ts is None:
            continue
        toks = [t for t in ow.norm(raw).split()
                if len(t) > 2 and t not in ow.STOP
                and t not in ow.FURNITURE_TOKENS]
        if len(toks) < gram_lo:
            continue
        for g in set(ow.grams(toks, gram_lo, gram_hi)):
            if not ow.FURNITURE.search(g):
                seen[g].append((ts, ch, sd, zn))

    rows = []
    for phrase, hits in seen.items():
        chans = {h[1] for h in hits}
        if len(hits) < min_reports or len(chans) < min_channels:
            continue
        hits.sort(key=lambda h: h[0])
        t0 = hits[0][0]

        # first-use per channel, in order — this is the adoption curve
        first_by_chan = {}
        for ts, ch, sd, zn in hits:
            if ch not in first_by_chan:
                first_by_chan[ch] = (ts, sd)
        timeline = sorted(
            ({"h": round((ts - t0).total_seconds() / 3600, 2),
              "channel": ch, "side": sd}
             for ch, (ts, sd) in first_by_chan.items()),
            key=lambda x: x["h"])

        span = timeline[-1]["h"] or 0.0
        n_chan = len(timeline)
        # channels adopted per active hour; a burst reads high, a slow drip low
        velocity = round(n_chan / span, 2) if span > 0 else None

        s0 = timeline[0]["side"]
        cross = next((e for e in timeline
                      if e["side"] != s0 and e["side"] != "?"), None)
        cross_h = cross["h"] if cross else None
        # how early in the phrase's life did it jump the divide? 0.0 = at once
        cross_frac = (round(cross_h / span, 3)
                      if cross_h is not None and span > 0 else None)

        sides = defaultdict(int)
        for _, _, s, _ in hits:
            sides[s] += 1

        rows.append({
            "phrase": phrase,
            "reports": len(hits),
            "channels": n_chan,
            "sides": len([s for s in sides if s != "?"]),
            "side_balance": dict(sorted(sides.items(), key=lambda x: -x[1])),
            "zone": hits[0][3],
            "origin": {"at": t0.isoformat(), "channel": timeline[0]["channel"],
                       "side": s0},
            "span_hours": span,
            "velocity_chan_per_hr": velocity,
            "hours_to_cross_side": cross_h,
            "cross_fraction": cross_frac,
            "crossed_to": {"side": cross["side"], "channel": cross["channel"]}
                          if cross else None,
            "confined": cross is None,
            "timeline": timeline,
        })

    rows = maximal(rows)
    rows.sort(key=lambda r: (r["confined"],
                             r["cross_fraction"] if r["cross_fraction"]
                             is not None else 9,
                             -(r["velocity_chan_per_hr"] or 0)))
    return rows


def summarise(rows):
    crossed = [r for r in rows if not r["confined"]]
    vels = [r["velocity_chan_per_hr"] for r in crossed
            if r["velocity_chan_per_hr"] is not None]
    lats = [r["hours_to_cross_side"] for r in crossed
            if r["hours_to_cross_side"] is not None]
    fast = [r for r in crossed
            if r["hours_to_cross_side"] is not None
            and r["hours_to_cross_side"] < 1.0]
    return {
        "phrases_total": len(rows),
        "crossed_side": len(crossed),
        "confined": len(rows) - len(crossed),
        "median_velocity": sorted(vels)[len(vels) // 2] if vels else None,
        "median_cross_latency_hrs": sorted(lats)[len(lats) // 2]
                                    if lats else None,
        "crossed_under_1hr": len(fast),
        "fastest": ({"phrase": crossed[0]["phrase"],
                     "cross_latency_hrs": crossed[0]["hours_to_cross_side"],
                     "velocity": crossed[0]["velocity_chan_per_hr"]}
                    if crossed else None),
    }


def main():
    ap = argparse.ArgumentParser(description="Ohrwurm propagation velocity")
    ap.add_argument("--file")
    ap.add_argument("--latest", action="store_true")
    ap.add_argument("--prior", help="an earlier velocity tile from a "
                    "NON-overlapping window, to compute acceleration")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--min-reports", type=int, default=3)
    ap.add_argument("--min-channels", type=int, default=2)
    ap.add_argument("--gram-lo", type=int, default=2)
    ap.add_argument("--gram-hi", type=int, default=5)
    a = ap.parse_args()

    path = Path(a.file) if a.file else (
        newest("tg_translated_*.json") or newest("tg_wardesk_*.json")
        if a.latest else None)
    if not path:
        print("Need --file or --latest.", file=sys.stderr)
        return 1
    if not path.exists():
        print(f"missing: {path}", file=sys.stderr)
        return 1
    print(f"pull: {path.name}", file=sys.stderr)

    ow = load_ohrwurm()
    doc = json.loads(path.read_text(encoding="utf-8"))
    msgs = ow.find_messages(doc)
    det = ow.detect(msgs)
    fmap = det[0] if isinstance(det, tuple) else det
    rows = build(ow, msgs, fmap, a.min_reports, a.min_channels,
                 a.gram_lo, a.gram_hi)
    summ = summarise(rows)

    accel = None
    if a.prior:
        pr = Path(a.prior)
        if pr.exists():
            prior = json.loads(pr.read_text(encoding="utf-8"))
            pw = prior.get("window") or {}
            here_lo = min((e["h"] for r in rows for e in r["timeline"]),
                          default=None)
            # windows overlap check is the operator's — we only refuse the
            # obviously-degenerate case of the same source file
            if prior.get("source_pull") == path.name:
                accel = {"status": "refused",
                         "why": "prior tile is the same pull — no delta"}
            else:
                pm = prior.get("summary", {}).get("median_cross_latency_hrs")
                cm = summ["median_cross_latency_hrs"]
                if pm and cm:
                    accel = {
                        "status": "measured",
                        "prior_pull": prior.get("source_pull"),
                        "prior_median_cross_latency_hrs": pm,
                        "current_median_cross_latency_hrs": cm,
                        "delta_hrs": round(cm - pm, 2),
                        "reading": ("cross-side adoption is FASTER than the "
                                    "prior window" if cm < pm else
                                    "cross-side adoption is SLOWER than the "
                                    "prior window" if cm > pm else
                                    "unchanged"),
                        "caveat": ("valid only if the two windows do not "
                                   "overlap — the operator confirms that, this "
                                   "tool does not"),
                    }
        else:
            print(f"  prior tile not found: {pr}", file=sys.stderr)

    payload = {
        "schema": "ohrwurm_velocity/v1",
        "generated": datetime.now(timezone.utc).isoformat(),
        "source_pull": path.name,
        "floors": {"min_reports": a.min_reports,
                   "min_channels": a.min_channels,
                   "gram_widths": [a.gram_lo, a.gram_hi]},
        "caveat": ("velocity is measured WITHIN this pull; acceleration needs "
                   "two dated pulls with non-overlapping windows and is not "
                   "computed unless --prior supplies one. First-in-this-corpus "
                   "is not first in the world."),
        "summary": summ,
        "acceleration": accel,
        "phrases": rows,
    }

    print(f"\nphrases {summ['phrases_total']} · crossed side "
          f"{summ['crossed_side']} · median cross latency "
          f"{summ['median_cross_latency_hrs']}h · crossed under 1h "
          f"{summ['crossed_under_1hr']}", file=sys.stderr)
    if summ["fastest"]:
        f = summ["fastest"]
        print(f"fastest crossing: '{f['phrase']}' in "
              f"{f['cross_latency_hrs']}h", file=sys.stderr)
    if accel:
        print(f"acceleration: {accel.get('reading', accel.get('why'))}",
              file=sys.stderr)

    if a.dry_run:
        print(json.dumps(payload, ensure_ascii=False, indent=2)[:1500])
        print("\n(dry run — nothing written)", file=sys.stderr)
        return 0

    blob = json.dumps(payload, ensure_ascii=False, indent=2)
    (FORECASTS / "ohrwurm_velocity_latest.json").write_text(blob, encoding="utf-8")
    if DOCS.exists():
        (DOCS / "ohrwurm_velocity.json").write_text(blob, encoding="utf-8")
        print(f"  → {DOCS / 'ohrwurm_velocity.json'}  (served copy)",
              file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
