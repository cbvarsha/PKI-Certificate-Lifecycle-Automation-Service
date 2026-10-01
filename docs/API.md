# API Overview

This document defines the intended API documentation structure for the PKI control plane.

## Certificate lifecycle

Representative API domains:

- certificate requests;
- certificates;
- renewals;
- revocation;
- policy evaluation.

## Secure signing

Representative domains:

- signing requests;
- signing approvals;
- logical key metadata;
- HSM / Key Vault operations.

## Policy and compliance

Representative domains:

- crypto policies;
- compliance rules;
- trust configuration.

## Operations

Representative domains:

- dashboard;
- audit logs;
- events and alerts;
- system health.

## Identity

Representative domains:

- users;
- roles;
- permissions.

> Endpoint paths and request/response schemas should be generated from the checked-in backend implementation and kept synchronized with the code. This file intentionally does not invent endpoint contracts that are not currently present in the repository.
