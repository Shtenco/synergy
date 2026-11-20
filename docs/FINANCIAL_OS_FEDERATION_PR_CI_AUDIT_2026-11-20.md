# Financial OS and federation PR / CI audit — 2026-11-20

## Scope and inventory

A live REST inventory of all pull requests was collected from `synergy_financial_os` and `synergy_system`. Both endpoints returned fewer than 100 records, so the first page covers the complete observed PR set.

| Repository | PR total | Open | Closed | Draft | Merged |
|---|---:|---:|---:|---:|---:|
| `synergy_financial_os` | 39 | 39 | 0 | 36 | 0 |
| `synergy_system` | 54 | 47 | 7 | 48 | 2 |
| **Total** | **93** | **86** | **7** | **84** | **2** |

There are **78 direct dependency edges** where a PR's `base.ref` equals another PR's head branch. This is a very high stack density: the repositories need explicit parent-first integration plans, not bulk merging by PR number. Three branch names are used by two PRs each:
- Financial OS: `feat/distribution-available-capacity-v4-refund-restored-20260828` is head for PR #32 and #33.
- System: `feat/economic-os-rc5-canonical-capture-ready-20260828` is head for PR #34 and #35.
- System: `feat/economic-os-rc4-local-persistence-restart-20260828` is head for PR #31 and #32.

These duplicated head refs make a naive one-parent-per-child dependency graph ambiguous; review PR base refs and exact SHAs, not only branch names.

## Financial OS — distribution/accounting and external-profit chain

### Stack and branch age

The distribution/accounting chain runs through PRs #1–#33. Its newer children include:
- PR #32/#33: same head branch for DistributionAvailableCapacity v4.
- PR #37: External Profit Bus accounting, based on that shared v4 branch.
- PR #38: External Profit Import, also based on that shared v4 branch.
- PR #39: separate Federation V3 eligible-asset growth truth proposal.

The current main-vs-branch ancestry sample:
- PR #38 head `feat/external-profit-import-v1-20260905`: **452 ahead / 24 behind** after this pass's fixes.
- Shared parent branch `feat/distribution-available-capacity-v4-refund-restored-20260828`: **444 ahead / 24 behind** after the package-discovery fix.
- PR #39 `federation-v3-domain-expansion`: **23 ahead / 24 behind**.

PR #38 itself contains 7 commits / 5 files / 614 additions and PR #37 contains 6 commits / 4 files / 533 additions. Their parent branch is much larger, so the incremental child diffs must not be mistaken for the entire integration size.

### External Profit Import V1 source review

The importer is a fail-closed accounting boundary, not a generic cash inflow shortcut. Its source currently:
- Requires a fixed schema ID, non-empty source/evidence IDs, 64-character hex evidence and route digests, provider references and source repository.
- Uses finite `Decimal` amounts, non-negative canonical P&L and a JSON boolean admissibility flag.
- Allows posting only for `REALIZED_EXTERNAL_PNL`; unresolved classifications, internal marks, capital reallocation, not-realized and inadmissible inputs are non-postable.
- Requires positive realized P&L, admissibility, and external cash delta at least as large as the canonical P&L.
- Posts double-entry external cash / external revenue only when settlement asset equals reporting currency; USD and USDT are not implicitly interchangeable.
- Requires the target accounts to be EXTERNAL ASSET and EXTERNAL REVENUE; ledger duplicate-reference protection remains active.

**Audit-integrity defect found and fixed:** arbitrary envelope metadata was expanded after authoritative fields in the posted ledger metadata, so a caller could override `source`, `source_repository`, `settlement_asset`, `route_digest`, `provider_references` or `economic_class`. The importer now rejects those six reserved keys, and six parameterized regression cases were added.

Commits on the PR #38 head branch:
- `1accffbadaf3593bd8dbb08b85893636a5fc70db` — reject reserved audit metadata keys.
- `37fdb3b2ae8c2a70815d36020e910a283567d84f` — add six negative tests.
- The branch also has explicit setuptools package discovery, so `config`, `schemas` and `fixtures` are not auto-discovered as Python packages.

**Shared parent package-discovery defect found and fixed:** a prior canonical-core CI run for PR #37 failed during editable-install metadata generation because setuptools auto-discovered `config`, `schemas`, `fixtures` and `sinergy_financial_os` as competing top-level packages. The shared v4 parent branch now explicitly declares `[tool.setuptools.packages.find]` with `include = ["sinergy_financial_os*"]` and `exclude = ["tests*"]`. This places the fix at the shared parent rather than only in one child.

