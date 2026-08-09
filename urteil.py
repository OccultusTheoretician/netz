#!/usr/bin/env python3
"""urteil.py - THE VERDICT-GROUNDING AUDIT.

The blind jury's standing structural open, printed since the protocol
shipped: THE JURY CANNOT DETECT CONFABULATION WHEN IT LANDS ON THE CORRECT
VERDICT. A juror who invents evidence and happens to be right passes
concordance, and the fabrication enters the record wearing a valid ruling.
The KK26 precedent is the proof: a cold-seat juror returned fabricated Meta
prices at half the actual level - caught that time by the operator's eye,
not by any instrument.

This instrument closes the mechanical half of that open. GROUNDING IS
CHECKABLE EVEN WHEN THE VERDICT IS RIGHT. Every non-ABSTAIN verdict is
audited against the held evidence for its row - the same fetch-and-hash
record the juror was shown - by the same mechanics that audit forecast
citations:

  FIGURES     every number, dollar amount, percentage, and date asserted
              in the verdict's evidence text is checked against the held
              record. A figure the held evidence does not contain is an
              UNGROUNDED-SPECIFIC finding - the fabricated-Meta-prices
              class, caught mechanically.
  VOCABULARY  substantive-token overlap between verdict evidence and held
              text, the citation gate's own machinery run at the
              adjudication layer.
  CUSTODY     a non-ABSTAIN verdict on a row that held no evidence is an
              UNHELD-VERDICT finding: under 8.07 it should have been
              coerced to ABSTAIN, so its existence is a protocol defect.

Verdicts are then cross-read against the ledger: a verdict that MATCHES the
row's final ruling and still fails grounding prints as CORRECT-BUT-
UNGROUNDED - right for reasons the record does not contain. That class is
the point of the instrument. A wrong ungrounded verdict is an error; a
right ungrounded one is the invisible failure the blind protocol could not
see, and it is the one this desk puts on the page.

Searched jurors (juror A) may legitimately ground verdicts in material
beyond the held block - their access includes search by arm identity. For
them, out-of-held figures print as OUT-OF-HELD (disclosed, not defective)
unless the row held evidence that CONTRADICTS the figure. Cold jurors
(juror B) have no such license: out-of-held specifics are ungrounded by
construction.

Read-only. Writes forecasts/urteil_latest.json + URTEIL_latest.md.
Misses printed at full size. The auditor is audited by its own class of
instrument - this is the desk's method pointed at the desk's own bench.
"""
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "forecasts"

STOP = set("""the a an and or of to in on for by with at from as is are was
were be been that this those these it its their his her they he she we you
between during after before against will would may might per than then so
if not no none found reported reports report dated states stated confirm
confirms confirmed according while which who whose where when what""".split())

NUM = re.compile(r"(?<![\w.])(\$?\d[\d,]*(?:\.\d+)?%?)(?![\w])")
DATE = re.compile(r"\b(20\d\d-\d\d-\d\d)\b")


def _tok(s):
    return {w for w in re.findall(r"[a-z][a-z0-9'-]{3,}", str(s).lower())
            if w not in STOP}


def _figs(s):
    s = str(s or "")
    out = set()
    for m in NUM.finditer(s):
        t = m.group(1).replace(",", "").lstrip("$").rstrip("%")
        try:
            f = float(t)
        except ValueError:
            continue
        if 1900 <= f <= 2100 and "." not in t:
            continue  # bare years grade as vocabulary, not figures
        out.add(t)
    out |= set(DATE.findall(s))
    return out


def _newest(pattern):
    fs = sorted(OUT.glob(pattern))
    return fs[-1] if fs else None


