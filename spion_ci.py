#!/usr/bin/env python3
"""
SPION-CI  —  the quiet channel, hosted.

Runs the page-watch channel on infrastructure the operator does not control.
Standard library only. No model, no LM Studio, no local state.

Reads   : spion_sources.json
Writes  : docs/spion_state.json   (current condition of every watched source)
          docs/spion_log.json     (append-only observation record)

Two independent change signals per source, recorded separately:
  DECLARED  — the server's own ETag / Last-Modified, via conditional request
  DERIVED   — SHA-256 over normalized extracted text, computed here

They disagree sometimes. That disagreement is information and is printed,
not reconciled: a moved ETag with a stable text hash is cosmetic churn; a
moved text hash under a stable ETag means the server's cache metadata is
lying about its own content.

Change is characterized without storing page text. Each source keeps a list
of truncated per-paragraph hashes; a new observation diffs hash sets to get
paragraphs added and removed, and quotes a hard-capped excerpt of what
appeared. Nothing about the prior state is retained in plaintext.

Exit status is 0 unless every source failed. One dead host is data, not a
build failure.
"""

import hashlib
import html.parser
import json
import os
import pathlib
import random
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

SCHEMA = "spion-state/1.0"
GENERATOR = "spion_ci.py/1.0"

ROOT = pathlib.Path(__file__).resolve().parent
SOURCES_PATH = ROOT / "spion_sources.json"
STATE_PATH = ROOT / "docs" / "spion_state.json"
LOG_PATH = ROOT / "docs" / "spion_log.json"

# The handoff. CI watches; the desk analyses, because the model is local and
# always will be. Changes land here in scouter's own items schema, with ids
# computed by scouter's own sid(), so `scouter.py spion` can merge them into
# items.json without duplicating anything it already holds.
PENDING_PATH = ROOT / "spion_pending.json"

TIMEOUT = 30
RETRIES = 3
POLITE_DELAY = (1.5, 3.5)          # seconds between fetches, randomized
EXCERPT_MAX_PARAS = 12             # hard cap on quoted new material
EXCERPT_MAX_CHARS = 240            # per paragraph
PARA_MIN_CHARS = 24                # ignore fragments as paragraph units
LOG_MAX_EVENTS = 4000              # oldest trimmed past this


def utcnow():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_json(path, default):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return default


def save_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=2, ensure_ascii=False, sort_keys=False)
        fh.write("\n")
    tmp.replace(path)


def sha256_hex(data):
    if isinstance(data, str):
        data = data.encode("utf-8")
    return hashlib.sha256(data).hexdigest()


# ---------------------------------------------------------------- extraction

class TextExtractor(html.parser.HTMLParser):
    """Text only. Script, style, and head content dropped; attributes ignored.

    Attributes are ignored on purpose: cache-busting query strings, nonces,
    CSRF tokens, and analytics ids live there and move on every request. A
    hash over raw bytes reports a change every single run and the instrument
    becomes noise. Text is the thing a reader would notice changed.
    """

    DROP = {"script", "style", "noscript", "svg", "template"}
    BLOCK = {
        "p", "div", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6",
        "section", "article", "header", "footer", "td", "th", "br", "blockquote",
    }

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self._suppress = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.DROP:
            self._suppress += 1
        elif tag in self.BLOCK:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self.DROP:
            self._suppress = max(0, self._suppress - 1)
        elif tag in self.BLOCK:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self._suppress:
            self.parts.append(data)

    def text(self):
        return "".join(self.parts)


