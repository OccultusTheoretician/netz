#!/usr/bin/env python3
"""
kfk_enrich.py - propose graded blocks for ForeKaster. v3.

WHAT v2 GOT WRONG, AND IT REACHED A PROPOSAL FILE

Running --batch against San Marino produced this:

    "name": "&lt;ref name=\\"Carattoni\\"/>",
    "grade": "DOCUMENTED"

A citation tag captured as a commander's name and graded DOCUMENTED because a
cia.gov link sat nearby. unwiki() stripped <tags> BEFORE unescaping entities,
so escaped markup survived as text and no check asked whether the result
looked like a person.

A confident, sourced, well-formatted lie, produced by the tool built to stop
exactly that. Three fixes:

  1. ENTITY ORDER. Unescape &lt; and &gt; first, then strip tags. Escaped
     markup no longer survives the pass.
  2. A NAME GATE. clean_name() rejects anything containing markup residue,
     lacking two consecutive letters, shorter than four characters or longer
     than eighty, or matching a known citation pattern. A rejected value is
     reported as REJECTED with the reason, never proposed.
  3. FIRST VALUE ONLY. Infobox commander fields often carry several entries
     separated by line breaks. v2 concatenated them. v3 takes the first and
     says how many it discarded.

NEW IN v3: PARENT RESOLUTION

v2 emitted parent_hint - a NAME, unusable because the file keys parent by id.
v3 matches that name against every formation's name and designation and, where
exactly one matches, emits a real parent block carrying the id. Where zero or
several match it says so and emits nothing. That is what turns the 82nd
Airborne's infobox line "command_structure: XVIII Airborne Corps" into a
usable link to F-XVIII.

THE STANDING RULE

A commander claim on a SPECULATIVE existence claim asserts who commands
something the file has not established exists. Batch mode proposes the
existence upgrade and the commander together from the same source, or neither.

GRADING: DOCUMENTED only where a .mil or .gov citation sits near the claim.
Otherwise REPORTED. Never higher. A wiki infobox is a secondary source.

IT WRITES A PROPOSAL FILE. IT NEVER TOUCHES KriegForeKaster.json.

    python kfk_enrich.py --page "82nd Airborne Division"
    python kfk_enrich.py --batch --limit 15
    python kfk_enrich.py --batch
    python kfk_enrich.py --parents-only          resolve command structure only
    python kfk_enrich.py --apply kfk_proposals_YYYY-MM-DD.json --dry-run

Standard library only. ASCII-only output.
"""

import argparse
import datetime as dt
import html as _html
import json
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

SRC = Path("KriegForeKaster.json")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) kfk_enrich/3.0 "
      "(+https://retroprescientaudit.com)")
TIMEOUT = 30
WIKI_HTML = "https://en.wikipedia.org/api/rest_v1/page/html/%s"
WIKI_SEARCH = ("https://en.wikipedia.org/w/api.php?action=opensearch&format=json"
               "&limit=3&search=%s")

CMD_KEYS = ["current_commander", "commander", "commander1", "chief",
            "chief_of_staff", "commander_in_chief"]
PARENT_KEYS = ["command_structure", "part_of", "parent"]

PRIMARY = re.compile(r"https?://[^\s\"']*\.(?:mil|gov)(?:/|\"|'|\s|$)"
                     r"|https?://[^\s\"']*\.gov\.[a-z]{2}"
                     r"|https?://[^\s\"']*\.gouv\.[a-z]{2}", re.I)

# residue that means the extractor caught markup rather than a name
JUNK = re.compile(r"(?:<|&lt;|&gt;|\bref\s+name\b|\{\{|\}\}|\[\[|\]\]"
                  r"|^\s*ref\b|citation needed|/>)", re.I)


def fetch(url, quiet=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT,
                                    context=ssl.create_default_context()) as r:
            return r.read().decode("utf-8", errors="replace")
    except Exception as ex:
        if not quiet:
            print("  fetch failed: %s" % type(ex).__name__, file=sys.stderr)
        return None


def unwiki(v):
    """FIX 1 - unescape entities BEFORE stripping tags, so escaped markup
    such as &lt;ref name="X"/&gt; cannot survive as text."""
    v = _html.unescape(v)
    v = re.sub(r"(?s)<[^>]*>", " ", v)          # now catches the unescaped form
    v = re.sub(r"\[\[([^\]|]*\|)?([^\]]*)\]\]", r"\2", v)
    v = re.sub(r"(?s)\{\{[^{}]*\}\}", " ", v)
    return re.sub(r"\s+", " ", v).strip(" ,;|")


