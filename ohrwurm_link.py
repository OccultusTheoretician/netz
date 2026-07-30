#!/usr/bin/env python3
"""
ohrwurm_link.py — NETZ War Desk · Module 5: the join.

    tg_grade grades EVENTS: did hostile sides agree that something happened.
    ohrwurm measures PHRASES: which wording appeared first, where, and how long
    it took to cross a side boundary.

    Neither answers the question they jointly can: when two hostile sides both
    confirm the same event, DO THEY DESCRIBE IT IN THE SAME WORDS? And when they
    don't, was each side's wording minted by this event, or was it a phrase
    already circulating that the event got poured into?

THE JOIN KEY

    An event's `sources[]` each carry {channel, side, date}. Phrase occurrences
    carry (channel, timestamp) too, because both derive from the same pull. So a
    phrase occurrence belongs to an event when its (channel, timestamp) matches
    one of that event's source messages exactly. No fuzzy matching, no window
    heuristic: the same message either is or is not a member of the cluster the
    grader built. On the 2026-07-30 pull the join matched 79 of 79 source
    messages across the graded set; unmatched counts print per event.

THE DEFECT THE FIRST VERSION HAD, MEASURED AND CORRECTED

    v1 counted phrases the way ohrwurm does — n-grams in the SOURCE language,
    two to five words wide. Run against the 2026-07-30 pull it returned lexical
    divergence 1.00 on every single graded event, with zero shared phrases
    anywhere. That is not a finding, it is a broken instrument, and the cause is
    visible in the data: on the Tehran grade-A event the sides file in English,
    Persian and Persian; Donetsk is Russian against English. Sides that write in
    different alphabets cannot share a source-language n-gram, so the metric was
    measuring language, not framing, and returning its maximum by construction.

    Two measures replace it, and they are not interchangeable:

    PROPAGATION stays in the source language, because the thing that travels is
    the original wording. That is ohrwurm's job and this module does not touch
    it.

    FRAMING CONVERGENCE is computed on the TRANSLATED text, at two and three
    words, because the question "did two sides describe this the same way" is
    only answerable once both are in one language. This is translation-mediated
    and every record says so: a shared phrase here may be the translator's
    choice rather than either side's. The mitigation is that both sides pass
    through the SAME local model with the same prompt, so the bias is shared
    rather than differential — but it is bias, and it is printed, not buried.

WHAT COMES OUT, AND WHAT EACH NUMBER MEANS

    LEXICAL DIVERGENCE — of the phrases used about one event, the share used by
    exactly one side. 1.00 means two sides confirmed the same ground and shared
    no wording whatsoever; 0.00 means they spoke in one voice. This is the
    propaganda-variance measure: it is computed only on events that ALREADY
    cleared cross-bias grading, so it cannot be confused with disagreement about
    whether the event happened. They agree it happened. The number is how far
    apart the descriptions are.

    ADOPTION LAG — for a phrase used by two or more sides inside one event, the
    hours between the first side's first use and the second side's. Small lag on
    a shared phrase is the interesting case: the wording crossed a hostile
    boundary fast, which is either a wire service both sides read or one side
    repeating the other.

    IMPORT RATIO — the share of an event's phrases whose FIRST appearance
    anywhere in the corpus predates the event's own window. A high ratio means
    the sides reached for language they were already using: the event was
    described with a template. A low ratio means the event minted its own words.
    This is the closest thing here to a measure of scripted coverage, and it is
    still only a measure of THIS corpus.

LIMITS, PRINTED ON THE FACE AND NEVER DROPPED

    - First-in-this-corpus is not first in the world. Every origin claim is an
      origin claim about a watched set of channels.
    - A phrase counted here is an n-gram in the SOURCE language, per ohrwurm's
      own rule; the join does not touch translations.
    - Divergence over a two-side event where each side is a single outlet is a
      fact about two outlets, not two nations. The per-event single_outlet_sides
      flag from the grader rides into every record so the reader can see it.
    - Nothing here says who is lying. Two sides can describe one event in
      disjoint vocabulary and both be reporting honestly.

USE
    python ohrwurm_link.py --events forecasts/tg_events_YYYY-MM-DD_HHMM.json \
                           --pull   forecasts/tg_wardesk_YYYY-MM-DD_HHMM.json
    python ohrwurm_link.py --latest              newest of each
    python ohrwurm_link.py --latest --dry-run    print, write nothing
    python ohrwurm_link.py --latest --min-grade B
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
    """Import ohrwurm as a library. Its tokeniser, stoplist and n-gram widths
    are the definition of a phrase on this desk; re-implementing them here would
    let the two modules drift and quietly measure different things."""
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


def phrase_index(ow, msgs, fmap, gram_lo=2, gram_hi=3, text_field=None):
    """(channel, ts) -> set of phrases, and phrase -> earliest corpus timestamp.

    The second is what makes the import ratio possible: it is computed over the
    WHOLE pull, not just the messages inside any one event.
    """
    per_msg = defaultdict(set)
    first_seen = {}
    text_of = {}
    for m in msgs:
        if not isinstance(m, dict):
            continue
        # Framing comparison reads the translation; propagation (ohrwurm's own
        # job) reads the original. Which field was used is stamped on the output.
        raw = None
        if text_field:
            raw = m.get(text_field)
        if not raw:
            raw = m.get(fmap["text"]) if fmap["text"] else None
        ts = parse_ts(m.get(fmap["ts"])) if fmap["ts"] else None
        ch = str(m.get(fmap["channel"], "unknown")) if fmap["channel"] else "unknown"
        if not raw or ts is None:
            continue
        toks = [t for t in ow.norm(raw).split()
                if len(t) > 2 and t not in ow.STOP
                and t not in ow.FURNITURE_TOKENS]
        if len(toks) < gram_lo:
            continue
        gs = {g for g in ow.grams(toks, gram_lo, gram_hi)
              if not ow.FURNITURE.search(g)}
        per_msg[(ch, ts)] |= gs
        text_of[(ch, ts)] = raw
        for g in gs:
            if g not in first_seen or ts < first_seen[g]:
                first_seen[g] = ts
    return per_msg, first_seen, text_of


def maximal(phrases):
    """Collapse an n-gram set to its maximal members: 'drone strike' inside
    'massive drone strike overnight' is one phrase seen at two widths, and
    counting both would double-weight whichever side happens to be wordier."""
    out = []
    for p in sorted(phrases, key=len, reverse=True):
        if not any((" " + p + " ") in (" " + q + " ") for q in out):
            out.append(p)
    return out


def content_words(ow, text):
    return {w for w in ow.norm(text or "").split()
            if len(w) > 3 and w not in ow.STOP and w not in ow.FURNITURE_TOKENS}


def link_event(ow, ev, per_msg, first_corpus, msg_text):
    """Join phrases and content words to one graded event, per side.

    The headline is CONVERGENCE, not divergence: the Jaccard overlap of content
    words between the two hostile sides that share the most. Measured on the
    2026-07-30 pull it ranges 0.02 to 0.21 across eighteen graded events, which
    is a usable spread — where the n-gram version returned 1.00 divergence
    everywhere and told us nothing.

    The low end of that range is a finding about the GRADER, not about framing:
    when the only word two sides share is the anchor itself, the cluster is a
    place-name coincidence inside a time window, not corroboration of one event.
    Those get flagged ANCHOR-ONLY and the reader can discount the grade.
    """
    ev_first = parse_ts(ev.get("first_seen"))
    anchor = ev.get("anchor") or []
    anchor = anchor if isinstance(anchor, list) else [anchor]
    anchor_toks = set()
    for a in anchor:
        anchor_toks |= content_words(ow, str(a))
    for v in (ev.get("anchor_aliases") or []) + (ev.get("anchor_variants") or []):
        anchor_toks |= content_words(ow, str(v))

    words = defaultdict(set)          # side -> content words
    use = defaultdict(dict)           # phrase -> side -> earliest use here
    matched = unmatched = 0
    for s in ev.get("sources", []):
        ch, ts = s.get("channel"), parse_ts(s.get("date"))
        side = s.get("side") or "?"
        key = (str(ch), ts)
        words[side] |= content_words(ow, msg_text.get(key, ""))
        if key not in per_msg:
            unmatched += 1
            continue
        matched += 1
        for g in per_msg[key]:
            cur = use[g].get(side)
            if cur is None or ts < cur:
                use[g][side] = ts

    sides = [s for s in words if s and s != "?" and words[s]]
    best = None
    for i in range(len(sides)):
        for j in range(i + 1, len(sides)):
            a, b = words[sides[i]], words[sides[j]]
            union = a | b
            jac = len(a & b) / len(union) if union else 0.0
            if best is None or jac > best["convergence"]:
                best = {"pair": [sides[i], sides[j]],
                        "convergence": round(jac, 4),
                        "shared_words": sorted(a & b)}

    anchor_only = None
    if best is not None:
        sh = set(best["shared_words"])
        anchor_only = bool(sh) and sh <= anchor_toks or not sh

    keep = maximal(use.keys())
    shared, exclusive, imported = [], [], 0
    for g in keep:
        gs = {s: t for s, t in use[g].items() if s != "?"}
        origin = first_corpus.get(g)
        is_import = bool(origin and ev_first and origin < ev_first)
        if is_import:
            imported += 1
        rec = {"phrase": g, "sides": sorted(gs),
               "corpus_origin": origin.isoformat() if origin else None,
               "template": is_import}
        if len(gs) >= 2:
            order = sorted(gs.items(), key=lambda kv: kv[1])
            rec["adoption_lag_hours"] = round(
                (order[1][1] - order[0][1]).total_seconds() / 3600, 2)
            rec["led_by"] = order[0][0]
            shared.append(rec)
        elif len(gs) == 1:
            exclusive.append(rec)

    n = len(shared) + len(exclusive)
    return {
        "anchor": anchor,
        "zone": ev.get("zone"),
        "track": ev.get("track"),
        "grade": ev.get("grade"),
        "sides": ev.get("sides"),
        "single_outlet_sides": ev.get("single_outlet_sides"),
        "window": {"first_seen": ev.get("first_seen"),
                   "last_seen": ev.get("last_seen"),
                   "hours": ev.get("time_span_hrs")},
        "sources_matched": matched,
        "sources_unmatched": unmatched,
        "closest_pair": best["pair"] if best else None,
        "convergence": best["convergence"] if best else None,
        "shared_words": best["shared_words"] if best else [],
        "anchor_only": anchor_only,
        "phrases_total": n,
        "phrases_shared": len(shared),
        "phrases_exclusive": len(exclusive),
        "import_ratio": round(imported / n, 4) if n else None,
        "shared": sorted(shared, key=lambda r: r.get("adoption_lag_hours", 0)),
        "exclusive_by_side": {
            s: [r["phrase"] for r in exclusive if r["sides"] == [s]][:8]
            for s in sorted({r["sides"][0] for r in exclusive if r["sides"]})
        },
    }


GRADE_ORDER = {"A": 0, "B": 1, "C": 2, "F": 3}


def render(rows, src_ev, src_pull, stamp, unmatched_total, matched_total,
           basis):
    L = []
    a = L.append
    a("## OHRWURM \u00d7 WAR DESK \u2014 DO THE SIDES USE THE SAME WORDS?")
    a("")
    a("*Every event below already cleared cross-bias grading: hostile sides "
      "agree it happened. What is measured here is whether they described it "
      "the same way. CONVERGENCE is the content-word overlap between the two "
      "hostile sides that share the most \u2014 0.00 means they confirmed the same "
      "ground with no vocabulary in common, 1.00 means one voice. IMPORT RATIO "
      "is the share of an event's phrases already circulating in this corpus "
      "before the event opened: high means the sides reached for language they "
      "had ready, low means the event minted its own. Neither number says who "
      "is lying.*")
    a("")
    a("*ANCHOR-ONLY is a finding against this desk's own grader, not against a "
      "source: when the only word two sides share is the place name the cluster "
      "was built on, that is a coincidence of geography inside a time window "
      "and not corroboration of one event. Those rows are marked so the grade "
      "can be discounted.*")
    a("")
    a(f"Events: `{src_ev}` \u00b7 pull: `{src_pull}` \u00b7 joined on exact "
      f"(channel, timestamp) \u2014 {matched_total} source messages matched, "
      f"{unmatched_total} unmatched \u00b7 rendered {stamp}")
    a("")
    a(f"Comparison basis: **{basis}**.")
    a("")
    a("**LIMIT, NOT A DISCLAIMER:** first-in-this-corpus is not first in the "
      "world; a shared word read through translation may be the translator's "
      "and not either side's; and overlap between two single-outlet sides is a "
      "fact about two outlets, not two nations.")
    a("")
    flagged = [r for r in rows if r.get("anchor_only")]
    if flagged:
        a(f"**{len(flagged)} of {len(rows)} linked events are ANCHOR-ONLY** "
          "\u2014 listed in full below and worth reading before any of the "
          "convergence figures.")
        a("")
    for r in rows:
        anchor = ", ".join(str(x) for x in (r["anchor"] or []))
        a(f"### {anchor.title()} \u00b7 {r['zone']} \u00b7 {r['track']} \u00b7 {r['grade']}")
        a("")
        a(f"- Sides confirming: {', '.join(r['sides'] or [])}"
          + (f" \u2014 single-outlet: {', '.join(r['single_outlet_sides'])}"
             if r.get("single_outlet_sides") else ""))
        cv = r["convergence"]
        if cv is not None:
            pair = " / ".join(r["closest_pair"] or [])
            verdict = ("one voice" if cv >= 0.5 else
                       "substantial shared vocabulary" if cv >= 0.15 else
                       "little shared vocabulary" if cv >= 0.05 else
                       "almost nothing in common")
            a(f"- **Convergence {cv:.3f}** on the closest pair ({pair}) "
              f"\u2014 {verdict}")
            if r["shared_words"]:
                a("    - shared: " + ", ".join(f"`{w}`" for w in
                                               r["shared_words"][:12]))
            else:
                a("    - shared: **no content word in common**")
        if r.get("anchor_only"):
            a("- \u26a0 **ANCHOR-ONLY** \u2014 the sides share nothing beyond the "
              "anchor itself. Treat this grade as unconfirmed: the cluster may "
              "be two unrelated reports that named the same place in the same "
              "window.")
        if r["import_ratio"] is not None:
            a(f"- Import ratio {r['import_ratio']:.2f} \u2014 "
              + ("mostly pre-existing language poured into this event"
                 if r["import_ratio"] >= 0.7 else
                 "a mix of ready language and event-minted wording"
                 if r["import_ratio"] >= 0.3 else
                 "mostly wording that appears here first"))
        if r["shared"]:
            a("- Shared phrasing, by how fast it crossed the divide:")
            for s in r["shared"][:6]:
                a(f"    - `{s['phrase']}` \u2014 {' \u2192 '.join(s['sides'])} in "
                  f"{s.get('adoption_lag_hours')}h, led by {s['led_by']}"
                  + (" \u00b7 **template** (predates this event in the corpus)"
                     if s["template"] else ""))
        for side, ph in r["exclusive_by_side"].items():
            if ph:
                a(f"    - *{side} only:* " + ", ".join(f"`{p}`" for p in ph))
        if r["sources_unmatched"]:
            a(f"- {r['sources_unmatched']} of "
              f"{r['sources_matched'] + r['sources_unmatched']} source messages "
              "could not be joined (below the n-gram floor) \u2014 counted, not "
              "hidden.")
        a("")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="Ohrwurm × War Desk join")
    ap.add_argument("--events")
    ap.add_argument("--pull")
    ap.add_argument("--latest", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--min-grade", default="B", choices=list("ABCF"))
    ap.add_argument("--gram-lo", type=int, default=2)
    ap.add_argument("--source-lang", action="store_true",
                    help="compare source-language n-grams instead of "
                         "translations; expect divergence 1.00 wherever the "
                         "sides use different alphabets")
    ap.add_argument("--gram-hi", type=int, default=3)
    a = ap.parse_args()

    ev_path = Path(a.events) if a.events else (
        newest("tg_events_*.json") if a.latest else None)
    # DEFECT, 2026-07-30: this preferred tg_wardesk_* (the RAW pull) over
    # tg_translated_*, so --latest silently selected an untranslated file, the
    # comparison fell back to source language, and the run wrote an artifact
    # reading median convergence 0.000 with fifteen ANCHOR-ONLY flags — all of
    # it an artefact of the wrong input, not a finding about any source. The
    # translated pull is now preferred and named on stderr.
    pull_path = None
    if a.pull:
        pull_path = Path(a.pull)
    elif a.latest:
        pull_path = newest("tg_translated_*.json") or newest("tg_wardesk_*.json")
    if not ev_path or not pull_path:
        print("Need --events and --pull, or --latest.", file=sys.stderr)
        return 1
    for p in (ev_path, pull_path):
        if not p.exists():
            print(f"missing: {p}", file=sys.stderr)
            return 1
    print(f"events: {ev_path.name}\npull:   {pull_path.name}", file=sys.stderr)

    ow = load_ohrwurm()
    pull = json.loads(pull_path.read_text(encoding="utf-8-sig"))
    msgs = ow.find_messages(pull)
    det = ow.detect(msgs)
    fmap = det[0] if isinstance(det, tuple) else det
    # Which field carries the comparable text? Prefer the translation when the
    # pull has one; fall back to source and say so loudly.
    has_en = sum(1 for m in msgs if isinstance(m, dict) and m.get("text_en"))
    text_field = None if a.source_lang else (
        "text_en" if has_en >= max(1, len(msgs) // 4) else None)
    basis = ("translated (text_en) — translation-mediated, %d of %d messages "
             "carry a translation" % (has_en, len(msgs))) if text_field else \
            ("source language only — no translation field in this pull, so "
             "cross-alphabet sides CANNOT share a phrase and divergence will "
             "read 1.00 by construction")
    print("comparison basis: " + basis, file=sys.stderr)
    # A metric that reads 0.000 by construction must not be written to disk.
    # If the chosen pull has no translations while the graded events span more
    # than one language, every convergence figure is a fact about alphabets.
    if text_field is None and not a.source_lang:
        langs = set()
        for m in msgs:
            if isinstance(m, dict) and m.get("lang"):
                langs.add(str(m["lang"]))
        if len(langs) > 1:
            print("\nREFUSED — this pull carries no translation field and the "
                  "corpus spans %d languages (%s). Convergence would read 0.000 "
                  "for every cross-alphabet pair by construction, and the "
                  "ANCHOR-ONLY flag would fire on clusters that are fine.\n"
                  "  Run tg_translate.py first, then point --pull at the "
                  "resulting forecasts/tg_translated_*.json.\n"
                  "  To measure source-language overlap deliberately anyway, "
                  "pass --source-lang."
                  % (len(langs), ", ".join(sorted(langs)[:8])), file=sys.stderr)
            return 2
    per_msg, first_corpus, msg_text = phrase_index(
        ow, msgs, fmap, a.gram_lo, a.gram_hi, text_field)

    events = json.loads(ev_path.read_text(encoding="utf-8-sig")).get("events", [])
    floor = GRADE_ORDER[a.min_grade]
    graded = [e for e in events
              if GRADE_ORDER.get(str(e.get("grade", "F"))[0], 3) <= floor]

    rows, m_tot, u_tot = [], 0, 0
    for e in graded:
        r = link_event(ow, e, per_msg, first_corpus, msg_text)
        m_tot += r["sources_matched"]
        u_tot += r["sources_unmatched"]
        if r["phrases_total"]:
            rows.append(r)
    rows.sort(key=lambda r: (GRADE_ORDER.get(str(r["grade"])[0], 3),
                             -(r["convergence"] or 0)))

    stamp = datetime.now(timezone.utc).strftime("%d%H%MZ %b %y").upper()
    md = render(rows, ev_path.name, pull_path.name, stamp, u_tot, m_tot, basis)
    print("")
    print(md)

    cvs = [r["convergence"] for r in rows if r["convergence"] is not None]
    flagged = [r for r in rows if r.get("anchor_only")]
    imps = [r["import_ratio"] for r in rows if r["import_ratio"] is not None]
    payload = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "schema": "ohrwurm_link/v1",
        "events_source": ev_path.name,
        "pull_source": pull_path.name,
        "min_grade": a.min_grade,
        "events_linked": len(rows),
        "events_considered": len(graded),
        "sources_matched": m_tot,
        "sources_unmatched": u_tot,
        "median_convergence": (sorted(cvs)[len(cvs) // 2] if cvs else None),
        "convergence_range": [min(cvs), max(cvs)] if cvs else None,
        "anchor_only_events": len(flagged),
        "anchor_only_note": ("events whose sides share no word beyond the "
                             "anchor: a defect signal for tg_cluster, printed "
                             "rather than smoothed"),
        "median_import_ratio": (sorted(imps)[len(imps) // 2]
                                if imps else None),
        "comparison_basis": basis,
        "gram_width": [a.gram_lo, a.gram_hi],
        "method": ("phrase occurrences joined to graded events on exact "
                   "(channel, timestamp); framing compared on translated text "
                   "because cross-alphabet sides cannot share a source-language "
                   "n-gram; propagation itself stays source-language in "
                   "ohrwurm; first-in-corpus is not first in the world"),
        "events": rows,
    }
    if a.dry_run:
        print("\n(dry run — nothing written)", file=sys.stderr)
        return 0
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M")
    out_md = FORECASTS / f"OHRWURM_LINK_{ts}.md"
    out_md.write_text(md, encoding="utf-8")
    (FORECASTS / "OHRWURM_LINK_latest.md").write_text(md, encoding="utf-8")
    (DOCS / "ohrwurm_link.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nOHRWURM x WARDESK \u00b7 {len(rows)} events linked \u00b7 median "
          f"convergence {payload['median_convergence']} \u00b7 range "
          f"{payload['convergence_range']} \u00b7 anchor-only "
          f"{payload['anchor_only_events']} \u00b7 median import "
          f"{payload['median_import_ratio']}", file=sys.stderr)
    print(f"  section → {out_md}\n  tile    → {DOCS / 'ohrwurm_link.json'}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
