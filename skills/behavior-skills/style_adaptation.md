---
# Metadata
title: "Style Adaptation"
description: "Adjust communication and code style to match different contexts, audiences, and team conventions"
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
  - style-adaptation
  - communication
  - flexibility
  - audience-awareness
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "12 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Style Adaptation Skill

## Overview

Adjust your communication and code style to match different contexts, audiences, and team conventions. This skill helps you write code and documentation that fits seamlessly into any project or team culture.

## Core Competencies

- **Pattern Observation**: Quickly identify naming, formatting, and communication conventions in a new codebase or team
- **Convention Extraction**: Make implicit style rules explicit by analyzing configs, docs, and existing code
- **Style Matching**: Adapt your output to blend seamlessly with existing project conventions
- **Contextual Judgment**: Know when to follow existing style and when to propose improvements
- **Multi-Project Fluency**: Switch between different style contexts without cross-contamination

## When to Use

- Joining a new team or project
- Contributing to open source
- Working with multiple codebases
- Writing documentation for different audiences
- Adapting to client preferences
- Code reviews across different teams

## The Style Adaptation Framework

### Step 1: Observe Existing Patterns

**Goal:** Understand the current style before contributing.

**What to Look For:**

#### Code Style
- **Naming conventions:** camelCase, snake_case, PascalCase, kebab-case
- **Indentation:** Spaces vs tabs, 2 vs 4 spaces
- **Braces:** K&R style, Allman style, no braces
- **Quotes:** Single, double, backticks
- **Semicolons:** Always, never, optional
- **Line length:** 80, 100, 120 characters
- **Import organization:** Alphabetical, by type, grouped

#### Documentation Style
- **Tone:** Formal, casual, technical, friendly
- **Detail level:** Minimal, comprehensive, balanced
- **Format:** JSDoc, docstrings, inline comments
- **Language:** Imperative, descriptive, explanatory

#### Communication Style
- **Directness:** Blunt, diplomatic, indirect
- **Formality:** Professional, casual, friendly
- **Emoji usage:** None, minimal, frequent
- **Response time:** Immediate, thoughtful delays

### Step 2: Identify Style Rules

**Goal:** Make implicit conventions explicit.

**Sources of Truth:**
1. **Style guides:** ESLint config, Prettier rules, editorconfig
2. **Documentation:** CONTRIBUTING.md, README, style guides
3. **Existing code:** The codebase itself is the best reference
4. **Team norms:** Ask team members about unwritten rules

**Create a Quick Reference:**
```markdown
## Project X Style Guide

### Naming
- Variables: camelCase
- Classes: PascalCase  
- Constants: UPPER_SNAKE_CASE
- Files: kebab-case.tsx

### Formatting
- Indent: 2 spaces
- Quotes: single
- Semicolons: required
- Line length: 100 chars

### Git Commits
- Format: type(scope): message
- Types: feat, fix, docs, style, refactor, test, chore
```

### Step 3: Match the Style

**Goal:** Blend in seamlessly with existing work.

**Techniques:**

#### Use Automated Tools
```bash
# Install project-specific tooling
npm install

# Run linter to catch style issues
npm run lint

# Auto-format with project config
npm run format
```

#### Study Representative Examples
Find well-regarded files in the codebase:
```
# Look at similar files for patterns
find src -name "*.service.ts" | head -5

# Study how senior team members write code
git log --author="senior-dev" --oneline
```

#### Mirror Language and Tone
```
❌ Your usual: "This function is kinda slow"
✅ Matching formal: "Performance optimization may be beneficial"
✅ Matching casual: "This could use some speedup"
```

### Step 4: Adapt Incrementally

**Goal:** Adjust gradually while maintaining authenticity.

**Approach:**
1. Start with obvious, mechanical conventions (formatting, naming)
2. Move to structural patterns (file organization, module patterns)
3. Finally adapt subtle aspects (commenting style, error handling)

**Don't:**
- Change everything at once
- Sacrifice clarity for conformity
- Adopt bad practices just because they exist

### Step 5: Know When to Deviate

**Goal:** Balance adaptation with improvement.

**When to Follow Existing Style:**
- Team has agreed-upon conventions
- Style is documented and enforced
- Deviation would cause friction
- It's purely aesthetic preference

**When to Propose Changes:**
- Current style causes bugs
- Industry standard is clearly better
- Team is open to improvement
- You can justify the change

**How to Propose:**
```
"I noticed we're using [current pattern]. I'm wondering if 
[alternative] might help with [specific benefit]. What do 
others think?"
```

## Style Dimensions

### Code Formatting

| Aspect | Options | Example |
|--------|---------|---------|
| **Naming** | camelCase, snake_case, PascalCase | `userData`, `user_data`, `UserData` |
| **Braces** | Same line, new line | `function() {` vs `function()\n{` |
| **Quotes** | Single, double, backtick | `'text'`, `"text"`, `` `text` `` |
| **Trailing commas** | Always, never, multiline | `[a, b,]` vs `[a, b]` |
| **Spaces** | 2, 4, tabs | `  ` vs `    ` vs `\t` |

