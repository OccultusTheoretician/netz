#!/usr/bin/env python3
"""
cite_integrity.py — CITATION INTEGRITY AUDIT (RPAS 4.02f, 1.04, 5.04)

WHY THIS EXISTS

    4.02f requires a forecaster's declared priors to be readable. The
    keyed/keyless determination (1.04, the master law) turns on exactly that
    reading: a claim deducible from the cited priors is KEYED; a claim that
    went beyond them is KEYLESS. So the keyless count — the number the desk's
    novelty claim rests on — is only as sound as the citations underneath it.

    The KK18 gate in kkr.py rejects a row only when the union of its cited
    items shares NO substantive vocabulary with the claim. Two failures walk
    straight through it:

      SHOTGUN     cite every item in the report. Overlap with something is
                  then guaranteed, the gate passes, and the declared prior is
                  the entire record — which is the same as declaring none.
                  A prior that excludes nothing predicts nothing.

      THIN        overlap consists only of words common across the whole
                  report ("government", "official", "military"). Shared
                  vocabulary is not shared content. A token that appears in
                  most items discriminates nothing and cannot ground a claim.

    Both manufacture the appearance of a readable prior, and both push the
    keyed/keyless call toward KEYLESS by making the priors look narrower than
    they are. That is the corruption: any system scoring "went beyond its
    inputs" is corruptible by mislabelling the inputs, and nobody scoring that
    way audits the labels.

WHAT IT DOES NOT DO

    It does not edit the ledger. Sealed rows are never edited; a defect found
    after sealing is a printed finding, not a silent substitution. Output is a
    report and a JSON verdict file. Forward enforcement is kkr.py's job.

METHOD (stated so a stranger can recompute it)

    For each row carrying a resolvable source_report:
      1. Parse the report's numbered items.
      2. Compute document frequency of every content word ACROSS THAT
         REPORT's items. Rarity is measured inside the report, not against
         English at large — the discriminating question is whether a token
         separates the cited item from its 24 neighbours.
      3. Score EACH cited item separately against the claim:
           STRONG  shares >=1 content word with df <= DF_RARE_FRAC
           WEAK    shares content words, all of them common in this report
           NONE    shares nothing
      4. Verdict the row.

    Thresholds are printed in every report. They are judgment calls and are
    labelled as such; changing one changes the finding and must be disclosed.

USE
    python cite_integrity.py                      audit ledger.json
    python cite_integrity.py --ledger X.json      audit another record
    python cite_integrity.py --report OUT.md      write the report
    python cite_integrity.py --json OUT.json      write machine verdicts
    python cite_integrity.py --arm lmstudio/auto  restrict to one arm
    python cite_integrity.py --verbose            print every defective row
"""

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---------------------------------------------------------------- thresholds
# Judgment calls. Printed in the report. Change one, disclose it.
DF_RARE_FRAC = 0.25     # token in <=25% of the report's items = discriminating
SHOTGUN_ABS = 8         # citing >=8 items is not citing
SHOTGUN_FRAC = 0.50     # or >=50% of the report record, whichever binds first
DEADWEIGHT_MIN = 3      # only flag deadweight once a row cites at least 3
DEADWEIGHT_FRAC = 0.50  # >50% of cited items contributing nothing

STOP = set("""a an and are as at be been being between by for from had has have
her his in into is it its of on or that the their there these they this to was were
will with within after before during over under more most least than then when where
which who whom whose about above below across against among around because but each
either how if just like near new now only other same since so some such through
until up upon very what while would could should may might must can also per not no
report reports reported reporting confirm confirms confirmed confirming public
statement source sources credible outlet outlets news via data official announce
announced announces announcement said says say state states stated including include
""".split())


def content_words(s: str) -> set:
    """Substantive vocabulary only. Dates, bare numbers and identifier tokens
    are stripped so a shared '2026' or 'CVE' can never read as support.
    Matches kkr._content_words so the two instruments agree on what a word is."""
    out = set()
    for t in re.findall(r"[A-Za-z][A-Za-z'-]{2,}", s.lower()):
        t = t.strip("'-")
        if len(t) < 4 or t in STOP:
            continue
        out.add(t[:-1] if t.endswith("s") and len(t) > 4 else t)
    return out


def tokens_overlap(a: set, b: set) -> set:
    """Overlap tolerant of demonym and adjectival forms. Must stay identical to
    kkr._tokens_overlap: an auditor stricter than the gate it audits reports a
    defect rate the gate would never have produced, which is a stated-versus-
    operational gap on the desk's own masthead."""
    hit = set()
    for x in a:
        for y in b:
            if x == y:
                hit.add(x)
            elif len(x) >= 4 and len(y) >= 4 and (x.startswith(y) or y.startswith(x)):
                hit.add(x)
            else:
                n = 0
                for cx, cy in zip(x, y):
                    if cx != cy:
                        break
                    n += 1
                if n >= 5:
                    hit.add(x)
    return hit


