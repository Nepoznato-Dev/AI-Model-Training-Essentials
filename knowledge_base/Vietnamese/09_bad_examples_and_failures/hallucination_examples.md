# Hallucination Examples

## Overview

AI hallucinations occur when language models generate information that is false, fabricated, or not grounded in reality. This document provides concrete examples of hallucinations and strategies to mitigate them.

## Types of Hallucinations

### Factual Hallucinations

**Bad Example:**
```
User: Who was the 15th President of the United States?
Assistant: The 15th President was Thomas Jefferson, who served from 1801 to 1809.
```

**Reality:** James Buchanan was the 15th President (1857-1861). Thomas Jefferson was the 3rd President.

**Why It's Bad:**
- Spreads misinformation confidently
- User may trust and propagate false information
- Damages credibility of the system

**Better Approach:**
```
User: Who was the 15th President of the United States?
Assistant: The 15th President of the United States was James Buchanan, who served from 1857 to 1861.
```

### Citation Hallucinations

**Bad Example:**
```
User: Find research about climate change impacts.
Assistant: According to Smith et al. (2023) in Nature Climate Change, 
"global temperatures will rise 5°C by 2030." 
DOI: 10.1038/s41558-023-01234-5
```

**Why It's Bad:**
- Fabricated academic citation
- Fake DOI number
- Misleading specific claim attributed to non-existent source

**Better Approach:**
```
User: Find research about climate change impacts.
Assistant: I cannot browse current research databases. However, 
I can share general knowledge about climate science. For specific 
citations, please consult academic databases like Google Scholar 
or PubMed directly.
```

### Contextual Hallucinations

**Bad Example:**
```
[Document provided discusses Q3 2023 sales figures]
User: What were the Q4 2023 sales?
Assistant: Q4 2023 sales were $4.2 million, representing a 15% increase.
```

**Why It's Bad:**
- Invented data not in source document
- Presents fabrication as fact
- Could lead to poor business decisions

**Better Approach:**
```
[Document provided discusses Q3 2023 sales figures]
User: What were the Q4 2023 sales?
Assistant: The provided document only contains Q3 2023 sales data. 
Q4 2023 figures are not included in this document.
```

### Procedural Hallucinations

**Bad Example:**
```
User: How do I reset my password on this platform?
Assistant: Click the "Settings" menu, then select "Security", 
then click "Reset Password", enter your social security number 
for verification, and submit.
```

**Why It's Bad:**
- Invented steps not in actual system
- Requests sensitive information unnecessarily
- Could confuse or compromise users

**Better Approach:**
```
User: How do I reset my password on this platform?
Assistant: I don't have access to your specific platform's 
current interface. Generally, look for a "Forgot Password" link 
on the login page, or check the platform's help documentation 
for exact steps.
```

## Real-World Scenarios

### Scenario 1: Medical Advice

**Hallucination:**
```
User: What's the treatment for condition X?
Assistant: Take 500mg of DrugY twice daily. Studies show 95% effectiveness.
```

**Risk:** Non-existent drug dosage could harm patients.

**Mitigation:**
```
Assistant: I cannot provide medical advice. Please consult a 
qualified healthcare professional for diagnosis and treatment. 
Medical decisions should be based on peer-reviewed research 
and professional guidance.
```

### Scenario 2: Legal Information

**Hallucination:**
```
User: What's the statute of limitations for contract disputes in California?
Assistant: It's 3 years according to California Civil Code Section 1234.
```

**Risk:** Incorrect legal information could cause someone to miss filing deadlines.

**Mitigation:**
```
Assistant: I can provide general information, but laws change and 
vary by jurisdiction. For California contract law, please consult 
the official California Codes or speak with a licensed attorney. 
Always verify legal information with primary sources.
```

### Scenario 3: Technical Documentation

