# SYNERGY live reconciliation — 2026-11-20

## 1. Owner inventory

The connected GitHub installation currently exposes **92 repositories** under `Shtenco`:

| Metric | Live value |
|---|---:|
| Total repositories | 92 |
| Public | 16 |
| Private | 76 |
| Archived | 0 |
| Default branch `main` | 92 / 92 |

The 92nd repository, absent from the prior 91-repository owner registry, is `Shtenco/synergy_hierarchical_cognitive_memory_architecture`.

## 2. Branch inventory

| Metric | Live value |
|---|---:|
| Branch refs | **1,294** |
| Unique HEADs summed within repositories | **1,208** |
| Branch refs with non-historical SHA provenance | **1,294 / 1,294** |
| Refs with compare-to-main ancestry in this pass | **210** |
| Refs still needing ancestry comparison | **1,084** |
| Ancestry result: AHEAD / BEHIND / DIVERGED / IDENTICAL | **36 / 22 / 120 / 32** |
| Repositories in prior live branch-audit tranche | **60** |
| Records in prior live branch-audit tranche | **1,077** |

All branch HEADs in the canonical inventory now have non-historical SHA provenance from the same-day live branch audit, priority PR metadata or the new compare-to-main pass. The 210 compared refs have current ancestry fields; the other 1,084 have live SHA values but have not yet been ancestry-compared in this pass.

Branch protection remains a separate permission-dependent audit. The prior census marked 0/1,292 refs protected; the two newly discovered cognitive-memory refs have protection state `null / NOT_CHECKED`. No fresh administrative branch-protection query was completed.

## 3. Open pull requests

Current repository-scoped discovery returned **549 open PRs across all 92 repositories**. The previous 548-row PR map is retained only as a historical snapshot and has been replaced in the canonical map.

- 549 PRs have discovery-level repository, number, title and URL.
- 18 priority PRs have live `get_pr_info` metadata including head/base branch, SHA, draft, mergeability and change counts.
- 531 PRs remain `DISCOVERY_ONLY_GET_PR_INFO_PENDING`; no head/base SHA, review or CI state is inferred for them.

Canonical artifacts:
- `registry/OPEN_PR_BRANCH_MAP_2026-11-20.json`
- `registry/OPEN_PR_BRANCH_MAP_2026-11-20.csv`

## 4. Newly registered cognitive-memory component

