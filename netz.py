#!/usr/bin/env python3
"""
NETZ v2.0 — local auto-collation engine for the daily intelligence report.

Pipeline: fetch (RSS + JSON APIs) → window → dedupe/cluster → corroboration
scoring → delta vs. previous run → PIR matching → convergence detection →
synthesis with ICD 203 estimative discipline (optional, via LM Studio) →
Admiralty-graded report, markdown + dark HTML.

No API keys anywhere. If no model is loaded, the collated report still ships.

Usage:
    python netz.py [--hours 48] [--no-llm] [--open] [--config my.json]
"""

import argparse
import html
import json
import os
import platform
import re
import subprocess
import sys
import webbrowser
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import feedparser
import requests

DEFAULT_CONFIG = "report_config.json"
HERE = Path(__file__).resolve().parent
STATE_FILE = HERE / "state.json"

STOPWORDS = set("""
a an and are as at be by for from has have how in is it its of on or that the
this to was were what when where which who will with after amid over under
new says said say more than into out up down about their his her they them
""".split())

CITE_RE = re.compile(r"\[(\d+(?:\s*,\s*\d+)*)\]")
TAG_RE = re.compile(r"<[^>]+>")
CAP_SEQ_RE = re.compile(r"\b([A-Z][a-zA-Z\u00C0-\u024F]+(?:\s+[A-Z][a-zA-Z\u00C0-\u024F]+){0,3})\b")
TRACKING_PARAMS = {"utm_source", "utm_medium", "utm_campaign", "utm_term",
                   "utm_content", "fbclid", "gclid", "ref", "cmpid", "ns_mchannel"}
UA = {"User-Agent": "NETZ/2.0 (personal OSINT collation; contact via config)"}


def load_config(path: str) -> dict:
    p = Path(path)
    if not p.is_absolute():
        p = HERE / p
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


# ----------------------------------------------------------------------
# fetch + normalize (RSS)
# ----------------------------------------------------------------------

def canonical_url(url: str) -> str:
    try:
        parts = urlsplit(url)
        q = [(k, v) for k, v in parse_qsl(parts.query) if k.lower() not in TRACKING_PARAMS]
        return urlunsplit((parts.scheme, parts.netloc.lower(), parts.path.rstrip("/"),
                           urlencode(q), ""))
    except Exception:
        return url


def strip_html(text: str) -> str:
    return html.unescape(TAG_RE.sub(" ", text or "")).strip()


def parse_when(entry):
    for key in ("published_parsed", "updated_parsed"):
        t = entry.get(key)
        if t:
            try:
                return datetime(*t[:6], tzinfo=timezone.utc)
            except Exception:
                pass
    return None


def fetch_feed(source_name: str, url: str, category: str, timeout: int = 12) -> dict:
    result = {"source": source_name, "url": url, "category": category,
              "status": "ok", "items": [], "error": ""}
    try:
        resp = requests.get(url, timeout=timeout, headers=UA)
        resp.raise_for_status()
        parsed = feedparser.parse(resp.content)
        if parsed.bozo and not parsed.entries:
            result["status"] = "parse_fail"
            result["error"] = str(getattr(parsed, "bozo_exception", "unparseable"))
            return result
        for e in parsed.entries:
            title = strip_html(e.get("title", "")).strip()
            if not title:
                continue
            result["items"].append({
                "title": title,
                "link": canonical_url(e.get("link", "")),
                "summary": strip_html(e.get("summary", e.get("description", "")))[:400],
                "when": parse_when(e),
                "source": source_name,
                "category": category,
            })
    except requests.RequestException as exc:
        result["status"] = "fetch_fail"
        result["error"] = str(exc)[:160]
    except Exception as exc:  # noqa: BLE001
        result["status"] = "error"
        result["error"] = str(exc)[:160]
    return result


def fetch_all(config: dict, max_workers: int = 12):
    jobs, health = [], []
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = []
        for category, feeds in config["categories"].items():
            for source_name, url in feeds.items():
                futures.append(pool.submit(fetch_feed, source_name, url, category,
                                           config.get("fetch_timeout_seconds", 12)))
        for fut in as_completed(futures):
            jobs.append(fut.result())
    items = []
    for job in jobs:
        newest = max((i["when"] for i in job["items"] if i["when"]), default=None)
        health.append({"source": job["source"], "category": job["category"],
                       "status": job["status"], "count": len(job["items"]),
                       "newest": newest, "error": job["error"]})
        items.extend(job["items"])
    health.sort(key=lambda h: (h["category"], h["source"]))
    return items, health


def window_filter(items: list, hours: int) -> list:
    cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
    kept = []
    for it in items:
        if it["when"] is None:
            it["undated"] = True
            kept.append(it)
        elif it["when"] >= cutoff:
            it["undated"] = False
            kept.append(it)
    return kept


# ----------------------------------------------------------------------
# JSON API sources (keyless): ReliefWeb, NWS
# ----------------------------------------------------------------------

def fetch_reliefweb(config: dict, health: list) -> list:
    """Humanitarian-crisis reporting — injected into disaster category."""
    if not config.get("reliefweb_enabled", True):
        return []
    url = config.get("reliefweb_url", "https://api.reliefweb.int/v1/reports")
    entry = {"source": "ReliefWeb", "category": "disaster_infrastructure",
             "status": "ok", "count": 0, "newest": None, "error": ""}
    items = []
    try:
        rw_headers = dict(UA); rw_headers["Accept"] = "application/json"
        r = requests.get(url, timeout=15, headers=rw_headers,
                         params={"appname": "netz", "limit": 15,
                                 "profile": "list", "preset": "latest"})
        r.raise_for_status()
        for d in r.json().get("data", []):
            f = d.get("fields", {}) or {}
            title = f.get("title")
            if not title:
                continue
            when = None
            try:
                created = ((f.get("date") or {}).get("created")) or ""
                when = datetime.fromisoformat(created.replace("Z", "+00:00"))
                if when.tzinfo is None:
                    when = when.replace(tzinfo=timezone.utc)
            except Exception:
                pass
            items.append({"title": strip_html(title),
                          "link": f.get("url_alias") or f.get("url") or d.get("href", ""),
                          "summary": "", "when": when,
                          "source": "ReliefWeb", "category": "disaster_infrastructure"})
        entry["count"] = len(items)
        entry["newest"] = max((i["when"] for i in items if i["when"]), default=None)
    except Exception as exc:
        entry["status"] = "fetch_fail"
        entry["error"] = str(exc)[:160]
    health.append(entry)
    return items


def fetch_nws(config: dict) -> list:
    """Active Extreme/Severe NWS alerts (US)."""
    if not config.get("nws_enabled", True):
        return []
    url = config.get("nws_url", "https://api.weather.gov/alerts/active")
    try:
        r = requests.get(url, timeout=15, headers=UA,
                         params={"status": "actual", "severity": "Extreme,Severe"})
        r.raise_for_status()
        out = []
        for feat in r.json().get("features", [])[:60]:
            p = feat.get("properties", {}) or {}
            out.append({"event": p.get("event", "?"),
                        "severity": p.get("severity", ""),
                        "area": (p.get("areaDesc") or "")[:90],
                        "headline": (p.get("headline") or "")[:140]})
        return out
    except Exception:
        return []


# ----------------------------------------------------------------------
# dedupe + cluster + score
# ----------------------------------------------------------------------

def tokens(text: str) -> set:
    return {w for w in re.findall(r"[a-z\u00DF-\u00FF']+", text.lower())
            if len(w) > 3 and w not in STOPWORDS}


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def cluster_items(items: list, threshold: float = 0.45) -> list:
    seen_urls = {}
    deduped = []
    for it in items:
        key = it["link"] or it["title"]
        if key in seen_urls:
            continue
        seen_urls[key] = True
        it["tok"] = tokens(it["title"])
        deduped.append(it)

    clusters = []
    for it in deduped:
        placed = False
        for cl in clusters:
            if cl["items"][0]["category"] != it["category"]:
                continue
            if jaccard(it["tok"], cl["tokens"]) >= threshold:
                cl["items"].append(it)
                cl["tokens"] |= it["tok"]
                placed = True
                break
        if not placed:
            clusters.append({"items": [it], "tokens": set(it["tok"])})

    for cl in clusters:
        cl["sources"] = sorted({i["source"] for i in cl["items"]})
        cl["corroboration"] = len(cl["sources"])
        whens = [i["when"] for i in cl["items"] if i["when"]]
        cl["newest"] = max(whens) if whens else None
        cl["category"] = cl["items"][0]["category"]
        rep = max(cl["items"], key=lambda i: i["when"] or datetime.min.replace(tzinfo=timezone.utc))
        cl["rep"] = rep
    return clusters


