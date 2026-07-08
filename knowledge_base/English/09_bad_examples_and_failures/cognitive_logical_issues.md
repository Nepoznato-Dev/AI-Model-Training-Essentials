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

- **AI/LLM Failures**: See `ai_llm_failures.md` for hallucinations and reasoning issues
- **Contradictory Sources**: See documentation on evaluating conflicting information
- **Critical Thinking**: Apply these concepts to evaluate arguments and evidence
- **Prompt Engineering**: See `../02_artificial_intelligence/prompt_engineering.md` for techniques to reduce reasoning errors

---

## Additional Cognitive Biases in Software Development

### Status Quo Bias

**What It Is:** Preference for maintaining current state; any change is perceived as a loss.

**Bad Example:**
```markdown
Team Lead: "Should we upgrade to Python 3.12? It has performance improvements 
and security fixes."

Developer: "Python 3.8 works fine. Why risk breaking things?"

Reality: Staying on an older version increases technical debt, security risks,
and makes future upgrades harder.
```

**Mitigation:**
- Quantify costs of not changing
- Set regular upgrade schedules
- Create safe experimentation environments
- Frame changes as opportunities, not threats

### Optimism Bias

**What It Is:** Underestimating time, costs, and risks while overestimating benefits.

**Bad Example:**
```markdown
Project Plan:
- Development: 2 weeks (realistic: 4 weeks)
- Testing: 3 days (realistic: 1 week)
- Bug fixes: 2 days (realistic: 1-2 weeks)
- Contingency: None

Result: Project takes 3x longer than planned.
```

**Mitigation:**
- Use reference class forecasting (compare to similar past projects)
- Add contingency buffers (20-50%)
- Conduct pre-mortems
- Track estimation accuracy over time

### Survivorship Bias

**What It Is:** Focusing on successful examples while ignoring failures.

**Bad Example:**
```markdown
"Look at all these successful startups that didn't do market research!
We don't need market research either."

Reality: Many more startups failed without market research, but they're 
not visible because they didn't survive.
```

**Mitigation:**
- Study both successes AND failures
- Look for base rates and statistics
- Consider invisible data
- Avoid cherry-picking examples

### Fundamental Attribution Error

**What It Is:** Attributing others' behavior to character rather than circumstances.

**Bad Example:**
```markdown
"That developer made a bug because they're careless."

Reality: The bug might be due to unclear requirements, time pressure,
lack of testing infrastructure, or fatigue.
```

**Mitigation:**
- Consider situational factors
- Practice empathy
- Focus on systems, not individuals
- Use blameless post-mortems

### Hindsight Bias

**What It Is:** After an event occurs, believing it was predictable all along.

**Bad Example:**
```markdown
After production outage:
"I knew that deployment was risky. This was totally predictable."

Reality: The outcome wasn't obvious beforehand; hindsight makes it seem clear.
```

**Mitigation:**
- Document predictions before outcomes
- Review decision context, not just outcomes
- Avoid "I told you so" culture
- Focus on improving processes, not assigning blame

---

## More Logical Fallacies

### Appeal to Novelty

**What It Is:** Assuming something is better because it's newer.

**Bad Example:**
```markdown
"We should rewrite our entire backend in the latest framework. 
It's the newest, so it must be better."

Reality: Newer doesn't mean better for your specific use case.
Mature technologies often have better support and stability.
```

### Appeal to Tradition

**What It Is:** Arguing something is correct because it's always been done that way.

**Bad Example:**
```markdown
"We've always deployed on Fridays at 5 PM. We shouldn't change that."

Reality: Just because something is traditional doesn't make it optimal.
(Actually, deploying on Friday at 5 PM is generally considered bad practice!)
```

### Tu Quoque (Appeal to Hypocrisy)

**What It Is:** Dismissing criticism by pointing out the critic's inconsistency.

**Bad Example:**
```markdown
Senior Dev: "You should write tests for this code."
Junior Dev: "But you don't write tests for your code either!"

Reality: The validity of the advice is independent of who gives it.
```

### Loaded Question

**What It Is:** Asking a question that contains an assumption.

**Bad Example:**
```markdown
"Why did you write such terrible code for this module?"

Reality: The question assumes the code is terrible, putting the respondent
on the defensive regardless of actual code quality.
```

### No True Scotsman

**What It Is:** Making an exception to a universal claim when challenged.

**Bad Example:**
```markdown
Person A: "No professional developer writes code without tests."
Person B: "But John is a professional developer and doesn't write tests."
Person A: "Well, no TRUE professional developer writes code without tests."

Reality: This redefines the category to exclude counterexamples rather 
than revising the claim.
```

### Genetic Fallacy

**What It Is:** Judging something based on its origin rather than current merit.

**Bad Example:**
```markdown
"That library came from a small startup, so it can't be enterprise-grade."

Reality: The origin doesn't determine current quality. Evaluate based on
actual characteristics, not source.
```

### Middle Ground Fallacy

**What It Is:** Assuming the truth is always in the middle of two extremes.

