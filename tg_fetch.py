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
    return json.loads(REG.read_text(encoding="utf-8"))

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
    reg["_verification_protocol"]["last_run"] = datetime.datetime.utcnow().isoformat() + "Z"
    reg["_verification_protocol"]["resolved"] = resolved
    reg["_verification_protocol"]["dead"] = dead
    save_reg(reg)
    print(f"registry verified: {resolved} resolved, {dead} dead/invalid", file=sys.stderr)
    return reg

async def pull_channel(client, handle, hours=24, cap=80):
    """Pull recent messages. TEXT + metadata only; media noted as a flag, never downloaded."""
    from telethon import errors
    since = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=hours)
    out = []
    try:
        async for m in client.iter_messages(handle, limit=cap):
            if m.date < since:
                break
            if not (m.message or m.media):
                continue
            out.append({
                "channel": handle,
                "id": m.id,
                "date": m.date.isoformat(),
                "text": m.message or "",
                "has_media": bool(m.media),          # FLAG only — not downloaded
                "views": getattr(m, "views", None),
            })
    except errors.FloodWaitError as e:
        print(f"  flood-wait {e.seconds}s on {handle}", file=sys.stderr)
        await asyncio.sleep(e.seconds + 1)
    except Exception as e:
        print(f"  skip {handle}: {type(e).__name__}", file=sys.stderr)
    return out

async def main():
    from telethon import TelegramClient
    api_id = os.environ.get("TG_API_ID")
    api_hash = os.environ.get("TG_API_HASH")
    if not (api_id and api_hash):
        print("Set TG_API_ID and TG_API_HASH (from my.telegram.org, app type).", file=sys.stderr)
        sys.exit(1)

    reg = load_reg()
    verify = "--verify" in sys.argv or reg["_verification_protocol"].get("last_run") is None

    async with TelegramClient(SESSION, int(api_id), api_hash) as client:
        if verify:
            reg = await verify_registry(client, reg)

        live = [c for c in reg["channels"] if c.get("status") == "RESOLVED"]
        if not live:
            print("No RESOLVED channels yet. Run once with --verify after fixing handles.", file=sys.stderr)
            # still allow pulling 'probable/confirmed' by handle if user skips verify
            live = [c for c in reg["channels"] if c["confidence"] in ("confirmed","probable")]

        harvest, per_zone = [], {}
        for c in live:
            msgs = await pull_channel(client, c["handle"].lstrip("@"))
            for m in msgs:
                m["zone"] = c["zone"]; m["lang"] = c["lang"]
                m["bias"] = c["bias"]; m["source_type"] = c["source_type"]
            harvest.extend(msgs)
            per_zone[c["zone"]] = per_zone.get(c["zone"], 0) + len(msgs)
            await asyncio.sleep(1.5)  # be polite; avoid flood-wait

    OUT.mkdir(exist_ok=True)
    stamp = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H%M")
    path = OUT / f"tg_wardesk_{stamp}.json"
    path.write_text(json.dumps({
        "_meta": {"pulled": stamp+"Z", "n": len(harvest), "per_zone": per_zone,
                  "note": "Raw multilingual pull. NEXT STAGE: local-Qwen translate -> dedupe -> "
                          "CROSS-BIAS corroboration grade -> WAR DESK section of daily report."},
        "messages": harvest
    }, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"pulled {len(harvest)} messages across {len(per_zone)} zones -> {path}", file=sys.stderr)
    print("per-zone:", per_zone, file=sys.stderr)

if __name__ == "__main__":
    asyncio.run(main())
