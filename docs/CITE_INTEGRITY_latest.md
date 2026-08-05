# CITATION INTEGRITY AUDIT

Generated 2026-08-05T12:30:59Z · ledger `ledger.json` · 322 rows in scope

Read-only. Sealed rows are never edited; a defect found after sealing is a printed finding, not a substitution.

## Thresholds (judgment calls — changing one changes the finding)

- rare-token cut: document frequency <= 25% of the report's items
- shotgun: >= 8 cited items, or >= 50% of the record
- deadweight: > 50% of cited items contributing nothing, minimum 3 cites

## Result

- rows audited: **321**
- scope limitation (no resolvable source report): **1**
- defective: **47** (14.6% of audited)
- rows whose citation number does not identify a unique item: **286** (max candidates behind one number: 8)
  - AMBIGUOUS_REF: 286
  - UNSUPPORTED: 35
  - NO_CITES: 16
  - DEADWEIGHT: 10
  - SHOTGUN: 7

## The number that matters

Rows determined **KEYLESS**: 86
Of those, citations defective: **10** (11.6%)

A keyless determination says the claim went beyond its declared priors. Where the priors are unreadable, that determination was made against nothing. These rows are listed so the keyless count can be stated with its defect rate attached rather than as a clean integer.

- `KKR-20260725-01` · manual/fable · 2026-07-25 · UNSUPPORTED/AMBIGUOUS_REF · 1 cites (0 strong, 0 weak, 1 none)
- `KKR-20260726-16` · lmstudio/auto · 2026-07-26 · DEADWEIGHT/AMBIGUOUS_REF · 3 cites (1 strong, 0 weak, 2 none)
- `KKR-20260727-17` · manual/fable · 2026-07-27 · UNSUPPORTED/AMBIGUOUS_REF · 1 cites (0 strong, 0 weak, 1 none)
- `KKR-20260727-27` · manual/opus-5 · 2026-07-27 · DEADWEIGHT/AMBIGUOUS_REF · 3 cites (1 strong, 0 weak, 2 none)
- `KKR-20260730-03` · manual/fable-5 · 2026-07-30 · DEADWEIGHT/AMBIGUOUS_REF · 3 cites (1 strong, 0 weak, 2 none)
- `KKR-20260730-12` · manual/opus-5 · 2026-07-30 · UNSUPPORTED/AMBIGUOUS_REF · 3 cites (0 strong, 0 weak, 3 none)
- `KKR-20260730-14` · manual/opus-5 · 2026-07-30 · UNSUPPORTED/AMBIGUOUS_REF · 3 cites (0 strong, 0 weak, 3 none)
- `KKR-20260731-23` · manual/opus-5 · 2026-07-31 · DEADWEIGHT/AMBIGUOUS_REF · 3 cites (1 strong, 0 weak, 2 none)
- `KKR-20260731-27` · manual/opus-5 · 2026-07-31 · UNSUPPORTED/AMBIGUOUS_REF · 3 cites (0 strong, 0 weak, 3 none)
- `KKR-20260802-01` · lmstudio/auto · 2026-08-02 · UNSUPPORTED/AMBIGUOUS_REF · 1 cites (0 strong, 0 weak, 1 none)

## By arm

**Read this table with its defect attached.** Until 2026-08-04 the `--ingest` path resolved `source_report` three lines AFTER the gate ran, so `_citation_support` saw an empty field and returned pass on every row. Every manual arm entered ungated on citations; `cmd_generate` set the field first, so `lmstudio/auto` was the only arm ever checked at seal time. These rates therefore compare one gated arm against arms that were never gated, and the manual arms' rates are what an ungated lane produced — not evidence that gating does or does not work. Rows sealed from 2026-08-04 forward are gated on both paths (KK21c).

| arm | audited | defective | rate |
|---|---:|---:|---:|
| lmstudio/auto | 95 | 19 | 20% |
| manual/opus-5 | 50 | 11 | 22% |
| manual/fable | 45 | 6 | 13% |
| manual/opus-5/unattested | 25 | 3 | 12% |
| control/baserate | 25 | 3 | 12% |
| manual/fable-5 | 20 | 2 | 10% |
| manual/sonnet-5/unattested | 22 | 2 | 9% |
| manual/fable-5/unattested | 5 | 1 | 20% |
| operator/human | 6 | 0 | 0% |
| kfk/halflife | 10 | 0 | 0% |
| manual/sonnet-5 | 18 | 0 | 0% |

