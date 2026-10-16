#!/usr/bin/env python3
"""tg_public_arm.py - public Telegram forecasting lane (PUBLIC-1016).
Reads one PUBLIC Telegram group through the desk session, parses template
forecasts, hashes the poster's id with a local salt (Documents/netz_public/salt.txt,
never in the repo), and writes one arm file per poster into Documents/arm_raw
in the exact array format kkr.py --ingest reads. citations are [0] (the
operator/cold sentinel). The arm tag is public/<hash12>/cold. Same gate, same
Brier, same ledger as every other arm. The hash is one-way; the mapping is
never stored. Edits made in the group after a seal change nothing: the ledger
row is what was read at seal time. Read-only; the script never posts.
"""
import os, re, sys, json, hashlib, argparse, datetime, pathlib

HOME = pathlib.Path(os.environ.get("USERPROFILE") or os.path.expanduser("~"))
PUBDIR = HOME / "Documents" / "netz_public"
RAWDIR = HOME / "Documents" / "arm_raw"
SESSION = str(pathlib.Path(__file__).resolve().parent / "netz_wardesk")
KEYS = ("statement", "probability", "resolution", "deadline", "failure", "domain")
LINE = re.compile(r"^\s*(statement|probability|resolution|deadline|failure|domain)\s*:\s*(.*)$", re.I)

TEMPLATE = """FORECAST
statement: <one sentence, an absolute date window, no 'within the next N days'>
probability: <0-100>
resolution: <what source and what reading makes it TRUE>
deadline: <YYYY-MM-DD, at least 3 days out>
failure: <what makes it FALSE>
domain: <optional: military/conflict, economics/markets, politics, science, other>

Rules: one forecast per message, posted before 1800 America/Denver to count that day.
Your handle is never recorded; you appear on the board as public/<12 hex>/cold.
Scored by Brier against the same ledger as the model arms. Edits after seal do not count."""

def salt():
    p = PUBDIR / "salt.txt"
    if not p.exists():
        sys.exit("no salt at " + str(p))
    return p.read_text().strip()

def hid(sender_id, s):
    return hashlib.sha256((s + str(sender_id)).encode()).hexdigest()[:12]

def parse(text):
    """Return (row, reason). row is None when the message is not a forecast or is incomplete."""
    if not text or "forecast" not in text.lower()[:40]:
        return None, "not a forecast message"
    f = {}
    cur = None
    for raw in text.splitlines():
        m = LINE.match(raw)
        if m:
            cur = m.group(1).lower()
            f[cur] = m.group(2).strip()
        elif cur and raw.strip():
            f[cur] = (f[cur] + " " + raw.strip()).strip()
    missing = [k for k in ("statement", "probability", "resolution", "deadline", "failure") if not f.get(k)]
    if missing:
        return None, "missing " + ", ".join(missing)
    try:
        pr = int(round(float(f["probability"].rstrip("%"))))
    except ValueError:
        return None, "probability not a number"
    if not 0 <= pr <= 100:
        return None, "probability outside 0-100"
    try:
        datetime.datetime.strptime(f["deadline"], "%Y-%m-%d")
    except ValueError:
        return None, "deadline not YYYY-MM-DD"
    row = {"statement": f["statement"], "domain": f.get("domain") or "unclassified",
           "probability": pr, "resolution": f["resolution"], "deadline": f["deadline"],
           "citations": [0], "failure_condition": f["failure"]}
    return row, ""

SAMPLE = """FORECAST
statement: Between 2026-10-17 and 2026-10-31 the Bank of England announces a Bank Rate cut of at least 25 basis points.
probability: 35
resolution: TRUE if the Bank of England's own Monetary Policy Summary, published on bankofengland.co.uk between 2026-10-17 and 2026-10-31, records a cut of 25 bp or more.
deadline: 2026-11-03
failure: No cut of 25 bp or more is announced in that window.
domain: economics/markets"""

def selftest():
    row, why = parse(SAMPLE)
    assert row and row["probability"] == 35 and row["citations"] == [0], why
    bad, why = parse(SAMPLE.replace("deadline: 2026-11-03\n", ""))
    assert bad is None and "deadline" in why, why
    none, why = parse("hello everyone")
    assert none is None
    print("selftest PASS: template parses, missing field rejected, chatter ignored")

async def read_group(group, since, out_dir, write):
    from telethon import TelegramClient
    from telethon.errors import FloodWaitError
    import asyncio
    aid, ah = os.environ.get("TG_API_ID"), os.environ.get("TG_API_HASH")
    if not aid or not ah:
        sys.exit("TG_API_ID / TG_API_HASH not set")
    s = salt()
    since_dt = datetime.datetime.strptime(since, "%Y-%m-%d").replace(tzinfo=datetime.timezone.utc)
    by = {}
    intake = []
    dropped = 0
    async with TelegramClient(SESSION, int(aid), ah) as c:
        ent = await c.get_entity(group)
        print("group resolved:", getattr(ent, "title", group), "| reading since", since, "UTC")
        try:
            async for m in c.iter_messages(ent):
                if m.date < since_dt:
                    break
                sid = getattr(getattr(m, "from_id", None), "user_id", None)
                if sid is None or not m.message:
                    continue
                row, why = parse(m.message)
                if row is None:
                    if why != "not a forecast message":
                        dropped += 1
                        print(f"  drop msg {m.id} ({why})")
                    continue
                h = hid(sid, s)
                by.setdefault(h, []).append(row)
                intake.append({"msg_id": m.id, "utc": m.date.strftime("%Y-%m-%dT%H:%M:%SZ"),
                               "edited": bool(m.edit_date), "hash": h, "statement": row["statement"]})
        except FloodWaitError as fw:
            print("floodwait", fw.seconds, "s; rerun after"); return
    day = datetime.date.today()
    tag_day = day.strftime("%m_%d_%Y")
    print(f"\n{sum(len(v) for v in by.values())} forecasts from {len(by)} posters; {dropped} dropped")
    for h, rows in sorted(by.items()):
        fn = out_dir / f"public_{h}_packet{tag_day}.json"
        print(f"  public/{h}/cold  {len(rows):2d} rows -> {fn.name}")
        if write:
            fn.write_text(json.dumps(rows, indent=1), encoding="ascii")
            print(f"     python kkr.py --ingest \"{fn}\" --arm public/{h}/cold")
    if write and intake:
        ip = PUBDIR / f"intake_{day.isoformat()}.json"
        ip.write_text(json.dumps(intake, indent=1), encoding="ascii")
        print("intake record (local only):", ip)
    if not write:
        print("dry run; add --write to produce the arm files")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--group", default=os.environ.get("TG_PUBLIC_GROUP"))
    ap.add_argument("--since", default=datetime.date.today().isoformat())
    ap.add_argument("--out", default=str(RAWDIR))
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--template", action="store_true")
    a = ap.parse_args()
    if a.template:
        print(TEMPLATE); return
    if a.selftest:
        selftest(); return
    if not a.group:
        sys.exit("--group @handle (or TG_PUBLIC_GROUP) required")
    import asyncio
    asyncio.run(read_group(a.group, a.since, pathlib.Path(a.out), a.write))

if __name__ == "__main__":
    main()
