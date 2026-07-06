# Contradictory Sources

Contradictory sources occur when different references provide conflicting information about the same topic. This is a common challenge in research, development, and AI-assisted work. Learning to identify, evaluate, and resolve contradictions is essential for making sound decisions.

---

## Types of Contradictions

### Factual Contradictions

Direct conflicts about verifiable facts.

**Example:**
- Source A: "Python 3.10 was released on October 4, 2021."
- Source B: "Python 3.10 was released on September 15, 2021."

**Resolution:** Check official release records (python.org). Source A is correct.

---

### Recommendation Contradictions

Different sources recommend opposing approaches.

**Example:**
- Source A: "Use singleton pattern for database connections."
- Source B: "Avoid singleton pattern; use dependency injection instead."

**Resolution:** Both can be valid in different contexts. Evaluate based on your specific requirements.

---

### Version Contradictions

Information differs based on version or timeframe.

**Example:**
- Documentation v1: "The `asyncio.get_event_loop()` function returns the current event loop."
- Documentation v2: "`asyncio.get_event_loop()` is deprecated. Use `asyncio.get_running_loop()` instead."

**Resolution:** Check version dates and use the most recent authoritative source.

---

### Expert Disagreements

Qualified experts hold different opinions.

**Example:**
- Expert A: "Microservices are essential for scalable architecture."
- Expert B: "Start with a monolith; microservices add unnecessary complexity."

**Resolution:** Both perspectives have merit. Consider team size, domain complexity, and organizational maturity.

---

## Common Causes of Contradictions

| Cause | Description | Example |
|-------|-------------|---------|
| Outdated information | One source is no longer current | Old tutorial vs. current documentation |
| Different contexts | Advice applies to different situations | "Use caching" for read-heavy vs. write-heavy workloads |
| Varying expertise | Author knowledge levels differ | Blog post vs. peer-reviewed paper |
| Regional differences | Practices vary by location | GDPR compliance advice differs by region |
| Commercial bias | Vendor-specific recommendations | AWS recommends their services over alternatives |
| Evolving standards | Best practices change over time | Security recommendations evolve |

---

## Evaluating Conflicting Sources

### Source Credibility Assessment

```markdown
## Source Evaluation Checklist

### Authority
- [ ] Is the author qualified in this domain?
- [ ] What are their credentials?
- [ ] Do they have practical experience?

### Recency
- [ ] When was this published?
- [ ] Has the field changed since then?
- [ ] Is there a more recent update?

### Evidence
- [ ] Are claims supported by data?
- [ ] Can results be reproduced?
- [ ] Are methodologies transparent?

### Consensus
- [ ] Do other experts agree?
- [ ] Is this the prevailing view?
- [ ] Are dissenting views addressed?

### Bias
- [ ] Is there a commercial interest?
- [ ] Is the tone balanced or promotional?
- [ ] Are limitations acknowledged?
```

---

### Information Hierarchy

When sources conflict, prioritize in this order:

1. **Official documentation** - From the creators/maintainers
2. **Peer-reviewed research** - Vetted by experts
3. **Established industry standards** - Widely adopted practices
4. **Expert consensus** - Agreement among qualified practitioners
5. **Individual expert opinion** - Single authority perspective
6. **Community discussions** - Forums, social media
7. **Unverified claims** - Anonymous or unattributed sources

---

## Resolution Strategies

### Triangulation

Consult multiple independent sources to find consensus.

**Process:**
1. Gather 3-5 authoritative sources
2. Identify points of agreement
3. Note where disagreements occur
4. Weight sources by credibility
5. Make informed decision based on preponderance of evidence

**Example:**
```
Question: "What's the recommended password hashing algorithm?"

Sources consulted:
- OWASP guidelines → Argon2id
- NIST recommendations → Argon2, bcrypt, scrypt
- Python security best practices → bcrypt or argon2-cffi
- Django documentation → PBKDF2 (default), supports others

Consensus: Argon2id is preferred, bcrypt is acceptable alternative
```