# ----------------------------------------------------------------------
# delta tracking (the report remembers yesterday)
# ----------------------------------------------------------------------

def mark_delta(clusters: list):
    today = datetime.now(timezone.utc).date()
    prev = []
    if STATE_FILE.exists():
        try:
            prev = json.loads(STATE_FILE.read_text(encoding="utf-8")).get("stories", [])
        except Exception:
            prev = []
    for p in prev:
        p["_tok"] = set(p.get("tokens", []))
    for cl in clusters:
        first_seen = today
        for p in prev:
            if jaccard(cl["tokens"], p["_tok"]) >= 0.5:
                try:
                    first_seen = min(first_seen,
                                     datetime.strptime(p["first_seen"], "%Y-%m-%d").date())
                except ValueError:
                    pass
        cl["first_seen"] = first_seen
        cl["is_new"] = first_seen == today
        cl["age_days"] = (today - first_seen).days + 1
    state = {"stories": [{"tokens": sorted(cl["tokens"])[:30],
                          "title": cl["rep"]["title"][:120],
                          "first_seen": cl["first_seen"].strftime("%Y-%m-%d")}
                         for cl in clusters]}
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False), encoding="utf-8")


def delta_mark(cl) -> str:
    return "🆕" if cl.get("is_new", True) else f"↺D{cl.get('age_days', 1)}"


# ----------------------------------------------------------------------
# PIRs + convergence
# ----------------------------------------------------------------------

def pir_status(config: dict, clusters: list) -> list:
    out = []
    for pir in config.get("pirs", []):
        pt = tokens(pir)
        need = 2 if len(pt) >= 2 else 1
        hits = [cl for cl in clusters if len(pt & cl["tokens"]) >= need]
        hits.sort(key=lambda c: -c["corroboration"])
        out.append({"pir": pir, "hits": hits[:4]})
    return out


def convergence(clusters: list, min_categories: int = 2, top_n: int = 12) -> list:
    term_map = {}
    for cl in clusters:
        text = cl["rep"]["title"] + " " + cl["rep"]["summary"]
        for m in CAP_SEQ_RE.findall(text):
            term = m.strip()
            if term.lower() in STOPWORDS or len(term) < 4:
                continue
            entry = term_map.setdefault(term, {"categories": set(), "hits": 0})
            entry["categories"].add(cl["category"])
            entry["hits"] += 1
    hits = [(t, d) for t, d in term_map.items() if len(d["categories"]) >= min_categories]
    hits.sort(key=lambda x: (-len(x[1]["categories"]), -x[1]["hits"], x[0]))
    return [(t, sorted(d["categories"]), d["hits"]) for t, d in hits[:top_n]]


# ----------------------------------------------------------------------
# LM Studio synthesis (optional layer) — ICD 203 discipline
# ----------------------------------------------------------------------

def llm_probe(base_url: str, timeout: int = 5):
    try:
        r = requests.get(f"{base_url.rstrip('/')}/models", timeout=timeout)
        r.raise_for_status()
        data = r.json().get("data", [])
        return data[0]["id"] if data else None
    except Exception:
        return None


def llm_chat(base_url: str, model: str, system: str, user: str,
             max_tokens: int = 600, temperature: float = 0.2, timeout: int = 240):
    try:
        r = requests.post(f"{base_url.rstrip('/')}/chat/completions", timeout=timeout,
                          json={"model": model, "temperature": temperature,
                                "max_tokens": max_tokens,
                                "messages": [{"role": "system", "content": system},
                                             {"role": "user", "content": user}]})
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"].strip()
    except Exception:
        return None


# --- numeric provenance (patch_netz_numeric) --------------------------------
# Every prompt already forbids outside knowledge. None of them said a FIGURE is
# a claim, so the model wrote numbers as prose texture and cited whatever the
# sentence was about. This closes that specifically, in the model's own terms.
NUMERIC_RULE = (
    " NUMBERS ARE CLAIMS. Do not write any figure — percentage, currency amount, "
    "count, magnitude, area, casualty total, market level, or poll margin — unless "
    "that exact figure appears in the text of an item you cite for that sentence. "
    "If a figure would strengthen a sentence but is not in the record, write the "
    "sentence without it: 'oil prices fell sharply [8]' is correct where "
    "'oil prices fell 9% to below $88 [8]' is a fabrication if item 8 carries no "
    "such number. Never compute, convert, round, or infer a figure from other "
    "figures. Never restate a number from memory or general knowledge. Where the "
    "provided market snapshot gives a level or a daily change, that snapshot "
    "governs and no other value for the same instrument may be written. "
    "Do not write a completed-tense claim about a date later than this report's "
    "date. A sentence carrying an unsupported figure is worse than no sentence."
)
# ----------------------------------------------------------------------------

SYSTEM_PROMPT = (
    "You are an OSINT analyst drafting a section of a daily intelligence report. "
    "Work ONLY from the numbered items provided. Every sentence must end with a "
    "citation in square brackets, e.g. [3] or [3,7]. No outside knowledge. "
    "Separate reporting from assessment: sentences relaying what sources say use "
    "'X reports/reported'; analytic inference is prefixed 'We assess' and uses "
    "standardized estimative language only (almost certainly, very likely, likely, "
    "roughly even chance, unlikely, very unlikely). Never assess beyond what the "
    "cited items support; single-source claims may not be assessed above 'possibly'. "
    "If items conflict, state the conflict with both citations. If any standing "
    "requirement (PIR) listed is touched by the items, address it explicitly. "
    "End with exactly one sentence beginning 'WATCH:' naming the single most "
    "concrete observable to monitor in the next 24-72h, with citation. "
    "Dense prose, no bullets, no headers, 100-190 words."
 + NUMERIC_RULE)

BLUF_PROMPT = (
    "You are an OSINT analyst writing the KEY JUDGMENTS of a daily intelligence "
    "report from the numbered top signals provided, which span multiple categories. "
    "Write 3-5 judgments. Each is ONE sentence beginning 'KJ1:', 'KJ2:', etc., "
    "using standardized estimative language (almost certainly, very likely, likely, "
    "roughly even chance, unlikely), ending with a confidence tag in parentheses — "
    "(High confidence), (Moderate confidence), or (Low confidence) — followed by "
    "citations like [2] or [2,5]. Confidence must track sourcing: only "
    "multi-source-corroborated items support High confidence; single-source items "
    "cap at Moderate. Work ONLY from the items given. Lead with whatever crosses "
    "categories or carries the highest corroboration."
 + NUMERIC_RULE)

IW_PROMPT = (
    "You are an OSINT analyst. From the numbered top signals below, produce the "
    "INDICATIONS & WARNINGS and OUTLOOK blocks of a daily intelligence report. "
    "Format exactly:\nI&W:\n1. <one concrete observable to monitor in the next "
    "24-72h, tied to escalation or de-escalation, with citation [n]>\n2. ...\n"
    "(3 to 6 numbered lines)\nOUTLOOK:\n<one 60-90 word paragraph, standardized "
    "estimative language, every sentence cited [n]>\n"
    "Work ONLY from the items given. Observables must be checkable from public "
    "reporting (a statement, a closure, a price level, an advisory), never vague."
 + NUMERIC_RULE)


def number_items(clusters: list, limit: int):
    chosen = clusters[:limit]
    lines = []
    for n, cl in enumerate(chosen, 1):
        rep = cl["rep"]
        when = rep["when"].strftime("%d %b %H:%M UTC") if rep["when"] else "undated"
        lines.append(f"[{n}] {rep['title']} — {', '.join(cl['sources'])} "
                     f"({cl['corroboration']} source{'s' if cl['corroboration'] > 1 else ''}, "
                     f"{when}, {'new today' if cl.get('is_new', True) else 'day ' + str(cl.get('age_days', 1)) + ' of coverage'}). "
                     f"{rep['summary'][:250]}")
    return "\n".join(lines), chosen


