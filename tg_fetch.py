#!/usr/bin/env python3
"""
tg_fetch.py — NETZ War Desk ingestion.
Reads PUBLIC conflict channels from war_channels.json, verifies the registry on
first run, pulls recent messages, hands them to the collation pipeline.

SCOPE FENCE (see war_channels.json _charter): collation of what channels REPORT.
No person-targeting, no dossiers, no private/invite-only channels. Public read-only.

Requires:  pip install telethon
Credentials: my.telegram.org -> API development tools -> api_id + api_hash (APP, not bot)
Set as env vars: TG_API_ID, TG_API_HASH   (first run does interactive phone login,
then caches a .session file — never commit that file; add to .gitignore)
"""
import os, json, sys, asyncio, datetime, pathlib

REG = pathlib.Path("war_channels.json")
OUT = pathlib.Path("forecasts")  # NETZ intake dir; adjust to your report intake
SESSION = "netz_wardesk"         # .session cache; GITIGNORE THIS

def load_reg():
    return json.loads(REG.read_text(encoding="utf-8-sig"))

def save_reg(reg):
    REG.write_text(json.dumps(reg, indent=2, ensure_ascii=False), encoding="utf-8")

async def verify_registry(client, reg):
    """First-contact audit: resolve each handle, mark resolved/dead/renamed.
    The tool audits its own source list. Poisoned handles get flagged, not trusted."""
    from telethon import errors
    resolved = dead = 0
    for c in reg["channels"]:
        h = c["handle"].lstrip("@")
        try:
            ent = await client.get_entity(h)
            c["status"] = "RESOLVED"
            c["resolved_title"] = getattr(ent, "title", None)
            c["resolved_id"] = getattr(ent, "id", None)
            resolved += 1
        except (errors.UsernameNotOccupiedError, errors.UsernameInvalidError, ValueError):
            c["status"] = "DEAD"
            dead += 1
        except errors.FloodWaitError as e:
            print(f"  flood-wait {e.seconds}s on {h}; pausing", file=sys.stderr)
            await asyncio.sleep(e.seconds + 1)
        except Exception as e:
            c["status"] = f"ERROR:{type(e).__name__}"
    reg["_verification_protocol"]["last_run"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    reg["_verification_protocol"]["resolved"] = resolved
    reg["_verification_protocol"]["dead"] = dead
    save_reg(reg)
    print(f"registry verified: {resolved} resolved, {dead} dead/invalid", file=sys.stderr)
    return reg

async def pull_channel(client, handle, hours=24, cap=2000):
    """Pull the WINDOW, not a count. TEXT + metadata only; media flagged, never
    downloaded.

    DEFECT FIXED 2026-07-30, measured on three consecutive live pulls: the old
    signature was (hours=24, cap=80) with iter_messages(limit=80) — a count
    limit. The date-floor break only fired if the 80 newest messages spanned
    more than the window, so any channel posting over 80/day was silently
    truncated at exactly 80 (QudsNen, boris_rozhin, PRESSTV on 07-28; global
    zone again on 07-30). The window is now the boundary; cap is a safety
    ceiling that ANNOUNCES itself when it binds instead of masquerading as a
    quiet day.

    Second defect, same visit: FloodWaitError slept politely and then RETURNED
    with whatever it had — a flood-waited channel lost its tail silently. It
    now resumes from the last message id after the wait.
    """
    from telethon import errors
    since = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=hours)
    out, status = [], "ok"
    offset_id = 0          # 0 = newest; resume point after a flood-wait
    retries = 0
    while True:
        try:
            async for m in client.iter_messages(handle, limit=None,
                                                offset_id=offset_id):
                if m.date < since:
                    return out, status
                offset_id = m.id
                if not (m.message or m.media):
                    continue
                out.append({
                    "channel": handle,
                    "id": m.id,
                    "date": m.date.isoformat(),
                    "text": m.message or "",
                    "has_media": bool(m.media),      # FLAG only — not downloaded
                    "views": getattr(m, "views", None),
                })
                if len(out) >= cap:
                    print(f"  CAP HIT on {handle}: {cap} messages inside the "
                          f"window and the window is not exhausted — raise "
                          f"--cap or accept the cut", file=sys.stderr)
                    return out, "cap_hit"
            return out, status
        except errors.FloodWaitError as e:
            retries += 1
            if retries > 3:
                print(f"  {handle}: flood-waited {retries-1}x, giving up with "
                      f"{len(out)} messages held", file=sys.stderr)
                return out, f"floodwait_giveup_after_{retries-1}"
            print(f"  flood-wait {e.seconds}s on {handle} — resuming from "
                  f"id {offset_id} after the wait", file=sys.stderr)
            status = "floodwait_resumed"
            await asyncio.sleep(e.seconds + 1)
        except Exception as e:
            print(f"  skip {handle}: {type(e).__name__}: {e}", file=sys.stderr)
            return out, f"error:{type(e).__name__}"

