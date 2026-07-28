#!/usr/bin/env python3
"""
classify.py - content classification and PIR routing for NETZ.

WHY THIS EXISTS
    Category is assigned by feed. Al Jazeera, BBC World, DW and Defense One are
    hardcoded to military_conflict, so on 2026-07-27 that bucket held an
    All-Ireland final, a Parkinson's diagnosis, a Bali running club and a death
    at 81. Top Signals ranks inside those buckets and Key Judgments reads Top
    Signals, so the desk's five highest-confidence judgments that day were
    Pauline Hanson, Berlin, Boy George, a UK poll and Sam Altman - while
    Convergence Watch, which ignores feeds entirely, put Iran at the top with
    23 stories across four categories.

    Same day, all four PIRs printed "no collection against this requirement"
    while the record carried a US-Iran strike pause at a chokepoint, a surprise
    Singapore tightening, and CISA unreachable. Collection ran. Requirements sat
    unwired beside it.

DESIGN CHOICE, STATED
    This is a LEXICON classifier, not a model call. It is slower to improve and
    it will miss things a model would catch. It was chosen anyway because every
    decision it makes prints the rule that fired, which means a stranger can
    audit a category the way they can audit a citation. A model classifier is
    unauditable per item. On a desk whose whole argument is a checkable record,
    that trade goes this way. Revisit once there is a scored reason to.

    Nothing here deletes a feed's opinion. The original is kept as
    cl["feed_category"] and the override is recorded in cl["category_rule"].

USE
    python classify.py --selftest reports\\battle_report_2026-07-27_1502.md
        Dry run. Prints what would move and which PIRs would be answered.
        Changes nothing.
"""
from __future__ import annotations
import argparse, re, sys
from pathlib import Path

# ----------------------------------------------------------------------
# Lexicon. Weight 3 = decisive, 2 = strong, 1 = supporting.
# Keys are matched as whole words, case-insensitively.
# ----------------------------------------------------------------------
LEX: dict[str, dict[int, list[str]]] = {
    "military_conflict": {
        3: ["airstrike", "airstrikes", "ceasefire", "offensive", "missile", "missiles",
            "drone strike", "shelling", "incursion", "insurgency", "militia", "militias",
            "war crimes", "troop", "troops", "brigade", "division", "artillery",
            "no-fly", "blockade", "mobilisation", "mobilization", "armistice"],
        2: ["strike", "strikes", "military", "armed forces", "combat", "front line",
            "frontline", "war", "warfare", "occupation", "rebel", "rebels", "junta",
            "coup", "paramilitary", "hostilities", "truce", "casualties", "wounded",
            "central command", "centcom", "pentagon", "nato", "defence ministry",
            "defense ministry", "houthi", "hezbollah", "irgc"],
        1: ["conflict", "attack", "attacks", "security forces", "deployment"],
    },
    "cyber": {
        3: ["vulnerability", "vulnerabilities", "cve-", "zero-day", "ransomware",
            "exploit", "exploited", "malware", "backdoor", "data breach", "phishing",
            "command-and-control", "sandbox escape", "supply-chain attack", "kev"],
        2: ["hacked", "hacker", "hackers", "breach", "cyberattack", "cyber attack",
            "threat actor", "botnet", "credential", "credentials", "patch", "patched",
            "cisa", "encryption", "spyware", "intrusion"],
        1: ["cyber", "security researchers", "attack surface", "endpoint"],
    },
    "economic": {
        3: ["interest rate", "interest rates", "central bank", "monetary policy",
            "inflation", "rate cut", "rate hike", "basis points", "bond yield",
            "yields", "earnings", "gdp", "recession", "tariff", "tariffs",
            "federal reserve", "fomc", "ipo", "market debut"],
        2: ["oil prices", "crude", "brent", "stocks", "shares", "equities", "index",
            "investors", "profit", "revenue", "trade deal", "currency", "barrel",
            "commodity", "commodities", "treasury", "treasurys", "valuation"],
        1: ["market", "markets", "economy", "economic", "price", "prices", "growth"],
    },
    "disaster_infrastructure": {
        3: ["earthquake", "magnitude", "wildfire", "wildfires", "flood", "flooding",
            "hurricane", "typhoon", "cyclone", "tsunami", "landslide", "eruption",
            "famine", "drought", "evacuation", "evacuated", "power outage",
            "grid failure", "dam", "desalination"],
        2: ["blaze", "storm", "heatwave", "heat wave", "displaced", "displacement",
            "emergency services", "rescue", "aid", "relief", "hectares", "casualty",
            "infrastructure", "pipeline", "refinery"],
        1: ["fire", "damage", "alert", "warning", "crisis"],
    },
    "political": {
        3: ["election", "elections", "parliament", "referendum", "impeachment",
            "prime minister", "president", "cabinet", "legislation", "bill passed",
            "sanctions", "resignation", "coalition", "opinion poll", "voting intention",
            "senate", "congress", "supreme court", "indicted", "sworn in",
            "deported", "deportation", "immigration crackdown", "asylum", "visa revoked",
            "border enforcement", "ice raid", "extradition"],
        2: ["minister", "government", "policy", "vote", "voters", "party", "lawmakers",
            "diplomat", "diplomatic", "treaty", "summit", "ruling", "court", "lawsuit",
            "protest", "protests", "opposition"],
        1: ["political", "leader", "officials", "talks"],
    },
    "crime_security": {
        3: ["homicide", "murder", "manslaughter", "mass shooting", "stabbing",
            "kidnapping", "trafficking", "cartel", "arrested and charged",
            "sentenced", "convicted", "extradited", "raid"],
        2: ["shooting", "shot dead", "police", "prosecutors", "charged", "suspect",
            "custody", "gunman", "assault", "smuggling"],
        1: ["crime", "criminal", "investigation", "detained"],
    },
}

