# PKI Certificate Lifecycle Automation Service

> Enterprise-style portfolio implementation for certificate lifecycle management, trusted-infrastructure workflows, secure signing concepts, policy governance, RBAC, auditability and operational monitoring.

![Status](https://img.shields.io/badge/status-active%20development-2563eb)
![Backend](https://img.shields.io/badge/backend-Python%20%2F%20Flask-111827)
![Frontend](https://img.shields.io/badge/frontend-React%20%2F%20Vite-61DAFB)
![Database](https://img.shields.io/badge/database-SQLAlchemy-7B68EE)
![Domain](https://img.shields.io/badge/domain-PKI%20%2F%20Security-10B981)

## Overview

The **PKI Certificate Lifecycle Automation Service** is a control-plane style portfolio application for modelling how certificates and trusted infrastructure can be managed across their lifecycle.

The project brings together:

- certificate requests and policy validation;
- issuance simulation;
- certificate inventory;
- renewal and expiry monitoring;
- revocation workflows;
- secure signing request concepts;
- HSM / Key Vault abstractions;
- cryptographic policies;
- compliance rules;
- trust configuration;
- audit logs;
- security events and alerts;
- system-health monitoring;
- users, roles and permissions.

The goal is to understand the architecture and controls behind trusted infrastructure by building them into a coherent application rather than presenting isolated CRUD screens.

> **Security boundary:** This is a portfolio/learning implementation. It is not a production Certificate Authority and does not operate a real HSM. Real private keys, production credentials and customer data must not be stored in this repository.

## Architecture

```text
                 Security / PKI Operators
                           |
                           v
                 React + Tailwind UI
                           |
                           v
                    Flask REST API
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
       Policy Engine   Lifecycle     Signing / Key
                      Workflows       Controls
             |             |             |
             +-------------+-------------+
                           |
                           v
                 SQLAlchemy Persistence
                           |
             +-------------+-------------+
             |             |             |
        Certificates    Audit        Monitoring
        & Requests      Events       & Alerts
```

The UI is an operational control plane. Security-sensitive authorization and lifecycle controls should be enforced server-side in a production implementation.

## Core workflow

```text
Certificate Request
        |
        v
Policy Validation
        |
        v
Approval / Authorization
        |
        +----> Issuance Simulation
        |
        v
Active Certificate
        |
   +----+----+
   |         |
Renewal   Revocation
   |         |
   +----+----+
        |
        v
Audit + Events + Monitoring
```

## Application domains

| Domain | Representative capabilities |
|---|---|
| Certificate Management | New Request, My Requests, Certificates, Renewals, Revocation |
| Secure Signing | Signing Requests, key/signing controls, HSM/Key Vault concepts |
| Policy | Crypto Policies, Compliance Rules, Trust Configuration |
| Audit & Monitoring | Audit Logs, Events & Alerts, System Health |
| Identity & Access | Users, Roles & Permissions |
| Platform | Dashboard, settings, operational views |

## Technology

**Backend**
- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy

**Frontend**
- React
- Vite
- Tailwind CSS
- Dashboard/chart components

**Security concepts**
- PKI / certificate lifecycle
- RBAC
- separation of responsibilities
- cryptographic policy
- auditability
- HSM / Key Vault boundaries
- compliance controls

## Seeded operational data

The application is designed around meaningful seeded data rather than only a few records. Hundreds of realistic certificate records and related operational entities are used to make expiry monitoring, renewal queues and dashboard views behave more like an operational system.

The seeded data is synthetic and should never contain real customer or production information.

## Repository structure

```text
PKI-Certificate-Lifecycle-Automation-Service/
├── backend/
│   ├── app/
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   ├── package.json
│   └── Dockerfile
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API.md
│   ├── DEMO-WALKTHROUGH.md
│   ├── RUNBOOK.md
│   └── PROJECT-GUIDE.md
├── .github/
│   └── workflows/
├── docker-compose.yml
├── .env.example
├── SECURITY.md
├── CONTRIBUTING.md
└── README.md
```

> The repository documentation is being established first. Application source is kept separate from documentation commits so the implementation can be validated before it is presented as complete.

## Local development

The exact application startup commands depend on the current backend/frontend source tree. Once the source is committed, this README will contain the verified commands for the checked-in implementation.

## Engineering principles

1. Model lifecycle states explicitly.
2. Keep authorization and policy decisions server-side.
3. Separate requester and approver responsibilities where required.
4. Never expose private-key material to the browser.
5. Make operational state observable.
6. Keep simulated infrastructure clearly labelled.
7. Use synthetic data for portfolio demonstrations.
8. Document production gaps honestly.

## Production evolution

A production-grade implementation would require, at minimum:

- enterprise identity, SSO and MFA;
- server-side authorization and policy enforcement;
- managed database infrastructure;
- real CA integration;
- real HSM/KMS integration;
- protected secret management;
- TLS and secure service-to-service communication;
- tamper-resistant/immutable audit storage;
- centralized logging and monitoring;
- rate limiting;
- backup/recovery;
- vulnerability management;
- formal threat modelling;
- independent security review.

## Portfolio positioning

**PKI Certificate Lifecycle Automation Service** — Built a Flask/SQLAlchemy and React/Tailwind control-plane application to model certificate lifecycle automation, policy validation, issuance simulation, renewal and revocation workflows, secure signing concepts, RBAC, auditability, compliance controls and operational monitoring.

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [API](docs/API.md)
- [Demo Walkthrough](docs/DEMO-WALKTHROUGH.md)
- [Runbook](docs/RUNBOOK.md)
- [Project Guide](docs/PROJECT-GUIDE.md)
- [Security Policy](SECURITY.md)
- [Contributing](CONTRIBUTING.md)
