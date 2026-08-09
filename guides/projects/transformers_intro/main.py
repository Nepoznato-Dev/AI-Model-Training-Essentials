# Transformers Introduction - Main Script
# A minimal, heavily-commented introduction to using pre-trained transformer models
# Lines of code: ~180 (including comments)

# ============================================================================
# STEP 1: IMPORT REQUIRED LIBRARIES
# ============================================================================

from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch

print("=" * 70)
print("TRANSFORMERS INTRODUCTION PROJECT")
print("=" * 70)
print()

# ============================================================================
# STEP 2: LOAD A PRE-TRAINED MODEL USING PIPELINE
# ============================================================================

# The pipeline API is the easiest way to use transformers
# It automatically handles:
# - Model loading
# - Tokenization
# - Inference
# - Post-processing

print("Loading pre-trained sentiment analysis model...")
print("(First run will download the model, this may take a minute)")
print()

classifier = pipeline("sentiment-analysis")

print(f"✓ Model loaded successfully!")
print(f"  Model: {classifier.model.__class__.__name__}")
print(f"  Device: {classifier.device}")
print()

# ============================================================================
# STEP 3: SINGLE TEXT PREDICTION
# ============================================================================

print("-" * 70)
print("EXAMPLE 1: Single Text Prediction")
print("-" * 70)

text = "I absolutely love this product! Best purchase ever."
print(f"Input text: {text}")
print()

result = classifier(text)
print(f"Prediction: {result}")
print(f"Sentiment: {result[0]['label']}")
print(f"Confidence: {result[0]['score']:.2%}")
print()

# ============================================================================
# STEP 4: BATCH PROCESSING
# ============================================================================

print("-" * 70)
print("EXAMPLE 2: Batch Processing Multiple Texts")
print("-" * 70)

texts = [
    "This is amazing! I'm so happy with it.",
    "Terrible experience, would not recommend to anyone.",
    "It's okay, nothing special but does the job.",
    "Worst product I've ever bought. Complete waste of money!",
    "Exceeded my expectations! Highly recommend!"
]

print(f"Processing {len(texts)} texts...\n")

results = classifier(texts)

for i, (sample_text, result) in enumerate(zip(texts, results), 1):
    print(f"{i}. Text: {sample_text}")
    print(f"   Sentiment: {result['label']}")
    print(f"   Confidence: {result['score']:.2%}")
    print()

# ============================================================================
# STEP 5: UNDERSTANDING TOKENIZATION
# ============================================================================

print("-" * 70)
print("EXAMPLE 3: Understanding Tokenization")
print("-" * 70)

# Tokenizers convert text into numbers that the model can understand
# Let's see what happens behind the scenes

tokenizer = classifier.tokenizer

sample_text = "I love transformers!"
print(f"Original text: {sample_text}")
print()

# Tokenize the text
tokens = tokenizer.tokenize(sample_text)
print(f"Tokens: {tokens}")
print()

# Convert to token IDs
token_ids = tokenizer.encode(sample_text)
print(f"Token IDs: {token_ids}")
print()

# Show the mapping
print("Token → ID mapping:")
for token, token_id in zip(tokens, token_ids[1:-1]):  # Skip [CLS] and [SEP]
    print(f"  {token:15} → {token_id}")
print()

# ============================================================================
# STEP 6: TRYING DIFFERENT MODELS
# ============================================================================

print("-" * 70)
print("EXAMPLE 4: Using Different Pre-trained Models")
print("-" * 70)

# Hugging Face has thousands of pre-trained models
# Let's try a different sentiment analysis model

print("Loading alternative model: cardiffnlp/twitter-roberta-base-sentiment")
print("(This model was trained on Twitter data)")
print()

try:
    twitter_classifier = pipeline(
        "sentiment-analysis", 
        model="cardiffnlp/twitter-roberta-base-sentiment"
    )
    
    test_texts = [
        "This is lit! 🔥",
        "Not gonna lie, pretty disappointed",
        "Meh, it's alright I guess"
    ]
    
    print("Testing on informal/social media style text:\n")
    
    for sample_text in test_texts:
        result = twitter_classifier(sample_text)[0]
        print(f"Text: {sample_text}")
        print(f"Sentiment: {result['label']} ({result['score']:.2%})")
        print()
        
except Exception as e:
    print(f"Could not load alternative model: {e}")
    print("This is okay! The default model works fine for most cases.")
    print()

