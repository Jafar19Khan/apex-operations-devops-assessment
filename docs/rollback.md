# Release and rollback plan

## Image versioning
Use immutable tags such as `apex-operations-api:v1.0.0` and `v1.0.1`. Do not rely on `latest` as the only release identifier.

## Demonstration procedure
1. Build a known-good image and tag it `v1.0.0`.
2. Deploy it and verify `/health` and `/ready`.
3. Make a controlled application change and build `v1.0.1`.
4. Deploy the second image and capture the result.
5. If unhealthy, restore the Compose image reference to `v1.0.0`.
6. Recreate the API container and verify health/readiness.
7. Capture image tags, commands, container status, and post-rollback checks.

Finalize exact commands and run the demonstration before claiming rollback is verified.

## Data compatibility
This starter does not automate schema migrations. Production releases should use backward-compatible expand/contract migrations and verified backups before destructive schema changes.
