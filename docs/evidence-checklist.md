# Evidence checklist

Capture genuine output from your own execution. Redact secrets and personal information.

- [ ] `docker compose ps` showing API and database status
- [ ] `/health` response
- [ ] `/ready` response with database connected
- [ ] Successful API create/list requests
- [ ] Normal automated test run with passing tests
- [ ] Intentional-failure test showing expected non-zero result
- [ ] Successful GitHub Actions run
- [ ] Failed-test CI run proving release gate behavior
- [ ] Docker image tags for two versions
- [ ] Rollback command output and post-rollback health/readiness
- [ ] Structured application logs
- [ ] Trivy scan output and findings
- [ ] Failure investigation: symptom, logs, root cause, fix, recovery
- [ ] Architecture diagram
- [ ] Final repository tree and README instructions