def audit_citations(text: str, n_items: int):
    warnings = []
    cited = set()
    for m in CITE_RE.finditer(text):
        for num in re.split(r"\s*,\s*", m.group(1)):
            cited.add(int(num))
    bad = [c for c in cited if c < 1 or c > n_items]
    if bad:
        warnings.append(f"citations out of range: {sorted(bad)}")
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    uncited = sum(1 for s in sentences
                  if not CITE_RE.search(s) and not s.startswith(("I&W:", "OUTLOOK:")))
    if uncited:
        warnings.append(f"{uncited} sentence(s) carry no citation — audit before use")
    return text, warnings


# ----------------------------------------------------------------------
# admiralty grading, markets, KEV
# ----------------------------------------------------------------------

def admiralty_grade(cluster, rel_map: dict) -> str:
    letters = [rel_map.get(s, "C") for s in cluster["sources"]]
    best = min(letters)
    corr = cluster["corroboration"]
    cred = 1 if corr >= 3 else 2 if corr == 2 else 3
    return f"{best}{cred}"


def fetch_markets(config: dict) -> list:
    mcfg = config.get("markets") or {}
    rows = []
    # Yahoo Finance chart endpoint — keyless JSON, tolerant of blocked-provider fallback.
    yf_base = mcfg.get("yahoo_base", "https://query1.finance.yahoo.com/v8/finance/chart/")
    yf_headers = dict(UA); yf_headers["Accept"] = "application/json"
    for label, sym in (mcfg.get("yahoo") or {}).items():
        try:
            r = requests.get(f"{yf_base}{sym}", timeout=10, headers=yf_headers,
                             params={"range": "5d", "interval": "1d"})
            r.raise_for_status()
            res = (r.json().get("chart", {}).get("result") or [None])[0]
            meta = res.get("meta", {}) if res else {}
            price = meta.get("regularMarketPrice")
            # previousClose = prior session close. chartPreviousClose = close before the
            # requested RANGE begins (~5 sessions back at range=5d) — using it labels a
            # multi-day move as a daily one. Prior session first, range-close as fallback.
            prev = meta.get("previousClose") or meta.get("chartPreviousClose")
            if price is not None and prev:
                rows.append({"label": label, "value": f"{price:,.2f}",
                             "chg": (price - prev) / prev * 100})
            elif price is not None:
                rows.append({"label": label, "value": f"{price:,.2f}", "chg": None})
            else:
                rows.append({"label": label, "value": "unavailable", "chg": None})
        except Exception:
            rows.append({"label": label, "value": "unavailable", "chg": None})
    cg_ids = mcfg.get("coingecko") or {}
    if cg_ids:
        try:
            r = requests.get(mcfg.get("coingecko_base",
                             "https://api.coingecko.com/api/v3/simple/price"),
                             params={"ids": ",".join(cg_ids.values()),
                                     "vs_currencies": "usd",
                                     "include_24hr_change": "true"}, timeout=10)
            r.raise_for_status()
            data = r.json()
            for label, cid in cg_ids.items():
                d = data.get(cid) or {}
                if "usd" in d:
                    rows.append({"label": label, "value": f"${d['usd']:,.0f}",
                                 "chg": d.get("usd_24h_change")})
        except Exception:
            rows.append({"label": "crypto", "value": "unavailable", "chg": None})
    return rows


