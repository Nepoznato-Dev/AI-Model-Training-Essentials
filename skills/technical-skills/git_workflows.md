---
# Metadata
title: "Git Workflows"
description: "Effective version control practices using Git, including branching strategies, collaboration patterns, and repository management for software teams."
category: "Technical Skills"
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
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial skill creation"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2026-08-10"
reviewed_by: "Technical Skills Team"
next_review: "2027-02-10"

# Classification
tags: [git, version-control, branching-strategies, collaboration, code-review, workflow]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Git Workflows

Effective practices for using Git as a version control system, including branching strategies, collaboration patterns, commit hygiene, and repository management for software teams.

## Overview

Git is the universal tool for version control, but using it well requires more than knowing commands. Teams that adopt Git without agreed-upon workflows end up with tangled histories, broken main branches, merge conflicts that block progress, and release processes that require heroic effort.

A good Git workflow answers four questions for every team member: Where do I branch from? How do I get my changes in? When do I merge? What does the history look like? The answers depend on team size, release cadence, and risk tolerance — but they must be consistent.

This skill covers the most effective Git workflows, when to use each, and the commit practices that keep a repository healthy over months and years of development.

## Core Competencies

- Choosing and implementing a branching strategy appropriate to team size and release cadence
- Writing clear, useful commit messages that explain why, not just what
- Managing pull requests effectively: scope, review, and merge discipline
- Resolving merge conflicts without losing context or introducing bugs
- Keeping repository history clean and navigable (rebase vs. merge decisions)
- Setting up branch protection rules and required checks
- Using Git advanced features: stashing, cherry-picking, bisect, worktrees

## When to Use

- Setting up version control for a new project or team
- Establishing team conventions for branching and merging
- Debugging a complex issue using Git history (bisect, blame, log)
- Preparing a release from a development branch
- Onboarding new team members to the team's Git workflow
- Cleaning up a messy repository history
- Coordinating parallel feature development across multiple team members

## Framework/Methodology

### Phase 1: Branching Strategy

Choose a strategy based on your team's release pattern:

**Trunk-Based Development** (best for: small teams, CI/CD, daily deploys)

```
main ──●──●──●──●──●──●──●──●──→
          \     /   \     /
feature    ●──●      ●──●
```

- Everyone commits to short-lived feature branches from `main`
- Branches live at most 1-2 days before merging
- Feature flags hide incomplete work in production
- Requires strong CI and automated tests

**GitHub Flow** (best for: SaaS teams, weekly deploys)

```
main ──●──────────●──────────●──→
        \         /          /
feature  ●──●──●●    ●──●──●
```

- `main` is always deployable
- Feature branches are created from `main` and merged back via pull request
- No release branches; deploy from `main` after merge
- Simple, lightweight, works for most teams

**Git Flow** (best for: teams with scheduled releases, versioned software)

```
main    ──●────────────────●──────→
           \              /
release    ──●──●──●──●──●
               \      /
develop ──●──●──●──●──●──●──●──→
            \     \      \
feature      ●──●  ●──●   ●──●
```

- `main` reflects production releases (tagged)
- `develop` is the integration branch for features
- Feature branches from `develop`, merge back to `develop`
- Release branches from `develop`, merge to both `main` and `develop`
- Hotfix branches from `main`, merge to both

**Decision guide:**

| Factor | Trunk-Based | GitHub Flow | Git Flow |
|--------|-------------|-------------|----------|
| Team size | 2-10 | 3-30 | 5-50+ |
| Deploy frequency | Daily+ | Weekly | Scheduled releases |
| Complexity | Low | Low | High |
| Requires CI maturity | High | Medium | Low |

### Phase 2: Commit Hygiene

Good commits make history navigable and debugging possible.

**Commit message format:**

```
[type]: Brief description of what changed

Longer explanation of WHY this change was made, if the
reason is not obvious from the diff. Wrap at 72 characters.

Fixes: #123
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `ci`

**Commit size principle:**

- Each commit should be a single logical change
- If you need "and" to describe what the commit does, split it
- A commit should compile and pass tests on its own
- Aim for commits that are reviewable in 5-10 minutes

**Before committing:**

```bash
# Review what you're about to commit
git diff --cached

# Run tests locally
pytest -x

