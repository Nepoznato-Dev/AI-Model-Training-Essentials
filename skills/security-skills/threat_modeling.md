---
# Metadata
title: "Threat Modeling"
description: "A structured process for identifying, prioritizing, and mitigating security threats in systems and AI applications."
category: "Security Skills"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-01-15"
    author: "AI Model Training Team"
    changes: "Initial skill creation"

# Review
created: "2026-01-15"
last_modified: "2026-01-15"
review_date: "2026-07-15"
reviewed_by: "Security Skills Team"
next_review: "2027-01-15"

# Classification
tags: [threat-modeling, security, stride, risk-assessment, ai-security]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "12 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Threat Modeling

## Overview

Threat modeling is a structured process for identifying, prioritizing, and mitigating security threats in systems and applications. For AI systems, it addresses unique challenges like data poisoning, model inversion, and adversarial attacks.

This skill provides a systematic approach to threat modeling using industry-standard frameworks like STRIDE and DREAD, with specific guidance for AI/ML applications.

## Core Competencies

- **STRIDE Analysis**: Identifying threats using Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege
- **DREAD Rating**: Prioritizing risks based on Damage, Reproducibility, Exploitability, Affected Users, Discoverability
- **Data Flow Mapping**: Charting trust boundaries and data flows across system components
- **AI-Specific Threat Assessment**: Evaluating data poisoning, model extraction, adversarial examples, and prompt injection
- **Mitigation Planning**: Designing and documenting countermeasures with ownership and timelines
- **Compliance Alignment**: Mapping threats to GDPR, HIPAA, SOC 2, and EU AI Act requirements

## STRIDE Framework for AI

### Spoofing
- **Threat**: Attacker impersonates legitimate user or system
- **AI Context**: Fake API clients, stolen credentials for model access
- **Mitigations**: 
  - Multi-factor authentication
  - API key rotation
  - Rate limiting per user

### Tampering
- **Threat**: Unauthorized modification of data or models
- **AI Context**: Training data corruption, model weight manipulation
- **Mitigations**:
  - Data integrity checks (hashes, signatures)
  - Model versioning and signing
  - Access controls on training pipelines

### Repudiation
- **Threat**: Users deny performing actions
- **AI Context**: Denying model queries, data access
- **Mitigations**:
  - Comprehensive audit logging
  - Immutable logs (blockchain, write-once storage)
  - User activity tracking

### Information Disclosure
- **Threat**: Unauthorized access to sensitive information
- **AI Context**: Training data leakage, model inversion attacks
- **Mitigations**:
  - Differential privacy in training
  - Output filtering and sanitization
  - Query rate limits to prevent reconstruction

### Denial of Service
- **Threat**: Disrupting service availability
- **AI Context**: Resource exhaustion through expensive queries
- **Mitigations**:
  - Query complexity limits
  - Resource quotas per user
  - Auto-scaling infrastructure

### Elevation of Privilege
- **Threat**: Gaining unauthorized access levels
- **AI Context**: Prompt injection to bypass restrictions
- **Mitigations**:
  - Input validation and sanitization
  - Role-based access control
  - Principle of least privilege

## Threat Modeling Process

### Step 1: Define the System
```
Components:
- Data collection pipeline
- Training infrastructure
- Model serving API
- User interface
- Storage systems

Trust Boundaries:
- Public internet ↔ Load balancer
- Load balancer ↔ Application
- Application ↔ Database
- Internal network ↔ External APIs
```

### Step 2: Create Data Flow Diagrams

```
[User] → [API Gateway] → [Model Server] → [Database]
    ↓         ↓              ↓               ↓
  Auth     Rate Limit    Inference       Storage
  Check    Enforcement   Validation      Encryption
```

### Step 3: Identify Threats

For each component, ask:
- What can go wrong?
- What are we trying to protect?
- Who might attack this and why?

### Step 4: Rate Threats (DREAD)

- **Damage Potential**: How bad would a successful attack be? (1-10)
- **Reproducibility**: How easy is it to reproduce the attack? (1-10)
- **Exploitability**: How much work to exploit? (1-10)
- **Affected Users**: How many users impacted? (1-10)
- **Discoverability**: How easy to discover the vulnerability? (1-10)

**Risk Score** = (D + R + E + A + D) / 5

### Step 5: Define Countermeasures

For each high-risk threat:
1. Describe the mitigation
2. Assign ownership
3. Set priority and timeline
4. Define success criteria

## AI-Specific Threat Scenarios

### Scenario 1: Data Poisoning Attack
- **Attack**: Adversary injects malicious samples into training data
- **Impact**: Model learns incorrect patterns or backdoors
- **Detection**: Anomaly detection in training data, validation set monitoring
- **Prevention**: Data source verification, outlier detection, robust training

### Scenario 2: Model Extraction
- **Attack**: Query model repeatedly to reconstruct its functionality
- **Impact**: Loss of intellectual property, competitive disadvantage
- **Detection**: Monitor query patterns, detect systematic probing
- **Prevention**: Rate limiting, output perturbation, watermarking

### Scenario 3: Adversarial Examples
- **Attack**: Craft inputs that cause misclassification
- **Impact**: Safety issues, reliability concerns
- **Detection**: Adversarial detection models, input validation
- **Prevention**: Adversarial training, defensive distillation

