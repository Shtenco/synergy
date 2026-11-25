# SYNERGY Hypergraph Core — V3

Machine-readable repository inventory, evidence-aware dependency graph and target architecture for the ecosystem audit.

## Current snapshot
- 112 repository nodes keyed by immutable GitHub repository IDs (100 search results on page 1, 12 on page 2).
- 109 registry-declared `DEPENDS_ON` edges, all `candidate`; zero verified runtime edges.
- One hundred five unique repository README reviews (109 commit-pinned audit records) and ninety-two limited source reviews, each pinned to the exact inspected commit and file blob SHA (76 main-branch reviews and 7 branch-only prototype reviews).
- 39 proposed shared cores and domain routers are kept separate from actual repositories; 27 have first-pass overlap assessments and 12 remain unaudited.
- Six target architecture layers and twenty-eight candidate target relationships are documented separately from observed dependencies.

## Files
- `nodes.json`: 112 repository nodes and per-repository audit status.
- `edges.json`: registry-declared dependency edges; every edge remains `candidate` until source evidence verifies it.
- `architecture/target-graph.json`: six-layer target graph and candidate architecture links.
- `architecture/ownership-map.json`: canonical owners and integration direction; avoids duplicate core repositories.
- `architecture/overlap-matrix.json`: first-pass overlap review for proposed shared cores.
- `coverage.json`: measurable inventory and audit coverage.
- `gaps.json`: unresolved source audit, security, evidence, contract and overlap gaps.
- `proposals.json`: 39 proposed components, not actual repositories.
- `evidence/registry-snapshot.json`: provenance for the original 92-record registry snapshot.
- `evidence/repository-audits.json`: 109 commit-pinned audit records across 95 unique repositories; older main-branch snapshots are retained when a newer branch-only prototype is reviewed with selected source/test blob references.
- `contracts/`: requirements for versioned OpenAPI, JSON Schema, AsyncAPI and contract tests.
- `security/RESPONSE_PLAYBOOK.md`: credential rotation and live-execution containment without secret material.
- `schemas/`: JSON Schema contracts for repository nodes and n-ary hyperedges.

## Current findings
1. `synergy_system` has a stale 92-repository snapshot; its federation authority and contract registry remain canonical. The current main branch of hierarchical cognitive memory contains commit-pinned dependency and cross-repository intelligence, contrary to the older README-only claim.
2. `synergy_ai_browser-`: the Playwright route guard checks top-level document navigation, but continues subresource requests without equivalent host/IP checks. Treat as a high-priority potential SSRF/private-network exposure until fixed and tested.
3. `timeweb_synergy_service_recovery`: inspected recovery scenario is an in-memory simulator, while README describes local HTTP/SQLite restarts. Evidence scope must be reconciled.
4. `timeweb_synergy_cpu_gpu_cost_benchmark`: inspected code is an assumption-based cost calculator; a GPU benchmark harness and paid cloud evidence were not found in the inspected tree.
5. `timeweb_synergy_retry_storm_lab`: the protected policy reached 32.92% median success versus 56.25% for retry-budget plus bulkhead in its fixed localhost fault model. This is a configuration/granularity warning, not a general verdict on circuit breakers.
6. `timeweb_synergy_benchmark_statistics`: archived UCI digits results show binary model accuracy 88.81% versus FP32 95.85% over three paired seeds; uncertainty is exploratory and fixed-test-set limitations apply.

7. `synergy_meta_os`: compatibility runtime uses POSIX resource limits but is not a complete filesystem/network/namespace sandbox.
8. `synergy_meta_api`: V0.1 gateway keeps connector execution disabled by default until authentication is implemented.
9. `synergy_market_graph`: current fair-value graph is advisory and does not apply capacity/latency constraints.

10. `synergy_financial_os` recognition helper has an optional settlement evidence parameter and accepts empty balanced entries; `synergy_pay_system` settlement idempotency is process-local; `synergy_riskguard` treats fewer than five returns as zero VaR/CVaR.

11. `synergy_lead_search_engline` is an offline real-estate lead candidate store with human review, not a deployed multi-tenant crawler; current schema lacks tenant isolation.
12. `synergy_search_engline` is a HardNAV simulation, not a general search service.
13. `synergy_messenger` main branch has a manifest whose scripts reference missing source/test paths; the alpha runtime is not verified on main.
14. `synergy_ai_workspace` implementation exists only on a release branch; main remains README-only.

