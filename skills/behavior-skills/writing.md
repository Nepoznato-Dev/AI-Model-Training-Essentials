---
# Metadata
title: "Writing"
description: "Master the art of clear, effective written communication for technical audiences"
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
  - writing
  - documentation
  - technical-writing
  - communication
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Writing Skill

## Overview

Master the art of clear, effective written communication for technical audiences. This skill helps you produce documentation, articles, emails, and other written content that conveys information accurately and engagingly.

Writing is the primary medium for knowledge transfer in software development. Whether you're documenting an API, writing a commit message, or drafting a project proposal, clear writing amplifies your impact and reduces costly miscommunication.

## Core Competencies

- **Audience Analysis**: Assess reader background and tailor content to their level and needs
- **Structured Drafting**: Use outlines, the pyramid principle, and writing patterns to organize content logically
- **Concise Revision**: Transform verbose drafts into clear, scannable documents through ruthless editing
- **Format Selection**: Choose the right format (tutorial, explanation, reference) for the content's purpose
- **Technical Accuracy**: Ensure code examples, links, and facts are correct and current

## When to Use

- Writing technical documentation or READMEs
- Creating blog posts or articles
- Composing professional emails
- Drafting project proposals or reports
- Writing commit messages and pull request descriptions
- Creating tutorials or guides

## The Writing Framework

### Phase 1: Pre-Writing (Plan)

**Goal:** Clarify your purpose and audience before writing.

**Questions to Answer:**
- Who is my audience?
- What do they already know?
- What do they need to learn or do?
- What's the single most important message?
- What format best serves this content?

**Audience Analysis:**

| Audience | Focus On | Avoid |
|----------|----------|-------|
| **Developers** | Code examples, technical details, edge cases | Oversimplification, hand-waving |
| **Managers** | Outcomes, timelines, risks, ROI | Deep implementation details |
| **End Users** | Step-by-step instructions, screenshots | Technical jargon, assumptions |
| **Mixed** | Clear sections for different levels | Assuming uniform knowledge |

**Outline Structure:**
```
1. Introduction (hook + purpose)
2. Background/Context
3. Main Content (organized logically)
4. Examples/Applications
5. Summary/Next Steps
```

### Phase 2: Drafting (Write)

**Goal:** Get ideas down without over-editing.

**Principles:**
1. **Write first, edit later:** Don't stop to perfect sentences
2. **Follow your outline:** But allow for organic discoveries
3. **Use placeholders:** Mark spots needing research with [TODO]
4. **Focus on flow:** Ensure ideas connect logically

**Opening Strategies:**
- **The Problem Statement**: "Every developer has experienced the frustration of debugging a race condition..."
- **The Question**: "What if you could reduce your deployment time from 30 minutes to 3?"
- **The Statistic**: "Studies show that well-documented code reduces onboarding time by 50%."
- **The Story**: "Last month, a single typo in our configuration took down production for 4 hours."

### Phase 3: Revising (Improve)

**Goal:** Transform rough draft into polished content.

**Revision Checklist:**

#### Structural Review
- [ ] Does the organization make sense?
- [ ] Are transitions smooth between sections?
- [ ] Is the main point clear and prominent?
- [ ] Are examples relevant and helpful?

#### Clarity Review
- [ ] Are sentences concise (aim for 15-25 words)?
- [ ] Is jargon explained or avoided?
- [ ] Is active voice used predominantly?
- [ ] Are ambiguous phrases clarified?

**Before and After:**
```
❌ "The utilization of caching mechanisms facilitates 
the improvement of performance metrics in a significant manner."

✅ "Caching improves performance significantly."
```

### Phase 4: Formatting (Polish)

**Goal:** Make content visually scannable and accessible.

**Key Practices:**
- Use headings effectively (H1 for title, H2 for sections, H3 for subsections)
- Short paragraphs (2-4 sentences)
- Bullet points for lists, numbered lists for sequences
- Code blocks for technical content
- **Bold** for emphasis (sparingly), `inline code` for technical terms
- Tables for comparisons, screenshots for UI content

## Practical Templates

### Tutorial Pattern
```markdown
# How to [Achieve Specific Goal]

## Prerequisites
- What readers need before starting

## Step 1: [First Action]
Explanation of what to do and why.
[Code example]

## Step 2: [Next Action]
Continue with clear, sequential steps.

## Troubleshooting
Common issues and solutions.

## Next Steps
Where to go from here.
```

### Commit Message Pattern
```
type(scope): brief description

Longer explanation if needed. What changed and why.

Fixes #123
```
Types: feat, fix, docs, style, refactor, test, chore

### Pull Request Description Pattern
```markdown
## What Changed
Brief summary of modifications.

## Why
Business or technical rationale.

## Testing
How this was tested.

## Checklist
- [ ] Tests pass
- [ ] Documentation updated
- [ ] Breaking changes documented
```

## Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Wall of text | Readers give up, miss key points | Use headings, lists, and white space |
| Assumed knowledge | Readers get lost early | State prerequisites, link to background |
| Inconsistent terminology | Confusion about whether concepts differ | Create and follow a glossary |
| Outdated code examples | Examples don't work, erode trust | Test all examples, add version notes |
| No call to action | Readers don't know what to do next | End with clear next steps |

## Best Practices

1. **Read widely**: Study well-written technical content to internalize good patterns
2. **Write regularly**: Blog, document, or journal daily to build the muscle
3. **Edit ruthlessly**: Cut unnecessary words — if a sentence doesn't add value, remove it
4. **Use active voice**: "The system processes requests" not "Requests are processed by the system"
5. **Test your examples**: Every code snippet should work when copy-pasted
6. **Get feedback**: Ask "Was any part confusing?" and revise based on responses

## Tools & Resources

- **Grammarly** - Grammar and style checking for clear writing
- **Hemingway Editor** - Highlights complex sentences and passive voice
- **Google Developer Documentation Style Guide** - [developers.google.com/style](https://developers.google.com/style)
- **"On Writing Well"** by William Zinsser - Classic guide to nonfiction writing
- **"The Elements of Style"** by Strunk & White - Foundational grammar reference
- **Markdown** - Universal formatting language for technical documentation

## Example Application

**Scenario:** Writing documentation for a new API endpoint that the team just built

**Application:**
1. **Pre-Write**: Audience is backend developers. They need to integrate the endpoint. Format: API reference with example.
2. **Draft**: Follow reference pattern — Syntax, Parameters table, Returns, Example, Error handling
3. **Revise**: Cut verbose explanations, ensure code example is copy-pasteable, add error cases
4. **Format**: Use tables for parameters, code blocks for examples, bold for required fields
5. **Verify**: Test the code example against the actual API, confirm response format matches

**Outcome:** Developers integrated the endpoint in under 30 minutes. Zero support tickets about usage. Documentation referenced in team onboarding.

## Success Indicators

You've mastered writing when you can:

- ✅ Produce clear documentation that reduces support questions
- ✅ Write commit messages that explain the "why" in under 50 characters
- ✅ Adapt tone and detail level for different audiences (devs vs. managers vs. users)
- ✅ Get feedback like "this is the clearest explanation I've seen"
- ✅ Have your content referenced and shared by others
- ✅ Draft a technical proposal that gets approved without major revisions

## Related Skills

- [Explanation](explanation.md) - Communicating complex concepts clearly
- [Summarization](summarization.md) - Condensing information to key points
- [Teaching](teaching.md) - Structuring content for learning

## Version Information

---
version: 1.0.0
last_updated: 2026-01-15
reviewed_by: Behavior Skills Team
next_review: 2026-07-15
---
