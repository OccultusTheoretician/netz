#!/usr/bin/env python3
"""ident_probe.py — the identifier loop. Standing instrument, repo root.

`ident_audit.py` tests CVE tokens in machine-drafted synthesis prose against
the PUBLISHED record, and its own scope limitation is load-bearing: packets
are withheld (KNP 7.04), so UNSOURCED means *not present in the published
record*, not *invented*. This tool closes that gap from the other side: it
probes each UNSOURCED token against the authoritative registries themselves —
CISA KEV, NIST NVD, and MITRE CVE Services — and splits the class.

    python ident_probe.py --dry-run          census + probe plan, no network
    python ident_probe.py --selftest         classifier against canned fixtures
    python ident_probe.py                    live probe (~9s/token, printed)
    python ident_probe.py --limit 3          cautious first run

Verdicts, in precedence order:

    TRUNCATED            format-invalid (fewer than 4 sequence digits) — a
                         synthesis artifact, not an identifier; never probed.
    REAL-EXPLOITED       in the CISA KEV catalog. Implies the rest.
    REAL-RECORDED        published NVD record exists.
    REAL-RECORDED-MITRE  MITRE state PUBLISHED, NVD absent — a real record
                         the NVD enrichment backlog has not caught. Real.
    REAL-RESERVED        MITRE state RESERVED: the ID is assigned to a CNA
                         and no public content exists. The identifier is
                         real; any CLAIM the prose attached to it is still
                         ungrounded, because there is nothing to ground on.
    REJECTED             MITRE state REJECTED.
    ABSENT               404 at MITRE AND absent from NVD — the ID was never
                         assigned. This is the likely-confabulated class: an
                         identifier cited in dated synthesis prose that the
                         issuing authority has no record of ever creating.
    INDETERMINATE        a deciding fetch failed. Fail-open: a fetch that
                         did not run proves nothing, and says so.

Epistemics printed with every report: ABSENT is as-of the probe date; MITRE
assignment is near-immediate on allocation, so ABSENT weeks after the citing
report is strong. RESERVED and RECORDED-MITRE exist precisely because NVD
lags — probing NVD alone would overcount confabulation, which is why MITRE
is the deciding registry and NVD is corroboration.

Rate discipline: KEV is fetched ONCE and membership-checked locally (27
tokens do not need 27 catalog downloads). NVD keyless is 5 requests per 30
seconds — 6.5s between calls. One 429 gets one 35-second wait and one retry,
printed; a single rate-limit is not a finding (the GDELT lesson).

Outputs: `evidence/ident_probe_<stamp>.json` (full, gitignored per the KK23
evidence ruling), `ident_probe_latest.json` at root (pointer — unguarded by
runguard doctrine), and `IDENT_PROBE_<date>.md` through
`runguard.write_run_artifact` (fail-open to a plain write, printed, if the
guard is absent). Writes nothing to the ledger.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) ident_probe/1.0 "
      "(+https://retroprescientaudit.com)")
KEV = ("https://www.cisa.gov/sites/default/files/feeds/"
       "known_exploited_vulnerabilities.json")
NVD = "https://services.nvd.nist.gov/rest/json/cves/2.0"
MITRE = "https://cveawg.mitre.org/api/cve/"

CVE_OK = re.compile(r"^CVE-\d{4}-\d{4,7}$")
NVD_SLEEP = 6.5          # 5 req / 30 s keyless
MITRE_SLEEP = 2.0
TIMEOUT = 45

VERDICTS = ["TRUNCATED", "REAL-EXPLOITED", "REAL-RECORDED",
            "REAL-RECORDED-MITRE", "REAL-RESERVED", "REJECTED",
            "ABSENT", "INDETERMINATE"]


# ---------------------------------------------------------------- fetch

def fetch(url, retry_429=True):
    """Return (body_bytes|None, http_status|None). 404 is an ANSWER for the
    MITRE endpoint, so it returns (None, 404) rather than being an error."""
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT,
                                    context=ssl.create_default_context()) as r:
            return r.read(), r.status
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None, 404
        if e.code == 429 and retry_429:
            print("  429 rate-limited — waiting 35s and retrying once "
                  "(one rate-limit is not a finding)", file=sys.stderr)
            time.sleep(35)
            return fetch(url, retry_429=False)
        print(f"  FETCH FAILED - HTTP {e.code} {e.reason} :: {url}",
              file=sys.stderr)
        return None, e.code
    except Exception as e:
        print(f"  FETCH FAILED - {type(e).__name__}: {e} :: {url}",
              file=sys.stderr)
        return None, None


# ---------------------------------------------------------------- registries

def load_kev():
    """One fetch, local membership map. Returns (index, meta) or (None, {})."""
    body, status = fetch(KEV)
    if body is None:
        return None, {"error": f"kev fetch failed (status {status})"}
    try:
        d = json.loads(body.decode("utf-8"))
    except Exception as e:
        return None, {"error": f"kev parse failed ({type(e).__name__})"}
    idx = {}
    for v in d.get("vulnerabilities", []):
        cid = str(v.get("cveID", "")).upper()
        if cid:
            idx[cid] = {"dateAdded": v.get("dateAdded"),
                        "vendorProject": v.get("vendorProject"),
                        "product": v.get("product")}
    meta = {"catalogVersion": d.get("catalogVersion"),
            "dateReleased": d.get("dateReleased"),
            "entries": len(idx)}
    return idx, meta


def probe_mitre(token):
    """Returns ({'state':..., 'published':...} | 'NOT_FOUND' | None)."""
    body, status = fetch(MITRE + token)
    if status == 404:
        return "NOT_FOUND"
    if body is None:
        return None
    try:
        d = json.loads(body.decode("utf-8", errors="replace"))
        md = d.get("cveMetadata", {}) or {}
        return {"state": str(md.get("state", "")).upper(),
                "datePublished": md.get("datePublished"),
                "dateReserved": md.get("dateReserved"),
                "assigner": md.get("assignerShortName")}
    except Exception:
        return None


def probe_nvd(token):
    """Returns ({'published':..., 'status':...} | 'NOT_FOUND' | None)."""
    url = NVD + "?" + urllib.parse.urlencode({"cveId": token})
    body, status = fetch(url)
    if body is None:
        return None
    try:
        d = json.loads(body.decode("utf-8", errors="replace"))
        vulns = d.get("vulnerabilities", [])
        if not vulns:
            return "NOT_FOUND"
        c = vulns[0].get("cve", {})
        return {"published": c.get("published"),
                "vulnStatus": c.get("vulnStatus"),
                "lastModified": c.get("lastModified")}
    except Exception:
        return None


# ---------------------------------------------------------------- classifier

def classify(token, kev_hit, mitre, nvd):
    """Pure function over probe results — this is what the selftest tests.

    kev_hit: dict|None (None also when KEV itself failed; the caller marks
             that separately in meta and KEV absence alone never decides).
    mitre:   dict | 'NOT_FOUND' | None(fetch failed)
    nvd:     dict | 'NOT_FOUND' | None(fetch failed)
    """
    if not CVE_OK.match(token):
        return "TRUNCATED", ("fewer than 4 sequence digits — a truncation "
                             "artifact of synthesis prose, not an identifier")
    if kev_hit:
        return "REAL-EXPLOITED", (f"CISA KEV entry, dateAdded "
                                  f"{kev_hit.get('dateAdded')} "
                                  f"({kev_hit.get('vendorProject')}/"
                                  f"{kev_hit.get('product')})")
    if isinstance(nvd, dict):
        return "REAL-RECORDED", (f"NVD record, published "
                                 f"{str(nvd.get('published'))[:10]}, "
                                 f"status {nvd.get('vulnStatus')}")
    if isinstance(mitre, dict):
        st = mitre.get("state", "")
        if st == "PUBLISHED":
            return "REAL-RECORDED-MITRE", (
                f"MITRE state PUBLISHED ({str(mitre.get('datePublished'))[:10]}"
                f", assigner {mitre.get('assigner')}) with no NVD record — "
                f"the NVD enrichment lag, not a phantom")
        if st == "RESERVED":
            return "REAL-RESERVED", (
                f"MITRE state RESERVED (reserved "
                f"{str(mitre.get('dateReserved'))[:10]}, assigner "
                f"{mitre.get('assigner')}) — the identifier is real and "
                f"contentless; any claim attached to it is ungrounded")
        if st == "REJECTED":
            return "REJECTED", "MITRE state REJECTED"
        return "INDETERMINATE", f"MITRE returned unrecognized state {st!r}"
    if mitre == "NOT_FOUND" and nvd == "NOT_FOUND":
        return "ABSENT", ("no record at MITRE (the issuing authority) and "
                          "none at NVD — the ID was never assigned; "
                          "likely-confabulated as of the probe date")
    if mitre == "NOT_FOUND" and nvd is None:
        return "ABSENT", ("no record at MITRE, the issuing authority; the "
                          "NVD corroboration fetch failed, but MITRE alone "
                          "decides assignment")
    return "INDETERMINATE", ("a deciding fetch failed — a probe that did "
                             "not run proves nothing")


# ---------------------------------------------------------------- audit join

def load_audit(path):
    d = json.loads(Path(path).read_text(encoding="utf-8"))
    findings = d.get("findings", [])
    sealed = d.get("sealed", [])
    tokens = {}
    for f in findings:
        t = f.get("token", "")
        e = tokens.setdefault(t, {"token": t, "audit_finding": f.get("finding"),
                                  "reports": set(), "sealed_rows": [],
                                  "arms": set()})
        e["reports"].add(f.get("report", ""))
        if f.get("finding") == "MALFORMED":
            e["audit_finding"] = "MALFORMED"
    for s in sealed:
        t = s.get("token", "")
        if t in tokens:
            tokens[t]["sealed_rows"].append(
                {"id": s.get("id"), "arm": s.get("arm"),
                 "status": s.get("status"),
                 "keyed_keyless": s.get("keyed_keyless")})
            if s.get("arm"):
                tokens[t]["arms"].add(s["arm"])
    for e in tokens.values():
        e["reports"] = sorted(e["reports"])
        e["arms"] = sorted(e["arms"])
        dates = [m.group(0) for r in e["reports"]
                 for m in [re.search(r"\d{4}-\d{2}-\d{2}", r)] if m]
        e["first_report_date"] = min(dates) if dates else None
    return d, tokens


# ---------------------------------------------------------------- selftest

def selftest():
    cases = [
        ("CVE-2026-6", None, None, None, "TRUNCATED"),
        ("CVE-2026-63", None, None, None, "TRUNCATED"),
        ("CVE-2026-1234", {"dateAdded": "2026-08-01", "vendorProject": "X",
                           "product": "Y"}, None, None, "REAL-EXPLOITED"),
        ("CVE-2026-1234", None, {"state": "PUBLISHED",
                                 "datePublished": "2026-07-01"},
         {"published": "2026-07-02", "vulnStatus": "Analyzed"},
         "REAL-RECORDED"),
        ("CVE-2026-1234", None, {"state": "PUBLISHED",
                                 "datePublished": "2026-07-01",
                                 "assigner": "mitre"}, "NOT_FOUND",
         "REAL-RECORDED-MITRE"),
        ("CVE-2026-1234", None, {"state": "RESERVED",
                                 "dateReserved": "2026-06-01",
                                 "assigner": "cna"}, "NOT_FOUND",
         "REAL-RESERVED"),
        ("CVE-2026-1234", None, {"state": "REJECTED"}, "NOT_FOUND",
         "REJECTED"),
        ("CVE-2026-99999", None, "NOT_FOUND", "NOT_FOUND", "ABSENT"),
        ("CVE-2026-99999", None, "NOT_FOUND", None, "ABSENT"),
        ("CVE-2026-99999", None, None, "NOT_FOUND", "INDETERMINATE"),
        ("CVE-2026-99999", None, None, None, "INDETERMINATE"),
    ]
    passed = failed = 0
    print("ident_probe selftest (classifier over canned registry results)\n")
    for token, kev, mitre, nvd, want in cases:
        got, why = classify(token, kev, mitre, nvd)
        ok = got == want
        passed += ok
        failed += not ok
        print(f"  [{'PASS' if ok else 'FAIL'}] {token:18} "
              f"expect {want:19} got {got}")
        if not ok:
            print(f"         reason: {why}")
    print(f"\n  {passed} pass - {failed} fail")
    return 1 if failed else 0


# ---------------------------------------------------------------- rendering

def render_md(meta, results):
    by = {}
    for r in results:
        by.setdefault(r["verdict"], []).append(r)
    lines = []
    lines.append(f"# IDENT PROBE — {meta['probed'][:10]}")
    lines.append("")
    lines.append(f"Source audit: `{meta['audit_file']}` "
                 f"(generated {meta['audit_generated']}); "
                 f"{meta['tokens_total']} distinct tokens, "
                 f"{meta['tokens_probed']} probed this run.")
    kevm = meta.get("kev_meta") or {}
    if kevm.get("catalogVersion"):
        lines.append(f"Registries: CISA KEV catalogVersion "
                     f"{kevm['catalogVersion']} "
                     f"({kevm.get('entries')} entries) - NVD 2.0 - "
                     f"MITRE CVE Services.")
    else:
        lines.append(f"Registries: CISA KEV UNAVAILABLE this run "
                     f"({kevm.get('error','?')}) - NVD 2.0 - "
                     f"MITRE CVE Services. KEV absence decided nothing.")
    lines.append("")
    lines.append("The audit's UNSOURCED verdict means *not present in the "
                 "published record* — the packets are withheld (KNP 7.04), "
                 "so the CI cannot ground the identifiers its arms forecast "
                 "about. This probe closes the gap from the registry side. "
                 "ABSENT is as-of the probe date; MITRE assignment is "
                 "near-immediate on allocation, so absence weeks after the "
                 "citing report is strong. RESERVED and RECORDED-MITRE exist "
                 "because NVD lags — MITRE decides assignment, NVD "
                 "corroborates.")
    lines.append("")
    lines.append("| verdict | n | tokens |")
    lines.append("|---|---|---|")
    for v in VERDICTS:
        rs = by.get(v, [])
        if not rs:
            continue
        toks = ", ".join(r["token"] for r in rs)
        lines.append(f"| {v} | {len(rs)} | {toks} |")
    lines.append("")
    lines.append("## Per-token record")
    lines.append("")
    for r in sorted(results, key=lambda x: (VERDICTS.index(x["verdict"]),
                                            x["token"])):
        lines.append(f"### {r['token']} — {r['verdict']}")
        lines.append(f"- {r['reason']}")
        lines.append(f"- first seen in synthesis: "
                     f"{r.get('first_report_date') or '?'} "
                     f"across {len(r.get('reports', []))} report(s)")
        if r.get("sealed_rows"):
            rows = "; ".join(f"{s['id']} ({s['arm']}, "
                             f"{s.get('keyed_keyless') or 'undetermined'})"
                             for s in r["sealed_rows"])
            lines.append(f"- sealed rows citing it: {rows}")
        else:
            lines.append("- reaches no sealed row (synthesis prose only)")
        lines.append("")
    absent = by.get("ABSENT", [])
    if absent:
        arms = sorted({s["arm"] for r in absent
                       for s in r.get("sealed_rows", [])})
        lines.append("## The elicitation finding (data summary; DRAFT tier)")
        lines.append("")
        lines.append(f"{len(absent)} of {meta['tokens_probed']} probed "
                     f"identifiers were never assigned by the issuing "
                     f"authority. Machine-drafted synthesis prose cited "
                     f"CVE identifiers that do not exist, and "
                     f"{sum(1 for r in absent if r.get('sealed_rows'))} of "
                     f"them reached sealed forecast rows"
                     + (f" on arms: {', '.join(arms)}." if arms else "."))
        lines.append("")
        lines.append("This is a measured property of the elicitation "
                     "pipeline, printed rather than tidied. Sealed rows "
                     "stand; the finding enters the record as a new entry.")
    lines.append("")
    lines.append(f"Probe evidence: `evidence/ident_probe_"
                 f"{meta['stamp']}.json` (withheld per the KK23 evidence "
                 f"ruling, available on analyst query).")
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser(description="the identifier loop")
    ap.add_argument("--audit", default=str(HERE / "ident_audit_latest.json"))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--limit", type=int, default=0,
                    help="probe only the first N valid tokens")
    a = ap.parse_args()

    if a.selftest:
        return selftest()

    audit_path = Path(a.audit)
    if not audit_path.exists():
        print(f"ident_probe: {audit_path} not found — run ident_audit first "
              f"or pass --audit", file=sys.stderr)
        return 2
    audit, tokens = load_audit(audit_path)
    entries = sorted(tokens.values(), key=lambda e: e["token"])
    valid = [e for e in entries if CVE_OK.match(e["token"])]
    trunc = [e for e in entries if not CVE_OK.match(e["token"])]

    print(f"ident_probe over {audit_path.name} "
          f"(audit generated {audit.get('generated')})")
    print(f"  {len(entries)} distinct tokens - {len(valid)} probeable - "
          f"{len(trunc)} TRUNCATED (never probed)")
    sealed_n = sum(1 for e in entries if e["sealed_rows"])
    print(f"  {sealed_n} tokens reach sealed rows")

    if a.dry_run:
        est = len(valid) * (NVD_SLEEP + MITRE_SLEEP) + 5
        print(f"  plan: 1 KEV fetch + {len(valid)} MITRE + "
              f"{len(valid)} NVD calls, ~{est:.0f}s at keyless rate")
        for e in entries:
            kind = "TRUNCATED" if not CVE_OK.match(e["token"]) else "probe"
            rows = ",".join(s["id"] for s in e["sealed_rows"]) or "-"
            print(f"    {e['token']:20} {kind:9} first "
                  f"{e['first_report_date'] or '?'}  "
                  f"x{len(e['reports'])} reports  sealed: {rows}")
        return 0

    todo = valid[:a.limit] if a.limit else valid
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d_%H%M")
    print(f"  probing {len(todo)} tokens "
          f"(~{len(todo)*(NVD_SLEEP+MITRE_SLEEP):.0f}s)")

    kev_idx, kev_meta = load_kev()
    if kev_idx is None:
        print("  KEV unavailable this run — KEV absence will decide "
              "nothing (printed in the report)", file=sys.stderr)

    results = []
    for e in trunc:
        v, why = classify(e["token"], None, None, None)
        results.append({**e, "verdict": v, "reason": why,
                        "mitre": None, "nvd": None, "kev": None})
    for i, e in enumerate(todo, 1):
        t = e["token"]
        kev_hit = kev_idx.get(t.upper()) if kev_idx else None
        m = probe_mitre(t)
        time.sleep(MITRE_SLEEP)
        n = None
        if not kev_hit:
            n = probe_nvd(t)
            time.sleep(NVD_SLEEP)
        v, why = classify(t, kev_hit, m, n)
        results.append({**e, "verdict": v, "reason": why,
                        "kev": kev_hit,
                        "mitre": m if isinstance(m, dict) else str(m),
                        "nvd": n if isinstance(n, dict) else str(n)})
        print(f"  [{i:2}/{len(todo)}] {t:20} {v}")

    meta = {"schema": "ident-probe/1.0",
            "probed": dt.datetime.now(dt.timezone.utc)
            .strftime("%Y-%m-%dT%H:%M:%SZ"),
            "stamp": stamp,
            "audit_file": audit_path.name,
            "audit_generated": audit.get("generated"),
            "tokens_total": len(entries),
            "tokens_probed": len(todo),
            "kev_meta": kev_meta,
            "registries": {"kev": KEV, "nvd": NVD, "mitre": MITRE}}

    counts = {}
    for r in results:
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    print("\n  " + " - ".join(f"{k} {v}" for k, v in
                              sorted(counts.items(),
                                     key=lambda kv: VERDICTS.index(kv[0]))))

    ev_dir = HERE / "evidence"
    ev_dir.mkdir(exist_ok=True)
    full = {"meta": meta, "results": results}
    (ev_dir / f"ident_probe_{stamp}.json").write_text(
        json.dumps(full, indent=1, ensure_ascii=False), encoding="utf-8")
    (HERE / "ident_probe_latest.json").write_text(
        json.dumps({"meta": meta,
                    "verdicts": {r["token"]: r["verdict"] for r in results},
                    "counts": counts}, indent=1, ensure_ascii=False),
        encoding="utf-8")

    md = render_md(meta, results)
    md_path = HERE / f"IDENT_PROBE_{stamp[:10]}.md"
    try:
        import runguard
        written = runguard.write_run_artifact(md_path, md, tag="ident_probe")
    except Exception:
        print("  runguard absent — plain write (fail-open, printed)",
              file=sys.stderr)
        written = md_path
        md_path.write_text(md, encoding="utf-8")
    print(f"\n  wrote evidence/ident_probe_{stamp}.json (withheld, KK23)")
    print(f"  wrote ident_probe_latest.json")
    print(f"  wrote {Path(written).name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
