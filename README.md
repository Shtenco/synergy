# SYNERGY

> **Private master umbrella repository for the SYNERGY ecosystem.**

This repository is the **single entry point, architecture map, module registry and integration layer** for the SYNERGY family of repositories owned by `Shtenco`.

## Purpose

`Shtenco/synergy` does **not** replace or merge the source history of the child repositories.

Each subsystem keeps its own repository, issues, pull requests, releases and CI/CD. This master repository provides:

- one canonical map of the whole ecosystem;
- a machine-readable registry of SYNERGY modules;
- architecture and dependency documentation;
- common integration contracts;
- a place for cross-repository roadmaps and system-level decisions;
- automation hooks for NEXUS / Autopilot / AI-company orchestration.

## Current scope

M0 integration now inventories **81 / 81 repositories visible to the installed GitHub App**. Membership is determined by **content, role and cross-repository references**, not only by the word `SYNERGY` in the repository name.

The canonical artifacts are:

- [registry/repos.json](registry/repos.json) — full 81-repository inventory
- [registry/master_graph.json](registry/master_graph.json) — capability/dependency graph
- [docs/M0_MASTER_INTEGRATION.md](docs/M0_MASTER_INTEGRATION.md) — M0 audit
- [docs/MASTER_GRAPH.md](docs/MASTER_GRAPH.md) — human-readable graph
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- [docs/INTEGRATION.md](docs/INTEGRATION.md)

## System map

```text
SYNERGY
├── AGI / Agentic Company
│   ├── NEXUS
│   ├── Autopilot
│   ├── AI Company
│   ├── AI Coder
│   └── Science / workforce agents
├── Trading / Quant
│   ├── MIDAS
│   ├── QuantLab
│   ├── RiskGuard
│   ├── Market Graph
│   ├── Market Maker
│   ├── Relative Value
│   └── TradeMux / MarketVision / Adaptive Engine
├── Finance / Economy
│   ├── Financial OS
│   ├── Payment System
│   ├── USDS
│   ├── QE engines
│   ├── Triangle Money System
│   └── Agentic AI Economy
├── Blockchain / Protocol
│   ├── AI Blockchain
│   ├── Synergy Chain
│   ├── MetaChain
│   ├── budgeting / issuance modules
│   └── post-quantum transport
├── Compute / Compression / OS
│   ├── Turbo Linux
│   ├── Meta OS
│   ├── XPU / Motherboard
│   ├── GGUF / QR / AI compression
│   └── computing topology / matrix engines
├── Apps / Interfaces
│   ├── Super App
│   ├── Apps / Family
│   ├── Messenger
│   └── AI Trade Terminal
└── Search / Growth / Research
    ├── Search Engine
    ├── Lead Search Engine
    └── experimental research modules
```

## Canonical integration principle

Child repositories remain independent. They are connected to this umbrella through metadata and contracts rather than by copying their Git history.

Recommended dependency forms:

1. **API / protocol dependency** — preferred for services and agents.
2. **Package dependency** — preferred for reusable libraries.
3. **Git submodule** — only when a pinned source checkout is genuinely required.
4. **Artifact dependency** — models, binaries, schemas or releases consumed by version.
5. **Event / message contract** — for distributed NEXUS and agent fabric.

## Master identifiers

- GitHub owner: `Shtenco`
- Umbrella repository: `Shtenco/synergy`
- Default branch: `main`
- Visibility: **private**
- Registry schema: `registry/repos.json`

## Next system-level milestones

- normalize module metadata and ownership;
- map runtime dependencies between repositories;
- define shared protocol/schema versions;
- connect cross-repository CI health;
- connect GitHub Project roadmap;
- add automated repository discovery;
- expose the registry to NEXUS / Autopilot as a capability graph.

---

**Rule:** do not move secrets, credentials, private keys, API tokens or production configuration into this repository.
