"""Set up new language directories for the knowledge base.

Creates the full directory hierarchy and translated README.md files for
Bengali, Urdu, Filipino (Tagalog), and Swahili — mirroring the English structure.

Usage:
    python scripts/setup_new_languages.py
    python scripts/setup_new_languages.py --languages Bengali Swahili
    python scripts/setup_new_languages.py --dry-run
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

# ── Configuration ──────────────────────────────────────────────────────────

NEW_LANGUAGES = {
    "Bengali": "bn",
    "Urdu": "ur",
    "Filipino": "tl",
    "Swahili": "sw",
}

# Native titles for each language's top-level README
TITLES = {
    "Bengali": "জ্ঞান ভাণ্ডার",
    "Urdu": "علمی ذخیرہ",
    "Filipino": "Base ng Kaalaman",
    "Swahili": "Hazina ya Maarifa",
}

# Subcategory directory names (English, kept as-is for all languages)
SUBDIRS = {
    "01_coding_and_technology": ["programming_languages"],
    "02_ai_and_machine_learning": [
        "foundations", "architectures", "engineering",
        "nlp_and_speech", "ethics_and_safety",
    ],
    "03_data_science_and_analytics": ["mathematics"],
    "04_natural_sciences": ["life_sciences", "physical_sciences", "earth_and_environment"],
    "05_business_and_economics": [],
    "06_humanities_and_arts": [
        "arts", "history", "language",
        "philosophy_and_mind", "religion_and_mythology",
    ],
    "07_general_reference": [],
    "08_future_and_trends": ["technology", "society_and_domains", "strategy"],
    "09_lessons_from_failures": [],
    "10_quick_reference": ["programming", "infrastructure"],
}

TOP_LEVEL_DIRS = list(SUBDIRS.keys())

# ── Translation helper ─────────────────────────────────────────────────────

FENCE = re.compile(r"^\s*(```|~~~)")
INLINE = re.compile(r"(`[^`]*`|<[^>]+>|https?://[^\s)]+|\[[^]]*\]\([^)]*\))")


def translate_text(text: str, target: str) -> str:
    """Translate text using Google Translate API (same as restructure_and_translate.py)."""
    if not text.strip() or not re.search(r"[A-Za-z]", text):
        return text
    protected: list[str] = []

    def hold(match: re.Match[str]) -> str:
        protected.append(match.group(0))
        return f" XQZMARKER{len(protected) - 1}XQZ "

    query = INLINE.sub(hold, text)
    url = (
        "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en"
        f"&tl={quote(target)}&dt=t&q={quote(query)}"
    )
    request = Request(url, headers={"User-Agent": "knowledge-base-translator/1.0"})
    for attempt in range(3):
        try:
            with urlopen(request, timeout=30) as response:
                payload = json.loads(response.read().decode("utf-8"))
            break
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)
    result = "".join(part[0] for part in payload[0] if part and part[0])
    for index, original in enumerate(protected):
        result = result.replace(f" XQZMARKER{index}XQZ ", original)
        result = result.replace(f"XQZMARKER{index}XQZ", original)
    return result


def translate_block(text: str, target: str, delay: float = 0.15) -> str:
    """Translate a block of text, preserving code fences."""
    output: list[str] = []
    in_fence = False
    paragraph: list[str] = []

    def flush() -> None:
        if paragraph:
            block = "".join(paragraph)
            output.append(translate_text(block, target))
            paragraph.clear()

    for line in text.splitlines(keepends=True):
        if FENCE.match(line):
            flush()
            in_fence = not in_fence
            output.append(line)
        elif in_fence or not line.strip():
            flush()
            output.append(line)
        else:
            paragraph.append(line)
    flush()
    time.sleep(delay)
    return "".join(output)


# ── README generators ──────────────────────────────────────────────────────

def generate_top_level_readme(lang: str, lang_code: str, title: str) -> str:
    """Generate the top-level README.md for a new language."""
    return f"""# {title}

Kulikuwa na makala mbalimbali zinazohusu coding, teknolojia, AI, sayansi, biashara, humanities, na zaidi — zimeandikwa kwa mtindo wa mazungumzo ya asili ulioundwa kwa ajili ya mafunzo ya AI na ujifunzaji wa binadamu.

**Lugha:** {lang}  
**Jumla ya Faili:** 120+ hati za markdown  
**Mpangilio:** Saraka 10 za mada + rejea 34 za lugha za programu

---

## Muundo wa Saraka

