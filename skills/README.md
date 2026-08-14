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

### 🤖 AI Engineering Skills (`ai-engineering-skills/`)
**NEW!** Practical skills for building, fine-tuning, and deploying AI/ML systems.

- [Model Fine-Tuning](./ai-engineering-skills/model_fine_tuning.md) — Adapt pre-trained models with LoRA, QLoRA, and full fine-tuning
- [Experiment Design](./ai-engineering-skills/experiment_design.md) — Structure reproducible ML experiments with statistical rigor
- [Data Pipeline Design](./ai-engineering-skills/data_pipeline_design.md) — Build robust, scalable data pipelines for training and inference

[**Browse Category →**](./ai-engineering-skills/README.md)

### 🤖 Automation Skills (`automation-skills/`)
**NEW!** Skills for automating repetitive workflows and building reliable scripts.

- [Workflow Automation](./automation-skills/workflow_automation.md) — Design automated workflows with scheduling, retries, and monitoring
- [Scripting for Engineers](./automation-skills/scripting_for_engineers.md) — Write robust automation scripts with proper error handling and logging

[**Browse Category →**](./automation-skills/README.md)

### 🧠 Behavior Skills (`behavior-skills/`)
Cognitive and personal effectiveness skills for individual contributors.

- [Brainstorming](./behavior-skills/brainstorming.md)
- [Debugging](./behavior-skills/debugging.md)
- [Explanation](./behavior-skills/explanation.md)
- [Learning](./behavior-skills/learning.md)
- [Planning](./behavior-skills/planning.md)
- [Prompt Engineering](./behavior-skills/prompt_engineering.md)
- [Style Adaptation](./behavior-skills/style_adaptation.md)
- [Summarization](./behavior-skills/summarization.md)
- [Teaching](./behavior-skills/teaching.md)
- [Writing](./behavior-skills/writing.md)

### 🤝 Collaboration Skills (`collaboration-skills/`)
Skills for working effectively with others.

- [Code Review](./collaboration-skills/code_review.md)
- [Pair Programming](./collaboration-skills/pair_programming.md)
- [Team Collaboration](./collaboration-skills/team_collaboration.md)

### 🎨 Designing Skills (`designing-skills/`)
Design-related competencies for building better products.

- [API Design](./designing-skills/api_design.md)
- [GUI Design](./designing-skills/gui_design.md)
- [System Architecture](./designing-skills/system_architecture.md)
- [UI/UX Design](./designing-skills/ui_ux_design.md)
- [Visual Design](./designing-skills/visual_design.md)

### 📈 Data Skills (`data-skills/`)
Data engineering, analysis, and database design.

- [Data Analysis](./data-skills/data_analysis.md)
- [Database Design](./data-skills/database_design.md)
- [Experiment Tracking](./data-skills/experiment_tracking.md)

### ⚙️ DevOps Skills (`devops-skills/`)
Infrastructure, deployment, monitoring, and operational excellence.

- [CI/CD](./devops-skills/ci_cd.md)
- [Infrastructure as Code](./devops-skills/infrastructure_as_code.md)
- [Container Orchestration](./devops-skills/container_orchestration.md)
- [MLOps](./devops-skills/mlops.md)

### 🔒 Security Skills (`security-skills/`)
Application security and secure coding practices.

- [Authentication & Authorization](./security-skills/authentication_authorization.md)
- [Secure Coding](./security-skills/secure_coding.md)
- [Threat Modeling](./security-skills/threat_modeling.md)

### 🔧 Technical Skills (`technical-skills/`)
Core technical competencies for software development.

- [Programming Fundamentals](./technical-skills/programming_fundamentals.md)
- [Algorithm Design](./technical-skills/algorithm_design.md)
- [Model Evaluation](./technical-skills/model_evaluation.md)
- [Git Workflows](./technical-skills/git_workflows.md)

### ✅ Testing Skills (`testing-skills/`)
Quality assurance and testing methodologies.

- [Test Automation](./testing-skills/test_automation.md)
- [Unit Testing](./testing-skills/unit_testing.md)

### 📊 Research Skills (`research-skills/`)
Information gathering and analysis capabilities.

- [Critical Thinking](./research-skills/critical_thinking.md)
- [Information Retrieval](./research-skills/information_retrieval.md)

### 🗣️ Speaking Skills (`speaking-skills/`)
Communication and presentation abilities.

- [One-on-One Communication](./speaking-skills/one_on_one_communication.md)
- [Public Speaking](./speaking-skills/public_speaking.md)
- [Technical Presentation](./speaking-skills/technical_presentation.md)
- [Technical Writing](./speaking-skills/technical_writing.md)

### 👔 Management Skills (`management-skills/`)
Leadership and people management capabilities.

- [Project Management](./management-skills/project_management.md)

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

Structured skill sequences for common roles and goals:

### New Software Engineer
```
Learning → Debugging → Writing → Planning → Git Workflows → Code Review
```
Build the foundation: learn fast, solve problems systematically, communicate clearly.

### AI/ML Engineer
```
Experiment Design → Model Fine-Tuning → Data Pipeline Design → Prompt Engineering
→ Testing ML Systems → MLOps
```
Master the full ML lifecycle from experiment to production.

### Tech Lead / Senior Engineer
```
System Architecture → Explanation → Teaching → Project Management
→ Code Review → Team Collaboration
```
Multiply your impact through architecture decisions and team development.

### Full-Stack Developer
```
Programming Fundamentals → API Design → UI/UX Design → CI/CD
→ Secure Coding → Test Automation
```
Cover the complete stack from frontend to deployment with security and quality.

## Skill Count

| Category | Skills |
|----------|--------|
| AI Engineering | 3 |
| Automation | 2 |
| Behavior | 10 |
| Collaboration | 3 |
| Data | 3 |
| Designing | 5 |
| DevOps | 4 |
| Management | 1 |
| Research | 2 |
| Security | 3 |
| Speaking | 4 |
| Technical | 4 |
| Testing | 2 |
| **Total** | **46** |

## Inspiration & Acknowledgments

Our skill design methodology draws inspiration from leading open-source skill frameworks:
- [Anthropic Skills](https://github.com/anthropics/skills) — Progressive disclosure and decision-tree patterns
- [OpenAI Skills](https://github.com/openai/skills) — Curated skill collections
- [Google Skills](https://github.com/google/skills) — Domain-specific expertise
- [NVIDIA Skills](https://github.com/NVIDIA/skills) — GPU-optimized workflows
- [Awesome OpenClaw Skills](https://github.com/VoltAgent/awesome-openclaw-skills) — 5,300+ community skills for reference

See [`skill-creator.md`](skill-creator.md) for the full guide on creating new skills, including modern design patterns.