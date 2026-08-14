<!--
---
# Metadata
title: "Cybersecurity Fundamentals"
description: "Encryption, TLS, OWASP, secure coding, SDL"
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
tags: [cybersecurity, coding-and-technology]
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
# Cybersecurity Fundamentals

Security is a discipline that must be integrated into every layer of a system from the outset, rather than added as an afterthought. Whether building a web application, managing infrastructure, or shipping an API, understanding the threat landscape and the fundamentals of defence is essential.

---

## Encryption and Cryptography

### Symmetric vs Asymmetric Encryption

| Type | How It Works | Speed | Key Distribution | Examples |
|------|-------------|-------|-----------------|----------|
| **Symmetric** | Same key for encryption and decryption | Fast | Challenge: how to share the key? | AES-256, ChaCha20 |
| **Asymmetric** | Public key encrypts, private key decrypts | Slower | Public key can be shared openly | RSA, ECC (Elliptic Curve) |

In practice, most systems use **both**: asymmetric encryption to securely exchange a symmetric key, then symmetric encryption for the bulk of the data. This is how TLS/HTTPS works.

### Hashing

Hashing is a one-way function: it converts input into a fixed-size string. You can't reverse it, but the same input always produces the same output.

| Use Case | Recommended Algorithm | Avoid |
|----------|----------------------|-------|
| **Password storage** | Argon2id, bcrypt, scrypt | MD5, SHA-1, plain SHA-256 (too fast) |
| **Data integrity** | SHA-256, SHA-3 | MD5 (broken), SHA-1 (broken) |
| **Digital signatures** | Ed25519, RSA-2048+ | DSA |

### TLS/HTTPS

HTTPS is HTTP over TLS (Transport Layer Security). It provides:
- **Encryption**: Data in transit can't be read by eavesdroppers.
- **Authentication**: The server proves its identity via a certificate.
- **Integrity**: Data can't be modified in transit without detection.

Use TLS 1.2 or 1.3. Disable TLS 1.0 and 1.1. Enable HSTS (HTTP Strict Transport Security) to force browsers to always use HTTPS.

---

## Authentication and Authorisation

### Authentication: Who Are You?

| Method | Security Level | Use Case |
|--------|---------------|----------|
| **Password** | Low–Medium | Basic accounts (enforce 12+ chars, check for breaches) |
| **MFA (TOTP)** | High | Standard for sensitive accounts (Google Authenticator, Authy) |
| **Hardware key (FIDO2/WebAuthn)** | Very High | High-security accounts (YubiKey) |
| **Biometric** | Medium–High | Device unlock (fingerprint, face) — not great as sole factor |
| **OAuth2 / OIDC** | High | Third-party login ("Sign in with Google") |

**Password rules**: enforce minimum length (12–16 characters), check against breached password lists, use Argon2id or bcrypt for hashing with per-user salts.

### Authorisation: What Can You Do?

| Model | Description | Example |
|-------|-------------|---------|
| **RBAC** (Role-Based Access Control) | Permissions assigned to roles; users get roles | Admin, Editor, Viewer |
| **ABAC** (Attribute-Based) | Rules based on user attributes, resource, environment | "Managers can approve their team's requests" |
| **ACL** (Access Control List) | Explicit permissions per user/resource | File permissions (read/write/execute) |

**Principle of least privilege**: give every user, service, and process only the minimum access they need.

### JWT (JSON Web Tokens)

| Aspect | Recommendation |
|--------|---------------|
| **Signing** | RS256 or ES256 (asymmetric) preferred; HS256 acceptable with managed secrets |
| **Expiration** | 15–60 minutes for access tokens; use refresh tokens for longer sessions |
| **Storage** | HTTP-only cookies (not localStorage — vulnerable to XSS) |
| **Validation** | Always verify signature, issuer, audience, and expiration |

---

## OWASP Top 10 (2021)

The OWASP Top 10 is the standard awareness document for web application security. It represents the most critical risks:

| # | Risk | What It Means |
|---|------|--------------|
| 1 | **Broken Access Control** | Users can access resources they shouldn't |
| 2 | **Cryptographic Failures** | Weak or missing encryption for sensitive data |
| 3 | **Injection** | SQL, NoSQL, OS command, or LDAP injection |
| 4 | **Insecure Design** | Architectural flaws that can't be fixed with implementation |
| 5 | **Security Misconfiguration** | Default passwords, open ports, verbose error messages |
| 6 | **Vulnerable Components** | Known CVEs in dependencies |
| 7 | **Auth Failures** | Weak passwords, session mismanagement |
| 8 | **Integrity Failures** | Supply chain attacks, unsigned updates |
| 9 | **Logging/Monitoring Failures** | No detection of breaches |
| 10 | **SSRF** | Server tricked into making requests to internal systems |