def parse_report(path: Path) -> dict:
    """Numbered items -> {n: [text, ...]}.

    A number may carry SEVERAL texts. Report sections renumbered from 1 before
    KK21, so 25 numbers carried 111 items and a citation resolved to as many as
    twelve stories. That ambiguity is recorded here, not collapsed: a dict keyed
    by int silently keeps whichever line came last, which is what every support
    check this desk ran was doing without saying so."""
    items = {}
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except Exception:
        return items
    for line in lines:
        m = re.match(r"\s*(\d+)\.\s+(.*)", line)
        if m:
            items.setdefault(int(m.group(1)), []).append(
                re.sub(r"\[link\]\(\S+\)", "", m.group(2)))
    return items


def rare_set(items: dict) -> tuple:
    """Content words appearing in <= DF_RARE_FRAC of this report's items."""
    df, total = Counter(), 0
    for texts in items.values():
        for txt in texts:
            total += 1
            for w in content_words(txt):
                df[w] += 1
    cut = max(1, int(max(1, total) * DF_RARE_FRAC))
    return {w for w, c in df.items() if c <= cut}, df, cut


def audit_row(p: dict, items: dict, rare: set) -> dict:
    """Per-item support scoring for one projection."""
    cites = sorted({int(c) for c in (p.get("citations") or [])
                    if str(c).strip().lstrip("-").isdigit() and int(c) > 0})
    claim = content_words(f"{p.get('statement','')} {p.get('resolution','')}")
    per, ambig = {}, 0
    for c in cites:
        cands = items.get(c)
        if not cands:
            per[c] = "MISSING"
            continue
        if len(cands) > 1:
            ambig = max(ambig, len(cands))
        # Charitable resolution: a number that could mean several items is
        # read as its BEST candidate. The gate must never reject on a
        # reference it cannot resolve; the ambiguity is reported separately.
        best = "NONE"
        for txt in cands:
            shared = tokens_overlap(claim, content_words(txt))
            if not shared:
                continue
            if tokens_overlap(shared, rare):
                best = "STRONG"
                break
            best = "WEAK"
        per[c] = best
    vals = list(per.values())
    resolvable = [v for v in vals if v != "MISSING"]

    flags = []
    n_items = max(1, sum(len(v) for v in items.values()))
    if len(cites) >= SHOTGUN_ABS or (items and len(cites) / n_items >= SHOTGUN_FRAC):
        flags.append("SHOTGUN")
    if resolvable and all(v == "NONE" for v in resolvable):
        flags.append("UNSUPPORTED")
    elif resolvable and "STRONG" not in resolvable:
        flags.append("THIN")
    dead = sum(1 for v in resolvable if v == "NONE")
    if (len(resolvable) >= DEADWEIGHT_MIN
            and dead / len(resolvable) > DEADWEIGHT_FRAC
            and "UNSUPPORTED" not in flags):
        flags.append("DEADWEIGHT")
    if not cites:
        flags.append("NO_CITES")
    if ambig > 1:
        flags.append("AMBIGUOUS_REF")

    return {"id": p.get("id"), "arm": p.get("model"),
            "date_issued": p.get("date_issued"),
            "keyed_keyless": (p.get("keyed_keyless") or "").strip().lower() or None,
            "status": p.get("status"), "n_cites": len(cites),
            "report_items": len(items), "per_item": per,
            "strong": sum(1 for v in resolvable if v == "STRONG"),
            "weak": sum(1 for v in resolvable if v == "WEAK"),
            "none": dead,
            "missing": sum(1 for v in vals if v == "MISSING"),
            "max_candidates": ambig, "flags": flags,
            "verdict": _verdict(flags)}


_SOFT = {"NO_CITES", "AMBIGUOUS_REF"}


def _verdict(flags):
    """AMBIGUOUS_REF alone is a defect of the RECORD FORMAT, not of the
    forecaster's citation. It is reported and does not condemn the row."""
    hard = [f for f in flags if f not in _SOFT]
    if hard:
        return "DEFECTIVE"
    if "NO_CITES" in flags:
        return "NO_CITES"
    return "SUPPORTED"


