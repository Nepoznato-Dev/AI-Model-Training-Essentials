---
# Metadata
title: "Prompt Engineering"
description: "Designing, refining, and optimizing effective prompts for large language models to produce accurate, relevant, and consistent outputs."
category: "Behavior Skills"
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
reviewed_by: "Behavior Skills Team"
next_review: "2027-02-10"

# Classification
tags: [prompt-engineering, llm, ai-interaction, few-shot, chain-of-thought, instruction-design]
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

# Prompt Engineering

The practice of designing, refining, and optimizing inputs to large language models (LLMs) so that outputs are accurate, relevant, and consistent across varied contexts.

## Overview

Prompt engineering is the discipline of crafting instructions that guide AI models toward desired outcomes without modifying model weights. As LLMs become central to software development, research, content creation, and automation, the quality of the prompt directly determines the quality of the output.

A well-engineered prompt reduces hallucination, enforces format constraints, controls tone and style, and makes multi-step reasoning tractable. This skill covers the core techniques, design patterns, and iterative processes needed to write prompts that are reliable enough for production use.

The importance of this skill has grown alongside model capability: more capable models are also more sensitive to instruction phrasing, making prompt design a lever that amplifies or wastes that capability.

## Core Competencies

- Writing clear, unambiguous instructions that models can follow consistently
- Selecting and applying prompting techniques (zero-shot, few-shot, chain-of-thought, role prompting)
- Structuring prompts with explicit output format constraints
- Iterating on prompts based on observed failure modes
- Evaluating prompt quality systematically across edge cases
- Combining multiple techniques into composite prompt strategies
- Adapting prompts to different model families and their behavioral tendencies

## When to Use

- Interacting with any LLM-based API or assistant in a production workflow
- Building automated pipelines where LLM output feeds downstream systems
- Designing system prompts or agent instructions for AI-powered tools
- Debugging inconsistent or incorrect LLM outputs
- Creating evaluation datasets that require controlled model behavior
- Onboarding teammates to effective AI-assisted workflows
- Building RAG systems where retrieval context must be integrated into prompts

## Framework/Methodology

### Phase 1: Task Analysis

Before writing a prompt, clarify three things:

1. **What is the exact desired output?** Define the format (JSON, Markdown, plain text), length constraints, and required fields.
2. **What context does the model need?** Identify the minimum information the model must have to succeed — no more, no less.
3. **What are the failure modes?** Think about what wrong answers look like. Hallucinations? Format violations? Off-topic responses? This drives your constraints.

### Phase 2: Technique Selection

| Technique | When to Use | Example |
|-----------|-------------|---------|
| Zero-shot | Task is simple and unambiguous | "Classify this email as spam or not spam: ..." |
| Few-shot | Task requires a specific format or pattern | Provide 2-3 input/output examples before the actual query |
| Chain-of-thought (CoT) | Task requires multi-step reasoning | "Think step by step before answering" |
| Role prompting | Output should reflect a specific perspective or expertise | "You are a senior backend engineer reviewing this code..." |
| Structured output | Downstream systems need parseable results | "Return your answer as a JSON object with keys: ..." |
| Constraint prompting | Output must obey strict rules | "Answer in exactly 3 sentences. Do not mention X." |
| Decomposition | Complex task can be split into subtasks | "First list the requirements, then write the function, then add tests" |

### Phase 3: Prompt Construction

Assemble the prompt in this order:

1. **System instruction** — role, tone, behavioral constraints
2. **Context** — retrieved documents, conversation history, or background facts
3. **Task instruction** — the specific question or action
4. **Output format** — explicit schema or structural requirements
5. **Examples** (if few-shot) — representative input/output pairs

### Phase 4: Iteration & Evaluation

1. Run the prompt against 10-20 representative inputs
2. Categorize failures: format errors, factual errors, tone violations, incomplete outputs
3. Add targeted constraints to address each failure category
4. Re-test — each added constraint should fix failures without introducing new ones
5. Stop when the prompt passes your acceptance threshold (typically >90% on representative inputs)

## Practical Templates

### Template 1: Structured Extraction Prompt

```
You are a data extraction assistant. Your task is to extract structured information from the provided text.

## Output Format
Return a JSON object with the following keys:
- "entities": array of { "name": string, "type": string }
- "relationships": array of { "source": string, "target": string, "relation": string }
- "summary": string (max 2 sentences)

## Rules
- Only extract information explicitly stated in the text
- If a field cannot be populated, use null (do not guess)
- Keep entity types from this list: person, organization, location, product, event

## Input Text
{input_text}
```

### Template 2: Chain-of-Thought Analysis Prompt

```
You are an analytical assistant. Analyze the following problem step by step.

## Instructions
1. First, restate the problem in your own words
2. List the key facts and constraints
3. Consider at least two possible approaches
4. Select the best approach and explain why
5. Provide your final answer

## Problem
{problem_statement}
```

### Template 3: Few-Shot Classification Prompt

