# Teaching Skill

## Overview

Guide others in acquiring new knowledge and skills effectively. This skill helps you structure learning experiences, explain concepts clearly, and support skill development in others.

## When to Use

- Onboarding new team members
- Mentoring junior developers
- Leading training sessions or workshops
- Creating educational content
- Pair programming
- Code review as a teaching opportunity

## The Teaching Framework

### Step 1: Assess the Learner

**Goal:** Understand where the learner is starting from.

**Questions to Ask:**
- What's your current experience level with this topic?
- Have you worked with similar technologies before?
- What are your learning goals?
- How do you prefer to learn (visual, hands-on, reading)?
- What's your timeline for learning this?

**Assessment Methods:**
- **Skill inventory:** List related skills they already have
- **Pre-test:** Simple questions to gauge baseline knowledge
- **Discussion:** Talk about their experience and goals
- **Observation:** Watch them attempt a simple task

### Step 2: Set Clear Objectives

**Goal:** Define what success looks like for the learning session.

**Learning Objective Formula:**
```
By the end of this [session/course], you will be able to [action verb] [content] [condition/criteria]
```

**Examples:**
- "By the end of this session, you will be able to write basic SQL queries using SELECT, WHERE, and JOIN"
- "After this workshop, you will be able to create a React component with props and state"
- "By tomorrow, you'll be able to navigate the codebase and find relevant files independently"

**Bloom's Taxonomy Levels:**
| Level | Verbs | Example |
|-------|-------|---------|
| Remember | Define, list, recall | List the Git commands |
| Understand | Explain, describe, summarize | Explain how closures work |
| Apply | Use, implement, solve | Use async/await to handle promises |
| Analyze | Compare, contrast, differentiate | Compare REST vs GraphQL |
| Evaluate | Judge, critique, recommend | Critique this code architecture |
| Create | Build, design, develop | Build a complete API endpoint |

### Step 3: Structure the Content

**Goal:** Organize material in a logical, digestible sequence.

**Effective Sequences:**

#### Simple to Complex
```
Variables → Data Types → Operators → Functions → Objects → Classes
```

#### Concrete to Abstract
```
Specific example → Pattern recognition → General principle → Application
```

#### Known to Unknown
```
Connect new concepts to what they already understand
```

#### Problem-Centered
```
Present a problem → Teach concepts needed to solve it → Practice
```

**Chunking Guidelines:**
- Break content into 5-10 minute segments
- One concept per chunk
- Build on previous chunks
- Include practice between chunks

### Step 4: Deliver Instruction

**Goal:** Present material in an engaging, understandable way.

**Teaching Techniques:**

#### I Do, We Do, You Do
1. **I Do:** Demonstrate while explaining your thinking
2. **We Do:** Solve a problem together with guidance
3. **You Do:** Learner solves independently

#### Think Aloud
Verbalize your thought process:
```
"I'm looking at this error message... it says 'undefined is not a function'...
that usually means I'm calling something that doesn't exist...
let me check where this variable is defined..."
```

#### Scaffolding
Provide temporary support that's gradually removed:
- Start with templates and examples
- Provide hints before full answers
- Reduce help as competence grows

#### Analogies and Metaphors
Connect abstract concepts to familiar things:
```
"A Promise is like ordering food at a restaurant:
- You place the order (initiate the async operation)
- You get a ticket/pager (the Promise object)
- Sometimes your food is ready (resolved)
- Sometimes there's a problem (rejected)"
```

### Step 5: Check Understanding

**Goal:** Verify the learner has grasped the concepts.

**Formative Assessment Methods:**

#### Questions to Ask
- "Can you explain this back to me in your own words?"
- "What would happen if we changed X to Y?"
- "How is this different from [related concept]?"
- "When would you use this approach vs [alternative]?"

#### Practical Checks
- Have them solve a similar problem
- Ask them to debug intentionally broken code
- Request they teach the concept back to you
- Give a short coding exercise

#### Observational Cues
Watch for:
- ✅ Confident body language
- ✅ Asking insightful questions
- ✅ Making connections to prior knowledge
- ❌ Furrowed brow, confused expression
- ❌ Silent when you expect questions
- ❌ Copying without understanding

### Step 6: Provide Feedback

