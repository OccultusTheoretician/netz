#!/usr/bin/env python3
"""tg_cluster.py — NETZ War Desk Module 2 (v3): same-event clustering.

v3 corrects three defects in v2 that between them manufactured false Grade A
events and destroyed real ones:

  1. CHAINING. v2 used union-find over pairwise similarity. Union-find is
     transitive; the 8h window was only enforced pairwise. A~B, B~C, C~D welded
     four unrelated strikes into one 18h "event" spanning seven towns and scored
     it A. v3 keys clusters on the anchor itself and merges only on strong
     member overlap, capped at 3 anchors. Chains cannot form.

  2. NAMING DIVIDE. v2 treated Shechem and Nablus, Odessa and Odesa,
     Konstantinovka and Kostiantynivka as different places. Those are the same
     ground under the two sides' own names -- precisely the cases cross-bias
     verification exists for. v3 canonicalizes through ALIASES and records the
     surface variants, so the naming divide becomes visible evidence instead of
     a silent split.

  3. CAMP LABEL != SIDE. v2 counted distinct bias-label prefixes. In the
     registry, pro-russia / pro-kremlin / russian are three labels for one side:
     Rybar + Readovka + RIA alone scored "A -- confirmed across 3+ hostile
     camps" with no Ukrainian source in it. v3 grades on distinct SIDES.
     Camp labels are still reported, for transparency, but they do not grade.

Also: zone is now derived from where the event IS, not from the reporting
channel's beat, so an Iranian channel reporting Nablus lands in the Levant with
the Israeli and Palestinian reports of the same raid instead of in "iran" alone.
"""
import json, sys, re, pathlib, datetime, itertools
from collections import defaultdict, Counter

TIME_WINDOW_HRS = 8
MAX_ANCHORS = 3          # an "event" spanning more towns than this is a digest
DIGEST_PLACES = 4        # a message naming this many places is a roundup post
MERGE_OVERLAP = 0.6      # Jaccard on member sets required to merge two anchors

ZONE_MARKERS = {"gaza","tehran","hormuz","west bank","lebanon","israel","iran",
 "ukraine","russia","syria","yemen","red sea","sudan","donbas"}

# Statement-track anchors: topics that make a non-kinetic report clusterable.
# A statement confirmed across hostile sides means THE CLAIM CIRCULATED ON BOTH
# SIDES -- it does not mean the claim is true. The renderer prints that line.
STATEMENT_TOPICS = {"ceasefire","truce","negotiation","talks","sanctions","sanction",
 "mobilization","mobilisation","conscription","offensive","withdrawal","evacuation",
 "blockade","closure","ultimatum","nuclear","enrichment","embargo","prisoner swap",
 "prisoner exchange","martial law","no-fly","peace plan","security guarantees",
 "grain corridor","annexation","referendum","coup","oil price","tanker","escalation",
 "de-escalation","strait of hormuz","red sea","airspace","incursion","summit",
 "war powers","resolution","strike package","retaliation","casualty exchange"}
# Capitals double as metonyms for their governments ("Tehran rejects...").
# A capital-only message carrying topics+actors and no weapons is a statement,
# not a strike report, and is routed to the statement track.
CAPITALS = {"tehran","jerusalem","damascus","sanaa","khartoum"}
ACTOR_ZONE = {"khamenei":"iran","araghchi":"iran","irgc":"iran",
 "putin":"russia_ukraine","kremlin":"russia_ukraine","fsb":"russia_ukraine",
 "zelensky":"russia_ukraine","zelenskyy":"russia_ukraine","gur":"russia_ukraine","hur":"russia_ukraine",
 "netanyahu":"israel_gaza","idf":"israel_gaza","knesset":"israel_gaza","mossad":"israel_gaza",
 "sinwar":"israel_gaza","nasrallah":"lebanon","assad":"syria","erdogan":"kurdistan",
 "sdf":"kurdistan","rsf":"sudan","saf":"sudan","m23":"drc","wagner":"sahel"}
# Variant spellings and plurals of the same topic must land in the same bucket,
# or one story mints two "independent" events from its own vocabulary.
TOPIC_ALIASES = {"sanction":"sanctions","mobilisation":"mobilization",
                 "truce":"ceasefire","negotiations":"negotiation",
                 "prisoner exchange":"prisoner swap","de-escalation":"escalation"}
def canon_topic(w):
    return TOPIC_ALIASES.get(w, w)