# Check for accidental debug code or secrets
git diff --cached | grep -i "TODO\|FIXME\|password\|api_key"
```

### Phase 3: Pull Request Discipline

Pull requests are the primary collaboration mechanism in modern Git workflows.

**Scope:**
- A PR should represent one logical change
- If the PR description needs "and also" to describe all changes, split it
- Aim for PRs under 400 lines of diff (review quality drops sharply above this)

**Description template:**

```markdown
## What
[Brief description of the change]

## Why
[Business or technical motivation]

## How
[Key implementation decisions, if not obvious from the diff]

## Testing
[How this was tested — unit tests, manual verification, etc.]

## Screenshots
[If UI changes, before/after screenshots]
```

**Review etiquette:**
- Review within one business day of being assigned
- Distinguish between blocking issues (must fix) and suggestions (nice to have)
- Approve when all blocking issues are addressed; don't hold up for style nits
- The author merges after approval, not the reviewer

### Phase 4: Conflict Resolution

When merge conflicts arise:

1. **Pull the latest target branch** into your feature branch locally
2. **Resolve conflicts file by file**, understanding what both sides intended
3. **Run tests** after resolving — conflicts can introduce subtle bugs
4. **Commit the merge** with a clear message if merge commits are used
5. **Push and verify CI passes** before requesting review again

```bash
# Update your feature branch with latest main
git fetch origin
git rebase origin/main
# Resolve conflicts, then:
git add .
git rebase --continue
# Or abort if it gets too complex:
git rebase --abort
```

### Phase 5: History Management

**Rebase vs. merge — when to use each:**

| Action | Use When | Effect |
|--------|----------|--------|
| `git merge` | Preserving full history matters; shared branches | Creates a merge commit; preserves branch topology |
| `git rebase` | Clean linear history; local feature branches | Rewrites commits; makes history look linear |
| Squash merge | Many small commits that aren't useful individually | Single commit on main; detail preserved in PR |

**Golden rule:** Never rebase commits that have been pushed and are shared with others. Rebase is for local, unshared history only.

## Practical Templates

### Template 1: Branch Protection Rules (GitHub)

```yaml
# .github/branch-protection.yml (conceptual)
main:
  required_pull_request_reviews:
    required_approving_review_count: 1
    dismiss_stale_reviews: true
    require_code_owner_reviews: true
  required_status_checks:
    strict: true
    contexts:
      - "ci/tests"
      - "ci/lint"
      - "ci/build"
  enforce_admins: true
  restrictions:
    # Only allow merges via PR, never direct push
    users: []
    teams: []
  required_linear_history: false  # true if using rebase workflow
  required_conversation_resolution: true
```

### Template 2: .gitignore for Python Projects

```gitignore
# Byte-compiled / optimized
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
.venv/
venv/
env/

# Distribution / packaging
dist/
build/
*.egg-info/
*.egg

# IDE
.vscode/
.idea/
*.swp

# Environment variables
.env
.env.local

# Jupyter
.ipynb_checkpoints/

# ML artifacts (adjust paths to your project)
mlruns/
wandb/
*.pth
*.onnx
checkpoints/

