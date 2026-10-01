# PKI Certificate Lifecycle Automation Service — Project Guide

This repository guide accompanies the project implementation.

## Why the project exists

The project was created to move from security/cloud fundamentals into practical infrastructure-security engineering. PKI, certificates, trust, signing and key management were selected because they require understanding how multiple security controls interact.

## What is being built

A Python Flask backend and React/Tailwind frontend model:

- certificate requests;
- policy validation;
- issuance simulation;
- renewals;
- revocation;
- signing requests;
- HSM / Key Vault concepts;
- crypto policies;
- compliance rules;
- trust configuration;
- audit logs;
- events and alerts;
- system health;
- users, roles and permissions.

## Data scale

Hundreds of realistic synthetic certificate records and related operational entities are used so expiry monitoring and operational queues behave with meaningful volume.

## Engineering focus

The project focuses on:

- backend API design;
- data modelling;
- RBAC;
- auditability;
- security boundaries;
- certificate lifecycle concepts;
- reliability and monitoring.

## Honest capability statement

This is a portfolio/learning implementation. It does not represent operation of a production CA or HSM. The value is in modelling the workflows, architecture and controls and learning how they fit together.

## Future evolution

Potential next steps include:

- stronger automated API/frontend testing;
- schema migrations;
- enterprise identity;
- production-grade persistence;
- CA integration abstraction;
- HSM/KMS adapter abstraction;
- richer compliance evaluation;
- SIEM/audit export;
- metrics and tracing;
- hardened container deployment.
