#!/usr/bin/env python3
"""warte.py - KALIBRIERWARTE. The multi-model calibration observatory.

KK17 frontier bank, completed KK36. Reads the sealed ledger and renders
per-arm calibration: reliability bins, Brier, base rate, climatological
floor, skill - one tile per forecaster arm, no pooled figure anywhere
(a Brier belongs to one forecaster). VoidSection doctrine: trend under a
FROZEN rubric is the measurement, so every tile prints its rubric-hash
coverage - rows sealed before the commitment carry no hash and say so.

Writes forecasts/kalibrierwarte_latest.json and docs/kalibrierwarte.html.
Read-only against the ledger. n-floors are printed, never hidden.
"""
import json, sys, hashlib
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict

HERE = Path(__file__).resolve().parent
N_FLOOR_ARM = 10   # below this, the tile says so and shows no skill line
N_FLOOR_BIN = 5    # below this, the bin prints n<5 instead of a frequency
BINS = [(0,10),(10,20),(20,30),(30,40),(40,50),
        (50,60),(60,70),(70,80),(80,90),(90,101)]


def main():
    led = json.loads((HERE/"ledger.json").read_text(encoding="utf-8"))
    rows = led["projections"]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    _ledger_sha16 = hashlib.sha256((HERE/"ledger.json").read_bytes().replace(b"\r\n", b"\n")).hexdigest()[:16]  # SHELL-WARTE-2026-09-06
    # KK27C-WARTE: era split. A Brier belongs to one forecaster, and an era
    # boundary marks a different forecaster: the Rueckkopplungsverbot cut
    # lmstudio/auto into three. Pooling them under one tile would violate
    # the desk's own law inside the instrument built to enforce it. Reuses
    # arms.json eras and kkr's own bucketing rule - same boundaries, same
    # date_issued comparison, no second source of truth.
    try:
        _reg = {a["tag"]: a for a in json.loads(
            (HERE / "arms.json").read_text(encoding="utf-8-sig"))["arms"]}
    except Exception:
        _reg = {}
    # KK27D: keyless rows whose citations the integrity audit found
    # defective. A keyless determination says the claim went beyond its
    # declared priors; where those priors are unreadable the determination
    # was made against nothing, and the number is stated with its defect
    # rate attached rather than as a clean integer.
    defective = set()
    try:
        _ci = json.loads((HERE / "cite_integrity_latest.json")
                         .read_text(encoding="utf-8"))
        # DEFECTIVE only: reproduces the audit's own keyless_defective
        # figure exactly (10 of 86 at 2026-08-09). NO_CITES is a separate
        # verdict the audit does not fold in, so neither does this.
        defective = {r["id"] for r in _ci.get("rows", [])
                     if str(r.get("verdict", "")).upper() == "DEFECTIVE"}
    except Exception:
        pass

    arms = defaultdict(list)
    # KK31-B14: an era with rows issued and nothing resolved is a hole the
    # observatory discloses, not a tile that silently does not exist. Every
    # row buckets (not only resolved ones) so issued/open exist per era,
    # and every registered era of a tag present in the ledger gets a
    # bucket even at zero resolved.
    issuedc = defaultdict(int)
    openc = defaultdict(int)
    seen_tags = set()

    def _bucket_of(p):
        tag = str(p.get("model", "?"))
        eras = _reg.get(tag, {}).get("eras")
        bucket = tag
        if eras:
            d = str(p.get("date_issued") or "")
            for e in eras:
                if e.get("until") and d and d < e["until"]:
                    bucket = tag + "[" + e["id"] + "]"
                    break
                if e.get("from") and d and d >= e["from"]:
                    bucket = tag + "[" + e["id"] + "]"
        return tag, bucket

    for p in rows:
        tag, bucket = _bucket_of(p)
        seen_tags.add(tag)
        issuedc[bucket] += 1
        if p.get("status") == "open":
            openc[bucket] += 1
        if p.get("status") not in ("hit", "miss"):
            continue
        arms[bucket].append(p)
    for tag in sorted(seen_tags):
        for e in (_reg.get(tag, {}).get("eras") or []):
            arms.setdefault(tag + "[" + e["id"] + "]", [])
    open_hash = sum(1 for p in rows if p.get("status")=="open"
                    and p.get("rubric_hash"))
    open_all = sum(1 for p in rows if p.get("status")=="open")

    tiles = {}
    for arm in sorted(arms):
        rs = arms[arm]
        n = len(rs)
        if n == 0:
            tiles[arm] = {
                "resolved": 0, "issued": issuedc.get(arm, 0),
                "open": openc.get(arm, 0), "hits": 0, "misses": 0,
                "zero_state": (f"era registered - {issuedc.get(arm, 0)} "
                               f"issued, {openc.get(arm, 0)} open, nothing "
                               f"resolved yet. Printed rather than omitted; "
                               f"a hole the register discloses."),
                "bins": []}
            continue
        hits = sum(1 for p in rs if p["status"]=="hit")
        ps = [float(p.get("probability",0))/100.0 for p in rs]
        ys = [1.0 if p["status"]=="hit" else 0.0 for p in rs]
        brier = sum((a-b)**2 for a,b in zip(ps,ys))/n
        base = hits/n
        clim = base*(1-base)
        skill = None if clim==0 else 1.0-(brier/clim)
        hashed = sum(1 for p in rs if p.get("rubric_hash"))
        bins = []
        for lo,hi in BINS:
            sub = [(a,b) for a,b in zip(ps,ys) if lo <= a*100 < hi]
            if not sub:
                continue
            bn = len(sub)
            bins.append({
                "bin": f"{lo}-{hi-1 if hi==101 else hi}",
                "n": bn,
                "mean_p": round(sum(a for a,_ in sub)/bn, 3),
                "obs": (round(sum(b for _,b in sub)/bn, 3)
                        if bn >= N_FLOOR_BIN else None),
                "note": None if bn >= N_FLOOR_BIN else f"n<{N_FLOOR_BIN}"})
        # KK27D: the split. A Brier over KEYED rows scores arithmetic - the
        # outcome was deducible from the forecaster's own declared priors.
        # A Brier over KEYLESS rows scores foresight. The desk's whole claim
        # lives in the second number and nowhere else, so it is computed
        # separately, floored separately, and carries its own citation
        # defect rate: a keyless call made against unreadable priors was
        # made against nothing.
        split = {}
        for lab in ("keyed", "keyless"):
            sub = [p for p in rs
                   if str(p.get("keyed_keyless", "")).strip().lower() == lab]
            if not sub:
                split[lab] = {"resolved": 0, "note": "no resolved rows"}
                continue
            sn = len(sub); sh = sum(1 for p in sub if p["status"] == "hit")
            sp = [float(p.get("probability", 0))/100.0 for p in sub]
            sy = [1.0 if p["status"] == "hit" else 0.0 for p in sub]
            sb = sum((a-b)**2 for a, b in zip(sp, sy))/sn
            sbase = sh/sn
            sclim = sbase*(1-sbase)
            split[lab] = {
                "resolved": sn, "hits": sh, "misses": sn-sh,
                "brier": round(sb, 3), "base_rate": round(sbase, 3),
                "climatological": round(sclim, 3),
                "skill": (round(1.0-(sb/sclim), 3)
                          if sclim and sn >= N_FLOOR_ARM else None),
                "note": (None if sn >= N_FLOOR_ARM else
                         f"n<{N_FLOOR_ARM} - printed, not hidden"),
                "defect_ids": sorted(defective & {p["id"] for p in sub})}
        undet = sum(1 for p in rs if str(p.get("keyed_keyless", "")).strip()
                    .lower() not in ("keyed", "keyless"))
        tiles[arm] = {
            "resolved": n, "issued": issuedc.get(arm, n),
            "open": openc.get(arm, 0), "hits": hits, "misses": n-hits,
            "split": split, "undetermined": undet,
            "brier": round(brier,3), "base_rate": round(base,3),
            "climatological": round(clim,3),
            "skill": (round(skill,3) if skill is not None
                      and n >= N_FLOOR_ARM else None),
            "n_floor": (None if n >= N_FLOOR_ARM else
                        f"insufficient n ({n}<{N_FLOOR_ARM}) - "
                        f"printed, not hidden"),
            "rubric_hashed": hashed,
            "rubric_note": (None if hashed == n else
                            f"{n-hashed} of {n} resolved rows predate the "
                            f"rubric commitment - drift comparison anchors "
                            f"at the first hashed row"),
            "bins": bins}

    out = {"_meta": {"generated": now, "instrument": "kalibrierwarte/1.0",
                     "doctrine": "no pooled score exists; a Brier belongs "
                                 "to one forecaster; trend under a frozen "
                                 "rubric is the measurement",
                     "n_floor_arm": N_FLOOR_ARM, "n_floor_bin": N_FLOOR_BIN,
                     "open_rows_rubric_hashed": f"{open_hash}/{open_all}"},
           "arms": tiles}
    fj = HERE/"forecasts"/"kalibrierwarte_latest.json"
    fj.parent.mkdir(exist_ok=True)
    fj.write_text(json.dumps(out, indent=1)+"\n", encoding="utf-8")

    h = ["<!doctype html><html lang='en'><head><meta charset='utf-8'>",
         "<title>KALIBRIERWARTE</title>",
         "<meta name='description' content='The multi-model calibration observatory: per-arm reliability against its own base rates.'>",
         "<meta property='og:image' content='https://retroprescientaudit.com/og_nebelkraehe.png'>",
         "<meta name='viewport' content='width=device-width,initial-scale=1'>",
         "<link rel='stylesheet' href='fonts/fonts.css'>",
         "<link rel='stylesheet' href='brand.css'>",
         "<link rel='stylesheet' href='instrument.css'>",  # SHELL-WARTE-2026-09-06
         "<script defer src='instrument.js'></script>",
         "<style>body{background:#0c0e11;color:#d6d3cb;"
         "font-family:'IBM Plex Sans',sans-serif;max-width:900px;"
         "margin:0 auto;padding:0 1.25rem 3rem;font-size:15px;line-height:1.6}"
         ".kicker{font:500 .8rem 'IBM Plex Mono',monospace;"
         "letter-spacing:.06em;text-transform:uppercase;color:#8b8b85;"
         "margin-top:2.4rem}"
         "h1{color:#f2f0ea}"
         "table{border-collapse:collapse;margin:10px 0;"
         "font-family:'IBM Plex Mono',monospace;font-size:12.5px}"
         "td,th{border:1px solid #26292f;padding:4px 10px;text-align:right}"
         "th{color:#8b8b85;font-weight:600}.note{color:#8b8b85;max-width:46rem}"
         ".warn{color:#c9a227}"
         "</style></head><body>",
         # SHELL-WARTE-2026-09-06: the face is a workpaper (INSTRUMENT_SHELL.md)
         "<h1>Kalibrierwarte</h1>",
         "<section class='wp'>",
         "<aside class='wp-index'>",
         f"<p class='wp-ref'>W/P WARTE<small>kalibrierwarte/1.0 &middot; generated {now}</small></p>",
         "<p class='wp-purpose'>Calibration per arm, read from the sealed ledger. No pooled "
         "score exists; a Brier belongs to one forecaster. These tiles are descriptive and "
         "print the noise line under the floors; the only scores this desk claims come from "
         "the registered estimators at an arm's first checkpoint.</p>",
         "</aside>",
         "<aside class='wp-prov'>",
         "<dl class='wp-meta'>",
         f"<dt>Source of record</dt><dd><a href='ledger.json'><code>ledger.json</code></a>, "
         f"sha256 (LF) <code>{_ledger_sha16}</code> at render</dd>",
         "<dt>This page reads</dt><dd>the sealed ledger only; it writes "
         "<code>forecasts/kalibrierwarte_latest.json</code> beside this face</dd>",
         "<dt>Prepared by</dt><dd><code>warte.py</code>, unattended, at every seal and every chain run</dd>",
         "<dt>Governed by</dt><dd><a href='KALIBRIERWARTE_REGISTERED_REPORT_v3.md'>the registration</a>, "
         "Sections 13 and 14: hypotheses, floors and quality checks are fixed there, and any "
         "confirmatory figure comes from <code>warte_report.py</code> at 50 resolved within one cohort</dd>",
         "</dl>",
         "<details class='wp-howto'><summary>How to read this</summary>",
         "<p>Reliability is mean stated probability against observed frequency per decile; a "
         "decile with fewer than five resolved rows prints its count and no frequency. Under ten "
         "resolved an arm's skill is not printed; under thirty the tile is noise and says so.</p>",
         "<p>A Brier over KEYED rows scores arithmetic - the outcome was deducible from the "
         "forecaster's own declared priors. A Brier over KEYLESS rows scores foresight. Only the "
         "second bears on any claim this desk makes, and it carries its citation-defect count: a "
         "keyless call made against unreadable priors was made against nothing.</p>",
         f"<p>Rows sealed before the rubric commitment carry no hash and are marked. Open rows "
         f"carrying a rubric hash: {open_hash}/{open_all}.</p>",
         "</details>",
         "</aside>",
         "<div class='wp-body'>"]
    for arm, t in tiles.items():
        h.append(f"<h2>{arm}</h2>")
        if t.get("zero_state"):
            h.append(f"<p class='warn'>{t['zero_state']}</p>")
            continue
        h.append(f"<p>issued {t.get('issued', t['resolved'])} - open "
                 f"{t.get('open', 0)} - "
                 f"resolved {t['resolved']} - {t['hits']} hit / "
                 f"{t['misses']} miss - Brier {t['brier']} - base rate "
                 f"{t['base_rate']} - climatological {t['climatological']}"
                 + (f" - skill {t['skill']}" if t['skill'] is not None
                    else "") + "</p>")
        if t["n_floor"]:
            h.append(f"<p class='warn'>{t['n_floor']}</p>")
        if t["rubric_note"]:
            h.append(f"<p class='note'>{t['rubric_note']}</p>")
        sp = t.get("split", {})
        h.append("<table><tr><th>class</th><th>n</th><th>hits</th>"
                 "<th>Brier</th><th>skill</th><th>note</th></tr>")
        for lab in ("keyed", "keyless"):
            d = sp.get(lab, {})
            if not d.get("resolved"):
                h.append(f"<tr><td>{lab}</td><td>0</td><td>-</td><td>-</td>"
                         f"<td>-</td><td class='note'>no resolved rows</td>"
                         f"</tr>")
                continue
            nt = d.get("note") or ""
            if d.get("defect_ids"):
                nt += (("; " if nt else "")
                       + f"{len(d['defect_ids'])} row(s) with defective "
                         f"citations")
            h.append(f"<tr><td>{lab}</td><td>{d['resolved']}</td>"
                     f"<td>{d['hits']}</td><td>{d['brier']}</td>"
                     f"<td>{d['skill'] if d['skill'] is not None else '-'}"
                     f"</td><td class='note'>{nt}</td></tr>")
        if t.get("undetermined"):
            h.append(f"<tr><td>undetermined</td><td>{t['undetermined']}</td>"
                     f"<td colspan='4' class='warn'>resolved with no "
                     f"determination - KEYED by rule (RPAS 4.03)</td></tr>")
        h.append("</table>")
        h.append("<table><tr><th>bin</th><th>n</th><th>mean p</th>"
                 "<th>observed</th></tr>")
        for b in t["bins"]:
            obs = b["note"] if b["obs"] is None else f"{b['obs']}"
            h.append(f"<tr><td>{b['bin']}</td><td>{b['n']}</td>"
                     f"<td>{b['mean_p']}</td><td>{obs}</td></tr>")
        h.append("</table>")
    # SHELL-WARTE-2026-09-06: re-performance footer and receipt
    h.append("</div>")
    h.append("<footer class='wp-reperform'><h2>Re-performance</h2>"
             "<p>Every tile above recomputes from the record; nothing here is asserted that you cannot reproduce.</p>"
             "<ol>"
             "<li>Clone the repository: <code>git clone https://github.com/OccultusTheoretician/netz.git</code></li>"
             "<li><code>python warte.py</code> regenerates this face and <code>forecasts/kalibrierwarte_latest.json</code> "
             "from <code>ledger.json</code>; hash the record with line endings normalised to LF and compare with the receipt below.</li>"
             "<li><code>python warte_report.py</code> runs the registered estimators report-only: bootstrap intervals, "
             "the seat re-cut and the quality checks, reading hypotheses only for an arm at 50 resolved within one cohort. "
             "The registration pins that script's hash in Section 13.</li>"
             "<li>The rules governing every read are in the registration; a failed quality check halts the read, and the halt stands.</li>"
             "</ol>"
             f"<div class='wp-receipt'>ledger.json sha256 (LF), first 16: <code id='wp-receipt' data-value='{_ledger_sha16}'>{_ledger_sha16}</code>"
             "<button class='wp-copy' type='button' data-copy='#wp-receipt'>copy</button></div>"
             "<p class='wp-signoff'>kalibrierwarte/1.0 - read-only against the sealed ledger - misses printed at full size. "
             "Prepared by the generator; the operator adjudicates at the weekly sitting and does not edit sealed rows.</p>"
             "</footer></section></body></html>")
    fh = HERE/"docs"/"kalibrierwarte.html"
    fh.write_text("\n".join(h), encoding="utf-8")
    print(f"WARTE - {len(tiles)} arm tile(s) - {sum(t['resolved'] for t in tiles.values())} resolved rows read", file=sys.stderr)
    print(f"WARTE - json -> {fj}", file=sys.stderr)
    print(f"WARTE - face -> {fh}", file=sys.stderr)


if __name__ == "__main__":
    main()
