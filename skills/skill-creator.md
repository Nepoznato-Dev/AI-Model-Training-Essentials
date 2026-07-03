# Skill Creator Guide

A comprehensive guide for creating, structuring, and documenting new skills within this repository. This document serves as the meta-skill for skill development.

## Overview

The Skill Creator framework provides a standardized approach to documenting capabilities, ensuring consistency, reusability, and clarity across all skill definitions.

## Core Principles

### 1. Consistency
- Follow the established directory structure
- Use markdown (.md) as the primary format
- Adhere to the standard skill template
- Maintain uniform naming conventions (snake_case)

### 2. Completeness
- Include all required sections
- Provide practical examples
- Document common pitfalls
- List relevant tools and resources

### 3. Clarity
- Write in clear, actionable language
- Use visual aids (diagrams, tables) where helpful
- Avoid unnecessary jargon
- Define technical terms when first used

### 4. Reusability
- Design skills to be composable
- Create modular components
- Enable cross-referencing between skills
- Build upon existing skills

## Directory Structure

```
skills/
├── behavior-skills/          # Cognitive and workflow skills
│   ├── brainstorming.md
│   ├── debugging.md
│   └── ...
├── designing-skills/         # Design and architecture skills
│   ├── ui_ux_design.md
│   ├── system_architecture.md
│   └── ...
├── speaking-skills/          # Communication and presentation skills
│   ├── public_speaking.md
│   ├── technical_presentation.md
│   └── ...
├── research-skills/          # Information gathering and analysis
│   ├── information_retrieval.md
│   └── ...
├── collaboration-skills/     # Teamwork and coordination
│   ├── team_collaboration.md
│   ├── code_review.md
│   └── ...
└── skill-creator.md          # This file
```

## Standard Skill Template

Every skill document should follow this structure:

```markdown
# [Skill Name]

[Brief one-sentence description of the skill]

## Overview

[2-3 paragraphs explaining what the skill is, why it matters, and when to use it]

## Core Competencies

List the key abilities that make up this skill:
- Competency 1
- Competency 2
- Competency 3

## Framework/Methodology

### Phase 1: [Name]
[Description and steps]

### Phase 2: [Name]
[Description and steps]

### Phase 3: [Name]
[Description and steps]

## Practical Templates

### Template 1: [Use Case]
```
[Ready-to-use template]
```

### Template 2: [Use Case]
```
[Ready-to-use template]
```

## Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| [Description] | [Consequence] | [Solution] |

## Best Practices

1. **Practice 1**: Description
2. **Practice 2**: Description
3. **Practice 3**: Description

## Tools & Resources

- [Tool/Resource 1](link) - Brief description
- [Tool/Resource 2](link) - Brief description

## Example Application

**Scenario**: [Describe a realistic situation]

**Application**: [Show how the skill is applied step-by-step]

**Outcome**: [Describe the positive result]

## Success Indicators

You know you've mastered this skill when:
- ✓ [Indicator 1]
- ✓ [Indicator 2]
- ✓ [Indicator 3]

## Related Skills

- [[Related Skill 1]](path/to/skill.md)
- [[Related Skill 2]](path/to/skill.md)
```

## Writing Process

### Step 1: Identify the Skill
- What capability are we documenting?
- Is it distinct from existing skills?
- Does it have clear boundaries?

### Step 2: Research & Analysis
- Gather best practices from industry
- Review existing frameworks
- Identify common patterns
- Collect real-world examples

### Step 3: Structure the Content
- Outline the main sections
- Determine the framework/methodology
- Identify templates needed
- Plan examples and scenarios

### Step 4: Draft the Content
- Write following the standard template
- Include practical, actionable guidance
- Add visual elements where helpful
- Reference related skills

### Step 5: Review & Refine
- Check for completeness
- Verify accuracy
- Ensure clarity
- Test templates with examples

### Step 6: Validate
- Can someone use this skill immediately?
- Are the examples realistic?
- Is the formatting consistent?
- Do links work correctly?

## Naming Conventions

### File Names
- Use snake_case: `skill_name.md`
- Be descriptive but concise
- Avoid abbreviations unless universally known
- Match the skill's primary focus

### Section Headers
- Use Title Case for main headers
- Use sentence case for subheaders
- Keep hierarchy clear (##, ###, ####)

### Cross-References
- Use relative paths: `[[Skill Name]](path/to/file.md)`
- Link to related skills consistently
- Update links if files move

## Quality Checklist

Before submitting a new skill, verify:

- [ ] Follows standard template structure
- [ ] Contains all required sections
- [ ] Includes at least 2 practical templates
- [ ] Lists 3+ common pitfalls with solutions
- [ ] Provides 3+ best practices
- [ ] Includes 5+ tools/resources
- [ ] Contains at least 1 detailed example
- [ ] Lists 3+ success indicators
- [ ] Links to 2+ related skills
- [ ] Uses consistent formatting
- [ ] No broken links
- [ ] Clear, actionable language
- [ ] Appropriate for target audience

## Extending the Framework

### Adding New Categories

When a skill doesn't fit existing categories:

1. Create new directory: `mkdir skills/new-category-skills`
2. Add README.md to the category explaining its focus
3. Document the category in this guide
4. Ensure at least 3 skills justify the new category

### Creating Skill Variants

For specialized versions of existing skills:

1. Keep the core skill general
2. Create variant with suffix: `skill_name_variant.md`
3. Link variant from the main skill
4. Document when to use each variant

## Multi-Format Output

While skills are authored in Markdown, they can be exported to various formats for different use cases. See the **Formatter Skill** in `speaking-skills/formatting.md` for detailed instructions on converting skills to:

- Plain text (.txt)
- Word documents (.doc, .docx)
- Rich Text Format (.rtf)
- Apple Pages (.pages)
- CSV (.csv)
- JSON (.json)
- XML (.xml)
- SDF (.sdf)
- Excel spreadsheets (.xlsx)

## Version Control

### Skill Versioning
- Add version number in frontmatter if needed
- Track major changes in a changelog section
- Use git tags for significant updates

### Change Documentation
```markdown
## Changelog

### v1.1.0 (YYYY-MM-DD)
- Added: New template for X
- Updated: Expanded best practices section
- Fixed: Corrected example in Phase 2

### v1.0.0 (YYYY-MM-DD)
- Initial release
```

## Collaboration Guidelines

### Contributing New Skills
1. Create issue proposing the new skill
2. Get feedback on scope and structure
3. Create feature branch
4. Draft the skill document
5. Submit pull request
6. Address review feedback
7. Merge to main

### Updating Existing Skills
1. Identify needed improvements
2. Create issue describing changes
3. Update the skill document
4. Submit pull request
5. Get approval from maintainers

## Inspiration Sources

When developing new skills, consider:

- Industry best practices
- Academic research
- Open-source projects (e.g., addyosmani/agent-skills, NVIDIA/skills)
- Professional certifications
- Expert interviews
- Community feedback
- Real-world case studies

## Continuous Improvement

Skills should evolve based on:
- User feedback
- Changing industry practices
- New tools and technologies
- Effectiveness metrics
- Emerging patterns

Schedule regular reviews:
- Quarterly: Minor updates and corrections
- Annually: Major revisions and restructuring
- As needed: Emergency fixes for critical issues

## Getting Started

To create your first skill:

1. Read this guide completely
2. Study 2-3 existing skills as examples
3. Identify a gap or need
4. Create an issue proposing your skill
5. Follow the writing process outlined above
6. Submit for review

Remember: The goal is to create practical, actionable skills that help developers improve their capabilities immediately.

---

*This guide itself is a living document. Suggest improvements by submitting issues or pull requests.*