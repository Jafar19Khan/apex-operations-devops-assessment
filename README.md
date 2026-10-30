# Apex Operations API — DevOps Assessment

Starter project for the Apex AI Arabia Junior DevOps Engineer assessment.

## Scope
A small Flask API, PostgreSQL dependency, Docker Compose deployment, GitHub Actions CI, basic metrics, security notes, release/rollback plan, and evidence checklist. This is a local assessment project; it does not access Apex production systems or use paid cloud resources.

## Prerequisites
- Python 3.11+
- Git
- Docker Desktop with Docker Compose v2
- PowerShell and VS Code

## Quick start (PowerShell)
1. `Copy-Item .env.example .env`
2. Edit `.env` and replace the example local database password with a unique local-only value. Keep the password in sync in `POSTGRES_PASSWORD` and `DATABASE_URL`.
3. `docker compose up --build -d`
4. `docker compose ps`
5. `Invoke-RestMethod http://localhost:8000/health`
6. `Invoke-RestMethod http://localhost:8000/ready`
7. `Invoke-RestMethod http://localhost:8000/api/v1/operations`

Create a sample operation:
```powershell
$body = @{ name = "assessment-demo"; status = "created" } | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri http://localhost:8000/api/v1/operations -ContentType "application/json" -Body $body
```

Logs: `docker compose logs --tail=100 api`
Stop: `docker compose down`

PostgreSQL data is persisted in the `postgres_data` named volume. `docker compose down -v` deletes that data; use it only when intentional.

## Quality checks
```powershell
ruff check .
pytest -m "not intentional_failure" -q
```
The controlled intentional-failure demonstration is excluded from normal CI:
```powershell
pytest -m intentional_failure -q
```
That command is expected to return a failure. Capture its output, then run the normal suite again. Do not leave the normal CI pipeline red.

## CI
GitHub Actions runs Ruff, the normal test suite, and a Docker image build. The build job depends on successful quality checks. It does not deploy to cloud infrastructure.

## Documentation
See `docs/` for architecture, runbook, rollback, security, decision memo, and evidence checklist. Update `AI_DISCLOSURE.md` to accurately describe the assistance actually used.

## Important
This is a starter implementation, not proof of a successful deployment or test run. Run and verify every command in your own environment before claiming completion.
