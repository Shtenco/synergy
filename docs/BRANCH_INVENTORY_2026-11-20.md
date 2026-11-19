# Shtenco / SYNERGY — полный реестр Git-веток

**Срез:** 2026-11-20 · **Охват:** 92 репозитория · **1,294 refs**.

## Контрольные числа

- Репозитории: **92/92**
- Branch refs: **1,294**
- Уникальные HEAD внутри репозиториев: **1,208**
- Повторные refs на существующий HEAD внутри того же репозитория: **86**
- Все 1,294 refs имеют SHA с live provenance из branch audit, priority PR metadata или свежего compare-to-main.
- Ancestry compare-to-main выполнен для **210 refs**:
  - **36 AHEAD** — ветка содержит коммиты сверх main, main не содержит дополнительных коммитов относительно неё;
  - **22 BEHIND** — main содержит дополнительные коммиты, ветка не содержит собственных дополнительных;
  - **120 DIVERGED** — обе стороны имеют уникальные коммиты;
  - **32 IDENTICAL** — HEAD совпадает с main.
- Ещё **1,084 refs** имеют live SHA, но пока не прошли ancestry comparison в этом проходе.
- Защита: старый census указывал **0/1,292** защищённых refs; защита двух новых refs cognitive-memory repository не проверена и отмечена `null`.

## Существенные ancestry-находки

Особенно большие независимые веточные поколения:
- `synergistic_economics/research/bank-deposit-credit-audit-fix-20261115`: 1,165 коммитов впереди main.
- `synergistic_economics/research/financial-register-instance-provenance-v1`: 1,021 впереди.
- `synergistic_economics/feature/canonical-economic-entity-register-v1-rebased-20261115`: 914 впереди.
- `synergistic_metaverse/integration/rf-gnss-business-twin-rebased-20261116c`: 471 впереди и 4 позади.
- `synergistic_economics/audit-russian-readme`: main опережает ветку на 450 коммитов.
- `synergistic_economics/unified-economic-balance`: main опережает на 450, ветка имеет 13 собственных коммитов.
- `synergy/feature/web-ecosystem-v8-federation-20261014`: main опережает ветку на 241 коммит.

Это не решения об удалении. Каждая ветка требует отдельной проверки PR, tags, releases, workflows, issue links и межрепозиторных ссылок.

## Источники SHA

В canonical JSON/CSV каждая ветка имеет `head_sha_source`, `head_sha_observed_at`, `branch_relation_to_main`, `branch_ahead_of_main`, `main_ahead_of_branch` и `merge_base_sha` там, где сравнение выполнено.

## Новое обнаружение

`Shtenco/synergy_hierarchical_cognitive_memory_architecture` добавлен как 92-й репозиторий:
- `main` — `74b518c85d3a69fdc2e868737cbe9f4f2cac761c`;
- `feat/hierarchical-cognitive-memory-v1` — `2d6d7872653b9d525a74046e992a843b2a905d57`.

## Canonical artifacts

- [JSON](../registry/BRANCH_INVENTORY_2026-11-20.json)
- [CSV](../registry/BRANCH_INVENTORY_2026-11-20.csv)
- [Live reconciliation](LIVE_RECONCILIATION_2026-11-20.md)

**Ограничение:** ancestry сравнение выполнено для 210 refs, не для всех 1,294. Защита веток не перепроверена административным API; 0/1,292 — исторический census, две новые refs не проверены.
