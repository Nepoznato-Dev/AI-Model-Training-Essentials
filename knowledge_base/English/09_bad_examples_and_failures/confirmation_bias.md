# Confirmation Bias

Confirmation bias is the tendency to search for, interpret, favor, and recall information in a way that confirms one's preexisting beliefs or hypotheses. In software development and AI usage, this can lead to poor decisions and missed issues.

---

## What Is Confirmation Bias?

Confirmation bias causes people to:
- Seek evidence that supports their existing views
- Dismiss or undervalue contradictory evidence
- Interpret ambiguous information as supportive of their position
- Remember confirming instances more vividly than disconfirming ones

---

## Manifestations in Software Development

### Code Review Bias

**Bad Example:**
```markdown
Developer A (senior): "This looks good, nice work!"
Developer B (junior): "This has several potential issues..."

Team accepts Developer A's review without scrutiny but questions Developer B's feedback excessively.
```

**Why It's Bad:** Status influences perception of code quality rather than objective analysis.

---

### Technology Selection

**Bad Example:**
> "I've used React for years and it's great. All these articles about React being complex are outliers. Vue and Angular have way more problems."

**Reality:** The developer is:
- Recalling positive experiences with React
- Dismissing criticism as exceptions
- Attributing problems with other frameworks to inherent flaws

---

### Debugging Tunnel Vision

**Bad Example:**
```python
# Developer assumes the bug is in the new feature
def investigate_issue():
    check_new_feature_code()  # Spend hours here
    # Never check the config file that was also changed
```

**Better Approach:**
```python
def investigate_issue():
    list_all_recent_changes()
    systematically_test_each_hypothesis()
    follow_evidence_wherever_it_leads()
```

---

### Testing Blind Spots

**Bad Example:**
```python
# Only testing happy paths that confirm the code works
def test_payment_processor():
    test_successful_payment()  # ✓
    test_valid_card()  # ✓
    # Missing: invalid cards, network failures, edge cases
```

**Why It's Bad:** Tests confirm expectations rather than challenge assumptions.

---

### AI Prompt Engineering

**Bad Example:**
> User: "Tell me why microservices are better than monoliths."

**Problem:** This prompt invites confirmation of a premise rather than balanced analysis.

**Better Prompt:**
> User: "Compare microservices and monoliths. What are the trade-offs of each? When would you choose one over the other?"

---

## Signs You're Experiencing Confirmation Bias

| Indicator | Example |
|-----------|---------|
| Dismissing contradictory data | "That benchmark must be wrong" |
| Seeking only supporting sources | Reading only positive reviews of your chosen tool |
| Interpreting ambiguity as support | "The documentation doesn't say it won't work, so it probably will" |
| Remembering only successes | "My approach worked last time" (forgetting failures) |
| Getting defensive about criticism | Treating code feedback as personal attack |

---

## How to Counteract Confirmation Bias

### For Individuals

**Seek Disconfirming Evidence:**
> "What would prove my hypothesis wrong?"
> "What assumptions am I making?"

**Consider Alternative Explanations:**
> "What else could explain this behavior?"
> "If I hadn't written this code, what would I think of it?"

**Use Structured Decision-Making:**
```markdown
## Decision Template

**Hypothesis:** [What do I believe?]

**Supporting Evidence:**
- [List evidence FOR]

**Contradictory Evidence:**
- [List evidence AGAINST - force yourself to find some]

**Alternative Hypotheses:**
- [What else could be true?]

**What Would Change My Mind:**
- [Specific conditions]
```

### For Teams

**Blind Code Reviews:**
- Remove author names when possible
- Focus on the code, not who wrote it

**Pre-mortem Analysis:**
> "Imagine this project failed. What went wrong?"

**Devil's Advocate:**
- Assign someone to argue against the proposed solution
- Rotate this role to avoid stigma

**Diverse Perspectives:**
- Include people with different backgrounds and experience levels
- Encourage dissenting opinions

---

## Confirmation Bias in AI Interactions

### How AI Can Reinforce Bias

1. **Echo Chamber Effect**: AI may provide information that aligns with user's query framing
2. **Selective Citation**: Users may only notice sources that confirm their view
3. **Framing Influence**: How you ask determines what answers you get

### Mitigation Strategies

**Ask Balanced Questions:**
```
Bad:  "Why is PostgreSQL better than MySQL?"
Good: "Compare PostgreSQL and MySQL for [specific use case]. What are the strengths and weaknesses of each?"
```

**Request Contrarian Views:**
> "What are the strongest arguments against using this approach?"

**Cross-Reference AI Output:**
- Verify claims with independent sources
- Ask the same question multiple ways to check consistency

---

## Related Documents

- [[logical_fallacies]] - Errors in reasoning
- [[hallucinations]] - AI-generated false information
- [[misinformation]] - False or misleading information
- [[contradictory_sources]] - Handling conflicting information