Repository: [synergy_hierarchical_cognitive_memory_architecture](https://github.com/Shtenco/synergy_hierarchical_cognitive_memory_architecture)

- Main SHA from current PR base metadata: `74b518c85d3a69fdc2e868737cbe9f4f2cac761c`.
- Feature branch HEAD from current PR metadata: `2d6d7872653b9d525a74046e992a843b2a905d57`.
- PR #1: 84 commits, 25 files, 1,542 additions, 1 deletion; Draft; GitHub reported mergeable at metadata read.
- Latest current-head CI run 44634673642 is queued; no completed test steps or green CI claim exist.
- No PR reviews were recorded at the time of inspection.

### Source findings

The feature branch contains a provider-independent memory implementation with:
- L0 system core and append-only prompt history;
- budgeted context retrieval and model-profile registry;
- L2 hierarchical key/value, FTS5, graph and optional vector retrieval;
- L3 immutable versions, SHA-256 provenance and source snapshots;
- candidate consolidation and read-only repository ingestion.

Promotion blockers:
1. API routes have no authentication/authorization and are documented as local-development only.
2. Repository ingestion does not explicitly reject symlink files or prove resolved-path containment before reading.
3. The current `sources` index uses URI as a primary key while ingestion stores repository-relative paths; multiple repositories in one shared store can collide.
4. No shared typed memory contract or cross-repository E2E receipt exists.

The component was added to `synergy_system/registry/REPOSITORY_INTERFACES.json` as `ARCHITECTURAL_ONLY`, not as an integrated runtime edge. A single uncontracted component gap is recorded in `INTEGRATION_GAPS.json`. One P1 deployment/promotion blocker was added to `SECURITY_BLOCKERS.json`.

## 5. Priority source and integration review

### AI Autopilot — PR #24
- 95 commits, 13 files, 1,835 additions, 181 deletions; Draft and mergeable at metadata read.
- Source contains idempotent task creation, conditional single-winner execution claim, an `uncertain` fence, explicit approval for external writes and hard denial for payment/accounting/blockchain/host-shell capabilities.
- Associated CI run failed at job level with `steps=null`; this is not evidence that tests executed and failed.

### AI Coder — PR #7
- 167 commits, 19 files, 3,323 additions, 51 deletions; Draft and mergeable at metadata read.
- Context archive envelope binds source size and SHA-256; decoding enforces archive/output limits and exact restored length/hash. SQLite archive records have immutable update/delete triggers and namespace-scoped retrieval.
- The archive explicitly states namespace filtering is not authorization.
- Associated CI job failed with `steps=null`; no test execution is attested.

### AI Language — PR #35
- 143 commits, 20 files, 1,674 additions, 138 deletions; Draft and mergeable at metadata read.
- Semantic memory export is deterministic and content-addressed; credential-like fields and common token formats are redacted; prompt export is opt-in; schema is strict.
- The semantic-memory schema exists on the PR branch, not yet proven as a cross-repository runtime contract with the new cognitive-memory repository.
- All four Python matrix jobs failed with `steps=null`; no test execution is attested.

### XPU / UV-LWC — PR #4
- 118 commits, 25 files, 2,998 additions; Draft and mergeable at metadata read.
- Current branch contains full-domain self-consistent Poisson–drift–diffusion v0.6 and a 20/40/80-cell convergence harness, but the numerical study has not been executed and traps remain specification-only.
- Current exact-head CI runs 44634951360 and 44634951388 are queued. No device measurement, fabrication, or petahertz digital processor is claimed.

### SUMI — `synergy_system` PR #54
- One documentation file, 309 lines; Draft and mergeable at metadata read.
- The audit correctly identifies the missing compute-job/resource/model-artifact/receipt/verification contract family.
- No CI run or review evidence was returned.

### Long Term Harness — PRs #1–#4
- Four open Draft PRs form a stacked chain: #1 → #2 → #3 → #4.
- The latest free-first OpenRouter design has no live provider test, no certified execution sandbox and no independent verifier.
- All four associated CI runs failed with job records containing `steps=null`; no green test claim is valid.

### Other stale or stacked PRs
- `synergy_project` PR #2 is still titled for an 89-repository assessment, is Draft and currently `mergeable=false`; its scope must be rebased/reconciled against the 92-repository live inventory.
- `synergy_maps` PR #9 and `synergistic_economics` PR #17 target non-main feature branches; they require base-chain and exact-head CI review before promotion.
- `synergy_pay_system` PR #24 is a Draft audit artifact, not a verified settlement implementation.

## 6. System registry reconciliation

| Registry | Current value |
|---|---:|
| Owner inventory | 92 repositories |
| Architecture/interface registry | 76 repositories |
| Existing contract families | 39 |
| Runtime adapter edges | 44 |
| E2E-tested edges | 0 |
| Uncontracted candidate components | 1 |
| Security blockers | 4 P0 + 1 P1 |

Owner inventory and interface registry are different scopes. A repository in the owner inventory does not automatically become an interface participant or integrated runtime component.

## 7. Evidence rules

- `ARCHITECTURAL_ONLY` is not an integration.
- `ADAPTER_INTEGRATED` is not E2E-tested.
- A workflow failure with `steps=null` is classified as runner/CI evidence unavailable, not as a test assertion failure.
- A cancelled or queued workflow is not a pass.
- A PR marked mergeable is not approved, reviewed or production-ready.
- No branch is deleted, merged or force-updated by this reconciliation.

## 8. Remaining work

1. Fetch exact branch HEAD SHA and protection status for the 210 branches still carrying historical census SHA values.
2. Enrich the remaining 531 open PRs with head/base SHA, stacked dependencies, reviews and exact-head CI.
3. Complete source audits for the remaining candidate repositories; this report does not mark the prior 53-repository backlog complete.
4. Design and review a typed memory contract, then implement authenticated adapters and cross-repository E2E tests.
5. Restore CI execution evidence for Autopilot, AI Coder, AI Language, Long Term Harness and cognitive memory.
6. Reconcile stale PR #2 in `synergy_project` and refresh its repository count/scope.

**No merge, branch deletion, force-push, secret rotation or deployment was performed in this pass.**


## 9. Additional financial and execution audit deltas

- `synergy_agi_autopilot#24`: source contains conditional single-winner task claim, idempotency, uncertain-state fencing and approval-gated external effects. Exact-head Actions jobs failed with `steps=null`; no test execution is attested.
- `synergy_ai_coder#7`: bounded content-addressed archive and immutable SQLite records are implemented on the feature branch; namespace filtering is not authorization. Exact-head CI has no executed steps.
- `synergy_ai_language#35`: deterministic semantic-memory records and secret redaction exist on the feature branch; no cross-repo E2E with the new memory repository is proven.
- `synergy_financial_os#39`: transactional accounting outbox is present; the inspected outbox validates a caller-supplied hash but does not itself authenticate signer identity. CI has no executed steps.
- `synergy_pay_system#24`: the audit records critical settlement-lifecycle findings; PR #24 changes only an audit document, not the runtime fixes. Settlement evidence, finality, actual fill amounts, reconciliation and ledger posting are not one proven E2E path.
- `synergy_agentic_ai_economy#10`: modeled bridge/AMM fee estimates are separated from HardNAV and a verified-receipt journal is added, but the corrected 13,000-block replay remains pending; old fee-inclusive metrics are superseded.
- `synergy_usds#9`: six-level CPMM flywheel is a bounded research simulation, not a live yield mechanism. P0 deployer-key issue remains open through security PR #6; external key migration/rotation is manual and unverified.

The central integration-gap registry now records three observed contract/lifecycle risks in addition to the one uncontracted cognitive-memory component. The federation still has 39 contract families, 44 adapter edges and zero E2E-tested edges.


## 10. Complete SHA provenance and partial ancestry pass

All **1,294/1,294** branch refs now have non-historical SHA provenance in the canonical JSON/CSV. A fresh compare-to-main ancestry pass covered 210 refs: 36 AHEAD, 22 BEHIND, 120 DIVERGED and 32 IDENTICAL. The remaining 1,084 refs have SHA observations from the earlier same-day live branch audit or priority PR metadata but still need a compare-to-main ancestry result. No branch protection state was refreshed; the 1,292 historical refs retain the old 0-protected census and two new refs remain unchecked.