async def main():
    from telethon import TelegramClient
    api_id = os.environ.get("TG_API_ID")
    api_hash = os.environ.get("TG_API_HASH")
    if not (api_id and api_hash):
        print("Set TG_API_ID and TG_API_HASH (from my.telegram.org, app type).", file=sys.stderr)
        sys.exit(1)

    reg = load_reg()
    verify = "--verify" in sys.argv or reg["_verification_protocol"].get("last_run") is None
    def _flag(name, default):
        if name in sys.argv:
            try:
                return int(sys.argv[sys.argv.index(name) + 1])
            except (IndexError, ValueError):
                print(f"{name} needs an integer", file=sys.stderr); sys.exit(1)
        return default
    hours = _flag("--hours", 24)
    cap = _flag("--cap", 2000)

    async with TelegramClient(SESSION, int(api_id), api_hash) as client:
        if verify:
            reg = await verify_registry(client, reg)

        live = [c for c in reg["channels"] if c.get("status") == "RESOLVED"]
        if not live:
            print("No RESOLVED channels yet. Run once with --verify after fixing handles.", file=sys.stderr)
            # still allow pulling 'probable/confirmed' by handle if user skips verify
            live = [c for c in reg["channels"] if c["confidence"] in ("confirmed","probable")]

        harvest, per_zone, per_channel = [], {}, []
        for c in live:
            h = c["handle"].lstrip("@")
            msgs, status = await pull_channel(client, h, hours=hours, cap=cap)
            for m in msgs:
                m["zone"] = c["zone"]; m["lang"] = c["lang"]
                m["bias"] = c["bias"]; m["source_type"] = c["source_type"]
            harvest.extend(msgs)
            per_zone[c["zone"]] = per_zone.get(c["zone"], 0) + len(msgs)
            per_channel.append({"channel": h, "zone": c["zone"], "n": len(msgs),
                                "status": status,
                                "oldest": msgs[-1]["date"] if msgs else None,
                                "newest": msgs[0]["date"] if msgs else None})
            await asyncio.sleep(1.5)  # be polite; avoid flood-wait

        # the yield table: silence and truncation are both data
        print(f"\n{'channel':22} {'zone':16} {'msgs':>5}  status", file=sys.stderr)
        for r in sorted(per_channel, key=lambda x: -x["n"]):
            mark = "" if r["status"] == "ok" else f"  << {r['status'].upper()}"
            print(f"{r['channel']:22} {r['zone']:16} {r['n']:5}  {r['status']}{mark}",
                  file=sys.stderr)
        zero = [r["channel"] for r in per_channel if r["n"] == 0]
        if zero:
            print(f"\n{len(zero)} channel(s) returned NOTHING in the window: "
                  + ", ".join(zero), file=sys.stderr)
            print("A registered channel with zero yield is either dead, "
                  "renamed, or off its beat — that is registry data, not "
                  "weather.", file=sys.stderr)

    OUT.mkdir(exist_ok=True)
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d_%H%M")
    path = OUT / f"tg_wardesk_{stamp}.json"
    path.write_text(json.dumps({
        "_meta": {"pulled": stamp+"Z", "n": len(harvest), "per_zone": per_zone,
                  "window_hours": hours, "cap": cap,
                  "per_channel": per_channel,
                  "note": "Raw multilingual pull. NEXT STAGE: local-Qwen translate -> dedupe -> "
                          "CROSS-BIAS corroboration grade -> WAR DESK section of daily report."},
        "messages": harvest
    }, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"pulled {len(harvest)} messages across {len(per_zone)} zones -> {path}", file=sys.stderr)
    print("per-zone:", per_zone, file=sys.stderr)

if __name__ == "__main__":
    asyncio.run(main())
