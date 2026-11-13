> **Inventory reconciliation update — 2026-11-13:** live GitHub now exposes 89 repositories. The umbrella registry and master graph have been extended from 81 to 89; three renamed repositories were reconciled. Eight new entries (synergy_ai_llm_rwkv, synergy_ai_economic, synergy.github.io, synergy_meta_api, synergy_ai_workspace, synergistic_economics, synergy_metaverse, synergy_maps) have inventory-level classifications only. The detailed M0 capability audit remains the 81-repository baseline dated 2026-10-08; the eight additions still require the same source, dependency, security and evidence review.

---

# M0 MASTER INTEGRATION — 81/81 audit

**Audit date:** 2026-10-08  
**Scope:** every repository visible to the installed GitHub App for `Shtenco`.

## Result

The previous count of 68 was wrong as an ecosystem count: it was only a name-mask count for `synergy|sinergy|synegy`.

M0 now inventories **81 / 81 repositories** and treats membership as a graph/content question rather than a naming question.

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

- `registry/repos.json` — complete 81-repository inventory.
- `registry/master_graph.json` — machine-readable graph nodes/edges/capabilities/maturity.
- `docs/MASTER_GRAPH.md` — human-readable dependency map.
- `docs/M0_MASTER_INTEGRATION.md` — this audit.
- GitHub Project target: https://github.com/users/Shtenco/projects/3

## Authority rule

`Shtenco/synergy` indexes and orchestrates. It does not silently replace the source-of-truth responsibilities of `synergy_system`, financial ledgers, blockchain runtimes, validation labs, or child repositories.

## M1 target

M1 should convert the repository graph into a **runtime capability graph**:

`repo -> capability -> interface -> artifact -> runtime -> agent -> task -> evidence`

and continuously reconcile it with GitHub Project #3.