def clean_name(raw):
    """FIX 2 and 3 - take the first value, then gate it. Returns
    (name, discarded_count) or (None, reason)."""
    if not raw:
        return None, "empty"
    # Unescape BEFORE splitting. Splitting first breaks entities at their own
    # semicolon: "&lt;ref/&gt;" became "&lt", which the gate rejected for the
    # wrong reason, and "Jos&eacute; Rodriguez" would have become "Jos&eacute"
    # and passed as a name.
    raw = _html.unescape(raw)
    # A value whose markup contains a citation is a value where the extractor
    # caught the footnote, not the field. Stripping the tags and keeping what
    # is inside yields the citation BODY as a name - "&lt;ref&gt;junk&lt;/ref&gt;"
    # became "junk". Reject the whole value instead of salvaging it.
    if re.search(r"<\s*ref\b|</\s*ref\s*>", raw, re.I):
        return None, "value contains a citation tag"
    parts = [x for x in re.split(r"(?:<br\s*/?>|\n|\u2022)", raw) if x.strip()]
    first = unwiki(parts[0]) if parts else ""
    extra = max(0, len(parts) - 1)
    if not first:
        return None, "nothing left after cleaning"
    if JUNK.search(first):
        return None, "markup residue: %s" % first[:40]
    if not re.search(r"[A-Za-z]{2}", first):
        return None, "no letters: %s" % first[:40]
    if len(first) < 4:
        return None, "too short: %s" % first
    if len(first) > 80:
        return None, "too long (%d chars)" % len(first)
    if re.match(r"^(?:see|list|various|unknown|n/?a|vacant)\b", first, re.I):
        return None, "placeholder: %s" % first[:40]
    return first, extra


def infobox_raw(html, keys):
    out = {}
    for k in keys:
        m = re.search(r'"%s"\s*:\s*\{\s*"wt"\s*:\s*"((?:[^"\\]|\\.)*)"' % k, html)
        if m:
            out[k] = m.group(1).encode().decode("unicode_escape",
                                                errors="replace")
    return out


def grade_for(html, value):
    if not value:
        return None, []
    tok = value.split()[-1] if value.split() else ""
    i = html.find(tok) if tok else -1
    window = html[max(0, i - 4000): i + 4000] if i >= 0 else html[:20000]
    hits = []
    for m in PRIMARY.finditer(window):
        u = m.group(0).rstrip("\"' ")
        if u not in hits:
            hits.append(u)
        if len(hits) >= 2:
            break
    return ("DOCUMENTED" if hits else "REPORTED"), hits


def norm(s):
    return re.sub(r"[^a-z0-9]", "", str(s or "").lower())


def build_index(f):
    """name and designation -> id, for parent resolution."""
    idx = {}
    for r in f:
        for key in (r.get("name"), r.get("designation")):
            n = norm(key)
            if n:
                idx.setdefault(n, set()).add(r.get("id"))
    return idx


def resolve_parent(value, idx, self_id):
    """NEW IN v3 - a name only becomes a parent block if exactly one
    formation matches it. Ambiguity emits nothing."""
    n = norm(value)
    if not n:
        return None, "empty"
    hits = {i for i in idx.get(n, set()) if i != self_id}
    if not hits:
        for k, v in idx.items():
            if len(k) > 6 and (k in n or n in k):
                hits |= {i for i in v if i != self_id}
    if not hits:
        return None, "no formation in the file matches '%s'" % value[:44]
    if len(hits) > 1:
        return None, "%d formations match '%s' - ambiguous" % (len(hits),
                                                               value[:34])
    return sorted(hits)[0], None


def candidates(rec):
    nm = str(rec.get("name", "")).strip()
    out = [nm]
    m = re.match(r"^(.*?)\s*[\u2014\-]\s*national armed forces$", nm, re.I)
    if m:
        c = m.group(1).strip()
        out += ["Armed Forces of %s" % c, "%s Armed Forces" % c,
                "Military of %s" % c]
    des = str(rec.get("designation", "")).strip()
    if des and des != nm:
        out.append(des)
    seen, uniq = set(), []
    for t in out:
        if t and t.lower() not in seen:
            seen.add(t.lower())
            uniq.append(t)
    return uniq


def extract(title):
    html = fetch(WIKI_HTML % urllib.parse.quote(title.replace(" ", "_")), True)
    if html and len(html) > 2000:
        return title, html
    j = fetch(WIKI_SEARCH % urllib.parse.quote(title), True)
    if j:
        try:
            d = json.loads(j)
            alt = d[1][0] if len(d) > 1 and d[1] else None
        except Exception:
            alt = None
        if alt and alt.lower() != title.lower():
            html = fetch(WIKI_HTML % urllib.parse.quote(alt.replace(" ", "_")),
                         True)
            if html and len(html) > 2000:
                return alt, html
    return None, None


