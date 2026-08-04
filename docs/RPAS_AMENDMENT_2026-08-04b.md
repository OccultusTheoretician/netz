# RPAS-26 — AMENDMENT 2026-08-04b

**Corrects Amendment 2026-08-04, Part I·E. Adds one limitation the first amendment did not report. Records two findings under 6.04.**

Issued the same day as the text it corrects, four hours later, as a second dated amendment rather than an edit. **7.05** governs: revisions never alter the sealed record, and the first amendment is now part of that record. It stands as issued, with this correction attached.

A standard that reports its own defects and then quietly repairs its own account of them has not reported anything.

---

## 1 · CORRECTION — Part I·E overstated its own remedy

Amendment 2026-08-04, Part I·E, closed by stating that publishing hash commitments to the elicitation packets *"would close the limitation without republishing the underlying feed content."*

**That is too strong, and it is the same failure class the amendment was written to report.** The correct statement:

> A digest **closes retrofit**. Once a packet's bytes are committed and chained, the operator cannot rewrite what an arm was shown after seeing how the row resolved, and any later holder of the packet can prove it is the same file.
>
> A digest **does not close readability**. 1.04 asks whether a hit was *deducible* from the declared priors. A hash discloses nothing. For every entry whose packet is unpublished, the keyed/keyless determination remains uncheckable by a third party — the input is now fixed, and still not visible.

Half a remedy stated as a whole one. Corrected here, and stated in the register's own bytes so the artifact does not require this document to be read honestly.

**Full closure requires publishing packet bodies**, or publishing them under embargo until every entry citing them has resolved. Both carry real costs and neither is adopted here. The limitation stands, reduced in scope and accurately described.

---

## 2 · A LIMITATION THE FIRST AMENDMENT DID NOT REPORT

Part I·E reported 206 entries naming an unpublished packet. It did not report the remainder.

**Of 303 sealed entries, 206 name a `source_packet` and 97 name none at all.** Eighteen of those 97 are determined keyless.

For those entries the input is not merely unpublished — it is **unidentified**. There is no filename to look up, no digest to commit, and no artifact for any register to cover. The cause is on record in the desk's own source: the ingest path did not write the field until it was patched, so every entry that entered through manual ingest before that carried a blank one.

This is strictly worse than the limitation the first amendment reported, and the first amendment did not mention it. Both are stated now:

| | entries | the input is |
|---|---:|---|
| named, unpublished | 206 | fixed by digest, not readable |
| unnamed | **97** | not identified; no artifact exists to fix or publish |

These entries are marked, not removed, per 5.07. The condition is not retroactively repairable: the packets for July exist on the operator's machine, but which entry read which packet was never recorded and cannot now be established without assuming it.

---

## 3 · THE PACKET REGISTER (implemented; 4.04)

`docs/packet_register.json`. Twenty-two packets, hash-chained in filename order so an insertion or deletion breaks the chain. Chain head:

```
fdadfc8b606079dce21bb95bb5b7760b8add5ed71b54ae6263728ba437c85f9e
```

Each entry carries the packet's SHA-256, byte count, modification time, and **the count and identifiers of the sealed entries naming it** — the DECC-26 completeness control applied to inputs rather than disclosures, so the register carries its own denominator.

**First run produced a finding.** `kkr_packet_2026-07-26.md` and `kkr_packet_2026-07-26_1623.md` are **byte-identical** — the same digest, `5cb99173…`, and the same 44,832 bytes. One packet under two filenames, produced when the naming convention gained a time stamp mid-stream. Ten entries cite the timestamped name; nothing cites the other. No entry is affected, and the duplicate is recorded rather than deleted.

Twelve of the twenty-two packets are named by no sealed entry.

---

## 4 · A RESOLVER RETURNED A WRONG VERDICT, AND WHY NO ENTRY WAS AFFECTED

The first live test of the desk's mechanical resolvers ran 2026-08-04. The GDACS resolver returned **YES** for a predicate requiring a red alert, on an item whose own title reads *Green earthquake alert*. It matched the alert level as a substring against every string in the feed item flattened together, so the word "red" matched a legend, a description of a different event, or a URL fragment.

**It was the only instrument on this desk failing toward a verdict rather than toward a refusal**, which is the one direction an instrument arguing that it declines to guess cannot afford.

**No sealed entry was affected, and the reason is architectural rather than lucky.** Resolvers on this desk propose and never resolve; the only path that writes a verdict to the ledger is operator adjudication. A defect that would have been a false HIT in a coupled design was a wrong line in a report. The separation is stated in 5.06 and this is the first occasion it has been load-bearing.

The level is now read from the feed's namespaced alert element, failing that from the item title's leading word, and if neither is readable the resolver returns INDETERMINATE naming that rather than inferring from body text. Re-tested against 302 live feed items: INDETERMINATE.

Reported under 6.04 with the same ceremony as any finding this desk publishes about others. The defect was found by the desk's own first live parser test, and that test existed because the resolvers had been written and never run — which is itself the finding underneath this one.

---

## 5 · WHAT THIS AMENDMENT DOES NOT DO

It does not alter Amendment 2026-08-04, which stands as issued. It does not rescore an entry, edit a sealed row, or touch the anchored first edition. It does not repair the 97 entries whose input is unidentified, and it does not make the 206 readable.

It records that the desk's own account of its defects was itself defective, four hours after publishing it.

---

*Issued under RPAS-26 §7.05. Corrects Amendment 2026-08-04 Part I·E. The first edition and the first amendment remain as issued.*
