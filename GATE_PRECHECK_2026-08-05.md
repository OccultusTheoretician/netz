# FORECLOSURE-GATE PRECHECK -- 2026-08-05

Gate: `foreclose_check.py` v1.1 (date-added token fix, worldwide scope, citation-echo casualty check) -- selftest 6/6, regression on the sealed lmstudio run unchanged (1 FORECLOSED / 1 SATISFIED / 8 PASS).
Packet: `kkr_packet_2026-08-05_1501.md` (sha256 a19261b1...c3a26b09, byte-identical to `kkr_packet_latest.md` at check time).
This file is the printed record for any row dropped pre-ingest: a hand-drop without a printed reason is tidying; this is the reason, printed.

## lmstudio/auto[post-window] raw (ALREADY SEALED -- regression only)

```
PASS               row 0
REJECT_FORECLOSED  row 1
    the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-9198 dateAdded 2026-08-04, before the claimed window 2026-08-05..2026-08-12; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
REJECT_SATISFIED   row 2
    the packet already decides this claim; a forecast must be open at seal -- the packet carries a GDACS M6.3 depth 10km quake in Philippines dated 2026-08-05, inside the claimed window 2026-08-05..2026-08-12
PASS               row 3
PASS               row 4
PASS               row 5
PASS               row 6
PASS               row 7
PASS               row 8
PASS               row 9

summary: PASS=8 REJECT_FORECLOSED=1 REJECT_SATISFIED=1
```

## manual/opus-5/unattested

```
PASS               row 0
PASS               row 1
PASS               row 2
PASS               row 3
PASS               row 4
PASS               row 5
PASS               row 6
PASS               row 7
PASS               row 8
PASS               row 9

summary: PASS=10
```

## manual/sonnet-5/unattested

```
PASS               row 0
PASS               row 1
PASS               row 2
PASS               row 3
PASS               row 4
REJECT_SATISFIED   row 5
    the packet already decides this claim; a forecast must be open at seal -- the row's own citation [83], dated 2026-08-05 inside the claimed window 2026-08-05..2026-08-19, already reports 14 killed against the row's threshold of 10
PASS               row 6
PASS               row 7
PASS               row 8

summary: PASS=8 REJECT_SATISFIED=1
```

## manual/fable-5/unattested

```
PASS               row 0
PASS               row 1
PASS               row 2
PASS               row 3
PASS               row 4
PASS               row 5
PASS               row 6
PASS               row 7
PASS               row 8
PASS               row 9

summary: PASS=10
```

## Disposition

- opus: 10/10 PASS -- ingest as-is.
- fable: 10/10 PASS (via deterministic JSON extraction from the render; all 10 statement strings verified verbatim against the source md) -- ingest the JSON.
- sonnet: row 6 (Kyiv strike, p=40) REJECT_SATISFIED -- both its citations [83, 90] report the 2026-08-05 Kyiv strike (14 per Guardian URL, 21 per BBC headline) at or above its own threshold of 10, and its window opens 2026-08-05. Third instance of the already-decided class inside 24 hours, first caught pre-seal. DROP before ingest citing this record, or wire the gate hook first so the rejection prints natively in the KKR report.
- The sealed lmstudio run is regression only: -01/-02 stand and score per the 2026-08-05 ruling; nothing here re-opens them.