### Documentation Tone

| Audience | Tone | Characteristics |
|----------|------|-----------------|
| **Internal devs** | Casual, direct | Assumes context, uses jargon |
| **API consumers** | Clear, precise | Examples, edge cases |
| **End users** | Friendly, simple | No jargon, step-by-step |
| **Executives** | Concise, business-focused | Outcomes, not implementation |

### Communication Styles

| Style | Markers | When to Use |
|-------|---------|-------------|
| **Direct** | Short sentences, imperative mood | Emergency, experienced teams |
| **Diplomatic** | Hedging, suggestions | Cross-team, sensitive topics |
| **Detailed** | Explanations, context | Documentation, onboarding |
| **Minimal** | Just facts, no fluff | Status updates, busy contexts |

## Common Scenarios

### Joining a New Team

**First Week:**
1. Read all available documentation
2. Set up linting and formatting tools
3. Ask about unwritten conventions
4. Review recent PRs to see what gets approved
5. Start with small, low-risk contributions

**Questions to Ask:**
- "Are there any style quirks I should know about?"
- "What's the best way to learn our conventions?"
- "Any pet peeves I should avoid?"

### Contributing to Open Source

**Before Your First PR:**
1. Read CONTRIBUTING.md thoroughly
2. Look at recent merged PRs for patterns
3. Run all checks locally before submitting
4. Match the project's commit message style
5. Follow the review feedback style

**Example:**
```
# If project uses conventional commits:
❌ "Fixed the bug"
✅ "fix(parser): handle null values in JSON input"
```

### Multi-Project Work

**Context Switching Strategy:**
1. Keep separate editor profiles per project
2. Use project-specific IDE settings
3. Create quick reference cards for each
4. Take 5 minutes to review style before coding
5. Let tools (linters) enforce the differences

## Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Style imposition | Friction with team, rejected PRs | Adapt first, suggest changes later |
| Inconsistent mixing | Unreadable code within same file | Match surrounding code at all times |
| Over-conforming | Adopting genuinely harmful patterns | Respectfully suggest improvements for bad conventions |
| Style pedantry | Wastes review time on formatting | Use automated tools for mechanical style |
| Assuming universality | Unnecessary conflicts over preferences | Recognize style is often preference, not truth |

## Best Practices

1. **Observe before contributing**: Read existing code and docs for at least a day before your first PR
2. **Automate mechanical style**: Set up linters and formatters from the project's config immediately
3. **Study representative examples**: Find well-regarded files and model your work after them
4. **Ask about unwritten rules**: "Are there any style quirks I should know about?"
5. **Start small**: Make low-risk contributions to learn conventions before tackling complex changes
6. **Keep separate profiles**: Use project-specific editor configs to avoid cross-contamination

## Tools & Resources

- **ESLint/Prettier** - JavaScript/TypeScript linting and formatting
- **Black/Flake8** - Python code formatting and style checking
- **EditorConfig** - Cross-editor consistency for indentation, line endings, charset
- **RuboCop/gofmt/clang-format** - Style enforcement for Ruby, Go, C/C++
- **CONTRIBUTING.md templates** - Document project conventions for newcomers

## Example Application

**Scenario:** Contributing to an open-source Python project for the first time

**Application:**
1. **Observe**: Read CONTRIBUTING.md, scan recent merged PRs, note snake_case naming, 4-space indent, single quotes
2. **Configure**: Set up flake8 with project's `.flake8` config, enable Black with project's `pyproject.toml`
3. **Study**: Read 3 well-regarded service files to understand patterns (error handling, docstrings, imports)
4. **Contribute**: Submit a small bug fix matching all observed conventions — PR accepted without style feedback
5. **Propose change**: After 2 weeks, suggest adding type hints — team agrees, you lead the effort

**Outcome:** First PR accepted without changes. Earned trust to propose improvements. Became a regular contributor within 2 months.

## Success Indicators

You've mastered style adaptation when you can:

- ✅ Match a new project's style so well that your code is indistinguishable from existing work
- ✅ Set up appropriate tooling within your first hour on a new project
- ✅ Identify and document unwritten conventions that newcomers need to know
- ✅ Switch between multiple project styles without mixing them
- ✅ Know when to follow conventions and when to respectfully propose changes

## Related Skills

- [Learning](learning.md) - Quickly survey and absorb new project conventions
- [Code Review](../collaboration-skills/code_review.md) - Review for style consistency using automated tools
- [Explanation](explanation.md) - Document style decisions and rationale for the team

## Version Information

---
version: 1.0.0
last_updated: 2026-01-15
reviewed_by: Behavior Skills Team
next_review: 2026-07-15
---