```
knowledge_base/{lang}/
├── 01_coding_and_technology/
│   └── programming_languages/         # 34 individual language references
├── 02_ai_and_machine_learning/
│   ├── foundations/
│   ├── architectures/
│   ├── engineering/
│   ├── nlp_and_speech/
│   └── ethics_and_safety/
├── 03_data_science_and_analytics/
│   └── mathematics/
├── 04_natural_sciences/
│   ├── life_sciences/
│   ├── physical_sciences/
│   └── earth_and_environment/
├── 05_business_and_economics/
├── 06_humanities_and_arts/
│   ├── arts/
│   ├── history/
│   ├── language/
│   ├── philosophy_and_mind/
│   └── religion_and_mythology/
├── 07_general_reference/
├── 08_future_and_trends/
│   ├── technology/
│   ├── society_and_domains/
│   └── strategy/
├── 09_lessons_from_failures/
└── 10_quick_reference/
    ├── programming/
    └── infrastructure/
```

---

## Tafsiri za Lugha

| Lugha | Saraka | README |
|----------|-----------|--------|
| Bengali | `Bengali/` | [README](../Bengali/README.md) |
| Urdu | `Urdu/` | [README](../Urdu/README.md) |
| Filipino | `Filipino/` | [README](../Filipino/README.md) |
| Swahili | `Swahili/` | [README](../Swahili/README.md) |

> **Kumbuka:** Kiingereza ndicho chanzo kamili zaidi cha faili 120+. Lugha zingine zinaweza kuwa na faili chache.

---

## Rasilimali Zinazohusiana

| Rasilimali | Mahali | Maelezo |
|----------|----------|-------------|
| **Miongozo** | [`/guides`](../../guides/) | Miongozo ya kina kuhusu CNNs, Transformers, RAG, GANs, na zaidi |
| **Stadi** | [`/skills`](../../skills/) | Moduli 50+ za stadi za wakala wa AI |
| **Hali za Wakala** | [`/agent_modes`](../../agent_modes/) | Hali 16 za wakala zilizosanidiwa awali |
| **Wiki** | [`/wiki`](../../wiki/) | Miundo, usakinishaji, ufuatiliaji, usalama |

---

## Kuanza

1. **Chagua njia yako**: Pitia fahirisi kamili ya Kiingereza kwa maelezo zaidi.
2. **Chagua mada**: Nenda kwenye saraka yoyote yenye nambari kwa maudhui maalum.
3. **Angalia masharti**: Tazama [prerequisites](../../guides/prerequisites/) kwa maarifa ya msingi.

---

## Kuchangia

Michango inakaribishwa! Unapoongeza au kuhariri faili za knowledge base:

1. Fuata makubaliano ya majina na muundo wa saraka.
2. Tumia vichwa vya habari vya daraja (`#` title, `##` sections, `###` subsections).
3. Jumuisha majedwali ya kulinganisha inapofaa.
4. Andika kwa mtindo wa asili na wa mazungumzo.
5. Sasisha README ya lugha inayohusika.

---

*Knowledge base hii inasasishwa mara kwa mara. Saraka ya Kiingereza ndicho chanzo cha msingi; lugha zingine zinatafsiriwa hatua kwa hatua.*
"""


def generate_subdir_readme(
    dir_name: str, lang: str, lang_code: str,
) -> str:
    """Generate a README.md for a subdirectory, translated into the target language."""
    # Map of English subdirectory README content (simplified, structural)
    readme_templates = {
        "01_coding_and_technology": _readme_01,
        "02_ai_and_machine_learning": _readme_02,
        "03_data_science_and_analytics": _readme_03,
        "04_natural_sciences": _readme_04,
        "05_business_and_economics": _readme_05,
        "06_humanities_and_arts": _readme_06,
        "07_general_reference": _readme_07,
        "08_future_and_trends": _readme_08,
        "09_lessons_from_failures": _readme_09,
        "10_quick_reference": _readme_10,
    }
    generator = readme_templates.get(dir_name)
    if generator:
        return generator(lang, lang_code)
    return f"# {dir_name}\n"


def _readme_01(lang: str, lang_code: str) -> str:
    return f"""# Coding and Technology

Reference documents covering web development, databases, cloud computing, networking, DevOps, security, API design, and 34 programming languages.

---

## Structure

