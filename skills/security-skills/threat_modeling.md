# Threat Modeling for AI Systems

Systematic approach to identifying and mitigating security threats in AI/ML applications.

## What is Threat Modeling?

Threat modeling is a structured process for:
- Identifying potential security threats
- Prioritizing risks based on impact and likelihood
- Defining countermeasures and mitigations
- Documenting security decisions

## Why Threat Model AI Systems?

AI systems introduce unique security challenges:
- **Data poisoning**: Attackers corrupt training data
- **Model inversion**: Extracting sensitive training data from models
- **Adversarial examples**: Inputs designed to fool models
- **Model stealing**: Unauthorized copying of proprietary models
- **Prompt injection**: Manipulating LLM behavior through crafted inputs

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

---

**Related Documents**:
- [Secure Coding](secure_coding.md)
- [Security Testing](security_testing.md) (coming soon)

**Next Steps**: Apply threat modeling to your AI project using the template above.
