#!/usr/bin/env python3
"""
cite_audit.py - citation SUPPORT audit for a Prescient Desk battle report.

The existing audit counts sentences carrying no citation. That catches the
uncited. It does not catch the MISCITED, which ships clean today: a sentence
with [4] attached asserting a figure that appears nowhere in item 4.

This checks three things the current block does not:

  MISCITED   a numeric claim whose figure does not appear in any cited item
  UNRESOLVED a citation index with no matching item in that section's record
  FORWARD    a completed-tense assertion about a date later than the report DTG

Limitation, stated because it governs how findings should be read: a report's
record carries item TITLES, not article bodies. So this tool proves support
against the record AS PRINTED - which is the correct standard for this desk,
because the record as printed is the only thing a reader can check. A finding
means the desk asserted something its own published record does not carry.
It does not by itself mean the figure is false.

Usage:
    python cite_audit.py battle_report_2026-07-27_1502.md
    python cite_audit.py kkr_packet_latest.md --json findings.json
    python cite_audit.py report.md --strict     # exit 1 on any MISCITED
"""
import argparse, json, re, sys, unicodedata
from pathlib import Path

SNAP_ROW   = re.compile(r"^\|\s*([A-Za-z0-9&/ ]+?)\s*\|\s*\$?([\d,]+\.?\d*)\s*\|\s*([+-]?[\d.]+)%\s*\|", re.M)
DATEISH    = re.compile(r"\b(?:19|20)\d{2}\b|\b\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\b|\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}\b|\b20\d{2}-\d{2}-\d{2}\b", re.I)
THRESHOLD  = re.compile(r"\b(below|above|under|over|exceed(?:s|ing)?|beyond|at least|more than|less than)\s*\$?\d", re.I)
# Identifiers are not claims. NUM_RE's plain branch matches any bare integer of
# two or more digits, and DATEISH strips the 2026 out of CVE-2026-53921, leaving
# a five-digit serial to be flagged as an unsupported figure. Same for the 00 in
# "15:00 UTC". Scrubbed before extraction, exactly as dates already are. Kept
# deliberately narrow: only the two patterns actually observed misfiring, so
# this cannot quietly swallow a real figure. ORDER MATTERS: IDENT_RE must run
# BEFORE DATEISH, because DATEISH strips the 2026 out of CVE-2026-53921 and
# destroys the pattern IDENT_RE is looking for.
IDENT_RE   = re.compile(r"\bCVE-\d{4}-\d+\b|\b\d{1,2}:\d{2}\b", re.I)
# "the next 48 hours" is not a claim about anything. This lived inline in the
# figure loop and was missing from the snapshot loop, so in one run 48 was
# excluded from one check and flagged by the other. One rule, one place.
WINDOW_BOILERPLATE = {"20", "24", "48", "72"}
WATCHLINE  = re.compile(r"^\s*WATCH:", re.I)
FUTURE     = re.compile(r"\b(will|would|could|may|might|if|expect(?:ed)?|forecast|should|watch for|by the end of)\b", re.I)
COMPLETED_V= re.compile(r"\b(consumed|burned|killed|injured|displaced|destroyed|lost|gained|now|since|already|so far|to date|down|up|fell|rose|dropped|surged|reached|hit|exceeded|climbed|declined|topped|stands? at|totall?ing)\b", re.I)
ASSERTION  = re.compile(r"\b(show|shows|showed|is|are|was|were|reached|has|have|gap|dropp?(?:ed|ing)?|fell|rose|surged)\b", re.I)

SECTION_RE = re.compile(r"^##\s+([IVXL]+)\.\s+(.+?)\s*$", re.M)
RECORD_RE  = re.compile(r"^\*\*The record:?\*\*\s*$", re.M)
ITEM_RE    = re.compile(r"^\s*(\d+)\.\s+(.*)$")
CITE_RE    = re.compile(r"\[([0-9]+(?:\s*,\s*[0-9]+)*)\]")
DTG_RE     = re.compile(r"—\s*(\d{2})(\d{4})Z\s+([A-Z]{3})\s+(\d{2})")
ISO_RE     = re.compile(r"\b(20\d{2})-(\d{2})-(\d{2})\b")
DAYMON_RE  = re.compile(r"\b(\d{1,2})\s+(January|February|March|April|May|June|July|August|September|October|November|December)\b", re.I)
MONTHS = {m.lower(): i for i, m in enumerate(
    "January February March April May June July August September October November December".split(), 1)}

