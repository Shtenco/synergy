# AI Language and BQT — PR, dependency and CI audit (2026-11-20)

## Scope and inventory

A paginated GitHub REST `pulls?state=all&per_page=100&page=1` inventory was performed separately for both repositories. Each repository returned fewer than 100 PRs, so page 1 is complete for the observed endpoint snapshot.

| Repository | Total PRs | Open | Closed | Draft | Merged |
|---|---:|---:|---:|---:|---:|
| `synergy_ai_language` | 35 | 25 | 10 | 14 | 9 |
| `synergy_binary_quantum_theory` | 87 | 51 | 36 | 29 | 31 |
| **Total** | **122** | **76** | **46** | **43** | **40** |

The closed-but-not-merged PRs are not assumed to be accepted work; closure and merge are distinct. The machine-readable inventory retains PR number, title, state, draft flag, exact head/base refs and SHAs, merge timestamp, updated timestamp and URL.

## PR dependency graph

Twenty-four direct dependency edges were detected where a PR's `base.ref` exactly equals another PR's head branch. These are explicit branch-stack relationships, not inferred semantic relationships.

### AI Language

- PR #24 → #23 → #22 → #21: chained semantic/accounting requirement overlay.
- PR #35 is based on the already-merged repository-impact graph branch from PR #20.
- NEXUS chain: #16 → #12 → #10 → #9; #12 and #11 both branch from #10; #14 branches from #11; #15 and the closed #13 branch from #9.
- These stacks must be reviewed parent-first. A child PR is not independently merge-ready merely because its own diff is small.

### Binary Quantum Theory

- Latest W5 chain: PR #86 → #84 → #83 → #81; PR #82 also branches from #81.
- Q2 relational history chain includes #49 → #48 → #47 → #45 → #44, with #46 also branching from #45.
- The current BQT repo has many parallel research lines; don't collapse them into one giant PR or merge by PR-number order.

## Exact-head CI evidence

### AI Language

**PR #35 — semantic-memory bridge**
- Exact head: `f0d724f6cc2a84afa09049dc889bcd3eb753b5eb`.
- Both push and pull_request CI runs failed; all four Python matrix jobs (3.10–3.13) show `runner_id=0` and no steps. This is a runner/startup failure, not evidence that tests failed.

**PR #33 — federation V3 semantic requirements**
- Exact head: `02a83b7834d168582fe5542fe4b83e9765bcce22`.
- CI reached a real runner. Dependency installation succeeded; Ruff lint failed and the test step was skipped.
- The log reports **195 lint errors**, all confined to seven frozen benchmark/teacher artifacts: `nexus_r74_blind22/run_teacher.py`, `nexus_r77_blind24/run_teacher.py`, `nexus_r78_blind25/run_teacher.py`, `nexus_r78_arbitration/native_authority.py`, `nexus_r79_blind26/run_teacher.py`, `nexus_r710_blind27/run_teacher.py` and `nexus_r712_blind28/run_teacher.py`. The errors are E701/E702, E401 and E722; the failure is not a pytest regression because pytest did not run.
- A narrow Ruff exclusion for exactly those seven frozen files was committed to the PR branch as `2283602887c835656603f3b79f77cb5733b8b8e2`. Runtime package and tests remain under the configured Ruff rules.
- Exact-head CI rerun `44673053300` was queued at the last status check; lint and tests are not yet verified after the fix.
- Recommendation: decide and encode the intended lint boundary (production package vs frozen benchmark/reproducibility scripts). Do not suppress lint globally; if frozen scripts are intentionally immutable, use a documented, narrow per-path exclusion and lint all maintained runtime code.

**PR #17 — AI Language v0.4 hardening**
- Exact-head push and pull_request CI both succeeded on the observed SHA. This is useful positive evidence, but the branch is substantially stale/diverged from current main (4 ahead / 66 behind in the current comparison) and cannot be merged without a rebase/stack review and fresh CI.

**PR #24 — accounting-close requirement overlay**
- Exact-head specialized workflows `accounting-close-requirements-v3` and `requirement-binding-v1` succeeded. Generic CI failed; do not treat the specialized green checks as a complete green required-check set.

### Binary Quantum Theory

