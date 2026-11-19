# SYNERGY — master ecosystem registry

**Каноническая точка входа в экосистему Shtenco / SYNERGY.** Этот репозиторий хранит owner inventory, карту доменов, ссылки на архитектурные и экономические досье, а также сводные реестры веток, PR и интеграционных доказательств. Исходники и история каждого продукта остаются в самостоятельных репозиториях.

## Live governance snapshot — 2026-11-20

| Показатель | Текущее значение |
|---|---:|
| Доступные owner repositories | **92** |
| Public / Private / Archived | **16 / 76 / 0** |
| Default branch `main` | **92/92** |
| Branch refs | **1294** |
| Unique HEADs (sum within repositories) | **1208** |
| Branch SHA from live audit / PR metadata | **1083** |
| SHA values retained from dated census | **211** |
| Currently open PRs discovered repository-by-repository | **549** |
| PRs with full metadata enriched in this pass | **8** |
| PRs still discovery-only | **198** |
| Security blockers | **4 P0 + 1 P1** |
| E2E-tested federation edges | **0** |

**Interpretation:** 92 repositories are an inventory of assets, not 92 production systems. A branch name or PR title is not proof of implementation. Adapter presence is not E2E execution. CI is green only when the exact HEAD has completed test steps and retained evidence.

## Canonical registries and audit reports