```
01_coding_and_technology/
├── README.md
├── database_systems.md
├── cloud_architecture.md
├── networking_basics.md
├── devops_sysadmin.md
├── devops_and_cicd.md
├── cybersecurity_fundamentals.md
├── api_design_and_architecture.md
├── accessibility_and_inclusive_design.md
├── blockchain_and_distributed_systems.md
├── data_structures_and_algorithms.md
├── embedded_systems_and_iot.md
├── low_code_and_platform_engineering.md
├── mobile_development.md
├── performance_optimization.md
└── programming_languages/
    ├── python/
    ├── javascript/
    ├── rust/
    ├── go/
    └── ... (34 languages total)
```

## Files

| File | Topics |
|------|--------|
| [database_systems.md](database_systems.md) | SQL, NoSQL, design patterns, optimization |
| [cloud_architecture.md](cloud_architecture.md) | Cloud providers, architecture patterns, security |
| [networking_basics.md](networking_basics.md) | OSI model, TCP/IP, protocols, security |
| [devops_sysadmin.md](devops_sysadmin.md) | SSH, systemd, logging, monitoring, backups |
| [devops_and_cicd.md](devops_and_cicd.md) | CI/CD pipelines, Docker, Kubernetes, Terraform |
| [cybersecurity_fundamentals.md](cybersecurity_fundamentals.md) | Encryption, TLS, OWASP, secure coding |
| [api_design_and_architecture.md](api_design_and_architecture.md) | REST, GraphQL, gRPC, versioning, auth |
| [accessibility_and_inclusive_design.md](accessibility_and_inclusive_design.md) | WCAG, inclusive UX, assistive technology |
| [blockchain_and_distributed_systems.md](blockchain_and_distributed_systems.md) | Consensus, smart contracts, DeFi |
| [data_structures_and_algorithms.md](data_structures_and_algorithms.md) | Arrays, trees, graphs, sorting, searching |
| [embedded_systems_and_iot.md](embedded_systems_and_iot.md) | Microcontrollers, sensors, RTOS, IoT |
| [low_code_and_platform_engineering.md](low_code_and_platform_engineering.md) | Low-code platforms, internal developer platforms |
| [mobile_development.md](mobile_development.md) | iOS, Android, React Native, Flutter |
| [performance_optimization.md](performance_optimization.md) | Profiling, caching, CDN, query optimization |

## Programming Languages (34)

See [programming_languages/](programming_languages/) for individual language references.
"""


def _readme_02(lang: str, lang_code: str) -> str:
    return f"""# AI and Machine Learning

A structured collection of reference documents covering artificial intelligence fundamentals, model architectures, ML engineering, language and vision processing, and AI ethics.

## Structure

```
02_ai_and_machine_learning/
├── README.md
├── foundations/
│   ├── artificial_intelligence.md
│   └── ml_evaluation_and_workflow.md
├── architectures/
│   ├── generative_ai_deep_dive.md
│   ├── graph_neural_networks.md
│   ├── reinforcement_learning.md
│   ├── recommendation_systems.md
│   └── federated_learning_and_privacy.md
├── engineering/
│   ├── model_optimization_and_deployment.md
│   ├── ml_engineering_and_mlops.md
│   ├── data_engineering_and_pipelines.md
│   ├── local_ai_architecture.md
│   └── phi3_and_local_models.md
├── nlp_and_speech/
│   ├── nlp_fundamentals.md
│   ├── speech_and_audio_processing.md
│   ├── time_series_and_forecasting.md
│   ├── computer_vision_fundamentals.md
│   └── multimodal_ai.md
└── ethics_and_safety/
    ├── ai_ethics_and_governance.md
    └── ai_safety_and_alignment.md
```

## Files by Subcategory

### Foundations
| File | Description |
|------|-------------|
| [artificial_intelligence.md](foundations/artificial_intelligence.md) | AI overview, ML, deep learning, LLMs, ethics |
| [ml_evaluation_and_workflow.md](foundations/ml_evaluation_and_workflow.md) | ML pipelines, metrics, best practices |

### Model Architectures
| File | Description |
|------|-------------|
| [generative_ai_deep_dive.md](architectures/generative_ai_deep_dive.md) | GANs, VAEs, diffusion models, LLMs |
| [graph_neural_networks.md](architectures/graph_neural_networks.md) | GCNs, GATs, message passing, knowledge graphs |
| [reinforcement_learning.md](architectures/reinforcement_learning.md) | MDPs, Q-learning, policy gradients, RLHF |
| [recommendation_systems.md](architectures/recommendation_systems.md) | Collaborative filtering, matrix factorisation |
| [federated_learning_and_privacy.md](architectures/federated_learning_and_privacy.md) | Decentralised training, differential privacy |