def normalize(raw_bytes, content_type, strip_patterns):
    """Return (paragraphs, normalized_text) for a fetched body."""
    charset = "utf-8"
    m = re.search(r"charset=([\w\-]+)", content_type or "", re.I)
    if m:
        charset = m.group(1)
    try:
        raw = raw_bytes.decode(charset, errors="replace")
    except LookupError:
        raw = raw_bytes.decode("utf-8", errors="replace")

    if "html" in (content_type or "") or raw.lstrip()[:512].lower().startswith(("<!doctype", "<html")):
        parser = TextExtractor()
        try:
            parser.feed(raw)
        except Exception:
            pass  # malformed markup yields whatever was parsed before the fault
        text = parser.text()
    else:
        text = raw

    for pat in strip_patterns or []:
        try:
            text = re.sub(pat, "", text)
        except re.error:
            pass

    paragraphs = []
    for line in text.split("\n"):
        line = re.sub(r"[ \t\xa0\u200b]+", " ", line).strip()
        if len(line) >= PARA_MIN_CHARS:
            paragraphs.append(line)
    return paragraphs, "\n".join(paragraphs)


def para_hash(p):
    return sha256_hex(p)[:12]


def sid(*parts):
    """Byte-identical to scouter.sid(). Do not 'improve' — the whole point is
    that a pending item and a locally-detected item collide on the same id."""
    return hashlib.sha256("|".join(str(x) for x in parts).encode("utf-8")).hexdigest()[:12]


def pending_item(src, digest, summary):
    return {
        "id": sid(src["url"], digest),
        "ts": utcnow(),
        "source": src.get("name", src["id"]),
        "tier": src.get("tier", "PRIMARY"),
        "title": f"PAGE CHANGED: {src.get('name', src['id'])}",
        "url": src["url"],
        "summary": summary,
        "published": "",
        "content_hash": digest[:12],
        "status": "new",
        "triage": None,
        "detected_by": "spion-ci",
    }


# -------------------------------------------------------------------- fetch

def build_opener():
    opener = urllib.request.build_opener(NoRedirectLoggingHandler())
    return opener


class NoRedirectLoggingHandler(urllib.request.HTTPRedirectHandler):
    """Follow redirects but remember the final URL for the record."""
    pass