**Bad Example:**
```markdown
Developer A: "We should add comprehensive error handling."
Developer B: "Error handling isn't important, skip it."
Compromise: "Let's add some error handling, but not too much."

Reality: One position might be clearly correct. Compromise isn't always wise.
```

---

## Cognitive Biases in AI Systems

### Training Data Bias

AI models inherit biases present in their training data.

**Example:**
```markdown
Training data contains: "The doctor said..." (mostly male pronouns)
                       "The nurse said..." (mostly female pronouns)

Model learns: Doctors are typically male, nurses are typically female.

Result: Model exhibits gender bias in profession associations.
```

**Mitigation:**
- Audit training data for biases
- Use debiasing techniques
- Test for biased outputs
- Diverse data collection

### Automation Bias

**What It Is:** Over-relying on automated systems, even when they're wrong.

**Example:**
```markdown
AI suggests code with a subtle bug.
Developer accepts it without review because "the AI is usually right."

Result: Bug makes it to production.
```

**Mitigation:**
- Maintain human oversight
- Encourage critical evaluation of AI outputs
- Don't treat AI as infallible
- Implement review processes

### Illusion of Understanding

**What It Is:** Believing you understand how an AI works when you don't.

**Example:**
```markdown
User: "The AI understands what I mean, it's like talking to a person."

Reality: LLMs predict tokens based on patterns, they don't truly 
"understand" in the human sense. This illusion leads to over-trust.
```

**Mitigation:**
- Educate users about AI limitations
- Be transparent about how systems work
- Avoid anthropomorphizing AI
- Set appropriate expectations

---

## Case Studies

### Case Study 1: Confirmation Bias in Architecture Selection

**Incident:** A team chose a microservices architecture for a small application.

**Root Cause:** Team lead had read several articles praising microservices and 
only sought information confirming this choice, ignoring warnings about complexity.

**Impact:**
- Massive overhead for a team of 3 developers
- Deployment complexity increased 10x
- Performance degraded due to network calls
- Project delayed by 6 months

**Lesson:** Evaluate architectures based on your specific context, not just 
positive testimonials. Consider trade-offs explicitly.

### Case Study 2: Sunk Cost in Legacy System

**Incident:** Company continued maintaining a custom-built CRM for 5 years 
despite better alternatives.

**Root Cause:** "We've invested $2M already, we can't abandon it now."

**Impact:**
- Annual maintenance cost: $500K
- Opportunity cost: Couldn't use modern features
- Talent retention issues (developers wanted to work with modern tech)
- Total 5-year cost: $4.5M vs. $1.5M for SaaS alternative

**Lesson:** Past investment is sunk. Make decisions based on future value.

### Case Study 3: Availability Heuristic in Security

**Incident:** Team prioritized defending against a recently publicized attack 
vector while ignoring more likely threats.

**Root Cause:** Recent news coverage made one threat type highly available 
in memory, skewing risk assessment.

**Impact:**
- Spent $100K on mitigating low-probability threat
- Actual breach occurred through neglected vector
- Recovery cost: $500K+

**Lesson:** Use data-driven threat modeling, not recency-based prioritization.

---

## Practical Exercises

### Bias Detection Exercise

Review recent decisions and ask:

1. What assumptions did we make?
2. What evidence would contradict our conclusion?
3. Did we consider multiple options or anchor on the first idea?
4. Are we continuing because of future value or past investment?
5. What would we recommend if someone else asked us?

### Logical Fallacy Spotting

Practice identifying fallacies in everyday discussions:

```markdown
Statement: "If we don't adopt AI now, we'll be left behind forever."

Analysis: This is a slippery slope fallacy. It assumes inevitable 
progression to being "left behind" without evidence. Also presents 
a false dichotomy (adopt AI or be left behind).
```

### Pre-Mortem Technique

Before starting a project:

1. Imagine it's 6 months in the future
2. The project has failed spectacularly
3. Write the story of why it failed
4. Work backward to prevent those failure modes

This counters optimism bias and availability heuristic.

---

## Tools and Frameworks

### Decision Journal Template

```markdown
Date: [When]
Decision: [What we decided]
Context: [Situation and constraints]
Options Considered: [Alternatives evaluated]
Expected Outcome: [What we think will happen]
Confidence Level: [How sure we are]
Review Date: [When to revisit]

[Later] Actual Outcome: [What actually happened]
Lessons Learned: [What we'd do differently]
```

### Bias Checklist

Before making important decisions:

- [ ] Have we sought disconfirming evidence?
- [ ] Are we anchored on initial information?
- [ ] Is sunk cost influencing us?
- [ ] Are we overconfident in our estimates?
- [ ] Have we considered base rates?
- [ ] Are we falling for availability/recency bias?
- [ ] Would we make the same choice if starting fresh?

### Red Team Exercise

Assign someone to argue against the proposed decision:

- Their role is to find flaws
- They must present alternative viewpoints
- Team practices responding to criticism constructively
- Document concerns raised and addressed

This counters confirmation bias and groupthink.
