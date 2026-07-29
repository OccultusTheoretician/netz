#!/usr/bin/env python3
"""
kfk_walk.py - propose NEW ForeKaster records from a Wikidata subordinate tree.

WHY THIS AND NOT MORE SCRAPING

wd_probe established that XVIII Airborne Corps carries twelve P355 subordinate
claims - the whole order of battle in one call, with type and garrison
attached. ForeKaster holds four of them. The other eight are not enrichment of
existing records: they are formations the file does not have, with a parent
relation already established.

Scraping each child page for its parent was the long way round. Walking down
from the parent is one request.

WHAT IT PROPOSES, AND AT WHAT GRADE

For each subordinate absent from the file:

  existence   REPORTED. A Wikidata claim is typed and may carry a reference,
              which beats an infobox string - but it is a secondary source and
              grades no higher without reading the reference. Never DOCUMENTED
              from this path.
  parent      the walked formation's ForeKaster id, graded REPORTED, sourced
              to the P355 claim
  location    from P159 headquarters, REPORTED, only where the claim exists
  echelon     mapped from P31 by substring against the file's vocabulary, and
              left as "unit" where no map applies rather than guessed
  commander   NEVER. Wikidata does not carry one for these items, and the
              infobox path is a separate source with its own grade.

WHAT IT REFUSES

  - an entity whose label equals its own QID. Q11922588 exists as "a military
    organization in Sudan" with no English label, and a pull that recorded it
    would create a formation named Q11922588.
  - a subordinate already in the file under any name or designation.
  - a proposed id that collides with an existing one; it falls back to
    F-WD-<qid>, which is ugly and traceable, and traceable wins.

IT WRITES A PROPOSAL FILE AND NEVER TOUCHES KriegForeKaster.json.

    python kfk_walk.py --qid Q582971 --parent-id F-XVIII
    python kfk_walk.py --qid Q582971 --parent-id F-XVIII --json
    python kfk_walk.py --apply kfk_walk_YYYY-MM-DD.json --dry-run
    python kfk_walk.py --apply kfk_walk_YYYY-MM-DD.json

Keyless. Standard library only. ASCII-only output.
"""

import argparse
import datetime as dt
import json
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

SRC = Path("KriegForeKaster.json")
UA = "kfk_walk/1.0 (+https://retroprescientaudit.com) python-urllib"
TIMEOUT = 60
SPARQL = "https://query.wikidata.org/sparql"

TREE = """
SELECT ?child ?childLabel ?typeLabel ?hqLabel ?countryLabel
WHERE {
  wd:%(qid)s wdt:P355 ?child .
  OPTIONAL { ?child wdt:P31 ?type . }
  OPTIONAL { ?child wdt:P159 ?hq . }
  OPTIONAL { ?child wdt:P17 ?country . }
  FILTER NOT EXISTS { ?child wdt:P576 ?d . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
LIMIT 200
"""

# P31 label substring -> the file's echelon vocabulary. Unmapped stays "unit"
# rather than being guessed at.
ECHELON = [
    ("corps", "corps"), ("division", "division"), ("brigade", "brigade"),
    ("regiment", "regiment"), ("battalion", "battalion"),
    ("sustainment command", "command"), ("command", "command"),
    ("army", "army"), ("fleet", "fleet"), ("wing", "wing"),
    ("armed forces", "national"), ("military branch", "branch"),
]


