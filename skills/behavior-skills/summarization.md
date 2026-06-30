# Summarization Skill

## Overview

Condense large amounts of information into concise, accurate summaries while preserving key meaning. This skill helps you extract essential information from documents, code, discussions, and data.

## When to Use

- Reviewing long documents or reports
- Understanding codebases quickly
- Capturing meeting notes
- Creating executive briefings
- Preparing study materials
- Documenting research findings

## The Summarization Framework

### Step 1: Understand the Purpose

**Goal:** Determine what type of summary is needed.

**Summary Types:**

| Type | Purpose | Length | Focus |
|------|---------|--------|-------|
| **Executive** | Decision-makers need key points | 1 paragraph | Conclusions, recommendations |
| **Technical** | Engineers need details | 1-2 pages | Methods, implementations, specs |
| **Abstract** | Quick overview | 150-250 words | Main idea, scope |
| **Bullet Points** | Quick scanning | 5-10 bullets | Key facts, action items |
| **TL;DR** | Ultra-brief | 1-2 sentences | Core message |

**Questions to Answer:**
- Who is the audience?
- What will they use this for?
- How much detail do they need?
- What's the most important takeaway?

### Step 2: Extract Key Information

**Goal:** Identify the most important content.

**For Documents:**
1. Read the title and abstract/introduction
2. Scan section headings
3. Read first and last paragraphs of each section
4. Note repeated terms and concepts
5. Identify conclusions and recommendations

**For Code:**
1. Read file/module names
2. Check exported functions/classes
3. Read function signatures and docstrings
4. Look at main entry points
5. Identify key data structures

**For Meetings/Discussions:**
1. Note the stated objectives
2. Track decisions made
3. Capture action items with owners
4. Record key arguments and conclusions
5. Note follow-up questions

### Step 3: Organize Information

**Goal:** Structure the summary logically.

**Common Structures:**

#### Pyramid (Bottom Line Up Front)
```
Main Conclusion/Recommendation
├── Supporting Point 1
├── Supporting Point 2
└── Supporting Point 3
```

#### Chronological
```
Background → Events in Order → Current Status → Next Steps
```

#### Problem-Solution
```
Problem → Analysis → Solution → Implementation Plan
```

#### Compare-Contrast
```
Option A → Option B → Comparison → Recommendation
```

### Step 4: Write Concisely

**Goal:** Express ideas clearly in fewer words.

**Techniques:**

#### Remove Redundancy
```
❌ "The team members worked together collaboratively to jointly create..."
✅ "The team collaborated to create..."
```

#### Use Active Voice
```
❌ "It was decided by the committee that..."
✅ "The committee decided..."
```

#### Replace Phrases with Words
```
❌ "In order to" → ✅ "To"
❌ "Due to the fact that" → ✅ "Because"
❌ "At this point in time" → ✅ "Now"
```

#### Eliminate Filler
```
❌ "Basically, essentially, fundamentally..."
✅ Remove these words entirely
```

### Step 5: Verify Accuracy

**Goal:** Ensure the summary faithfully represents the source.

**Checklist:**
- [ ] No important information omitted
- [ ] No misrepresentation of facts
- [ ] Numbers and data are correct
- [ ] Conclusions match the source
- [ ] Tone is appropriate
- [ ] Attributions are clear

**Test:** Could someone understand the main points without reading the original?

## Summarization Patterns

### The 5-3-1 Method
- **5** key points from the source
- **3** supporting details
- **1** main takeaway

### The Abstract Formula
```
[Context] + [Problem/Goal] + [Method/Approach] + [Results/Outcome]
```

**Example:**
```
"In response to increasing user complaints about load times (context),
we investigated performance bottlenecks (problem). Using Chrome DevTools
and Lighthouse audits (method), we identified unoptimized images as the
primary cause and reduced average load time by 60% (outcome)."
```

### Code Summary Template
```markdown
## [Module/File Name]

**Purpose:** [What it does]

**Key Components:**
- `FunctionA`: [Brief description]
- `ClassB`: [Brief description]
- `InterfaceC`: [Brief description]

**Dependencies:** [What it relies on]

**Usage:** [How to use it]
```

### Meeting Notes Template
```markdown
## Meeting: [Topic] - [Date]

**Attendees:** [List]

**Decisions Made:**
- [Decision 1]
- [Decision 2]

**Action Items:**
- [ ] [Task] - @owner - Due [date]

**Key Discussion Points:**
- [Point 1]
- [Point 2]

**Next Meeting:** [Date/Time]
```

## Domain-Specific Summarization

### Technical Documentation
Focus on:
- API endpoints and parameters
- Input/output formats
- Error conditions
- Usage examples

### Research Papers
Focus on:
- Research question/hypothesis
- Methodology
- Key findings
- Limitations
- Future work

### Bug Reports
Focus on:
- Steps to reproduce
- Expected vs actual behavior
- Environment details
- Severity/impact
- Proposed fix

### Pull Requests
Focus on:
- What changed
- Why it changed
- Testing done
- Breaking changes (if any)

## Common Pitfalls

❌ **Too Brief:** Losing critical context
   - **Fix:** Include enough detail for the audience

❌ **Too Detailed:** Defeating the purpose
   - **Fix:** Remove examples unless essential

❌ **Biased:** Injecting personal opinion
   - **Fix:** Stick to what the source says

❌ **Out of Context:** Missing background
   - **Fix:** Include necessary prerequisites

❌ **Copy-Paste:** Not truly summarizing
   - **Fix:** Rewrite in your own words

## Quality Checklist

Before finalizing a summary, verify:

✅ **Completeness:** All key points included
✅ **Accuracy:** Faithfully represents source
✅ **Conciseness:** No unnecessary words
✅ **Clarity:** Easy to understand
✅ **Coherence:** Flows logically
✅ **Correctness:** Facts and figures accurate

## Practice Exercises

1. **One Sentence:** Summarize a 10-page document in one sentence
2. **Elevator Pitch:** Explain a complex topic in 30 seconds
3. **Headline Writing:** Create a headline that captures the essence
4. **Layered Summaries:** Write 1-paragraph, 3-sentence, and 1-sentence versions
5. **Compare:** Summarize the same content for different audiences

## Tools and Techniques

### Highlighting Strategy
1. First pass: Highlight anything potentially important
2. Second pass: Un-highlight nice-to-haves
3. Final: Only must-haves remain

### Keyword Extraction
Identify frequently occurring terms and concepts—they're usually central to the content.

### Reverse Outline
After reading, create an outline from memory. This reveals what stuck with you (often the important parts).

### Summary Verification
Ask someone unfamiliar with the source:
- "What do you think is the main point?"
- "What questions do you still have?"
- "Is anything unclear?"