15. `synergy_algotrading_graph_system` is a README-only architecture specification; executable graph models already exist in `synergy_market_graph` and `synergy_ai_financial_system`.
16. Relative-value and MIDAS institutional outputs are advisory/non-authorizing and must pass canonical RiskGuard validation.

17. `synergy_usds` and `synergy_cashero` contain tracked key/environment artifacts that require credential rotation review; `synergy_turbo_linux` has a documented historical unencrypted SSH private-key incident with revocation not yet evidenced.
18. `synergy_metachain` replay protection is process-local and does not verify chain proofs.
19. `synergy_computing_topology` has archived correctness results, but kernel runtime on the current host was not tested.

20. QuantLab is the validation authority; MIDAS AI is a target canonical advisory-contract layer; Market Maker and MarketVision are non-authorizing signal/feature producers.
21. Market Maker quotes and MIDAS institutional assessments are not broker orders; canonical RiskGuard and Financial OS remain separate authorities.

22. MIDAS AI Trading System main has a broken Risk Veto exception path, unauthenticated log/metrics WebSockets, a VaR/CVaR sign mismatch and non-persistent archive chain state.
23. `midas_lite` contains direct MT5 order submission in a legacy agent; `synergy_ai_trade_terminal` contains embedded credentials. Keep execution disabled and rotate credentials.
24. `synergy_usds`, `synergy_cashero` and `synergy_turbo_linux` have tracked or historical credential exposure findings. The security playbook records containment steps without storing secret material.

25. AI Language's multi-target code generator interpolates unescaped strings for C/Rust/Solidity/Kotlin; command execution is not an OS sandbox and trace output is not secret-redacted.
26. GLLM runtime and RWKV quantization code are branch-only; neither should be described as default-main functionality or production-ready model runtime.
27. Matrix SOTA is a documentation-only debt/credit maturity design, not an executable credit engine.

28. `synergy_qr_compress` is a shared-model temporal dictionary/patch codec; zero residual is only meaningful after amortizing dictionary storage and distribution.
29. `synegy_ai_compress` is a benchmark dossier whose engine source is a gitlink without `.gitmodules`; exact source retrieval is not reproducible from the repository alone.
30. `synergy_gguf_compress` and `synergy_shhts` are documentation-only on main.

31. `synergy_megaproject` is a research claim/evidence graph and can supply reviewed scientific evidence, but it is not a software dependency graph.
32. `synergy_eurasian` is an economic allocation simulator with scenario coefficients, not a live macroeconomic data authority.
33. `synergy_binary_quantum_theory` keeps mathematical proof status separate from unresolved physical validation gates.

