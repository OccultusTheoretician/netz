# IDENTIFIER GROUNDEDNESS AUDIT

Generated 2026-08-24T06:23:11Z · 64 report(s)

Identifiers appearing in machine-drafted synthesis prose are tested for format validity and for presence in the numbered record the synthesis summarises. An identifier the synthesis introduces on its own is unsourced by construction, and reads as more precise than the prose around it — which is why it goes unchecked.

## Result

- reports audited: **64**
- findings: **105**
> **Scope limitation.** `--packets` was not supplied, so UNSOURCED findings were tested against the published report only. The packet the forecaster arm actually read is excluded from the repository by `.gitignore` (`forecasts/kkr_packet_*.md`), and it carries article summaries the report's record lines omit. An UNSOURCED finding here means *not present in the published record* — it is not a claim that the identifier is invented. MALFORMED findings stand regardless of provenance.

  - MALFORMED: 3
  - UNSOURCED: 102
- distinct tokens: **44**

## Reached a sealed row

**25** sealed row(s) carry an identifier this audit flags. A sealed row is never edited; these are printed as findings.

| row | token | finding | arm | status | k/kl |
|---|---|---|---|---|---|
| `KKR-20260720-20` | `CVE-2026-6875` | UNSOURCED | lmstudio/auto | open | keyless |
| `KKR-20260721-04` | `CVE-2026-60137` | UNSOURCED | lmstudio/auto | hit | keyed |
| `KKR-20260721-07` | `CVE-2026-6` | MALFORMED | lmstudio/auto | miss | keyless |
| `KKR-20260806-32` | `CVE-2026-63077` | UNSOURCED | lmstudio/auto | open | keyed |
| `KKR-20260730-05` | `CVE-2026-20316` | UNSOURCED | manual/fable-5 | open | keyless |
| `KKR-20260730-15` | `CVE-2026-20316` | UNSOURCED | manual/opus-5 | open | keyed |
| `KKR-20260730-25` | `CVE-2026-20316` | UNSOURCED | manual/sonnet-5 | open | keyed |
| `KKR-20260804-02` | `CVE-2026-18577` | UNSOURCED | lmstudio/auto | miss | keyless |
| `KKR-20260804-10` | `CVE-2026-18577` | UNSOURCED | control/baserate | miss | keyed |
| `KKR-20260804-49` | `CVE-2026-18577` | UNSOURCED | lmstudio/auto | void | — |
| `KKR-20260804-59` | `CVE-2026-18577` | UNSOURCED | manual/opus-5/unattested | open | keyed |
| `KKR-20260804-64` | `CVE-2026-18577` | UNSOURCED | manual/sonnet-5/unattested | open | keyed |
| `KKR-20260804-59` | `CVE-2026-18556` | UNSOURCED | manual/opus-5/unattested | open | keyed |
| `KKR-20260805-01` | `CVE-2026-9198` | UNSOURCED | lmstudio/auto | miss | keyed |
| `KKR-20260808-22` | `CVE-2026-8037` | UNSOURCED | manual/sonnet-5 | open | keyed |
| `KKR-20260813-32` | `CVE-2026-55040` | UNSOURCED | manual/sonnet-5/unattested | open | keyed |
| `KKR-20260813-36` | `CVE-2026-55040` | UNSOURCED | control/baserate | open | keyed |
| `KKR-20260812-02` | `CVE-2026-20349` | UNSOURCED | lmstudio/auto | open | keyed |
| `KKR-20260817-69` | `CVE-2026-59310` | UNSOURCED | manual/opus-5/unattested | open | keyed |
| `KKR-20260817-72` | `CVE-2026-59310` | UNSOURCED | control/baserate | open | keyed |
| `KKR-20260817-29` | `CVE-2025-62593` | UNSOURCED | lmstudio/auto | open | keyed |
| `KKR-20260817-31` | `CVE-2025-62593` | UNSOURCED | lmstudio/auto | open | keyed |
| `KKR-20260818-04` | `CVE-2025-62593` | UNSOURCED | lmstudio/auto | open | — |
| `KKR-20260820-18` | `CVE-2026-73570` | UNSOURCED | manual/sonnet-5/unattested | open | — |
| `KKR-20260822-10` | `CVE-2026-69836` | UNSOURCED | manual/fable-5/unattested | open | — |

## Every finding

