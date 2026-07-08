# Cognitive Biases and Logical Fallacies

This document consolidates cognitive biases, logical fallacies, and reasoning errors that affect both human decision-making and AI system outputs.

---

## Cognitive Biases

Cognitive biases are systematic patterns of deviation from rationality in judgment and decision-making. In software development and AI systems, these can lead to poor design decisions, flawed requirements, and biased model behavior.

### Confirmation Bias

**What It Is:** The tendency to search for, interpret, and recall information in a way that confirms preexisting beliefs.

**Bad Example in Development:**
```python
# Developer believes their algorithm is O(n log n)
def analyze_complexity(code):
    # Only looks for evidence supporting O(n log n)
    sees_divide_and_conquer = True
    sees_recursion = True
    
    # Ignores contradictory evidence
    nested_loop_present = True  # Actually makes it O(n²)
    redundant_computation = True  # Adds extra factor
    
    return "O(n log n)"  # Wrong conclusion
```

**In Code Reviews:**
```markdown
Developer A (senior): "This looks good, nice work!"
Developer B (junior): "This has several potential issues..."

Team accepts Developer A's review without scrutiny but questions Developer B's feedback excessively.
```

**Mitigation:**
- Actively seek disconfirming evidence
- Use blind code reviews
- Encourage dissenting opinions
- Document assumptions explicitly

### Anchoring Bias

**What It Is:** Relying too heavily on the first piece of information encountered.

**Bad Example:**
```markdown
Project Manager: "This feature should take about 2 days."
Developer: (Anchored to 2 days, even though realistic estimate is 5 days)
"Okay, I'll try to finish in 2 days."

Result: Rushed work, technical debt, missed deadlines anyway.
```

**Mitigation:**
- Get multiple independent estimates
- Use planning poker for estimation
- Consider ranges instead of point estimates
- Reference historical data

### Sunk Cost Fallacy

**What It Is:** Continuing an endeavor because of previously invested resources (time, money, effort), even when abandoning would be better.

**Bad Example:**
```markdown
"We've already spent 6 months building this custom framework. 
We can't switch to the industry standard now, even though 
it would save us time in the long run."
```

**Mitigation:**
- Evaluate decisions based on future value, not past investment
- Regularly reassess project viability
- Create psychological safety for pivoting
- Use objective criteria for continue/stop decisions

### Availability Heuristic

**What It Is:** Overestimating the importance of information that is readily available or recent.

**Bad Example:**
```markdown
"I just read about a SQL injection attack, so we should 
prioritize SQL injection prevention over XSS, even though 
our security audit shows XSS is our bigger risk."
```

**Mitigation:**
- Use data-driven decision making
- Consult comprehensive threat models
- Look at base rates and statistics
- Avoid recency bias in prioritization

### Dunning-Kruger Effect

**What It Is:** People with low ability at a task overestimate their ability; experts may underestimate theirs.

**Bad Example:**
```markdown
Junior Developer: "I've completed a Python tutorial. 
I'm ready to architect our entire microservices platform."

Senior Developer: "I've been building distributed systems for 10 years. 
I'm probably missing something important in this design."
```

**Mitigation:**
- Encourage continuous learning
- Implement peer review processes
- Create mentorship programs
- Foster humility and curiosity

---

## Logical Fallacies

Logical fallacies are errors in reasoning that undermine argument validity. AI models can produce outputs containing these fallacies.

### Ad Hominem (Attack Against the Person)

**What It Is:** Attacking the person making an argument rather than the argument itself.

**Bad Example:**
```markdown
"This code review is wrong because the reviewer is a junior developer."
```

**Why It's Bad:** The validity of feedback depends on its content, not the reviewer's seniority.

### Appeal to Authority

**What It Is:** Claiming something is true because an authority figure says so, without evidence.

**Bad Example:**
```markdown
"This architecture must be correct because Google uses it."
```

**Why It's Bad:** What works for Google at their scale may not work for your use case.