def fetch_kev(config: dict, hours: int) -> list:
    if not config.get("kev_enabled", True):
        return []
    url = config.get("kev_url",
                     "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json")
    try:
        r = requests.get(url, timeout=15, headers=UA)
        r.raise_for_status()
        cutoff = (datetime.now(timezone.utc) - timedelta(days=max(1, hours // 24))).date()
        out = []
        for v in r.json().get("vulnerabilities", []):
            try:
                added = datetime.strptime(v.get("dateAdded", ""), "%Y-%m-%d").date()
            except ValueError:
                continue
            if added >= cutoff:
                out.append(v)
        out.sort(key=lambda v: v.get("dateAdded", ""), reverse=True)
        return out
    except Exception:
        return []


# ----------------------------------------------------------------------
# html rendering (dark dashboard)
# ----------------------------------------------------------------------

HTML_CSS = """
@import url('fonts/fonts.css');
:root{
  --field:#080B0F; --panel:#10141A; --panel2:#151A22; --panel3:#1A2029;
  --line:#222A34; --line2:#2E3844; --fg:#C2CAD3; --fg2:#EDF2F7; --dim:#6A7580;
  --brass:#C29B45; --brass2:#DCB55F; --green:#4E9E71; --red:#C05149;
  --blue:#7195B5; --crow:#9AA4B0; --ink:#8D97A2;
  --bg:var(--field); --amber:var(--brass); --amber2:var(--brass2); --redglow:var(--red);
  --brass3:#8A6E30; --steel:#7A97B4;
}

/* ===== GEOMETRIC FOG FIELD (matches landing) ===== */
.field-bg{position:fixed; inset:0; z-index:-2; background:var(--field);
  background-image:
    linear-gradient(135deg, transparent 0%, rgba(20,26,35,.55) 50%, transparent 100%),
    radial-gradient(80% 50% at 50% -5%, rgba(184,147,63,.055), transparent 60%)}
.facets{position:fixed; inset:0; z-index:-1; pointer-events:none; opacity:.42}
.facets svg{width:100%; height:100%; display:block}
.grain{position:fixed; inset:0; z-index:-1; pointer-events:none; opacity:.022;
  background-image:repeating-linear-gradient(0deg,#fff 0 1px,transparent 1px 3px)}

/* ===== PERSISTENT DESK NAV (every interior page) ===== */
.desknav{position:sticky; top:0; z-index:60; background:rgba(8,10,13,.86);
  backdrop-filter:blur(10px); border-bottom:1px solid var(--line)}
.desknav-in{max-width:900px; margin:0 auto; padding:.6rem 1.25rem; display:flex; align-items:center; gap:1rem}
.desknav .home{display:flex; align-items:center; gap:.6rem; margin-right:auto}
.desknav .home img{width:26px; height:auto; display:block; filter:drop-shadow(0 1px 4px rgba(0,0,0,.6))}
.desknav .home span{font-family:'IBM Plex Mono',monospace; font-size:.66rem; font-weight:600;
  letter-spacing:.26em; color:var(--fg2); text-transform:uppercase; white-space:nowrap}
.desknav .dn-links{display:flex; gap:1rem; align-items:center; flex-wrap:wrap; justify-content:flex-end}
.desknav .dn-links a{font-family:'IBM Plex Mono',monospace; font-size:.64rem; font-weight:500;
  letter-spacing:.14em; color:var(--dim); text-transform:uppercase; padding:.2rem 0; border-bottom:2px solid transparent}
.desknav .dn-links a:hover{color:var(--fg2)}
.desknav .dn-links a.here{color:var(--brass2); border-bottom-color:var(--brass)}
.desknav .dn-links a.cta-min{color:var(--brass2); border:1px solid var(--line2); padding:.28rem .6rem;
  clip-path:polygon(7px 0,100% 0,100% calc(100% - 7px),calc(100% - 7px) 100%,0 100%,0 7px)}
.desknav .dn-links a.cta-min:hover{border-color:var(--brass)}
body{position:relative}
*{box-sizing:border-box}
html{background:var(--field)}
body{
  background:var(--field); color:var(--fg); margin:0; padding:0;
  font:15.5px/1.65 'IBM Plex Sans','Segoe UI',system-ui,sans-serif;
  -webkit-font-smoothing:antialiased; text-rendering:optimizeLegibility;
}
main{max-width:900px; margin:0 auto; padding:0 1.25rem 4rem}

/* ---- LETTERHEAD ---- */
.letterhead{padding:1.8rem 0 0; margin-bottom:1.5rem}
.classbar{
  font-family:'IBM Plex Mono',monospace; font-size:.66rem; font-weight:600;
  letter-spacing:.34em; color:var(--brass); text-transform:uppercase;
  display:flex; justify-content:space-between; align-items:baseline; gap:1rem;
  padding:.55rem .2rem; margin-bottom:1.7rem;
  border-top:1px solid var(--line2); border-bottom:1px solid var(--line2);
}
.classbar .dtg{color:var(--fg2); letter-spacing:.18em}
.classbar .live{color:var(--fg2); letter-spacing:.18em}
.crest{display:flex; align-items:center; gap:1.5rem;
  padding-bottom:1.5rem; border-bottom:1px solid var(--line2)}
.crow-mark{width:180px; height:auto; flex-shrink:0}
.crest-text{display:flex; flex-direction:column; gap:.2rem; flex:1}
.crest-org{font-family:'IBM Plex Mono',monospace; font-size:.7rem; font-weight:600;
  letter-spacing:.32em; color:var(--crow); text-transform:uppercase}
.crest-title{margin:0; font-family:'Spectral',Georgia,serif; font-size:1.65rem; font-weight:600;
  color:var(--fg2); letter-spacing:.01em; line-height:1.15; margin:.15rem 0}
.crest-line{font-family:'IBM Plex Mono',monospace; font-size:.72rem; color:var(--brass2);
  letter-spacing:.06em; font-weight:500}
.crest-motto{font-family:'Spectral',serif; font-style:italic; font-size:.86rem;
  color:var(--ink); margin-top:.5rem; line-height:1.55}

/* ---- DASHBOARD TILES ---- */
.dash{display:grid; grid-template-columns:repeat(4,1fr); gap:.6rem; margin:1.4rem 0 1.6rem}
.tile{position:relative; background:var(--panel); border:1px solid var(--line);
  padding:.75rem .9rem .65rem; transition:border-color .15s, transform .15s;
  clip-path:polygon(0 0,100% 0,100% calc(100% - 10px),calc(100% - 10px) 100%,0 100%)}
.tile::before{content:"";position:absolute;top:0;left:0;width:2px;height:100%;background:var(--brass3)}
.tile:hover{border-color:var(--line2); transform:translateY(-1px)}
.tile.alert::before{background:var(--red)}
.tile.alert{border-top-color:var(--red)}
.tile-k{font-family:'IBM Plex Mono',monospace; font-size:.6rem; letter-spacing:.16em;
  color:var(--dim); text-transform:uppercase}
.tile-v{font-family:'IBM Plex Mono',monospace; font-variant-numeric:tabular-nums;
  font-size:1.35rem; font-weight:700; color:var(--fg2); line-height:1.2; margin-top:.28rem}
.tile-v.amber{color:var(--brass2)} .tile-v.red{color:var(--red)} .tile-v.green{color:var(--green)}
.tile-s{font-family:'IBM Plex Mono',monospace; font-size:.62rem; color:var(--dim); margin-top:.12rem}
@media(max-width:640px){.dash{grid-template-columns:repeat(2,1fr)} .crow-mark{width:110px}
  .crest{gap:1rem} .crest-title{font-size:1.28rem}}

/* ---- HEADINGS ---- */
h1{display:none}
h2{font-family:'IBM Plex Mono',monospace; font-size:.8rem; font-weight:700;
  color:var(--brass2); letter-spacing:.24em; text-transform:uppercase;
  margin:2.7rem 0 1rem; padding-bottom:.55rem;
  border-bottom:1px solid var(--line2)}
p{margin:.6rem 0; color:var(--fg)}
.meta{color:var(--dim); font-family:'IBM Plex Mono',monospace; font-size:.74rem;
  letter-spacing:.02em; line-height:1.75; padding:.6rem .9rem;
  background:var(--panel); border:1px solid var(--line); margin:.4rem 0 1rem}
a{color:var(--blue); text-decoration:none}
a:hover{color:var(--brass2); text-decoration:underline; text-underline-offset:2px}
strong{color:var(--fg2); font-weight:600}
em{color:var(--ink); font-style:italic}

/* ---- DUAL VOICE ---- */
.synthesis{font-family:'IBM Plex Mono',monospace; font-size:.82rem; line-height:1.7;
  background:var(--panel); border:1px solid var(--line); border-left:2px solid var(--blue);
  padding:.8rem 1rem; margin:.7rem 0; color:var(--fg)}
ol,ul{padding-left:1.5rem} li{margin:.48rem 0; padding-left:.2rem}
ol li::marker{color:var(--brass); font-family:'IBM Plex Mono',monospace; font-weight:700}
ul li::marker{color:var(--dim)}

/* ---- WARNINGS ---- */
blockquote{margin:.6rem 0; padding:.55rem .95rem;
  background:rgba(192,81,73,.08); border-left:2px solid var(--red);
  color:var(--fg); font-size:.8rem; font-family:'IBM Plex Mono',monospace;
  letter-spacing:.02em}

/* ---- TABLES ---- */
.secnav{display:flex;gap:.5rem;overflow-x:auto;-webkit-overflow-scrolling:touch;padding:.5rem 0 .6rem;margin:0 0 1rem;border-bottom:1px solid var(--line)}.secnav a{flex:0 0 auto;font:600 .66rem var(--mono);letter-spacing:.1em;color:var(--dim);text-decoration:none;border:1px solid var(--line);padding:.28rem .55rem;text-transform:uppercase;scroll-margin-top:1rem}.secnav a:hover{color:var(--brass);border-color:var(--brass)}.pmk{font:600 .6rem var(--mono);letter-spacing:.14em;color:var(--dim);margin-right:.55rem;vertical-align:middle}.snum{font-family:var(--mono);color:var(--brass);margin-right:.45rem}.stop{float:right;font-size:.68rem;color:var(--dim);text-decoration:none}.stop:hover{color:var(--brass)}h2{scroll-margin-top:1.2rem}.tablewrap{overflow-x:auto; -webkit-overflow-scrolling:touch; margin:1rem 0}
.tablewrap table{margin:0}
table{border-collapse:collapse; min-width:100%; width:max-content; font-size:.79rem;
  font-family:'IBM Plex Mono',monospace; font-variant-numeric:tabular-nums;
  margin:1rem 0; border:1px solid var(--line2)}
th,td{border-bottom:1px solid var(--line); padding:.5rem .75rem;
  text-align:left; vertical-align:top}
th{background:var(--panel2); color:var(--brass); text-transform:uppercase;
  letter-spacing:.13em; font-size:.64rem; font-weight:700;
  border-bottom:1px solid var(--line2)}
td{color:var(--fg)}
tr:nth-child(even) td{background:rgba(255,255,255,.012)}

.corr{color:var(--brass2); font-weight:600}
.single{color:var(--dim); font-style:italic}
hr{border:0; height:1px; background:var(--line2); margin:2.6rem 0}

.footbar{margin-top:3rem; padding:.55rem .2rem;
  border-top:1px solid var(--line2); border-bottom:1px solid var(--line2);
  font-family:'IBM Plex Mono',monospace; font-size:.66rem; letter-spacing:.34em;
  color:var(--brass); text-transform:uppercase; text-align:center}
.colophon{font-family:'Spectral',serif; font-style:italic; font-size:.82rem;
  color:var(--ink); text-align:center; margin-top:.9rem; line-height:1.65}
.discl{display:block; margin-top:.7rem; font-family:'IBM Plex Mono',monospace;
  font-style:normal; font-size:.68rem; line-height:1.7; color:var(--dim)}
.byline{font-family:'IBM Plex Mono',monospace; font-size:.68rem; letter-spacing:.14em;
  color:var(--crow); text-align:center; margin-top:.6rem; text-transform:uppercase}

/* ---- TABS ---- */
.tabbar{display:flex; flex-wrap:wrap; gap:.15rem; margin:0 0 1.6rem;
  padding:0; background:transparent; border-bottom:1px solid var(--line2);
  position:sticky; top:41px; z-index:20; background:rgba(8,10,13,.92); backdrop-filter:blur(8px)}
.tab{font-family:'IBM Plex Mono',monospace; font-size:.72rem; font-weight:600;
  letter-spacing:.12em; text-transform:uppercase; color:var(--dim);
  background:transparent; border:0; border-bottom:2px solid transparent;
  padding:.6rem .85rem; cursor:pointer; transition:color .15s, border-color .15s}
.tab:hover{color:var(--fg2)}
.tab.active{color:var(--fg2); border-bottom-color:var(--brass)}
.pane{display:none; opacity:0; transform:translateY(4px)}
.pane.active{display:block; animation:paneIn .28s ease forwards}
@keyframes paneIn{to{opacity:1; transform:none}}
@media(prefers-reduced-motion:reduce){.pane.active{animation:none; opacity:1; transform:none}}
.pane h2:first-child{margin-top:.5rem}

/* ---- PRINT: the working paper ---- */
@media print{
  :root{--field:#fff; --panel:#fff; --panel2:#f2f2f2; --panel3:#eee;
    --line:#999; --line2:#333; --fg:#111; --fg2:#000; --dim:#444;
    --brass:#000; --brass2:#000; --green:#1c5c3c; --red:#7a1f1f;
    --blue:#00358a; --crow:#222; --ink:#333}
  body{background:#fff; font-size:11pt}
  .tabbar{display:none}
  .pane{display:block !important}
  .crow-mark{width:110px}
  a{color:var(--blue); text-decoration:none}
  .tile{border:1px solid #333; border-top:2px solid #000}
  table,th,td{border-color:#333}
}
"""

# The crow mark — the real Nebelkrähe crest, embedded.
CROW_SVG = '''<img class="crow-mark" alt="Nebelkr&auml;he" src="crow_mark.svg"/>'''


def md_inline(text: str) -> str:
    t = html.escape(text, quote=False)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank">\1</a>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", t)
    t = re.sub(r"(\d+)× corroborated", r'<span class="corr">\1× corroborated</span>', t)
    t = re.sub(r"(\d+)×(?= \()", r'<span class="corr">\1×</span>', t)
    t = t.replace("(single-source)", '<span class="single">(single-source)</span>')
    return t


def _render_md_body(md: str) -> str:
    """Render a markdown fragment to HTML (no page chrome). Returns inner HTML."""
    lines = md.split("\n")
    out, i = [], 0
    in_ol = in_ul = False

    def close_lists():
        nonlocal in_ol, in_ul
        if in_ol:
            out.append("</ol>"); in_ol = False
        if in_ul:
            out.append("</ul>"); in_ul = False

    while i < len(lines):
        line = lines[i]
        if line.startswith("| ") and i + 1 < len(lines) and set(lines[i + 1].replace("|", "").strip()) <= set("- "):
            close_lists()
            headers = [c.strip() for c in line.strip("|").split("|")]
            out.append("<div class='tablewrap'><table><thead><tr>" +
                       "".join(f"<th>{md_inline(h)}</th>" for h in headers) +
                       "</tr></thead><tbody>")
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip("|").split("|")]
                out.append("<tr>" + "".join(f"<td>{md_inline(c)}</td>" for c in cells) + "</tr>")
                i += 1
            out.append("</tbody></table></div>")
            continue
        if line.startswith("# "):
            close_lists(); out.append(f"<h1>{md_inline(line[2:])}</h1>")
        elif line.startswith("### "):
            close_lists(); out.append(f"<h3>{md_inline(line[4:])}</h3>")
        elif line.startswith("## "):
            close_lists(); out.append(f"<h2>{md_inline(line[3:])}</h2>")
        elif line.startswith("> "):
            close_lists(); out.append(f"<blockquote>{md_inline(line[2:])}</blockquote>")
        elif re.match(r"^\d+\.\s", line):
            if not in_ol:
                close_lists(); out.append("<ol>"); in_ol = True
            out.append(f"<li>{md_inline(re.sub(r'^\\d+\\.\\s', '', line))}</li>")
        elif line.startswith("- "):
            if not in_ul:
                close_lists(); out.append("<ul>"); in_ul = True
            out.append(f"<li>{md_inline(line[2:])}</li>")
        elif line.strip() == "---":
            close_lists(); out.append("<hr>")
        elif line.strip() == "":
            close_lists()
        else:
            close_lists()
            # dual-voice: model synthesis (KJ, WATCH, OUTLOOK, We assess…) render as Claude voice
            _l = line.lstrip()
            is_synth = bool(re.match(r"^(KJ\d|WATCH:|OUTLOOK:|We assess|I&W:)", _l)) or \
                       _l.startswith("We ")
            if line.startswith("Window:"):
                cls = ' class="meta"'
            elif is_synth:
                cls = ' class="synthesis"'
            else:
                cls = ""
            out.append(f"<p{cls}>{md_inline(line)}</p>")
        i += 1
    close_lists()
    return "".join(out)


# ---- section grouping into dashboard + tabs ----
_TAB_MAP = [
    # (tab label, [section-title keywords that belong in this tab])
    ("Command", ["KEY JUDGMENTS", "INDICATIONS", "PIR STATUS"]),
    ("War Desk", ["WAR DESK"]),
    ("Markets", ["MARKET"]),
    ("Convergence", ["CONVERGENCE"]),
    ("Cyber", ["KEV", "CYBER"]),
    ("Threats", ["NWS", "MILITARY", "DISASTER"]),
    ("Politics", ["POLITICAL", "ECONOMIC"]),
    ("Record", ["APPENDIX"]),
]


def _split_sections(md: str):
    """Split a report's markdown into (heading, body_md) sections on '## ' lines.
    The preamble (before first ##) is returned separately."""
    parts = re.split(r"(?m)^(##\s+.+)$", md)
    preamble = parts[0]
    secs = []
    for j in range(1, len(parts), 2):
        heading = parts[j].strip()
        body = parts[j + 1] if j + 1 < len(parts) else ""
        secs.append((heading, body))
    return preamble, secs



def _intel_sections(inner: str, scope: str) -> str:
    """Pane-scoped sectioning: jump chips, ids, portion marks, numbering."""
    import re as _re
    h2s = _re.findall(r"<h2>(.*?)</h2>", inner, _re.DOTALL)
    if len(h2s) < 3:
        return inner
    chips, box = [], {"i": 0}
    def _repl(m):
        box["i"] += 1
        i = box["i"]
        title = m.group(1)
        sid = f"{scope}_h{i:02d}"
        plain = _re.sub(r"<[^>]+>", "", title).strip()[:26]
        chips.append(f"<a href='#{sid}'>{i:02d} · {plain}</a>")
        return (f"<h2 id='{sid}'><span class='pmk'>(U//OS)</span>"
                f"<span class='snum'>{i:02d}.</span> {title}"
                f"<a class='stop' href='#{scope}_nav'>\u25b2</a></h2>")
    inner = _re.sub(r"<h2>(.*?)</h2>", _repl, inner, flags=_re.DOTALL)
    nav = f"<nav class='secnav' id='{scope}_nav'>" + "".join(chips) + "</nav>"
    return nav + inner



def render_html(md: str, title: str) -> str:
    # ---- letterhead + dashboard data ----
    dtg_m = re.search(r"—\s*(\d{6}Z\s+\w{3}\s+\d{2})", md)
    dtg = dtg_m.group(1) if dtg_m else datetime.now(timezone.utc).strftime("%d%H%MZ %b %y").upper()
    is_ledger = "LEDGER" in title.upper() or "KKR" in title.upper()
    doc_kind = "PREDICTIVE LEDGER" if is_ledger else "DAILY INTELLIGENCE REPORT"

    def _grab(pat, default="—"):
        m = re.search(pat, md); return m.group(1) if m else default
    stories = _grab(r"→\s*([\d,]+)\s+stories")
    newc = _grab(r"\*\*(\d+)\s+new\*\*")
    conv_terms = re.findall(r"→ .+\((\d+) stories\)", md)
    conv_n = str(len(conv_terms)) if conv_terms else "—"
    kev_hits = re.findall(r"\*\*CVE-", md)
    kev_n = str(len(kev_hits)) if "KEV" in md else "0"
    mk = re.search(r"\|\s*(?:S&P 500|Brent|Gold)\s*\|\s*([\d,\.]+)\s*\|\s*([+-][\d\.]+%)", md)
    mk_txt = mk.group(2) if mk else "—"
    mk_cls = "green" if mk and mk.group(2).startswith("+") else ("red" if mk else "")

    tiles = ""
    if not is_ledger:
        tiles = (
            f"<div class='dash'>"
            f"<div class='tile'><div class='tile-k'>Stories</div>"
            f"<div class='tile-v amber'>{stories}</div><div class='tile-s'>{newc} new this window</div></div>"
            f"<div class='tile'><div class='tile-k'>Convergence</div>"
            f"<div class='tile-v'>{conv_n}</div><div class='tile-s'>cross-category terms</div></div>"
            f"<div class='tile {'alert' if kev_n not in ('0','—') else ''}'><div class='tile-k'>KEV Exploited</div>"
            f"<div class='tile-v {'red' if kev_n not in ('0','—') else ''}'>{kev_n}</div><div class='tile-s'>new CVEs in window</div></div>"
            f"<div class='tile'><div class='tile-k'>Market Pulse</div>"
            f"<div class='tile-v {mk_cls}'>{mk_txt}</div><div class='tile-s'>lead index move</div></div>"
            f"</div>")

    letterhead = (
        f"<div class='letterhead'>"
        f"<div class='classbar'><span>▲ NOTHING CLASSIFIED OR PRIVILEGED</span>"
        f"<span class='dtg'>{dtg}</span></div>"
        f"<div class='crest'>{CROW_SVG}<div class='crest-text'>"
        f"<div class='crest-org'>NEBELKRÄHE · OSINT DESK</div>"
        f"<h1 class='crest-title'>THE PRESCIENT DESK\u2122 · {doc_kind}</h1>"
        f"<div class='crest-line'>Forecasts kept on the record</div>"
        f"<div class='crest-motto'>Calling our shots in the fog. Soaring through our misses.</div>"
        f"</div></div>{tiles}</div>")

    footer = (
        "<div class='footbar'>▲ NOTHING CLASSIFIED OR PRIVILEGED</div>"
        "<div class='byline'>NEBELKRÄHE · THE PRESCIENT DESK</div>"
        "<div class='legalline' style='font-size:.72rem;opacity:.7;margin:.2rem 0 .5rem'><a href='terms.html'>Terms</a> · <a href='privacy.html'>Privacy</a></div>"
        "<div class='colophon'>Machine-collated open-source intelligence. Every synthesized "
        "claim traces to the record; the record traces to source. Grades are mechanical, "
        "not judgment. A ledger that keeps its own misses.<br>"
        "<span class='discl'>Method disclosure: collation, corroboration grading, and "
        "convergence detection are deterministic code. Category synthesis is model-drafted "
        "under citation audit; uncited sentences are flagged in place, not removed. "
        "Resolution and publication are the operator's.</span></div>")

    # ---- ledgers render linear (no tabs); reports render tabbed ----
    _, sections = _split_sections(md)
    if is_ledger or len(sections) < 4:
        body = _render_md_body(re.sub(r"(?m)^#\s+.+$", "", md))  # strip H1, keep rest
        page = f"{letterhead}{_intel_sections(body, 's')}{footer}"
    else:
        # assign each section to a tab bucket
        buckets = {label: [] for label, _ in _TAB_MAP}
        other = []
        for heading, sec_body in sections:
            htitle = heading.lstrip("# ").upper()
            placed = False
            for label, keys in _TAB_MAP:
                if any(k in htitle for k in keys):
                    buckets[label].append((heading, sec_body)); placed = True; break
            if not placed:
                other.append((heading, sec_body))
        if other:
            buckets.setdefault("More", []).extend(other)

        tabs_html, panes_html, first = [], [], True
        for label, _ in _TAB_MAP + [("More", [])]:
            secs = buckets.get(label) or []
            if not secs:
                continue
            tid = "tab_" + re.sub(r"\W+", "", label).lower()
            tabs_html.append(
                f"<button class='tab{' active' if first else ''}' onclick=\"netzTab('{tid}',this)\">{label}</button>")
            inner = "".join(f"<h2>{md_inline(h.lstrip('# '))}</h2>{_render_md_body(b)}"
                             for h, b in secs)
            inner = _intel_sections(inner, tid)
            panes_html.append(
                f"<div class='pane{' active' if first else ''}' id='{tid}'>{inner}</div>")
            first = False

        tabbar = "<div class='tabbar'>" + "".join(tabs_html) + "</div>"
        panes = "".join(panes_html)
        page = f"{letterhead}{tabbar}<div class='panes'>{panes}</div>{footer}"

    tabjs = """<script>
function netzTab(id, btn){
  document.querySelectorAll('.pane').forEach(function(p){p.classList.remove('active')});
  document.querySelectorAll('.tab').forEach(function(t){t.classList.remove('active')});
  var el=document.getElementById(id); if(el){ el.classList.add('active'); }
  if(btn) btn.classList.add('active');
  var tb=document.querySelector('.tabbar');
  if(tb && tb.getBoundingClientRect().top < 0){ tb.scrollIntoView({behavior:'smooth',block:'start'}); }
}
</script>"""

    tu = title.upper()
    if "LEDGER" in tu:
        h_ledger, h_kkr, h_report = "here", "", ""
    elif "KKR" in tu or "FORECAST" in tu:
        h_ledger, h_kkr, h_report = "", "here", ""
    else:
        h_ledger, h_kkr, h_report = "", "", "here"
    desknav = ("""<nav class="desknav"><div class="desknav-in"><a class="home" href="index.html"><img src="crow_mark.svg" alt=""><span>Nebelkr&auml;he</span></a><div class="dn-links"><a href="index.html">Desk</a><a class="{H_report}" href="report.html">Report</a><a class="{H_ledger}" href="ledger.html">Ledger</a><a class="{H_kkr}" href="kkr.html">Forecasts</a><a href="kraehes_kalls.html">Kalls</a><a href="KriegForeKaster.html">ForeKaster</a><a href="okk.html">OKK</a><a href="standards.html">Standards</a><a href="conformance.html">Conformance</a><a href="verify.html">Verify</a><a href="register.html">Register</a><a href="KriegForeKaster_compendium.html">Compendium</a><a href="ohrwurm.html">Ohrwurm</a><a href="spion.html">Spion</a><a href="fogsim.html">FogSim</a><a href="nest.html">Nest</a><a href="marks.html">Marks</a><a href="konsole.html">Konsole</a><a href="https://github.com/OccultusTheoretician/netz">GitHub</a></div></div></nav>""").replace("{H_report}",h_report).replace("{H_ledger}",h_ledger).replace("{H_kkr}",h_kkr)
    fog = ("""<div class="field-bg"></div><div class="facets"><svg viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="fg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#B8933F" stop-opacity=".10"/><stop offset="1" stop-color="#7A97B4" stop-opacity=".04"/></linearGradient></defs><g stroke="#28313D" stroke-width="1" fill="none" opacity=".6"><path d="M0,180 L360,90 L720,220 L1080,110 L1440,240"/><path d="M0,420 L300,520 L640,400 L980,540 L1440,430"/><path d="M0,680 L380,760 L760,640 L1120,780 L1440,660"/><path d="M360,90 L300,520 M720,220 L640,400 M1080,110 L980,540"/></g><g fill="url(#fg)" opacity=".5"><polygon points="360,90 720,220 640,400 300,520"/><polygon points="1080,110 1440,240 1440,430 980,540"/><polygon points="0,680 380,760 300,520 0,420"/></g></svg></div><div class="grain"></div>""")
    # ---- per-page meta: description and og tags -------------------------
    # Page identity comes from the nav "here" markers computed just above,
    # not from a second test on the title string. One signal, one source of
    # truth: if the nav is right, the canonical URL is right.
    if h_ledger == "here":
        _slug = "ledger.html"
        _desc = ("The permanent record: every projection ever sealed, resolved "
                 "or open, hits and misses alike, segregated by the forecaster "
                 "arm that issued it.")
    elif h_kkr == "here":
        _slug = "kkr.html"
        _desc = ("The Kaos Kontrol Report: falsifiable projections elicited from "
                 "a named forecaster arm, passed through a mechanical gate that "
                 "publishes its rejections, and sealed before any outcome exists.")
    else:
        _slug = "report.html"
        _desc = ("Machine-collated open-source intelligence. Every synthesised "
                 "claim traces to the record; the record traces to source.")
    _site = "https://retroprescientaudit.com"
    _ttl = html.escape(title)
    # og_nebelkraehe.png is lowercase on purpose - Pages is case-sensitive and
    # a capital K here once broke every link preview on the site.
    _meta = (
        f'<meta name="description" content="{_desc}">'
        f'<meta property="og:title" content="{_ttl} &middot; The Prescient Desk">'
        f'<meta property="og:description" content="{_desc}">'
        f'<meta property="og:image" content="{_site}/og_nebelkraehe.png">'
        f'<meta property="og:url" content="{_site}/{_slug}">'
        f'<meta property="og:type" content="website">'
        f'<meta name="twitter:card" content="summary_large_image">'
    )
    # Structured data: tells a crawler what this page IS. Without it a
    # search for the desk's own name surfaces unrelated audit firms.
    _jsonld = (
        '<script type="application/ld+json">{"@context":"https://schema.org",'
        '"@type":"WebPage","name":"' + _ttl + '",'
        '"description":"' + _desc.replace('"', "'") + '",'
        '"url":"' + _site + '/' + _slug + '",'
        '"isPartOf":{"@type":"WebSite","name":"Retro-Prescient Audit",'
        '"url":"' + _site + '"},'
        '"publisher":{"@type":"Organization","name":"The Prescient Desk"}}'
        '</script>'
    )
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'>"
            f"<meta name='viewport' content='width=device-width,initial-scale=1'>"
            f"<link rel='icon' type='image/svg+xml' href='crow_mark.svg'>"
            f"<link rel='stylesheet' href='brand.css'>"
            f"<script defer src='brand.js'></script>"
            f"<link rel='apple-touch-icon' href='apple-touch-icon.png'>"
            f"<link rel='canonical' href='{_site}/{_slug}'>"
            f"<title>{html.escape(title)} · Nebelkrähe</title>{_meta}"
            f"{_jsonld}<style>{HTML_CSS}</style></head>"
            f"<body>{fog}{desknav}<main>{page}</main>{tabjs}<script src='kontrols.js' defer></script></body></html>")


