#!/usr/bin/env python3
"""
ohrwurm.py — NETZ War Desk · Module 4: propagation and variance.

    Kaos Kontrol function. An Ohrwurm is a phrase that lodges and repeats —
    what this measures is which ones lodged, in whose ears, and how fast they
    travelled from the side that planted them to the side that did not.

WHAT THIS MEASURES, AND WHY IT IS NOT THE WAR DESK

    tg_grade grades EVENTS. A claim confirms when hostile sides agree, and
    repetition inside one side is rejected as echo — Grade C, printed so the
    reader can see what the method threw away.

    That discarded echo is this instrument's entire signal.

    Ohrwurm does not ask whether something happened. It asks how the WORDING
    moved: which phrasing appeared first, where, on which side of the divide,
    how long before a second channel carried it, whether it ever crossed a side
    boundary, and which channels that normally speak went quiet.

    Cross-bias grading needs independent outlets and does not improve with
    volume — sides are a fixed taxonomy, so ten thousand channels produce the
    same side count and a much larger echo pile. Propagation is the opposite:
    it needs saturation, because the distribution IS the measurement. One fetch,
    two consumers, and only the graded set needs translation.

THE CLAIM IT PRODUCES, AND ITS LIMIT

    "Phrase P first appears in this corpus at time T, on channel C, side S; it
    reached side S' at T+d." That is falsifiable and dated. The limit is printed
    on every face and must never be dropped: FIRST IN THIS CORPUS IS NOT FIRST
    IN THE WORLD. It is an origin claim about a watched set, not about reality,
    and it is only as strong as the channel list behind it.

    Origin claims emit as seal-ready records — statement plus SHA-256 — so a
    first-appearance call can be committed under KNP before the phrase becomes
    salient. That is the retro-prescient shape applied to language rather than
    to events.

WHY NO MODEL RUNS HERE

    n-grams are counted in the SOURCE language. The propagating unit is the
    original wording, not a translation of it — routing Russian through Qwen and
    counting the English would measure the translator. Deterministic, auditable,
    and it costs nothing per message, which is what makes thousands of channels
    tractable.

USE
    python ohrwurm.py --schema                  detect fields, print, exit
    python ohrwurm.py --latest                  newest tg_wardesk_*.json
    python ohrwurm.py --file forecasts\\tg_wardesk_2026-07-28_0157.json
    python ohrwurm.py --latest --min-reports 3 --dry-run
"""
from __future__ import annotations
import argparse, hashlib, json, re, sys, unicodedata
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent

# The side map is NOT reimplemented here. tg_cluster.SIDES is the registry and
# side_of() is its accessor; two instruments disagreeing about what a side is
# would be worse than the bug this fixes. v1 graded on the raw bias label, so
# rybar (PRO-RUSSIA STATE-ADJACENT) -> boris_rozhin (PRO-RUSSIA) scored as a
# cross-side crossing. Both are RU. That is echo, and grading it as its opposite
# is the exact claim the War Desk exists to refuse.
try:
    sys.path.insert(0, str(HERE))
    from tg_cluster import side_of as _side_of        # noqa: E402
    SIDE_MAP_SOURCE = "tg_cluster.side_of"
except Exception as _e:                                # pragma: no cover
    _side_of = None
    SIDE_MAP_SOURCE = f"UNAVAILABLE ({_e})"


def side_of(bias):
    if _side_of is None:
        return "UNMAPPED:no-side-map"
    return _side_of(bias)
FORECASTS = HERE / "forecasts"
DOCS = HERE / "docs"

# field-name candidates, in priority order. The pull's schema is discovered,
# not assumed — different fetch versions have used different names.
CAND = {
    "text":    ["text", "message", "msg", "body", "content", "raw", "text_orig"],
    "ts":      ["date", "ts", "timestamp", "time", "datetime", "sent_at"],
    "channel": ["channel", "chan", "source", "peer", "username", "from", "outlet"],
    "side":    ["side", "bias", "camp", "alignment", "bloc"],
    "zone":    ["zone", "theatre", "theater", "region", "front"],
}

URL = re.compile(r"https?://\S+|t\.me/\S+|@\w+")
NONWORD = re.compile(r"[^\w\u0400-\u04FF\u0590-\u05FF\u0600-\u06FF\s-]", re.U)
WS = re.compile(r"\s+")