# figures worth checking. bare small integers are excluded - too noisy.
NUM_RE = re.compile(r"""
    (?P<pct>\d{1,3}(?:\.\d+)?\s*(?:percent|%|-point|\s?point))
  | (?P<money>\$\s?\d[\d,]*(?:\.\d+)?)
  | (?P<big>\b\d{1,3}(?:,\d{3})+\b)
  | (?P<dec>\b\d+\.\d+\b)
  | (?P<plain>\b\d{2,}\b)
""", re.X | re.I)

COMPLETED = re.compile(
    r"\b(has|have)\s+(reached|risen|fallen|dropped|surged|hit|exceeded|climbed|declined|topped)\b"
    r"|\b(reached|rose|fell|dropped|surged|hit|exceeded|climbed|declined|topped)\b", re.I)

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    return re.sub(r"\s+", " ", s).strip()

# --- full-title resolution (patch_ohrwurm_nav_and_cite) ----------------------
# Published record items are truncated to ten words for copyright reasons. The
# MODEL, however, is given the full headline in the packet. Checking figures
# against the truncated form flags supported claims as fabrications, which is
# the wrong question. Where a packet is present, resolve each item to its full
# title and check against that; otherwise fall back and say so.
PACKET_DIRS = ["forecasts", ".", "reports"]
_PKT_ITEM = re.compile(r"^\s*(\d+)\.\s+(.*?)(?:\s+·\s|$)", re.M)


def load_packet_titles(report_path):
    """Return {section_title: {n: full_title}} from the packet that PAIRS
    with this report, by filename stem - never by modification time.

    battle_report_2026-07-28_1502.md pairs with kkr_packet_2026-07-28_1502.md.
    The previous version accepted report_path and then ignored it, taking
    whichever packet was newest, so the finding count depended on clock
    skew and a mispaired packet would repoint every citation index onto a
    different numbered list without saying so.
    """
    rp = Path(report_path).resolve()
    base = rp.parent.parent
    stem, matched = rp.name, False
    for pre in ("battle_report_", "report_"):
        if stem.startswith(pre):
            stem, matched = stem[len(pre):], True
            break
    if not matched:
        print("  cite_audit: WARNING - %s carries no known report prefix, so no "
              "packet can be paired to it. Figures will be checked against the "
              "report's own record section, whose titles are truncated."
              % rp.name)
        return None, None
    want = "kkr_packet_" + stem
    pkt = None
    for d in PACKET_DIRS:
        cand = base / d / want
        if cand.exists():
            pkt = cand
            break
    if pkt is None:
        print("  cite_audit: WARNING - no %s found under %s. NOT falling back to "
              "the newest packet: pairing by modification time makes the finding "
              "count a function of clock skew, and citation indices resolve "
              "positionally, so the wrong packet silently repoints every index. "
              "Checking against the report's own record section instead."
              % (want, "/".join(PACKET_DIRS)))
        return None, None
    text = pkt.read_text(encoding="utf-8", errors="replace")
    out, cur = {}, None
    for line in text.splitlines():
        m = re.match(r"^##\s+[IVXL]+\.\s+(.+?)\s*$", line)
        if m:
            cur = norm(m.group(1))
            out.setdefault(cur, {})
            continue
        if cur:
            im = _PKT_ITEM.match(line)
            if im:
                t = re.sub(r"^[^A-Za-z0-9\[]*", "", im.group(2))
                t = re.sub(r"^\[[^\]]*\]\s*", "", t)
                out[cur][int(im.group(1))] = norm(t.strip("* "))
    return out, pkt.name
# ----------------------------------------------------------------------------

def digits(s):
    return re.sub(r"[^0-9.]", "", s)

