# SYNERGY Live Branch Audit — Umbrella, Economic Master and Super App

**Audit date:** 2026-11-20  
**Scope:** live branch HEADs, open PRs and latest 10 workflow runs for three top-level repositories.  
**Method:** read-only GitHub REST; purpose checked against current main README; exact branch SHA and PR associations fetched live.  
**Limit:** no production deployment, Android device installation, signed release or external economic settlement was performed.

## Summary

| Repository | Role / evidence boundary | Branches | Open PRs | Latest workflow | Main CI | Decision |
|---|---|---:|---:|---|---|---|
| [`Shtenco/synergy_project`](https://github.com/Shtenco/synergy_project) | Federated economic OS master dossier: capital, payments, finance, science and industrial capacity. Architecture/documentation root, not itself a single executable runtime. | 5 | 3 | none observed | CI_NOT_VERIFIED absent exact-main checks | Keep governance, economic master and mobile shell distinct. |
| [`Shtenco/synergy`](https://github.com/Shtenco/synergy) | Umbrella registry and architecture map; owns canonical ecosystem inventory, dependency graph, integration contracts and audit evidence, not child runtime code. | 4 | 1 | none observed | CI_NOT_VERIFIED absent exact-main checks | Keep governance, economic master and mobile shell distinct. |
| [`Shtenco/sinergy_super_app`](https://github.com/Shtenco/sinergy_super_app) | PWA/mobile shell with service worker, web manifest, Android Gradle wrapper and assembleDebug workflow; source provenance is not proof of signed APK or production deployment. | 7 | 3 | Build APK: failure @ main/3494f2cdebd0 | CI_NOT_VERIFIED absent exact-main checks | Keep governance, economic master and mobile shell distinct. |

## synergy_project

**Purpose:** Federated economic OS master dossier: capital, payments, finance, science and industrial capacity. Architecture/documentation root, not itself a single executable runtime.  
**Current main:** `fcfaa292ab97b622ac6292b8179aaa66a4e585a4`.  
**Open PRs:** 3.  
**Latest workflow observations:** none.

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `audit/portfolio-89-repositories-v1` | `9ffa1736783df8f4ff19163d0b9d5716fcba0ca9` | Draft: reconcile and assess all 89 SYNERGY repositories | #2 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; exact-head CI and review required. Economic master remains R&D/pre-production; do not infer a single integrated operating system from the dossier. Retain candidate; review scope, docs and integration effects before merge. |
| `grant-dossier-ip-valuation-v1` | `4c6e1c3b4c735c78bab947b7f114d6b59b84231e` | Inferred from branch name: grant dossier ip valuation v1 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and references before cleanup. Economic master remains R&D/pre-production; do not infer a single integrated operating system from the dossier. Retain pending lifecycle review. |
| `main` | `fcfaa292ab97b622ac6292b8179aaa66a4e585a4` | Canonical default branch | MAIN | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and references before cleanup. Economic master remains R&D/pre-production; do not infer a single integrated operating system from the dossier. Retain canonical; do not claim operational deployment without evidence. |
| `research/ip-financing-readiness-2026-11-14` | `40cd4901df5aae9b63cb51e4f2aa8df25c9c9103` | docs: add preliminary IP-backed financing readiness report | #3 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; exact-head CI and review required. Economic master remains R&D/pre-production; do not infer a single integrated operating system from the dossier. Retain candidate; review scope, docs and integration effects before merge. |
| `valuation-v3-87-assets-20261114` | `66b5fed8332a65865962cafb22cb41c3701b38f5` | Add V3 valuation register for 87 SYNERGY technical repositories | #1 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; exact-head CI and review required. Economic master remains R&D/pre-production; do not infer a single integrated operating system from the dossier. Retain candidate; review scope, docs and integration effects before merge. |

## synergy

**Purpose:** Umbrella registry and architecture map; owns canonical ecosystem inventory, dependency graph, integration contracts and audit evidence, not child runtime code.  
**Current main:** `0a9f38f6196c1b25252086be2ff56a799601838b`.  
**Open PRs:** 1.  
**Latest workflow observations:** none.

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `audit/reconcile-live-89-inventory-v1` | `cb4862803521c5ebba1041c5496177bf3e06e69e` | Inferred from branch name: audit reconcile live 89 inventory v1 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and references before cleanup. Umbrella changes affect global navigation and evidence registry; validate cross-links and registry counts. Retain pending lifecycle review. |
| `feature/web-ecosystem-v8-federation-20261014` | `26cb5ce943a3ddeafc3509b59a8c563dde97bbad` | Inferred from branch name: feature web ecosystem v8 federation 20261014 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and references before cleanup. Umbrella changes affect global navigation and evidence registry; validate cross-links and registry counts. Retain pending lifecycle review. |
| `feature/82-repo-ecosystem-registry-20261014` | `e91c0c8099fbcc49b6dd28e245e6603caaa5a7a9` | Registry: reconcile 82 repositories (RWKV candidate) | #2 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; exact-head CI and review required. Umbrella changes affect global navigation and evidence registry; validate cross-links and registry counts. Retain candidate; review scope, docs and integration effects before merge. |
| `main` | `0a9f38f6196c1b25252086be2ff56a799601838b` | Canonical default branch | MAIN | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and references before cleanup. Umbrella changes affect global navigation and evidence registry; validate cross-links and registry counts. Retain canonical; do not claim operational deployment without evidence. |

## sinergy_super_app

**Purpose:** PWA/mobile shell with service worker, web manifest, Android Gradle wrapper and assembleDebug workflow; source provenance is not proof of signed APK or production deployment.  
**Current main:** `3494f2cdebd0b9510ac65a470b32a085e4920537`.  
**Open PRs:** 3.  
**Latest workflow observations:** Build APK=failure @ main/3494f2cdebd0 (2026-10-23T22:03:26Z); Build APK=failure @ main/fcd5b0640f9c (2026-10-23T22:03:24Z); Build APK=failure @ main/26498f601670 (2026-10-23T20:04:47Z); Build APK=failure @ main/1aa66007a00d (2026-10-23T19:55:45Z); Build APK=failure @ main/336cc9779a8c (2026-10-19T18:52:16Z); Build APK=failure @ main/80cfea5fc458 (2026-09-29T01:32:21Z); Build APK=failure @ main/584a3642dc23 (2026-09-28T22:55:25Z); Build APK=failure @ main/49122aebb8cf (2026-09-28T22:55:01Z); Build APK=failure @ main/e00afb6583d0 (2026-09-28T17:23:35Z); Build APK=failure @ main/4e94add943ce (2026-09-28T16:21:34Z).

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `build/sinergy-finance-v3-wallet` | `0c50c082a77d3a2765c96ec30fabce0ab04843e4` | Inferred from branch name: build sinergy finance v3 wallet | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and references before cleanup. Require exact Gradle CI, APK artifact digest, signing provenance, install test, offline behavior and Android permission audit. Retain pending lifecycle review. |
| `build/sinergy-v65-real` | `402efdd7acc8f8210d115eeb73af2404b5edd63d` | Inferred from branch name: build sinergy v65 real | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and references before cleanup. Require exact Gradle CI, APK artifact digest, signing provenance, install test, offline behavior and Android permission audit. Retain pending lifecycle review. |
| `docs/editorial-batch03` | `873755ebcb122ed073cf19d78f82bab2607096e3` | Inferred from branch name: docs editorial batch03 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; verify ancestry and references before cleanup. Require exact Gradle CI, APK artifact digest, signing provenance, install test, offline behavior and Android permission audit. Retain pending lifecycle review. |
| `feature/sinergy-finance-v1` | `dd5abc8a2608bd4b20ee964cd0dc84a76505c08d` | SINERGY Finance v1.0.0 Android APK | #1 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; exact-head CI and review required. Require exact Gradle CI, APK artifact digest, signing provenance, install test, offline behavior and Android permission audit. Retain candidate; review scope, docs and integration effects before merge. |
| `federation-v3-domain-expansion` | `63d65b7d00016fe1b6dd8159b3adc5647a6aee86` | Federation V3: define super-app as non-authoritative federation client | #2 ready | NOT_OBSERVED in latest-10 workflow window | PR base=main; exact-head CI and review required. Require exact Gradle CI, APK artifact digest, signing provenance, install test, offline behavior and Android permission audit. Retain candidate; review scope, docs and integration effects before merge. |
| `main` | `3494f2cdebd0b9510ac65a470b32a085e4920537` | Canonical default branch | MAIN | failure (Build APK, 2026-10-23T22:03:26Z) | No open PR; purpose inferred; verify ancestry and references before cleanup. Require exact Gradle CI, APK artifact digest, signing provenance, install test, offline behavior and Android permission audit. Retain canonical; do not claim operational deployment without evidence. |
| `migration/synergy-723-2026-09` | `2a5e042853a63c180cfea4fa6234623ce0dbafcf` | chore: stage SYNERGY 723-file migration provenance | #3 draft | NOT_OBSERVED in latest-10 workflow window | PR base=main; exact-head CI and review required. Require exact Gradle CI, APK artifact digest, signing provenance, install test, offline behavior and Android permission audit. Retain candidate; review scope, docs and integration effects before merge. |

## Governance decisions

- Keep `synergy` as the umbrella architecture and inventory root.
- Keep `synergy_system` as the federation/security authority and contract root.
- Keep `synergy_project` as the economic master dossier, not a substitute for service-level runtime evidence.
- Keep `sinergy_super_app` as an application client; it must consume authorized APIs and must not own treasury or broker signing keys.
- No repository merge is required to maintain these boundaries.

**No branches, PRs, deployments, mobile devices or economic systems were modified.**