| report | token | finding |
|---|---|---|
| battle_report_2026-07-20_1923.md | `CVE-2026-6875` | UNSOURCED |
| battle_report_2026-07-20_1923.md | `CVE-2026-42533` | UNSOURCED |
| battle_report_2026-07-20_2058.md | `CVE-2026-6875` | UNSOURCED |
| battle_report_2026-07-20_2058.md | `CVE-2026-14266` | UNSOURCED |
| battle_report_2026-07-20_2106.md | `CVE-2026-6875` | UNSOURCED |
| battle_report_2026-07-20_2106.md | `CVE-2026-14266` | UNSOURCED |
| battle_report_2026-07-20_2131.md | `CVE-2026-6875` | UNSOURCED |
| battle_report_2026-07-20_2131.md | `CVE-2026-14266` | UNSOURCED |
| battle_report_2026-07-20_2137.md | `CVE-2026-6875` | UNSOURCED |
| battle_report_2026-07-20_2137.md | `CVE-2026-14266` | UNSOURCED |
| battle_report_2026-07-21_1532.md | `CVE-2026-60137` | UNSOURCED |
| battle_report_2026-07-21_1532.md | `CVE-2026-63030` | UNSOURCED |
| battle_report_2026-07-21_1532.md | `CVE-2026-0770` | UNSOURCED |
| battle_report_2026-07-21_1532.md | `CVE-2021-27137` | UNSOURCED |
| battle_report_2026-07-21_1532.md | `CVE-2026-6` | MALFORMED |
| battle_report_2026-07-21_1548.md | `CVE-2026-60137` | UNSOURCED |
| battle_report_2026-07-21_1548.md | `CVE-2026-63030` | UNSOURCED |
| battle_report_2026-07-21_1548.md | `CVE-2026-0770` | UNSOURCED |
| battle_report_2026-07-21_1548.md | `CVE-2021-27137` | UNSOURCED |
| battle_report_2026-07-21_1548.md | `CVE-2026-50523` | UNSOURCED |
| battle_report_2026-07-21_1548.md | `CVE-2026-63` | MALFORMED |
| battle_report_2026-07-21_1548.md | `CVE-2026-6` | MALFORMED |
| battle_report_2026-07-22_0409.md | `CVE-2026-60137` | UNSOURCED |
| battle_report_2026-07-22_0409.md | `CVE-2026-63030` | UNSOURCED |
| battle_report_2026-07-22_0409.md | `CVE-2026-0770` | UNSOURCED |
| battle_report_2026-07-22_0409.md | `CVE-2021-27137` | UNSOURCED |
| battle_report_2026-07-22_0416.md | `CVE-2026-60137` | UNSOURCED |
| battle_report_2026-07-22_0416.md | `CVE-2026-63030` | UNSOURCED |
| battle_report_2026-07-22_0416.md | `CVE-2026-0770` | UNSOURCED |
| battle_report_2026-07-22_0416.md | `CVE-2021-27137` | UNSOURCED |
| battle_report_2026-07-22_1500.md | `CVE-2026-60137` | UNSOURCED |
| battle_report_2026-07-22_1500.md | `CVE-2026-63030` | UNSOURCED |
| battle_report_2026-07-22_1500.md | `CVE-2026-0770` | UNSOURCED |
| battle_report_2026-07-22_1500.md | `CVE-2021-27137` | UNSOURCED |
| battle_report_2026-07-22_1545.md | `CVE-2026-60137` | UNSOURCED |
| battle_report_2026-07-22_1545.md | `CVE-2026-63030` | UNSOURCED |
| battle_report_2026-07-22_1545.md | `CVE-2026-0770` | UNSOURCED |
| battle_report_2026-07-22_1545.md | `CVE-2021-27137` | UNSOURCED |
| battle_report_2026-07-22_1545.md | `CVE-2026-29059` | UNSOURCED |
| battle_report_2026-07-22_1545.md | `CVE-2026-50522` | UNSOURCED |
| battle_report_2026-07-23_1500.md | `CVE-2026-16232` | UNSOURCED |
| battle_report_2026-07-23_1500.md | `CVE-2026-50522` | UNSOURCED |
| battle_report_2026-07-23_1503.md | `CVE-2026-16232` | UNSOURCED |
| battle_report_2026-07-23_1503.md | `CVE-2026-50522` | UNSOURCED |
| battle_report_2026-07-23_1503.md | `CVE-2026-64600` | UNSOURCED |
| battle_report_2026-07-28_0100.md | `CVE-2025-68686` | UNSOURCED |
| battle_report_2026-07-28_0100.md | `CVE-2026-16812` | UNSOURCED |
| battle_report_2026-07-28_0108.md | `CVE-2025-68686` | UNSOURCED |
| battle_report_2026-07-28_0108.md | `CVE-2026-16812` | UNSOURCED |
| battle_report_2026-07-28_0122.md | `CVE-2025-68686` | UNSOURCED |
| battle_report_2026-07-28_0122.md | `CVE-2026-16812` | UNSOURCED |
| battle_report_2026-07-28_0215.md | `CVE-2025-68686` | UNSOURCED |
| battle_report_2026-07-28_0215.md | `CVE-2026-16812` | UNSOURCED |
| battle_report_2026-07-28_0416.md | `CVE-2025-68686` | UNSOURCED |
| battle_report_2026-07-28_0416.md | `CVE-2026-16812` | UNSOURCED |
| battle_report_2026-07-28_0432.md | `CVE-2025-68686` | UNSOURCED |
| battle_report_2026-07-28_0432.md | `CVE-2026-16812` | UNSOURCED |
| battle_report_2026-07-28_0458.md | `CVE-2025-68686` | UNSOURCED |
| battle_report_2026-07-28_0458.md | `CVE-2026-16812` | UNSOURCED |
| battle_report_2026-07-28_1502.md | `CVE-2025-68686` | UNSOURCED |
| battle_report_2026-07-28_1502.md | `CVE-2026-16812` | UNSOURCED |
| battle_report_2026-07-28_1502.md | `CVE-2026-53264` | UNSOURCED |
| battle_report_2026-07-28_1502.md | `CVE-2026-53921` | UNSOURCED |
| battle_report_2026-07-28_1529.md | `CVE-2025-68686` | UNSOURCED |
| battle_report_2026-07-28_1529.md | `CVE-2026-16812` | UNSOURCED |
| battle_report_2026-07-28_1529.md | `CVE-2026-53921` | UNSOURCED |
| battle_report_2026-07-28_1529.md | `CVE-2026-63077` | UNSOURCED |
| battle_report_2026-07-29_1502.md | `CVE-2026-10702` | UNSOURCED |
| battle_report_2026-07-30_1503.md | `CVE-2026-20316` | UNSOURCED |
| battle_report_2026-07-30_1503.md | `CVE-2026-66066` | UNSOURCED |
| battle_report_2026-07-30_1503.md | `CVE-2026-66067` | UNSOURCED |
| battle_report_2026-08-03_1424.md | `CVE-2026-18577` | UNSOURCED |
| battle_report_2026-08-03_1501.md | `CVE-2026-18577` | UNSOURCED |
| battle_report_2026-08-03_2320.md | `CVE-2026-18577` | UNSOURCED |
| battle_report_2026-08-03_2351.md | `CVE-2026-18577` | UNSOURCED |
| battle_report_2026-08-04_1502.md | `CVE-2026-18577` | UNSOURCED |
| battle_report_2026-08-05_1501.md | `CVE-2026-18556` | UNSOURCED |
| battle_report_2026-08-05_1501.md | `CVE-2026-34486` | UNSOURCED |
| battle_report_2026-08-05_1501.md | `CVE-2026-9198` | UNSOURCED |
| battle_report_2026-08-06_0426.md | `CVE-2026-63077` | UNSOURCED |
| battle_report_2026-08-07_1747.md | `CVE-2026-8037` | UNSOURCED |
| battle_report_2026-08-08_1517.md | `CVE-2026-8037` | UNSOURCED |
| battle_report_2026-08-11_1750.md | `CVE-2026-55040` | UNSOURCED |
| battle_report_2026-08-12_1518.md | `CVE-2026-20349` | UNSOURCED |
| battle_report_2026-08-12_1518.md | `CVE-2026-68820` | UNSOURCED |
| battle_report_2026-08-12_1518.md | `CVE-2026-72898` | UNSOURCED |
| battle_report_2026-08-13_1519.md | `CVE-2026-55040` | UNSOURCED |
| battle_report_2026-08-13_1519.md | `CVE-2026-68820` | UNSOURCED |
| battle_report_2026-08-14_1517.md | `CVE-2026-59310` | UNSOURCED |
| battle_report_2026-08-17_1537.md | `CVE-2025-62593` | UNSOURCED |
| battle_report_2026-08-17_1537.md | `CVE-2026-69414` | UNSOURCED |
| battle_report_2026-08-17_1537.md | `CVE-2026-59310` | UNSOURCED |
| battle_report_2026-08-17_1537.md | `CVE-2026-54121` | UNSOURCED |
| battle_report_2026-08-18_1516.md | `CVE-2025-62593` | UNSOURCED |
| battle_report_2026-08-19_1519.md | `CVE-2026-33824` | UNSOURCED |
| battle_report_2026-08-19_1519.md | `CVE-2026-59310` | UNSOURCED |
| battle_report_2026-08-19_1519.md | `CVE-2026-55040` | UNSOURCED |
| battle_report_2026-08-19_1519.md | `CVE-2026-65400` | UNSOURCED |
| battle_report_2026-08-20_1537.md | `CVE-2026-64849` | UNSOURCED |
| battle_report_2026-08-20_1537.md | `CVE-2026-32475` | UNSOURCED |
| battle_report_2026-08-20_1537.md | `CVE-2026-73570` | UNSOURCED |
| battle_report_2026-08-21_1524.md | `CVE-2026-72530` | UNSOURCED |
| battle_report_2026-08-21_1524.md | `CVE-2026-72529` | UNSOURCED |
| battle_report_2026-08-21_1524.md | `CVE-2026-69836` | UNSOURCED |
| battle_report_2026-08-22_1516.md | `CVE-2026-73570` | UNSOURCED |

