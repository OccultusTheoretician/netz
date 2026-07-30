# denom — evidentiary completeness for AI-generated records

**Prove the denominator, not just the sample.**

An AI deployer facing an auditor can show the outputs it chooses to show. That
is a management-selected sample, and a management-selected sample is not
evidence about the population it came from. Timestamping each output — the thing
several tools already do — does not fix this: you can seal fifty records, reveal
the six that look good, and every revealed hash verifies while the record is a
lie.

`denom` fixes the denominator. Every record is sealed at creation into an
append-only, hash-chained vault. Periodically the vault emits an **anchor** — a
record count, a Merkle root over all commitments, and the chain head — which you
publish where you do not control the clock. Contents stay private. Later, any
subset can be disclosed with inclusion proofs, and **an auditor verifies the
subset against the anchor without trusting you** — confirming each disclosed
record was sealed before the anchor *and* that the subset comes from a
population of exactly the committed size.

Cherry-picking stays possible. Undetectable cherry-picking does not.

---

## Why this, why now

The EU AI Act carries penalties to €35M or 7% of worldwide turnover, with
Article 12 record-keeping and Article 50 transparency obligations landing on
concrete 2026 dates. The compliance-tooling market that grew up around it is
**documentation-first** — technical files, classification, impact assessments —
and priced for large enterprises (incumbent AI-governance suites run roughly
€30k–€100k+/year, sales-led).

The thin, underbuilt part of that stack is evidence *integrity*: the buyer's
question that current comparisons name as the sharpest differentiator is whether
an auditor can trust the evidence or has to trust the vendor — resolved by
cryptographic integrity verification, tamper-evident storage, and independent
verification. `denom` is exactly that layer, and it adds the one control the
timestamp-only products miss: a committed denominator.

**Positioning:** not a governance suite, not a documentation portal. The
evidence-integrity primitive those suites lack, usable standalone or as the
verifiable core beneath them.

---

## What it proves — and what it does not

Stated plainly, because an evidence tool that overclaims is worse than none.

**Proves**
- Each disclosed record existed, byte-for-byte unmodified, at anchor time.
- Each disclosed record belonged to a sealed population whose size was
  committed in advance — the denominator is honest.
- The vault is internally consistent: append-only, hash-chained, every
  commitment reopens (`denom audit`).

**Does not prove**
1. **Capture completeness.** It proves the size of what was *sealed*, not that
   everything the system produced was sealed. Closing that gap is a deployment
   control: enforce sealing in the serving path, reconcile vault counts against
   inference or billing logs, state the reconciliation in the audit. `denom
   report` prints this residual on its face.
2. **Anchor time strength.** An anchor is only as strong as where it is
   published. Publish where you do not control the clock (a public git host, an
   RFC 3161 token, a transparency log).
3. **Record quality.** Sealing proves existence and integrity, not that a
   record is correct, legal, or truthful.

A tool that names the discretions it cannot remove is stronger than one that
implies it has none. `denom report` names them every time.

---

## Install

None. One file, Python 3.10+, standard library only. No dependencies, no
network calls, no service to trust.

```
python denom.py --help
```

## Use

```
python denom.py init
python denom.py seal --file output_0001.json --meta model=acme-7b --meta req=abc
python denom.py seal --text "..." --meta model=acme-7b
# ... seal every output your system produces ...

python denom.py anchor            # emits ANCHOR_*.json; PUBLISH it externally
python denom.py disclose --seq 12 40 91 --out disclosure.json

# hand disclosure.json + the published anchor to the auditor. They run:
python denom.py verify-bundle disclosure.json --anchor ANCHOR_00000500.json

python denom.py audit             # internal integrity check
python denom.py report            # completeness posture + disclosed discretions
```

The vault's `openings/` directory holds salts and record contents — **private,
never published.** Only anchors and disclosure bundles are shareable. Keep the
vault out of any public repository.

---

## How it works

- **Commitment.** `H(TAG ‖ salt ‖ H(content) ‖ H(canonical-meta))`, 32-byte
  random salt per record. Hides content; binds it.
- **Chain.** `h_i = H(TAG ‖ h_{i-1} ‖ entry-core)`, genesis prev = 0. Append-only;
  any retroactive edit breaks the chain (`denom audit` catches it).
- **Tree.** Merkle root per RFC 6962 (Certificate Transparency): domain-separated
  leaf/node tags, unbalanced split at the largest power of two, no leaf
  duplication — so the duplicate-leaf malleability class does not apply.
- **Anchor.** count + root + head, canonicalized and hashable to a single
  digest for external publication.
- **Disclosure.** per-record opening + RFC 6962 audit path, verified against the
  anchor's root and count.

Every hash is SHA-256 with domain separation. The verifier is the same file; an
auditor needs nothing from the operator but the bundle and the published anchor.

---

## Status

`denom.py` 0.1.0 — reference core, adversarially tested (eight forgery classes
rejected; Merkle property-tested across tree sizes 1–24). This is the
evidence-integrity primitive. A production deployment adds: serving-path sealing
middleware, count-vs-inference reconciliation, multi-year retention/export, and
role-scoped custody — the operational layer where evidence tools are judged.

Companion: `DENOM_STANDARD.md` — the method specification a compliance team
reads and an implementer builds to.