34. PQ-EVM's standards-based provider is optional behind a Cargo feature; the default build does not enable it, and the project remains unaudited research/integration code.
35. `synergy_blochain_budget` provides source-bound public budget/EIS traceability and Merkle proofs, not legal/accounting authority; its JSONL append chain is not safe for concurrent writers or crash recovery.
36. `synergy_triangle_money_system` distinguishes HardNAV from liquidity multiplier but uses mock assets in its integration fixture; no external liquidity or production oracle is proven.
37. `synergy_crypto_pump` implements purged walk-forward folds, but the helper defaults purge and embargo to zero; the caller must explicitly configure leakage-safe horizons.
38. `synergy_2chain_qe` contains bridge/AMM contracts, but the checked arbitrage executor still marks the external DEX leg as simulated.
39. `synergy_graph_print_money` V7.4 has in-kind multi-token repayment logic and a pinned Base fork gate; README reports the hosted fork workflow currently fails before its first step.
40. `synergistic_economics` has a deterministic double-entry research kernel, but its ledger and event store are in-memory rather than durable.
41. `synergy_ai_economic` main is documentation-only; the executable V8 prototype is on a research branch and the README labels the economic twin as a synthetic-assumption research model.
42. `synergy_eurasian` main contains a static federation audit, but its README reports main-branch test collection fails because V6.6 imports are absent; feature branches are not the release branch.
43. `synergy_trademux` has a paper-routing adapter and typed execution contracts, but no proven broker fills or durable idempotency; quote/fill numeric validation needs hardening.
44. `synergy_project` is a capital-governance dossier and payload contract, not an authorization runtime; non-finite Decimal amounts require rejection and its PR #2 inventory count is stale.
45. `synergy_complex_matrix_multiplication` contains substantial operator research, but the V9 pipeline is explicitly incomplete and some runners depend on local checkpoints/dynamic source execution.
46. `synergy_app_family` and `synergy_post_quantum_radio` are specification-only on main.
47. `synergy_metaverse` implements spatial evidence verification and envelope interfaces, but production KMS/HSM, governed key registry, consent/revocation and backup-erasure controls are not deployed.
48. `synergy_ai_blockchain` has a substantial Rust/PQ research implementation, but production PQ providers, EVM client integration, light clients, bridge proofs and independent cryptographic audit remain open.
49. `shtenco_micro_ai` pins MNN/model revisions and tests metric parsing; its CI is a CPU smoke test, not a device-specific mobile benchmark.
50. `synergy_cold_nuclear` explicitly separates evaluated data, derived calculations, hypotheses and stress tests; its LENR models do not establish cold fusion or transmutation.
51. `synergy_binary_quantum_theory` keeps finite mathematical checks separate from physicalization and experiment; its current theory status explicitly remains open.
52. `synergy_long_term_harness` has content-addressed SQLite memory and fenced mission leases on open PR branches; main remains README-only and independent verifier/host identity adapters are incomplete.
53. `synergy_ai_company` Auto-Company 2.0 exists on an open feature PR with paper-mode defaults and approval gates; risk caps still need NaN/Infinity validation.
54. `synergy_messenger` has an alpha.9 source branch, but the claimed 249-test release suite is absent from the reviewed branch and the npm test path is unresolved.
55. The base `main` registry snapshot was 92 repositories; this PR branch reconciles the inventory to 112 immutable GitHub IDs. The legacy rebuild script still omits those IDs, so a future regeneration can regress the canonical registry.
56. `timeweb_synergy_codebase_intelligence` has a reproducible 15-scenario runner, but repository-navigation scenario 04 generates synthetic metadata rather than inspecting a real codebase.
57. `synergy_ai_investment_committee` is an advisory committee with explicit `authorization=false`; market input validation still needs finite/range guards.
58. `synergy_megaproject` separates source/measurement/derived evidence from hypotheses and never auto-mutates the canonical graph; its graph validator is structural, not source verification.
59. `dlp_solver`'s V18 gcd experiment is a synthetic negative result, not a key-recovery method; its benchmark contract still needs finite elapsed-time validation.
60. `synergy_shttps` is specification-only on main; no production HTTPS replacement is implemented.

## Evidence rules
1. Repository names are not identities; GitHub repository IDs are.
2. A registry dependency is a candidate edge, not proof of an import or runtime call.
3. `candidate`, `reviewed`, `verified`, and `rejected` are distinct states. `verified` requires reproducible source or runtime evidence.
4. Proposed components are not repository inventory entries.
5. Hashes establish byte identity, not truth, authorization or correctness.
6. No tests were executed as part of the current repository review; archived results are not fresh CI runs.
7. Existing implementation boundaries: `synergy_system` owns governance/contracts; hierarchical cognitive memory owns static dependency and cross-repository evidence intelligence; Hypergraph V3 is a projection/read model, not a new competing runtime or repository.

## Coverage
- Inventory: 112/112 unique IDs returned by owner-scoped search.
- README reviewed: 105/112 (93.75%).
- Source reviewed (limited scope): 92/112 (82.14%): 85 main-branch reviews and 7 branch-only prototype reviews.
- Dependency edges verified: 0/109.
- Cross-repository contracts verified: 0.

## Next audit sequence
1. Close the browser subresource network-policy finding.
2. Audit the remaining 20 repositories for source, and 7 for a first README review: manifests, imports, API routes, event schemas, tests and workflows.
3. Replace registry-only candidate edges with source-pinned evidence.
4. Extract contracts and validate compatibility.
5. Run capability-overlap analysis before proposing any new repository.