# Content that carries no standing-requirement value regardless of feed.
NOISE = {
    3: ["all-ireland", "gaelic football", "world cup", "premier league", "grand slam",
        "wimbledon", "tour de france", "t20", "test match", "nba", "nfl", "olympics",
        "box office", "chart-topping", "singles chart", "album", "red carpet"],
    2: ["match", "final", "champions", "striker", "goalkeeper", "tournament",
        "celebrity", "actor", "actress", "singer", "song", "film", "movie", "series",
        "recipe", "horoscope", "obituary", "dies at", "died at", "diagnosis reveals"],
}

MIN_SCORE = 3            # below this the feed's category is left alone
MARGIN    = 2            # winner must beat runner-up by this to override


def _hits(text: str, table: dict[int, list[str]]) -> tuple[int, list[str]]:
    low = " " + re.sub(r"[^a-z0-9\- ]+", " ", text.lower()) + " "
    score, fired = 0, []
    for weight, terms in table.items():
        for t in terms:
            if re.search(r"(?<![a-z0-9])" + re.escape(t) + r"(?![a-z0-9])", low):
                score += weight
                fired.append(f"{t}({weight})")
    return score, fired


def classify_text(text: str, fallback: str) -> tuple[str, str, dict]:
    """Return (category, rule, all_scores). Falls back to the feed's category."""
    scores = {cat: _hits(text, tab) for cat, tab in LEX.items()}
    noise, noise_fired = _hits(text, NOISE)

    ranked = sorted(((s, c, f) for c, (s, f) in scores.items()), reverse=True)
    top_s, top_c, top_f = ranked[0]
    second_s = ranked[1][0] if len(ranked) > 1 else 0

    decisive = any(f.endswith("(3)") for f in top_f)
    if noise >= 3 and noise - top_s >= MARGIN and not decisive:
        return "noise", f"noise:{','.join(noise_fired[:3])}", {c: s for s, c, _ in ranked}
    if top_s < MIN_SCORE:
        return fallback, f"feed:{fallback} (no lexicon signal)", {c: s for s, c, _ in ranked}
    if top_s - second_s < MARGIN:
        return fallback, f"feed:{fallback} (ambiguous {top_c}/{ranked[1][1]})", {c: s for s, c, _ in ranked}
    return top_c, f"content:{','.join(top_f[:4])}", {c: s for s, c, _ in ranked}