# tokens too common to carry propagation signal, across the pull's main languages
STOP = set("""
the a an and or of in on at to for from with by is are was were be been it its this that
will not over past carried out has have had more than after before during said says say told
according also would could should may might there here them then when what which who whom
new one two three first second last next each any all some most other another such only
report reports reported statement announced according added noted claims claimed
и в на с по за из от до к у не что как для или а но же то это все еще уже был была было
их его ее них там где когда так вот бы ли мы вы они он она оно
של את עם על אל כי לא זה הוא היא הם אנחנו אתם
في من على إلى عن مع هذا هذه ذلك التي الذي قد لا ما هو هي
der die das und in den von zu mit auf ist im für dem nicht ein eine als auch es an
""".split())


# Photo credits, wire furniture and attribution lines. Template suppression
# needs 75% of channels to fire; a credit line carried by two outlets slips
# under that floor and still is not propagation.
FURNITURE = re.compile(
    r"\bgetty images?\b|\breuters\b|\bap photo\b|\bfile photo\b|\bphoto by\b"
    r"|\bscreenshot\b|\bread more\b|\bsubscribe\b|\bvia getty\b|\bimage credit\b"
    r"|\bcourtesy of\b|\brights reserved\b|\bfollow us\b|\bshare this\b"
    r"|\bgetty\b|\bphotograph\b|\bcopyright\b|\bhandout\b|\bstringer\b",
    re.I)


# Credit-line vocabulary never enters an n-gram. Matching furniture on the
# assembled phrase leaves fragments ("images rights") that match nothing; the
# only reliable place to stop it is before grams are built.
FURNITURE_TOKENS = {
    "getty", "images", "image", "photograph", "photo", "reuters", "afp", "epa",
    "copyright", "reserved", "rights", "handout", "stringer", "screenshot",
    "subscribe", "credit", "courtesy", "caption", "pictured", "file",
}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "")
    s = URL.sub(" ", s)
    s = NONWORD.sub(" ", s)
    return WS.sub(" ", s).strip().lower()


def parse_ts(v):
    if v is None:
        return None
    if isinstance(v, (int, float)):
        try:
            return datetime.fromtimestamp(v, tz=timezone.utc)
        except (ValueError, OSError, OverflowError):
            return None
    s = str(v).strip().replace("Z", "+00:00")
    for cut in (s, s[:19]):
        try:
            d = datetime.fromisoformat(cut)
            return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def find_messages(doc):
    """Return the message list wherever the pull happens to keep it."""
    if isinstance(doc, list):
        return doc
    for k in ("messages", "msgs", "items", "records", "posts", "data"):
        v = doc.get(k)
        if isinstance(v, list) and v:
            return v
    # zone-keyed: {"iran": [...], "russia_ukraine": [...]}
    out = []
    for k, v in doc.items():
        if isinstance(v, list) and v and isinstance(v[0], dict):
            for m in v:
                m.setdefault("zone", k)
            out += v
    return out


def detect(msgs):
    keys = set()
    for m in msgs[:400]:
        if isinstance(m, dict):
            keys |= set(m.keys())
    mapping = {}
    for role, cands in CAND.items():
        mapping[role] = next((c for c in cands if c in keys), None)
    return mapping, sorted(keys)


def grams(tokens, lo=2, hi=5):
    n = len(tokens)
    for size in range(lo, hi + 1):
        for i in range(n - size + 1):
            yield " ".join(tokens[i:i + size])