### ML Engineering
| File | Description |
|------|-------------|
| [model_optimization_and_deployment.md](engineering/model_optimization_and_deployment.md) | Quantisation, pruning, distillation, ONNX |
| [ml_engineering_and_mlops.md](engineering/ml_engineering_and_mlops.md) | Model serving, registries, drift monitoring |
| [data_engineering_and_pipelines.md](engineering/data_engineering_and_pipelines.md) | ETL/ELT, data lakes, Kafka, feature stores |
| [local_ai_architecture.md](engineering/local_ai_architecture.md) | Local AI deployment architectures |
| [phi3_and_local_models.md](engineering/phi3_and_local_models.md) | Running models locally |

### NLP and Speech
| File | Description |
|------|-------------|
| [nlp_fundamentals.md](nlp_and_speech/nlp_fundamentals.md) | Text processing, embeddings, Transformers |
| [speech_and_audio_processing.md](nlp_and_speech/speech_and_audio_processing.md) | ASR, TTS, audio features, Whisper |
| [time_series_and_forecasting.md](nlp_and_speech/time_series_and_forecasting.md) | ARIMA, Prophet, LSTMs, seasonality |
| [computer_vision_fundamentals.md](nlp_and_speech/computer_vision_fundamentals.md) | CNNs, object detection, segmentation |
| [multimodal_ai.md](nlp_and_speech/multimodal_ai.md) | Vision-language models, CLIP, DALL-E |

### Ethics and Safety
| File | Description |
|------|-------------|
| [ai_ethics_and_governance.md](ethics_and_safety/ai_ethics_and_governance.md) | AI bias, fairness, accountability, regulation |
| [ai_safety_and_alignment.md](ethics_and_safety/ai_safety_and_alignment.md) | Alignment problem, RLHF, interpretability |
"""


def _readme_03(lang: str, lang_code: str) -> str:
    return f"""# Data Science and Analytics

Reference documents covering data processing, statistics, mathematics, big data, visualisation, and experimentation.

## Structure

```
03_data_science_and_analytics/
├── README.md
├── data_science_and_analytics.md
├── data_visualization.md
├── statistical_testing_and_experimentation.md
├── causal_inference.md
├── data_ethics_and_privacy.md
├── ensemble_methods.md
├── feature_engineering.md
├── geospatial_analysis.md
└── mathematics/
    ├── mathematics.md
    ├── statistics_and_probability.md
    └── logic_and_critical_thinking.md
```

## Files

### Mathematics
| File | Description |
|------|-------------|
| [mathematics.md](mathematics/mathematics.md) | Number systems, algebra, geometry, calculus |
| [statistics_and_probability.md](mathematics/statistics_and_probability.md) | Probability theory, hypothesis testing, regression |
| [logic_and_critical_thinking.md](mathematics/logic_and_critical_thinking.md) | Propositional logic, Boolean algebra, fallacies |

### Data Science & Analytics
| File | Description |
|------|-------------|
| [data_science_and_analytics.md](data_science_and_analytics.md) | Data processing, ML, big data, BI |
| [data_visualization.md](data_visualization.md) | Chart selection, design principles, storytelling |
| [statistical_testing_and_experimentation.md](statistical_testing_and_experimentation.md) | Hypothesis testing, A/B testing, causal inference |
| [causal_inference.md](causal_inference.md) | DAGs, confounders, difference-in-differences |
| [data_ethics_and_privacy.md](data_ethics_and_privacy.md) | GDPR, data consent, algorithmic bias |
| [ensemble_methods.md](ensemble_methods.md) | Bagging, boosting, stacking, random forests |
| [feature_engineering.md](feature_engineering.md) | Transformations, encodings, feature selection |
| [geospatial_analysis.md](geospatial_analysis.md) | Coordinate systems, spatial operations, GeoPandas |
"""


def _readme_04(lang: str, lang_code: str) -> str:
    return f"""# Natural Sciences

Reference documents covering physics, chemistry, biology, medicine, environment, agriculture, and earth sciences.

## Structure

```
04_natural_sciences/
├── README.md
├── life_sciences/
│   ├── biology_fundamentals.md
│   ├── genetics_and_genomics.md
│   ├── medicine_and_healthcare.md
│   ├── neuroscience.md
│   └── food_agriculture_and_nutrition.md
├── physical_sciences/
│   ├── physics.md
│   ├── chemistry.md
│   └── materials_science.md
└── earth_and_environment/
    ├── earth_science.md
    ├── astronomy_and_cosmology.md
    └── environmental_science_and_sustainability.md
```

## Files by Subcategory