INSTITUTIONS = {"idf","irgc","centcom","nato","un","icc","kremlin","knesset","pentagon",
 "state department","foreign ministry","defense ministry","white house","opec",
 "security council","mossad","fsb","gur","hur"}

# canonical place -> zone. The event's zone, not the channel's.
PLACE_ZONE = {}
def _z(zone, *places):
    for p in places: PLACE_ZONE[p] = zone
_z("russia_ukraine","konstantinovka","pokrovsk","bakhmut","avdiivka","kharkiv","kherson",
   "zaporizhzhia","kupiansk","kramatorsk","chasiv yar","toretsk","belgorod","kursk","crimea",
   "sevastopol","donetsk","luhansk","sumy","odesa","mariupol","melitopol","nikopol","vovchansk")
# KK28-TOOLWORK (board 13): main-theatre capitals + recurring deep-strike
# geography. The WARDESK's most-cited cities were unresolvable by this table.
_z("russia_ukraine","kyiv","lviv","dnipro","mykolaiv","kryvyi rih","chernihiv","izium",
   "sloviansk","moscow","st petersburg","engels","rostov-on-don","voronezh","bryansk",
   "novorossiysk")
_z("israel_gaza","rafah","khan younis","jabalia","jenin","nablus","tel aviv","haifa","tulkarem",
   "deir al-balah","gaza city","ramallah","hebron","jerusalem")
_z("lebanon","beirut","dahiyeh")
_z("syria","damascus","golan","aleppo","latakia")
_z("iran","isfahan","natanz","bushehr","bandar abbas","jask","sirik","fordow","parchin","tehran")
_z("yemen","sanaa","hodeidah","bab al-mandab")
_z("sudan","khartoum","omdurman","darfur","el fasher","port sudan")
_z("sahel","bamako","ouagadougou","niamey")
_z("drc","goma","rutshuru")
_z("myanmar","naypyidaw","rakhine","kachin")

# surface variant -> canonical. THE cross-bias instrument for place names:
# the two sides that most need comparing use different names for the same ground.
ALIASES = {
 # KK28-TOOLWORK: Russian-form and transliteration variants for the additions —
 # the cross-bias point of the table: both sides' names for the same ground.
 "kiev":"kyiv", "kyyiv":"kyiv", "lvov":"lviv", "dnepr":"dnipro",
 "dnipropetrovsk":"dnipro", "nikolaev":"mykolaiv", "mykolayiv":"mykolaiv",
 "krivoy rog":"kryvyi rih", "kryvyi rig":"kryvyi rih", "chernigov":"chernihiv",
 "izyum":"izium", "slavyansk":"sloviansk", "saint petersburg":"st petersburg",
 "sankt-peterburg":"st petersburg", "moskva":"moscow", "rostov":"rostov-on-don",
 "kostiantynivka":"konstantinovka", "konstantinivka":"konstantinovka",
 "odessa":"odesa", "kharkov":"kharkiv", "kherson city":"kherson",
 "zaporozhye":"zaporizhzhia", "zaporizhia":"zaporizhzhia",
 "kupyansk":"kupiansk", "lugansk":"luhansk", "artemovsk":"bakhmut",
 "krasnoarmeysk":"pokrovsk", "ugledar":"vuhledar", "vuhledar":"vuhledar",
 "shechem":"nablus", "shchem":"nablus",
 "khan yunis":"khan younis", "khan-younis":"khan younis",
 "jabalya":"jabalia", "tulkarm":"tulkarem", "deir el-balah":"deir al-balah",
 "al-quds":"jerusalem", "beit lahia":"jabalia",
 "sana'a":"sanaa", "hudaydah":"hodeidah", "al hudaydah":"hodeidah",
 "esfahan":"isfahan", "ispahan":"isfahan", "bandar-abbas":"bandar abbas",
 "el-fasher":"el fasher", "al-fashir":"el fasher",
}
SPECIFIC_PLACES = set(PLACE_ZONE) | set(ALIASES)

