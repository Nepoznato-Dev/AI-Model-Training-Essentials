# Poor Commit Messages

## Overview

Poor commit messages make it difficult to understand project history, debug issues, and collaborate effectively. This document catalogs common commit message anti-patterns and provides guidelines for writing clear, useful commit messages.

## Anti-Patterns

### Vague One-Word Messages

**Bad Examples:**
```bash
git commit -m "fix"
git commit -m "update"
git commit -m "change"
git commit -m "improve"
git commit -m "refactor"
git commit -m "cleanup"
git commit -m "stuff"
git commit -m "things"
```

**Why It's Bad:**
- No information about what was fixed/updated/changed
- Useless for searching history
- Provides no context for code review
- Makes `git blame` investigations impossible

**Better Approach:**
```bash
git commit -m "fix: resolve null pointer exception in user service"
git commit -m "update: bump lodash to 4.17.21 for security patch"
git commit -m "change: replace sync file operations with async"
git commit -m "improve: reduce API response time by 40%"
git commit -m "refactor: extract validation logic to separate module"
git commit -m "cleanup: remove unused import statements"
```

### WIP Commits Left in History

**Bad Examples:**
```bash
git commit -m "WIP"
git commit -m "wip"
git commit -m "Work in progress"
git commit -m "TODO: finish this later"
git commit -m "almost done"
git commit -m "getting there"
```

**Why It's Bad:**
- Clutters history with incomplete work
- No indication of what the WIP contains
- Should be squashed before merging
- Unprofessional in shared repositories

**Better Approach:**
```bash
# Option 1: Don't push WIP commits
git add .
git stash  # Save work locally without committing

# Option 2: Squash before merging
git rebase -i main  # Squash WIP commits into one

# Option 3: Use descriptive progress commits
git commit -m "feat(auth): implement login form UI"
git commit -m "feat(auth): add form validation"
git commit -m "feat(auth): connect to authentication API"
```

### Joke or Unprofessional Messages

**Bad Examples:**
```bash
git commit -m "asdfasdf"
git commit -m "idk lol"
git commit -m "it works somehow"
git commit -m "pray this works"
git commit -m "hacky fix but whatever"
git commit -m "monday commits"
git commit -m "why is this so hard"
git commit -m "final final final really"
```

**Why It's Bad:**
- Unprofessional and disrespectful to team
- Zero informational value
- Creates negative team culture
- Embarrassing in open source projects

**Better Approach:**
```bash
git commit -m "fix: workaround for race condition in cache layer"
git commit -m "fix: add error handling for edge case in parser"
git commit -m "refactor: simplify complex conditional logic"
```

### Overly Long Rambling Messages

**Bad Example:**
```bash
git commit -m "Okay so I was working on this thing and at first I thought 
it would be easy but then I ran into this weird bug where the database 
was returning null values even though I swear I inserted them correctly 
and after like 3 hours I realized I was querying the wrong table which 
is embarrassing but anyway I fixed it and also while I was here I 
changed some other stuff that probably should have been a separate 
commit but I'm too tired now and also updated the README because it 
was out of date and added a TODO for something I'll do later maybe"
```

**Why It's Bad:**
- Important information buried in noise
- Difficult to scan quickly
- Multiple changes should be separate commits
- Unprofessional tone

**Better Approach:**
```bash
git commit -m "fix: correct database query to use users table

Was accidentally querying user_backup table instead of users.
Added validation to prevent similar mistakes in future.

Also updated README with correct setup instructions."
```

### Missing Context for Breaking Changes

**Bad Examples:**
```bash
git commit -m "update API"
git commit -m "change config format"
git commit -m "remove old methods"
git commit -m "database migration"
```

**Why It's Bad:**
- Breaking changes not clearly indicated
- Team members unaware of migration needs
- Can break production deployments
- No migration instructions provided

**Better Approach:**
```bash
git commit -m "BREAKING CHANGE: update user API response format

Changes:
- Removed 'fullName' field (use 'firstName' + 'lastName')
- Changed 'age' from number to string
- Renamed 'email' to 'primaryEmail'

Migration:
- Update frontend to concatenate firstName and lastName
- Parse age as integer if needed
- Update email references to primaryEmail

See MIGRATION.md for detailed guide.
Closes #234"
```

### Commit Message Format Issues

**Bad Structure:**
```bash
# Missing subject line
git commit -m "
This commit fixes several bugs in the authentication system
including the token expiration issue and the password reset
flow problem.
"

# Subject line too long
git commit -m "Fixed the bug in the authentication module where the JWT tokens were not being properly validated causing users to be logged out unexpectedly"

# No body for complex changes
git commit -m "Refactor entire payment processing system"
```

**Better Structure:**
```bash
# Proper format with subject and body
git commit -m "fix: resolve JWT token validation issue

Tokens were being rejected due to incorrect issuer validation.
Updated to use correct issuer URL from environment config.

Fixes #567"
```

## Best Practices

### Conventional Commits Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature (triggers minor version)
- `fix`: Bug fix (triggers patch version)
- `docs`: Documentation only
- `style`: Formatting, missing semi-colons, etc.
- `refactor`: Code change that neither fixes nor adds features
- `perf`: Performance improvement
- `test`: Adding or correcting tests
- `chore`: Changes to build process or tools
- `ci`: CI configuration changes
- `build`: Build system or external dependencies
- `revert`: Reverts previous commit

**Examples:**
```bash
feat(auth): add OAuth2 Google authentication

Implement Google OAuth2 flow for user sign-in.
- Add Google OAuth client configuration
- Create callback handler endpoint
- Update user model for OAuth tokens
- Add integration tests

Closes #123

---

fix(payment): handle declined card errors gracefully

Display user-friendly error message when card is declined.
Previously showed generic server error.

Fixes #456

---

BREAKING CHANGE: api: v2 user endpoint changes

Removed fields: fullName, age
Added fields: firstName, lastName, birthDate

Migration guide available in docs/MIGRATION-v2.md
```

### Subject Line Guidelines

```bash
# DO: Use imperative mood
git commit -m "fix: resolve memory leak in cache"
# NOT: "fixed" or "fixes"

# DO: Keep under 50 characters
git commit -m "feat: add user profile page"

# DO: Capitalize first letter
git commit -m "Fix authentication bug"
# NOT: "fix authentication bug"

# DO: No period at end
git commit -m "Update documentation"
# NOT: "Update documentation."
```

### Body Guidelines

```bash
# DO: Explain WHAT and WHY, not HOW
git commit -m "fix: increase timeout for slow queries

Production database occasionally takes >5s for complex joins.
Increasing timeout prevents premature request failures.
"

# DO: Wrap at 72 characters
# DO: Reference issues and PRs
# DO: Include migration steps for breaking changes
```

## Testing Checklist

- [ ] Subject line under 50 characters
- [ ] Uses imperative mood ("fix" not "fixed")
- [ ] First letter capitalized
- [ ] No period at end of subject
- [ ] Body explains why, not just what
- [ ] Breaking changes clearly marked
- [ ] Related issues referenced
- [ ] No WIP commits in main branch
- [ ] Follows team convention consistently
- [ ] Spell-checked and professional tone

## Related Documents

- [[bad_git_history]] - Overall Git history best practices
- [[poor_documentation]] - Documentation standards
- [[code_smells]] - Code quality indicators
- [[bad_variable_names]] - Naming conventions