def open_in_browser(path: Path):
    try:
        if platform.system() == "Windows":
            os.startfile(path)  # noqa: S606
        elif platform.system() == "Darwin":
            subprocess.run(["open", str(path)], check=False)
        else:
            webbrowser.open(path.as_uri())
    except Exception:
        pass


# ----------------------------------------------------------------------
# report
# ----------------------------------------------------------------------

# --- published-surface headline policy (patch_pub_title) ---------------------
# The full title is kept everywhere internally: clustering, dedup, the LLM packet
# and cite_audit all read it. Only PUBLISHED surfaces shorten it, and each keeps
# its link, so the record stays checkable. See UK NLA v Meltwater and EU DSM
# Article 15 — the carve-out there covers "very short extracts", and a complete
# headline is not obviously one. This shortens the reproduction, not the evidence.
PUB_TITLE_WORDS = 10


def pub_title(t, n: int = PUB_TITLE_WORDS) -> str:
    w = str(t or "").split()
    return " ".join(w) if len(w) <= n else " ".join(w[:n]) + " \u2026"
# ----------------------------------------------------------------------------


def fmt_when(dt) -> str:
    return dt.strftime("%d %b %H:%M UTC") if dt else "undated"


def age_hours(dt) -> str:
    if not dt:
        return "—"
    h = (datetime.now(timezone.utc) - dt).total_seconds() / 3600
    return f"{h:.1f}h"




