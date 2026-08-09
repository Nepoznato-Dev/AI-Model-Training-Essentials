---
# Metadata
title: "Summarization"
description: "Condense large amounts of information into concise, accurate summaries while preserving key meaning"
category: "Behavior Skills"
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
reviewed_by: "Behavior Skills Team"
next_review: "2027-01-15"

# Classification
tags:
  - summarization
  - concise-communication
  - information-distillation
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
# Summarization Skill

## Overview

Condense large amounts of information into concise, accurate summaries while preserving key meaning. This skill helps you extract essential information from documents, code, discussions, and data.

## Core Competencies

- **Purpose-Driven Summarization**: Select the right summary type (executive, technical, TL;DR) for the audience and context
- **Key Information Extraction**: Identify conclusions, decisions, and action items from documents, code, and discussions
- **Concise Writing**: Eliminate redundancy and filler while preserving essential meaning
- **Accuracy Verification**: Ensure summaries faithfully represent source material without distortion
- **Multi-Format Output**: Produce bullet points, abstracts, meeting notes, and code summaries as needed

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

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Too brief | Critical context lost, decisions misinformed | Include enough detail for the audience's needs |
| Too detailed | Defeats the purpose of summarizing | Remove examples unless essential to understanding |
| Biased summary | Injects personal opinion, misrepresents source | Stick strictly to what the source says |
| Missing context | Readers can't understand without background | Include necessary prerequisites and scope |
| Copy-paste instead of summary | Not truly condensed or synthesized | Rewrite in your own words |

## Best Practices

1. **Know your audience first**: Executive summaries focus on decisions; technical summaries focus on methods
2. **Use the 5-3-1 method**: 5 key points, 3 supporting details, 1 main takeaway
3. **Read first, write second**: Understand the full source before attempting to summarize
4. **Remove redundancy ruthlessly**: "In order to" → "To"; "Due to the fact that" → "Because"
5. **Verify with the source**: Could someone understand the main points without reading the original?
6. **Use structured templates**: Meeting notes, code summaries, and abstracts have proven formats

## Tools & Resources

- **Markdown** - Structure summaries with headers, bullets, and tables for scannability
- **Obsidian/Notion** - Build linked summaries in a personal knowledge base
- **tl;dr AI tools** - Generate initial drafts for human refinement
- **The Abstract Formula** - [Context] + [Problem] + [Method] + [Outcome]
- **Diátaxis Framework** - Distinguish tutorials, how-to guides, reference, and explanation

## Example Application

**Scenario:** Summarizing a 50-page technical investigation report for executive leadership

**Application:**
1. **Purpose**: Executive summary for decision-makers — need conclusions and recommendations only
2. **Extract**: Read report, identify 3 key findings, 2 recommendations, and the timeline
3. **Structure**: Pyramid principle — lead with recommendation, then supporting evidence
4. **Write concisely**: Reduced 50 pages to 1 page with 5 bullet points
5. **Verify**: Checked all numbers against source, confirmed no misrepresentation

**Outcome**: Executives made a decision in one meeting based on the summary. No need to read the full report. Saved ~10 hours of leadership time.

## Success Indicators

You've mastered summarization when you can:

- ✅ Reduce a 50-page document to a 1-page executive summary without losing key points
- ✅ Produce audience-appropriate summaries (executive vs. technical) from the same source
- ✅ Write meeting notes that capture all decisions and action items with owners
- ✅ Summarize a codebase's purpose and structure in under 5 bullet points
- ✅ Verify accuracy — source authors confirm your summary is faithful

## Related Skills

- [Explanation](explanation.md) - Communicating summarized information clearly
- [Teaching](teaching.md) - Using summaries to structure learning materials
- [Critical Thinking](../research-skills/critical_thinking.md) - Evaluating source quality before summarizing

## Version Information

---
version: 1.0.0
last_updated: 2026-01-15
reviewed_by: Behavior Skills Team
next_review: 2026-07-15
---