# camp label -> side. Grading counts SIDES. Labels remain visible but do not grade.
SIDES = {
 "pro-russia":"RU", "pro-kremlin":"RU", "russian":"RU", "russia":"RU",
 "pro-ukraine":"UA", "ukrainian":"UA", "ukraine":"UA",
 "pro-israel":"IL", "israeli":"IL",
 "pro-palestinian":"PS", "palestinian":"PS", "hamas":"PS",
 "pro-hezbollah/axis":"AXIS", "houthi":"AXIS", "iranian":"AXIS", "hezbollah":"AXIS",
 "anti-regime":"OPP", "opposition":"OPP",
 "syrian":"SY", "turkish":"TR", "pro-sdf":"SDF",
 "anti-junta":"NUG", "junta":"JUNTA", "junta-aligned":"JUNTA", "nug-aligned":"NUG",
 "saf-aligned":"SAF", "rsf-aligned":"RSF", "aes-aligned":"AES",
 "m23-aligned":"M23", "drc-gov":"DRC", "prc-aligned":"PRC", "taiwan-gov":"TW",
 "coalition-aligned":"GCC", "turkish-aligned":"TR", "kurdish":"SDF",
 "western":"WEST", "us":"WEST", "nato":"WEST",
 "mixed":"MIXED", "neutral-ish":"MIXED", "neutral":"MIXED",
}
def side_of(bias: str) -> str:
    b = (bias or "").strip().lower()
    camp = b.split()[0] if b else ""
    return SIDES.get(camp) or SIDES.get(b) or ("UNMAPPED:" + (camp or "?"))

ACTORS = {"zelensky","zelenskyy","putin","netanyahu","khamenei","araghchi","trump","centcom",
 "idf","rsf","saf","wagner","cassad","erdogan","assad","sdf","m23","sinwar","nasrallah",
 "gallant","zvinchuk"}
WEAPONS = {"himars","atacms","storm shadow","shahed","geran","kinzhal","iskander","shahed-136",
 "drone","uav","missile","airstrike","ballistic","cruise","artillery","s-300","s-400","patriot",
 "f-16","f-35","tomahawk","hypersonic","glide bomb","fab","kab"}
CAP_RE = re.compile(r'\b([A-Z][a-z]{3,})\b')
NUM_RE = re.compile(r'\b(\d{2,})\b')
CASUALTY_RE = re.compile(r'\b(\d+)\s*(?:killed|dead|wounded|injured|casualt|soldiers?|troops?)', re.I)
STOP_CAPS = {"the","this","that","russian","ukrainian","israeli","iranian","president","minister",
 "july","august","monday","tuesday","today","footage","report","reports","video","channel","office"}


def canon(p: str) -> str:
    return ALIASES.get(p, p)


_WORD_CACHE = {}
def _word_in(term, t):
    """Boundary match: 'un' must be the word UN, not a syllable of 'until'."""
    pat = _WORD_CACHE.get(term)
    if pat is None:
        pat = _WORD_CACHE[term] = re.compile(r"\b" + re.escape(term) + r"\b")
    return bool(pat.search(t))


def signals(text_en):
    t = text_en.lower()
    raw = {p for p in SPECIFIC_PLACES if p in t}
    return {"specific": {canon(p) for p in raw},
            "variants": raw,
            "zonemark": {p for p in ZONE_MARKERS if p in t},
            "actors": {a for a in ACTORS if _word_in(a, t)} |
                      {i for i in INSTITUTIONS if _word_in(i, t)},
            "topics": {canon_topic(w) for w in STATEMENT_TOPICS if w in t},
            "weapons": {w for w in WEAPONS if w in t},
            "caps": set(m.lower() for m in CAP_RE.findall(text_en)) - STOP_CAPS,
            "nums": set(NUM_RE.findall(text_en)),
            "casualty": set(CASUALTY_RE.findall(text_en))}


def parse_dt(s):
    try:
        return datetime.datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except Exception:
        return None


def grade_event(n_sides, n_reports):
    """Grade on hostile SIDES, never on camp labels. Three Kremlin outlets are one
    voice; that is the entire point of the instrument."""
    if n_sides >= 3 and n_reports >= 3: return "A — confirmed across 3+ hostile sides"
    if n_sides >= 2 and n_reports >= 2: return "B — corroborated across the bias divide"
    if n_reports >= 3: return "C — multiply reported, single side (echo, not corroboration)"
    if n_reports == 2: return "F — repeated within one side, below the 3-report echo floor"
    return "F — single source, uncorroborated"


def cluster(msgs):
    events = kinetic_pass(msgs) + statement_pass(msgs)
    events.sort(key=lambda e: (e["n_sides"], e["n_reports"]), reverse=True)
    return events