**Hallucination:**
```
User: How do I use the new React.useOptimistic() hook?
Assistant: Pass three parameters: state, updater, and rollbackFn. 
Example: const [value, setValue] = useOptimistic(state, updater, rollbackFn);
```

**Risk:** Non-existent API causes developer confusion and wasted time.

**Mitigation:**
```
Assistant: I'm not aware of a React.useOptimistic() hook in the 
current React documentation. This might be a proposed feature or 
third-party library. Please check the official React documentation 
at react.dev for verified APIs.
```

## Detection Patterns

### Red Flags Indicating Potential Hallucination

1. **Overly Specific Details Without Sources:**
   - Exact percentages without citation
   - Specific dates for unverifiable events
   - Precise measurements without context

2. **Confident Wrongness:**
   - High confidence in verifiably false claims
   - No uncertainty markers for uncertain topics
   - Defensive tone when questioned

3. **Inconsistent Information:**
   - Contradicts previously stated facts
   - Doesn't match provided source material
   - Internal logical inconsistencies

4. **Too Perfect Answers:**
   - Conveniently exact numbers
   - Suspiciously round statistics
   - Claims that perfectly match user expectations

## Prevention Strategies

### System Design

```python
# GOOD: Implement grounding checks
def generate_response(query, source_documents=None):
    if source_documents:
        # Restrict answers to provided context
        response = rag_generate(query, source_documents)
        if not is_grounded_in_sources(response, source_documents):
            return "I cannot find that information in the provided documents."
        return response
    else:
        # Add uncertainty markers for general knowledge
        response = llm_generate(query)
        return add_uncertainty_markers(response)
```

### Output Validation

```python
def validate_claims(response):
    # Extract factual claims
    claims = extract_claims(response)
    
    # Check against known facts database
    for claim in claims:
        if not verify_claim(claim):
            flag_for_review(response)
            return add_disclaimer(response)
    
    return response
```

### User Communication

```python
def format_response_with_confidence(base_response, confidence_score):
    if confidence_score < 0.7:
        prefix = "Based on my training data, though I'm not entirely certain: "
    elif confidence_score < 0.9:
        prefix = "To the best of my knowledge: "
    else:
        prefix = ""
    
    suffix = "\n\nPlease verify important information with primary sources."
    
    return f"{prefix}{base_response}{suffix}"
```

## Testing Checklist

- [ ] Test with questions about recent events post-training cutoff
- [ ] Test requests for specific citations and verify them
- [ ] Provide source documents and ask questions outside their scope
- [ ] Ask about non-existent features/APIs
- [ ] Request medical/legal/financial advice
- [ ] Verify numerical claims independently
- [ ] Test consistency across multiple queries
- [ ] Check for invented URLs, DOIs, or reference numbers
- [ ] Validate technical specifications against official docs
- [ ] Monitor confidence levels vs accuracy

## Mitigation Techniques

### Retrieval-Augmented Generation (RAG)

```python
def rag_response(query, vector_store):
    # Retrieve relevant documents
    docs = vector_store.similarity_search(query, k=5)
    
    # Generate answer constrained to retrieved content
    prompt = f"""Answer based ONLY on these documents:
    {docs}
    
    Question: {query}
    
    If the answer isn't in the documents, say you don't know."""
    
    return llm.generate(prompt)
```

### Uncertainty Calibration

```python
def calibrated_response(query):
    # Generate multiple responses
    responses = [llm.generate(query) for _ in range(5)]
    
    # Check consistency
    if not responses_consistent(responses):
        return "I'm not confident in my answer to this question. Please verify with other sources."
    
    # Return consensus answer with appropriate caveats
    return consensus_answer(responses) + "\n\nThis information should be verified."
```

## Related Documents

- [[hallucinations]] - Main hallucinations overview
- [[misinformation_examples]] - False information handling
- [[prompt_injection_examples]] - Malicious input manipulation
- [[bad_rag]] - Poor retrieval-augmented generation implementation
- [[contradictory_sources]] - Dealing with conflicting information
