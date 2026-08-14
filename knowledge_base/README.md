# Knowledge Base

A multilingual collection of structured reference documents covering coding, technology, AI, science, business, humanities, and more. Designed for both AI training and human learning.

**Total Languages:** 23  
**English Files:** 120+ markdown documents  
**Organization:** 10 thematic directories, 6 with nested subfolders

---

## Directory Structure

Each language directory mirrors the same thematic organisation:

```
knowledge_base/
├── English/
│   ├── 01_coding_and_technology/
│   │   └── programming_languages/         # 34 individual language references
│   ├── 02_ai_and_machine_learning/
│   │   ├── foundations/                   # AI fundamentals, ML workflows, prompt engineering
│   │   ├── architectures/                 # Generative AI, GNNs, RL, recommendation systems
│   │   ├── engineering/                   # MLOps, optimization, data engineering
│   │   ├── nlp_and_speech/               # NLP, computer vision, multimodal AI
│   │   └── ethics_and_safety/            # AI governance, alignment
│   ├── 03_data_science_and_analytics/
│   │   └── mathematics/                   # Core math, statistics, logic
│   ├── 04_natural_sciences/
│   │   ├── life_sciences/                 # Biology, medicine, agriculture
│   │   ├── physical_sciences/             # Physics, chemistry
│   │   └── earth_and_environment/         # Environment, geography
│   ├── 05_business_and_economics/         # Economics, finance, law, management
│   ├── 06_humanities_and_arts/
│   │   ├── arts/                          # Literature, visual arts, performing arts
│   │   ├── history/                       # World history
│   │   ├── language/                      # Linguistics
│   │   ├── philosophy_and_mind/           # Philosophy, psychology
│   │   └── religion_and_mythology/        # Comparative religion, mythology
│   ├── 07_general_reference/              # Dictionary, general knowledge, communication
│   ├── 08_future_and_trends/
│   │   ├── technology/                    # Emerging tech, computing, AI in daily life
│   │   ├── society_and_domains/           # Work, healthcare, education, transport
│   │   └── strategy/                      # Scenario planning, geopolitics
│   ├── 09_lessons_from_failures/          # AI failures, security issues, system reliability
│   └── 10_quick_reference/
│       ├── programming/                   # Python, SQL, regex, Git cheat sheets
│       └── infrastructure/                # Linux, Docker, cloud, CI/CD, monitoring
├── Arabic/
├── Bengali/
├── Filipino/
├── French/
├── German/
├── ... (24 languages total)
└── Vietnamese/
```

### Subfolder Convention

Directories with 10+ files and clear thematic groupings use **nested subfolders** to organise content. Each subfolder has its own set of focused documents, and files include a `subcategory` frontmatter field. Directories with fewer files or no clear thematic splits remain flat. Every directory — whether flat or nested — has a `README.md` index with a file listing and suggested reading paths.

| Pattern | Directories |
|---------|-------------|
| **With subfolders** | 01 (programming_languages), 02 (5), 03 (mathematics), 04 (3), 06 (5), 08 (3), 10 (2) |
| **Flat (with README)** | 05, 07, 09 |

### Content Directories

| Directory | Topics |
|-----------|--------|
| **01_coding_and_technology** | Web dev, databases, cloud, networking, DevOps, security, API design, architecture patterns, 34 programming languages |
| **02_ai_and_machine_learning** | AI fundamentals, ML workflows, local AI, prompt engineering, computer vision, NLP, MLOps, data engineering |
| **03_data_science_and_analytics** | Data processing, statistics, big data, business intelligence, data visualisation, statistical testing |
| **04_natural_sciences** | Physics, chemistry, biology, medicine, environment, agriculture |
| **05_business_and_economics** | Business principles, finance, investing, economics, law, marketing, management, global trade |
| **06_humanities_and_arts** | History, geography, arts, literature, psychology, language, philosophy |
| **07_general_reference** | General knowledge, technology, communication, world cultures, practical life skills, media literacy, environment |
| **08_future_and_trends** | Emerging technologies, future of work/healthcare/transport, scenario planning |
| **09_lessons_from_failures** | AI/LLM failures, code quality issues, security vulnerabilities, system reliability |
| **10_quick_reference** | Cheat sheets for Python, Git, SQL, Linux, Docker/K8s, regex, cloud comparison, Bash |

