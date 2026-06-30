# AI-Model-Training-Essentials

A comprehensive knowledge base and configuration repository for AI agents, providing structured knowledge files, skill definitions, and agent mode configurations.

## 📁 Repository Structure

```
/workspace
├── knowledge_base/       # Language-specific knowledge files organized by topic
│   └── English/         # English language knowledge base
│       ├── 01_technology_and_computing/
│       ├── 02_artificial_intelligence/
│       ├── 03_data_science/
│       ├── 04_science/
│       ├── 05_business_and_finance/
│       ├── 06_humanities/
│       ├── 07_reference/
│       ├── 08_future/
│       ├── 09_practical_skills/    ← NEW
│       ├── 10_cheat_sheets/
│       ├── 11_case_studies/        ← NEW (coming soon)
│       └── 12_interview_prep/      ← NEW (coming soon)
├── skills/               # AI agent skill definitions
├── agent_modes/          # Agent mode configurations
└── README.md             # This file
```

## 🚀 Quick Start

### For AI Agents
1. Select your agent mode from `agent_modes/`
2. Load relevant skills from `skills/`
3. Reference knowledge from `knowledge_base/{language}/`

### For Humans
1. Browse by topic in your preferred language
2. Use cheat sheets for quick reference
3. Follow practical skills guides for professional development

## 📊 Repository Stats

| Metric | Count |
|--------|-------|
| Languages | 12 |
| Knowledge Categories | 10+ |
| Knowledge Files | 50+ |
| Skill Documents | 30+ |
| Agent Modes | 5 |

## 🔍 How to Find Information

- **By topic**: Browse category folders (01_, 02_, etc.)
- **By language**: Go to `knowledge_base/{language}/`
- **Quick refs**: Check `10_cheat_sheets/`
- **Skills**: See `skills/{category}-skills/`
- **Practical skills**: New `09_practical_skills/` directory

---

## 📚 Contents

### English/ — Knowledge Base

Domain-specific knowledge files covering a wide range of topics:

#### Technology & Computing (01)
| File | Description |
|------|-------------|
| cloud_architecture.md | Cloud computing fundamentals and patterns |
| coding_languages.md | Programming languages and development concepts |
| database_systems.md | Database technologies and design |
| networking_basics.md | Network fundamentals and protocols |
| web_development.md | Web technologies and frameworks |

#### Artificial Intelligence (02)
| File | Description |
|------|-------------|
| artificial_intelligence.md | AI fundamentals, history, machine learning |
| local_ai_architecture.md | Local AI system architecture |
| ml_evaluation_and_workflow.md | ML model evaluation and workflows |
| phi3_and_local_models.md | Phi3 and local model information |
| prompt_engineering.md | Prompt design and optimization techniques |

#### Data Science (03), Science (04), Business (05), Humanities (06)
See individual category directories for complete listings.

#### Practical Skills (09) ← NEW
| File | Description |
|------|-------------|
| research_methods.md | Research methodologies and frameworks |
| critical_thinking.md | Critical thinking and logical reasoning |
| technical_writing.md | Technical documentation best practices |
| presentation_skills.md | Presentation design and delivery |
| career_development.md | Career growth strategies |
| problem_solving.md | Systematic problem-solving approaches |
| time_management.md | Productivity and time management |

#### Reference (07) & Cheat Sheets (10)
Quick reference materials and condensed guides.

---

### skills/ — Agent Skills

Skill definitions that enable AI agents to perform specific tasks:

#### Behavior Skills (`behavior-skills/`)
- brainstorming.md — Idea generation techniques
- debugging.md — Code debugging strategies
- explanation.md — Clear explanation methods
- learning.md — Learning and adaptation approaches
- planning.md — Task planning methodologies
- style_adaptation.md — Communication style adjustments
- summarization.md — Content summarization techniques
- teaching.md — Teaching and instruction methods

#### Design Skills (`designing-skills/`)
- api_design.md — API design principles
- system_architecture.md — System architecture patterns
- ui_ux_design.md — UI/UX design guidelines

#### Speaking Skills (`speaking-skills/`)
- text_formatting.md — Text formatting standards
- public_speaking.md — Public speaking techniques
- technical_presentation.md — Technical presentation skills

#### Writing & Creation
- writing-knowledge.md — Writing best practices
- skill-creator.md — Skill creation guidelines

---

### agent_modes/ — Agent Configurations

Pre-configured agent modes for different interaction patterns:

| Mode | Description |
|------|-------------|
| Agent.Agent.md | Full coding agent for research, planning, editing, testing |
| Ask.Agent.md | Question-answering mode for direct queries |
| Explore.Agent.md | Exploration mode for discovering and investigating topics |
| Plan.Agent.md | Planning mode for structured task breakdown |
| Review.Agent.md | Review mode for code and content analysis |

---

## 🛠️ Usage

### For AI Agents

1. **Knowledge Retrieval**: Reference relevant `.md` files based on the topic domain
2. **Skill Activation**: Load appropriate skills based on task requirements
3. **Mode Selection**: Choose the appropriate agent mode based on interaction type

### For Contributors

1. **Adding Knowledge**: Create new `.md` files following the existing format
2. **Adding Skills**: Add new skill files in the appropriate subdirectory
3. **Adding Agent Modes**: Create new agent configurations with proper YAML frontmatter

---

## 📝 File Format

Knowledge files use Markdown format with clear section headers:

```markdown
# Topic Title

## Section Name

Content goes here...

## Another Section

More content...
```

Agent mode files use YAML frontmatter for configuration:

```yaml
---
name: ModeName
description: What this mode does
target: vscode
tools: ['list', 'of', 'tools']
---
```

---

## 🎯 Purpose

This repository serves as:
- A structured knowledge base for AI agents to reference during interactions
- A skill library for enhancing agent capabilities
- A configuration hub for different agent operational modes
- A maintainable and extensible framework for AI agent development
- A learning resource for humans seeking to improve technical and professional skills

---

## 🗺️ Roadmap

### Q3 2025
- [x] Complete 09_practical_skills/ directory
- [ ] Add 20+ new technical skill documents
- [ ] Implement automated link checking

### Q4 2025
- [ ] Add Italian, Dutch language support
- [ ] Create interactive learning paths
- [ ] Build search functionality

---

## 📄 License
