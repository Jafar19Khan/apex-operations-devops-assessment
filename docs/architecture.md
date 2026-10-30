# Architecture

## Scope
A local, reproducible demonstration. The assessment does not require cloud deployment.

## Components
- Flask API served by Gunicorn.
- PostgreSQL database.
- Docker Compose for local orchestration.
- GitHub Actions for lint, tests, and image build.
- Prometheus-compatible `/metrics` endpoint and scrape configuration.

## Request flow
1. Client calls the API on `127.0.0.1:8000`.
2. Flask validates the request.
3. Data operations connect to PostgreSQL using `DATABASE_URL`.
4. PostgreSQL stores records in the `postgres_data` named volume.
5. API logs are emitted to stdout.

## Health semantics
- `/health`: process-level liveness.
- `/ready`: verifies PostgreSQL can execute `SELECT 1`.
- Compose waits for the database health check before starting the API.

## CI flow
GitHub Actions installs dependencies, runs Ruff and Pytest, then builds the image only if quality checks pass.