**Goal:** Help the learner improve through constructive feedback.

**Feedback Principles:**

#### Be Specific
```
❌ "Good job"
✅ "Your function naming is clear and consistent, which makes the code easy to follow"
```

#### Focus on the Work, Not the Person
```
❌ "You're not getting this"
✅ "This approach has a issue with edge cases"
```

#### Balance Positive and Constructive
```
"What's working well: [specific strengths]
What to improve: [specific areas]
How to improve: [actionable suggestions]"
```

#### Timely and Frequent
- Give feedback soon after the work
- Don't wait until the end to address issues
- Celebrate small wins along the way

## Teaching Patterns

### The Concept Attainment Model
1. Show examples that fit the concept
2. Show examples that don't fit
3. Learner identifies the pattern
4. Learner defines the concept
5. Test with new examples

### Guided Discovery
1. Present a problem or scenario
2. Let learner explore and experiment
3. Ask probing questions
4. Guide toward discovery
5. Formalize the learning

### Case-Based Learning
1. Present a real-world case
2. Analyze the situation together
3. Discuss possible approaches
4. Reveal what was actually done
5. Extract general principles

### Peer Teaching
1. Teach a concept to the learner
2. Have them teach it to someone else
3. Observe and provide feedback
4. Discuss what worked and what didn't

## Common Teaching Scenarios

### Explaining a New Concept

```markdown
## Teaching Plan: [Concept Name]

### Hook (Why should they care?)
[Real-world relevance or problem it solves]

### Prerequisites
[What they need to know first]

### Core Explanation
[Clear, concise definition]

### Example
[Concrete, relatable example]

### Non-Example
[What it's NOT, to clarify boundaries]

### Practice
[Hands-on exercise]

### Check Understanding
[Questions or tasks to verify learning]
```

### Debugging Session as Teaching

```markdown
## Approach

1. Let them share their screen
2. Ask them to explain what they're trying to do
3. Ask: "What have you tried so far?"
4. Guide them to observe the actual behavior
5. Ask: "What do you think is causing this?"
6. Help them form a hypothesis
7. Let them test their hypothesis
8. After fixing, ask: "What did you learn?"
```

### Code Review as Teaching

```markdown
## Teaching-Focused Review

### Start Positive
"This function handles the core logic well, especially..."

### Ask Questions Instead of Dictating
"What do you think about extracting this into a helper function?"

### Explain the Why
"We prefer immutability here because it prevents..."

### Prioritize
Focus on 2-3 most important points, not every nitpick

### Offer Resources
"Here's a great article on this pattern..."
```

## Adapting to Learning Styles

### Visual Learners
- Use diagrams and flowcharts
- Draw on whiteboard
- Show code examples
- Use color coding

### Auditory Learners
- Explain concepts verbally
- Encourage discussion
- Use mnemonics
- Have them explain back

### Kinesthetic Learners
- Hands-on coding exercises
- Build projects immediately
- Learn by debugging
- Physical analogies

### Reading/Writing Learners
- Provide documentation links
- Take notes together
- Write summaries
- Read code together

## Common Teaching Mistakes

❌ **Moving Too Fast:** Covering too much without checking understanding
   - **Fix:** Pause frequently, ask questions

❌ **Assuming Knowledge:** Skipping prerequisites
   - **Fix:** Explicitly state assumptions, check first

❌ **Taking Over:** Doing the work for them
   - **Fix:** Guide, don't do; let them struggle productively

❌ **No Context:** Teaching isolated facts
   - **Fix:** Connect to bigger picture and real applications

❌ **One-Size-Fits-All:** Same approach for everyone
   - **Fix:** Adapt to individual learner needs

❌ **No Practice:** All theory, no application
   - **Fix:** Balance explanation with hands-on work

## Building a Growth Mindset

Encourage learners by:

✅ Praising effort over innate ability
✅ Normalizing struggle as part of learning
✅ Sharing your own learning journey
✅ Framing mistakes as learning opportunities
✅ Setting high but achievable expectations
✅ Celebrating progress, not just perfection

**Phrases to Use:**
- "That's a common confusion—let's work through it"
- "Great question! That shows you're thinking deeply"
- "Let's figure this out together"
- "What have you learned from trying that?"
- "You're developing the right instincts"