WARDESK_FILE = HERE / "forecasts" / "WARDESK_latest.md"


def war_desk_body(hours: int) -> str:
    """Body of the WAR DESK section, produced by tg_grade.py (Module 3).

    Freshness is a publication gate: a desk older than the report window is
    withheld and SAID to be withheld. An absent pull prints as an absent pull.
    """
    if not WARDESK_FILE.exists():
        return ("*No WAR DESK run on record. The Telegram cross-bias pipeline has not "
                "produced a graded file — section reports empty rather than omitted.*\n")
    age = (datetime.now(timezone.utc).timestamp() - WARDESK_FILE.stat().st_mtime) / 3600
    if age > hours:
        return (f"*Last cross-bias pull ran {age:.1f}h ago, outside this {hours}h report "
                f"window. The stale desk is withheld rather than passed off as current.*\n")
    body = WARDESK_FILE.read_text(encoding="utf-8")
    lines = body.split("\n")
    if lines and lines[0].startswith("## "):   # heading re-issued below with the numeral
        lines = lines[1:]
    return "\n".join(lines).strip() + "\n"


def render_report(config, clusters, conv, health, synth, model_used, hours, counts,
                  markets_data, kevs, nws_alerts, pirs) -> str:
    now = datetime.now(timezone.utc)
    rel_map = config.get("source_reliability", {})
    dtg = now.strftime("%d%H%MZ %b %y").upper()
    n_new = sum(1 for c in clusters if c.get("is_new", True))
    sec = iter(["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
                "XI", "XII", "XIII", "XIV", "XV", "XVI"])
    out = []
    out.append("**NOTHING CLASSIFIED OR PRIVILEGED**\n")
    out.append(f"# THE PRESCIENT DESK\u2122 — DAILY INTELLIGENCE REPORT — {dtg}\n")
    synth_line = f"synthesis: {model_used}" if model_used else "synthesis: OFF — collation only"
    out.append(f"Window: last {hours}h · {counts['fetched']} items → {counts['stories']} stories "
               f"(**{n_new} new**, {counts['stories'] - n_new} ongoing) · {synth_line} · "
               f"grades: Admiralty A-F × 1-6 · 🆕 new today, ↺Dn = day n of coverage\n")

    top = sorted(clusters, key=lambda c: (-c["corroboration"],
                 -(c["newest"].timestamp() if c["newest"] else 0)))[:config.get("top_signals", 8)]

    out.append(f"## {next(sec)}. KEY JUDGMENTS\n")
    if synth.get("bluf"):
        out.append(synth["bluf"] + "\n")
        for w in synth.get("bluf_warnings", []):
            out.append(f"> ⚠ {w}\n")
    else:
        out.append("*Synthesis layer off — top signals listed without analytic judgments.*\n")
    out.append("**Top signals (the record behind the judgments):**\n")
    for n, cl in enumerate(top, 1):
        rep = cl["rep"]
        out.append(f"{n}. {delta_mark(cl)} **[{admiralty_grade(cl, rel_map)}] {pub_title(rep['title'])}** — "
                   f"{cl['corroboration']}× corroborated ({', '.join(cl['sources'])}), "
                   f"{fmt_when(cl['newest'])} · [{cl['category']}] · [link]({rep['link']})")
    out.append("")

    out.append(f"## {next(sec)}. INDICATIONS & WARNINGS\n")
    if synth.get("iw"):
        out.append(synth["iw"] + "\n")
        for w in synth.get("iw_warnings", []):
            out.append(f"> ⚠ {w}\n")
    else:
        out.append("*Synthesis layer off — no I&W block this run.*")
    out.append("")

    out.append(f"## {next(sec)}. WAR DESK — CROSS-BIAS CONFIRMED EVENTS\n")
    out.append(war_desk_body(hours))
    out.append("")

    out.append(f"## {next(sec)}. PIR STATUS\n")
    if pirs:
        for p in pirs:
            out.append(f"**PIR: {p['pir']}**\n")
            if p["hits"]:
                for cl in p["hits"]:
                    out.append(f"- {delta_mark(cl)} [{admiralty_grade(cl, rel_map)}] "
                               f"{pub_title(cl['rep']['title'])} · [link]({cl['rep']['link']})")
            else:
                out.append("- No collection against this requirement this window.")
            out.append("")
    else:
        out.append("No PIRs defined — add standing questions to `pirs` in config.")
        out.append("")

    out.append(f"## {next(sec)}. MARKET SNAPSHOT\n")
    if markets_data:
        out.append("*Machine-read quotes, prior-session close as reference. These figures "
                   "govern: any price stated in a synthesis above is a claim from the record "
                   "and is subject to the citation audit.*\n")
        out.append("| instrument | last | Δ vs prior close |")
        out.append("|---|---|---|")
        for m in markets_data:
            chg = f"{m['chg']:+.2f}%" if m["chg"] is not None else "—"
            out.append(f"| {m['label']} | {m['value']} | {chg} |")
    else:
        out.append("Market feeds unavailable this run.")
    out.append("")

    out.append(f"## {next(sec)}. CONVERGENCE WATCH\n")
    if conv:
        out.append("Terms surfacing across independent categories this window "
                   "(deterministic — token co-occurrence, not model inference):\n")
        for term, cats, hits in conv:
            out.append(f"- **{term}** → {', '.join(cats)} ({hits} stories)")
    else:
        out.append("No cross-category term convergence above threshold this window.")
    out.append("")

    out.append(f"## {next(sec)}. NWS SEVERE ALERTS (US)\n")
    if nws_alerts:
        counts_by = {}
        for a in nws_alerts:
            counts_by[a["event"]] = counts_by.get(a["event"], 0) + 1
        out.append("Active Extreme/Severe: " +
                   ", ".join(f"**{k}** ×{v}" for k, v in
                             sorted(counts_by.items(), key=lambda x: -x[1])) + "\n")
        for a in nws_alerts[:8]:
            out.append(f"- **{a['event']}** ({a['severity']}) — {a['area']}")
    else:
        out.append("No active Extreme/Severe alerts (or endpoint unreachable — "
                   "grade accordingly).")
    out.append("")

    out.append(f"## {next(sec)}. CISA KEV — NEWLY CATALOGUED EXPLOITED VULNERABILITIES\n")
    if kevs:
        for v in kevs[:15]:
            out.append(f"- **{v.get('cveID','?')}** — {v.get('vendorProject','')} "
                       f"{v.get('product','')}: {v.get('vulnerabilityName','')} "
                       f"(added {v.get('dateAdded','')}). "
                       f"{v.get('shortDescription','')[:180]}")
    else:
        out.append("No new KEV entries in window (or catalog unreachable — grade accordingly).")
    out.append("")

    by_cat = {}
    for cl in clusters:
        by_cat.setdefault(cl["category"], []).append(cl)
    for cat, cls in sorted(by_cat.items()):
        cls.sort(key=lambda c: (-c["corroboration"],
                 -(c["newest"].timestamp() if c["newest"] else 0)))
        out.append(f"## {next(sec)}. {cat.upper()}\n")
        s = synth.get(cat)
        if s:
            out.append("**Synthesis** *(machine-drafted; every sentence cites the record below — "
                       "uncited claims are flagged, not trusted)*:\n")
            out.append(s["text"] + "\n")
            for w in s["warnings"]:
                out.append(f"> ⚠ **CITATION AUDIT** — {w}. Flag published deliberately: "
                           f"this desk shows its own unverified seams rather than "
                           f"quietly deleting them.\n")
        out.append("**The record:**\n")
        for n, cl in enumerate(cls[:config.get("max_items_per_category", 25)], 1):
            rep = cl["rep"]
            corr = f" · {cl['corroboration']}× ({', '.join(cl['sources'])})" \
                if cl["corroboration"] > 1 else f" · {cl['sources'][0]} (single-source)"
            out.append(f"{n}. {delta_mark(cl)} [{admiralty_grade(cl, rel_map)}] "
                       f"{pub_title(rep['title'])}{corr} · {fmt_when(cl['newest'])} · [link]({rep['link']})")
        out.append("")

    out.append("## APPENDIX — FEED HEALTH\n")
    out.append("| feed | category | status | items | newest |")
    out.append("|---|---|---|---|---|")
    for h in health:
        status = h["status"] if h["status"] == "ok" else f"**{h['status']}**"
        out.append(f"| {h['source']} | {h['category']} | {status} | {h['count']} | "
                   f"{age_hours(h['newest'])} |")
    dead = [h for h in health if h["status"] != "ok"]
    if dead:
        out.append("\nDead/degraded feeds this run: " +
                   ", ".join(f"{h['source']} ({h['error'][:60]})" for h in dead))
    out.append(f"\n---\n**NOTHING CLASSIFIED OR PRIVILEGED**\n\n*The Prescient Desk\u2122 · engine NETZ v2.0 · every synthesized "
               f"claim must trace to the record; the record traces to source links; the links "
               f"are the audit trail. Admiralty grades are mechanical (feed tier × "
               f"corroboration), not analyst judgment.*")
    return "\n".join(out)