def analyse(msgs, fmap, min_reports, min_channels, gram_lo, gram_hi):
    seen = defaultdict(list)          # phrase -> [(ts, channel, side, zone)]
    chan_zone = defaultdict(set)      # channel -> zones it spoke in
    zone_chans = defaultdict(set)

    for m in msgs:
        if not isinstance(m, dict):
            continue
        raw = m.get(fmap["text"]) if fmap["text"] else None
        ts = parse_ts(m.get(fmap["ts"])) if fmap["ts"] else None
        ch = str(m.get(fmap["channel"], "unknown")) if fmap["channel"] else "unknown"
        raw_side = m.get(fmap["side"]) if fmap["side"] else None
        sd = side_of(raw_side) if raw_side else "?"
        zn = str(m.get(fmap["zone"], "?")) if fmap["zone"] else "?"
        if not raw or ts is None:
            continue
        chan_zone[ch].add(zn)
        zone_chans[zn].add(ch)
        toks = [t for t in norm(raw).split()
                if len(t) > 2 and t not in STOP and t not in FURNITURE_TOKENS]
        if len(toks) < gram_lo:
            continue
        for g in set(grams(toks, gram_lo, gram_hi)):
            seen[g].append((ts, ch, sd, zn))

    rows = []
    for phrase, hits in seen.items():
        if FURNITURE.search(phrase):
            continue
        chans = {h[1] for h in hits}
        if len(hits) < min_reports or len(chans) < min_channels:
            continue
        hits.sort(key=lambda h: h[0])
        t0, c0, s0, z0 = hits[0]

        t_second_chan = next((h[0] for h in hits if h[1] != c0), None)
        t_cross_side = next((h[0] for h in hits if h[2] != s0 and h[2] != "?"), None)
        cross_ch = next((h[1] for h in hits if h[2] != s0 and h[2] != "?"), None)
        cross_sd = next((h[2] for h in hits if h[2] != s0 and h[2] != "?"), None)

        sides = defaultdict(int)
        for _, _, s, _ in hits:
            sides[s] += 1

        span = (hits[-1][0] - t0).total_seconds() / 3600
        rows.append({
            "phrase": phrase,
            "reports": len(hits),
            "channels": len(chans),
            "sides": len([s for s in sides if s != "?"]),
            "side_balance": dict(sorted(sides.items(), key=lambda x: -x[1])),
            "zone": z0,
            "origin": {"at": t0.isoformat(), "channel": c0, "side": s0},
            "hours_to_second_channel": round((t_second_chan - t0).total_seconds() / 3600, 2)
                                        if t_second_chan else None,
            "hours_to_cross_side": round((t_cross_side - t0).total_seconds() / 3600, 2)
                                        if t_cross_side else None,
            "crossed_to": {"side": cross_sd, "channel": cross_ch} if cross_sd else None,
            "confined_to_origin_side": cross_sd is None,
            "span_hours": round(span, 2),
        })

    # --- collapse overlapping n-grams to their maximal form -----------------
    # "drone strike on port" and "massive drone strike on port overnight" with the
    # same report count and the same origin are one phrase seen at two widths.
    # Keep the longest; a shorter gram survives only if it appears somewhere the
    # longer one does not, which means it is genuinely a separate phrase.
    rows.sort(key=lambda r: (-len(r["phrase"]), -r["reports"]))
    # Same first-appearance timestamp, same origin channel, same report count =
    # one underlying message seen through several sliding windows. Keep the
    # longest form; it is the most specific statement of the phrase.
    best = {}
    for r in rows:
        k = (r["origin"]["at"], r["origin"]["channel"], r["reports"])
        cur = best.get(k)
        if cur is None or len(r["phrase"]) > len(cur["phrase"]):
            best[k] = r
    rows = list(best.values())

    # --- template suppression ------------------------------------------------
    # A phrase carried by nearly every channel across nearly every side is not
    # propagating, it is furniture: digest headers, subscribe footers, channel
    # signatures. Flagged rather than deleted, because what counts as furniture
    # is a judgement and the reader should be able to check it.
    all_chans = len({c for cs in zone_chans.values() for c in cs}) or 1
    all_sides = len({s for r in rows for s in r["side_balance"] if s != "?"}) or 1
    for r in rows:
        r["template"] = (r["channels"] >= max(3, round(all_chans * 0.75))
                         and r["sides"] >= max(3, all_sides - 1))

    rows.sort(key=lambda r: (r["template"], -r["reports"], r["origin"]["at"]))
    # SILENCE requires a channel->zone registry. Comparing against every channel
    # in the pull says a Russia-Ukraine channel is "silent on Iran", which is not
    # silence - it is a channel that does not cover Iran. Without war_channels.json
    # this block reports nothing rather than reporting something false.
    registry = HERE / "war_channels.json"
    silence = {}
    if registry.exists():
        try:
            reg = json.loads(registry.read_text(encoding="utf-8"))
            expect = defaultdict(set)
            def walk(node, zone=None):
                if isinstance(node, dict):
                    for k, v in node.items():
                        walk(v, k if isinstance(v, (list, dict)) else zone)
                elif isinstance(node, list) and zone:
                    for it in node:
                        name = it.get("channel") or it.get("name") if isinstance(it, dict) else it
                        if isinstance(name, str):
                            expect[zone].add(name)
            walk(reg)
            for z, spoke in zone_chans.items():
                miss = sorted(expect.get(z, set()) - spoke)
                if miss:
                    silence[z] = miss
            if not expect:
                silence = {"_unavailable": ["war_channels.json parsed but no channel->zone "
                                            "mapping recognised"]}
        except Exception as e:
            silence = {"_unavailable": [f"war_channels.json unreadable: {e}"]}
    else:
        silence = {"_unavailable": ["war_channels.json not found — silence is not "
                                    "measurable from a single pull"]}

    unmapped = sorted({h[2] for hits in seen.values() for h in hits
                       if str(h[2]).startswith("UNMAPPED")})
    return rows, {z: len(v) for z, v in zone_chans.items()}, silence, unmapped