def kinetic_pass(msgs):
    txt = [(m.get("text_en") or m.get("text") or "") for m in msgs]
    sig = [signals(t) for t in txt]
    dts = [parse_dt(m.get("date")) for m in msgs]

    # 1 — anchor-keyed bucketing. A roundup naming five towns contributes evidence
    #     to five places without welding them into one event.
    buckets = defaultdict(list)
    for i, s in enumerate(sig):
        if not s["specific"]:
            continue
        if s["specific"] <= CAPITALS and s["topics"] and s["actors"] and not s["weapons"]:
            continue                      # government-metonym statement, not a strike
        for p in s["specific"]:
            buckets[p].append(i)

    # 2 — split each anchor bucket into time-contiguous runs (absolute, not pairwise)
    cand = []
    for place, members in buckets.items():
        members.sort(key=lambda i: dts[i] or datetime.datetime.min.replace(
            tzinfo=datetime.timezone.utc))
        run = []
        for i in members:
            # window is ABSOLUTE from the run's first message. Splitting on gaps alone
            # lets consecutive sub-window gaps accumulate into a 20h "event".
            if run and dts[i] and dts[run[0]] and \
               (dts[i] - dts[run[0]]).total_seconds() > TIME_WINDOW_HRS * 3600:
                cand.append(({place}, set(run))); run = []
            run.append(i)
        if run:
            cand.append(({place}, set(run)))

    # 3 — merge only on strong member overlap, hard-capped on anchor count
    merged, used = [], [False] * len(cand)
    for a in range(len(cand)):
        if used[a]:
            continue
        anchors, members = set(cand[a][0]), set(cand[a][1])
        used[a] = True
        for b in range(a + 1, len(cand)):
            if used[b] or len(anchors) >= MAX_ANCHORS:
                continue
            mb = cand[b][1]
            inter = len(members & mb)
            union = len(members | mb)
            if union and inter / union >= MERGE_OVERLAP:
                anchors |= cand[b][0]; members |= mb; used[b] = True
        merged.append((anchors, members))

    events = []
    for anchors, members in merged:
        ms = [msgs[i] for i in sorted(members)]
        idxs = sorted(members)
        camps = sorted({(m.get("bias") or "").split()[0] for m in ms if m.get("bias")})
        sides = sorted({side_of(m.get("bias")) for m in ms if m.get("bias")})
        per_side = Counter(side_of(m.get("bias")) for m in ms if m.get("bias"))
        chans_by_side = defaultdict(set)
        for m in ms:
            if m.get("bias") and m.get("channel"):
                chans_by_side[side_of(m["bias"])].add(m["channel"])
        per_side_channels = {k: len(v) for k, v in sorted(chans_by_side.items())}
        channels = sorted({m.get("channel") for m in ms if m.get("channel")})
        seen_names = sorted(set().union(*[sig[i]["variants"] for i in idxs]))
        aliases = sorted({v for v in seen_names if canon(v) in anchors})
        comentioned = sorted({v for v in seen_names if canon(v) not in anchors})
        mdts = [d for d in (dts[i] for i in idxs) if d]
        span = round((max(mdts) - min(mdts)).total_seconds() / 3600, 1) if len(mdts) > 1 else 0
        mergedsig = signals(" ".join(txt[i] for i in idxs))
        zone = PLACE_ZONE.get(sorted(anchors)[0], ms[0].get("zone", "unzoned"))

        sources = []
        for i in idxs:
            m = msgs[i]
            sources.append({
                "channel": m.get("channel"),
                "bias": m.get("bias"),
                "camp": (m.get("bias") or "").split()[0],
                "side": side_of(m.get("bias")),
                "casualty": sorted(sig[i]["casualty"]),
                "is_digest": len(sig[i]["specific"]) >= DIGEST_PLACES,
                "text_en": (m.get("text_en") or "")[:240],
                "date": m.get("date"),
            })

        events.append({
            "zone": zone,
            "channel_zones": sorted({m.get("zone") for m in ms if m.get("zone")}),
            "anchor": sorted(anchors),
            "anchor_aliases": aliases,          # true variant spellings of THIS anchor
            "co_mentioned": comentioned,        # other places named in the same messages
            "anchor_variants": aliases,         # legacy key, now correct
            "n_reports": len(ms),
            "n_channels": len(channels),
            "bias_camps": camps, "n_bias_camps": len(camps),
            "sides": sides, "n_sides": len(sides),
            "report_balance": dict(per_side.most_common()),
            "channels_per_side": per_side_channels,
            "single_outlet_sides": sorted(k for k, v in per_side_channels.items() if v == 1),
            "cross_side": len(sides) >= 2,
            "cross_bias": len(sides) >= 2,          # kept for downstream compatibility
            "digest_reports": sum(1 for s in sources if s["is_digest"]),
            "actors": sorted(mergedsig["actors"]),
            "weapons": sorted(mergedsig["weapons"]),
            "casualty_figures": sorted(mergedsig["casualty"]),
            "time_span_hrs": span,
            "first_seen": min(mdts).isoformat() if mdts else None,
            "last_seen": max(mdts).isoformat() if mdts else None,
            "grade": grade_event(len(sides), len(ms)),
            "sources": sources,
        })

    for e in events:
        e["track"] = "kinetic"
    return events