# ----------------------------------------------------------------------
# main
# ----------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="NETZ v2.0 — local auto-collation intelligence report")
    ap.add_argument("--config", default=DEFAULT_CONFIG)
    ap.add_argument("--hours", type=int, default=None)
    ap.add_argument("--no-llm", action="store_true")
    ap.add_argument("--out", default=None)
    ap.add_argument("--open", action="store_true")
    args = ap.parse_args()

    config = load_config(args.config)
    hours = args.hours or config.get("window_hours", 24)

    print(f"NETZ · fetching {sum(len(v) for v in config['categories'].values())} feeds …",
          file=sys.stderr)
    items, health = fetch_all(config)
    items.extend(fetch_reliefweb(config, health))
    windowed = window_filter(items, hours)
    clusters = cluster_items(windowed, config.get("cluster_threshold", 0.45))
    mark_delta(clusters)
    conv = convergence(clusters)
    # --- content classification + PIR routing (patch_netz_classify) ---------
    # Category arrived from the feed table, not from the item. Al Jazeera, BBC
    # World, DW and Defense One were all hardcoded military_conflict, which put
    # an All-Ireland final and a death at 81 in the same bucket as an airstrike,
    # and Top Signals ranked inside that bucket. reclassify() overrides the
    # category from content and keeps the feed's opinion at cl["feed_category"].
    # Every override is written to classify_log.json with the rule that fired.
    import classify
    classify.reclassify(clusters)
    pirs = pir_status(config, clusters)
    # PIRs printed "no collection" on a day the record carried a chokepoint
    # de-escalation and a surprise central-bank tightening. route_pirs fills
    # only requirements that came back empty; anything matched upstream stands.
    pirs = classify.route_pirs(config, clusters, pirs)
    # ------------------------------------------------------------------------
    counts = {"fetched": len(items), "windowed": len(windowed), "stories": len(clusters)}
    print(f"NETZ · {counts['fetched']} fetched → {counts['windowed']} in window → "
          f"{counts['stories']} stories "
          f"({sum(1 for c in clusters if c.get('is_new', True))} new)", file=sys.stderr)

    synth, model_used = {}, None
    if not args.no_llm:
        base = config.get("lmstudio_base_url", "http://localhost:1234/v1")
        model_used = config.get("lmstudio_model") or llm_probe(base)
        if model_used:
            print(f"NETZ · synthesis via {model_used}", file=sys.stderr)
            pir_note = ""
            if config.get("pirs"):
                pir_note = "\nStanding requirements (PIRs):\n" + \
                           "\n".join(f"- {p}" for p in config["pirs"])
            by_cat = {}
            for cl in clusters:
                by_cat.setdefault(cl["category"], []).append(cl)
            for cat, cls in by_cat.items():
                cls.sort(key=lambda c: (-c["corroboration"],
                         -(c["newest"].timestamp() if c["newest"] else 0)))
                numbered, chosen = number_items(cls, config.get("llm_items_per_category", 20))
                text = llm_chat(base, model_used, SYSTEM_PROMPT,
                                f"Category: {cat}{pir_note}\nItems:\n{numbered}")
                if text:
                    text, warnings = audit_citations(text, len(chosen))
                    synth[cat] = {"text": text, "warnings": warnings}
            top = sorted(clusters, key=lambda c: (-c["corroboration"],
                         -(c["newest"].timestamp() if c["newest"] else 0)))
            numbered, chosen = number_items(top, config.get("top_signals", 8))
            bluf = llm_chat(base, model_used, BLUF_PROMPT, f"Top signals:\n{numbered}")
            if bluf:
                bluf, bw = audit_citations(bluf, len(chosen))
                synth["bluf"], synth["bluf_warnings"] = bluf, bw
            iw = llm_chat(base, model_used, IW_PROMPT, f"Top signals:\n{numbered}",
                          max_tokens=700)
            if iw:
                iw, iww = audit_citations(iw, len(chosen))
                synth["iw"], synth["iw_warnings"] = iw, iww
        else:
            print("NETZ · no model loaded at LM Studio endpoint — collation only",
                  file=sys.stderr)

    markets_data = fetch_markets(config)
    kevs = fetch_kev(config, hours)
    nws_alerts = fetch_nws(config)
    print(f"NETZ · markets: {len(markets_data)} · KEV: {len(kevs)} new · "
          f"NWS severe: {len(nws_alerts)}", file=sys.stderr)

    report = render_report(config, clusters, conv, health, synth, model_used, hours,
                           counts, markets_data, kevs, nws_alerts, pirs)

    out_dir = Path(args.out or config.get("output_dir", "reports"))
    if not out_dir.is_absolute():
        out_dir = HERE / out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M")
    out_path = out_dir / f"battle_report_{stamp}.md"
    out_path.write_text(report, encoding="utf-8")
    html_doc = render_html(report, f"The Prescient Desk \u2014 Report {stamp}")
    html_path = out_dir / f"battle_report_{stamp}.html"
    html_path.write_text(html_doc, encoding="utf-8")
    (out_dir / "latest.html").write_text(html_doc, encoding="utf-8")
    print(f"NETZ · report → {out_path}", file=sys.stderr)
    print(f"NETZ · html   → {html_path} (+ latest.html)", file=sys.stderr)
    if args.open:
        open_in_browser(html_path)
    print(out_path)


if __name__ == "__main__":
    main()
