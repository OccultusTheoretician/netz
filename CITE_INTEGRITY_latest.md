# CITATION INTEGRITY AUDIT

Generated 2026-09-06T09:38:52Z · ledger `ledger.json` · 1545 rows in scope

Read-only. Sealed rows are never edited; a defect found after sealing is a printed finding, not a substitution.

## Thresholds (judgment calls — changing one changes the finding)

- rare-token cut: document frequency <= 25% of the report's items
- shotgun: >= 8 cited items, or >= 50% of the record
- deadweight: > 50% of cited items contributing nothing, minimum 3 cites

## Result

- rows audited: **1544**
- scope limitation (no resolvable source report): **1**
- defective: **204** (13.2% of audited)
- rows whose citation number does not identify a unique item: **329** (max candidates behind one number: 8)
  - AMBIGUOUS_REF: 329
  - UNSUPPORTED: 121
  - DEADWEIGHT: 79
  - NO_CITES: 24
  - SHOTGUN: 24
  - THIN: 1

## The number that matters

Rows determined **KEYLESS**: 108
Of those, citations defective: **11** (10.2%)

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
- `KKR-20260808-05` · lmstudio/auto · 2026-08-08 · UNSUPPORTED · 2 cites (0 strong, 0 weak, 2 none)

## By arm

**Read this table with its defect attached.** Until 2026-08-04 the `--ingest` path resolved `source_report` three lines AFTER the gate ran, so `_citation_support` saw an empty field and returned pass on every row. Every manual arm entered ungated on citations; `cmd_generate` set the field first, so `lmstudio/auto` was the only arm ever checked at seal time. These rates therefore compare one gated arm against arms that were never gated, and the manual arms' rates are what an ungated lane produced — not evidence that gating does or does not work. Rows sealed from 2026-08-04 forward are gated on both paths (KK21c).

| arm | audited | defective | rate |
|---|---:|---:|---:|
| lmstudio/auto | 296 | 84 | 28% |
| control/baserate | 458 | 40 | 9% |
| manual/opus-5/unattested | 185 | 24 | 13% |
| manual/fable-5/unattested | 168 | 13 | 8% |
| manual/opus-5 | 74 | 12 | 16% |
| manual/sonnet-5/unattested | 173 | 11 | 6% |
| manual/fable-5.1/unattested | 31 | 7 | 23% |
| manual/fable | 45 | 6 | 13% |
| lmstudio/realist | 11 | 4 | 36% |
| manual/fable-5 | 38 | 2 | 5% |
| manual/sonnet-5 | 45 | 1 | 2% |
| operator/human | 10 | 0 | 0% |
| kfk/halflife | 10 | 0 | 0% |

