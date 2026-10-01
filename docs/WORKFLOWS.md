# PKI Workflow Catalogue

## Certificate lifecycle

```mermaid
flowchart LR
 A[New Request] --> B[Input Validation]
 B --> C[Policy Evaluation]
 C --> D{Compliant?}
 D -- No --> E[Reject / Remediate]
 D -- Yes --> F[Pending Approval]
 F --> G{Approver Decision}
 G -- Reject --> H[Rejected]
 G -- Approve --> I[Issue Certificate]
 I --> J[Active Inventory]
 J --> K{Lifecycle Event}
 K --> L[Renew]
 K --> M[Revoke]
 L --> J
 M --> N[Revoked]
 F --> O[Audit Event]
 I --> O
 L --> O
 M --> O
```

## Approval and separation of duties

```mermaid
sequenceDiagram
 participant R as Requester
 participant P as Policy Engine
 participant A as PKI Approver
 participant C as CA Service
 participant L as Audit Log
 R->>P: Submit certificate request
 P->>P: Validate algorithm / validity / environment
 P->>A: Create pending approval
 A->>A: Review request and policy evidence
 A->>C: Approve issuance
 C-->>R: Certificate becomes available
 A->>L: Record approval
 C->>L: Record issuance
```

## Revocation

A revocation changes certificate lifecycle state, records the revocation timestamp and emits an audit event. A production implementation would additionally update CA revocation services such as CRL/OCSP.