def statement_pass(msgs):
    """Second pass over messages WITHOUT a specific place anchor -- the statements,
    posture claims, policy moves, and negotiations the place-gate discards. Keyed on
    (zone, topic), same absolute window, same side-grading. Anchor = the topic."""
    txt = [(m.get("text_en") or m.get("text") or "") for m in msgs]
    sig = [signals(t) for t in txt]
    dts = [parse_dt(m.get("date")) for m in msgs]

    def statement_shaped(s_):
        if not s_["topics"] or not (s_["actors"] or len(s_["topics"]) >= 2):
            return False                  # a topic word alone is not a statement
        if s_["specific"] and not (s_["specific"] <= CAPITALS and not s_["weapons"]):
            return False                  # a real place + weapons is the kinetic pass's
        return True

    def statement_zone(s_, msg):
        zones = Counter(ACTOR_ZONE[a] for a in s_["actors"] if a in ACTOR_ZONE)
        return zones.most_common(1)[0][0] if zones else msg.get("zone", "unzoned")

    buckets = defaultdict(list)
    for i, s_ in enumerate(sig):
        if not statement_shaped(s_):
            continue
        zone = statement_zone(s_, msgs[i])
        for tp in s_["topics"]:
            buckets[(zone, tp)].append(i)

    cand = []
    for (zone, tp), members in buckets.items():
        members.sort(key=lambda i: dts[i] or datetime.datetime.min.replace(
            tzinfo=datetime.timezone.utc))
        run = []
        for i in members:
            if run and dts[i] and dts[run[0]] and                (dts[i] - dts[run[0]]).total_seconds() > TIME_WINDOW_HRS * 3600:
                cand.append((zone, tp, list(run))); run = []
            run.append(i)
        if run:
            cand.append((zone, tp, list(run)))

    events = []
    for zone, tp, idxs in cand:
        ms = [msgs[i] for i in idxs]
        camps = sorted({(m.get("bias") or "").split()[0] for m in ms if m.get("bias")})
        sides = sorted({side_of(m.get("bias")) for m in ms if m.get("bias")})
        per_side = Counter(side_of(m.get("bias")) for m in ms if m.get("bias"))
        chans_by_side = defaultdict(set)
        for m in ms:
            if m.get("bias") and m.get("channel"):
                chans_by_side[side_of(m["bias"])].add(m["channel"])
        channels = sorted({m.get("channel") for m in ms if m.get("channel")})
        mdts = [d for d in (dts[i] for i in idxs) if d]
        span = round((max(mdts) - min(mdts)).total_seconds() / 3600, 1) if len(mdts) > 1 else 0
        actors = sorted(set().union(*[sig[i]["actors"] for i in idxs]) or set())
        events.append({
            "track": "statement", "zone": zone, "anchor": [tp],
            "anchor_aliases": [tp], "co_mentioned": [],
            "statement_actors": actors,
            "n_reports": len(ms), "n_channels": len(channels),
            "bias_camps": camps, "n_bias_camps": len(camps),
            "sides": sides, "n_sides": len(sides),
            "report_balance": dict(per_side.most_common()),
            "channels_per_side": {k: len(v) for k, v in sorted(chans_by_side.items())},
            "single_outlet_sides": sorted(k for k, v in chans_by_side.items() if len(v) == 1),
            "cross_side": len(sides) >= 2, "cross_bias": len(sides) >= 2,
            "digest_reports": sum(1 for i in idxs if len(sig[i]["topics"]) >= 4),
            "actors": actors, "weapons": [], "casualty_figures": [],
            "time_span_hrs": span,
            "first_seen": min(mdts).isoformat() if mdts else None,
            "last_seen": max(mdts).isoformat() if mdts else None,
            "grade": grade_event(len(sides), len(ms)),
            "sources": [{"channel": msgs[i].get("channel"), "bias": msgs[i].get("bias"),
                         "camp": (msgs[i].get("bias") or "").split()[0],
                         "side": side_of(msgs[i].get("bias")),
                         "casualty": [], "is_digest": len(sig[i]["topics"]) >= 4,
                         "text_en": (msgs[i].get("text_en") or "")[:240],
                         "date": msgs[i].get("date")} for i in idxs],
        })
    return events


