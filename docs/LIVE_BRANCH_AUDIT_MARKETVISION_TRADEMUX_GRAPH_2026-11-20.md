# SYNERGY Live Branch Audit — MarketVision, TradeMux and Graph Research

**Audit date:** 2026-11-20  
**Scope:** live branch HEADs, open PRs and latest 10 workflow runs for three market/graph repositories.  
**Method:** read-only GitHub REST; exact branch SHA and PR head/base associations. CI credited only to exact SHA observations.  
**Limit:** no broker execution, venue routing, live market feed or external graph ground-truth validation was performed.

## Summary

| Repository | Role | Branches | Open PRs | Latest workflow | Main CI | Disposition |
|---|---|---:|---:|---|---|---|
| [`Shtenco/synergy_marketvision`](https://github.com/Shtenco/synergy_marketvision) | Market visualization, analytics, charting and trader decision interfaces | 3 | 0 | ci: failure @ main/1baf9fa65c99 | CI_NOT_VERIFIED absent exact-main checks | Analytics, routing and graph research remain separate capabilities. |
| [`Shtenco/synergy_trademux`](https://github.com/Shtenco/synergy_trademux) | Trade routing/multiplexer, venue selection and execution orchestration | 3 | 0 | ci: failure @ main/fe584afeba14 | CI_NOT_VERIFIED absent exact-main checks | Analytics, routing and graph research remain separate capabilities. |
| [`Shtenco/synergy_epstein_network`](https://github.com/Shtenco/synergy_epstein_network) | Graph/network research and relationship analysis | 6 | 0 | vendor-and-build: failure @ main/48a00e43026f | CI_NOT_VERIFIED absent exact-main checks | Analytics, routing and graph research remain separate capabilities. |

## synergy_marketvision

**Role:** Market visualization, analytics, charting and trader decision interfaces.  
**Current main:** `1baf9fa65c9974bb241f3a4fb2a352424bfe9bcc`.  
**Open PRs:** 0.  
**Latest 10 workflow observations:** ci=failure @ main/1baf9fa65c99 (2026-10-24T02:35:11Z); ci=failure @ main/963d6b9c8790 (2026-10-24T02:35:09Z); ci=failure @ main/fb2fb0d58f72 (2026-10-24T02:35:07Z); ci=failure @ main/d247aa656dec (2026-10-24T01:29:13Z); ci=failure @ main/937697293b53 (2026-10-23T20:08:12Z); ci=failure @ main/16394054ae0d (2026-10-19T19:17:01Z); ci=failure @ main/cd355ade1e66 (2026-09-29T01:38:57Z); ci=failure @ main/66472082641c (2026-09-29T01:23:14Z); ci=failure @ main/2a855b293068 (2026-09-28T20:43:58Z); ci=failure @ main/a1bf3551b6d0 (2026-09-28T20:43:12Z).

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `enterprise/v2.0.0` | `beccaaaac02ee80bc79b31b5ab2f417c2072d85e` | Inferred from branch name: enterprise v2.0.0 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry and downstream consumers. Charts and visual analytics are not authoritative execution signals; data freshness, timezone and source provenance must be explicit. Retain pending branch lifecycle review. |
| `main` | `1baf9fa65c9974bb241f3a4fb2a352424bfe9bcc` | Canonical default branch | MAIN | failure (ci, 2026-10-24T02:35:11Z) | No open PR; purpose inferred; inspect ancestry and downstream consumers. Charts and visual analytics are not authoritative execution signals; data freshness, timezone and source provenance must be explicit. Retain canonical; exact runtime/API and security evidence required. |
| `production/v3.0.0` | `6dbe5c5b9d846b66cabc9136deb24dfd34cec842` | Inferred from branch name: production v3.0.0 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry and downstream consumers. Charts and visual analytics are not authoritative execution signals; data freshness, timezone and source provenance must be explicit. Retain pending branch lifecycle review. |

## synergy_trademux

**Role:** Trade routing/multiplexer, venue selection and execution orchestration.  
**Current main:** `fe584afeba1410f40640672f277be4ab16e76b8c`.  
**Open PRs:** 0.  
**Latest 10 workflow observations:** ci=failure @ main/fe584afeba14 (2026-10-24T02:35:19Z); ci=failure @ main/e9e55cc1ea97 (2026-10-24T02:35:16Z); ci=failure @ main/1e88681ef365 (2026-10-24T02:35:14Z); ci=failure @ main/d855d46bcfab (2026-10-23T20:08:07Z); ci=failure @ main/320a2d0161bf (2026-10-19T19:02:20Z); ci=failure @ main/65b316b7143f (2026-09-29T01:39:15Z); ci=failure @ main/350516d009cf (2026-09-29T01:25:39Z); ci=failure @ main/a3c1fa7bd007 (2026-09-28T18:04:40Z); ci=failure @ main/365d3a23bd80 (2026-09-28T18:03:51Z); ci=failure @ main/4fbf39b7ee8c (2026-09-28T18:01:51Z).

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `enterprise/v2.0.0` | `d1aca7234dadaa86286d08466efe51a9a88fc4f4` | Inferred from branch name: enterprise v2.0.0 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry and downstream consumers. Route selection needs venue health, fees, depth, latency, partial-fill, retry/idempotency and risk-limit controls. Retain pending branch lifecycle review. |
| `main` | `fe584afeba1410f40640672f277be4ab16e76b8c` | Canonical default branch | MAIN | failure (ci, 2026-10-24T02:35:19Z) | No open PR; purpose inferred; inspect ancestry and downstream consumers. Route selection needs venue health, fees, depth, latency, partial-fill, retry/idempotency and risk-limit controls. Retain canonical; exact runtime/API and security evidence required. |
| `production/v3.0.0` | `5255319629b44c9651cc4424c5b9d0b3ae16fe71` | Inferred from branch name: production v3.0.0 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry and downstream consumers. Route selection needs venue health, fees, depth, latency, partial-fill, retry/idempotency and risk-limit controls. Retain pending branch lifecycle review. |

## synergy_epstein_network

**Role:** Graph/network research and relationship analysis.  
**Current main:** `48a00e43026f441a3b95a5e91bd442b8174f0c10`.  
**Open PRs:** 0.  
**Latest 10 workflow observations:** vendor-and-build=failure @ main/48a00e43026f (2026-11-16T11:16:56Z); vendor-and-build=failure @ main/48a00e43026f (2026-11-09T11:31:12Z); vendor-and-build=cancelled @ main/48a00e43026f (2026-11-02T11:06:22Z); vendor-and-build=failure @ main/48a00e43026f (2026-10-26T08:55:13Z); vendor-and-build=cancelled @ main/48a00e43026f (2026-10-24T02:35:26Z); test=success @ main/48a00e43026f (2026-10-24T02:35:26Z); test=success @ main/f8338bbd5468 (2026-10-24T02:35:24Z); vendor-and-build=cancelled @ main/f8338bbd5468 (2026-10-24T02:35:24Z); test=success @ main/4d63998a4572 (2026-10-24T02:35:21Z); vendor-and-build=cancelled @ main/4d63998a4572 (2026-10-24T02:35:21Z).

| Branch | Live HEAD SHA | Purpose | State / PR | CI evidence | Blockers / decision |
|---|---|---|---|---|---|
| `build/master-graph-v1` | `6fb950e6eca96e82e98422cba516202c94025301` | Inferred from branch name: build master graph v1 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry and downstream consumers. Graph edges require source provenance, confidence, entity-resolution controls and false-positive analysis; do not infer culpability from network proximity. Retain pending branch lifecycle review. |
| `build/v2-vendor-entity-resolution` | `feb8c37d1bd442ce8b73bb401e9e5bb8d16a5c9a` | Inferred from branch name: build v2 vendor entity resolution | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry and downstream consumers. Graph edges require source provenance, confidence, entity-resolution controls and false-positive analysis; do not infer culpability from network proximity. Retain pending branch lifecycle review. |
| `data/direct-vendor-v2` | `bd6ff52e1556d39a80fcea49e2ae93e7e0532001` | Inferred from branch name: data direct vendor v2 | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry and downstream consumers. Graph edges require source provenance, confidence, entity-resolution controls and false-positive analysis; do not infer culpability from network proximity. Retain pending branch lifecycle review. |
| `fix/actions-bootstrap` | `e6e56fd94b4cbb03704551e06369d7d7cf176c1d` | Inferred from branch name: fix actions bootstrap | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry and downstream consumers. Graph edges require source provenance, confidence, entity-resolution controls and false-positive analysis; do not infer culpability from network proximity. Retain pending branch lifecycle review. |
| `fix/zero-dependency-vendoring` | `2e3a609d1dfe946ceb44aab31e043162d6c85ce4` | Inferred from branch name: fix zero dependency vendoring | NO_OPEN_PR | NOT_OBSERVED in latest-10 workflow window | No open PR; purpose inferred; inspect ancestry and downstream consumers. Graph edges require source provenance, confidence, entity-resolution controls and false-positive analysis; do not infer culpability from network proximity. Retain pending branch lifecycle review. |
| `main` | `48a00e43026f441a3b95a5e91bd442b8174f0c10` | Canonical default branch | MAIN | failure (vendor-and-build, 2026-11-16T11:16:56Z) | No open PR; purpose inferred; inspect ancestry and downstream consumers. Graph edges require source provenance, confidence, entity-resolution controls and false-positive analysis; do not infer culpability from network proximity. Retain canonical; exact runtime/API and security evidence required. |

## Integration decisions

- MarketVision can supply observation/visualization but not order authority.
- TradeMux can route approved intents only after deterministic risk authorization and venue-specific execution checks.
- Graph research remains a separate evidence domain with provenance and uncertainty labels.
- No branch deletion or merge should be based solely on lack of open PR.

**No branches, PRs, market accounts or graph datasets were modified.**