def seal_records(rows, limit=12):
    rows = [r for r in rows if not r.get("template")]
    """Origin claims as sealed statements. Content hash, KNP-shaped."""
    out = []
    for r in rows[:limit]:
        stmt = (f"In the NETZ watched-channel corpus, the phrase [{r['phrase']}] "
                f"first appears at {r['origin']['at']} on channel {r['origin']['channel']} "
                f"(side {r['origin']['side']}, zone {r['zone']}). "
                f"First in this corpus is not first in the world.")
        out.append({"statement": stmt,
                    "sha256": hashlib.sha256(stmt.encode("utf-8")).hexdigest(),
                    "phrase": r["phrase"], "kind": "origin_claim"})
    return out


CAVEAT = ("*First appearance is measured **inside this corpus only**. It is an origin claim "
          "about a watched channel set, not about the world, and it is exactly as strong as "
          "that channel list. Phrases are counted in their source language: the propagating "
          "unit is the original wording, not a translation of it.*")


def render(rows, zone_counts, silence, src, stamp):
    o = ["## OHRWURM — PHRASE PROPAGATION AND VARIANCE\n", CAVEAT, ""]
    o.append(f"Pull: `{src}` · {len(rows)} phrases above floor · rendered {stamp}\n")

    live = [r for r in rows if not r.get("template")]
    template = [r for r in rows if r.get("template")]
    crossed = [r for r in live if not r["confined_to_origin_side"]]
    confined = [r for r in live if r["confined_to_origin_side"]]
    o.append(f"**{len(crossed)} crossed a side boundary · {len(confined)} stayed inside "
             f"the side that originated them.**\n")
    o.append("> A phrase confined to one side is circulation. A phrase that crosses is either "
             "an event both sides can see, or an injection that took. This instrument does not "
             "distinguish those two — it dates and measures the crossing, and the reader judges "
             "which it was.\n")

    o.append("\n**◆ CROSSED THE DIVIDE**\n")
    if not crossed:
        o.append("_None this window. Every phrase above the floor stayed inside its origin side._\n")
    for r in crossed[:15]:
        o.append(f"**[{r['phrase']}]** · {r['zone']}")
        o.append(f"- origin {r['origin']['at']} · {r['origin']['channel']} · side {r['origin']['side']}")
        o.append(f"- crossed to **{r['crossed_to']['side']}** after "
                 f"**{r['hours_to_cross_side']}h** via {r['crossed_to']['channel']}")
        o.append(f"- {r['reports']} reports · {r['channels']} channels · "
                 f"{r['sides']} sides · balance {r['side_balance']}")
        o.append(f"- second channel at {r['hours_to_second_channel']}h · span {r['span_hours']}h\n")

    o.append("\n**▨ CONFINED — HIGH VOLUME, ONE SIDE**\n")
    o.append("> These are the propaganda candidates. Volume without crossing is a side talking "
             "to itself, which is the shape of a line being distributed rather than an event "
             "being observed.\n")
    for r in confined[:15]:
        o.append(f"- **[{r['phrase']}]** · {r['zone']} · {r['reports']} rpt / {r['channels']} chan · "
                 f"all *{r['origin']['side']}* · second channel {r['hours_to_second_channel']}h · "
                 f"span {r['span_hours']}h · origin {r['origin']['channel']}")

    if template:
        o.append(f"\n\n**▪ TEMPLATE — SUPPRESSED ({len(template)})**\n")
        o.append("> Carried by most channels across most sides. That is furniture — digest "
                 "headers, subscribe footers, channel signatures — not propagation. Listed so "
                 "the suppression can be checked rather than trusted.\n")
        for r in template[:8]:
            o.append(f"- [{r['phrase']}] · {r['reports']} rpt / {r['channels']} chan / {r['sides']} sides")

    o.append("\n\n**◻ SILENCE**\n")
    o.append("> A channel that speaks elsewhere and not here is data. Absence of collection and "
             "absence of event render identically unless this block is printed.\n")
    if "_unavailable" in silence:
        o.append(f"_Not measured: {silence['_unavailable'][0]}. A zone with no assigned "
                 f"channels and a zone whose channels went quiet are different facts, and "
                 f"this instrument will not guess which it is looking at._")
    elif not silence:
        o.append("_Every channel assigned to a zone spoke in it this window._")
    else:
        for z, missing in sorted(silence.items()):
            o.append(f"- **{z}** — {zone_counts.get(z,0)} of "
                     f"{zone_counts.get(z,0)+len(missing)} assigned channels spoke · "
                     f"**{len(missing)} silent**: {', '.join(missing[:6])}"
                     + (" …" if len(missing) > 6 else ""))

    o.append("\n\n**◈ SEAL-READY ORIGIN CLAIMS**\n")
    o.append("> Each carries the SHA-256 of its own statement. Committing one under KNP dates a "
             "first-appearance call before the phrase becomes salient — the retro-prescient shape "
             "applied to language rather than to events.\n")
    for s in seal_records(rows):
        o.append(f"- `{s['sha256'][:16]}…` — [{s['phrase']}]")
    return "\n".join(o)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file")
    ap.add_argument("--latest", action="store_true")
    ap.add_argument("--schema", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--min-reports", type=int, default=4)
    ap.add_argument("--min-channels", type=int, default=2)
    ap.add_argument("--gram-lo", type=int, default=2)
    ap.add_argument("--gram-hi", type=int, default=5)
    a = ap.parse_args()

    if a.file:
        src = Path(a.file)
    else:
        pulls = sorted(FORECASTS.glob("tg_wardesk_*.json"),
                       key=lambda p: p.stat().st_mtime, reverse=True)
        if not pulls:
            print("no tg_wardesk_*.json in forecasts\\ — run tg_fetch.py first")
            return 1
        src = pulls[0]

    doc = json.loads(src.read_text(encoding="utf-8"))
    msgs = find_messages(doc)
    if not msgs:
        print(f"no message list found in {src.name}. Top-level keys: {list(doc)[:12]}")
        return 1
    fmap, keys = detect(msgs)

    print(f"OHRWURM · {src.name} · {len(msgs)} messages")
    print(f"  field map: {fmap}")
    if a.schema:
        print(f"  all keys seen: {keys}")
        missing = [k for k, v in fmap.items() if v is None]
        if missing:
            print(f"  UNMAPPED: {missing} — paste the key list above and Claude will extend CAND.")
        return 0
    if not fmap["text"] or not fmap["ts"]:
        print("  FAIL — no text or timestamp field detected. Run --schema and paste the keys.")
        return 1

    rows, zone_counts, silence, unmapped = analyse(msgs, fmap, a.min_reports,
                                                   a.min_channels, a.gram_lo, a.gram_hi)
    print(f"  side map: {SIDE_MAP_SOURCE}")
    if unmapped:
        print(f"  ! UNMAPPED SIDES (add to tg_cluster.SIDES): {', '.join(unmapped)}")
    stamp = datetime.now(timezone.utc).strftime("%d%H%MZ %b %y").upper()
    face = render(rows, zone_counts, silence, src.name, stamp)

    live = [r for r in rows if not r.get("template")]
    crossed = sum(1 for r in live if not r["confined_to_origin_side"])
    print(f"  {len(rows)} phrases above floor · {len(live)} live "
          f"({crossed} crossed, {len(live)-crossed} confined) · "
          f"{len(rows)-len(live)} suppressed as template")

    if a.dry_run:
        print("\n" + face)
        print("\n(dry run — nothing written)")
        return 0

    out_stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M")
    FORECASTS.mkdir(exist_ok=True)
    jf = FORECASTS / f"ohrwurm_{out_stamp}.json"
    mf = FORECASTS / f"OHRWURM_{out_stamp}.md"
    payload = {
        "schema": "ohrwurm/v1",
        "generated": datetime.now(timezone.utc).isoformat(),
        "source_pull": src.name,
        "caveat": "first appearance is corpus-local, not global; phrases counted in source language",
        "floors": {"min_reports": a.min_reports, "min_channels": a.min_channels,
                   "gram_range": [a.gram_lo, a.gram_hi]},
        "phrases": rows,
        "side_map_source": SIDE_MAP_SOURCE,
        "unmapped_sides": unmapped,
        "zone_channel_counts": zone_counts,
        "silence": silence,
        "seal_ready": seal_records(rows),
    }
    blob = json.dumps(payload, ensure_ascii=False, indent=1)
    jf.write_text(blob, encoding="utf-8")
    mf.write_text(face, encoding="utf-8")
    print(f"  → {jf}")
    print(f"  → {mf}")

    # The served copy is a build product, never a manual copy. Same rule the
    # ledger mirrors learned the hard way: three drifted in one night before
    # render_ledger was made to publish them itself.
    if DOCS.exists():
        (DOCS / "ohrwurm_latest.json").write_text(blob, encoding="utf-8")
        print(f"  → {DOCS / 'ohrwurm_latest.json'}  (served copy)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
