# Contributing

This project is maintained as an actively developed portfolio/reference implementation.

## Development workflow

1. Create a focused branch from `main`.
2. Keep changes scoped to one feature or fix.
3. Do not commit credentials, private keys, real certificates, `.env` files or local databases.
4. Run backend checks and the frontend production build before submitting changes.
5. Update architecture/API documentation when behaviour changes.
6. Describe security or data-model implications in the pull request.

## Commit style

Prefer concise conventional-style messages:

- `feat: add certificate renewal queue`
- `fix: enforce revocation authorization`
- `docs: document certificate lifecycle`
- `test: cover policy validation`

## Quality expectations

Changes should preserve:

- explicit lifecycle states;
- server-side authorization;
- auditability;
- clear simulated-infrastructure boundaries;
- reproducible local setup.
