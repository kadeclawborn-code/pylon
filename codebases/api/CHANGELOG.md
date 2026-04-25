# Changelog

All notable changes to `pylon-api`. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), versioning per [SemVer](https://semver.org/spec/v2.0.0.html).

## [2.4.2] — 2026-04-23

### Fixed
- Switchyard webhook signature verification now auto-rotates GitHub App keys via JWKS endpoint, with a 12h refresh cycle. Previously the key was hardcoded; key rotation upstream caused a 90-minute production incident on 2026-04-22 (PYL-306).

## [2.4.1] — 2026-04-09

### Fixed
- Marketplace publishing form description field on Safari (PYL-304). TanStack Form interaction with Safari's input event was clearing pasted content on first keystroke.

## [2.4.0] — 2026-03-29

### Added
- Beacon Rule Marketplace public preview (PYL-100). Customers can now publish custom rules and subscribe to others. Includes versioning, rule-detail browsing, fire-rate aggregates.
- Per-rule fire rate visibility on the rules listing page (PYL-224).
- Pylon CI status check name customization (PYL-225).

### Changed
- Audit log queries now stream for >10k rows (PYL-303). Page-query window capped at 30 days; longer windows must use export.

## [2.3.0] — 2026-03-15

### Added
- Audit logs (PYL-103, PYL-217–PYL-220). Available on Business+ tier. 1y retention on Business, 7y on Enterprise.
- CSV / JSON export for audit logs.
- SOC 2 Type II evidence query API stub (full Auditor portal lands in 2.5.x for the Q3 audit window).

## [2.2.0] — 2026-03-13

### Added
- GitLab MR analyzer pipeline integration (PYL-209). MR open/update events now trigger Beacon analyzer runs same as GitHub PRs.
- GitLab merge-block enforcer in review (PYL-210).

## [2.1.5] — 2026-02-12

### Changed
- Migrated `pgvector` 0.5 → 0.7 for Beacon's similarity search (PYL-401).

## [2.1.0] — 2026-02-02

### Added
- Tower team-comparison data API (PYL-213). Multi-team comparison endpoint with permissions check.

### Fixed
- Beacon `python.bare-except` no longer triggers on test fixtures by default (PYL-302). Customers can override scoping.

## [2.0.0] — 2026-01-30

### Added
- Audit log UI for Business+ tier (PYL-218).

### Changed
- **BREAKING**: `Finding.severity` enum normalized to `info | low | medium | high | blocking`. Customers using old severity strings (`warning`, `error`) need to update their suppression configs. Migration guide in docs.
- FastAPI 0.110 → 0.115 (PYL-400). Pydantic v2 `model_validator` rename in one schema.

## [1.9.0] — 2025-12-19

### Added
- Audit log event schema and ingest (PYL-217). Append-only Postgres table; PII-sanitized rule diffs.

## [1.8.5] — 2025-12-15

### Fixed
- Tower cycle-time chart now shows actual time for repos with single-developer history (PYL-301). Previously excluded as "self-reviews."

## [1.8.0] — 2025-12-05

### Added
- GitLab MR comment poster (PYL-207). Pylon comments now post to GitLab MRs, matching GitHub UX.
- GitLab OAuth + token refresh (PYL-208). Customers can install Pylon via GitLab Cloud OAuth.

## [1.7.0] — 2025-11-21

### Added
- GitLab webhook ingest (PYL-206). Switchyard endpoint accepts GitLab webhook payloads. HMAC-SHA256 verification, latency p95 < 1.5s.

## [1.6.1] — 2025-10-30

### Fixed
- GitHub App reinstall now re-registers webhook subscriptions (PYL-300). Prior versions only registered on initial install. 11 customer orgs identified and backfilled.

## [1.6.0] — 2025-10-26

### Added
- Switchyard hardening pass post-Q3 incident: structured retries, dead-letter queue, latency p95 instrumentation.

---

Earlier history (versions 1.0 – 1.5) lives in the `pre-2025-q4` archive branch. Notable lineage there: original Beacon analyzer in 1.0 (Jan 2025); GitHub App support in 1.2 (Mar 2025); Tower v0 ingest pipeline in 1.4 (Aug 2025).
