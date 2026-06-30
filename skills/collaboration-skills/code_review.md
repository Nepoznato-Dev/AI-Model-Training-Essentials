# Code Review Skill

## Overview
The ability to effectively review others' code and have your code reviewed, focusing on improving quality, sharing knowledge, and maintaining team standards.

## Core Competencies

### 1. Technical Evaluation
- **Correctness**: Does the code work as intended?
- **Efficiency**: Is performance acceptable for the use case?
- **Security**: Are there vulnerabilities or risks?
- **Scalability**: Will it handle growth appropriately?
- **Testing**: Is functionality adequately tested?

### 2. Code Quality Assessment
- **Readability**: Can others understand it easily?
- **Maintainability**: Is it easy to modify and extend?
- **Consistency**: Does it follow team conventions?
- **Simplicity**: Is it unnecessarily complex?
- **Documentation**: Is intent clear through comments/docs?

### 3. Communication Skills
- **Constructive Feedback**: Critique code, not the person
- **Clarity**: Be specific about issues and suggestions
- **Tone**: Maintain respectful, supportive language
- **Prioritization**: Distinguish critical vs. nice-to-have
- **Discussion Management**: Know when to take offline

### 4. Review Process Management
- **Timeliness**: Review within agreed SLAs
- **Thoroughness**: Balance depth with velocity
- **Scope Management**: Keep PRs focused and reasonable
- **Follow-up**: Ensure feedback is addressed
- **Approval Judgment**: Know when to approve vs. request changes

## Frameworks & Methods

### Review Priority Levels
```
🔴 BLOCKER - Must fix before merge
   - Security vulnerabilities
   - Data loss potential
   - Breaking existing functionality
   - Major performance issues

🟡 IMPORTANT - Should fix, discuss if delaying
   - Code quality issues
   - Missing tests for critical paths
   - Potential bugs
   - Violation of team standards

🟢 SUGGESTION - Nice to have, don't block
   - Naming improvements
   - Refactoring opportunities
   - Additional test coverage
   - Documentation enhancements
```

### The Review Checklist
```markdown
## Functionality
- [ ] Code does what it's supposed to do
- [ ] Edge cases handled
- [ ] Error handling appropriate
- [ ] No logic errors

## Testing
- [ ] Tests cover happy path
- [ ] Tests cover edge cases
- [ ] Tests are meaningful (not just for coverage)
- [ ] Tests pass consistently

## Security
- [ ] No hardcoded secrets
- [ ] Input validation present
- [ ] SQL injection prevented
- [ ] XSS/CSRF protections in place
- [ ] Authentication/authorization correct

## Performance
- [ ] No obvious inefficiencies
- [ ] Database queries optimized
- [ ] No N+1 queries
- [ ] Caching used appropriately

## Code Quality
- [ ] Follows style guide
- [ ] Functions are focused (single responsibility)
- [ ] Variable/function names are clear
- [ ] No code duplication
- [ ] Complexity is reasonable

## Maintainability
- [ ] Dependencies are justified
- [ ] Configuration is externalized
- [ ] Logging is adequate
- [ ] Monitoring considerations addressed
```

### Feedback Phrases That Work

#### For Critical Issues
✅ "This could cause [specific problem]. Consider [solution]."
✅ "I'm concerned about [issue] because [reason]."
✅ "Let's make sure we handle [edge case] here."

#### For Suggestions
✅ "Have you considered [alternative approach]?"
✅ "What do you think about [suggestion]?"
✅ "Minor nit: [issue] - feel free to ignore if you disagree."

#### For Positive Reinforcement
✅ "Great solution for [problem]!"
✅ "I like how you handled [specific aspect]."
✅ "This test case is really thorough, nice work!"

#### When You Need Clarification
✅ "Can you help me understand the reasoning behind...?"
✅ "I'm not familiar with this pattern, can you explain...?"
✅ "What was the motivation for choosing this approach?"

## Practical Templates

### Pull Request Template
```markdown
## Description
[Brief description of what this PR does]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Refactoring
- [ ] Documentation update

## Testing Done
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing performed
- [ ] Test evidence (screenshots/logs): 

## Checklist
- [ ] Code follows team style guidelines
- [ ] Self-review completed
- [ ] Comments added where necessary
- [ ] Documentation updated
- [ ] No new warnings introduced

## Related Issues
Closes #[issue number]

## Deployment Notes
[Any special deployment considerations]

## Screenshots (if UI changes)
[Before/After images]
```