### Life Sciences
| File | Description |
|------|-------------|
| [biology_fundamentals.md](life_sciences/biology_fundamentals.md) | Cells, DNA, evolution, ecology |
| [genetics_and_genomics.md](life_sciences/genetics_and_genomics.md) | DNA, gene expression, CRISPR, GWAS |
| [medicine_and_healthcare.md](life_sciences/medicine_and_healthcare.md) | Medical specialties, diagnosis, treatment |
| [neuroscience.md](life_sciences/neuroscience.md) | Neurons, brain structure, neurotransmitters |
| [food_agriculture_and_nutrition.md](life_sciences/food_agriculture_and_nutrition.md) | Agriculture, nutrition, food systems |

### Physical Sciences
| File | Description |
|------|-------------|
| [physics.md](physical_sciences/physics.md) | Forces, mechanics, thermodynamics, quantum |
| [chemistry.md](physical_sciences/chemistry.md) | Atomic structure, periodic table, bonding |
| [materials_science.md](physical_sciences/materials_science.md) | Crystal structures, polymers, semiconductors |

### Earth and Environment
| File | Description |
|------|-------------|
| [earth_science.md](earth_and_environment/earth_science.md) | Plate tectonics, atmosphere, weather |
| [astronomy_and_cosmology.md](earth_and_environment/astronomy_and_cosmology.md) | Stars, galaxies, Big Bang, dark matter |
| [environmental_science_and_sustainability.md](earth_and_environment/environmental_science_and_sustainability.md) | Ecosystems, climate, energy, policy |
"""


def _readme_05(lang: str, lang_code: str) -> str:
    return f"""# Business and Economics

Reference documents covering business principles, economics, finance, law, management, and organisational design.

---

## Files

| File | Topics |
|------|--------|
| [business_and_economics.md](business_and_economics.md) | Business models, economics fundamentals, market structures |
| [finance_and_investing.md](finance_and_investing.md) | Financial markets, asset classes, valuation, portfolio theory |
| [behavioural_economics.md](behavioural_economics.md) | Cognitive biases, prospect theory, nudges |
| [game_theory.md](game_theory.md) | Nash equilibrium, auction theory, mechanism design |
| [law_and_legal_systems.md](law_and_legal_systems.md) | Legal traditions, contract law, corporate law |
| [marketing_and_digital_strategy.md](marketing_and_digital_strategy.md) | Marketing fundamentals, SEO, content strategy |
| [management_and_project_methodologies.md](management_and_project_methodologies.md) | Agile, Scrum, Waterfall, Six Sigma, OKRs |
| [organisational_design_and_culture.md](organisational_design_and_culture.md) | Org structures, culture types, change management |
| [supply_chain_and_operations.md](supply_chain_and_operations.md) | Supply chain management, logistics, lean manufacturing |
| [intellectual_property_and_innovation.md](intellectual_property_and_innovation.md) | Patents, trademarks, copyrights, trade secrets |
| [global_economy_and_trade.md](global_economy_and_trade.md) | International trade, economic indicators, globalisation |

---

## Suggested Reading

- **Business fundamentals:** `business_and_economics.md` → `finance_and_investing.md`
- **Management track:** `management_and_project_methodologies.md` → `organisational_design_and_culture.md`
- **Strategy track:** `game_theory.md` → `behavioural_economics.md` → `marketing_and_digital_strategy.md`
- **Legal & IP:** `law_and_legal_systems.md` → `intellectual_property_and_innovation.md`
- **Global economy:** `business_and_economics.md` → `global_economy_and_trade.md`
"""


def _readme_06(lang: str, lang_code: str) -> str:
    return f"""# Humanities and Arts

Reference documents covering history, arts, psychology, language, philosophy, and religion.

## Structure

```
06_humanities_and_arts/
├── README.md
├── arts/
│   ├── literature.md
│   ├── visual_arts.md
│   ├── performing_arts.md
│   └── music_theory_and_acoustics.md
├── history/
│   ├── history_and_culture.md
│   └── geography_and_geopolitics.md
├── language/
│   ├── language_and_english.md
│   └── linguistics_and_language_science.md
├── philosophy_and_mind/
│   ├── philosophy_and_critical_thinking.md
│   └── psychology_and_human_behavior.md
└── religion_and_mythology/
    └── world_religions_and_comparative_mythology.md
```

## Files by Subcategory

