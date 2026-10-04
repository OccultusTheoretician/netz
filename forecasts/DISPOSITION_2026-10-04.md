# DISPOSITION — JURY SITTING 2026-10-04

**AUTHORSHIP.** Drafted by the desk's assistant; reviewed and adopted by the operator as his ruling on 2026-10-04. The rulings below are his.

## Inputs

| input | detail | LF-sha256 |
|---|---|---|
| packet | `forecasts/audit_packet_2026-10-04.md` — every open row past deadline: 502 rows, 363 unique claims (139 rows repeat a control's or arm's claim word for word) | — |
| juror A | `forecasts/jury_A_2026-10-04.json` — basis `claude` (Opus 5.5), web search on; two incognito chats, account preferences removed, connectors off; unique claims only, verdicts fanned to every row carrying the claim; the operator's only words to the juror after the packet were "Continue" and a request for the file | `65c86c0a40d03323…` |
| juror B | `forecasts/jury_B_2026-10-04.json` — basis `qwen`, local, no search; held-evidence rule applied (67 rows held) | `8b95b55834ea08a1…` |
| held evidence | `forecasts/held_evidence_2026-10-04.json` | `1381b72c41ba2a1e…` |
| clerk | KEV pass against catalogVersion 2026.10.04 (1,734 entries, feed sha256 `f51fed1c9213e7b7`): 75 rows, 56 AGREES, 19 CHECK | — |

Kappa +0.152 on 502 rows juried by both; meaningless while juror B abstains on 435.

## Rule

1. **Concordant HIT or MISS** — both seats agree: accepted (`jury-concordant`).
2. **Juror A alone** — A returns HIT or MISS at high or moderate confidence and B abstains: A's verdict adopted (`claude`).
3. **Everything else left open** — abstain, ambiguous, or A at low confidence.

## Exceptions, each with its reason

- **Ten discords adopted from juror A.** Eight are KEV rows where B repeated the mechanical matcher's false positives — a generic "Microsoft" match read as Entra or Exchange (`-0822-13`, `-0901-23`, `-0902-06`, `-0902-20`, `-0902-27`), a window taken from the statement's date when the criterion opens a day later (`-0902-59`, `-0902-78`), and "Chrome V8" not matching the catalog's "Chromium V8" (`-0904-10`, where the catalog shows CVE-2026-87491 added 2026-09-09, inside the window). The clerk's catalog lines side with A on all eight. The other two are `-0906-13` and `-0906-40`: A found the 2026-09-17 M6.5 (us7000ti1p) about 160 km from us7000tdvt, while B's held evidence was queried at default Kyushu coordinates.
- **Voided: `-0913-03`.** Its criterion requires the USGS Significant Quakes feed, an earthquake catalog, to confirm a California wildfire; it cannot resolve on its own terms. A defect of the record.
- **Left open despite a rulable verdict:** `-0924-31` (A could not confirm the HU.W issuer and zones its criterion names), and `-0819-24`, `-0819-45`, `-0822-11` (held evidence queried at the wrong epicentre; these await a correct query).
- **Clerk CHECKs that did not change a verdict:** each read against its own criterion. They are parser misreads — stopwords taken as search terms, a generic vendor name, a product spelled differently, or a count claim the parser cannot read.

## Outcome

270 ruled — **175 hit, 94 miss, 1 void** — and 232 left open. By basis: 53 concordant, 216 juror A, 1 operator (the void).

## Execution

The rulings were entered through the `kkr.py --jury` console by `jury_walk_2026-10-04.py` (sha256 `AE99839BF23E1D34…`). It answers each console prompt by the row id on screen, never by position, and refuses to run if the console's row set or order differs from the reviewed sheet by a single row. The console's full transcript is retained with the operator. Each resolved row carries its own `audit` block: basis, both verdicts, and the evidence relied on.

## Defects surfaced for the bench

The mechanical KEV matcher accepts a generic vendor name as a product match. It misses product spelling variants. It takes a window from the statement's dates when the criterion states its own. The USGS resolver falls back to default Kyushu coordinates when a claim names an event id it could look up.