### Scenario 4: Prompt Injection (LLMs)
- **Attack**: Craft prompts to bypass safety filters
- **Impact**: Harmful outputs, data leakage, policy violations
- **Detection**: Input/output filtering, pattern matching
- **Prevention**: Prompt hardening, instruction hierarchy, sandboxing

## Tools and Resources

### Threat Modeling Tools
- Microsoft Threat Modeling Tool
- OWASP Threat Dragon
- IriusRisk
- PyTM (Python Threat Modeling)

### AI Security Resources
- OWASP Top 10 for LLM Applications
- MITRE ATLAS (Adversarial Threat Landscape for AI Systems)
- NIST AI Risk Management Framework
- Partnership on AI guidelines

## Documentation Template

```markdown
## Threat: [Name]

**STRIDE Category**: [Category]
**DREAD Score**: [Score]/50

### Description
[Brief description of the threat]

### Attack Vector
[How could this be exploited?]

### Impact
[What would be the consequences?]

### Likelihood
[How probable is this attack?]

### Mitigations
1. [Countermeasure 1]
2. [Countermeasure 2]

### Status
[ ] Open
[ ] In Progress
[ ] Mitigated
[ ] Accepted Risk

### Owner
[Team/Person responsible]

### Target Date
[YYYY-MM-DD]
```

## Best Practices

1. **Start Early**: Begin threat modeling during design phase
2. **Iterate**: Update as system evolves
3. **Involve Team**: Include developers, security, and stakeholders
4. **Focus on High-Risk**: Prioritize based on impact and likelihood
5. **Document Everything**: Maintain living threat model document
6. **Test Mitigations**: Verify countermeasures work as expected
7. **Stay Updated**: Follow AI security research and new threats

## Compliance Considerations

- **GDPR**: Data protection and privacy by design
- **HIPAA**: Healthcare data security requirements
- **SOC 2**: Security controls and auditing
- **EU AI Act**: Risk management for AI systems

## Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Skipping threat modeling | Vulnerabilities discovered late, costly fixes | Integrate into design phase |
| Focusing only on known threats | Missing novel AI-specific attacks | Use STRIDE systematically |
| Not updating the threat model | Stale documentation, missed risks | Review quarterly and after changes |
| Over-relying on automated tools | Missing business logic threats | Combine tools with manual analysis |
| Ignoring supply chain threats | Third-party component vulnerabilities | Map all dependencies and data flows |

## Best Practices

1. **Start Early**: Begin threat modeling during design phase, not after deployment
2. **Iterate**: Update the threat model as the system evolves and new threats emerge
3. **Involve the Team**: Include developers, security engineers, and stakeholders
4. **Focus on High-Risk**: Prioritize based on DREAD scores and business impact
5. **Document Everything**: Maintain a living threat model document accessible to the team
6. **Test Mitigations**: Verify countermeasures work as expected through penetration testing
7. **Stay Updated**: Follow AI security research and emerging threat landscapes

## Tools & Resources

- **Microsoft Threat Modeling Tool** - Free threat identification for system designs
- **OWASP Threat Dragon** - Open-source threat modeling with STRIDE support
- **IriusRisk** - Automated threat modeling platform
- **PyTM** (Python Threat Modeling) - Code-based threat modeling
- **OWASP Top 10 for LLM Applications** - [owasp.org/Top-10-for-LLM-Apps](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- **MITRE ATLAS** - Adversarial Threat Landscape for AI Systems
- **NIST AI Risk Management Framework** - [nist.gov/ai](https://www.nist.gov/artificial-intelligence)

## Example Application

**Scenario:** Building an AI-powered customer support chatbot

**Application:**
1. **Define System**: API gateway → LLM server → Knowledge base → User interface
2. **Identify Threats**: Prompt injection (STRIDE: Elevation of Privilege), Training data leakage (Information Disclosure), Model extraction via repeated queries (DoS)
3. **Rate with DREAD**: Prompt injection scores 42/50 (critical), Data leakage scores 35/50 (high)
4. **Define Countermeasures**: Input sanitization, output filtering, rate limiting, differential privacy
5. **Assign Ownership**: Security team owns prompt injection mitigation, ML team owns data leakage prevention

**Outcome:** Threat model document with prioritized mitigations, clear ownership, and a review cadence aligned with release cycles.

## Success Indicators

You've mastered threat modeling when you can:

- ✅ Systematically identify threats using STRIDE for any system architecture
- ✅ Accurately rate risks using DREAD and prioritize mitigations
- ✅ Create comprehensive data flow diagrams with trust boundaries
- ✅ Address AI-specific threats (poisoning, extraction, adversarial examples)
- ✅ Maintain a living threat model that evolves with the system
- ✅ Align threat mitigations with compliance requirements
- ✅ Conduct threat modeling workshops with cross-functional teams

## Related Skills

- [Secure Coding](secure_coding.md) - Implementing security at the code level
- [Authentication & Authorization](authentication_authorization.md) - Access control mechanisms
- [System Architecture](../designing-skills/system_architecture.md) - Designing secure system boundaries

## Version Information

---
version: 1.0.0
last_updated: 2026-01-15
reviewed_by: Security Skills Team
next_review: 2026-07-15
---
