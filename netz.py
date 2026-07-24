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
)

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
)

IW_PROMPT = (
    "You are an OSINT analyst. From the numbered top signals below, produce the "
    "INDICATIONS & WARNINGS and OUTLOOK blocks of a daily intelligence report. "
    "Format exactly:\nI&W:\n1. <one concrete observable to monitor in the next "
    "24-72h, tied to escalation or de-escalation, with citation [n]>\n2. ...\n"
    "(3 to 6 numbered lines)\nOUTLOOK:\n<one 60-90 word paragraph, standardized "
    "estimative language, every sentence cited [n]>\n"
    "Work ONLY from the items given. Observables must be checkable from public "
    "reporting (a statement, a closure, a price level, an advisory), never vague."
)


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
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=Spectral:ital,wght@0,500;0,600;1,400&display=swap');
:root{
  --field:#0B0D10; --panel:#10141A; --panel2:#151A22; --panel3:#1A2029;
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
.crest-title{font-family:'Spectral',Georgia,serif; font-size:1.65rem; font-weight:600;
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
table{border-collapse:collapse; width:100%; font-size:.79rem;
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
CROW_SVG = '''<img class="crow-mark" alt="Nebelkrähe" src="data:image/png;base64,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"/>'''


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
            out.append("<table><thead><tr>" +
                       "".join(f"<th>{md_inline(h)}</th>" for h in headers) +
                       "</tr></thead><tbody>")
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip("|").split("|")]
                out.append("<tr>" + "".join(f"<td>{md_inline(c)}</td>" for c in cells) + "</tr>")
                i += 1
            out.append("</tbody></table>")
            continue
        if line.startswith("# "):
            close_lists(); out.append(f"<h1>{md_inline(line[2:])}</h1>")
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
        f"<div class='classbar'><span>▲ UNCLASSIFIED // OPEN SOURCES</span>"
        f"<span class='dtg'>{dtg}</span></div>"
        f"<div class='crest'>{CROW_SVG}<div class='crest-text'>"
        f"<div class='crest-org'>NEBELKRÄHE · OSINT DESK</div>"
        f"<div class='crest-title'>NETZ {doc_kind}</div>"
        f"<div class='crest-line'>The prescient desk · forecasts kept on the record</div>"
        f"<div class='crest-motto'>Calling our shots in the fog. Soaring through our misses.</div>"
        f"</div></div>{tiles}</div>")

    footer = (
        "<div class='footbar'>▲ UNCLASSIFIED // OPEN SOURCES</div>"
        "<div class='byline'>NEBELKRÄHE · THE PRESCIENT DESK</div>"
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
        page = f"{letterhead}{body}{footer}"
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
    desknav = ("""<nav class="desknav"><div class="desknav-in"><a class="home" href="index.html"><img src="crow.png" alt=""><span>Nebelkr&auml;he</span></a><div class="dn-links"><a class="{H_report}" href="report.html">Report</a><a class="{H_ledger}" href="ledger.html">Ledger</a><a class="{H_kkr}" href="kkr.html">Forecasts</a><a href="https://github.com/OccultusTheoretician/netz">GitHub</a><a class="cta-min" href="index.html">Home</a></div></div></nav>""").replace("{H_report}",h_report).replace("{H_ledger}",h_ledger).replace("{H_kkr}",h_kkr)
    fog = ("""<div class="field-bg"></div><div class="facets"><svg viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="fg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#B8933F" stop-opacity=".10"/><stop offset="1" stop-color="#7A97B4" stop-opacity=".04"/></linearGradient></defs><g stroke="#28313D" stroke-width="1" fill="none" opacity=".6"><path d="M0,180 L360,90 L720,220 L1080,110 L1440,240"/><path d="M0,420 L300,520 L640,400 L980,540 L1440,430"/><path d="M0,680 L380,760 L760,640 L1120,780 L1440,660"/><path d="M360,90 L300,520 M720,220 L640,400 M1080,110 L980,540"/></g><g fill="url(#fg)" opacity=".5"><polygon points="360,90 720,220 640,400 300,520"/><polygon points="1080,110 1440,240 1440,430 980,540"/><polygon points="0,680 380,760 300,520 0,420"/></g></svg></div><div class="grain"></div>""")
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'>"
            f"<meta name='viewport' content='width=device-width,initial-scale=1'>"
            f"<link rel='icon' type='image/png' href='crow.png'>"
            f"<title>{html.escape(title)} · Nebelkrähe</title><style>{HTML_CSS}</style></head>"
            f"<body>{fog}{desknav}<main>{page}</main>{tabjs}</body></html>")


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

def fmt_when(dt) -> str:
    return dt.strftime("%d %b %H:%M UTC") if dt else "undated"


def age_hours(dt) -> str:
    if not dt:
        return "—"
    h = (datetime.now(timezone.utc) - dt).total_seconds() / 3600
    return f"{h:.1f}h"


def render_report(config, clusters, conv, health, synth, model_used, hours, counts,
                  markets_data, kevs, nws_alerts, pirs) -> str:
    now = datetime.now(timezone.utc)
    rel_map = config.get("source_reliability", {})
    dtg = now.strftime("%d%H%MZ %b %y").upper()
    n_new = sum(1 for c in clusters if c.get("is_new", True))
    sec = iter(["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
                "XI", "XII", "XIII", "XIV", "XV", "XVI"])
    out = []
    out.append("**UNCLASSIFIED // OPEN SOURCES**\n")
    out.append(f"# NETZ DAILY INTELLIGENCE REPORT — {dtg}\n")
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
        out.append(f"{n}. {delta_mark(cl)} **[{admiralty_grade(cl, rel_map)}] {rep['title']}** — "
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

    out.append(f"## {next(sec)}. PIR STATUS\n")
    if pirs:
        for p in pirs:
            out.append(f"**PIR: {p['pir']}**\n")
            if p["hits"]:
                for cl in p["hits"]:
                    out.append(f"- {delta_mark(cl)} [{admiralty_grade(cl, rel_map)}] "
                               f"{cl['rep']['title']} · [link]({cl['rep']['link']})")
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
                       f"{rep['title']}{corr} · {fmt_when(cl['newest'])} · [link]({rep['link']})")
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
    out.append(f"\n---\n**UNCLASSIFIED // OPEN SOURCES**\n\n*NETZ v2.0 · every synthesized "
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
    pirs = pir_status(config, clusters)
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
    html_doc = render_html(report, f"NETZ Report {stamp}")
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