---

### Context Analysis

Determine if contradictions arise from different contexts.

**Questions to Ask:**
- What assumptions does each source make?
- What constraints are they addressing?
- Who is the intended audience?
- What problem is each trying to solve?

**Example:**
```
Contradiction:
- "Use global variables for configuration" (Source A)
- "Never use global variables" (Source B)

Context Analysis:
- Source A: Small scripts, simple configuration
- Source B: Large applications, concurrent systems

Resolution: Both correct in their contexts. For small scripts, globals are fine. 
For large applications, use proper configuration management.
```

---

### Temporal Resolution

Check if one source is outdated.

**Steps:**
1. Note publication dates
2. Check for version changes
3. Look for deprecation notices
4. Verify against current releases

**Example:**
```
Contradiction about Flask routing:

Source A (2018): "@app.route('/user/<id>')"
Source B (2023): "@app.route('/user/<int:id>')"

Resolution: Source B reflects newer Flask conventions with type converters.
Both work, but Source B is more explicit and current.
```

---

## Documenting Contradictions

### Decision Records

When you encounter and resolve contradictions, document the decision.

```markdown
## Architecture Decision Record: Database Choice

**Date:** 2024-01-15
**Status:** Decided

### Question
Should we use PostgreSQL or MongoDB for user session storage?

### Conflicting Sources
- Team member A recommends PostgreSQL (ACID compliance)
- Team member B recommends MongoDB (flexible schema, fast writes)
- Industry blogs show both approaches

### Analysis
| Criteria | PostgreSQL | MongoDB |
|----------|------------|---------|
| ACID compliance | Yes | Limited |
| Write throughput | Good | Excellent |
| Query flexibility | High | High |
| Team expertise | Strong | Limited |
| Operational complexity | Known | Unknown |

### Decision
Use PostgreSQL because:
1. Team has existing expertise
2. ACID compliance important for sessions
3. Write throughput sufficient for our scale

### Notes
Revisit if write volume increases 10x or requirements change.
```

---

### Uncertainty Acknowledgment

When contradictions can't be fully resolved, acknowledge uncertainty.

**Example:**
```markdown
## Implementation Note: Caching Strategy

There's disagreement in the community about cache invalidation strategy:

**Option A (TTL-based):** Simpler, may serve stale data
**Option B (Event-based):** More complex, always fresh

We're implementing Option A initially because:
- Faster to implement
- Stale data acceptable for our use case (5-minute TTL)
- Can upgrade to Option B later if needed

**Confidence Level:** Medium
**Review Date:** After 3 months of production use
```

---

## Handling AI-Generated Contradictions

### When AI Provides Conflicting Information

**Scenario:**
```
Query 1: "What's the best Python web framework?"
Response 1: "Django is best for most use cases due to batteries-included approach."

Query 2: "Compare Django and Flask"
Response 2: "Flask is better for microservices and simple APIs."
```

**Analysis:**
- Not truly contradictory - different contexts
- Response 1: General purpose applications
- Response 2: Microservices specifically

**Best Practice:**
Ask clarifying questions to get consistent, contextualized answers.

---

### Verifying AI Output Against External Sources

```python
def verify_ai_response(ai_response, trusted_sources):
    """Cross-check AI output against authoritative sources."""
    claims = extract_claims(ai_response)
    verification_results = []
    
    for claim in claims:
        source_matches = []
        for source in trusted_sources:
            match = source.verify(claim)
            source_matches.append(match)
        
        if all(source_matches):
            verification_results.append({"claim": claim, "status": "verified"})
        elif any(source_matches):
            verification_results.append({"claim": claim, "status": "disputed"})
        else:
            verification_results.append({"claim": claim, "status": "unverified"})
    
    return verification_results
```

---

## Related Documents

- [[hallucinations]] - AI-generated false information
- [[misinformation]] - False or misleading information
- [[logical_fallacies]] - Errors in reasoning
- [[confirmation_bias]] - Seeking confirming information
