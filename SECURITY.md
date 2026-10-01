# Security Policy

## Project classification

This repository is an educational/portfolio implementation of PKI and trusted-infrastructure control-plane concepts.

It is **not** a production Certificate Authority, production signing service or production HSM implementation.

## Demonstrated security concepts

- role-based access control;
- certificate lifecycle authorization;
- requester/approver separation of responsibilities;
- cryptographic policy modelling;
- audit-event generation;
- HSM / Key Vault boundary modelling;
- operational alerting;
- service-health visibility.

## Important limitations

The current implementation uses synthetic data and simulated infrastructure where appropriate.

Do not store:

- real private keys;
- production certificates;
- production credentials;
- API secrets;
- customer data;
- confidential company information.

The browser must not be treated as a security boundary.

## Production requirements

A production deployment would require:

- enterprise identity and MFA;
- server-side authorization;
- protected secrets;
- real HSM/KMS integration;
- secure CA integration;
- TLS;
- tamper-resistant audit logging;
- secure key ceremonies;
- rate limiting;
- hardened deployment;
- vulnerability management;
- backup/recovery;
- formal threat modelling;
- independent security review.

## Reporting

For this portfolio repository, report non-sensitive security issues through GitHub issues. Never publish credentials, private keys or sensitive reproduction data.
