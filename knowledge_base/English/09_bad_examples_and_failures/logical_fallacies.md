# Logical Fallacies

Logical fallacies are errors in reasoning that undermine the validity of an argument. AI models can produce outputs containing logical fallacies, and users may also make fallacious requests. Understanding these helps identify flawed reasoning.

---

## Common Logical Fallacies in AI Contexts

### Ad Hominem (Attack Against the Person)

Attacking the person making an argument rather than the argument itself.

**Bad Example:**
> "This code review is wrong because the reviewer is a junior developer."

**Why It's Bad:** The validity of feedback depends on its content, not the reviewer's seniority.

---

### Appeal to Authority

Claiming something is true because an authority figure says so, without evidence.

**Bad Example:**
> "This architecture must be correct because Google uses it."

**Why It's Bad:** What works for Google at their scale may not work for your use case. Context matters.

---

### False Dichotomy (Black-and-White Thinking)

Presenting only two options when more exist.

**Bad Example:**
> "We must either rewrite everything from scratch or live with this technical debt forever."

**Better Approach:** Consider incremental refactoring, targeted improvements, or hybrid solutions.

---

### Slippery Slope

Arguing that one event will inevitably lead to extreme consequences without evidence.

**Bad Example:**
> "If we allow this small shortcut in the code, soon the entire codebase will be unmaintainable."

**Why It's Bad:** Small compromises don't necessarily cascade into disaster with proper governance.

---

### Circular Reasoning (Begging the Question)

The conclusion is assumed in the premise.

**Bad Example:**
> "This framework is the best choice because it's superior to all alternatives."

**Why It's Bad:** No actual evidence is provided; the claim just restates itself.

---

### Hasty Generalization

Drawing broad conclusions from insufficient evidence.

**Bad Example:**
> "I tried one microservice framework and it was complicated. All microservice frameworks are overly complex."

**Why It's Bad:** One experience doesn't represent the entire category.

---

### Post Hoc Ergo Propter Hoc (False Cause)

Assuming that because B followed A, A caused B.

**Bad Example:**
> "We deployed the new feature and then saw increased latency. The new feature caused the latency."

**Why It's Bad:** Correlation doesn't imply causation. Other factors (traffic spike, infrastructure issues) could be responsible.

---

### Appeal to Popularity (Bandwagon Fallacy)

Arguing something is correct because many people believe it.

**Bad Example:**
> "Everyone is using Kubernetes, so we should too."

**Why It's Bad:** Popularity doesn't guarantee suitability for your specific needs.

---

### Straw Man

Misrepresenting someone's argument to make it easier to attack.

**Bad Example:**
> Developer A: "We should add more tests for this module."
> Developer B: "So you want us to spend all day writing tests and never ship features?"

**Why It's Bad:** Developer A didn't say "all day" - this misrepresents their position.

---

### Sunk Cost Fallacy

Continuing a project because of invested resources, not future value.

**Bad Example:**
> "We've already spent 6 months on this approach, we can't switch now."

**Better Approach:** Evaluate based on future costs and benefits, not past investments.

---

### Composition/Division Fallacy

Assuming what's true for parts is true for the whole (or vice versa).

**Bad Example:**
> "Each microservice is fast, so the entire distributed system will be fast."

**Why It's Bad:** System-level performance depends on interactions, network latency, and coordination overhead.

---

## Logical Fallacies in AI Outputs

AI models may produce fallacious reasoning:

| Fallacy | AI Example |
|---------|-----------|
| False Cause | "Users abandoned the app after the redesign, so the redesign caused churn" (ignores seasonality, competitors) |
| Appeal to Authority | "This security practice is correct because it's mentioned in a popular blog" |
| Hasty Generalization | "One user reported a bug, so the feature is broken for everyone" |
| False Dichotomy | "Either we use AI or we can't automate this task" |

---

## How to Avoid Logical Fallacies

### For Critical Thinking

1. **Question assumptions**: What evidence supports this claim?
2. **Consider alternatives**: Are there other explanations or options?
3. **Check causality**: Is there actual causal evidence or just correlation?
4. **Evaluate sources**: Is the authority relevant and credible?
5. **Look for nuance**: Are there middle grounds between extremes?

### For Code Reviews

```markdown
## Review Checklist - Avoiding Fallacies

- [ ] Am I attacking the person or the code?
- [ ] Am I assuming causation from correlation?
- [ ] Am I considering all options or just two extremes?
- [ ] Is my evidence sufficient for the conclusion?
- [ ] Am I influenced by sunk costs?
```

### For Architecture Decisions

```markdown
## Decision Framework

1. What problem are we solving?
2. What evidence supports each option?
3. What are the trade-offs?
4. What would change our minds?
5. How will we measure success?
```

---

## Related Documents

- [[hallucinations]] - AI-generated false information
- [[confirmation_bias]] - Seeking information that confirms existing beliefs
- [[misinformation]] - False or misleading information
- [[contradictory_sources]] - Handling conflicting information
