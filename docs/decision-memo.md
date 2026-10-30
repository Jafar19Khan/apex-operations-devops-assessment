# Technical decision memo

## Context
The assessment requests a small API, reproducible local deployment, CI checks, safe release/rollback, basic observability, security hygiene, and a cloud-hosting proposal.

## Decisions
| Decision | Rationale | Trade-off |
|---|---|---|
| Flask | Lightweight and explainable for a small API | Fewer built-in conventions than larger frameworks |
| PostgreSQL | Demonstrates a real dependency and persistence | Requires a database container |
| Docker Compose | Reproducible local multi-container deployment | Not a production cluster orchestrator |
| GitHub Actions | Repository-native CI | Uses a hosted runner |
| Pytest + Ruff | Straightforward tests and linting | Coverage thresholds are not configured |
| Prometheus client | Exposes basic request metrics | Alert rules/dashboard need further configuration |

## Assumptions
- Local deployment is the execution target.
- Synthetic data is sufficient.
- No paid cloud resources or Apex production access will be used.

## Limitations and next improvements
- Complete and verify release/rollback evidence.
- Add meaningful alert rules if justified.
- Run and document Trivy scans.
- Consider TLS, authentication, backups, and migration tooling only for a justified deployment target.