def run(q):
    url = SPARQL + "?format=json&query=" + urllib.parse.quote(q)
    req = urllib.request.Request(url, headers={
        "User-Agent": UA, "Accept": "application/sparql-results+json"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT,
                                    context=ssl.create_default_context()) as r:
            return json.loads(r.read().decode("utf-8", errors="replace")) \
                .get("results", {}).get("bindings", [])
    except urllib.error.HTTPError as ex:
        print("QUERY FAILED - HTTP %s %s" % (ex.code, ex.reason), file=sys.stderr)
        return None
    except Exception as ex:
        print("QUERY FAILED - %s: %s" % (type(ex).__name__, ex), file=sys.stderr)
        return None


def val(row, k):
    v = (row.get(k) or {}).get("value", "")
    return v.rsplit("/", 1)[-1] if v.startswith("http://www.wikidata.org/") else v


def norm(s):
    return re.sub(r"[^a-z0-9]", "", str(s or "").lower())


def echelon_for(type_label):
    t = str(type_label or "").lower()
    for key, ech in ECHELON:
        if key in t:
            return ech
    return "unit"


def derive_id(label, taken, qid):
    """A readable id where one can be derived, F-WD-<qid> where it collides."""
    m = re.match(r"^(\d+)(?:st|nd|rd|th)?\s+(.*)$", str(label))
    if m:
        num = m.group(1)
        words = re.findall(r"[A-Z]", m.group(2).title())
        cand = "F-%s%s" % (num, "".join(words[:3]))
    else:
        words = re.findall(r"[A-Z]", str(label).title())
        cand = "F-%s" % "".join(words[:5])
    cand = re.sub(r"[^A-Z0-9\-]", "", cand.upper())
    if len(cand) > 3 and cand not in taken:
        return cand
    return "F-WD-%s" % qid


def load():
    if not SRC.exists():
        print("FAIL - KriegForeKaster.json not found. Run from C:\\netz.",
              file=sys.stderr)
        return None
    return json.loads(SRC.read_text(encoding="utf-8"))


def cmd_walk(a):
    d = load()
    if d is None:
        return 1
    f = d.get("formations", [])
    known = {}
    for r in f:
        for key in (r.get("name"), r.get("designation")):
            if norm(key):
                known[norm(key)] = r.get("id")
    taken = {r.get("id") for r in f}
    parent = next((r for r in f if r.get("id") == a.parent_id), None)
    if not parent:
        print("FAIL - no formation with id %s in the file. The parent must "
              "exist before subordinates are attached to it." % a.parent_id,
              file=sys.stderr)
        return 1

    rows = run(TREE % {"qid": a.qid})
    if rows is None:
        return 1

    today = dt.date.today().isoformat()
    wd_url = "https://www.wikidata.org/wiki/%s" % a.qid
    have, new, refused = [], [], []
    seen = set()

    for r in rows:
        cq = val(r, "child")
        if cq in seen:
            continue
        seen.add(cq)
        label = val(r, "childLabel")
        if not label or label == cq:
            refused.append((cq, "no English label - would create a formation "
                                "named after its own QID"))
            continue
        n = norm(label)
        # A parenthetical qualifier breaks exact matching: the file holds
        # 10th Mountain Division (Light Infantry) where Wikidata has the
        # bare name. Without this the walk proposes a duplicate of a unit
        # already present, under the same parent.
        if n not in known:
            for k in known:
                if len(k) > 8 and (k.startswith(n) or n.startswith(k)):
                    n = k
                    break
        if n in known:
            have.append((cq, label, known[n]))
            continue
        fid = derive_id(label, taken, cq)
        taken.add(fid)
        rec = {
            "id": fid,
            "faction": parent.get("faction"),
            "echelon": echelon_for(val(r, "typeLabel")),
            "parent": {"id": a.parent_id, "grade": "REPORTED", "as_of": today,
                       "sources": [wd_url],
                       "note": ("Wikidata P355 subordinate claim on %s. "
                                "Secondary source." % a.qid)},
            "name": label,
            "designation": label,
            "existence": {"grade": "REPORTED", "as_of": today,
                          "sources": ["https://www.wikidata.org/wiki/%s" % cq],
                          "note": ("Wikidata item %s, typed %s, recorded as a "
                                   "subordinate of %s. A secondary source: it "
                                   "establishes that the formation is "
                                   "described, not its composition or posture."
                                   % (cq, val(r, "typeLabel") or "unclassified",
                                      a.qid))},
            "location": ({"place": val(r, "hqLabel"), "grade": "REPORTED",
                          "as_of": today,
                          "sources": ["https://www.wikidata.org/wiki/%s" % cq],
                          "note": "Wikidata P159 headquarters location."}
                         if val(r, "hqLabel") else None),
            "projections": [],
            "notes": "Proposed by kfk_walk from a Wikidata subordinate tree.",
            "wikidata": cq,
        }
        if rec["location"] is None:
            del rec["location"]
        new.append(rec)

    print("")
    print("SUBORDINATE WALK - %s under %s" % (a.qid, a.parent_id))
    print("=" * 72)
    print("  parent in file: %s" % parent.get("name"))
    print("  %d subordinate claim(s) returned" % len(seen))
    print("")
    if have:
        print("  ALREADY IN THE FILE (%d)" % len(have))
        for cq, label, fid in have:
            print("    %-11s %-40s -> %s" % (cq, label[:40], fid))
        print("")
    if refused:
        print("  REFUSED (%d)" % len(refused))
        for cq, why in refused:
            print("    %-11s %s" % (cq, why))
        print("")
    if not new:
        print("  Nothing new to propose. That is a finding, not a failure.")
        return 0
    print("  PROPOSED AS NEW RECORDS (%d)" % len(new))
    print("  %-12s %-38s %-11s %s" % ("id", "name", "echelon", "location"))
    for rec in new:
        print("  %-12s %-38s %-11s %s"
              % (rec["id"], rec["name"][:38], rec["echelon"],
                 (rec.get("location") or {}).get("place", "")[:20]))
    if a.json:
        print("")
        print(json.dumps(new, indent=2, ensure_ascii=False))

    out = Path("kfk_walk_%s.json" % today)
    out.write_text(json.dumps(
        {"generated": today, "tool": "kfk_walk/1.0", "source": "wikidata",
         "walked": a.qid, "parent_id": a.parent_id,
         "already_present": len(have), "refused": len(refused),
         "new": new}, indent=2, ensure_ascii=False), encoding="utf-8")
    print("")
    print("  written -> %s" % out.name)
    print("")
    print("  Every new record carries existence REPORTED and no commander.")
    print("  Wikidata does not hold one for these items; the infobox path is a")
    print("  separate source with its own grade, run separately.")
    print("")
    print("  NOTHING APPLIED. Read it, delete what you do not accept, then:")
    print("    python kfk_walk.py --apply %s --dry-run" % out.name)
    return 0


def cmd_apply(a):
    p = Path(a.apply)
    if not p.exists():
        print("FAIL - not found: %s" % p, file=sys.stderr)
        return 1
    pr = json.loads(p.read_text(encoding="utf-8"))
    if pr.get("tool") != "kfk_walk/1.0":
        print("REFUSED - proposal file written by %s, not kfk_walk/1.0."
              % pr.get("tool", "an unknown tool"), file=sys.stderr)
        return 1
    d = load()
    if d is None:
        return 1
    existing = {r.get("id") for r in d.get("formations", [])}
    add, skip = [], 0
    for rec in pr.get("new", []):
        if rec.get("id") in existing:
            skip += 1
            continue
        add.append(rec)
    print("")
    print("  %d new record(s) %s, %d skipped as already present"
          % (len(add), "would be added" if a.dry_run else "added", skip))
    for rec in add:
        print("    %-12s %s" % (rec["id"], rec["name"][:48]))
    if a.dry_run:
        print("")
        print("  DRY RUN - KriegForeKaster.json untouched.")
        return 0
    SRC.with_name(SRC.name + ".prewalk").write_text(
        SRC.read_text(encoding="utf-8"), encoding="utf-8")
    d["formations"].extend(add)
    d["as_of"] = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    SRC.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")
    print("")
    print("  WRITTEN. Backup: %s.prewalk" % SRC.name)
    print("  Now: python kfk_state.py ; python build_okk.py")
    print("  Then sync docs/KriegForeKaster.json or desk verify will fail the")
    print("  mirror, which is the invariant doing its job.")
    return 0


def main():
    ap = argparse.ArgumentParser(
        description="propose new ForeKaster records from a Wikidata tree")
    ap.add_argument("--qid", help="parent formation QID, e.g. Q582971")
    ap.add_argument("--parent-id", help="that formation's id in the file")
    ap.add_argument("--apply")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.apply:
        return cmd_apply(a)
    if a.qid and a.parent_id:
        return cmd_walk(a)
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
