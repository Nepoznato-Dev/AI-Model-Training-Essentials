# Repository Guide

This page explains how the repository is organized and where to add or find content. Use the [Wiki home](README.md) for engineering topics, learning paths, and reference material.

## Choose a Starting Point

| Goal | Start here |
|------|------------|
| Learn AI engineering concepts | [Learning paths](learning_paths/beginner.md) |
| Build a working project | [Runnable projects](../guides/projects/README.md) |
| Study a model family | [Guides](../guides/README.md) |
| Retrieve general knowledge | [Knowledge base](../knowledge_base/README.md) |
| Give an AI agent reusable behavior | [Skills library](../skills/README.md) |
| Configure an interaction mode | [Agent modes](../agent_modes/) |

## Repository Map

| Directory | Purpose | More information |
|-----------|---------|------------------|
| `guides/` | In-depth AI training material, prerequisites, errors, and runnable projects | [Guides README](../guides/README.md) |
| `knowledge_base/` | Topic-oriented reference content in multiple languages | [Knowledge base README](../knowledge_base/README.md) |
| `skills/` | Modular behavior, collaboration, design, research, and technical skills | [Skills README](../skills/README.md) |
| `wiki/` | Curated engineering documentation and navigation | [Wiki home](README.md) |
| `agent_modes/` | Ready-to-use agent behavior configurations | [Agent modes](../agent_modes/) |

## Knowledge Base Organization

The English knowledge base is grouped into technology and computing, artificial intelligence, data science, science, business and finance, humanities, reference, future topics, failure examples, and cheat sheets. Each language directory follows the same topic-oriented approach where translations are available.

Use the knowledge base for focused reference material. Use the guides when you need a sequence of explanations, exercises, or a runnable implementation.

## Skills and Agent Modes

Skills are reusable capability descriptions. Agent modes combine a task style with tools and behavioral instructions. When adding one:

1. Choose the closest existing category.
2. Follow the local README and neighboring file format.
3. Include purpose, capabilities, usage examples, and limitations where relevant.
4. Add the new file to the appropriate directory README.

See [skill creation guidance](../skills/skill-creator.md) and the existing [agent modes](../agent_modes/).

## Adding Documentation

### Knowledge or guide pages

Use a descriptive filename, begin with one level-one heading, and include an overview, clearly grouped sections, practical examples, and related resources. Link to nearby material instead of duplicating it.

### Wiki pages

Wiki pages should answer one coherent question or support one workflow. Add the page to [wiki/README.md](README.md), link back to the relevant guide or repository directory, and keep setup commands synchronized with the project they describe.

### Agent mode files

Agent modes use YAML frontmatter followed by Markdown instructions:

```markdown
---
name: ModeName
description: What this mode does
tools: ['tool-name']
---

# Mode Instructions

Describe the behavior, workflow, and boundaries for the mode.
```

### Markdown checklist

- Links point to existing files and use paths relative to the current page.
- Commands work from the directory stated in the instructions.
- Examples are concise and tested when they are executable.
- New pages are linked from the nearest README or index.
- Content is not copied into multiple locations without a reason.

## Related Resources

- [Main README](../README.md) - concise project overview and quick start
- [Contributing guide](../CONTRIBUTING.md) - contribution and pull request expectations
- [Wiki home](README.md) - engineering topics and navigation