def fetch(url, etag, last_modified, user_agent, contact_url):
    """Return dict: status, body, headers, final_url, error."""
    headers = {
        "User-Agent": f"{user_agent} (+{contact_url})",
        "Accept": (
            "text/html,application/xhtml+xml,application/xml;q=0.9,"
            "application/json;q=0.9,application/pdf;q=0.8,*/*;q=0.7"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "identity",
    }
    if etag:
        headers["If-None-Match"] = etag
    if last_modified:
        headers["If-Modified-Since"] = last_modified

    last_err = None
    for attempt in range(RETRIES):
        req = urllib.request.Request(url, headers=headers, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                body = resp.read()
                return {
                    "status": resp.status,
                    "body": body,
                    "headers": {k.lower(): v for k, v in resp.headers.items()},
                    "final_url": resp.geturl(),
                    "error": None,
                }
        except urllib.error.HTTPError as exc:
            if exc.code == 304:
                return {"status": 304, "body": b"", "headers": {},
                        "final_url": url, "error": None}
            last_err = f"HTTP {exc.code} {exc.reason}"
            if exc.code in (400, 401, 403, 404, 406, 410):
                break          # contract problem, not a transient one
        except Exception as exc:                      # noqa: BLE001
            last_err = f"{type(exc).__name__}: {exc}"
        time.sleep(2 ** attempt)
    return {"status": 0, "body": b"", "headers": {}, "final_url": url, "error": last_err}


# --------------------------------------------------------------------- main

def main():
    cfg = load_json(SOURCES_PATH, None)
    if not cfg:
        print(f"spion: no readable {SOURCES_PATH.name}", file=sys.stderr)
        return 2

    user_agent = cfg.get("user_agent", "SpionCI/1.0")
    contact_url = cfg.get("contact_url", "https://example.invalid/spion")
    sources = cfg.get("sources", [])

    state = load_json(STATE_PATH, {})
    prior = state.get("sources", {}) if isinstance(state, dict) else {}
    log = load_json(LOG_PATH, {})
    events = log.get("events", []) if isinstance(log, dict) else []

    run_id = utcnow()
    checked = changed = unchanged = errored = 0
    pending = {i["id"]: i for i in load_json(PENDING_PATH, {}).get("items", [])}

    for i, src in enumerate(sources):
        sid = src["id"]
        prev = prior.get(sid, {})
        if i:
            time.sleep(random.uniform(*POLITE_DELAY))

        res = fetch(
            src["url"],
            prev.get("etag"),
            prev.get("last_modified"),
            user_agent,
            contact_url,
        )
        checked += 1
        now = utcnow()
        cur = dict(prev)
        cur.update({
            "id": sid,
            "name": src.get("name", sid),
            "org": src.get("org", ""),
            "url": src["url"],
            "last_checked_utc": now,
        })

        # ---- transport failure ------------------------------------------
        if res["error"]:
            errored += 1
            fails = prev.get("consecutive_errors", 0) + 1
            cur["consecutive_errors"] = fails
            cur["last_error"] = res["error"]
            cur["condition"] = "unreachable"
            if prev.get("condition") != "unreachable":
                events.append({
                    "utc": now, "source": sid, "kind": "error",
                    "detail": res["error"],
                })
            prior[sid] = cur
            print(f"  ! {sid:<22} {res['error']}")
            continue

        cur["consecutive_errors"] = 0
        cur.pop("last_error", None)

        # ---- server says nothing moved ----------------------------------
        if res["status"] == 304:
            unchanged += 1
            cur["condition"] = "steady"
            cur["last_signal"] = "declared-304"
            prior[sid] = cur
            print(f"  = {sid:<22} 304 not modified")
            continue

        hdrs = res["headers"]
        ctype = hdrs.get("content-type", "")
        new_etag = hdrs.get("etag")
        new_lastmod = hdrs.get("last-modified")
        declared_moved = bool(
            (new_etag and prev.get("etag") and new_etag != prev.get("etag"))
            or (new_lastmod and prev.get("last_modified")
                and new_lastmod != prev.get("last_modified"))
        )

        cur["etag"] = new_etag
        cur["last_modified"] = new_lastmod
        cur["content_type"] = ctype.split(";")[0].strip()
        if res["final_url"] != src["url"]:
            cur["redirected_to"] = res["final_url"]

        # ---- PDF and other binaries: byte hash, honestly labelled --------
        if "pdf" in ctype.lower() or src.get("mode") == "bytes":
            cur["mode"] = "bytes"
            digest = sha256_hex(res["body"])
            cur["text_hash"] = digest
            cur["bytes"] = len(res["body"])
            moved = bool(prev.get("text_hash")) and digest != prev.get("text_hash")
            if moved:
                changed += 1
                cur["condition"] = "moved"
                cur["last_changed_utc"] = now
                events.append({
                    "utc": now, "source": sid, "kind": "change",
                    "signal": "derived-bytes",
                    "declared_moved": declared_moved,
                    "note": "byte hash over binary; PDF metadata churn can "
                            "produce a move with no substantive edit",
                    "bytes_before": prev.get("bytes"),
                    "bytes_after": len(res["body"]),
                })
                it = pending_item(src, digest,
                    f"Byte hash moved on a binary source ({prev.get('bytes')} -> "
                    f"{len(res['body'])} bytes). PDF metadata churn can produce a "
                    f"move with no substantive edit; open the source to confirm.")
                pending[it["id"]] = it
                print(f"  * {sid:<22} bytes moved  {prev.get('bytes')} -> {len(res['body'])}")
            else:
                unchanged += 1
                cur["condition"] = "steady" if prev else "baselined"
                print(f"  = {sid:<22} bytes steady")
            prior[sid] = cur
            continue

        # ---- text sources ------------------------------------------------
        cur["mode"] = "text"
        paras, text = normalize(res["body"], ctype, src.get("strip_patterns"))
        digest = sha256_hex(text)
        hashes = [para_hash(p) for p in paras]
        cur["text_hash"] = digest
        cur["text_len"] = len(text)
        cur["paragraphs"] = len(paras)

        if not prev.get("text_hash"):
            cur["condition"] = "baselined"
            cur["para_hashes"] = hashes
            cur["last_changed_utc"] = now
            events.append({"utc": now, "source": sid, "kind": "baseline",
                           "paragraphs": len(paras), "text_len": len(text)})
            prior[sid] = cur
            print(f"  + {sid:<22} baselined  {len(paras)} paragraphs")
            continue

        if digest == prev["text_hash"]:
            unchanged += 1
            cur["condition"] = "steady"
            cur["para_hashes"] = prev.get("para_hashes", hashes)
            cur["last_signal"] = "declared-moved-text-steady" if declared_moved else "steady"
            prior[sid] = cur
            print(f"  = {sid:<22} steady"
                  + ("  [etag moved, text did not]" if declared_moved else ""))
            continue

        # a real content move
        changed += 1
        old_set = set(prev.get("para_hashes", []))
        new_set = set(hashes)
        added = [p for p in paras if para_hash(p) not in old_set]
        removed_n = len(old_set - new_set)

        excerpt = [p[:EXCERPT_MAX_CHARS] for p in added[:EXCERPT_MAX_PARAS]]
        cur["para_hashes"] = hashes
        cur["condition"] = "moved"
        cur["last_changed_utc"] = now
        cur["last_signal"] = "derived-and-declared" if declared_moved else "derived-only"

        events.append({
            "utc": now,
            "source": sid,
            "kind": "change",
            "signal": cur["last_signal"],
            "declared_moved": declared_moved,
            "paragraphs_added": len(added),
            "paragraphs_removed": removed_n,
            "text_len_before": prev.get("text_len"),
            "text_len_after": len(text),
            "hash_before": prev["text_hash"],
            "hash_after": digest,
            "excerpt": excerpt,
            "excerpt_truncated": len(added) > EXCERPT_MAX_PARAS,
        })
        summary = (f"Extracted text moved: {len(added)} paragraph(s) added, "
                   f"{removed_n} removed. Signal {cur['last_signal']}."
                   + ("" if declared_moved else " Server cache metadata did not move.")
                   + (" First new material: " + added[0][:300] if added else ""))
        it = pending_item(src, digest, summary)
        pending[it["id"]] = it
        flag = "" if declared_moved else "  [text moved, server metadata did not]"
        print(f"  * {sid:<22} MOVED  +{len(added)} -{removed_n} paragraphs{flag}")
        prior[sid] = cur

    if checked and errored == checked:
        print("spion: every source failed — treating as run failure", file=sys.stderr)
        return 1

    if len(events) > LOG_MAX_EVENTS:
        events = events[-LOG_MAX_EVENTS:]

    save_json(STATE_PATH, {
        "schema": SCHEMA,
        "generator": GENERATOR,
        "as_of": run_id,
        "run_host": os.environ.get("GITHUB_ACTIONS") and "github-actions" or "local",
        "run_url": (
            f"{os.environ.get('GITHUB_SERVER_URL','')}/"
            f"{os.environ.get('GITHUB_REPOSITORY','')}/actions/runs/"
            f"{os.environ.get('GITHUB_RUN_ID','')}"
            if os.environ.get("GITHUB_RUN_ID") else None
        ),
        "counts": {"checked": checked, "moved": changed,
                   "steady": unchanged, "unreachable": errored},
        "sources": prior,
    })
    save_json(LOG_PATH, {
        "schema": "spion-log/1.0",
        "generator": GENERATOR,
        "as_of": run_id,
        "events": events,
    })

    save_json(PENDING_PATH, {
        "schema": "spion-pending/1.0",
        "generator": GENERATOR,
        "as_of": run_id,
        "_note": "Consumed by `scouter.py spion` on the desk machine: merge these "
                 "into items.json by id, then clear. Ids match scouter.sid(url, hash), "
                 "so anything the local channel already caught collides and dedupes.",
        "items": list(pending.values()),
    })

    print(f"spion: {checked} checked · {changed} moved · "
          f"{unchanged} steady · {errored} unreachable · "
          f"{len(pending)} pending for triage")
    return 0


if __name__ == "__main__":
    sys.exit(main())