- [Owner repository inventory JSON](registry/repos.json)
- [Branch inventory JSON](registry/BRANCH_INVENTORY_2026-11-20.json)
- [Branch inventory CSV](registry/BRANCH_INVENTORY_2026-11-20.csv)
- [Live branch audit JSON — 60 repositories / 1,077 records](registry/LIVE_BRANCH_AUDIT_2026-11-20.json)
- [Open PR map JSON — 549 current discoveries](registry/OPEN_PR_BRANCH_MAP_2026-11-20.json)
- [Open PR map CSV](registry/OPEN_PR_BRANCH_MAP_2026-11-20.csv)
- [Live reconciliation report](docs/LIVE_RECONCILIATION_2026-11-20.md)
- [Security blockers](https://github.com/Shtenco/synergy_system/blob/main/registry/SECURITY_BLOCKERS.json)
- [Repository/interface registry — 76 components](https://github.com/Shtenco/synergy_system/blob/main/registry/REPOSITORY_INTERFACES.json)
- [Integration gaps — 39 contract families plus 1 uncontracted component](https://github.com/Shtenco/synergy_system/blob/main/registry/INTEGRATION_GAPS.json)

### Provenance limitations

- 1,077 branch SHA values have live audit/PR metadata provenance. The remaining 211 SHA values are retained from the dated census and were not individually re-fetched in this pass.
- Protection state for the two new cognitive-memory refs is unknown; old protection values remain from the prior census.
- The 549 PR discovery records contain full head/base metadata for 8 priority PRs; the other 198 remain explicitly marked `DISCOVERY_ONLY_GET_PR_INFO_PENDING`.
- The old 91-repository and 548-PR reports remain historical artifacts; they are not current totals.

## Architecture ownership

| Repository | Responsibility |
|---|---|
| [`synergy`](https://github.com/Shtenco/synergy) | Umbrella owner inventory, ecosystem map, registry navigation |
| [`synergy_system`](https://github.com/Shtenco/synergy_system) | Governance, authority boundaries, contracts, interface registry, security gates |
| [`synergy_project`](https://github.com/Shtenco/synergy_project) | Economic master dossier, capital, finance, science and industrial development |
| [`synergy_megaproject`](https://github.com/Shtenco/synergy_megaproject) | Civilizational research graph and frontier technology catalog |
| [`synergy_meta_os`](https://github.com/Shtenco/synergy_meta_os) | Node/service lifecycle and capability orchestration |
| [`synergy_net`](https://github.com/Shtenco/synergy_net) | P2P transport and mesh data plane |
| [`synergy_ai_blockchain`](https://github.com/Shtenco/synergy_ai_blockchain) | PQ mesh primitives, Agent Fabric and trust evidence |
| [`synergy_agi_nexus`](https://github.com/Shtenco/synergy_agi_nexus) / [`synergy_agi_olga`](https://github.com/Shtenco/synergy_agi_olga) | Intelligence architecture and research lineages |
| [`synergy_hierarchical_cognitive_memory_architecture`](https://github.com/Shtenco/synergy_hierarchical_cognitive_memory_architecture) | Candidate hierarchical memory engine; not yet integrated |
| [`synergy_ai_coder`](https://github.com/Shtenco/synergy_ai_coder) | Evidence-bound coding and recursive context archive |
| [`synergy_ai_language`](https://github.com/Shtenco/synergy_ai_language) | Semantic requirements, code intelligence and semantic-memory export |
| [`synergy_long_term_harness`](https://github.com/Shtenco/synergy_long_term_harness) | Long-horizon Manager/Executor/Auditor control-plane harness |
| [`synergy_financial_os`](https://github.com/Shtenco/synergy_financial_os) / [`synergy_pay_system`](https://github.com/Shtenco/synergy_pay_system) | Financial authority and settlement |
| [`synergy_midas_ai`](https://github.com/Shtenco/synergy_midas_ai) / [`synergy_market_graph`](https://github.com/Shtenco/synergy_market_graph) | Market intelligence and trading research |

These are responsibility boundaries, not assertions of live runtime integration.

## Full owner repository inventory

| Repository | Domain | Maturity label | Visibility | Default branch |
|---|---|---|---|---|
| [`3D_bars_market_structure`](https://github.com/Shtenco/3D_bars_market_structure) | trading-quant | LEGACY_RND | public | main |
| [`computer_vision_trading_metatrader_5`](https://github.com/Shtenco/computer_vision_trading_metatrader_5) | trading-quant | LEGACY_RND | public | main |
| [`cross_forex_arbitrage_trading_metatrader_5`](https://github.com/Shtenco/cross_forex_arbitrage_trading_metatrader_5) | trading-quant | LEGACY_RND | public | main |
| [`dlp_solver`](https://github.com/Shtenco/dlp_solver) | science-research | ACTIVE_EXPERIMENTAL | private | main |
| [`global_liquidity_dataminer`](https://github.com/Shtenco/global_liquidity_dataminer) | trading-quant | LEGACY_RND | public | main |
| [`midas_lite`](https://github.com/Shtenco/midas_lite) | trading-quant | LEGACY_RND | public | main |
| [`print_money_synergychain`](https://github.com/Shtenco/print_money_synergychain) | finance-economy | STUB_SPEC_ONLY | private | main |
| [`quantum-trading_metatrader5`](https://github.com/Shtenco/quantum-trading_metatrader5) | trading-quant | LEGACY_RND | public | main |
| [`shtenco_micro_ai`](https://github.com/Shtenco/shtenco_micro_ai) | compute-os | RND_CANDIDATE | private | main |
| [`shtenco_multi_threaded_trading_robot_with_machine_learning_python`](https://github.com/Shtenco/shtenco_multi_threaded_trading_robot_with_machine_learning_python) | trading-quant | LEGACY_RND | public | main |
| [`shtenco.github.io`](https://github.com/Shtenco/shtenco.github.io) | presentation | PRESENTATION_CANDIDATE | public | main |
| [`shtencoauantai.github.io`](https://github.com/Shtenco/shtencoauantai.github.io) | presentation | PRESENTATION_CANDIDATE | public | main |
| [`sinergy_app`](https://github.com/Shtenco/sinergy_app) | apps-interface | STUB_SPEC_ONLY | private | main |
| [`sinergy_super_app`](https://github.com/Shtenco/sinergy_super_app) | apps-interface | CANDIDATE | private | main |
| [`swap_arbitrage_metatrader_5`](https://github.com/Shtenco/swap_arbitrage_metatrader_5) | trading-quant | LEGACY_RND | public | main |
| [`synegy_ai_compress`](https://github.com/Shtenco/synegy_ai_compress) | compute-os | CANDIDATE | private | main |
| [`synergistic_economics`](https://github.com/Shtenco/synergistic_economics) | finance-economy | RND_SIMULATION | public | main |
| [`synergy`](https://github.com/Shtenco/synergy) | architecture-governance | ARCHITECTURAL_MASTER | private | main |
| [`synergy_2chain_qe`](https://github.com/Shtenco/synergy_2chain_qe) | finance-economy | RND_CANDIDATE | private | main |
| [`synergy_adaptive_engine`](https://github.com/Shtenco/synergy_adaptive_engine) | trading-quant | CANDIDATE | private | main |
| [`synergy_agentic_ai_economy`](https://github.com/Shtenco/synergy_agentic_ai_economy) | agi-agentic | RND_SIMULATION | private | main |
| [`synergy_agi_autopilot`](https://github.com/Shtenco/synergy_agi_autopilot) | agi-agentic | STUB_SPEC_ONLY | private | main |
| [`synergy_agi_nexus`](https://github.com/Shtenco/synergy_agi_nexus) | agi-agentic | CANDIDATE | private | main |
| [`synergy_agi_olga`](https://github.com/Shtenco/synergy_agi_olga) | agi-agentic | CANDIDATE | private | main |
| [`synergy_agi_trader`](https://github.com/Shtenco/synergy_agi_trader) | agi-agentic | CANDIDATE | private | main |
| [`synergy_ai_blockchain`](https://github.com/Shtenco/synergy_ai_blockchain) | blockchain-protocol | CANDIDATE | private | main |
| [`synergy_ai_coder`](https://github.com/Shtenco/synergy_ai_coder) | agi-agentic | CANDIDATE | private | main |
| [`synergy_ai_company`](https://github.com/Shtenco/synergy_ai_company) | agi-agentic | STUB_SPEC_ONLY | private | main |
| [`synergy_ai_economic`](https://github.com/Shtenco/synergy_ai_economic) | finance-economy | STUB_SPEC_ONLY | public | main |
| [`synergy_ai_financial_system`](https://github.com/Shtenco/synergy_ai_financial_system) | finance-economy | RND_LOCAL_TESTING | private | main |
| [`synergy_ai_investment_committee`](https://github.com/Shtenco/synergy_ai_investment_committee) | trading-quant | CANDIDATE | private | main |
| [`synergy_ai_language`](https://github.com/Shtenco/synergy_ai_language) | agi-agentic | RND | private | main |
| [`synergy_ai_llm_rwkv`](https://github.com/Shtenco/synergy_ai_llm_rwkv) | compute-os | RND | private | main |
| [`synergy_ai_trade_terminal`](https://github.com/Shtenco/synergy_ai_trade_terminal) | trading-quant | RND | private | main |
| [`synergy_ai_workspace`](https://github.com/Shtenco/synergy_ai_workspace) | apps-interface | STUB_SPEC_ONLY | private | main |
| [`synergy_algotrading_graph_system`](https://github.com/Shtenco/synergy_algotrading_graph_system) | trading-quant | STUB_SPEC_ONLY | private | main |
| [`synergy_app`](https://github.com/Shtenco/synergy_app) | apps-interface | CANDIDATE | private | main |
| [`synergy_app_family`](https://github.com/Shtenco/synergy_app_family) | apps-interface | STUB_SPEC_ONLY | private | main |
| [`synergy_apps`](https://github.com/Shtenco/synergy_apps) | apps-interface | ARCHITECTURAL_MASTER | private | main |
| [`synergy_binary_quantum_theory`](https://github.com/Shtenco/synergy_binary_quantum_theory) | science-research | ACTIVE_EXPERIMENTAL | public | main |
| [`synergy_blochain_budget`](https://github.com/Shtenco/synergy_blochain_budget) | finance-economy | CANDIDATE | private | main |
| [`synergy_cashero`](https://github.com/Shtenco/synergy_cashero) | finance-economy | SECURITY_BLOCKED | public | main |
| [`synergy_chain`](https://github.com/Shtenco/synergy_chain) | blockchain-protocol | CANDIDATE | private | main |
| [`synergy_chain_print_money`](https://github.com/Shtenco/synergy_chain_print_money) | finance-economy | STUB_SPEC_ONLY | private | main |
| [`synergy_cold_nuclear`](https://github.com/Shtenco/synergy_cold_nuclear) | research-other | RND_SCIENCE | private | main |
| [`synergy_complex_matrix_multiplication`](https://github.com/Shtenco/synergy_complex_matrix_multiplication) | compute-os | ACTIVE_EXPERIMENTAL | private | main |
| [`synergy_computing_topology`](https://github.com/Shtenco/synergy_computing_topology) | compute-os | ACTIVE_EXPERIMENTAL | private | main |
| [`synergy_crypto_pump`](https://github.com/Shtenco/synergy_crypto_pump) | trading-quant | CANDIDATE | private | main |
| [`synergy_epstein_network`](https://github.com/Shtenco/synergy_epstein_network) | graph-research | CANDIDATE | private | main |
| [`synergy_eurasian`](https://github.com/Shtenco/synergy_eurasian) | finance-economy | MODEL_SPEC_READY | public | main |
| [`synergy_financial_os`](https://github.com/Shtenco/synergy_financial_os) | finance-economy | RND_FEDERATION | private | main |
| [`synergy_gguf_compress`](https://github.com/Shtenco/synergy_gguf_compress) | compute-os | STUB_SPEC_ONLY | private | main |
| [`synergy_gllm_nexus`](https://github.com/Shtenco/synergy_gllm_nexus) | agi-agentic | CANDIDATE | private | main |
| [`synergy_graph_print_money`](https://github.com/Shtenco/synergy_graph_print_money) | finance-economy | CANDIDATE | private | main |
| [`synergy_hierarchical_cognitive_memory_architecture`](https://github.com/Shtenco/synergy_hierarchical_cognitive_memory_architecture) | agi-agentic | CANDIDATE | private | main |
| [`synergy_lead_search_engline`](https://github.com/Shtenco/synergy_lead_search_engline) | search-growth | RND | private | main |
| [`synergy_long_term_harness`](https://github.com/Shtenco/synergy_long_term_harness) | agi-agentic | STUB_SPEC_ONLY | private | main |
| [`synergy_maps`](https://github.com/Shtenco/synergy_maps) | apps-interface | STUB_SPEC_ONLY | private | main |
| [`synergy_market_graph`](https://github.com/Shtenco/synergy_market_graph) | trading-quant | CANDIDATE | private | main |
| [`synergy_market_maker`](https://github.com/Shtenco/synergy_market_maker) | trading-quant | CANDIDATE | private | main |
| [`synergy_marketvision`](https://github.com/Shtenco/synergy_marketvision) | trading-quant | CANDIDATE | private | main |
| [`synergy_matrix_sota`](https://github.com/Shtenco/synergy_matrix_sota) | compute-os | STUB_SPEC_ONLY | private | main |
| [`synergy_megaproject`](https://github.com/Shtenco/synergy_megaproject) | research-strategy | ACTIVE_RESEARCH | private | main |
| [`synergy_messenger`](https://github.com/Shtenco/synergy_messenger) | apps-interface | HARDENED_ALPHA | private | main |
| [`synergy_meta_api`](https://github.com/Shtenco/synergy_meta_api) | protocol-transport | STUB_SPEC_ONLY | private | main |
| [`synergy_meta_os`](https://github.com/Shtenco/synergy_meta_os) | compute-os | CANDIDATE | private | main |
| [`synergy_metachain`](https://github.com/Shtenco/synergy_metachain) | blockchain-protocol | CANDIDATE | private | main |
| [`synergy_metaverse`](https://github.com/Shtenco/synergy_metaverse) | apps-interface | STUB_SPEC_ONLY | private | main |
| [`synergy_midas_ai`](https://github.com/Shtenco/synergy_midas_ai) | trading-quant | CANDIDATE | private | main |
| [`synergy_midas_ai_trading_system`](https://github.com/Shtenco/synergy_midas_ai_trading_system) | trading-quant | LEGACY_RND | private | main |
| [`synergy_midas_institutional`](https://github.com/Shtenco/synergy_midas_institutional) | trading-quant | CANDIDATE | private | main |
| [`synergy_motherboard_xpu_xml`](https://github.com/Shtenco/synergy_motherboard_xpu_xml) | compute-os | CANDIDATE | private | main |
| [`synergy_net`](https://github.com/Shtenco/synergy_net) | protocol-transport | CANDIDATE | private | main |
| [`synergy_nexus_science_agent`](https://github.com/Shtenco/synergy_nexus_science_agent) | agi-agentic | CANDIDATE | private | main |
| [`synergy_pay_system`](https://github.com/Shtenco/synergy_pay_system) | finance-economy | CANDIDATE | private | main |
| [`synergy_post_quantum_radio`](https://github.com/Shtenco/synergy_post_quantum_radio) | protocol-transport | STUB_SPEC_ONLY | private | main |
| [`synergy_project`](https://github.com/Shtenco/synergy_project) | architecture-governance | RND | private | main |
| [`synergy_qe`](https://github.com/Shtenco/synergy_qe) | finance-economy | STUB_SPEC_ONLY | private | main |
| [`synergy_qr_compress`](https://github.com/Shtenco/synergy_qr_compress) | compute-os | CANDIDATE | private | main |
| [`synergy_quantlab`](https://github.com/Shtenco/synergy_quantlab) | trading-quant | CANDIDATE | private | main |
| [`synergy_relative_value`](https://github.com/Shtenco/synergy_relative_value) | trading-quant | CANDIDATE | private | main |
| [`synergy_riskguard`](https://github.com/Shtenco/synergy_riskguard) | trading-quant | CANDIDATE | private | main |
| [`synergy_search_engline`](https://github.com/Shtenco/synergy_search_engline) | finance-economy | RND | private | main |
| [`synergy_shhts`](https://github.com/Shtenco/synergy_shhts) | protocol-transport | STUB_SPEC_ONLY | private | main |
| [`synergy_shttps`](https://github.com/Shtenco/synergy_shttps) | protocol-transport | STUB_SPEC_ONLY | private | main |
| [`synergy_system`](https://github.com/Shtenco/synergy_system) | architecture-governance | ARCHITECTURAL_MASTER | private | main |
| [`synergy_trademux`](https://github.com/Shtenco/synergy_trademux) | trading-quant | CANDIDATE | private | main |
| [`synergy_triangle_money_system`](https://github.com/Shtenco/synergy_triangle_money_system) | finance-economy | ACTIVE_EXPERIMENTAL | private | main |
| [`synergy_turbo_linux`](https://github.com/Shtenco/synergy_turbo_linux) | compute-os | SECURITY_BLOCKED | private | main |
| [`synergy_usds`](https://github.com/Shtenco/synergy_usds) | finance-economy | SECURITY_BLOCKED | private | main |
| [`synergy.github.io`](https://github.com/Shtenco/synergy.github.io) | presentation | PRESENTATION_CANDIDATE | public | main |
| [`synergychain.github.io`](https://github.com/Shtenco/synergychain.github.io) | blockchain-protocol | PRESENTATION_CANDIDATE | private | main |

## Federation rules

1. Keep repositories independent; do not collapse the federation into a monorepo.
2. Every authority has one canonical owner. AI recommendations are not authorization; UI state is not ledger state; transport is not settlement.
3. Every cross-repository edge requires a versioned contract, source-pinned adapters and exact-head evidence.
4. `ARCHITECTURAL_ONLY`, `CONTRACT_DEFINED`, `PARTIAL_IMPLEMENTATION` and `ADAPTER_INTEGRATED` are different states. Only reproducible cross-repository tests may produce `E2E_TESTED`.
5. No promotion based only on README, PR body, branch name or model-generated claim.
6. Preserve historical and experimental branches until provenance, dependency and PR review justify a separate archival decision.
7. Security blockers are deployment/promotion gates, not documentation suggestions.

## Security posture

Four unresolved P0 credential/security blockers remain in `synergy_usds`, `synergy_cashero`, `synergy_turbo_linux` and `synergy_ai_trade_terminal`. A P1 production/promotion blocker is recorded for the cognitive-memory candidate: unauthenticated local API, symlink ingestion boundary and cross-repository source-identity collision risks. Secret rotation/revocation is not claimed unless externally evidenced.

## Current next gates

- Re-fetch exact HEAD SHA and branch protection for the 211 branches still carrying historical census SHAs.
- Enrich 198 remaining open PRs with head/base SHA, reviews, stacked dependencies and exact-head CI.
- Complete the remaining source audits; the earlier 53-repository backlog is not marked complete.
- Define the cognitive-memory contract and prove authenticated, namespace-safe integration with AI Language, AI Coder and Long Term Harness.
- Restore actionable CI evidence for Autopilot, AI Coder, AI Language, Long Term Harness and cognitive memory.
- Reconcile stale portfolio PRs against the 92-repository owner inventory.

---
*Generated from connected GitHub inventory and repository-scoped PR discovery on 2026-11-20. No source branches were merged, deleted or force-updated by this README refresh.*