### False Dichotomy (Black-and-White Thinking)

**What It Is:** Presenting only two options when more exist.

**Bad Example:**
```markdown
"We either rewrite everything in Rust or accept that our 
codebase will always be slow and buggy."
```

**Reality:** Many options exist between these extremes (optimize hot paths, use Rust for specific components, improve Python code, etc.)

### Slippery Slope

**What It Is:** Arguing that one event will inevitably lead to a chain of negative consequences.

**Bad Example:**
```markdown
"If we allow this small technical debt, soon our entire 
codebase will be unmaintainable and the company will fail."
```

**Why It's Bad:** Assumes inevitable progression without evidence; ignores mitigating factors.

### Circular Reasoning

**What It Is:** Using the conclusion as a premise.

**Bad Example:**
```markdown
"Our code is high quality because we write good code."
```

### Post Hoc Ergo Propter Hoc (False Cause)

**What It Is:** Assuming that because B followed A, A caused B.

**Bad Example:**
```markdown
"We deployed the new feature and then saw increased latency. 
The new feature must be causing the latency."
```

**Reality:** Correlation doesn't imply causation. Other factors could be responsible.

### Straw Man

**What It Is:** Misrepresenting someone's argument to make it easier to attack.

**Bad Example:**
```markdown
Developer A: "We should add more tests for edge cases."
Developer B: "So you want us to spend all our time writing tests 
and never ship features?"
```

### Bandwagon Fallacy

**What It Is:** Arguing something is correct because many people believe it.

**Bad Example:**
```markdown
"Everyone is using Kubernetes, so we should too."
```

**Why It's Bad:** Popularity doesn't guarantee suitability for your specific needs.

---

## Reasoning Failures in AI

### Multi-Step Logic Errors

**Bad Example:**
```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Yes, Alice must be a programmer.
```

**Why It's Bad:**
- Commits the fallacy of affirming the consequent
- Alice could write code without being a programmer
- Logical structure: (P→Q, Q) ⊬ P

**Correct Reasoning:**
```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Not necessarily. While all programmers write code, not everyone
who writes code is a programmer. Alice could be a student, hobbyist, or
work in another field that involves coding.
```

### Mathematical Reasoning Failures

**Bad Example:**
```
User: A bat and ball cost $1.10 together. The bat costs $1 more than the ball.
How much does the ball cost?
Assistant: The ball costs $0.10.
```

**Reality:** If the ball costs $0.10 and the bat costs $1 more ($1.10), the total would be $1.20. The correct answer is $0.05 for the ball and $1.05 for the bat.

### Causal Reasoning Errors

**Bad Example:**
```
User: Ice cream sales and drowning rates both increase in summer. Does ice cream cause drowning?
Assistant: Yes, there appears to be a causal relationship.
```

**Reality:** Both are caused by a third factor (hot weather), not by each other.

---

## Strategies for Improvement

### For Human Decision-Making

1. **Awareness Training**: Learn to recognize common biases
2. **Checklist Usage**: Use decision checklists to counteract biases
3. **Diverse Teams**: Include people with different perspectives
4. **Pre-mortems**: Imagine failure and work backward to identify causes
5. **Documentation**: Record reasoning for later review

### For AI Systems

1. **Chain-of-Thought Prompting**: Ask the model to show reasoning steps
2. **Self-Correction**: Have the model review and critique its answers
3. **Formal Verification**: Use symbolic reasoning tools for critical logic
4. **Decomposition**: Break complex problems into smaller steps
5. **External Tools**: Use calculators and solvers for mathematical tasks
6. **Multiple Samples**: Generate multiple responses and compare

---

## Related Topics

- **AI/LLM Failures**: See `01_ai_llm_failures.md` for hallucinations and reasoning issues
- **Contradictory Sources**: See documentation on evaluating conflicting information
- **Critical Thinking**: Apply these concepts to evaluate arguments and evidence