New exact-head workflows for PR #38 and the shared parent were queued at the last check:
- PR #38 canonical-core CI: run [44673424885](https://github.com/Shtenco/synergy_financial_os/actions/runs/44673424885).
- PR #38 External Profit Import V1: run [44673424697](https://github.com/Shtenco/synergy_financial_os/actions/runs/44673424697).
- Shared parent canonical-core CI: run [44673594162](https://github.com/Shtenco/synergy_financial_os/actions/runs/44673594162).
- Shared parent DistributionAvailableCapacity v4: run [44673594230](https://github.com/Shtenco/synergy_financial_os/actions/runs/44673594230).

No post-fix green result is claimed yet. After the source/test commits, PR #38's External Profit Import workflow (run `44673424697`) failed before runner allocation (`runner_id=0`, zero steps); its canonical-core run `44673424885` remained queued. The shared parent canonical-core run `44673594162` also failed before runner allocation, while the DistributionAvailableCapacity v4 run `44673594230` remained queued. The earlier PR #38 attempts at SHA `5338ded...` failed before runner steps; the earlier PR #37 packaging failure was a real runner-side setuptools error. Thus the package and metadata fixes remain unverified by CI.

### PR #39

The federation V3 eligible-asset growth branch is 23 ahead / 24 behind, Draft, 23 commits / 8 files / 1,219 additions. Both exact-head workflow runs failed before runner steps. It remains blocked pending runnable CI and stack/rebase review.

## SYNERGY System — federation PRs

### Federation V3 chain

- PR #46 is the root integration branch, based on main: 5 commits / 5 files / 818 additions; exact-head `Federation V3 Validate` push and PR checks succeeded.
- PR #47 builds on PR #46 with typed contracts/runtime types/cross-repo tests: 23 commits / 18 files / 1,348 additions; exact-head `Federation V3 Contracts` checks succeeded.
- PR #48 builds on PR #47 with secure event fabric: 16 commits / 13 files / 1,617 additions; both contract and event-fabric checks succeeded.
- All three are non-Draft and reported mergeable in the metadata snapshot, but the stack is not independently mergeable in arbitrary order. Their base branches are nested; parent-first sequencing is mandatory.
- Their head SHAs are old (September 6) and their ancestry comparisons show substantial divergence from the current main snapshot: PR #46/#47/#48 are not certified against current main by old green CI alone. Re-run exact-head checks after an intentional rebase/restack before any merge.

### Other priority federation PRs

**PR #54 — SUMI Phase 0 audit**
- Draft; 1 commit / 1 file / 309 additions; branch 1 ahead / 139 behind current main.
- `mergeable=false` in the inspected metadata and no exact-head Actions run is visible. It is an audit document, not proof that integrations are working.

**PR #49 — PQ Federation Trust Registry**
- Non-Draft; 71 commits / 48 files / 8,957 additions; reported mergeable, but exact-head Federation V5 workflows failed before runner steps (`runner_id=0`, empty steps).
- Its branch is 71 ahead / 337 behind current main. The size and staleness demand a scoped review and fresh CI, not an automatic merge.

## Decisions

- **KEEP:** preserve Financial OS and SYNERGY System as separate authority domains.
- **DEVELOP:** parent-first restack of the distribution/accounting chain; maintain external-profit evidence binding; parent-first federation chain #46 → #47 → #48.
- **BLOCKED:** Financial OS PR #37/#38 until the new workflows execute; PR #39 until runner/CI; System PR #54 until rebase/conflict and CI evidence; PR #49 until fresh CI and a scoped review.
- **MERGE-READY:** none of the reviewed Financial OS or System PRs in this pass. Old green checks on PR #46–#48 are positive historical evidence, but not a current-main revalidation.
- No PR was merged or closed, no branch was deleted, and no force-push was performed.

## Evidence links

- [Financial OS PR #38](https://github.com/Shtenco/synergy_financial_os/pull/38)
- [Financial OS PR #37](https://github.com/Shtenco/synergy_financial_os/pull/37)
- [Financial OS PR #39](https://github.com/Shtenco/synergy_financial_os/pull/39)
- [SYNERGY System PR #46](https://github.com/Shtenco/synergy_system/pull/46)
- [SYNERGY System PR #47](https://github.com/Shtenco/synergy_system/pull/47)
- [SYNERGY System PR #48](https://github.com/Shtenco/synergy_system/pull/48)
- [SYNERGY System PR #49](https://github.com/Shtenco/synergy_system/pull/49)
- [SYNERGY System PR #54](https://github.com/Shtenco/synergy_system/pull/54)
