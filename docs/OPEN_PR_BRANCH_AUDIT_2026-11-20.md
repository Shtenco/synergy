# SYNERGY — Open PR / Branch Association Audit

**Snapshot:** 2026-11-20  
**Scope:** repository-scoped open PR discovery across all 92 owner repositories.

## Current discovery

- Repositories queried: **92/92**
- Currently open PRs discovered: **206**
- PRs with live `get_pr_info` enrichment in the priority pass: **14**
- PRs still marked `DISCOVERY_ONLY_GET_PR_INFO_PENDING`: **192**

The previous 548-row PR map was a dated snapshot and is superseded as a current total. It must not be used as the present open-PR count.

## Metadata coverage

For 14 priority PRs, the canonical JSON/CSV includes current title, state, draft flag, mergeability, head/base branches, head/base SHAs, commit count and changed-file/addition/deletion counts. For the remaining 192 PRs only repository, number, title and URL are recorded; no head/base SHA, draft state, review or CI result is inferred.

Priority PRs enriched:
- `synergy_hierarchical_cognitive_memory_architecture#1`
- `synergy_motherboard_xpu_xml#4`
- `synergy_system#54`
- `synergy_long_term_harness#1–#4`
- `synergy_agi_autopilot#24`
- `synergy_ai_coder#7`
- `synergy_ai_language#35`
- `synergistic_economics#17`
- `synergy_maps#9`
- `synergy_project#2`
- `synergy_pay_system#24`

## Known stacked PR chains and blockers

- `synergy_long_term_harness`: #1 → #2 → #3 → #4; all Draft, all CI runs failed with job records containing `steps=null`; no live provider or sandbox E2E is verified.
- `synergy_ai_coder#7`: based on `feat/autonomous-engineering-foundation-20261114`; requires parent-chain review and exact-head CI.
- `synergy_ai_language#35`: based on `feature/repository-impact-graph`; semantic-memory schema is present on the feature branch, not yet a proven cross-repo runtime contract.
- `synergy_agi_autopilot#24`: based on `hardening/m12-independent-verification-v1`; conditional dispatch and uncertain-state fencing are implemented in source, but hosted CI has no executed steps.
- `synergy_maps#9` and `synergistic_economics#17`: target feature branches rather than `main`; base ancestry and CI must be reviewed before promotion.
- `synergy_project#2`: still describes an 89-repository assessment, is Draft and reports `mergeable=false`; reconcile against 92 current repositories.

## CI and review policy

A PR is not merge-ready because GitHub reports `mergeable=true`. Require:
1. exact head SHA;
2. current base SHA and merge-base/ancestry;
3. reviews and unresolved review threads;
4. completed exact-head CI with executed steps and retained logs/artifacts;
5. security and authority-boundary review;
6. explicit disposition for stacked dependencies.

A workflow job with `steps=null` is classified as **execution evidence unavailable**, not as a test assertion failure. A cancelled or queued run is not a pass.

## Canonical artifacts

- [Current PR map JSON](../registry/OPEN_PR_BRANCH_MAP_2026-11-20.json)
- [Current PR map CSV](../registry/OPEN_PR_BRANCH_MAP_2026-11-20.csv)
- [Live reconciliation](LIVE_RECONCILIATION_2026-11-20.md)

No PR was merged, closed, retargeted or force-updated by this audit.