def build_blocks(rec, resolved, html, today, idx, log):
    cmdraw = infobox_raw(html, CMD_KEYS)
    parraw = infobox_raw(html, PARENT_KEYS)
    url = WIKI_HTML % urllib.parse.quote(resolved.replace(" ", "_"))
    blocks = {}

    for k in CMD_KEYS:
        if k not in cmdraw:
            continue
        name, extra = clean_name(cmdraw[k])
        if not name:
            log.append("commander rejected (%s): %s" % (k, extra))
            continue
        g, srcs = grade_for(html, name)
        note = "English Wikipedia infobox field %s. Secondary source, graded %s." % (k, g)
        if extra:
            note += " %d further value(s) in the field were discarded." % extra
        blocks["commander"] = {"name": name, "grade": g, "as_of": today,
                               "sources": ([url] + srcs)[:3], "note": note}
        break

    for k in PARENT_KEYS:
        if k not in parraw:
            continue
        val, _ = clean_name(parraw[k])
        if not val:
            continue
        pidv, why = resolve_parent(val, idx, rec.get("id"))
        if not pidv:
            log.append("parent unresolved (%s): %s" % (k, why))
            continue
        g, srcs = grade_for(html, val)
        blocks["parent"] = {
            "id": pidv, "value": val, "grade": g, "as_of": today,
            "sources": ([url] + srcs)[:3],
            "note": ("Infobox field %s, resolved to formation %s by exact or "
                     "unique name match against this file." % (k, pidv))}
        break

    ex = rec.get("existence") or {}
    if blocks and ex.get("grade") == "SPECULATIVE":
        g, srcs = grade_for(html, resolved)
        blocks["existence"] = {
            "grade": g, "as_of": today, "sources": ([url] + srcs)[:3],
            "note": ("Upgraded from SPECULATIVE. An English Wikipedia article "
                     "with a military infobox exists for this formation. A "
                     "secondary source: it establishes that the formation is "
                     "described, not that its composition or posture is known.")}
    return blocks


def cmd_batch(d, a):
    f = d.get("formations", [])
    idx = build_index(f)
    if a.parents_only:
        todo = [r for r in f if not r.get("parent")]
        what = "without a parent link"
    else:
        todo = [r for r in f if not r.get("commander")]
        what = "without a commander claim"
    if a.limit:
        todo = todo[:a.limit]
    today = dt.date.today().isoformat()
    delay = a.delay if a.delay is not None else 1.0

    print("")
    print("BATCH ENRICHMENT - PROPOSAL ONLY")
    print("=" * 72)
    print("  %d formation(s) %s; processing %d at %.1fs apart"
          % (len(todo), what, len(todo), delay))
    print("")

    props, misses, rejects = {}, [], []
    for i, rec in enumerate(todo, 1):
        fid = rec.get("id")
        got = None
        for cand in candidates(rec):
            t, h = extract(cand)
            if h:
                got = (t, h)
                break
            time.sleep(delay / 2)
        if not got:
            misses.append((fid, rec.get("name"), "no page"))
            print("  %3d/%d  MISS      %s" % (i, len(todo),
                                              str(rec.get("name"))[:44]))
            time.sleep(delay)
            continue
        title, html = got
        log = []
        blocks = build_blocks(rec, title, html, today, idx, log)
        if a.parents_only:
            blocks = {k: v for k, v in blocks.items() if k == "parent"}
        if not blocks:
            misses.append((fid, rec.get("name"), "; ".join(log) or "no fields"))
            print("  %3d/%d  NONE      %-30s %s"
                  % (i, len(todo), str(rec.get("name"))[:30],
                     (log[0] if log else "no usable field")[:34]))
        else:
            props[fid] = {"name": rec.get("name"), "resolved_title": title,
                          "blocks": blocks, "log": log}
            print("  %3d/%d  PROPOSE   %-30s %s"
                  % (i, len(todo), str(rec.get("name"))[:30],
                     "+".join(sorted(blocks))))
        for msg in log:
            rejects.append((fid, msg))
        time.sleep(delay)

    out = Path("kfk_proposals_%s.json" % today)
    out.write_text(json.dumps(
        {"generated": today, "tool": "kfk_enrich/3.0", "source": "en.wikipedia.org",
         "processed": len(todo), "proposed": len(props), "missed": len(misses),
         "rejected_values": [{"id": i, "reason": m} for i, m in rejects],
         "proposals": props,
         "misses": [{"id": i, "name": n, "why": w} for i, n, w in misses]},
        indent=2, ensure_ascii=False), encoding="utf-8")

    print("")
    print("  %d proposal(s), %d without usable fields, %d value(s) rejected"
          % (len(props), len(misses), len(rejects)))
    print("  written -> %s" % out.name)
    print("")
    print("  Rejected values are logged with the reason, not silently dropped.")
    print("  NOTHING APPLIED. Read it, delete what you do not accept, then:")
    print("    python kfk_enrich.py --apply %s --dry-run" % out.name)
    return 0