```
Classify the sentiment of the given text as "positive", "negative", or "neutral".

Examples:
Text: "The new update fixed all the bugs I was having." → positive
Text: "I've been waiting three weeks for a response." → negative
Text: "The package arrived on Tuesday as expected." → neutral

Text: "{input_text}" →
```

### Template 4: RAG Context Integration Prompt

```
You are a helpful assistant. Answer the user's question using only the information provided in the context below.

## Context
{retrieved_context}

## Rules
- If the answer is not in the context, say "I don't have enough information to answer that."
- Cite the relevant section of the context when possible
- Do not add information beyond what the context provides

## Question
{user_question}
```

## Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Vague instructions ("be helpful") | Model interprets broadly, output is inconsistent | Use specific, measurable constraints |
| Overloading a single prompt with multiple tasks | Each task gets less attention, quality drops | Decompose into sequential prompts or use clear section headers |
| Providing too much context | Model loses track of relevant information (lost-in-the-middle) | Place critical information at the beginning and end; summarize when possible |
| No output format specification | Responses vary in structure, breaking downstream parsing | Always specify the expected format explicitly with an example |
| Ignoring model-specific behavior | Techniques that work on one model may fail on another | Test prompts across target models; maintain model-specific prompt variants |
| Prompting without evaluation | No way to detect regressions when prompt changes | Always build a small evaluation set before finalizing a prompt |

## Best Practices

1. **Start simple, add complexity only when needed.** A clear one-sentence instruction outperforms a convoluted multi-paragraph prompt for simple tasks.
2. **Use explicit delimiters** to separate instructions, context, and input data. Markdown headers, XML tags, or triple backticks all help models parse structure.
3. **Specify what NOT to do** alongside what to do. Negative constraints ("Do not include disclaimers") are as important as positive ones.
4. **Version your prompts.** Treat prompts like code — track changes, test before deploying, and maintain a changelog.
5. **Build evaluation sets early.** Even 10-20 test cases let you measure whether a prompt change helped or hurt.
6. **Use system messages for stable instructions** and user messages for variable content. This separation maps to how most LLM APIs process context.
7. **Test edge cases deliberately.** Include adversarial inputs, empty inputs, and inputs that nearly match but should produce different outputs.

## Tools & Resources

- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering) - Comprehensive guide from Anthropic on prompt design
- [OpenAI Prompt Engineering Best Practices](https://platform.openai.com/docs/guides/prompt-engineering) - Official OpenAI recommendations
- [LangChain Prompt Templates](https://python.langchain.com/docs/concepts/prompt_templates/) - Programmatic prompt construction with variable injection
- [PromptFoo](https://promptfoo.dev/) - Open-source tool for systematic prompt evaluation and comparison
- [Chain-of-Thought Prompting (Wei et al., 2022)](https://arxiv.org/abs/2201.11903) - Foundational paper on CoT reasoning
- [DSPy](https://github.com/stanfordnlp/dspy) - Framework for programming (not prompting) language models with optimized prompt compilation

## Example Application

**Scenario**: A team is building a customer support bot that must classify incoming tickets into categories, extract relevant metadata, and draft responses — all from raw email text.

**Application**:

1. *Task analysis* — Three subtasks identified: classification (fixed categories), metadata extraction (customer name, order ID, urgency), response drafting (polite, concise, action-oriented).

2. *Technique selection* — Few-shot for classification (5 examples per category), structured output for metadata (JSON schema), role prompting for response drafting ("You are a senior support agent...").

3. *Prompt construction* — Three separate prompts are designed rather than one combined prompt, because each subtask has different failure modes and evaluation criteria.

4. *Iteration* — Initial prompts achieve 78% classification accuracy. Analysis shows confusion between "billing" and "account" categories. Adding two contrastive examples (similar text, different category) improves accuracy to 94%.

**Outcome**: The decomposed prompt strategy achieves reliable classification (>90%), clean JSON extraction that integrates with the ticketing system, and response drafts that require minimal human editing — reducing average ticket handling time by 40%.

## Success Indicators

You know you've mastered prompt engineering when:

- You can consistently achieve >90% accuracy on structured extraction tasks with proper evaluation
- You instinctively decompose complex LLM tasks into focused sub-prompts before writing
- Your prompts include explicit format constraints and negative rules by default
- You maintain evaluation sets and measure prompt changes quantitatively
- You can explain why a specific technique (CoT, few-shot, decomposition) is appropriate for a given task
- Your prompts are portable across model families with minimal adjustment
- Downstream systems receive consistently well-formatted output without post-processing fixes

## Related Skills

- [Writing](writing.md) - Clear written communication complements prompt design
- [Explanation](explanation.md) - Understanding how to explain things improves instruction design
- [Debugging](debugging.md) - Systematic investigation applies to prompt failure analysis
- [Planning](planning.md) - Task decomposition skills transfer directly to prompt decomposition
- [Summarization](summarization.md) - Context compression is essential for effective RAG prompts
