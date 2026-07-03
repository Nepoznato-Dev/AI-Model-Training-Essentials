# Style Adaptation Skill

## Overview

Adjust your communication and code style to match different contexts, audiences, and team conventions. This skill helps you write code and documentation that fits seamlessly into any project or team culture.

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

## Anti-Patterns

❌ **Style Imposition:** Forcing your preferences on existing projects
   - **Fix:** Adapt first, suggest changes later through proper channels

❌ **Inconsistent Mixing:** Using different styles within same file
   - **Fix:** Pick one style per file, match surrounding code

❌ **Over-Conforming:** Adopting genuinely harmful patterns
   - **Fix:** Respectfully suggest improvements for problematic conventions

❌ **Style Pedantry:** Making style the focus of reviews
   - **Fix:** Use automated tools, focus human review on substance

❌ **Assuming Universality:** Thinking your way is the right way
   - **Fix:** Remember style is often preference, not truth

## Tools for Style Adaptation

### Linters and Formatters
- **ESLint/Prettier:** JavaScript/TypeScript
- **Black/Flake8:** Python
- **RuboCop:** Ruby
- **gofmt:** Go
- **clang-format:** C/C++

### Editor Configuration
- **.editorconfig:** Cross-editor standards
- **Workspace settings:** VS Code workspace-specific configs
- **Project templates:** Starter configs for new projects

### Learning Aids
- **Code snapshots:** Save examples of "good" code from the project
- **Checklists:** Pre-submission style checks
- **Pair programming:** Learn by working with experienced members

## Building Style Flexibility

**Practice Exercises:**
1. Rewrite the same function in 3 different style guides
2. Contribute to projects with conflicting conventions
3. Document the style guide for your current project
4. Do a code review focusing only on style consistency

**Mindset Shifts:**
- Style consistency > personal preference
- Team harmony > being right about formatting
- Adaptability is a professional skill
- Good engineers can work in any style
