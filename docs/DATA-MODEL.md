# Data Model

```mermaid
erDiagram
 USER ||--o{ CERTIFICATE_REQUEST : creates
 USER ||--o{ AUDIT_EVENT : performs
 ROLE ||--o{ USER : assigned
 CERTIFICATE_REQUEST ||--o| CERTIFICATE : issues
 CERTIFICATE ||--o{ AUDIT_EVENT : produces
 CRYPTO_POLICY ||--o{ CERTIFICATE_REQUEST : governs
 TRUST_AUTHORITY ||--o{ CERTIFICATE : issues
 HSM_INSTANCE ||--o{ SIGNING_REQUEST : protects
 USER ||--o{ SIGNING_REQUEST : requests
 SIGNING_REQUEST ||--o{ AUDIT_EVENT : produces

 CERTIFICATE {
   string id
   string commonName
   string type
   string environment
   string issuer
   datetime issueDate
   datetime expiryDate
   string status
   string keyAlgorithm
   string serial
 }
 CERTIFICATE_REQUEST {
   string id
   string requester
   string status
   string environment
   string keyAlgorithm
   int validity
 }
 AUDIT_EVENT {
   string id
   datetime timestamp
   string event
   string actor
   string target
   string details
 }
```

The frontend seed contains hundreds of synthetic certificate and audit records to exercise filtering, expiry, approval and monitoring workflows without using real organizational data.