### Arts
| File | Description |
|------|-------------|
| [literature.md](arts/literature.md) | Literary genres, forms, poetry, movements |
| [visual_arts.md](arts/visual_arts.md) | Art movements, mediums, design principles |
| [performing_arts.md](arts/performing_arts.md) | Theater, film, dance traditions |
| [music_theory_and_acoustics.md](arts/music_theory_and_acoustics.md) | Scales, chords, harmony, rhythm, acoustics |

### History
| File | Description |
|------|-------------|
| [history_and_culture.md](history/history_and_culture.md) | World history from ancient to modern |
| [geography_and_geopolitics.md](history/geography_and_geopolitics.md) | Physical/human geography, political systems |

### Language
| File | Description |
|------|-------------|
| [language_and_english.md](language/language_and_english.md) | Grammar, usage, writing |
| [linguistics_and_language_science.md](language/linguistics_and_language_science.md) | Phonetics, syntax, semantics, pragmatics |

### Philosophy and Mind
| File | Description |
|------|-------------|
| [philosophy_and_critical_thinking.md](philosophy_and_mind/philosophy_and_critical_thinking.md) | Schools of thought, ethics, logic |
| [psychology_and_human_behavior.md](philosophy_and_mind/psychology_and_human_behavior.md) | Cognitive, social, developmental psychology |

### Religion and Mythology
| File | Description |
|------|-------------|
| [world_religions_and_comparative_mythology.md](religion_and_mythology/world_religions_and_comparative_mythology.md) | Major world religions, comparative mythology |
"""


def _readme_07(lang: str, lang_code: str) -> str:
    return f"""# General Reference

Reference documents covering general knowledge, technology, communication, learning, research, and practical life skills.

---

## Files

| File | Topics |
|------|--------|
| [general_knowledge.md](general_knowledge.md) | Solar system, human body, geography, energy |
| [technology_and_computing.md](technology_and_computing.md) | Computing basics, internet, databases, cloud |
| [safe_communication.md](safe_communication.md) | Communication guidelines and best practices |
| [learning_science_and_pedagogy.md](learning_science_and_pedagogy.md) | Retrieval practice, spaced repetition, Bloom's taxonomy |
| [research_methodology.md](research_methodology.md) | Scientific method, sampling, validity, experimental design |
| [writing_and_communication.md](writing_and_communication.md) | Pyramid principle, presentations, persuasion |
| [world_cultures_and_societies.md](world_cultures_and_societies.md) | Cultural dimensions, major cultural regions |
| [practical_life_skills.md](practical_life_skills.md) | Personal finance, nutrition, cooking, time management |
| [media_literacy_and_information.md](media_literacy_and_information.md) | Source evaluation, misinformation, fact-checking |
| [environmental_awareness.md](environmental_awareness.md) | Climate science, ecosystems, biodiversity |

---

## Suggested Reading

- **General:** `general_knowledge.md` → `technology_and_computing.md`
- **Academic:** `research_methodology.md` → `learning_science_and_pedagogy.md`
- **Communication:** `writing_and_communication.md` → `safe_communication.md`
- **Media literacy:** `media_literacy_and_information.md` → `environmental_awareness.md`
"""


def _readme_08(lang: str, lang_code: str) -> str:
    return f"""# Future and Trends

Reference documents covering emerging technologies, future of work, healthcare, transportation, scenario planning, and geopolitics.

## Structure

```
08_future_and_trends/
├── README.md
├── technology/
│   ├── emerging_technologies.md
│   ├── future_of_computing.md
│   ├── ai_in_everyday_life.md
│   ├── climate_technology_and_green_innovation.md
│   └── space_exploration_roadmap.md
├── society_and_domains/
│   ├── demographic_shifts.md
│   ├── education_transformation.md
│   ├── future_of_work.md
│   ├── future_healthcare.md
│   ├── future_transportation.md
│   └── sustainable_future.md
└── strategy/
    ├── scenario_planning.md
    ├── 2026_and_future_events.md
    └── geostrategic_futures.md
```

## Files by Subcategory

### Technology
| File | Description |
|------|-------------|
| [emerging_technologies.md](technology/emerging_technologies.md) | Quantum computing, biotech, nanotechnology |
| [future_of_computing.md](technology/future_of_computing.md) | Moore's Law, quantum computing, neuromorphic chips |
| [ai_in_everyday_life.md](technology/ai_in_everyday_life.md) | Recommendation systems, smart assistants, privacy |
| [climate_technology_and_green_innovation.md](technology/climate_technology_and_green_innovation.md) | Renewable energy, EVs, carbon capture |
| [space_exploration_roadmap.md](technology/space_exploration_roadmap.md) | Space missions and timelines |