def cluster_text(cl: dict) -> str:
    parts = []
    for it in cl.get("items", []) or []:
        for k in ("title", "summary", "text"):
            v = it.get(k)
            if isinstance(v, str):
                parts.append(v)
    for k in ("title", "summary"):
        v = cl.get(k)
        if isinstance(v, str):
            parts.append(v)
    return " ".join(parts)[:4000]


def reclassify(clusters: list, log_path: str | None = "classify_log.json") -> list:
    """In place. Keeps the feed's opinion at feed_category, records the rule.

    Writes a decision log so every override is auditable on disk even before
    the faces render the rule. That log is the whole reason this is a lexicon
    and not a model call - drop it and the trade stops paying.
    """
    for cl in clusters:
        feed_cat = cl.get("category")
        cat, rule, scores = classify_text(cluster_text(cl), feed_cat)
        cl["feed_category"] = feed_cat
        cl["category_rule"] = rule
        cl["category_scores"] = scores
        cl["category"] = feed_cat if cat == "noise" else cat
        cl["low_value"] = (cat == "noise")

    if log_path:
        try:
            import json, datetime
            rows = [{"title": (cluster_text(c)[:140] or "(empty)"),
                     "feed_category": c.get("feed_category"),
                     "category": c.get("category"),
                     "low_value": c.get("low_value"),
                     "rule": c.get("category_rule"),
                     "scores": c.get("category_scores")}
                    for c in clusters]
            moved = sum(1 for r in rows if r["feed_category"] != r["category"])
            json.dump({"generated_at": datetime.datetime.now(datetime.timezone.utc)
                                        .strftime("%Y-%m-%dT%H:%M:%SZ"),
                       "classifier": "classify.py lexicon v1",
                       "clusters": len(rows), "moved": moved,
                       "demoted_low_value": sum(1 for r in rows if r["low_value"]),
                       "decisions": rows},
                      open(log_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        except Exception as e:
            print(f"classify: log write failed ({e}) - continuing", file=sys.stderr)
    return clusters


# ----------------------------------------------------------------------
# PIR routing
# ----------------------------------------------------------------------
PIR_EXPAND = {
    "chokepoint": ["hormuz", "bab el-mandeb", "bab al-mandab", "suez", "malacca",
                   "strait", "straits", "tanker", "tankers", "shipping lane",
                   "red sea", "gulf of aden", "maritime"],
    "vulnerabilit": ["cve-", "zero-day", "exploited", "kev", "patch", "rce",
                     "sandbox escape", "critical infrastructure", "scada", "ics"],
    "central bank": ["federal reserve", "fomc", "ecb", "boj", "monetary authority",
                     "rate hike", "rate cut", "basis points", "tightening", "easing"],
    "dislocation": ["selloff", "sell-off", "plunged", "surged", "circuit breaker",
                    "worst day", "biggest one-day", "rout"],
    "ceasefire":  ["truce", "pause", "paused", "halt", "halted", "armistice",
                   "de-escalation", "peace talks"],
    "offensive":  ["ground operation", "incursion", "assault", "advance", "captured",
                   "airstrike", "airstrikes", "strikes"],
    "conflict onset": ["declared war", "invaded", "invasion", "mobilised", "mobilized"],
}


def _pir_terms(pir_text: str) -> list[str]:
    low = pir_text.lower()
    terms = [w for w in re.findall(r"[a-z][a-z\-]{4,}", low)
             if w not in {"about", "which", "their", "these", "those", "where",
                          "affecting", "exceeding", "listed", "major", "state-level"}]
    for key, expansion in PIR_EXPAND.items():
        if key in low:
            terms += expansion
    return sorted(set(terms))


def route_pirs(config: dict, clusters: list, existing: list | None = None) -> list:
    """Match classified clusters to standing requirements.

    Returns the same shape pir_status produces, with an `items` list populated
    where the record actually answers the requirement. Anything already matched
    upstream is preserved - this only fills what came back empty.
    """
    pirs = config.get("pirs", []) or []
    existing_by_text = {}
    for e in (existing or []):
        if isinstance(e, dict) and e.get("pir"):
            existing_by_text[e["pir"]] = e

    out = []
    for p in pirs:
        text = p if isinstance(p, str) else p.get("pir", "")
        prior = existing_by_text.get(text, {"pir": text, "items": []})
        if prior.get("items"):
            out.append(prior)
            continue

        terms = _pir_terms(text)
        scored = []
        for cl in clusters:
            if cl.get("low_value"):
                continue
            blob = " " + re.sub(r"[^a-z0-9\- ]+", " ", cluster_text(cl).lower()) + " "
            fired = []
            for t in terms:
                pat = (r"(?<![a-z0-9])" + re.escape(t) + r"(?![a-z0-9])") if len(t) < 6 \
                      else (r"(?<![a-z0-9])" + re.escape(t[:max(5, len(t)-3)]))
                if re.search(pat, blob):
                    fired.append(t)
            if len(fired) >= 2:
                scored.append((len(fired), fired[:4], cl))
        scored.sort(key=lambda x: -x[0])

        prior["items"] = [{"cluster": cl, "matched_on": fired, "score": n}
                          for n, fired, cl in scored[:6]]
        prior["routed_by"] = "classify.route_pirs"
        out.append(prior)
    return out


# ----------------------------------------------------------------------
# Selftest against a rendered report. Changes nothing.
# ----------------------------------------------------------------------
SEC_RE  = re.compile(r"^##\s+[IVXL]+\.\s+(.+?)\s*$", re.M)
ITEM_RE = re.compile(r"^\s*(\d+)\.\s+(?:.*?\]\s*)?(.+?)\s+·", re.M)

def selftest(path: str) -> int:
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    marks = [(m.start(), m.group(1).strip()) for m in SEC_RE.finditer(text)]
    clusters = []
    for i, (pos, title) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        cat = title.lower().replace(" ", "_")
        if cat not in LEX and cat not in ("disaster_infrastructure",):
            continue
        for m in ITEM_RE.finditer(text[pos:end]):
            headline = re.sub(r"^[^A-Za-z0-9]*", "", m.group(2)).strip()
            clusters.append({"category": cat, "items": [{"title": headline}]})

    if not clusters:
        print("selftest: no numbered record items parsed - is this a battle report?")
        return 2

    before = [(c["category"], c["items"][0]["title"]) for c in clusters]
    reclassify(clusters)

    moved = [(b, c) for (b, c) in zip(before, clusters) if b[0] != c["category"] or c["low_value"]]
    print(f"classify selftest · {path}")
    print(f"  {len(clusters)} items · {len(moved)} would move or be demoted\n")
    for (old_cat, title), cl in moved:
        tag = "NOISE" if cl["low_value"] else f"{old_cat} -> {cl['category']}"
        print(f"  [{tag}]")
        print(f"     {title[:96]}")
        print(f"     rule: {cl['category_rule']}\n")

    kept = {}
    for cl in clusters:
        if not cl["low_value"]:
            kept[cl["category"]] = kept.get(cl["category"], 0) + 1
    print("  post-classification counts: " + ", ".join(f"{k} {v}" for k, v in sorted(kept.items())))
    print(f"  demoted as low-value: {sum(1 for c in clusters if c['low_value'])}")

    demo_pirs = {"pirs": [
        "Escalation or de-escalation at maritime chokepoints (Hormuz, Bab el-Mandeb, Suez, Malacca)",
        "Actively exploited vulnerabilities affecting critical infrastructure or government systems",
        "Central bank policy shifts or market dislocations exceeding 2% daily moves",
        "State-level conflict onset, ceasefire, or major offensive operations"]}
    print("\n  PIR routing against these clusters (config pirs will differ):")
    for p in route_pirs(demo_pirs, clusters, None):
        n = len(p["items"])
        print(f"\n   PIR: {p['pir'][:78]}")
        print(f"        {n} item(s) matched" if n else "        no collection")
        for it in p["items"][:3]:
            print(f"          - {it['cluster']['items'][0]['title'][:78]}")
            print(f"            on: {', '.join(it['matched_on'])}")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", metavar="REPORT")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest(a.selftest))
    print(__doc__)
