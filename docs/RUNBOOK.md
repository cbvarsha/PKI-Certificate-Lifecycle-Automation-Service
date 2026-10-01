# Engineering Runbook

## Repository safety

Never commit:

- `.env`;
- secrets;
- private keys;
- real certificates;
- customer data;
- local database files.

## Local environment

The verified commands for the checked-in implementation should be maintained here once the application source is committed.

## Validation checklist

Before a release:

1. backend dependency installation succeeds;
2. backend application starts;
3. API health endpoint responds;
4. database initialization/seed succeeds;
5. frontend dependency installation succeeds;
6. frontend production build succeeds;
7. lifecycle workflows can be exercised with synthetic data;
8. authorization boundaries are checked;
9. audit events are generated;
10. Docker build succeeds if containerized deployment is enabled.

## Incident troubleshooting

### API unavailable

Check the backend process/container, dependency installation, environment variables and database connectivity.

### Frontend cannot reach API

Check the configured API base URL and browser network requests.

### Empty dashboard

Check database initialization and seed execution before changing UI code.

### Incorrect certificate counts

Validate the backend query/filter first. The frontend should not independently invent lifecycle state.

## Data reset

Use the project-specific database reset/seed command only after confirming the implementation's documented behaviour. Never reset a production database with demo commands.