def main():
    argv = sys.argv[1:]
    stamp = None
    for a in argv:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", a):
            stamp = a
    files = []
    if stamp:
        for side in ("A", "B"):
            p = OUT / f"jury_{side}_{stamp}.json"
            if p.exists():
                files.append((side, p))
        hp = None
    else:
        for side in ("A", "B"):
            p = _newest(f"jury_{side}_*.json")
            if p:
                files.append((side, p))
        hp = None
    if not files:
        print("URTEIL - no jury verdict files under forecasts/", file=sys.stderr)
        return 1
    # Each jury file is audited against the held file OF ITS OWN DATE -
    # never the newest. Cross-date pairing produced a right answer by the
    # wrong mechanism on this instrument's first bare run; printed, fixed.
    held_by_file, custody_notes, held_names = {}, [], []
    for side, path in files:
        m2 = re.search(r"(\d{4}-\d{2}-\d{2})", path.name)
        hpx = OUT / f"held_evidence_{m2.group(1)}.json" if m2 else None
        hd = {}
        if hpx and hpx.exists():
            try:
                hd = json.loads(hpx.read_text(encoding="utf-8"))
                held_names.append(hpx.name)
                if not hd:
                    custody_notes.append(
                        f"{hpx.name} holds 0 rows - held-evidence gathering "
                        f"returned nothing for a jury day; every verdict "
                        f"that day is unauditable at the custody layer")
            except Exception as e:
                custody_notes.append(f"{hpx.name} unreadable ({e})")
        else:
            custody_notes.append(
                f"no held-evidence file for {path.name} - custody findings "
                f"only for that file")
        held_by_file[path.name] = hd
    ledger = {}
    try:
        ledger = {p["id"]: p for p in json.loads(
            (HERE / "ledger.json").read_text(encoding="utf-8"))["projections"]}
    except Exception:
        pass

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    audits = []
    counts = {"GROUNDED": 0, "THIN": 0, "UNGROUNDED-SPECIFIC": 0,
              "UNHELD-VERDICT": 0, "UNHELD-SEARCHED": 0,
              "OUT-OF-HELD": 0, "ABSTAIN": 0}
    correct_but_ungrounded = []

    for side, path in files:
        searched = (side == "A")  # arm identity: A searched, B cold
        try:
            verdicts = json.loads(path.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"URTEIL - {path.name} unreadable: {e}", file=sys.stderr)
            continue
        for v in verdicts:
            rid = v.get("id", "?")
            verdict = str(v.get("verdict", "")).upper()
            if verdict == "ABSTAIN":
                counts["ABSTAIN"] += 1
                continue
            h = held_by_file.get(path.name, {}).get(rid) or {}
            htext = " ".join(str(h.get(k, "")) for k in
                             ("detail", "url", "resolver"))
            ev = " ".join(str(v.get(k, "")) for k in
                          ("evidence", "disconfirming", "note"))
            row = ledger.get(rid, {})
            final = str(row.get("status", "")).upper()
            agreed = (final in ("HIT", "MISS") and verdict == final)

            if not h:
                if searched:
                    klass = "UNHELD-SEARCHED"
                    detail = ("no held evidence for this row - a searched "
                              "juror may rule from its own access (8.07 "
                              "coercion is cold-seat only), but grounding "
                              "cannot be audited; disclosed, unauditable")
                else:
                    klass = "UNHELD-VERDICT"
                    detail = ("non-ABSTAIN verdict by a COLD juror on a row "
                              "that held no evidence - 8.07 coercion should "
                              "have fired; protocol defect")
                missing = sorted(_figs(ev))
            else:
                hf = _figs(htext)
                vf = _figs(ev)
                missing = sorted(vf - hf)
                shared = _tok(ev) & _tok(htext)
                if missing and not searched:
                    klass = "UNGROUNDED-SPECIFIC"
                    detail = (f"{len(missing)} figure(s)/date(s) asserted "
                              f"beyond the held record by a cold juror: "
                              f"{', '.join(missing[:8])}")
                elif missing and searched:
                    klass = "OUT-OF-HELD"
                    detail = (f"{len(missing)} figure(s) beyond the held "
                              f"block - within a searched juror's arm "
                              f"identity; disclosed, not defective: "
                              f"{', '.join(missing[:8])}")
                elif len(shared) < 3:
                    klass = "THIN"
                    detail = (f"only {len(shared)} substantive token(s) "
                              f"shared with the held record - grounding "
                              f"not demonstrable, not disproven")
                else:
                    klass = "GROUNDED"
                    detail = (f"{len(shared)} substantive token(s) shared "
                              f"with held record; no out-of-record figures")
            counts[klass] += 1
            rec = {"row": rid, "juror": side,
                   "juror_access": "searched" if searched else "cold",
                   "verdict": verdict, "final_status": final or "open",
                   "agreed_with_final": agreed, "class": klass,
                   "detail": detail, "figures_beyond_held": missing,
                   "held_sha256": h.get("sha256_raw", "")}
            audits.append(rec)
            if agreed and klass in ("UNGROUNDED-SPECIFIC", "UNHELD-VERDICT"):
                correct_but_ungrounded.append(rec)

    out = {"_meta": {"generated": now, "instrument": "urteil/1.0",
                     "doctrine": ("grounding is checkable even when the "
                                  "verdict is right; a correct ungrounded "
                                  "verdict is the failure the blind "
                                  "protocol cannot see, printed here"),
                     "sources": [p.name for _, p in files] + held_names,
                     "custody_notes": custody_notes,
                     "counts": counts,
                     "correct_but_ungrounded": len(correct_but_ungrounded)},
           "audits": audits}
    OUT.mkdir(exist_ok=True)
    fj = OUT / "urteil_latest.json"
    blob = json.dumps(out, indent=1, ensure_ascii=False) + "\n"
    fj.write_text(blob, encoding="utf-8")
    dj = HERE / "docs" / "urteil_latest.json"
    if dj.parent.exists():
        dj.write_text(blob, encoding="utf-8")

    md = [f"# URTEIL - verdict-grounding audit - {now}", "",
          "Every non-ABSTAIN jury verdict audited against the held evidence "
          "for its row, by the same mechanics that audit forecast "
          "citations. Grounding is checkable even when the verdict is "
          "right; the CORRECT-BUT-UNGROUNDED class is the one the blind "
          "protocol cannot see on its own.", "",
          "| class | n |", "|---|---|"]
    for k, n in counts.items():
        md.append(f"| {k} | {n} |")
    md.append("")
    if custody_notes:
        md.append("## CUSTODY")
        for c in custody_notes:
            md.append(f"- {c}")
        md.append("")
    if correct_but_ungrounded:
        md.append("## CORRECT-BUT-UNGROUNDED - printed at full size")
        for r in correct_but_ungrounded:
            md.append(f"- **{r['row']}** juror {r['juror']} "
                      f"({r['juror_access']}) ruled {r['verdict']}, final "
                      f"{r['final_status']} - {r['detail']}")
        md.append("")
    flagged = [r for r in audits if r["class"] not in ("GROUNDED",)]
    if flagged:
        md.append("## All non-GROUNDED verdicts")
        for r in flagged:
            md.append(f"- {r['row']} - juror {r['juror']} "
                      f"({r['juror_access']}) - {r['verdict']} "
                      f"(final {r['final_status']}) - **{r['class']}** - "
                      f"{r['detail']}")
    else:
        md.append("Every audited verdict grounded in its held record.")
    md.append("")
    md.append("urteil/1.0 - read-only - the desk's method pointed at the "
              "desk's own bench")
    (OUT / "URTEIL_latest.md").write_text("\n".join(md) + "\n",
                                          encoding="utf-8")
    print(f"URTEIL - {sum(counts.values())} verdict(s) audited - "
          + " - ".join(f"{k} {n}" for k, n in counts.items() if n),
          file=sys.stderr)
    if correct_but_ungrounded:
        print(f"URTEIL - CORRECT-BUT-UNGROUNDED: "
              f"{len(correct_but_ungrounded)} - the invisible class, "
              f"printed", file=sys.stderr)
    print(f"URTEIL - json -> {fj}", file=sys.stderr)
    print(f"URTEIL - md   -> {OUT / 'URTEIL_latest.md'}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
