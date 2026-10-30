# Security controls and limitations

## Starter controls
- API container runs as a non-root user.
- PostgreSQL is not published to the host.
- API port is bound to loopback (`127.0.0.1`).
- Credentials are environment-configured, not embedded in source.
- `.env` is ignored by Git.
- SQL statements use parameterized values.
- Request input is validated.
- Container health checks are configured.

## Required operator actions
- Replace the example local password before starting.
- Never commit `.env`, credentials, tokens, or real personal data.
- Use synthetic/public data only.
- Run and document dependency/base-image scanning.
- Keep GitHub Actions permissions minimal.

## Scanning
Run a Trivy image scan after building. Record the exact command, tool version, result, and accepted risks. Do not claim a clean scan until it has run.

## Limitations
This is an assessment starter, not a hardened internet-facing production service. TLS termination, authentication, rate limiting, backup automation, and production secret management are outside the initial scope.