**PR #87 — selective proof integration**
- Exact head: `131d9d180c90f9e578d0a8c713e5e74f62b1c7d4`.
- The `core-regression` run had 60 jobs: **59 succeeded and 1 failed**. The failed job was `canonical-core`; 40 earlier scientific/numerical checks within that job passed, including the scope, ledger, q=2, Peter–Weyl, HDA, Regge and TT checks.
- The final step `Registered canonical integration status` ran `bcqg_bit_to_gravity_final.py --strict` and exited 2. Its emitted JSON explicitly says candidate framework true, structural candidate not closed, core theory not closed, physicalization incomplete, and required physicalization gates still `open_physical` (common-scale calibration, connected interblock history, dynamical Maxwell kernel, IR six-vector, lensing dynamics, physical background/scalar cosmology, physical projector history and physical TT kernel).
- This is an intentional fail-closed scientific status gate, not a code defect to bypass. Do not remove `--strict`, set physicalization booleans true, or relabel the theory as experimentally confirmed just to obtain a green check.
- In the same PR's workflow matrix, 59/60 jobs succeeded and one final strict gate failed. This is meaningful positive evidence with one explicit release blocker; the PR remains Draft and not merge-ready.

**PR #84 — W5 direct all-M SU(2) commutator audit**
- Workflow run #44443956138 contains 42 jobs: one stale-run preflight succeeded, while 40 direct-all-M matrix jobs and the aggregate comparator failed.
- The direct matrix jobs compiled modules and passed their invariant unit tests, but the actual numerical commutator step was cancelled or did not complete. The aggregate artifact explicitly reports `INCOMPLETE_PRODUCTION_SHADOW_EQUIVALENCE`, `comparison_performed=false`, `input_columns_compared=0`.
- Therefore this run proves neither production/shadow equality nor inequality. It is an incomplete computation caused by missing matrix artifacts, not a numerical mismatch. Do not cite it as a scientific counterexample or a pass.

**PR #86 — paired W5 V09/V10 seed and cutoff audit**
- Exact head: `96ec89b83950de3a507eb269c4621d6bcbca09cf`.
- Two runs for the same SHA (push and pull_request) remained queued. In the last 100-run query, ten workflow runs were queued across five distinct SHAs, each SHA represented by both push and PR events.
- The workflow defines a 30-job matrix (3 cutoffs × 2 modes × 5 seed values), `max-parallel: 1`, and `cancel-in-progress: false`. This produces a queue-amplification risk: the current ten queued runs represent up to 300 matrix job executions before aggregation. The duplicate push/PR runs and sequential matrix policy should be rationalized before adding more commits.
- Do not claim the paired audit has run or passed; it is queued, not completed.

## Branch ancestry evidence

The central ancestry ledger now contains **187 / 1,202** non-main comparisons, with **1,015 pending**. AI Language PR #33's branch SHA was refreshed after the Ruff-scope fix; its current ancestry remains 2 ahead / 9 behind. Current statuses in the ledger: 8 ahead, 17 behind, 162 diverged. The 14 new AI Language/BQT comparisons show:
- AI Language semantic-memory bridge: 152 ahead / 63 behind; large, diverged integration, not a quick merge.
- AI Language federation V3 branch: 1 ahead / 9 behind.
- AI Language v0.4 hardening: 4 ahead / 66 behind.
- AI Language requirement chain branches are 1–20 ahead and 56 behind, with stacked dependencies.
- BQT latest proof-index integration branch: 56 ahead / 0 behind (ahead-only).
- BQT W5 and q2 research branches are very large and diverged (362–1,131 ahead, 26 behind in the inspected sample); branch names do not imply merge readiness.
- BQT v21 C1 repair branch is 622 ahead / 632 behind and is strongly diverged.

## Decisions

- **KEEP:** preserve the two independent research/product repositories and their separate histories.
- **DEVELOP:** continue PR stacks parent-first; refresh stale branches; isolate maintained runtime lint from frozen benchmark scripts without weakening runtime lint.
- **BLOCKED:** AI Language PR #33 by 195 Ruff errors; AI Language PR #35 by runner-startup failures; BQT PR #87 by the intentionally open strict physicalization gate; BQT PR #84 by incomplete/cancelled matrix evidence; BQT PR #86 by queued duplicate matrix load.
- **MERGE-READY:** none of the reviewed priority PRs.
- No branch was deleted, force-pushed, merged or archived in this pass.

## Evidence links

- [AI Language PR #35](https://github.com/Shtenco/synergy_ai_language/pull/35)
- [AI Language PR #33](https://github.com/Shtenco/synergy_ai_language/pull/33)
- [AI Language PR #17](https://github.com/Shtenco/synergy_ai_language/pull/17)
- [BQT PR #87](https://github.com/Shtenco/synergy_binary_quantum_theory/pull/87)
- [BQT PR #86](https://github.com/Shtenco/synergy_binary_quantum_theory/pull/86)
- [BQT PR #84](https://github.com/Shtenco/synergy_binary_quantum_theory/pull/84)