def report_date(text):
    m = DTG_RE.search(text)
    if not m: return None
    day, _, mon, yy = m.groups()
    mm = {"JAN":1,"FEB":2,"MAR":3,"APR":4,"MAY":5,"JUN":6,
          "JUL":7,"AUG":8,"SEP":9,"OCT":10,"NOV":11,"DEC":12}.get(mon.upper())
    if not mm: return None
    return (2000 + int(yy), mm, int(day))

def parse_sections(text):
    """Return ordered sections, each with its prose span and its numbered record."""
    marks = [(m.start(), m.group(1), norm(m.group(2))) for m in SECTION_RE.finditer(text)]
    out = []
    for i, (pos, numeral, title) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        body = text[pos:end]
        rec_m = RECORD_RE.search(body)
        prose, items = body, {}
        if rec_m:
            prose = body[:rec_m.start()]
            for line in body[rec_m.end():].splitlines():
                im = ITEM_RE.match(line)
                if im: items[int(im.group(1))] = norm(im.group(2))
        out.append({"numeral": numeral, "title": title, "prose": prose, "items": items})
    return out

def sentences(prose):
    prose = re.sub(r"^\s*>.*$", "", prose, flags=re.M)          # drop existing audit banners
    prose = re.sub(r"^\s*\|.*$", "", prose, flags=re.M)         # drop tables
    prose = re.sub(r"\*\*(.+?)\*\*", r"\1", prose)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(\u201c\"])", prose)
    return [norm(p) for p in parts if len(norm(p)) > 30]

def resolve_scope(sections, idx):
    """KJ / I&W / OUTLOOK cite the Top Signals list, which lives in section I."""
    sec = sections[idx]
    if sec["items"]:
        return sec["items"], sec["title"]
    for s in sections:
        if s["items"] and "KEY JUDGMENT" in s["title"].upper():
            return s["items"], s["title"]
    # Top Signals block is inside KEY JUDGMENTS in this template
    for s in sections:
        if "KEY JUDGMENT" in s["title"].upper():
            top = {}
            for line in s["prose"].splitlines():
                im = ITEM_RE.match(line)
                if im: top[int(im.group(1))] = norm(im.group(2))
            if top: return top, s["title"] + " / Top signals"
    return {}, sec["title"]

