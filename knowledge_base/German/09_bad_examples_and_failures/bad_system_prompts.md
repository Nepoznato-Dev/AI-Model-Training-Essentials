# Bad System Prompts

## Overview

System prompts define the behavior, constraints, and personality of AI assistants. Bad system prompts lead to inconsistent behavior, security vulnerabilities, poor task performance, or unintended outputs. Common issues include vague instructions, missing constraints, conflicting goals, and inadequate safety guardrails.

## When to Reference This Document

- Designing AI assistant behaviors
- Configuring LLM-based applications
- Implementing safety constraints
- Debugging inconsistent model outputs
- Creating specialized AI personas

## Common System Prompt Failures

### Vague Instructions

**Bad Example**:
```
You are a helpful assistant. Be nice and answer questions.
```

**Why It's Bad**:
- No clear scope of assistance
- Undefined boundaries
- Inconsistent behavior across sessions
- No guidance on handling edge cases

**Solution**: Specific, actionable instructions
```
You are a technical support assistant for our software product.

SCOPE:
- Answer questions about product features
- Troubleshoot common errors
- Guide users through setup processes

CONSTRAINTS:
- Do not provide information about competitor products
- Do not make promises about future features
- Escalate billing questions to human agents

STYLE:
- Be concise and technical
- Use step-by-step instructions
- Include relevant documentation links
```

### Missing Safety Guardrails

**Bad Example**:
```
You are an AI assistant that answers any question honestly.
```

**Why It's Bad**:
- No protection against harmful requests
- Vulnerable to jailbreak attempts
- May reveal sensitive information
- No ethical boundaries defined

**Solution**: Explicit safety constraints
```
You are a helpful AI assistant with strict safety guidelines.

SAFETY RULES:
- Never provide instructions for illegal activities
- Do not generate hate speech, harassment, or discrimination
- Refuse requests involving self-harm or violence
- Do not reveal personal or confidential information
- Decline to write malicious code or exploits

IF UNSURE:
- When uncertain about safety, err on the side of caution
- Politely decline and explain why
- Suggest alternative, safe approaches
```

### Conflicting Goals

**Bad Example**:
```
Be extremely detailed and comprehensive in your answers.
Also keep responses short and concise.
Always prioritize user satisfaction above all else.
But never compromise on accuracy.
```

**Why It's Bad**:
- Creates internal conflict
- Unpredictable prioritization
- Frustrating user experience
- Model may ignore some instructions

**Solution**: Clear priority hierarchy
```
Response priorities (in order):
1. ACCURACY: Information must be factually correct
2. SAFETY: Never compromise safety guidelines
3. CLARITY: Explain concepts clearly and simply
4. CONCISENESS: Be brief while maintaining completeness
5. DETAIL: Provide examples when helpful

When priorities conflict:
- Accuracy always trumps brevity
- Safety overrides all other concerns
- Ask clarifying questions if requirements are unclear
```

### No Persona Definition

**Bad Example**:
```
Answer user questions.
```

**Why It's Bad**:
- Inconsistent tone and style
- No domain expertise signaled
- Unclear communication style
- Poor user expectation setting

**Solution**: Define clear persona
```
PERSONA: Senior Software Engineer

EXPERTISE:
- Python, JavaScript, Go programming
- Cloud architecture (AWS, GCP)
- Database design and optimization
- API design best practices

COMMUNICATION STYLE:
- Professional but approachable
- Use technical terms appropriately
- Provide code examples when relevant
- Explain trade-offs in design decisions

LIMITATIONS:
- Acknowledge when unsure
- Admit knowledge gaps honestly
- Suggest consulting documentation for edge cases
```

### Overly Restrictive Prompts

**Bad Example**:
```
Only answer questions about topic X.
Use exactly this format for every response.
Never deviate from these exact words.
Do not add any additional information.
Never ask clarifying questions.
```

**Why It's Bad**:
- Cannot handle edge cases
- Frustrating for users
- Misses opportunities to help
- Brittle to variations

**Solution**: Balanced flexibility
```
PRIMARY FOCUS: Topic X (software development)

FLEXIBILITY:
- You may address related topics when relevant
- Adapt format to suit the question type
- Add context when it improves understanding
- Ask clarifying questions when needed

GUIDELINES:
- Stay on topic but be helpful
- Use appropriate formats (code, lists, prose)
- Provide context for complex answers
- Seek clarification for ambiguous requests
```

### Missing Context Handling

**Bad Example**:
```
You are a customer service bot. Help customers.
```

**Why It's Bad**:
- No guidance on conversation history
- Cannot handle multi-turn conversations
- Forgets previous context
- Repetitive responses

**Solution**: Context-aware instructions
```
CONVERSATION HANDLING:

CONTEXT USAGE:
- Reference previous messages when relevant
- Maintain consistency across turns
- Remember user preferences mentioned earlier
- Build on previous explanations

MULTI-TURN STRATEGY:
- Acknowledge previous points before continuing
- Track unresolved questions
- Summarize long conversations periodically
- Know when to restart or redirect

CONTEXT LIMITS:
- If conversation exceeds context window, summarize key points
- Prioritize recent messages over older ones
- Flag when important context may be lost
```

## Real-World Scenarios

### Scenario 1: Healthcare Chatbot
Missing safety guardrails allow chatbot to provide dangerous medical advice, leading to potential harm.

### Scenario 2: Financial Advisor AI
Vague instructions cause inconsistent investment recommendations, eroding user trust.

### Scenario 3: Educational Tutor
Overly restrictive prompt prevents tutor from adapting to different learning styles and student needs.

## Detection Patterns

Watch for these warning signs:
- Inconsistent responses to similar questions
- Security vulnerabilities exploited
- Off-topic or inappropriate content
- Ignoring stated constraints
- Confusing or contradictory outputs
- Poor handling of edge cases

## Prevention Strategies

1. **Be Specific**: Clear, actionable instructions
2. **Define Boundaries**: Explicit scope and limitations
3. **Prioritize Constraints**: Hierarchy for conflicts
4. **Include Safety**: Guardrails for harmful content
5. **Test Extensively**: Edge cases and adversarial inputs
6. **Iterate**: Refine based on observed behavior
7. **Monitor**: Track outputs for drift or issues

## Testing Checklist

- [ ] Are instructions specific and actionable?
- [ ] Are safety guardrails clearly defined?
- [ ] Is there a priority hierarchy for conflicts?
- [ ] Is the persona well-defined?
- [ ] Is there appropriate flexibility?
- [ ] Does it handle multi-turn conversations?
- [ ] Has it been tested with adversarial inputs?

## Related Documents

- [[bad_agent_design]] - System prompts guide agent behavior
- [[prompt_injection_examples]] - Vulnerabilities from weak prompts
- [[hallucination_examples]] - How prompts affect accuracy
- [[misinformation_examples]] - Preventing false information
