---
# Metadata
title: "Critical Thinking"
description: "Objectively analyze information, identify logical fallacies, evaluate arguments, and make reasoned judgments"
category: "Research Skills"
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
reviewed_by: "Research Skills Team"
next_review: "2027-01-15"

# Classification
tags:
  - critical-thinking
  - analysis
  - evaluation
  - problem-solving
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "12 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Critical Thinking Skill

## Overview
The ability to objectively analyze information, identify logical fallacies, evaluate arguments, and make reasoned judgments.

## Core Competencies

### 1. Analysis & Interpretation
- **Information Breakdown**: Decompose complex problems into components
- **Pattern Recognition**: Identify trends, correlations, and anomalies
- **Context Understanding**: Consider situational factors
- **Assumption Identification**: Recognize stated and unstated premises

### 2. Evaluation & Reasoning
- **Evidence Assessment**: Distinguish strong vs. weak evidence
- **Logical Consistency**: Check for contradictions and fallacies
- **Argument Deconstruction**: Identify claims, evidence, and warrants
- **Inference Drawing**: Make logical conclusions from available data

### 3. Problem Solving
- **Root Cause Analysis**: Dig beyond symptoms to underlying causes
- **Multiple Perspectives**: Consider various viewpoints
- **Solution Generation**: Brainstorm diverse approaches
- **Decision Frameworks**: Apply structured decision-making methods

### 4. Metacognition
- **Self-Awareness**: Recognize own biases and limitations
- **Thinking Process Monitoring**: Evaluate your reasoning quality
- **Intellectual Humility**: Acknowledge uncertainty and gaps
- **Continuous Improvement**: Refine thinking based on feedback

## Frameworks & Methods

### Logical Fallacies to Recognize

#### Formal Fallacies
- **Affirming the Consequent**: If P then Q, Q, therefore P (invalid)
- **Denying the Antecedent**: If P then Q, not P, therefore not Q (invalid)

#### Informal Fallacies
- **Ad Hominem**: Attacking the person, not the argument
- **Straw Man**: Misrepresenting opponent's position
- **False Dichotomy**: Presenting only two options when more exist
- **Appeal to Authority**: Claiming truth because authority says so
- **Slippery Slope**: Arguing one step leads to extreme consequences
- **Circular Reasoning**: Conclusion appears in premise
- **Post Hoc Ergo Propter Hoc**: After this, therefore because of this
- **Appeal to Emotion**: Manipulating feelings instead of using logic
- **Bandwagon**: True because many people believe it
- **Hasty Generalization**: Broad conclusion from small sample

### Root Cause Analysis Tools

#### 5 Whys Technique
```
Problem: Production deployment failed
1. Why? → Tests didn't catch the bug
2. Why? → Test coverage was incomplete
3. Why? → Requirements weren't clear
4. Why? → No formal requirements review
5. Why? → Process doesn't mandate reviews

Root Cause: Missing process requirement for reviews
```

#### Fishbone Diagram (Ishikawa)
```
                    ┌─────────────┐
                    │   PROBLEM   │
                    └──────┬──────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   ┌────┴────┐       ┌─────┴─────┐      ┌────┴────┐
   | People  |       |  Process  |      |Technology|
   └────┬────┘       └─────┬─────┘      └────┬────┘
        │                  │                  │
   - Training         - Documentation    - Legacy code
   - Communication    - Reviews          - Tool limitations
```

### Decision-Making Frameworks

#### Pros-Cons-Analysis (PCA)
| Option | Pros (+) | Cons (-) | Interesting (?) |
|--------|----------|----------|-----------------|
| A      |          |          |                 |
| B      |          |          |                 |

#### Weighted Decision Matrix
| Criteria | Weight | Option A | Option B | Option C |
|----------|--------|----------|----------|----------|
| Cost     | 0.3    | 8×0.3=2.4| 6×0.3=1.8| 9×0.3=2.7|
| Quality  | 0.4    | 7×0.4=2.8| 9×0.4=3.6| 6×0.4=2.4|
| Time     | 0.3    | 6×0.3=1.8| 5×0.3=1.5| 8×0.3=2.4|
| **Total**|        | **7.0**  | **6.9**  | **7.5**  |

#### Cynefin Framework
```
COMPLEX                          COMPLICATED
(Context-free)                   (Expert knowledge needed)
    │                                │
    │    ╭─────────────╮            │
    │    │   CHAOS    │             │
    │    │  Act-Sense │             │
    │    │   -Respond │             │
    │    ╰──────┬──────╯            │
    │           │                   │
    │    ╭──────┴──────╮            │
    │    │  COMPLEX   │             │
    │    │ Probe-Sense│             │
    │    │  -Respond  │             │
    │    ╰─────────────╯            │
    │                               │
CONFUSED                       CLEAR
(Not sure which domain)          (Best practices apply)
                                    │
                                    │
                            Sense-Categorize-Respond
```

## Practical Templates

### Argument Analysis Template
```markdown
# Argument Analysis: [Topic]

## Claim
[What is being asserted?]

## Evidence Provided
1. 
2. 
3. 

## Underlying Assumptions
- Stated: 
- Unstated: 

## Logic Check
- [ ] Evidence supports claim
- [ ] No logical fallacies detected
- [ ] Alternative explanations considered
- [ ] Counterarguments addressed

## Strengths of Argument

## Weaknesses of Argument

## My Conclusion
[Well-reasoned judgment with confidence level]
```

