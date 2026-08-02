# AI-Model-Training-Essentials

> 🌍 **Multilingual Knowledge Base & AI Agent Configuration Repository. For small local models**


[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Languages](https://img.shields.io/badge/languages-20-multicolor)](knowledge_base/)
[![Knowledge Files](https://img.shields.io/badge/knowledge_files-52+-green)](knowledge_base/English/)
[![Skills](https://img.shields.io/badge/skills-50+-orange)](skills/)
[![Projects](https://img.shields.io/badge/projects-runnable-lightgrey)](guides/projects/)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Repository Structure](#-repository-structure)
- [Quick Start for Beginners](#-quick-start-for-beginners)
- [Knowledge Base](#-knowledge-base)
- [Skills Library](#-skills-library)
- [Runnable Projects](#-runnable-projects)
- [Common Errors](#-common-errors)
- [Agent Modes](#-agent-modes)
- [Multi-Language Support](#-multi-language-support)
- [Usage Guide](#-usage-guide)
- [Contributing](#-contributing)
- [File Formats](#-file-formats)
- [License](#-license)

---

## 🎯 Overview

This repository serves as a foundational framework for AI agent development, providing:

- **Structured Knowledge**: 52+ domain-specific knowledge files organized by category
- **Skill Definitions**: 50+ skill modules covering behavior, design, communication, and technical capabilities
- **Runnable Projects**: Hands-on implementations for RAG and more (located in `guides/projects/`)
- **Agent Configurations**: 9 pre-configured agent modes for different interaction patterns
- **Multi-Language Support**: Knowledge base available in 20 languages

---

## 📁 Repository Structure

```
/workspace
├── knowledge_base/          # Multi-language knowledge files (20 languages)
│   ├── Arabic/              # Arabic knowledge base
│   ├── English/             # English knowledge base (52+ files)
│   ├── French/              # French knowledge base
│   ├── German/              # German knowledge base
│   ├── Indonesian/          # Indonesian knowledge base
│   ├── Italian/             # Italian knowledge base
│   ├── Japanese/            # Japanese knowledge base
│   ├── Korean/              # Korean knowledge base
│   ├── Mandarin (Simplified Chinese)/   # Simplified Chinese knowledge base
│   ├── Mandarin (Traditional Chinese)/  # Traditional Chinese knowledge base
│   ├── Persian/             # Persian knowledge base
│   ├── Polish/              # Polish knowledge base
│   ├── Portuguese/          # Portuguese knowledge base
│   ├── Russian/             # Russian knowledge base
│   ├── Spanish/             # Spanish knowledge base
│   ├── Thai/                # Thai knowledge base
│   ├── Turkish/             # Turkish knowledge base
│   └── Vietnamese/          # Vietnamese knowledge base
├── guides/                  # Complete AI training guides
│   ├── RAG/                 # Retrieval-Augmented Generation
│   ├── Transformers/        # Language models
│   ├── CNNs/                # Convolutional Neural Networks
│   ├── GANs/                # Generative Adversarial Networks
│   ├── GNNs/                # Graph Neural Networks
│   ├── Agentic_Systems/     # Autonomous AI agents
│   ├── MoE/                 # Mixture of Experts
│   ├── Infrastructure_Layers/      # Infrastructure patterns
│   ├── Orchestration_Patterns/     # Orchestration patterns
│   ├── User Questions/      # User-submitted questions
│   ├── projects/            # Runnable projects
│   │   ├── rag_simple/      # Simple RAG implementation
│   │   └── rag-chatbot/     # RAG chatbot project
│   ├── README.md            # Guides overview
│   ├── hardware_reality_check.md    # Hardware requirements
│   ├── how_to_build_ai.md   # AI building guide
│   └── progression_map.md   # Learning progression
├── skills/                  # AI agent skill definitions (50+ skills)
│   ├── behavior-skills/     # Behavioral capabilities
│   ├── collaboration-skills/# Team collaboration
│   ├── data-skills/         # Data handling
│   ├── designing-skills/    # Design capabilities
│   ├── devops-skills/       # DevOps practices
│   ├── focused-skills/      # Focused skill modules
│   ├── management-skills/   # Management capabilities
│   ├── research-skills/     # Research methods
│   ├── security-skills/     # Security practices
│   ├── speaking-skills/     # Communication skills
│   ├── technical-skills/    # Technical capabilities
│   ├── testing-skills/      # Testing methodologies
│   ├── skill-creator.md     # Skill creation guide
│   ├── focused_skills.md    # Focused skills documentation
│   └── writing-knowledge.md # Writing best practices
├── agent_modes/             # Agent configuration files (9 modes)
│   ├── Agent.Agent.md       # Full coding agent
│   ├── Ask.Agent.md         # Q&A mode
│   ├── Chat.Agent.md        # Chat mode
│   ├── Debug.Agent.md       # Debugging mode
│   ├── Explore.Agent.md     # Exploration mode
│   ├── Plan.Agent.md        # Planning mode
│   ├── Review.Agent.md      # Review mode
│   ├── Secure.Agent.md      # Security mode
│   └── Test.Agent.md        # Testing mode
├── LICENSE                  # License file
└── README.md                # This file
```

Note: If you don't actually speak any other languages it's fine, you can use tools like Qwen Coder for completely free or GitHub Copilot if you don't mind using your Copilot credits, you can also open a issue and ask me to translate it for you.

---

## 🚀 Quick Start for Beginners

New to AI/ML development? Start here!

### Step 1: Run Your First Project (15 minutes)

Get hands-on immediately with a runnable project:

```bash
cd guides/projects/rag_simple
pip install -r requirements.txt
python main.py
```

See all [Runnable Projects](guides/projects/README.md) →

### Step 2: Pick a Learning Path

Choose based on your interest:

| Path | Start Here | Projects | Career Goal |
|------|-----------|----------|-------------|
| **NLP Engineer** | [RAG Guide](guides/RAG/) | RAG Simple | Search, Q&A systems |
| **Deep Learning** | [Transformers Guide](guides/Transformers/) | Coming soon | NLP, Translation |
| **Computer Vision** | [CNNs Guide](guides/CNNs/) | Coming soon | Image recognition |
| **AI Agents** | [Agentic Systems](guides/Agentic_Systems/) | Coming soon | Autonomous agents |

### Step 3: Explore the Guides

Browse the complete guide collection in the [guides/](guides/) directory:
- [Hardware Reality Check](guides/hardware_reality_check.md) - Understanding hardware requirements
- [How to Build AI](guides/how_to_build_ai.md) - Comprehensive AI building guide
- [Progression Map](guides/progression_map.md) - Learning path roadmap

---

## 📚 Knowledge Base

### English Knowledge Base Structure

The English knowledge base contains **52+ files** organized into 10 categories:

#### 01 Technology and Computing (7 files)
| File | Description |
|------|-------------|
| `cloud_architecture.md` | Cloud computing architectures and patterns |
| `coding_languages.md` | Programming languages and development concepts |
| `database_systems.md` | Database technologies and design principles |
| `networking_basics.md` | Network fundamentals and protocols |
| `technology_glossary.md` | Technical terminology reference |
| `tool_usage.md` | Development tool usage instructions |
| `web_development.md` | Web development frameworks and practices |

#### 02 Artificial Intelligence (5 files)
| File | Description |
|------|-------------|
| `artificial_intelligence.md` | AI fundamentals, history, ML, and deep learning |
| `local_ai_architecture.md` | Local AI system architecture |
| `ml_evaluation_and_workflow.md` | ML model evaluation and workflows |
| `phi3_and_local_models.md` | Phi3 and local model information |
| `prompt_engineering.md` | Prompt design and optimization techniques |

#### 03 Data Science (2 files)
| File | Description |
|------|-------------|
| `data_science_and_analytics.md` | Data analysis and analytics methods |
| `math_and_logic.md` | Mathematical concepts and logical reasoning |

#### 04 Science (4 files)
| File | Description |
|------|-------------|
| `environmental_science_and_sustainability.md` | Environmental topics and sustainability |
| `food_agriculture_and_nutrition.md` | Food systems, agriculture, and nutrition |
| `medicine_and_healthcare.md` | Medical and healthcare information |
| `science_and_nature.md` | Scientific concepts and natural phenomena |

#### 05 Business and Finance (3 files)
| File | Description |
|------|-------------|
| `business_and_economics.md` | Business principles and economics |
| `finance_and_investing.md` | Financial concepts and investment strategies |
| `law_and_legal_systems.md` | Legal systems and jurisprudence |

#### 06 Humanities (5 files)
| File | Description |
|------|-------------|
| `arts_and_literature.md` | Arts, literature, and creative works |
| `geography_and_geopolitics.md` | Geographic and geopolitical topics |
| `history_and_culture.md` | Historical events and cultural topics |
| `language_and_english.md` | Language rules and English grammar |
| `psychology_and_human_behavior.md` | Psychology and behavioral science |

#### 07 Reference (4 files)
| File | Description |
|------|-------------|
| `dictionary.md` | Terminology and definitions |
| `general_knowledge.md` | General information and facts |
| `safe_communication.md` | Guidelines for safe AI communication |
| `technology_and_computing.md` | General technology overview |

#### 08 Future (1 file)
| File | Description |
|------|-------------|
| `2026_and_future_events.md` | Future predictions and emerging trends |

#### 10 Cheat Sheets (4 files)
| File | Description |
|------|-------------|
| `git_commands.md` | Git command reference |
| `linux_commands.md` | Linux command line reference |
| `python_syntax.md` | Python syntax quick reference |
| `sql_quick_ref.md` | SQL query reference |

---

## 🛠️ Skills Library

The skills library contains **50+ skill modules** organized by capability type:

### Behavior Skills (`behavior-skills/`)
Core behavioral capabilities for AI interactions:
- `brainstorming.md` — Idea generation techniques
- `debugging.md` — Code debugging strategies
- `explanation.md` — Clear explanation methods
- `learning.md` — Learning and adaptation approaches
- `planning.md` — Task planning methodologies
- `style_adaptation.md` — Communication style adjustments
- `summarization.md` — Content summarization techniques
- `teaching.md` — Teaching and instruction methods

### Collaboration Skills (`collaboration-skills/`)
Team-oriented capabilities:
- `code_review.md` — Code review best practices
- `pair_programming.md` — Pair programming techniques
- `team_collaboration.md` — Teamwork strategies

### Design Skills (`designing-skills/`)
Design and architecture capabilities:
- `api_design.md` — API design principles
- `gui_design.md` — GUI design guidelines
- `system_architecture.md` — System architecture patterns
- `ui_ux_design.md` — UI/UX design principles
- `visual_design.md` — Visual design guidelines

### Speaking Skills (`speaking-skills/`)
Communication capabilities:
- `formatting.md` — Content formatting standards
- `one_on_one_communication.md` — Direct communication techniques
- `public_speaking.md` — Presentation skills
- `technical_presentation.md` — Technical presentation methods
- `text_formatting.md` — Text formatting standards

### Technical Skills
Specialized technical capabilities across multiple domains:
- **DevOps**: CI/CD pipelines and deployment strategies
- **Security**: Secure coding practices
- **Testing**: Test automation methodologies
- **Research**: Information retrieval and critical thinking
- **Data**: Data handling and processing

### Focused Skills (`focused-skills/`)
Specialized focused skill modules for targeted tasks.

### Core Documentation
- `skill-creator.md` — Guidelines for creating new skills
- `focused_skills.md` — Focused skills documentation
- `writing-knowledge.md` — Writing best practices and standards

---

##  Agent Modes

Pre-configured agent modes for different interaction patterns:

| Mode | File | Use Case |
|------|------|----------|
| **Agent** | `Agent.Agent.md` | Full coding agent for research, planning, editing, testing, and code improvement |
| **Ask** | `Ask.Agent.md` | Question-answering mode for direct queries and information retrieval |
| **Chat** | `Chat.Agent.md` | Conversational mode for natural dialogue and interactive discussions |
| **Debug** | `Debug.Agent.md` | Debugging mode for identifying and fixing code issues |
| **Explore** | `Explore.Agent.md` | Exploration mode for discovering and investigating new topics |
| **Plan** | `Plan.Agent.md` | Planning mode for structured task breakdown and roadmap creation |
| **Review** | `Review.Agent.md` | Review mode for code analysis, content review, and quality assurance |
| **Secure** | `Secure.Agent.md` | Security mode for secure coding practices and vulnerability analysis |
| **Test** | `Test.Agent.md` | Testing mode for test creation and validation |

Each agent mode includes:
- YAML frontmatter configuration
- Tool specifications
- Behavioral guidelines
- Interaction patterns

---

## 🌍 Multi-Language Support

The knowledge base supports **20 languages** currently available.

| Language | Directory | Status |
|----------|-----------|--------|
| Arabic | `Arabic/` | ✅ Available |
| English | `English/` | ✅ Fully Supported and Available |
| French | `French/` | ✅ Available |
| German | `German/` | ✅ Available |
| Indonesian | `Indonesian/` | ✅ Available |
| Italian | `Italian/` | ✅ Available |
| Japanese | `Japanese/` | ✅ Available |
| Korean | `Korean/` | ✅ Available |
| Mandarin (Simplified) | `Mandarin (Simplified Chinese)/` | ✅ Available |
| Mandarin (Traditional) | `Mandarin (Traditional Chinese)/` | ✅ Available |
| Persian | `Persian/` | ✅ Available |
| Polish | `Polish/` | ✅ Available |
| Portuguese | `Portuguese/` | ✅ Available |
| Russian | `Russian/` | ✅ Available |
| Spanish | `Spanish/` | ✅ Available |
| Thai | `Thai/` | ✅ Available |
| Turkish | `Turkish/` | ✅ Available |
| Vietnamese | `Vietnamese/` | ✅ Available |

---

## 🚀 Usage Guide

### For AI Agents

1. **Knowledge Retrieval**
   ```
   - Identify the topic domain
   - Navigate to the appropriate language directory
   - Reference relevant .md files based on category
   ```

2. **Skill Activation**
   ```
   - Assess task requirements
   - Load appropriate skills from skills/ directory
   - Combine multiple skills for complex tasks
   ```

3. **Mode Selection**
   ```
   - Choose agent mode based on interaction type:
     * Coding tasks → Agent.Agent.md
     * Questions → Ask.Agent.md
     * Research → Explore.Agent.md
     * Planning → Plan.Agent.md
     * Reviews → Review.Agent.md
   ```

### For Contributors

#### Adding Knowledge Files
1. Create new `.md` file in appropriate category under `knowledge_base/English/`
2. Follow the standard format (see [File Formats](#-file-formats))
3. Update the relevant language directories manually
4. Add entry to this README

#### Adding Skills
1. Create new skill file in appropriate `skills/` subdirectory
2. Reference `skill-creator.md` for guidelines
3. Include clear examples and use cases
4. Update relevant README files

#### Adding Agent Modes
1. Create new configuration in `agent_modes/`
2. Include YAML frontmatter with name, description, target, and tools
3. Define interaction patterns and behaviors
4. Document in this README

---

## 📝 File Formats

### Knowledge Files

Markdown format with clear hierarchical structure:

```markdown
# Topic Title

Brief introduction to the topic.

## Section Name

Detailed content with explanations, examples, and references.

### Subsection (if needed)

More specific information.

## Another Section

Additional content with supporting details.

## References

- Link or citation 1
- Link or citation 2
```

### Skill Files

Structured skill definitions:

```markdown
# Skill Name

## Description

What this skill does and when to use it.

## Capabilities

- Capability 1
- Capability 2

## Usage Examples

Example scenarios and applications.

## Best Practices

Guidelines for effective use.
```

### Agent Mode Files

YAML frontmatter with configuration:

```yaml
---
name: ModeName
description: What this mode does
tools: ['list', 'of', 'tools']
---

# Mode Instructions

Detailed behavioral guidelines and interaction patterns.
```

---

## 🎯 Purpose

This repository serves as:

- **Structured Knowledge Base**: Organized, domain-specific information for AI reference (52+ files)
-  **Skill Library**: Modular capabilities for enhancing agent performance (50+ skills)
-  **Configuration Hub**: Centralized agent mode definitions (9 modes)
-  **Multi-Language Resource**: Globally accessible knowledge in 20 languages
-  **Runnable Projects**: Hands-on implementations for practical learning
-  **Extensible Framework**: Maintainable and scalable architecture for AI development
-  **Collaboration Platform**: Standardized formats for team contributions

---

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Make** your changes following the established formats
4. **Test** your changes thoroughly
5. **Commit** your changes (`git commit -m 'Add amazing feature'`)
6. **Push** to the branch (`git push origin feature/amazing-feature`)
7. **Open** a Pull Request

### Contribution Areas
- 📚 New knowledge files
- 🛠️ New skill definitions
- 🌍 More translations for existing content
- 🐛 Bug fixes and corrections
- 📝 Documentation improvements

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support

For questions, suggestions, or issues:
- Open an issue in the repository
- Refer to the documentation in each directory
- Check the `skill-creator.md` for skill development guidance

---

<div align="center">

**Built with ♡ for the local and open source local AI community**

[↑ Back to Top ↑](#ai-model-training-essentials)

</div>
