# High-Branch Repository Audit — 2026-11-20

**Scope:** ten repositories with the largest branch counts, plus targeted CI/evidence review of the highest-priority Binary Quantum Gravity branches.  
**Source:** 2026-11-20 branch inventory and open-PR map, exact branch HEADs and selected GitHub Actions runs.  
**Important:** branch count is not implementation count. Multiple refs may point to one commit; a passing workflow is valid only for its exact HEAD SHA.

## 1. Highest branch-count repositories

| Repository | Branch refs | Distinct HEADs | Duplicate refs | Open PRs | Draft / ready | PRs targeting non-main |
|---|---:|---:|---:|---:|---:|---:|
| synergy_binary_quantum_theory | 178 | 167 | 11 | 51 | 27 / 24 | 16 |
| synergy_ai_language | 129 | 105 | 24 | 25 | 13 / 12 | 10 |
| synergy_system | 62 | 60 | 2 | 47 | 43 / 4 | 40 |
| synergy_agi_nexus | 58 | 57 | 1 | 19 | 16 / 3 | 0 |
| synergychain.github.io | 52 | 48 | 4 | 25 | 20 / 5 | 0 |
| synergy_gllm_nexus | 48 | 47 | 1 | 24 | 23 / 1 | 0 |
| synergy_financial_os | 40 | 40 | 0 | 39 | 36 / 3 | 0 |
| synergy_agi_olga | 38 | 37 | 1 | 11 | 5 / 6 | 0 |
| synergy_midas_ai | 35 | 20 | 15 | 5 | 4 / 1 | 3 |
| synergy_meta_os | 33 | 32 | 1 | 28 | 26 / 2 | 23 |

The largest branch-management concerns are:

- **synergy_ai_language:** 24 branch names point to one HEAD (180746a0268c), with no open PR attached to those aliases. Twenty of its 25 open PRs have not been updated for more than 90 days.
- **synergy_midas_ai:** 16 branch names point to one HEAD (d568685cff70), including multiple tmp/noop and release-test names; none of those duplicate aliases has an open PR.
- **synergy_binary_quantum_theory:** ten old research/bqg-2t branch names point to one HEAD (b03bf253a43a), with no open PR. Two experiment branches share another HEAD (326b53733b68), also without an open PR.
- **synergy_system:** 40 of 47 open PRs target non-main bases. This is a highly stacked integration graph; only seven PRs target main.
- **synergy_financial_os:** 39 open PRs, 36 drafts; all 40 branch refs have distinct HEADs. This is a large active development queue, not a merged production release.

No branch was deleted or renamed. Duplicate HEADs are cleanup candidates only after PR, tag, release, workflow and external-reference checks.

## 2. Binary Quantum Gravity — 178 branches / 51 open PRs

### Branch topology

- 178 branch refs, 167 distinct HEAD commits, 11 duplicate refs.
- 51 open PRs: 27 draft, 24 ready-for-review.
- 35 PRs target main; 16 target other branches.
- No open PR in this repository is older than 90 days by last-updated timestamp.
- Ten old research/bqg-2t branch aliases share one commit and have no open PR. Two experiment aliases share another commit and have no open PR.
- The K5 V19/V20 branch pair shares the same HEAD; only the V19 branch is the head of open PR #71.

### Current high-priority PR branch evidence

| PR | Branch / current HEAD | Current evidence | Assessment |
|---|---|---|---|
| #87 | integration/bqg-proof-index-mirror-spectral-20261119 / 131d9d180c90 | Three selected workflows passed on the exact HEAD: physical-history reference diagnostics, mirror-mass/Wilson-Dirac finite gate, HDA compression algebra regression | Useful proof-index integration candidate; still Draft and not merged |
| #86 | research/w5-v09-v10-repro-20261119 / 96ec89b83950 | Paired regression tests and original V09/V10 suites passed; actual frozen-seed comparison was cancelled; matrix run left many jobs queued and some failed after runner shutdown/cancellation | No completed paired numerical result or final artifact |
| #85 | research/bqg-q2-correspondence-audit-hardening-20261119 / e7ac35b4c3ec | Latest visible Q2 workflow runs used older HEADs (1cd471…, 55553…, 3250f…); none matched current branch HEAD | Exact-HEAD validation is missing |
| #84 | research/bqg-intrinsic-clock-lorentzian-bridge-20261116 / 785363b61271 | Direct all-M W5 workflow failed on exact HEAD; invariant/shadow tests passed, but the long actual commutator process was terminated after the runner received a shutdown signal | Infrastructure cancellation, not a demonstrated numerical assertion failure; no complete all-M evidence |
| #71 | research/v19-canonical-k5-replay-20261015 / 1a715e22d10b | Numerical continuation succeeded; higher-shell and L1-q4 evidence jobs passed; core regression failed before downstream gates | Partial exact finite K5 result; not a completed physicalization |

### PR #71 — what actually passed

The workflow logs establish the following bounded results:

1. **Higher-shell:** downloaded 31 certified exact source columns; independently recomputed heavy column 28; reassembled exact 32D Lambda and block-Lanczos matrices; canonical spectrum guard passed.
2. **L1 q4:** downloaded and audited 24 certified source columns; recomputed S4 six-edge metric compression; canonical metric-value guard passed.
3. **Finite K5 bridge:** the script reported an exact finite SU(2) K5 algebra test as passed and replayed a saved vector. Its own scope note explicitly excludes the real Lorentzian EEF Hamiltonian, HDA closure, a continuum phase, matter and experiment.
4. **K5 completion is still false:** the log reports direct reverse column incomplete; only 50 of 352 required direct-HE inputs available; zero new HE inputs; zero second-CK actions; full error not certified; physicalization incomplete.

### PR #71 — why core regression failed

The canonical-core workflow stopped at scripts/audit_core_scope.py. It rejected the retired vocabulary “mirror” in seven files:

- research/v15_k5_32input/README_RU.md
- research/v18_k5_feshbach/test_v18_schur.py
- research/v18_k5_feshbach/v18_schur_audit.py
- research/v17_k5_parity/README_RU.md
- research/v16_k5_full_initial/README_RU.md
- research/v19_canonical_k5/replay_k5.py
- research/v19_canonical_k5/README_RU.md

Because the scope gate failed, all subsequent canonical-core tests were skipped. This is a deterministic source-policy blocker, separate from the numerical continuation success. No branch was modified in this audit.

## 3. Review priorities

1. **BQG PR #86 / #84:** rerun the expensive W5 all-M/paired seed jobs on a stable runner; do not label cancellation as a mathematical pass or failure.
2. **BQG PR #85:** obtain CI on exact HEAD e7ac35b4c3ec before using its Q2 results as current.
3. **BQG PR #71:** resolve the seven retired-vocabulary hits under a reviewed patch, then rerun the complete canonical-core suite. Preserve the passed higher-shell and L1 q4 artifacts separately.
4. **synergy_ai_language / synergy_midas_ai:** classify same-HEAD branch aliases; preserve history and check external PR references before any cleanup.
5. **synergy_system:** reduce stacked-PR complexity by validating dependency order and merging only evidence-complete slices. Forty PRs currently target non-main bases.

## 4. Non-negotiable evidence rule

A branch existing, a PR being ready, or a workflow passing on an older SHA is not evidence that the current branch head passed. Every scientific claim must bind to exact commit SHA, workflow run, input manifest, output artifact and stated physical scope.