### Critical Question Checklist
```markdown
## Clarity
- [ ] What exactly is being claimed?
- [ ] Are key terms defined?
- [ ] Is the question/problem clearly stated?

## Accuracy
- [ ] Is the information true?
- [ ] How can we verify it?
- [ ] Are sources reliable?

## Precision
- [ ] Are there specific details?
- [ ] Is it sufficiently detailed?
- [ ] Are numbers/data exact?

## Relevance
- [ ] Does this relate to the issue?
- [ ] How does this help answer the question?
- [ ] Is it addressing the real problem?

## Depth
- [ ] Does it address complexities?
- [ ] Are multiple factors considered?
- [ ] Are difficulties acknowledged?

## Breadth
- [ ] Are other viewpoints considered?
- [ ] What would opponents say?
- [ ] Are there alternative approaches?

## Logic
- [ ] Do conclusions follow from evidence?
- [ ] Are there contradictions?
- [ ] Does this make sense given what we know?

## Significance
- [ ] Is this the most important factor?
- [ ] What's the impact?
- [ ] Does this matter in the bigger picture?
```

### Bias Self-Check Template
```markdown
# Bias Reflection

## Situation/Decision
[What am I thinking about?]

## Potential Biases to Consider
- [ ] **Confirmation Bias**: Am I seeking only supporting evidence?
- [ ] **Anchoring Bias**: Am I over-relying on first information?
- [ ] **Availability Heuristic**: Am I overweighting recent/vivid examples?
- [ ] **Sunk Cost Fallacy**: Am I continuing due to past investment?
- [ ] **Overconfidence**: Am I more certain than evidence warrants?
- [ ] **Groupthink**: Am I conforming to group opinion?
- [ ] **Halo Effect**: Am I letting one positive trait influence overall judgment?
- [ ] **Status Quo Bias**: Am I preferring current state without reason?

## Mitigation Strategies
- Seek disconfirming evidence
- Consult diverse perspectives
- Use structured decision frameworks
- Sleep on important decisions
- Consider opposite position seriously

## Revised Thinking
[After bias check, how has my thinking changed?]
```

## Common Pitfalls

### ❌ What to Avoid
- Accepting claims without evidence
- Confusing correlation with causation
- Letting emotions override logic
- Ignoring contradictory evidence
- Overconfidence in conclusions
- Black-and-white thinking
- Not considering base rates
- Falling for persuasive but flawed arguments
- Analysis paralysis (overthinking)
- Dismissing expert consensus without cause

### ✅ Best Practices
- Pause before accepting or rejecting claims
- Ask "What would change my mind?"
- Seek out opposing viewpoints charitably
- Quantify uncertainty when possible
- Update beliefs based on new evidence
- Distinguish facts from interpretations
- Consider opportunity costs
- Use probabilistic thinking
- Document reasoning for review
- Practice intellectual humility

## Tools & Resources

### Critical Thinking Tools
- **Mind mapping software**: Visualize connections
- **Argument mapping tools**: Rationale, Kialo
- **Decision analysis software**: TreeAge, SilverDecisions
- **Statistical tools**: R, Python for data analysis

### Learning Resources
- **Books**: 
  - "Thinking, Fast and Slow" by Daniel Kahneman
  - "The Demon-Haunted World" by Carl Sagan
  - "Superforecasting" by Philip Tetlock
  - "Calling Bullshit" by Carl Bergstrom & Jevin West
  
- **Online Courses**:
  - Coursera: Critical Thinking Specialization
  - edX: Logic and Critical Thinking
  - Khan Academy: Logic tutorials

- **Websites**:
  - LessWrong (rationality community)
  - Farnam Street (mental models)
  - Your Logical Fallacy Is (fallacy reference)

## Example Application

### Scenario: Evaluating a New Technology Adoption Proposal

**Claim**: "We should adopt Microservice Architecture because it's industry standard."

**Critical Analysis:**

1. **Identify Assumptions**
   - Industry standard = right for us
   - Benefits outweigh costs
   - Team can handle complexity

2. **Gather Evidence**
   - What problems does it solve?
   - What problems does it create?
   - What do similar companies report?

3. **Consider Alternatives**
   - Modular monolith
   - Service-oriented architecture
   - Status quo with improvements

4. **Evaluate Trade-offs**
   - Development velocity vs. scalability
   - Team expertise vs. learning curve
   - Short-term cost vs. long-term benefit

5. **Make Reasoned Recommendation**
   - Based on specific context, not trends
   - Acknowledge uncertainties
   - Propose pilot/test approach

## Related Skills

- [Information Retrieval](information_retrieval.md) - Gathering evidence for analysis
- [Data Analysis](../data-skills/data_analysis.md) - Quantitative reasoning with data
- [Explanation](../behavior-skills/explanation.md) - Communicating reasoned conclusions

## Version Information

---
version: 1.0.0
last_updated: 2026-01-15
reviewed_by: Research Skills Team
next_review: 2026-07-15
---