# OS
.DS_Store
Thumbs.db
```

### Template 3: Conventional Commits Configuration

```json
// .commitlintrc.json
{
  "extends": ["@commitlint/config-conventional"],
  "rules": {
    "type-enum": [2, "always", [
      "feat", "fix", "docs", "style", "refactor",
      "perf", "test", "build", "ci", "chore", "revert"
    ]],
    "subject-max-length": [2, "always", 72],
    "body-max-line-length": [2, "always", 100],
    "description-min-length": [2, "always", 10]
  }
}
```

## Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Long-lived feature branches | Merge conflicts multiply; integration becomes painful | Keep branches under 2 days; merge small increments |
| Giant pull requests | Reviewers skim, miss bugs; PR sits unreviewed | Scope PRs to one logical change; split if over 400 lines |
| Committing secrets or large files | Security risk; bloated repository | Use pre-commit hooks; add sensitive patterns to .gitignore |
| Rewriting shared history | Breaks other developers' local clones | Never rebase or force-push to shared branches |
| Vague commit messages ("fix", "update", "wip") | History becomes useless for debugging | Follow conventional commit format; explain the "why" |
| Merging without running tests locally | CI failures block the team; wasted time | Always run relevant tests before pushing |

## Best Practices

1. **Branch from the latest target branch.** Before creating a feature branch, pull the latest `main` or `develop` to minimize conflicts later.
2. **Delete branches after merging.** Stale branches clutter the repository and cause confusion about what's still active.
3. **Use signed commits for important repositories.** `git config commit.gpgsign true` adds a cryptographic signature proving the commit came from you.
4. **Set up pre-commit hooks.** Automate linting, formatting, and secret detection before commits reach the repository.
5. **Write the PR description for the reviewer.** They don't have your context. Explain what changed and why in the PR body, not just the title.
6. **Use `git bisect` for regression hunting.** When something broke and you don't know when, bisect finds the exact commit in O(log n) steps.
7. **Tag releases semantically.** Use annotated tags (`git tag -a v1.2.0 -m "Release 1.2.0"`) with semantic versioning for every production release.

## Tools & Resources

- [Pro Git Book](https://git-scm.com/book/en/v2) - Free comprehensive Git reference
- [Conventional Commits](https://www.conventionalcommits.org/) - Specification for structured commit messages
- [semantic-release](https://github.com/semantic-release/semantic-release) - Automated versioning and package publishing based on commit messages
- [pre-commit](https://pre-commit.com/) - Framework for managing Git pre-commit hooks
- [GitFlow cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/) - Visual reference for Git Flow branching model
- [Oh Shit, Git!?!](https://ohshitgit.com/) - Plain-English recovery recipes for common Git mistakes
- [Trunk Based Development](https://trunkbaseddevelopment.com/) - Comprehensive guide to trunk-based workflows

## Example Application

**Scenario**: A team of 6 developers shares a repository. The `main` branch is frequently broken because people merge large, unreviewed PRs directly. Feature branches live for weeks, creating massive merge conflicts. No one trusts the Git history because commit messages say "fix stuff" and "update."

**Application**:

1. *Workflow adoption* — The team agrees on GitHub Flow: `main` is always deployable, all changes go through PRs, branches live at most 2 days. They document this in `CONTRIBUTING.md`.

2. *Branch protection* — They enable branch protection on `main`: requires 1 approving review, requires passing CI, prevents force pushes. No one can bypass the process.

3. *Commit conventions* — They adopt Conventional Commits with a `commitlint` hook. Commit messages now follow `feat:`, `fix:`, `docs:` format. The team agrees that "if you can't describe the commit in one clear sentence, the change is too big."

4. *PR size discipline* — They set a team norm: PRs should be under 400 lines of diff. If a feature requires more, it's split into sequential PRs that each build on the previous. Review turnaround is committed to: under 1 business day.

5. *History cleanup* — They enable squash-merging for feature branches. The `main` branch history becomes a clean sequence of meaningful, single-commit changes. The detailed discussion lives in the PR.

6. *Recovery tooling* — They add `git bisect` and `git reflog` to the team's shared knowledge. When a regression appears, anyone can find the exact commit in minutes instead of hours.

**Outcome**: Within one month, `main` breakages drop from 3 per week to 0. PR review time drops from 2 days average to under 1 day. The team can use `git log` to understand why changes were made, and `git bisect` to find regressions in under 5 minutes. New hires report that the contribution process is clear from day one.

## Success Indicators

You know you've mastered Git workflows when:

- Your team follows a consistent branching strategy that everyone can explain in one sentence
- `main` is always deployable and rarely broken
- Commit messages explain the "why" and follow a consistent format
- Pull requests are small, well-described, and reviewed within one business day
- You can find any past change using `git log`, `git blame`, or `git bisect` in under 5 minutes
- Merge conflicts are rare because branches are short-lived and integrated frequently
- New team members understand the workflow from reading `CONTRIBUTING.md` alone

## Related Skills

- [Programming Fundamentals](programming_fundamentals.md) - Version control is foundational to all software development
- [Code Review](../collaboration-skills/code_review.md) - Pull request discipline and code review are tightly coupled practices
- [Team Collaboration](../collaboration-skills/team_collaboration.md) - Git workflows are the structural backbone of async team collaboration
- [CI/CD](../devops-skills/ci_cd.md) - Branch protection and required checks connect Git workflow to deployment automation
