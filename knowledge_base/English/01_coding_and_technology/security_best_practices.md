<!--
---
# Metadata
title: "Security Best Practices"
description: "OWASP Top 10, input validation, auth, secrets management"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [security, best, practices, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Security Best Practices

A practical guide to securing applications, infrastructure, and data — from development to production.

---

## OWASP Top 10 (2021) — Overview

1. **Broken Access Control**: Users can access resources they shouldn't.
2. **Cryptographic Failures**: Weak or missing encryption.
3. **Injection**: SQL, NoSQL, OS command, or LDAP injection.
4. **Insecure Design**: Architectural flaws.
5. **Security Misconfiguration**: Default passwords, open ports, verbose errors.
6. **Vulnerable and Outdated Components**: Known CVEs in dependencies.
7. **Identification and Authentication Failures**: Weak passwords, session mismanagement.
8. **Software and Data Integrity Failures**: Supply chain attacks, unsigned updates.
9. **Security Logging and Monitoring Failures**: No detection of breaches.
10. **Server-Side Request Forgery (SSRF)**: Abuse of server to make requests to internal systems.

---

## Input Validation and Output Encoding

### Validation Rules
- **Whitelist > Blacklist**: Define allowed patterns (e.g., regex for email) rather than blocking known bad patterns.
- **Length limits**: Enforce maximum lengths to prevent buffer overflows and DoS.
- **Type checking**: Ensure integers are integers, booleans are booleans.
- **Use well-tested libraries**: For email, URL, and date validation, use standard libraries (e.g., `email-validator` in Python, `validator.js` in Node).

### Output Encoding
- **HTML encoding**: Encode `<`, `>`, `&`, `"`, `'` to prevent XSS.
- **SQL parameterisation**: Never concatenate user input into SQL queries. Use parameterised queries (prepared statements) or an ORM.
- **Shell escaping**: Avoid building shell commands from user input; if unavoidable, use `shlex.quote()` or similar.

---

## Authentication and Authorisation

### Password Management
- **Hashing**: Store passwords with a strong, slow hashing algorithm: **Argon2id** (preferred), **bcrypt**, **scrypt**, or **PBKDF2**.
- **Salting**: Add a unique per-user salt.
- **Minimum length**: Enforce at least 12–16 characters.
- **MFA (Multi-Factor Authentication)**: Require a second factor (TOTP, SMS, hardware key) for sensitive operations.
- **Rate limiting**: Prevent brute-force attempts on login endpoints (e.g., 5 attempts per 5 minutes per IP/user).

### Session Management
- Use secure, HTTP-only, SameSite cookies for session tokens.
- Set appropriate expiration times.
- Invalidate sessions on logout and on password change.
- Avoid exposing session IDs in URLs.

### OAuth2 / OIDC
- Use well-established libraries (e.g., Authlib, PyJWT, Passport.js, Spring Security).
- Validate ID tokens thoroughly (signature, issuer, audience, expiration).
- Use state parameters to prevent CSRF.
- Keep client secrets confidential.

### JWT (JSON Web Tokens)
- **Sign**: Use RS256 or ES256 (asymmetric) for better security; HS256 (symmetric) is acceptable if shared secrets are managed well.
- **Validate**: Always verify signature, issuer (`iss`), audience (`aud`), and expiration (`exp`).
- **Keep short expiration**: 15–60 minutes for access tokens; use refresh tokens for longer sessions.
- **Store securely**: Never store JWTs in localStorage (vulnerable to XSS); use HTTP-only cookies instead.

---

## API Security

### Authentication
- Always authenticate API calls (except public endpoints).
- Prefer API keys or OAuth2 tokens over basic auth (which sends credentials on every request).

### Rate Limiting and Throttling
- Apply per-user and per-IP rate limits to prevent abuse and DoS.
- Return `429 Too Many Requests` with a `Retry-After` header.

### CORS (Cross-Origin Resource Sharing)
- Allow only specific origins (never `*` in production).
- Validate `Origin` header on the server side.

### Input Validation
- Validate all request parameters, including headers and body.
- Reject unexpected fields (`"strict": true` or `additionalProperties: false` in JSON Schema).

### HTTPS / TLS
- Enforce HTTPS in production.
- Use HSTS (HTTP Strict Transport Security) to force browsers to use HTTPS.
- Use TLS 1.2 or 1.3 (disable TLS 1.0/1.1).

---

## Secrets Management

### Never Hardcode Secrets
- Do not commit secrets (API keys, passwords, database URLs) to source control.
- Use environment variables or secret management tools.

### Tools

| Tool | Description |
|------|-------------|
| **HashiCorp Vault** | Enterprise-grade, dynamic secrets |
| **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager** | Cloud-native |
| **SOPS** | Encrypt secrets in files and commit them (with KMS or GPG) |
| **Docker secrets** | For Swarm mode; Kubernetes secrets (consider external Secrets Store CSI driver) |

### Rotation
- Regularly rotate secrets and service accounts.
- Automate rotation where possible.

---

## Dependency Management

### Vulnerability Scanning

| Language/Platform | Tools |
|-------------------|-------|
| **Python** | `safety`, `pip-audit`, `bandit` |
| **Node** | `npm audit`, `yarn audit`, `snyk` |
| **Rust** | `cargo audit` |
| **Go** | `govulncheck` |
| **General** | `Dependabot` (GitHub), `Renovate`, `Trivy` |

### Patching
- Keep dependencies updated to patched versions.
- Set up automated pull requests for minor/patch updates.
- Review changelogs for breaking changes.

### Supply Chain Integrity
- Use package lockfiles (`package-lock.json`, `Cargo.lock`, `go.sum`) to ensure reproducible builds.
- Verify checksums of downloaded dependencies.
- Prefer official registries and trust only verified publishers.

---

## Infrastructure Security

### Firewalls
- Block all inbound ports except those explicitly needed (e.g., 80, 443).
- Limit SSH access to specific IP ranges (or use a VPN/bastion host).
- Use security groups (AWS) or NSGs (Azure) for fine-grained control.

### OS Hardening
- Apply security updates regularly (`sudo apt upgrade`, `yum update`).
- Disable unnecessary services and default accounts.
- Use fail2ban to block brute-force attempts on SSH.
- Harden SSH: disable root login, use key-based auth, change default port (optional).

### Network Segmentation
- Place databases and caches in private subnets with no internet access.
- Use a DMZ for public-facing services.
- Apply the principle of least privilege to network access.

### Secrets in Infrastructure
- Never store secrets in CI/CD environment variables unless encrypted.
- Use the cloud provider's IAM roles for EC2/VM instances instead of long-lived keys.

---

## Logging and Monitoring

### What to Log
- Authentication events (success/failure).
- Access control decisions (authorisation failures).
- Admin actions (user creation, deletion, permission changes).
- Database schema changes.
- System errors and exceptions.
- API requests and responses (redact sensitive data).

### What Not to Log
- Passwords, secrets, tokens, PII (Personal Identifiable Information) unless hashed/redacted.
- Full credit card numbers.

### Alerting
- Set up alerts for:
  - Multiple failed logins (potential brute force).
  - Unusual access patterns (e.g., from new locations, at odd hours).
  - New admin accounts created.
  - High error rates or latency spikes.
- Use a SIEM (Security Information and Event Management) for advanced correlation.

### Log Retention
- Retain logs for at least 30–90 days depending on regulatory requirements.
- Store logs in a centralised, tamper-evident system (e.g., ELK Stack, Splunk, Datadog).

---

## Secure Development Lifecycle (SDL)

1. **Training**: Ensure developers understand common vulnerabilities.
2. **Threat modelling**: Identify potential threats early in design.
3. **Secure coding standards**: Enforce via linters and code review checklists.
4. **SAST** (Static Application Security Testing): Scan source code for vulnerabilities (SonarQube, CodeQL).
5. **DAST** (Dynamic Application Security Testing): Scan running applications (OWASP ZAP, Burp Suite).
6. **SCA** (Software Composition Analysis): Scan dependencies.
7. **Penetration testing**: Regular ethical hacking exercises.
8. **Bug bounty**: Encourage external researchers to find vulnerabilities responsibly.
9. **Incident response plan**: Have a clear plan for when a breach is detected.

---

## Emergency Checklist (When a Breach is Suspected)

1. **Do not panic** — but act quickly.
2. **Isolate** the affected systems (disconnect from network if needed).
3. **Preserve evidence**: Capture logs, memory dumps, and disk images.
4. **Identify** the scope: which systems, which data.
5. **Rotate** all compromised credentials and secrets.
6. **Patch** the vulnerability.
7. **Notify** affected users and regulatory bodies if required (within legal timeframes).
8. **Conduct a post-mortem** to understand root cause and improve processes.
