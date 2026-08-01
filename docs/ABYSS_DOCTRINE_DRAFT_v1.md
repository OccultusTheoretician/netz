# ABYSS-26 — THE ABYSSAL SEQUENCE
## Contingent-Commitment Doctrine · DRAFT rev 1 · 2026-08-01

**PROVENANCE: DRAFT tier.** Claude-drafted under the operator's direction. Rev 1 replaces rev 0's model on evidence (§2) and reports a prior-art finding that narrows the novelty claim (§3). Becomes doctrine only on the operator's rework and ruling.

---

## 1. AUDIT OF THE INSTRUMENT AS IT STANDS

Run against the live ledger, not read from the source.

**1.01 The tree is empty, and structurally cannot be filled.**
`abyss.py status` reports **0 of 250 rows declare a condition** — the instrument's own output says *"the tree is flat until they do."* The cause is upstream: `kkr.py` contains **no reference to `precondition` anywhere**. The gate does not validate it, `cmd_ingest`'s passthrough list does not carry it, and no prompt asks a forecaster for it. **abyss.py reads a field that nothing in the pipeline can write.** It has never had anything to draw. That is the whole finding, and everything in §5 follows from it.

**1.02 What is built, and is good.**
The classifier walks conditions to fixed point with **transitive foreclosure** — a question standing on a collapsed question is itself collapsed. The status separation is correct and load-bearing: *void is our defect, foreclosed is the world's path,* and neither enters the Brier. **Shadow mass** — the count of sealed questions a single resolution killed — is computed and ranked. Retrofit detection compares `date_issued` against the parent's `resolved_date` and refuses conditions declared after the fact, rendering the offending edge in red rather than trusting it. `check` exits 1 on any violation, so it is CI-wireable. Standard library only; writes nothing to the ledger.

**1.03 Defects found in the implementation.**

a. **`requires` is unvalidated.** `pre.get("requires")` is compared against status strings but never checked at seal. A typo (`"hits"`, `"HIT"`) silently makes the row unforeclosable — it can never match, so it never collapses, and it sits in the scoring population looking conditional while behaving flat. Needs a gate check against `{hit, miss}`.

b. **No cycle guard.** `classify` iterates to fixed point; a precondition cycle (A requires B, B requires A) does not crash it, but neither node ever resolves and both sit LIVE forever, invisible. A cycle check belongs at seal, not at render.

c. **Retrofit detection has a hole.** It fires only when the parent has a `resolved_date`. A child sealed after its parent's *deadline passed* but before the operator got around to adjudicating it is not caught — and that window is where the laundering opportunity actually lives, because the operator controls when resolution happens. The predicate should be `date_issued > min(parent.resolved_date, parent.deadline)`.

d. **Roots filter drops live-flat rows.** `roots` requires `i in kids or state[i] != "open"`, so an open row with no children and no parent never renders. Correct for a tree view, worth stating on the face so the SVG isn't read as the whole ledger.

e. **Foreclosure has no keyed/keyless interaction.** A foreclosed row carries an unresolved 4.02f determination forever. Harmless, but the field should be marked N/A on foreclosure rather than left `unset`, or it will read as an outstanding gap in every conformance count.

---

## 2. THE MODEL — rev 0 WITHDRAWN

Rev 0 proposed sealing whole trees as single commitments with conserved mass. **That is the wrong architecture and it is withdrawn.** The implementation's model is better on three counts:

- **Every node is already a fully gated, sealed, scored KKR row.** No new sealing machinery, no new seal construction, no second book. The tree is a *reading* of the ledger, not a structure beside it — the same relation `arms.json` and `domains.json` have to identity and domain.
- **Trees emerge rather than being declared.** A forecaster does not have to see the whole structure at seal time. They declare one edge — *this row stands on that one* — and the shape assembles itself. That matches how causal-chain reasoning actually arrives.
- **Grafting is free and needs no residual accounting.** A new row declaring a precondition on a still-open parent *is* a graft, already legal, already dated, already sealed.

**Adopted: the per-row precondition model.** Rev 0's mass conservation, residual bookkeeping, and whole-tree sealing are dropped. What survives from rev 0 is §2's causal-chain qualification, the no-figure-nodes rule, and the machine-shadow/operator-rule separation — carried forward below.

---

## 3. PRIOR ART — THE HONEST FINDING

**3.01 Foreclosure is occupied.** Metaculus **conditional pairs**, live since 2023, implement the identical semantic: when a parent resolves Yes, the "if No" conditional is **annulled and not scored**; questions that are annulled are no longer open for forecasting and are excluded from scoring. Their own live questions carry the line *"this branch was annulled because the parent question resolved Yes."*

That is foreclosure. Same rule, same reason, published first, at scale. **The core mechanic of abyss.py is not novel and must not be claimed as such.** Rev 0 listed platform conditionals as a sweep target; the sweep returns them as occupant, not neighbour.

