# SYNERGY — Open PR / Branch Association Audit

**Snapshot:** 2026-11-20  
**Scope:** one repository-scoped `is:open` search for each of the 92 owner repositories.

## Current discovery

- Repositories queried individually: **92/92**
- Currently open PRs discovered: **549**
- PRs with live `get_pr_info` enrichment in the priority pass: **18**
- PRs still marked `DISCOVERY_ONLY_GET_PR_INFO_PENDING`: **531**

The 549 count is the sum of individual repository searches. Earlier multi-repository search batches returned incomplete results and are not used as the final count. The older 548-row map was a previous snapshot; one current PR is now present in the 92nd repository.

## Metadata coverage

For 18 priority PRs, the canonical JSON/CSV includes title, state, draft flag, mergeability, head/base branches, head/base SHAs, commit count and change counts. For the other 531 PRs, only repository, number, title and URL are recorded; no head/base SHA, draft state, review or CI result is inferred.

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
- `synergy_financial_os#39`
- `synergy_usds#6, #9`
- `synergy_agentic_ai_economy#10`

## Known stacked PR chains and blockers

- `synergy_long_term_harness`: #1 → #2 → #3 → #4; all Draft, all CI runs failed with job records containing `steps=null`; no live provider or sandbox E2E is verified.
- `synergy_ai_coder#7`: based on `feat/autonomous-engineering-foundation-20261114`; requires parent-chain review and exact-head CI.
- `synergy_ai_language#35`: based on `feature/repository-impact-graph`; semantic-memory schema is present on the feature branch, not yet a proven cross-repo runtime contract.
- `synergy_agi_autopilot#24`: based on `hardening/m12-independent-verification-v1`; conditional dispatch and uncertain-state fencing are implemented in source, but hosted CI has no executed steps.
- `synergy_maps#9` and `synergistic_economics#17`: target feature branches rather than `main`; base ancestry and CI must be reviewed before promotion.
- `synergy_project#2`: still describes an 89-repository assessment, is Draft and reports `mergeable=false`; reconcile against 92 current repositories.
- `synergy_usds#6`: open non-Draft security PR; removal of committed deployer key and external key migration/rotation are still manual blockers.

## CI and review policy

A PR is not merge-ready because GitHub reports `mergeable=true`. Require exact head/base SHA, reviews, unresolved threads, completed exact-head CI with executed steps, security review and explicit disposition for stacked dependencies.

A workflow job with `steps=null` is classified as **execution evidence unavailable**, not as a test assertion failure. A cancelled or queued run is not a pass.

## Canonical artifacts

- [Current PR map JSON](../registry/OPEN_PR_BRANCH_MAP_2026-11-20.json)
- [Current PR map CSV](../registry/OPEN_PR_BRANCH_MAP_2026-11-20.csv)
- [Live reconciliation](LIVE_RECONCILIATION_2026-11-20.md)

No PR was merged, closed, retargeted or force-updated by this audit.