### Society and Domains
| File | Description |
|------|-------------|
| [demographic_shifts.md](society_and_domains/demographic_shifts.md) | Population trends, migration, urbanization |
| [education_transformation.md](society_and_domains/education_transformation.md) | Online learning, AI tutoring |
| [future_of_work.md](society_and_domains/future_of_work.md) | Automation, remote work, reskilling |
| [future_healthcare.md](society_and_domains/future_healthcare.md) | Personalized medicine, AI diagnostics |
| [future_transportation.md](society_and_domains/future_transportation.md) | EVs, autonomous vehicles, hyperloop |
| [sustainable_future.md](society_and_domains/sustainable_future.md) | Climate, energy transition, circular economy |

### Strategy
| File | Description |
|------|-------------|
| [scenario_planning.md](strategy/scenario_planning.md) | Future scenarios and frameworks |
| [2026_and_future_events.md](strategy/2026_and_future_events.md) | Upcoming events, space missions, tech trends |
| [geostrategic_futures.md](strategy/geostrategic_futures.md) | Geopolitics, US-China, multipolar world |
"""


def _readme_09(lang: str, lang_code: str) -> str:
    return f"""# Lessons from Failures

Reference documents covering AI/LLM failures, code quality issues, security vulnerabilities, cognitive biases, and system reliability patterns.

---

## Files

| File | Topics |
|------|--------|
| [ai_llm_failures.md](ai_llm_failures.md) | Hallucinations, bias, alignment failures |
| [code_quality_issues.md](code_quality_issues.md) | Common coding mistakes and anti-patterns |
| [cognitive_logical_issues.md](cognitive_logical_issues.md) | Reasoning errors and cognitive biases |
| [rag_vector_search.md](rag_vector_search.md) | RAG and vector search pitfalls |
| [security_vulnerabilities.md](security_vulnerabilities.md) | Common security vulnerabilities |
| [system_reliability.md](system_reliability.md) | System failures and reliability patterns |
| [api_design_and_integration_failures.md](api_design_and_integration_failures.md) | API anti-patterns, breaking changes, cascading failures |
| [data_pipeline_and_etl_failures.md](data_pipeline_and_etl_failures.md) | Schema drift, duplicate data, validation gaps |
| [ml_project_failures.md](ml_project_failures.md) | Data leakage, expectation mismatches, model decay |

---

## Suggested Reading

- **AI failures:** `ai_llm_failures.md` → `ml_project_failures.md` → `rag_vector_search.md`
- **Code quality:** `code_quality_issues.md` → `api_design_and_integration_failures.md`
- **Security:** `security_vulnerabilities.md` → `system_reliability.md`
- **Cognitive:** `cognitive_logical_issues.md`
"""


def _readme_10(lang: str, lang_code: str) -> str:
    return f"""# Quick Reference

Cheat sheets and quick-reference guides for programming, infrastructure, and DevOps tools.

## Structure

```
10_quick_reference/
├── README.md
├── programming/
│   ├── python_syntax.md
│   ├── sql_quick_ref.md
│   ├── regular_expressions.md
│   └── git_commands.md
└── infrastructure/
    ├── linux_commands.md
    ├── bash_and_shell_scripting.md
    ├── docker_and_kubernetes.md
    ├── cloud_services_comparison.md
    ├── ansible_quick_ref.md
    ├── terraform_quick_ref.md
    ├── cicd_pipeline_config.md
    └── prometheus_and_grafana.md
```

## Files by Subcategory

### Programming
| File | Description |
|------|-------------|
| [python_syntax.md](programming/python_syntax.md) | Python syntax cheat sheet |
| [sql_quick_ref.md](programming/sql_quick_ref.md) | SQL query reference |
| [regular_expressions.md](programming/regular_expressions.md) | Regex syntax, common patterns |
| [git_commands.md](programming/git_commands.md) | Git commands and workflows |