**3.02 The adjacent literature is also occupied.** Conditional prediction markets and decision markets (Hanson's market scoring rule line; Chen–Kash on decision-market incentives) price conditional claims and handle the unrealised branch. Proper scoring for conditional forecasts is formalised (Boeken–Zoeter–Mooij 2025, observational vs counterfactual correctness). Preregistration's HARKing literature (Kerr 1998; Nosek et al.) owns the general form of "a hypothesis declared after the result is known is not a prediction."

**3.03 What survives, scoped and falsifiable.** Three things, and the claim is their *conjunction on a self-published operator ledger*, not any one alone:

a. **Retrofit detection as an enforced, published integrity check.** Metaculus does not need this — the *platform* creates conditional pairs, so a forecaster cannot backdate a condition. A solo forecaster on a self-published ledger **can**, and it is the cheapest possible laundering of a miss into a non-event. `abyss check` detects it mechanically, refuses to honour the edge, keeps the row in the scoring population, and renders the violation in red. This is the same structural move as the keyed/keyless split: a per-entry pre-registration requirement that makes a self-published record auditable by a stranger who trusts neither the operator nor the repo. **No prior art found for it in one search — which is one search, not a sweep. It must be swept properly before the claim ships (RPAS 7.03).**

b. **Transitive foreclosure.** Metaculus conditionals are *pairs* — one level, no cascade. Foreclosure propagating through arbitrary depth, so that a question standing on collapsed ground is itself collapsed, is a different object from an annulled pair.

c. **Shadow mass as a published measure.** Platforms annul silently, as bookkeeping. Nothing found publishes *"this single resolution killed N sealed questions"* as a reported figure. It is the operational counterpart of the desk's own keystone — pathing necessitates a blind region — made countable rather than argued.

**3.04 The honest formulation for the face.** Not *"a new kind of forecasting."* Rather: *conditional forecasting is established practice; this desk adds the integrity machinery a self-published ledger requires and a platform does not, and reports the collapse the record casts on itself.* That is a smaller claim than "unique in the world," and it is the one that survives contact.

---

## 4. DOCTRINE

**4.01 Declaration.** A projection may carry `"precondition": {"id": "<parent KKR id>", "requires": "hit"|"miss"}`. It is declared at seal, inside the sealed preimage, or it does not exist.

**4.02 The retrofit rule (must).** A precondition is honoured only if the child was sealed while the parent was still open — `date_issued <= min(parent.resolved_date, parent.deadline)`. A condition declared after its parent could have been known **is not honoured**: the row stays in the scoring population and is scored as issued, and the violation is printed by id and rendered in red. *A condition declared after the fact can launder a miss into a foreclosure*, and this rule is the whole reason the instrument can be trusted by a stranger.

**4.03 Foreclosure is not void, and neither is scored.** VOID is the desk's defect, withdrawn with a reason. FORECLOSED is the world's path — a sound question that never met the world. Both are excluded from every Brier; scoring a foreclosed row in either direction invents a result. They are reported separately and never share a bucket.

**4.04 Causal-chain qualification (carried from rev 0).** A precondition edge must carry a **mechanism** — one sentence on why the parent's outcome produces pressure toward the child. An edge asserting only sequence or correlation is rejected. This excludes market-threshold chaining ("Brent above 90, then above 100") which is distributional, not causal, and belongs flat.

**4.05 No figure-nodes.** A node may cite figures in its resolution basis; a node that *is* a figure — an index level, a variance, a rate — does not qualify as tree material. The tree measures structural foresight. The flat arms already price distributions.

**4.06 Machine shadows, operator rules (carried from rev 0).** Where a keyless resolver can detect that a parent's failure condition has tripped, the display may mark descendants provisionally collapsed. **Shadowing writes nothing.** Foreclosure is entered only on operator adjudication of the parent. This preserves the duecheck finding: of eight probed endpoints, four would have written wrong verdicts. A machine that greys is useful; a machine that rules is a defect class already refused.

**4.07 The coverage exploit — OPEN, and the model does not close it.**
Under §2's adopted model, foreclosed rows are unscored. So a forecaster can seal *both* branches at a fork: one forecloses unscored, the other scores. **That is a free option, and it is exactly the "forecasting every possibility" failure the operator named.** Rev 0 closed it with mass conservation; the per-row model has no equivalent and currently has no answer.

Proposed fix, for the operator's ruling — **the sibling-set declaration**: rows sealed as alternatives at the same fork must declare a shared `fork_id` at seal, and the gate requires their probabilities to sum to ≤ 1.0 with the shortfall printed as declared residual. Covering the fork then forces every branch's probability down; a forecaster who covers everything publishes a set of low-confidence claims and scores like one. Hedging is not forbidden — it is **rendered as dilution**, visibly, on the face. The complement measure is **fork concentration** (max sibling probability), printed beside shadow mass so that breadth and conviction are both legible.

This is the one open design question in the doctrine. Everything else above is either implemented or specified.

---

## 5. BUILD GAPS — in dependency order

1. **`kkr.py` cannot write a precondition.** Gate validation, `cmd_ingest` passthrough, and seal-preimage inclusion. Until this lands nothing else matters, because the field is unwritable and the tree is empty by construction.
2. **Gate checks:** `requires ∈ {hit, miss}` (1.03a); cycle detection (1.03b); parent exists and is open at seal; mechanism sentence present (4.04).
3. **Retrofit predicate widened** to `min(resolved_date, deadline)` (1.03c).
4. **Fork-set machinery**, if the operator rules 4.07 in.
5. **Live face** — `abyss_tree.svg` is generated but not linked from nav or sitemap. The real-time death display is the product, and it currently ships to a file nobody can reach.
6. **`abyss check` into CI** — it exits 1 on violation and belongs in the spion or conformance run, where an integrity failure surfaces without being asked for.

---

## 6. WHAT TO SAY ON THE FACE

> Conditional forecasting is established practice — Metaculus conditional pairs annul the branch the world removed, and have since 2023. This desk claims no originality on the semantic. What it adds is the machinery a self-published ledger needs and a platform does not: a condition is honoured only if it was sealed while its parent was still open, violations are printed by id, foreclosure propagates through depth, and the number of sealed questions each resolution collapsed is published as a figure. Void is our defect. Foreclosed is the world's path. Neither is scored, and they never share a bucket.

That paragraph concedes the mechanic, names the addition, and states the discipline — which is the desk's standing form, and it is stronger than a novelty claim that would not survive its own prior-art sweep.