# ============================================================================
# STEP 7: EXPLORING OTHER TASKS
# ============================================================================

print("-" * 70)
print("EXAMPLE 5: Other Transformer Tasks")
print("-" * 70)

# Transformers can do much more than sentiment analysis!
# Here are some examples:

# Task 1: Question Answering
print("\n1. QUESTION ANSWERING")
qa_pipeline = pipeline("question-answering")
context = """
The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France.
It is named after the engineer Gustave Eiffel, whose company designed and built the tower.
Constructed from 1887 to 1889, it was originally criticized by some of France's leading 
artists and intellectuals for its design, but it has since become a global cultural icon.
"""
question = "Who is the tower named after?"

qa_result = qa_pipeline(question=question, context=context)
print(f"Question: {question}")
print(f"Answer: {qa_result['answer']}")
print(f"Confidence: {qa_result['score']:.2%}")

# Task 2: Zero-Shot Classification
print("\n2. ZERO-SHOT CLASSIFICATION")
zero_shot = pipeline("zero-shot-classification")
sequence = "I just ran my first marathon and finished in under 4 hours!"
candidate_labels = ["sports", "politics", "technology", "entertainment"]

zs_result = zero_shot(sequence, candidate_labels)
print(f"Text: {sequence}")
print(f"Predicted category: {zs_result['labels'][0]} ({zs_result['scores'][0]:.2%})")

# Task 3: Summarization
print("\n3. SUMMARIZATION")
summarizer = pipeline("summarization")
long_text = """
Artificial intelligence is intelligence demonstrated by machines, as opposed to natural 
intelligence displayed by animals including humans. Leading AI textbooks define the field 
as the study of intelligent agents: any device that perceives its environment and takes 
actions that maximize its chance of successfully achieving its goals. Colloquially, the 
term artificial intelligence is often used to describe machines that mimic cognitive 
functions humans associate with the human mind, such as learning and problem solving.
"""

summary = summarizer(long_text, max_length=50, min_length=25)
print(f"Original length: {len(long_text)} characters")
print(f"Summary: {summary[0]['summary_text']}")

# ============================================================================
# STEP 8: PRACTICAL EXAMPLE - BUILD A SIMPLE SENTIMENT ANALYZER
# ============================================================================

print("\n" + "=" * 70)
print("BONUS: Build Your Own Sentiment Analyzer Function")
print("=" * 70)

def analyze_sentiment(text, threshold=0.7):
    """
    Analyze sentiment of a text and return emoji based on result.
    
    Args:
        text: Input text to analyze
        threshold: Confidence threshold (default 0.7)
    
    Returns:
        Dictionary with sentiment, confidence, and emoji
    """
    result = classifier(text)[0]
    sentiment = result['label']
    confidence = result['score']
    
    # Assign emoji based on sentiment
    if sentiment == "POSITIVE":
        emoji = "😊"
    elif sentiment == "NEGATIVE":
        emoji = "😞"
    else:
        emoji = "😐"
    
    # Check if model is uncertain
    if confidence < threshold:
        emoji = "🤔"  # Uncertain
    
    return {
        'text': text,
        'sentiment': sentiment,
        'confidence': confidence,
        'emoji': emoji
    }

# Test our custom function
print("\nTesting custom sentiment analyzer:\n")

test_cases = [
    "I'm having a wonderful day!",
    "This is the worst thing ever",
    "The weather is okay today"
]

for text in test_cases:
    result = analyze_sentiment(text)
    print(f"{result['emoji']} {result['sentiment']} ({result['confidence']:.2%})")
    print(f"   Text: {result['text']}")
    print()

# ============================================================================
# CONCLUSION
# ============================================================================

print("=" * 70)
print("CONGRATULATIONS! You've completed the Transformers Introduction!")
print("=" * 70)
print("""
What you learned:
✓ How to load pre-trained transformer models
✓ How to make predictions with the pipeline API
✓ How tokenization works
✓ How to try different models
✓ Other transformer tasks (QA, classification, summarization)
✓ How to build a simple application

Next steps:
1. Read the full Transformers Guide in /guides/Transformers/
2. Try fine-tuning a model on your own data
3. Explore the Hugging Face Model Hub
4. Build a real application with transformers

Resources:
- Hugging Face Documentation: https://huggingface.co/docs/transformers
- Model Hub: https://huggingface.co/models
- Free Course: https://huggingface.co/course
""")
print("=" * 70)
