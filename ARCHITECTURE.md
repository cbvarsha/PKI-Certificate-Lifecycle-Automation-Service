# Architecture

## 1. Design intent

The PKI Certificate Lifecycle Automation Service is designed as a control plane around certificate lifecycle and trusted-infrastructure operations.

The architecture separates presentation, API orchestration, domain/control logic and persistence.

## 2. Logical architecture

```text
Users / Operators
       |
       v
React + Tailwind Control Plane
       |
       v
Flask REST API
       |
       +-------------------------------+
       |               |               |
       v               v               v
Certificate       Policy /        Signing / Key
Lifecycle         Compliance       Controls
Services          Services        Abstractions
       |               |               |
       +---------------+---------------+
                       |
                       v
              SQLAlchemy Data Layer
                       |
          +------------+------------+
          |            |            |
     Certificates    Audit       Monitoring
     Requests        Events      & Alerts
```

## 3. Frontend layer

The React/Vite frontend provides operational modules for:

- dashboard;
- certificate requests;
- certificate inventory;
- renewals;
- revocation;
- signing requests;
- HSM / Key Vault views;
- crypto policies;
- compliance rules;
- trust configuration;
- audit logs;
- events and alerts;
- system health;
- users and roles;
- settings.

Tailwind is used for the enterprise-style interface and chart/dashboard components provide operational visibility.

## 4. Backend layer

The Python Flask service provides the API boundary and application orchestration.

Flask-SQLAlchemy and SQLAlchemy provide persistence and data modelling.

Business logic should remain behind API/service boundaries so lifecycle, authorization and policy rules are not dependent on browser behaviour.

## 5. Certificate lifecycle

A representative lifecycle is:

```text
REQUESTED
   |
   v
VALIDATING
   |
   v
APPROVAL
   |
   v
ISSUANCE SIMULATION
   |
   v
ACTIVE
   |
   +-----------> RENEWAL QUEUE
   |                   |
   |                   v
   |              RENEWED / ACTIVE
   |
   +-----------> REVOCATION
                       |
                       v
                   REVOKED
```

Exact state names are implementation-specific and should be treated as part of the backend API contract.

## 6. Security boundary

The browser is not a security boundary.

A production system must enforce:

- authentication;
- authorization;
- policy validation;
- separation of duties;
- key-access controls;
- audit generation;

on the server side.

Private keys must remain within an approved HSM/KMS boundary and must never be exposed through normal application APIs.

## 7. HSM / Key Vault abstraction

The portfolio application models HSM and Key Vault concepts to understand:

- key ownership;
- key state;
- signing permissions;
- operational health;
- separation of responsibilities;
- auditability.

This does not represent a production HSM integration.

## 8. Audit and evidence

Lifecycle operations should create traceable audit events containing safe operational metadata.

Production evolution should use tamper-resistant or immutable audit storage, centralized logging and controlled evidence retention.

## 9. Reliability

Trusted infrastructure is operationally sensitive. The design therefore treats:

- certificate expiry;
- failed signing;
- service availability;
- dependency health;
- alert state;
- audit availability

as operational concerns rather than purely UI features.

## 10. Production target architecture

```text
Enterprise Identity / MFA
          |
          v
     API Gateway
          |
          v
React Control Plane
          |
          v
PKI Orchestration Services
    |          |          |
    v          v          v
   CA        HSM/KMS    Audit Store
    |          |          |
    +----------+----------+
               |
         Monitoring / SIEM
```