### Code Review Response Template
```markdown
## Reviewer: [Name]
## PR: [Link]
## Review Date: [Date]

### ✅ What Works Well
1. 
2. 

### 🔴 Blockers (Must Fix)
| Location | Issue | Suggestion |
|----------|-------|------------|
| Line 45  |       |            |

### 🟡 Important (Should Fix)
| Location | Issue | Suggestion |
|----------|-------|------------|
|          |       |            |

### 🟢 Suggestions (Optional)
| Location | Issue | Suggestion |
|----------|-------|------------|
|          |       |            |

### ❓ Questions
1. 

### Overall Status
- [ ] Approved - Ready to merge
- [ ] Approved with minor nits (non-blocking)
- [ ] Changes requested - Please address blockers
- [ ] Needs significant revision - Let's discuss

### Next Steps
[Specific actions needed before approval]
```

### Review Turnaround Guidelines
```markdown
## SLA Expectations
- Standard PRs: Within 24 hours
- Urgent/Hotfix: Within 4 hours
- Large PRs (>500 lines): Within 48 hours with initial feedback

## If You Can't Review Fully
- Acknowledge receipt: "Got this, will review by [time]"
- Provide partial feedback if possible
- Request extension if needed: "Need more time for thorough review"

## Author Responsibilities
- Respond to all comments (even if just "done" or "disagree because...")
- Make requested changes promptly
- Re-request review after addressing feedback
- Keep PR size reasonable (<400 lines ideal)
```

## Common Pitfalls

### ❌ What to Avoid

#### As a Reviewer
- Nitpicking without considering trade-offs
- Requiring changes that are purely personal preference
- Reviewing for style when linters exist
- Delaying reviews without communication
- Leaving vague comments ("this seems wrong")
- Making it personal ("you always...")
- Approving without actually reviewing
- Bikeshedding on minor details

#### As an Author
- Getting defensive about feedback
- Arguing without providing reasoning
- Making unrelated changes in same PR
- Expecting immediate review
- Submitting broken builds for review
- Not responding to comments
- Taking feedback personally

### ✅ Best Practices

#### As a Reviewer
- Start with something positive
- Explain the "why" behind suggestions
- Use questions when uncertain
- Batch similar comments together
- Approve promptly when ready
- Offer to pair on complex fixes
- Recognize good solutions

#### As an Author
- Self-review before requesting review
- Write clear PR descriptions
- Keep changes focused on one concern
- Respond to every comment
- Explain your reasoning when disagreeing
- Say thank you for thorough reviews
- Learn from recurring feedback

## Tools & Resources

### Review Platforms
- **GitHub**: Pull requests with inline comments
- **GitLab**: Merge requests with threaded discussions
- **Bitbucket**: Code review with tasks
- **Phabricator**: Advanced review workflows
- **Gerrit**: Patch-based review system

### Automation Tools
- **Linters**: ESLint, Pylint, RuboCop, etc.
- **Formatters**: Prettier, Black, gofmt
- **Static Analysis**: SonarQube, CodeClimate
- **Security Scanning**: Snyk, Dependabot, GitHub Security
- **Test Coverage**: Coveralls,Codecov

### Best Practice Guides
- Google's Engineering Practices documentation
- Atlassian's Code Review Best Practices
- Microsoft's Engineering System guidelines
- "Effective Code Review" by SmartBear

## Example Application

### Scenario: Reviewing a Database Migration PR

**Context:**
PR adds new `user_preferences` table with migration

**Review Focus Areas:**

1. **Migration Safety**
   - Is it reversible (has down migration)?
   - Will it lock the table during deploy?
   - Is data backfill needed? How long will it take?

2. **Schema Design**
   - Are columns appropriately typed?
   - Are indexes included for common queries?
   - Are constraints defined (NOT NULL, unique)?
   - Is naming consistent with existing tables?

3. **Model Layer**
   - Are validations in place?
   - Are associations defined correctly?
   - Are factory/test helpers updated?

4. **Sample Review Comments:**

```
🔴 BLOCKER - Line 23
The `settings` column is JSON but has no validation. 
Consider using a structured type or adding application-level 
validation to prevent malformed data.

🟡 IMPORTANT - Line 45
This index on `created_at` might not be necessary unless 
we're querying by date range frequently. Can you share 
the query patterns that need this?

🟢 SUGGESTION - Line 12
Consider naming this `preference_key` instead of just `key` 
for consistency with our other config tables.

✅ POSITIVE
Great job including the rollback migration! The test 
coverage for edge cases is thorough.
```

## Success Indicators
- Bug detection rate improves over time
- Knowledge spreads across team
- Code consistency increases
- Junior developers grow faster
- Fewer production incidents from new code
- Review cycle time decreases
- Team trust and psychological safety improve
- Positive feedback about review culture