---

## Secure Coding Practices

### Input Validation

| Rule | Why |
|------|-----|
| **Whitelist > Blacklist** | Define what's allowed, not what's blocked |
| **Parameterised queries** | Never concatenate user input into SQL — use prepared statements or ORM |
| **HTML encoding** | Encode `<`, `>`, `&`, `"`, `'` to prevent XSS |
| **Shell escaping** | Avoid building shell commands from user input; use `shlex.quote()` |
| **Length limits** | Enforce maximum lengths to prevent buffer overflows and DoS |
| **Type checking** | Ensure integers are integers, booleans are booleans |

### Common Vulnerabilities

| Vulnerability | Attack | Defence |
|--------------|--------|---------|
| **SQL Injection** | `' OR 1=1 --` in login form | Parameterised queries |
| **XSS** | `<script>alert('hacked')</script>` in comment field | Output encoding, Content Security Policy |
| **CSRF** | Trick user's browser into making unauthorised request | CSRF tokens, SameSite cookies |
| **Path Traversal** | `../../etc/passwd` in file parameter | Validate and sanitise file paths |
| **IDOR** | Change `/user/123` to `/user/124` to see someone else's data | Authorisation checks on every request |

---

## Network Security

### Firewalls

| Type | Description |
|------|-------------|
| **Packet-filtering** | Rules based on IP, port, protocol |
| **Stateful** | Tracks connection states; more intelligent filtering |
| **Application-level (WAF)** | Inspects HTTP traffic; blocks SQL injection, XSS, etc. |
| **Cloud security groups** | Virtual firewalls for cloud instances (AWS SGs, Azure NSGs) |

**Rule of thumb**: block all inbound traffic by default; only open what's explicitly needed (80, 443 for web).

### Network Segmentation

Place databases and caches in private subnets with no direct internet access. Use a DMZ for public-facing services (web servers, load balancers). Apply the principle of least privilege to network access.

---

## Secrets Management

### The Golden Rule

**Never hardcode secrets.** No API keys, passwords, or database URLs in source code. No secrets in environment variables committed to Git. No secrets in Docker images.

### Tools

| Tool | Type | Best For |
|------|------|----------|
| **HashiCorp Vault** | Enterprise secrets manager | Dynamic secrets, encryption as a service |
| **AWS Secrets Manager** | Cloud-native | AWS environments |
| **Azure Key Vault** | Cloud-native | Azure environments |
| **SOPS** | Encrypted files | Encrypt secrets in Git (with KMS or GPG) |
| **Docker Secrets** | Container-native | Docker Swarm (for K8s, consider Secrets Store CSI) |
| **dotenv (.env)** | Local development | Development only — never in production or committed |

### Rotation

Rotate secrets regularly and automatically. If a secret is leaked (e.g., committed to a public repo), rotate it immediately — even if you think nobody saw it.

---

## Dependency Security

Your application is only as secure as its weakest dependency.

### Scanning Tools

| Language | Tools |
|----------|-------|
| **Python** | `safety`, `pip-audit`, `bandit` |
| **Node.js** | `npm audit`, `yarn audit`, `snyk` |
| **Rust** | `cargo audit` |
| **Go** | `govulncheck` |
| **General** | `Dependabot` (GitHub), `Renovate`, `Trivy` |

### Supply Chain Integrity

- Use lockfiles (`package-lock.json`, `Cargo.lock`, `go.sum`) for reproducible builds.
- Verify checksums of downloaded dependencies.
- Prefer official registries and verified publishers.
- Automate minor/patch updates via Dependabot or Renovate.

---

## Security Development Lifecycle (SDL)

| Phase | Activity |
|-------|----------|
| **Training** | Ensure developers understand common vulnerabilities |
| **Threat Modelling** | Identify potential threats during design |
| **Secure Coding Standards** | Enforce via linters and code review checklists |
| **SAST** | Static analysis of source code (SonarQube, CodeQL) |
| **DAST** | Dynamic analysis of running application (OWASP ZAP, Burp Suite) |
| **SCA** | Software composition analysis — scan dependencies |
| **Penetration Testing** | Regular ethical hacking exercises |
| **Bug Bounty** | Encourage external researchers to find vulnerabilities |
| **Incident Response Plan** | Have a clear plan for when a breach is detected |

---

## Emergency Checklist

When you suspect a breach:

1. **Don't panic** — but act quickly.
2. **Isolate** affected systems (disconnect from network if needed).
3. **Preserve evidence**: capture logs, memory dumps, disk images.
4. **Identify scope**: which systems, which data?
5. **Rotate** all compromised credentials and secrets.
6. **Patch** the vulnerability.
7. **Notify** affected users and regulators if required (within legal timeframes).
8. **Post-mortem**: document root cause and action items within 24–48 hours.
