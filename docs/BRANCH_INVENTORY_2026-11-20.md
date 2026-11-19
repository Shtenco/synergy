# Shtenco / SYNERGY — полный реестр Git-веток

**Срез:** 2026-11-20  
**Охват:** 92 репозитория, видимые установленному GitHub App.  
**Источник:** полный 2026-11-20 census для 91 прежнего репозитория, live branch-audit tranche и current PR-head metadata.

## Контрольные числа

- Репозитории: **92/92**
- Branch refs: **1,294**
- Сумма уникальных HEAD внутри репозиториев: **1,208**
- Повторные refs на уже существующий HEAD внутри того же репозитория: **86**
- Live SHA provenance: **1,084**
- SHA из dated census, не перепроверенные в этой итерации: **210**
- Во всех 92 репозиториях default branch — `main`.
- Защита: старый census указывал **0/1,292** защищённых refs; защита двух новых refs cognitive-memory repository не проверена и отмечена `null`.

Уникальный HEAD считается внутри репозитория, а не глобально. Совпадение HEAD не является анализом PR или разрешением на удаление ветки.

## Источники SHA

В canonical JSON/CSV каждая ветка имеет `head_sha_source` и `head_sha_observed_at`. Значения `LIVE_BRANCH_AUDIT_2026-11-20` и `LIVE_PR_METADATA` имеют соответствующую живую provenance. Значение `HISTORICAL_CENSUS_2026-11-20` означает, что SHA взят из датированного census, а не заново запрошен в этом проходе.

## Новое обнаружение

`Shtenco/synergy_hierarchical_cognitive_memory_architecture` добавлен как 92-й репозиторий:
- `main` — `74b518c85d3a69fdc2e868737cbe9f4f2cac761c`;
- `feat/hierarchical-cognitive-memory-v1` — `2d6d7872653b9d525a74046e992a843b2a905d57`.

## Canonical artifacts

- [JSON](../registry/BRANCH_INVENTORY_2026-11-20.json)
- [CSV](../registry/BRANCH_INVENTORY_2026-11-20.csv)
- [Live reconciliation](LIVE_RECONCILIATION_2026-11-20.md)

**Ограничение:** 210 исторических SHA не были перепроверены, две новые ветки не имеют проверенного protection state, а source/CI аудит всех 1,294 refs не завершён.
