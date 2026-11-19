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

| Metric | Value |
|---|---:|
| Branch refs | 1,294 |
| Unique HEADs summed within repositories | 1,208 |
| Live SHA observations | 1,079 |
| Dated census SHA values not individually re-fetched in this pass | 215 |
| Repositories in live branch-audit tranche | 60 |
| Records in live branch-audit tranche | 1,077 |

The branch inventory JSON/CSV merges the existing 1,075 live branch observations, the two newly discovered memory-repository refs and 14 priority PR-head observations. The 215 remaining SHA values retain their dated census provenance. This is not a claim that every branch HEAD was freshly queried in this pass.

Branch protection for the 1,292 historical refs remains sourced from the prior census. The two newly discovered refs have protection state `null / NOT_CHECKED`. No new live protection query was available in this audit pass.

## 3. Open pull requests

Current repository-scoped discovery returned **206 open PRs across all 92 repositories**. The previous 548-row PR map is retained only as a historical snapshot and has been replaced in the canonical map.

- 206 PRs have discovery-level repository, number, title and URL.
- 14 priority PRs have live `get_pr_info` metadata including head/base branch, SHA, draft, mergeability and change counts.
- 192 PRs remain `DISCOVERY_ONLY_GET_PR_INFO_PENDING`; no head/base SHA, review or CI state is inferred for them.

Canonical artifacts:
- `registry/OPEN_PR_BRANCH_MAP_2026-11-20.json`
- `registry/OPEN_PR_BRANCH_MAP_2026-11-20.csv`

## 4. Newly registered cognitive-memory component

Repository: [synergy_hierarchical_cognitive_memory_architecture](https://github.com/Shtenco/synergy_hierarchical_cognitive_memory_architecture)

- Main SHA from current PR base metadata: `74b518c85d3a69fdc2e868737cbe9f4f2cac761c`.
- Feature branch HEAD from current PR metadata: `37bebe6e8d75444ced7e610b821664892eabe0f8`.
- PR #1: 80 commits, 25 files, 1,538 additions, 1 deletion; Draft; GitHub reported mergeable at metadata read.
- Latest associated CI run for the inspected head was cancelled; the job contained no execution steps. No green CI claim is made.
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
- 112 commits, 25 files, 2,924 additions; Draft and mergeable at metadata read.
- Current branch contains full-domain self-consistent Poisson–drift–diffusion v0.6 and a 20/40/80-cell convergence harness, but the numerical study has not been executed and traps remain specification-only.
- No device measurement, fabrication, or petahertz digital processor is claimed.

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

1. Fetch exact branch HEAD SHA and protection status for the 215 branches still carrying historical census SHA values.
2. Enrich the remaining 192 open PRs with head/base SHA, stacked dependencies, reviews and exact-head CI.
3. Complete source audits for the remaining candidate repositories; this report does not mark the prior 53-repository backlog complete.
4. Design and review a typed memory contract, then implement authenticated adapters and cross-repository E2E tests.
5. Restore CI execution evidence for Autopilot, AI Coder, AI Language, Long Term Harness and cognitive memory.
6. Reconcile stale PR #2 in `synergy_project` and refresh its repository count/scope.

**No merge, branch deletion, force-push, secret rotation or deployment was performed in this pass.**
