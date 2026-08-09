#!/usr/bin/env python3
"""spine_stamp.py - THE SPINE DECLARES ITS REAL AGE, NOT ITS FILE DATE.

docs/kfk_spine.json was flagged stale in the 2026-08-09 site audit on the
strength of generated_at: 2026-07-27 - thirteen days. That framing is
wrong, and correcting it matters more than bumping a date would.

The spine is 251 state actors lifted from the CIA World Factbook. Its
SNAPSHOT age is thirteen days. Its SOURCE-FIELD age is another thing
entirely: every populated field carries its own as_of from the Factbook,
and those run

    2025: 950 fields    2026: 25    2024: 24    2023: 7    2011: 1
    no as_of: 241

so the median fact in this file is roughly a year old at source, and one
is fifteen years old. Re-pulling the snapshot today would change the file
date and almost none of the facts. A reader told "13 days" would conclude
the file is nearly current, which is false in the direction that matters.

And 251 of 251 actors carry NULL for chief_of_defence, service_chiefs and
hq_coordinates - null by design, because no open bulk source fills them.
That is the shape of what is NOT known, and it is the more useful number
than any freshness stamp.

This script writes that census into the file's own header, so the page
built from it can state its real limits instead of a file mtime. It
computes; it never asserts. Run it after any spine refresh.

Read-only against actor data - only the header block is written.
"""
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPINE = HERE / "docs" / "kfk_spine.json"


def main():
    if not SPINE.exists():
        print("SPINE - docs/kfk_spine.json absent - INDETERMINATE",
              file=sys.stderr)
        return 1
    d = json.loads(SPINE.read_text(encoding="utf-8"))
    actors = d.get("actors") or []
    if not actors:
        print("SPINE - zero actors parsed - INDETERMINATE, not zero facts",
              file=sys.stderr)
        return 1

    years, nulls, total, populated = Counter(), Counter(), 0, 0
    for a in actors:
        for fname, f in (a.get("fields") or {}).items():
            total += 1
            if not isinstance(f, dict) or f.get("value") in (None, "", []):
                nulls[fname] += 1
                continue
            populated += 1
            m = re.search(r"(20\d\d)", str(f.get("as_of") or ""))
            years[m.group(1) if m else "no as_of"] += 1

    dated = {y: n for y, n in years.items() if y != "no as_of"}
    oldest = min(dated) if dated else None
    median_year = None
    if dated:
        run, half = 0, sum(dated.values()) / 2.0
        for y in sorted(dated):
            run += dated[y]
            if run >= half:
                median_year = y
                break

    d["freshness"] = {
        "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "snapshot_generated_at": d.get("generated_at"),
        "why_snapshot_age_misleads": (
            "The file date is when this desk pulled the Factbook, not when "
            "the facts were true. Re-pulling today would change the file "
            "date and almost none of the facts. Snapshot age is the wrong "
            "staleness measure for this file; source-field age is the right "
            "one, and it is printed below."),
        "source": d.get("spine_source"),
        "source_cadence": (
            "The CIA World Factbook revises continuously but most military "
            "fields turn over roughly annually. A snapshot days or weeks old "
            "is normal for this source; a snapshot years old would not be."),
        "actors": len(actors),
        "field_instances": total,
        "populated": populated,
        "null_by_design": total - populated,
        "source_field_as_of_years": dict(sorted(years.items())),
        "median_source_year": median_year,
        "oldest_source_year": oldest,
        "always_null_fields": sorted(
            [f for f, n in nulls.items() if n == len(actors)]),
        "null_means": ("unsourced, not zero - no open bulk source fills "
                       "command-level fields, and the gap is recorded rather "
                       "than guessed"),
    }
    SPINE.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n",
                     encoding="utf-8")
    print(f"SPINE - {len(actors)} actors - {populated}/{total} fields "
          f"populated, {total - populated} null by design", file=sys.stderr)
    print(f"SPINE - source-field years: "
          + ", ".join(f"{y}:{n}" for y, n in sorted(years.items())),
          file=sys.stderr)
    print(f"SPINE - median source year {median_year}, oldest {oldest} - "
          f"snapshot age is NOT the staleness measure", file=sys.stderr)
    print(f"SPINE - always-null: "
          + ", ".join(sorted([f for f, n in nulls.items()
                              if n == len(actors)])), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