---

## Language Translations

| Language | Directory | README |
|----------|-----------|--------|
| Arabic | `Arabic/` | [README](Arabic/README.md) |
| Bengali | `Bengali/` | [README](Bengali/README.md) |
| English | `English/` | [README](English/README.md) |
| Filipino | `Filipino/` | [README](Filipino/README.md) |
| French | `French/` | [README](French/README.md) |
| German | `German/` | [README](German/README.md) |
| Hindi | `Hindi/` | [README](Hindi/README.md) |
| Indonesian | `Indonesian/` | [README](Indonesian/README.md) |
| Italian | `Italian/` | [README](Italian/README.md) |
| Japanese | `Japanese/` | [README](Japanese/README.md) |
| Korean | `Korean/` | [README](Korean/README.md) |
| Mandarin_Simplified | `Mandarin_Simplified/` | [README](Mandarin_Simplified/README.md) |
| Mandarin_Traditional | `Mandarin_Traditional/` | [README](Mandarin_Traditional/README.md) |
| Persian | `Persian/` | [README](Persian/README.md) |
| Polish | `Polish/` | [README](Polish/README.md) |
| Portuguese | `Portuguese/` | [README](Portuguese/README.md) |
| Russian | `Russian/` | [README](Russian/README.md) |
| Spanish | `Spanish/` | [README](Spanish/README.md) |
| Swahili | `Swahili/` | [README](Swahili/README.md) |
| Thai | `Thai/` | [README](Thai/README.md) |
| Turkish | `Turkish/` | [README](Turkish/README.md) |
| Urdu | `Urdu/` | [README](Urdu/README.md) |
| Vietnamese | `Vietnamese/` | [README](Vietnamese/README.md) |

> **Note:** English is the most complete translation with 120+ files. Other languages vary in coverage — some have fewer files, particularly in `08_future_and_trends`. The subfolder structure currently exists only in English; other languages retain the flat layout.

---

## Related Resources

Beyond the language-specific knowledge base, the repository also contains:

| Resource | Location | Description |
|----------|----------|-------------|
| **Guides** | [`/guides`](../guides/) | In-depth chapter-based guides on CNNs, Transformers, RAG, GANs, GNNs, Agentic Systems, MoE, and more |
| **Skills** | [`/skills`](../skills/) | 50+ skill modules for AI agents — behaviour, collaboration, design, DevOps, security, testing |
| **Agent Modes** | [`/agent_modes`](../agent_modes/) | 16 pre-configured agent modes across four categories: Core Workflow (Agent, Plan, Explore, Ask, Chat), Quality & Reliability (Debug, Test, Review, Lint, Performance), Security & Operations (Secure, DevOps, Database), and Specialized (Documentation, Migration, Orchestrator) |
| **Wiki** | [`/wiki`](../wiki/) | Architecture patterns, deployment, monitoring, security, learning paths |
| **Projects** | [`/guides/projects`](../guides/projects/) | Runnable code examples (RAG chatbot, CNN basics, Transformers intro) |

---

## Getting Started

1. **Choose your path**: Browse the [English README](English/README.md) for the full file index and learning paths.
2. **Pick a topic**: Navigate to any numbered directory for domain-specific content.
3. **Check prerequisites**: See [prerequisites](../guides/prerequisites/) for foundational knowledge.
4. **Follow the progression**: The [progression map](../guides/progression_map.md) outlines a recommended learning journey.

---

## Contributing

Contributions are welcome! When adding or editing knowledge base files:

1. Follow the existing naming conventions and directory structure.
2. Use clear hierarchical headings (`#` title, `##` sections, `###` subsections).
3. Include comparison tables where appropriate.
4. Write in a natural, conversational tone — not robotic definition lists.
5. Update the relevant language README to reflect new files.
6. For new files in subfolder directories, add the `subcategory` frontmatter field matching the subfolder name.
7. When a flat directory grows beyond ~12 files with clear thematic groupings, consider splitting it into subfolders.

See the [Contributing Guide](../CONTRIBUTING.md) for full details.

---

*This knowledge base is continuously updated. The English directory is the primary source; other languages are translated progressively.*
