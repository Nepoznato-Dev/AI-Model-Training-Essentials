# Skills Repository

A comprehensive collection of professional skills for software developers, engineers, and technical professionals.

## Overview

This repository contains structured skill documentation organized by category. Each skill document follows a consistent template including:

- **Core Competencies**: What you'll learn
- **Frameworks & Methods**: Proven approaches and methodologies
- **Practical Templates**: Ready-to-use templates and checklists
- **Common Pitfalls**: What to avoid
- **Best Practices**: Industry-standard recommendations
- **Tools & Resources**: Helpful tools and learning materials
- **Examples**: Real-world applications
- **Success Indicators**: How to measure proficiency

## Categories

### 🎯 Focused Skills Library (`focused-skills/`)
**NEW!** 10 well-developed ML/AI skills with practice projects and deliberately broken code to debug.

Each skill includes:
- Clear learning objectives tied to specific guides
- Hands-on practice exercises
- Broken code to fix (learn by debugging!)
- Real-world applications
- Mastery checklists

[**Start Here →**](./focused-skills/README.md)

---

### 🧠 Behavior Skills (`behavior-skills/`)
Cognitive and personal effectiveness skills for individual contributors.

- Brainstorming
- Debugging
- Explanation
- Learning
- Planning
- Style Adaptation
- Summarization
- Teaching
- Writing

### 🤝 Collaboration Skills (`collaboration-skills/`)
Skills for working effectively with others.

- Code Review
- Pair Programming
- Team Collaboration

### 🎨 Designing Skills (`designing-skills/`)
Design-related competencies for building better products.

- API Design
- GUI Design
- System Architecture
- UI/UX Design
- Visual Design

### 📊 Research Skills (`research-skills/`)
Information gathering and analysis capabilities.

- Critical Thinking
- Information Retrieval

### 🗣️ Speaking Skills (`speaking-skills/`)
Communication and presentation abilities.

- One-on-One Communication
- Public Speaking
- Technical Presentation

### 🔧 Technical Skills (`technical-skills/`)
Core technical competencies for software development.

- Programming Fundamentals
- Algorithm Design

### ✅ Testing Skills (`testing-skills/`)
Quality assurance and testing methodologies.

- Test Automation
- Unit Testing

### ⚙️ DevOps Skills (`devops-skills/`)
Infrastructure, deployment, monitoring, and operational excellence.

- CI/CD
- Infrastructure as Code
- Container Orchestration

### 🔒 Security Skills (`security-skills/`)
Application security and secure coding practices.

- Authentication & Authorization
- Secure Coding
- Threat Modeling

### 👔 Management Skills (`management-skills/`)
Leadership and people management capabilities.

- Project Management

### 📈 Data Skills (`data-skills/`)
Data engineering, analysis, and database design.

- Data Analysis
- Database Design

## Skill Template

All skills follow the template defined in [`skill-creator.md`](skill-creator.md):

```markdown
# [Skill Name]

## Overview
[Brief description of the skill and its importance]

## Core Competencies
[List of key competencies this skill covers]

## When to Use
[Situations where this skill applies]

## Framework/Methodology
[Detailed framework or approach]

## Practical Templates
[Ready-to-use templates, checklists, or formats]

## Common Pitfalls
[Mistakes to avoid]

## Best Practices
[Industry-standard recommendations]

## Tools & Resources
[Helpful tools, libraries, and learning materials]

## Examples
[Real-world application examples]

## Success Indicators
[How to measure proficiency]

## Related Skills
[Links to complementary skills]
```

## YAML Frontmatter

Every skill file includes a YAML frontmatter block at the top (between `---` delimiters) with metadata for contributors and reviewers:

```yaml
---
# Metadata
title: "Skill Name"
description: "One-line description"
category: "Category Name"
version: "1.0.0"
status: "active"              # active | draft | deprecated | archived

# Contribution
authors:
  - name: "Author Name"
    email: "author@example.com"
    role: "original_author"   # original_author | contributor | maintainer | reviewer
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-01-15"
    author: "Author Name"
    changes: "Initial skill creation"

# Review
created: "2026-01-15"
last_modified: "2026-01-15"
review_date: "2026-07-15"
reviewed_by: "Category Skills Team"
next_review: "2027-01-15"

# Classification
tags: [tag1, tag2, tag3]
difficulty_level: "intermediate"  # beginner | intermediate | advanced
prerequisites: []
estimated_reading_time: "X min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
```

See the [Contributing](#contributing) section below for how to update frontmatter when making changes.

## Contributing

We welcome contributions! Here's how to get started:

### Creating a New Skill

1. **Propose**: Open a GitHub issue describing the new skill and why it's needed
2. **Branch**: Create a feature branch from `main`
3. **Draft**: Create the skill file following the [standard template](skill-creator.md)
4. **Frontmatter**: Fill in ALL frontmatter fields at the top of the file
5. **Submit**: Open a pull request for review

### Updating an Existing Skill

When making changes to a skill file, **always update the frontmatter**:

1. **Bump the version** (follow [SemVer](https://semver.org/)):
   - **Patch** (1.0.x): Typos, formatting, minor corrections
   - **Minor** (1.x.0): New sections, expanded content, new templates
   - **Major** (x.0.0): Complete rewrite or restructuring
2. **Add a changelog entry** (newest first):
   ```yaml
   changelog:
     - version: "1.1.0"
       date: "2026-08-05"
       author: "Your Name"
       changes: "Added new template for X, expanded best practices"
     - version: "1.0.0"
       date: "2026-01-15"
       author: "Original Author"
       changes: "Initial skill creation"
   ```
3. **Update `last_modified`** to today's date
4. **Add yourself** to `contributors` if this is your first change to the file

### Review Process

- All changes are reviewed by category maintainers before merge
- Ensure the [Quality Checklist](skill-creator.md) passes
- Keep cross-references and links up to date
- Follow the existing tone and style of the skill

## Learning Paths

Learning paths mapping skills to roles and experience levels are coming soon.