def load_msgs(paths):
    seen, out = set(), []
    for p in paths:
        d = json.loads(pathlib.Path(p).read_text(encoding="utf-8-sig"))
        for m in d["messages"]:
            k = (m["channel"], m["id"])
            if k in seen:
                continue
            seen.add(k); out.append(m)
    return out


def main():
    fc = pathlib.Path("forecasts")
    if "--all" in sys.argv:
        paths = sorted(fc.glob("tg_translated_*.json"))
    elif "--latest" in sys.argv or len(sys.argv) < 2:
        paths = sorted(fc.glob("tg_translated_*.json"))[-1:]
    else:
        paths = [pathlib.Path(sys.argv[1])]
    if not paths:
        print("No translated pulls.", file=sys.stderr); sys.exit(1)
    print(f"clustering from: {[p.name for p in paths]}", file=sys.stderr)

    msgs = load_msgs(paths); events = cluster(msgs)
    kin = [e for e in events if e["track"] == "kinetic"]
    stmt = [e for e in events if e["track"] == "statement"]
    xs = [e for e in events if e["cross_side"]]
    multi = [e for e in events if e["n_reports"] > 1]
    gA = [e for e in events if e["grade"].startswith("A")]
    gB = [e for e in events if e["grade"].startswith("B")]
    unmapped = sorted({s for e in events for s in e["sides"] if s.startswith("UNMAPPED")})

    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d_%H%M")
    out = fc / f"tg_events_{stamp}.json"
    out.write_text(json.dumps({"_meta": {
        "clustered": stamp + "Z", "schema": "tg_events/v3", "n_messages": len(msgs),
        "n_events": len(events), "n_multi_report": len(multi), "n_cross_side": len(xs),
        "grade_A": len(gA), "grade_B": len(gB), "unmapped_sides": unmapped,
        "note": "v3: anchor-keyed (no chaining), place aliases canonicalized, "
                "graded on hostile SIDES not camp labels, zone from event location."},
        "events": events}, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\n{len(msgs)} messages -> {len(events)} events "
          f"({len(kin)} kinetic + {len(stmt)} statement)", file=sys.stderr)
    print(f"  {len(multi)} multi-report | {len(xs)} cross-side | {len(gA)} grade-A | "
          f"{len(gB)} grade-B", file=sys.stderr)
    if unmapped:
        print(f"  ! UNMAPPED SIDES (add to SIDES): {', '.join(unmapped)}", file=sys.stderr)
    print(f"output: {out}\n", file=sys.stderr)
    print("=== GRADE A/B EVENTS (cross-side confirmed) ===", file=sys.stderr)
    for e in (gA + gB)[:10]:
        tk = "S" if e.get("track") == "statement" else "K"
        loc = ", ".join(e["anchor"]) or e["zone"]
        var = ""
        if len(e["anchor_aliases"]) > 1:
            var = f" [names: {'/'.join(e['anchor_aliases'])}]"
        cas = f" | cas:{e['casualty_figures']}" if e["casualty_figures"] else ""
        wpn = f" | {','.join(e['weapons'][:3])}" if e["weapons"] else ""
        bal = "/".join(f"{k}:{v}" for k, v in e["report_balance"].items())
        print(f"  [{e['grade'][:1]}/{tk}] {loc} ({e['zone']}){var} - {e['n_reports']}rpt/"
              f"{e['n_sides']}sides({bal})/{e['time_span_hrs']}h{cas}{wpn}", file=sys.stderr)
    if not (gA or gB):
        print("  (none cleared specific-anchor + cross-side this batch)", file=sys.stderr)


if __name__ == "__main__":
    main()
