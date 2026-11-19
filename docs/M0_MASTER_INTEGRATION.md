> **Inventory reconciliation update — 2026-11-20:** live GitHub exposes **91/91 owner repositories**. The umbrella registry and master graph now contain 91 records; three historical repository-name mismatches were corrected and ten post-baseline repositories are tracked with explicit maturity/evidence limits. The 81-repository M0 source/capability audit dated 2026-10-08 remains the deep baseline; the later additions must not be silently promoted to the same audit status. The complete branch inventory records **1,292 refs** across all 91 repositories (1,206 summed unique HEADs within repositories; 86 repeated refs). See [branch inventory JSON](../registry/BRANCH_INVENTORY_2026-11-20.json), [CSV](../registry/BRANCH_INVENTORY_2026-11-20.csv), and [summary](BRANCH_INVENTORY_2026-11-20.md).

---

# M0 MASTER INTEGRATION — 91/91 owner inventory · 81/81 deep baseline

**Deep baseline audit date:** 2026-10-08  
**Current inventory snapshot:** 2026-11-20  
**Scope:** all 91 repositories visible to the installed GitHub App for `Shtenco`; deep source/capability audit baseline remains 81 repositories.

## Result

The previous count of 68 was wrong as an ecosystem count: it was only a name-mask count for `synergy|sinergy|synegy`.

M0 originally inventoried **81 / 81 repositories** and treated membership as a graph/content question rather than a naming question. The live owner inventory is now **91 / 91**; the ten post-baseline records are tracked in the umbrella registry with explicit maturity and audit limitations.

## Current 91-repository inventory and branch census

- Owner inventory: **91/91**; no missing or extra repository names versus the installed GitHub inventory at this snapshot.
- Branch refs: **1,292** across the 91 repositories.
- Sum of unique branch HEADs within repositories: **1,206**.
- Repeated refs pointing to an already represented HEAD within the same repository: **86**.
- Protected branch refs reported by GitHub API: **0/1,292**, including all 91 default branches.
- Every repository has a `main` branch in this snapshot.
- The branch census records names, HEAD SHAs, protection flags and default-branch identity. It does not by itself establish branch content quality, PR disposition, CI status, deployment or safety of deletion.

Canonical branch artifacts: [JSON](../registry/BRANCH_INVENTORY_2026-11-20.json) · [CSV](../registry/BRANCH_INVENTORY_2026-11-20.csv) · [report](BRANCH_INVENTORY_2026-11-20.md).

## What was inspected

For every repository the M0 pass inspected:

- root structure;
- README when present;
- latest commit/activity;
- architecture/status language;
- explicit cross-repository references where visible.

## Key findings

1. **`synergy_system` is an architectural constitution/federation root**, while **`Shtenco/synergy` is now the umbrella portfolio/master index**.
2. **`synergy_midas_ai` explicitly federates legacy repositories** such as `midas_lite`, computer-vision trading, cross-FX arbitrage, swap arbitrage, global-liquidity datamining, multi-threaded ML trading and quantum-trading research.
3. Maturity must be first-class: the portfolio contains architectural masters, candidates, active experiments, legacy R&D, hardened alpha, specification-only stubs and security-blocked nodes.
4. Repository names are not authoritative. Example: **`synergy_search_engline` currently describes a HARDNAV / triangular non-inflationary economy**, so M0 classifies it under finance/economy rather than search.
5. Security gating is required before federation promotion. M0 flags `synergy_cashero` and `synergy_usds` as **SECURITY_BLOCKED** from committed-credential indicators, and `synergy_turbo_linux` for credential-file review.

## Canonical artifacts

- `registry/repos.json` — complete 91-repository owner inventory.
- `registry/master_graph.json` — machine-readable graph nodes/edges/capabilities/maturity.
- `registry/BRANCH_INVENTORY_2026-11-20.json` — every branch ref and HEAD SHA across all 91 repositories.
- `docs/MASTER_GRAPH.md` — human-readable dependency map.
- `docs/M0_MASTER_INTEGRATION.md` — this audit.
- GitHub Project target: https://github.com/users/Shtenco/projects/3

## Authority rule

`Shtenco/synergy` indexes and orchestrates. It does not silently replace the source-of-truth responsibilities of `synergy_system`, financial ledgers, blockchain runtimes, validation labs, or child repositories.

## M1 target

M1 should convert the repository graph into a **runtime capability graph**:

`repo -> capability -> interface -> artifact -> runtime -> agent -> task -> evidence`

and continuously reconcile it with GitHub Project #3.