def audit(path, verbose=False):
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    rdate = report_date(text)
    sections = parse_sections(text)
    pkt_titles, pkt_name = load_packet_titles(path)
    title_src = f"full titles from {pkt_name}" if pkt_titles else "printed record (truncated)"
    findings, checked = [], 0

    for i, sec in enumerate(sections):
        items, scope = resolve_scope(sections, i)
        if not items: continue
        for sent in sentences(sec["prose"]):
            cites = []
            for cm in CITE_RE.finditer(sent):
                cites += [int(n) for n in re.split(r"\s*,\s*", cm.group(1))]
            if not cites: continue
            checked += 1

            missing = [c for c in cites if c not in items]
            if missing:
                findings.append({"kind":"UNRESOLVED","section":sec["title"],"scope":scope,
                                 "cites":cites,"detail":f"no item {missing} in this record",
                                 "sentence":sent[:220]})

            # Prefer the packet's untruncated title for the same item number.
            def _full(c):
                if pkt_titles:
                    for k, v in pkt_titles.items():
                        if k.upper().startswith(scope.split(" /")[0].upper()[:8]) and c in v:
                            return v[c] + " " + items.get(c, "")
                return items.get(c, "")
            pool = " ".join(_full(c) for c in cites if c in items)
            pool_d = {digits(x) for x in NUM_RE.findall(pool) for x in ([x] if isinstance(x,str) else x) if digits(x)}
            pool_d |= {digits(m.group(0)) for m in NUM_RE.finditer(pool)}

            raw_body = CITE_RE.sub("", sent)
            body = DATEISH.sub(" ", IDENT_RE.sub(" ", raw_body))
            for m in NUM_RE.finditer(body):
                tok = m.group(0)
                d = digits(tok)
                if not d or d in WINDOW_BOILERPLATE: continue
                if d in pool_d: continue
                if any(d in p for p in pool_d): continue
                window = body[max(0,m.start()-40):m.end()+10]
                if WATCHLINE.search(sent):
                    kind = "THRESHOLD"
                elif (THRESHOLD.search(window) and FUTURE.search(sent)
                      and not COMPLETED_V.search(window) and not ASSERTION.search(window)):
                    kind = "THRESHOLD"
                else:
                    kind = "MISCITED"
                findings.append({"kind":kind,"section":sec["title"],"scope":scope,
                                 "cites":cites,"detail":f"figure {tok.strip()} absent from cited item(s)",
                                 "sentence":sent[:220]})

            if rdate and COMPLETED.search(raw_body):
                for dm in ISO_RE.finditer(raw_body):
                    if tuple(int(x) for x in dm.groups()) > rdate:
                        findings.append({"kind":"FORWARD","section":sec["title"],"scope":scope,
                                         "cites":cites,"detail":f"completed tense about {dm.group(0)}, after report date",
                                         "sentence":sent[:220]})
                for dm in DAYMON_RE.finditer(raw_body):
                    d_, mon = int(dm.group(1)), MONTHS[dm.group(2).lower()]
                    if (rdate[0], mon, d_) > rdate:
                        findings.append({"kind":"FORWARD","section":sec["title"],"scope":scope,
                                         "cites":cites,"detail":f"completed tense about {dm.group(0)}, after report date",
                                         "sentence":sent[:220]})
    snap = {norm(m.group(1)).lower(): (m.group(2).replace(",",""), m.group(3)) for m in SNAP_ROW.finditer(text)}
    if snap:
        for sec in sections:
            for sent in sentences(sec["prose"]):
                low = sent.lower()
                for inst,(last,chg) in snap.items():
                    if not re.search(r"\b"+re.escape(inst)+r"\b", low): continue
                    for m in NUM_RE.finditer(
                            DATEISH.sub(" ", IDENT_RE.sub(" ", CITE_RE.sub("", sent)))):
                        d = digits(m.group(0))
                        if not d or d in WINDOW_BOILERPLATE: continue
                        try: v = float(d)
                        except ValueError: continue
                        ref_last, ref_chg = float(last), abs(float(chg))
                        near_price  = abs(v - ref_last) / max(ref_last,1) < 0.06
                        near_change = abs(v - ref_chg) < 1.0
                        if 1 < v < 500 and not near_price and not near_change and v < ref_last*1.5:
                            findings.append({"kind":"SNAPSHOT","section":sec["title"],"scope":"MARKET SNAPSHOT",
                                             "cites":[],"detail":f"{inst} stated as {m.group(0).strip()} but the report's governing snapshot says {last} ({chg}%)",
                                             "sentence":sent[:220]})
                            break

    return {"file": str(path), "title_source": title_src,
            "report_date": "-".join(f"{x:02d}" for x in rdate) if rdate else None,
            "cited_sentences_checked": checked,
            "findings": findings}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("report")
    ap.add_argument("--json", metavar="OUT")
    ap.add_argument("--strict", action="store_true", help="exit 1 if any MISCITED found")
    a = ap.parse_args()

    r = audit(a.report)
    counts = {}
    for f in r["findings"]: counts[f["kind"]] = counts.get(f["kind"], 0) + 1
    print(f"cite_audit · {r['file']} · report {r['report_date']} · "
          f"{r['cited_sentences_checked']} cited sentences checked")
    print(f"           · checked against: {r.get('title_source','?')}")
    print("           · " + (", ".join(f"{k} {v}" for k, v in sorted(counts.items())) or "clean"))
    for f in r["findings"]:
        print(f"\n  [{f['kind']}] {f['section']}  cites {f['cites']}  (scope: {f['scope']})")
        print(f"      {f['detail']}")
        print(f"      \"{f['sentence']}\"")
    if a.json:
        Path(a.json).write_text(json.dumps(r, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"\nwrote {a.json}")
    if a.strict and counts.get("MISCITED"): sys.exit(1)

if __name__ == "__main__":
    main()
