# SYNERGY Live Branch Audit — SHHTS, SHTTPS and Post-Quantum Radio

**Audit date:** 2026-11-20  
**Scope:** live branch HEADs, open PRs and latest 10 workflow runs for three transport/security repositories.  
**Method:** read-only GitHub REST; purpose cross-checked against current main README; exact branch SHA and PR associations fetched live.  
**Limit:** no radio hardware, network endpoint, cryptographic implementation or secure channel was tested.

## Summary

| Repository | Role / implementation boundary | Branches | Open PRs | Latest workflow | Main CI | Decision |
|---|---|---:|---:|---|---|---|
| [`Shtenco/synergy_shhts`](https://github.com/Shtenco/synergy_shhts) | Experimental infrastructure/security transport node; current main explicitly STUB with no sufficiently evidenced implementation. | 1 | 0 | none observed | CI_NOT_VERIFIED / no main implementation evidence | Keep as specifications/stubs; do not admit as production transport. |
| [`Shtenco/synergy_shttps`](https://github.com/Shtenco/synergy_shttps) | Experimental secure application transport node; current main explicitly STUB, not a production HTTPS replacement or protocol. | 3 | 2 | SHTTPS protocol CI: failure @ feat/stcp-shttps-remote-mcp-v2-20260925/f3eda6bb7cdf | CI_NOT_VERIFIED / no main implementation evidence | Keep as specifications/stubs; do not admit as production transport. |
| [`Shtenco/synergy_post_quantum_radio`](https://github.com/Shtenco/synergy_post_quantum_radio) | UART/LoRa/SDR post-quantum transport specification; current main contains README only, no runtime/tests/build/CI/evidence. | 2 | 1 | rust-ci: failure @ feat/pq-radio-teleportation-v1-20260927/2938d6aa1e93 | CI_NOT_VERIFIED / no main implementation evidence | Keep as specifications/stubs; do not admit as production transport. |

## synergy_shhts

**Purpose:** Experimental infrastructure/security transport node; current main explicitly STUB with no sufficiently evidenced implementation.  
**Current main:** `8d8c1d2f7b0b1983aaaee92fa56544ceb9382c51`.  
**Open PRs:** 0.  
**Latest workflow observations:** none.

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `main` | `8d8c1d2f7b0b1983aaaee92fa56544ceb9382c51` | Canonical default branch | MAIN | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry and consumers before cleanup. Need source tree, protocol framing, threat model, tests and reproducible endpoint interoperability. Retain canonical stub/spec; exclude from deployed capability inventory. |

## synergy_shttps

**Purpose:** Experimental secure application transport node; current main explicitly STUB, not a production HTTPS replacement or protocol.  
**Current main:** `f7207aa8082c78399e4130f4eaf29ff8984c5413`.  
**Open PRs:** 2.  
**Latest workflow observations:** SHTTPS protocol CI=failure @ feat/stcp-shttps-remote-mcp-v2-20260925/f3eda6bb7cdf (2026-09-25T07:15:04Z); SHTTPS protocol CI=failure @ feat/stcp-shttps-remote-mcp-v2-20260925/f3eda6bb7cdf (2026-09-25T07:15:01Z); SHTTPS protocol CI=failure @ feat/stcp-shttps-remote-mcp-v2-20260925/37423c8fce07 (2026-09-25T07:14:31Z); SHTTPS protocol CI=failure @ feat/stcp-shttps-remote-mcp-v2-20260925/37423c8fce07 (2026-09-25T07:14:28Z); SHTTPS protocol CI=failure @ feat/stcp-shttps-remote-mcp-v2-20260925/ae0c50c45d12 (2026-09-25T07:13:57Z); SHTTPS protocol CI=failure @ feat/stcp-shttps-remote-mcp-v2-20260925/ae0c50c45d12 (2026-09-25T07:13:53Z); SHTTPS protocol CI=failure @ feat/stcp-shttps-remote-mcp-v2-20260925/a7f08cd3f73b (2026-09-25T07:13:20Z); SHTTPS protocol CI=failure @ feat/stcp-shttps-remote-mcp-v2-20260925/a7f08cd3f73b (2026-09-25T07:13:19Z); SHTTPS protocol CI=failure @ feat/stcp-shttps-remote-mcp-v2-20260925/e9c291aa1aee (2026-09-25T07:13:16Z); SHTTPS protocol CI=failure @ feat/stcp-shttps-remote-mcp-v2-20260925/1f0008c4b534 (2026-09-25T07:12:53Z).

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `feat/shttps-v1-pq-compressed-protocol` | `7f3072d5a86b95fa4bb1da52fbad7395fee4e88f` | feat: SHTTPS v1 post-quantum compressed federation protocol | #1 ready | NOT_OBSERVED in latest-10 workflow window | PR base=main; require source, tests and threat-model review. Need defined wire protocol, certificate/key lifecycle, downgrade/replay protections and interoperability tests. Retain candidate; no promotion without executable tests and independent security review. |
| `feat/stcp-shttps-remote-mcp-v2-20260925` | `f3eda6bb7cdfd5478f9594dad4ee5dd91381e9b8` | Transport Convergence T1: STCP + SHTTPS v2 + SYNERGY Remote MCP | #2 ready | failure (SHTTPS protocol CI, 2026-09-25T07:15:04Z) | PR base=main; require source, tests and threat-model review. Need defined wire protocol, certificate/key lifecycle, downgrade/replay protections and interoperability tests. Retain candidate; no promotion without executable tests and independent security review. |
| `main` | `f7207aa8082c78399e4130f4eaf29ff8984c5413` | Canonical default branch | MAIN | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry and consumers before cleanup. Need defined wire protocol, certificate/key lifecycle, downgrade/replay protections and interoperability tests. Retain canonical stub/spec; exclude from deployed capability inventory. |

## synergy_post_quantum_radio

**Purpose:** UART/LoRa/SDR post-quantum transport specification; current main contains README only, no runtime/tests/build/CI/evidence.  
**Current main:** `b3084f709aaa1023289cfec6e550a1a35d884513`.  
**Open PRs:** 1.  
**Latest workflow observations:** rust-ci=failure @ feat/pq-radio-teleportation-v1-20260927/2938d6aa1e93 (2026-09-27T20:07:52Z); rust-ci=failure @ feat/pq-radio-teleportation-v1-20260927/2938d6aa1e93 (2026-09-27T20:07:49Z); rust-ci=failure @ feat/pq-radio-teleportation-v1-20260927/ef80e0ba5540 (2026-09-27T20:07:41Z); rust-ci=failure @ feat/pq-radio-teleportation-v1-20260927/ef80e0ba5540 (2026-09-27T20:07:37Z); rust-ci=failure @ feat/pq-radio-teleportation-v1-20260927/87999565653c (2026-09-27T20:07:34Z); rust-ci=failure @ feat/pq-radio-teleportation-v1-20260927/bb2ff4d37737 (2026-09-27T20:07:32Z); rust-ci=failure @ feat/pq-radio-teleportation-v1-20260927/30e6088b4568 (2026-09-27T20:06:50Z); rust-ci=failure @ feat/pq-radio-teleportation-v1-20260927/30e6088b4568 (2026-09-27T20:06:49Z); rust-ci=failure @ feat/pq-radio-teleportation-v1-20260927/f1db8b37ab7f (2026-09-27T20:06:47Z); rust-ci=failure @ feat/pq-radio-teleportation-v1-20260927/52a4266a4fef (2026-09-27T20:06:05Z).

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `feat/pq-radio-teleportation-v1-20260927` | `2938d6aa1e939b198fb4e98bb32b3cbfc958f6e4` | feat: R3 real hardware PQ radio + PI-PQ forensics | #1 ready | failure (rust-ci, 2026-09-27T20:07:52Z) | PR base=main; require source, tests and threat-model review. Need concrete PQ algorithm suite, UART/LoRa/SDR hardware runtime, side-channel analysis, radio link tests and independent cryptographic review. Retain candidate; no promotion without executable tests and independent security review. |
| `main` | `b3084f709aaa1023289cfec6e550a1a35d884513` | Canonical default branch | MAIN | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry and consumers before cleanup. Need concrete PQ algorithm suite, UART/LoRa/SDR hardware runtime, side-channel analysis, radio link tests and independent cryptographic review. Retain canonical stub/spec; exclude from deployed capability inventory. |

## Disposition

All three repositories remain separate experimental transport/security domains. They should not be counted as available network capabilities until source, test, build, threat model, cryptographic review and end-to-end interoperability evidence exist. Their parent links to Meta-OS are architecture declarations, not runtime dependencies.

**No branches, PRs, hardware or network configuration were modified.**
