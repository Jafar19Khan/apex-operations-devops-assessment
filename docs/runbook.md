# Runbook

## Start
```powershell
Copy-Item .env.example .env
# Edit .env; use a unique local-only password and keep DATABASE_URL in sync.
docker compose up --build -d
```

## Verify
```powershell
docker compose ps
Invoke-RestMethod http://localhost:8000/health
Invoke-RestMethod http://localhost:8000/ready
Invoke-RestMethod http://localhost:8000/api/v1/operations
```

## Logs
```powershell
docker compose logs --tail=100 api
docker compose logs --tail=100 db
```

## API unavailable
1. Run `docker compose ps`.
2. Inspect `docker compose logs api`.
3. Check whether local port 8000 is already in use.
4. Verify the API health endpoint from inside the container.

## Readiness returns 503
1. Inspect database logs and service health.
2. Verify `DATABASE_URL` matches the database name, username, password, and service hostname `db`.
3. Do not expose the password in screenshots or logs.

## Missing database schema
The SQL initialization script runs only when PostgreSQL initializes an empty data directory. `docker compose down -v` followed by `docker compose up --build -d` recreates it but deletes all database data. Use only when data loss is acceptable.

## Stop
```powershell
docker compose down
```
