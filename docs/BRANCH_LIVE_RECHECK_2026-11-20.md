# Live Branch-Name Recheck — 2026-11-20

**Owner:** `Shtenco`  
**Scope:** all 91 repositories returned by the authenticated owner inventory.  
**Result:** **91/91 repositories matched exactly** against the canonical branch census by branch name and per-repository count.

## Aggregate result

| Measure | Result |
|---|---:|
| Repositories | 91 / 91 |
| Live branch-name sets matched | 91 / 91 |
| Branch refs in canonical census | 1,292 |
| Main refs | 91 |
| Non-main refs | 1,201 |
| Summed unique HEADs within repositories | 1,206 |
| Repeated refs to an existing HEAD within same repo | 86 |

## Method

1. Retrieved the complete accessible repository inventory for owner `Shtenco`.
2. Queried the GitHub branch listing for every repository, following pagination until each result set was complete.
3. Compared each live branch-name set with the corresponding repository entry in [`registry/BRANCH_INVENTORY_2026-11-20.json`](../registry/BRANCH_INVENTORY_2026-11-20.json).
4. All 91 sets matched exactly: no branch-name additions, removals or count differences were found against the census.

## Per-repository reconciliation

| Repository | Live branch count | Census branch count | Unique HEADs in census | Repeated refs | Name-set result |
|---|---:|---:|---:|---:|---|
| [`Shtenco/shtenco.github.io`](https://github.com/Shtenco/shtenco.github.io) | 6 | 6 | 0 | MATCH |
| [`Shtenco/quantum-trading_metatrader5`](https://github.com/Shtenco/quantum-trading_metatrader5) | 2 | 2 | 0 | MATCH |
| [`Shtenco/computer_vision_trading_metatrader_5`](https://github.com/Shtenco/computer_vision_trading_metatrader_5) | 2 | 2 | 0 | MATCH |
| [`Shtenco/swap_arbitrage_metatrader_5`](https://github.com/Shtenco/swap_arbitrage_metatrader_5) | 2 | 2 | 0 | MATCH |
| [`Shtenco/cross_forex_arbitrage_trading_metatrader_5`](https://github.com/Shtenco/cross_forex_arbitrage_trading_metatrader_5) | 2 | 2 | 0 | MATCH |
| [`Shtenco/global_liquidity_dataminer`](https://github.com/Shtenco/global_liquidity_dataminer) | 2 | 2 | 0 | MATCH |
| [`Shtenco/3D_bars_market_structure`](https://github.com/Shtenco/3D_bars_market_structure) | 9 | 9 | 0 | MATCH |
| [`Shtenco/shtenco_multi_threaded_trading_robot_with_machine_learning_python`](https://github.com/Shtenco/shtenco_multi_threaded_trading_robot_with_machine_learning_python) | 2 | 2 | 0 | MATCH |
| [`Shtenco/synergy_midas_ai_trading_system`](https://github.com/Shtenco/synergy_midas_ai_trading_system) | 18 | 18 | 0 | MATCH |
| [`Shtenco/midas_lite`](https://github.com/Shtenco/midas_lite) | 3 | 3 | 0 | MATCH |
| [`Shtenco/synergy_turbo_linux`](https://github.com/Shtenco/synergy_turbo_linux) | 18 | 18 | 0 | MATCH |
| [`Shtenco/synergy_agi_olga`](https://github.com/Shtenco/synergy_agi_olga) | 38 | 37 | 1 | MATCH |
| [`Shtenco/synergy_ai_coder`](https://github.com/Shtenco/synergy_ai_coder) | 8 | 8 | 0 | MATCH |
| [`Shtenco/synergy_ai_trade_terminal`](https://github.com/Shtenco/synergy_ai_trade_terminal) | 5 | 5 | 0 | MATCH |
| [`Shtenco/shtencoauantai.github.io`](https://github.com/Shtenco/shtencoauantai.github.io) | 14 | 14 | 0 | MATCH |
| [`Shtenco/synergy_cashero`](https://github.com/Shtenco/synergy_cashero) | 11 | 11 | 0 | MATCH |
| [`Shtenco/synergy_ai_language`](https://github.com/Shtenco/synergy_ai_language) | 129 | 105 | 24 | MATCH |
| [`Shtenco/sinergy_super_app`](https://github.com/Shtenco/sinergy_super_app) | 7 | 7 | 0 | MATCH |
| [`Shtenco/synergy_binary_quantum_theory`](https://github.com/Shtenco/synergy_binary_quantum_theory) | 178 | 167 | 11 | MATCH |
| [`Shtenco/synergy_ai_financial_system`](https://github.com/Shtenco/synergy_ai_financial_system) | 31 | 30 | 1 | MATCH |
| [`Shtenco/synergy_algotrading_graph_system`](https://github.com/Shtenco/synergy_algotrading_graph_system) | 1 | 1 | 0 | MATCH |
| [`Shtenco/synegy_ai_compress`](https://github.com/Shtenco/synegy_ai_compress) | 19 | 18 | 1 | MATCH |
| [`Shtenco/synergy_pay_system`](https://github.com/Shtenco/synergy_pay_system) | 27 | 27 | 0 | MATCH |
| [`Shtenco/synergy_ai_blockchain`](https://github.com/Shtenco/synergy_ai_blockchain) | 32 | 32 | 0 | MATCH |
| [`Shtenco/synergy_chain`](https://github.com/Shtenco/synergy_chain) | 29 | 27 | 2 | MATCH |
| [`Shtenco/synergychain.github.io`](https://github.com/Shtenco/synergychain.github.io) | 52 | 48 | 4 | MATCH |
| [`Shtenco/synergy_cold_nuclear`](https://github.com/Shtenco/synergy_cold_nuclear) | 2 | 2 | 0 | MATCH |
| [`Shtenco/synergy_usds`](https://github.com/Shtenco/synergy_usds) | 10 | 10 | 0 | MATCH |
| [`Shtenco/synergy_financial_os`](https://github.com/Shtenco/synergy_financial_os) | 40 | 40 | 0 | MATCH |
| [`Shtenco/synergy_eurasian`](https://github.com/Shtenco/synergy_eurasian) | 19 | 19 | 0 | MATCH |
| [`Shtenco/synergy_matrix_sota`](https://github.com/Shtenco/synergy_matrix_sota) | 3 | 3 | 0 | MATCH |
| [`Shtenco/synergy_agi_nexus`](https://github.com/Shtenco/synergy_agi_nexus) | 58 | 57 | 1 | MATCH |
| [`Shtenco/synergy_midas_ai`](https://github.com/Shtenco/synergy_midas_ai) | 35 | 20 | 15 | MATCH |
| [`Shtenco/synergy_system`](https://github.com/Shtenco/synergy_system) | 62 | 60 | 2 | MATCH |
| [`Shtenco/synergy_nexus_science_agent`](https://github.com/Shtenco/synergy_nexus_science_agent) | 8 | 8 | 0 | MATCH |
| [`Shtenco/synergy_net`](https://github.com/Shtenco/synergy_net) | 22 | 22 | 0 | MATCH |
| [`Shtenco/synergy_meta_os`](https://github.com/Shtenco/synergy_meta_os) | 33 | 32 | 1 | MATCH |
| [`Shtenco/synergy_blochain_budget`](https://github.com/Shtenco/synergy_blochain_budget) | 8 | 8 | 0 | MATCH |
| [`Shtenco/synergy_agi_autopilot`](https://github.com/Shtenco/synergy_agi_autopilot) | 29 | 20 | 9 | MATCH |
| [`Shtenco/sinergy_app`](https://github.com/Shtenco/sinergy_app) | 1 | 1 | 0 | MATCH |
| [`Shtenco/synergy_app`](https://github.com/Shtenco/synergy_app) | 4 | 4 | 0 | MATCH |
| [`Shtenco/synergy_qr_compress`](https://github.com/Shtenco/synergy_qr_compress) | 12 | 12 | 0 | MATCH |
| [`Shtenco/synergy_metachain`](https://github.com/Shtenco/synergy_metachain) | 5 | 4 | 1 | MATCH |
| [`Shtenco/synergy_motherboard_xpu_xml`](https://github.com/Shtenco/synergy_motherboard_xpu_xml) | 5 | 5 | 0 | MATCH |
| [`Shtenco/print_money_synergychain`](https://github.com/Shtenco/print_money_synergychain) | 9 | 9 | 0 | MATCH |
| [`Shtenco/synergy_project`](https://github.com/Shtenco/synergy_project) | 5 | 5 | 0 | MATCH |
| [`Shtenco/dlp_solver`](https://github.com/Shtenco/dlp_solver) | 23 | 23 | 0 | MATCH |
| [`Shtenco/synergy_crypto_pump`](https://github.com/Shtenco/synergy_crypto_pump) | 3 | 3 | 0 | MATCH |
| [`Shtenco/synergy_graph_print_money`](https://github.com/Shtenco/synergy_graph_print_money) | 6 | 6 | 0 | MATCH |
| [`Shtenco/synergy_app_family`](https://github.com/Shtenco/synergy_app_family) | 1 | 1 | 0 | MATCH |
| [`Shtenco/synergy_chain_print_money`](https://github.com/Shtenco/synergy_chain_print_money) | 1 | 1 | 0 | MATCH |
| [`Shtenco/synergy_ai_company`](https://github.com/Shtenco/synergy_ai_company) | 2 | 2 | 0 | MATCH |
| [`Shtenco/synergy_shhts`](https://github.com/Shtenco/synergy_shhts) | 1 | 1 | 0 | MATCH |
| [`Shtenco/synergy_shttps`](https://github.com/Shtenco/synergy_shttps) | 3 | 3 | 0 | MATCH |
| [`Shtenco/synergy_gguf_compress`](https://github.com/Shtenco/synergy_gguf_compress) | 10 | 10 | 0 | MATCH |
| [`Shtenco/synergy_gllm_nexus`](https://github.com/Shtenco/synergy_gllm_nexus) | 48 | 47 | 1 | MATCH |
| [`Shtenco/synergy_messenger`](https://github.com/Shtenco/synergy_messenger) | 14 | 6 | 8 | MATCH |
| [`Shtenco/synergy_apps`](https://github.com/Shtenco/synergy_apps) | 11 | 10 | 1 | MATCH |
| [`Shtenco/synergy_agi_trader`](https://github.com/Shtenco/synergy_agi_trader) | 3 | 3 | 0 | MATCH |
| [`Shtenco/synergy_quantlab`](https://github.com/Shtenco/synergy_quantlab) | 3 | 3 | 0 | MATCH |
| [`Shtenco/synergy_riskguard`](https://github.com/Shtenco/synergy_riskguard) | 3 | 3 | 0 | MATCH |
| [`Shtenco/synergy_market_graph`](https://github.com/Shtenco/synergy_market_graph) | 3 | 3 | 0 | MATCH |
| [`Shtenco/synergy_midas_institutional`](https://github.com/Shtenco/synergy_midas_institutional) | 3 | 3 | 0 | MATCH |
| [`Shtenco/synergy_relative_value`](https://github.com/Shtenco/synergy_relative_value) | 3 | 3 | 0 | MATCH |
| [`Shtenco/synergy_ai_investment_committee`](https://github.com/Shtenco/synergy_ai_investment_committee) | 3 | 3 | 0 | MATCH |
| [`Shtenco/synergy_market_maker`](https://github.com/Shtenco/synergy_market_maker) | 3 | 3 | 0 | MATCH |
| [`Shtenco/synergy_adaptive_engine`](https://github.com/Shtenco/synergy_adaptive_engine) | 3 | 3 | 0 | MATCH |
| [`Shtenco/synergy_marketvision`](https://github.com/Shtenco/synergy_marketvision) | 3 | 3 | 0 | MATCH |
| [`Shtenco/synergy_trademux`](https://github.com/Shtenco/synergy_trademux) | 3 | 3 | 0 | MATCH |
| [`Shtenco/synergy_epstein_network`](https://github.com/Shtenco/synergy_epstein_network) | 6 | 6 | 0 | MATCH |
| [`Shtenco/synergy_2chain_qe`](https://github.com/Shtenco/synergy_2chain_qe) | 5 | 5 | 0 | MATCH |
| [`Shtenco/synergy_qe`](https://github.com/Shtenco/synergy_qe) | 3 | 3 | 0 | MATCH |
| [`Shtenco/synergy_agentic_ai_economy`](https://github.com/Shtenco/synergy_agentic_ai_economy) | 15 | 15 | 0 | MATCH |
| [`Shtenco/synergy_megaproject`](https://github.com/Shtenco/synergy_megaproject) | 1 | 1 | 0 | MATCH |
| [`Shtenco/synergy_post_quantum_radio`](https://github.com/Shtenco/synergy_post_quantum_radio) | 2 | 2 | 0 | MATCH |
| [`Shtenco/synergy_complex_matrix_multiplication`](https://github.com/Shtenco/synergy_complex_matrix_multiplication) | 1 | 1 | 0 | MATCH |
| [`Shtenco/synergy_computing_topology`](https://github.com/Shtenco/synergy_computing_topology) | 3 | 3 | 0 | MATCH |
| [`Shtenco/synergy_search_engline`](https://github.com/Shtenco/synergy_search_engline) | 1 | 1 | 0 | MATCH |
| [`Shtenco/synergy_lead_search_engline`](https://github.com/Shtenco/synergy_lead_search_engline) | 3 | 3 | 0 | MATCH |
| [`Shtenco/synergy_triangle_money_system`](https://github.com/Shtenco/synergy_triangle_money_system) | 9 | 9 | 0 | MATCH |
| [`Shtenco/synergy`](https://github.com/Shtenco/synergy) | 4 | 4 | 0 | MATCH |
| [`Shtenco/synergy_ai_llm_rwkv`](https://github.com/Shtenco/synergy_ai_llm_rwkv) | 2 | 2 | 0 | MATCH |
| [`Shtenco/synergy_ai_economic`](https://github.com/Shtenco/synergy_ai_economic) | 3 | 3 | 0 | MATCH |
| [`Shtenco/synergy.github.io`](https://github.com/Shtenco/synergy.github.io) | 3 | 3 | 0 | MATCH |
| [`Shtenco/synergy_meta_api`](https://github.com/Shtenco/synergy_meta_api) | 2 | 2 | 0 | MATCH |
| [`Shtenco/synergy_ai_workspace`](https://github.com/Shtenco/synergy_ai_workspace) | 11 | 9 | 2 | MATCH |
| [`Shtenco/synergistic_economics`](https://github.com/Shtenco/synergistic_economics) | 19 | 19 | 0 | MATCH |
| [`Shtenco/synergy_metaverse`](https://github.com/Shtenco/synergy_metaverse) | 10 | 9 | 1 | MATCH |
| [`Shtenco/synergy_maps`](https://github.com/Shtenco/synergy_maps) | 10 | 10 | 0 | MATCH |
| [`Shtenco/shtenco_micro_ai`](https://github.com/Shtenco/shtenco_micro_ai) | 1 | 1 | 0 | MATCH |
| [`Shtenco/synergy_long_term_harness`](https://github.com/Shtenco/synergy_long_term_harness) | 5 | 5 | 0 | MATCH |

## Evidence limits

- This recheck confirms **branch names and counts**, not that every branch HEAD SHA remained unchanged after the census was generated.
- HEAD SHAs and within-repository duplicate-HEAD counts above are carried from the canonical 2026-11-20 census; they were not individually re-fetched in this name-only recheck.
- Branch protection flags are also census values, not a fresh branch-protection API recheck. The census records 0/1,292 protected refs; this should be revalidated with the appropriate administrative permission before changing governance policy.
- This report does not classify branches as mergeable, obsolete or safe to delete. Open PR relationships, tags, release references, workflow usage and cross-repository references must be checked before any cleanup.
- No branch, commit, PR, workflow, setting or source file was modified during the recheck.

## Canonical evidence

- [Full branch inventory — JSON](../registry/BRANCH_INVENTORY_2026-11-20.json)
- [Full branch inventory — CSV](../registry/BRANCH_INVENTORY_2026-11-20.csv)
- [Branch inventory report](BRANCH_INVENTORY_2026-11-20.md)
- [Open PR / branch map](../registry/OPEN_PR_BRANCH_MAP_2026-11-20.json)
- [High-branch repository / BQG audit](HIGH_BRANCH_REPOSITORY_AUDIT_2026-11-20.md)

**Conclusion:** the 1,292-ref census is fully reconciled at the branch-name/count level across all 91 currently accessible repositories. Exact HEAD and protection-state refresh remains a separate evidence task.
