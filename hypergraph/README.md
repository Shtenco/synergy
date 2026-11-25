# SYNERGY Hypergraph Core — V3

This directory is the machine-readable inventory and evidence-aware graph seed for the ecosystem audit.

## Files
- `nodes.json`: live owner-inventory repository nodes keyed by immutable GitHub repository ID.
- `edges.json`: registry-declared dependency edges. Every edge is `candidate` until source evidence verifies it.
- `coverage.json`: measurable inventory and audit coverage.
- `gaps.json`: unresolved inventory, evidence, contract and overlap gaps.
- `proposals.json`: proposed components, deliberately separate from actual repositories.
- `evidence/registry-snapshot.json`: provenance for the existing umbrella registry snapshot.
- `schemas/`: JSON Schema contracts for graph nodes and n-ary hyperedges.

## Evidence rules
1. Repository names are not identities; GitHub repository IDs are.
2. A registry dependency is a candidate edge, not proof of an import or runtime call.
3. `candidate`, `reviewed`, `verified`, and `rejected` are separate states. `verified` requires reproducible source or runtime evidence.
4. Proposed components are not repository inventory entries.
5. Hashes establish byte identity, not truth, authorization or correctness.
6. The owner listing returned 100 records in this observation. Do not infer that 100 is the account's final total or repeat the historical 112 claim without ID-level reconciliation.

## Next audit sequence
1. Reconcile repository IDs beyond the current listing cap.
2. Audit README, manifests, source imports, API routes, event schemas, tests and workflows in batches.
3. Replace registry-only candidate edges with file- and revision-specific evidence.
4. Extract contracts and validate compatibility.
5. Run overlap analysis before proposing new repositories.