def cmd_apply(a):
    p = Path(a.apply)
    if not p.exists():
        print("FAIL - not found: %s" % p, file=sys.stderr)
        return 1
    pr = json.loads(p.read_text(encoding="utf-8"))
    if pr.get("tool") != "kfk_enrich/3.0":
        print("REFUSED - this proposal file was written by %s. v2 and earlier "
              "captured markup as commander names. Regenerate with v3."
              % pr.get("tool", "an unknown version"), file=sys.stderr)
        return 1
    d = json.loads(SRC.read_text(encoding="utf-8"))
    byid = {r.get("id"): r for r in d.get("formations", [])}
    applied = skipped = 0
    for fid, entry in pr.get("proposals", {}).items():
        rec = byid.get(fid)
        if not rec:
            skipped += 1
            continue
        for name, blk in entry["blocks"].items():
            if rec.get(name) and name != "existence":
                skipped += 1
                continue
            if not a.dry_run:
                rec[name] = blk
            applied += 1
            if a.verbose:
                print("  %s  %s" % (fid, name))
    print("")
    print("  %d block(s) %s, %d skipped"
          % (applied, "would be applied" if a.dry_run else "applied", skipped))
    if a.dry_run:
        print("  DRY RUN - KriegForeKaster.json untouched.")
        return 0
    SRC.with_name(SRC.name + ".preenrich").write_text(
        SRC.read_text(encoding="utf-8"), encoding="utf-8")
    d["as_of"] = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    SRC.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")
    print("  WRITTEN. Backup: %s.preenrich" % SRC.name)
    print("  Now: python kfk_state.py ; python build_okk.py ; python desk.py verify")
    print("  The KriegForeKaster.json mirror will need a sync before shipping.")
    return 0


def cmd_one(d, page, fid, as_json):
    f = d.get("formations", [])
    idx = build_index(f)
    rec = None
    for r in f:
        if (fid and r.get("id") == fid) or \
           (page and str(r.get("name", "")).lower() == str(page).lower()):
            rec = r
            break
    title = page or (rec.get("name") if rec else None)
    if not title:
        print("FAIL - no --page and --id matched nothing.", file=sys.stderr)
        return 1
    resolved, html = extract(title)
    if not html:
        print("NO PAGE FOUND for %s. That is a finding." % title)
        return 0
    log = []
    blocks = build_blocks(rec or {}, resolved, html, dt.date.today().isoformat(),
                          idx, log)
    print("")
    print("PROPOSAL - %s" % title)
    print("=" * 68)
    print("  resolved : %s" % resolved)
    if rec:
        print("  in file  : %s . existence %s . commander %s . parent %s"
              % (rec.get("id"), (rec.get("existence") or {}).get("grade"),
                 (rec.get("commander") or {}).get("grade", "ABSENT"),
                 "set" if rec.get("parent") else "EMPTY"))
    for m in log:
        print("  REJECTED : %s" % m)
    print("")
    if not blocks:
        print("  NOTHING PROPOSED. A blank result is a finding, not a licence")
        print("  to write anything.")
        return 0
    if as_json:
        print(json.dumps(blocks, indent=2))
    else:
        for n, b in blocks.items():
            print("  %s:" % n)
            for k, v in b.items():
                print("    %-9s %s" % (k + ":",
                                       "; ".join(v) if isinstance(v, list) else v))
            print("")
    return 0


def main():
    ap = argparse.ArgumentParser(description="ForeKaster enrichment proposals")
    ap.add_argument("--page")
    ap.add_argument("--id")
    ap.add_argument("--batch", action="store_true")
    ap.add_argument("--parents-only", action="store_true")
    ap.add_argument("--apply")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--delay", type=float)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args()

    if a.apply:
        return cmd_apply(a)
    if not SRC.exists():
        print("FAIL - KriegForeKaster.json not found. Run from C:\\netz.",
              file=sys.stderr)
        return 1
    d = json.loads(SRC.read_text(encoding="utf-8"))
    if a.batch or a.parents_only:
        return cmd_batch(d, a)
    if a.page or a.id:
        return cmd_one(d, a.page, a.id, a.json)
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