### Infrastructure
| File | Description |
|------|-------------|
| [linux_commands.md](infrastructure/linux_commands.md) | Linux command line reference |
| [bash_and_shell_scripting.md](infrastructure/bash_and_shell_scripting.md) | Bash scripting, text processing |
| [docker_and_kubernetes.md](infrastructure/docker_and_kubernetes.md) | Docker, Compose, Kubernetes, Helm |
| [cloud_services_comparison.md](infrastructure/cloud_services_comparison.md) | AWS vs Azure vs GCP comparison |
| [ansible_quick_ref.md](infrastructure/ansible_quick_ref.md) | Ansible playbooks, modules, roles |
| [terraform_quick_ref.md](infrastructure/terraform_quick_ref.md) | IaC, Terraform commands, state |
| [cicd_pipeline_config.md](infrastructure/cicd_pipeline_config.md) | GitHub Actions, GitLab CI, Jenkins |
| [prometheus_and_grafana.md](infrastructure/prometheus_and_grafana.md) | PromQL, exporters, dashboards, alerting |
"""


# ── Directory creation ─────────────────────────────────────────────────────

def create_directory_structure(root: Path, lang: str, dry_run: bool = False) -> int:
    """Create the full directory tree for one language. Returns count of dirs created."""
    lang_dir = root / "knowledge_base" / lang
    created = 0

    for top_dir, subdirs in SUBDIRS.items():
        target = lang_dir / top_dir
        if not target.exists():
            if dry_run:
                print(f"  [DRY-RUN] mkdir {target.relative_to(root)}")
            else:
                target.mkdir(parents=True, exist_ok=True)
            created += 1

        for sub in subdirs:
            sub_target = target / sub
            if not sub_target.exists():
                if dry_run:
                    print(f"  [DRY-RUN] mkdir {sub_target.relative_to(root)}")
                else:
                    sub_target.mkdir(parents=True, exist_ok=True)
                created += 1

    return created


def create_readmes(
    root: Path, lang: str, lang_code: str, title: str,
    dry_run: bool = False, use_translation: bool = False,
) -> int:
    """Create README.md files for all directories. Returns count of files written."""
    lang_dir = root / "knowledge_base" / lang
    written = 0

    # Top-level README
    readme_path = lang_dir / "README.md"
    if not readme_path.exists():
        content = generate_top_level_readme(lang, lang_code, title)
        if use_translation:
            try:
                content = translate_block(content, lang_code, delay=0.1)
            except Exception as e:
                print(f"    Translation failed for top-level README: {e}")
        if dry_run:
            print(f"  [DRY-RUN] write {readme_path.relative_to(root)}")
        else:
            readme_path.write_text(content, encoding="utf-8")
        written += 1

    # Subdirectory READMEs
    for top_dir in TOP_LEVEL_DIRS:
        readme_path = lang_dir / top_dir / "README.md"
        if not readme_path.exists():
            content = generate_subdir_readme(top_dir, lang, lang_code)
            if use_translation:
                try:
                    content = translate_block(content, lang_code, delay=0.1)
                except Exception as e:
                    print(f"    Translation failed for {top_dir}/README.md: {e}")
            if dry_run:
                print(f"  [DRY-RUN] write {readme_path.relative_to(root)}")
            else:
                readme_path.write_text(content, encoding="utf-8")
            written += 1

    return written


# ── Main ──────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Set up new language directories for the knowledge base"
    )
    parser.add_argument(
        "--root", type=Path,
        default=Path(__file__).parent.parent,
        help="Repository root (default: auto-detect)",
    )
    parser.add_argument(
        "--languages", nargs="+",
        choices=sorted(NEW_LANGUAGES),
        help="Specific languages to set up (default: all 4)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show what would be created without creating",
    )
    parser.add_argument(
        "--translate", action="store_true",
        help="Translate README content via Google Translate (slow)",
    )
    args = parser.parse_args()

    languages = args.languages or list(NEW_LANGUAGES)
    root = args.root

    print(f"=== Setting up new language directories ===\n")
    print(f"  Repository root: {root}")
    print(f"  Languages: {', '.join(languages)}")
    print(f"  Dry run: {args.dry_run}")
    print(f"  Translation: {args.translate}\n")

    total_dirs = 0
    total_readmes = 0

    for lang in languages:
        lang_code = NEW_LANGUAGES[lang]
        title = TITLES[lang]
        print(f"  [{lang}] ({lang_code})")

        dirs_created = create_directory_structure(root, lang, args.dry_run)
        total_dirs += dirs_created
        print(f"    Directories: {dirs_created} created")

        readmes_written = create_readmes(
            root, lang, lang_code, title,
            dry_run=args.dry_run,
            use_translation=args.translate,
        )
        total_readmes += readmes_written
        print(f"    READMEs: {readmes_written} written")
        print()

    print(f"=== Summary ===")
    print(f"  Total directories created: {total_dirs}")
    print(f"  Total READMEs written: {total_readmes}")
    print(f"  Languages set up: {len(languages)}")
    print(f"\n  Next step: Run translation script to populate content files:")
    print(f"    python scripts/restructure_and_translate.py --root . --translate --languages {' '.join(languages)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