def main():
    ap = argparse.ArgumentParser(description="citation integrity audit (RPAS 4.02f / 1.04)")
    ap.add_argument("--ledger", default=str(HERE / "ledger.json"))
    ap.add_argument("--reports", default=str(HERE / "reports"))
    ap.add_argument("--report", help="write markdown report here")
    ap.add_argument("--json", dest="jsonout", help="write machine verdicts here")
    ap.add_argument("--arm", help="restrict to one arm tag")
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args()

    led = Path(a.ledger)
    if not led.exists():
        sys.exit(f"no ledger at {led}")
    rows = json.loads(led.read_text(encoding="utf-8"))["projections"]
    if a.arm:
        rows = [r for r in rows if r.get("model") == a.arm]

    rdir = Path(a.reports)
    cache = {}
    results, scoped = [], 0
    for p in rows:
        src = (p.get("source_report") or "").strip()
        if not src:
            scoped += 1
            continue
        path = rdir / src
        if not path.exists():
            scoped += 1
            continue
        if src not in cache:
            items = parse_report(path)
            cache[src] = ((items,) + rare_set(items)) if items else None
        if not cache[src]:
            scoped += 1
            continue
        items, rare, _df, _cut = cache[src]
        results.append(audit_row(p, items, rare))

    defective = [r for r in results if r["verdict"] == "DEFECTIVE"]
    flagcount = Counter(f for r in results for f in r["flags"])
    ambiguous = [r for r in results if "AMBIGUOUS_REF" in r["flags"]]

    # The finding that matters: keyless rulings resting on defective citations.
    kl = [r for r in results if r["keyed_keyless"] == "keyless"]
    kl_def = [r for r in kl if r["verdict"] == "DEFECTIVE"]
    by_arm = defaultdict(lambda: [0, 0])
    for r in results:
        by_arm[r["arm"]][0] += 1
        if r["verdict"] == "DEFECTIVE":
            by_arm[r["arm"]][1] += 1

    L = []
    w = L.append
    w("# CITATION INTEGRITY AUDIT")
    w("")
    w(f"Generated {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} "
      f"· ledger `{led.name}` · {len(rows)} rows in scope")
    w("")
    w("Read-only. Sealed rows are never edited; a defect found after sealing is a "
      "printed finding, not a substitution.")
    w("")
    w("## Thresholds (judgment calls — changing one changes the finding)")
    w("")
    w(f"- rare-token cut: document frequency <= {DF_RARE_FRAC:.0%} of the report's items")
    w(f"- shotgun: >= {SHOTGUN_ABS} cited items, or >= {SHOTGUN_FRAC:.0%} of the record")
    w(f"- deadweight: > {DEADWEIGHT_FRAC:.0%} of cited items contributing nothing, "
      f"minimum {DEADWEIGHT_MIN} cites")
    w("")
    w("## Result")
    w("")
    w(f"- rows audited: **{len(results)}**")
    w(f"- scope limitation (no resolvable source report): **{scoped}**")
    w(f"- defective: **{len(defective)}** "
      f"({len(defective)/max(1,len(results)):.1%} of audited)")
    w(f"- rows whose citation number does not identify a unique item: "
      f"**{len(ambiguous)}** "
      f"(max candidates behind one number: "
      f"{max([r['max_candidates'] for r in ambiguous], default=0)})")
    for f, c in flagcount.most_common():
        w(f"  - {f}: {c}")
    w("")
    w("## The number that matters")
    w("")
    w(f"Rows determined **KEYLESS**: {len(kl)}")
    w(f"Of those, citations defective: **{len(kl_def)}** "
      f"({len(kl_def)/max(1,len(kl)):.1%})")
    w("")
    if kl_def:
        w("A keyless determination says the claim went beyond its declared priors. "
          "Where the priors are unreadable, that determination was made against "
          "nothing. These rows are listed so the keyless count can be stated with "
          "its defect rate attached rather than as a clean integer.")
        w("")
        for r in kl_def:
            w(f"- `{r['id']}` · {r['arm']} · {r['date_issued']} · "
              f"{'/'.join(r['flags'])} · {r['n_cites']} cites "
              f"({r['strong']} strong, {r['weak']} weak, {r['none']} none)")
        w("")
    w("## By arm")
    w("")
    w("| arm | audited | defective | rate |")
    w("|---|---:|---:|---:|")
    for arm, (t, d) in sorted(by_arm.items(), key=lambda x: -x[1][1]):
        w(f"| {arm} | {t} | {d} | {d/max(1,t):.0%} |")
    w("")
    if a.verbose and defective:
        w("## Every defective row")
        w("")
        for r in defective:
            w(f"- `{r['id']}` {r['arm']} · {'/'.join(r['flags'])} · "
              f"cites {r['n_cites']}/{r['report_items']} "
              f"(S{r['strong']} W{r['weak']} N{r['none']} M{r['missing']})")
        w("")
    md = "\n".join(L)

    print(md if a.verbose else "\n".join(L[:len(L)]))
    if a.report:
        Path(a.report).write_text(md + "\n", encoding="utf-8")
        print(f"\nreport -> {a.report}", file=sys.stderr)
    if a.jsonout:
        Path(a.jsonout).write_text(json.dumps({
            "schema": "cite-integrity/1.0",
            "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "thresholds": {"df_rare_frac": DF_RARE_FRAC,
                           "shotgun_abs": SHOTGUN_ABS,
                           "shotgun_frac": SHOTGUN_FRAC,
                           "deadweight_min": DEADWEIGHT_MIN,
                           "deadweight_frac": DEADWEIGHT_FRAC},
            "audited": len(results), "scope_limited": scoped,
            "defective": len(defective),
            "keyless_total": len(kl), "keyless_defective": len(kl_def),
            "rows": results}, indent=1) + "\n", encoding="utf-8")
        print(f"verdicts -> {a.jsonout}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
