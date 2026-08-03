# Chapter 5: Training Generator Models for RAG

## 5.1 Introduction to RAG Generators

Now that you understand how to build complete RAG systems (Chapter 4), let's dive deep into training the generator component. The generator is what produces the final response that users see, so getting it right is crucial.

### What Does a Generator Do?

Think of the generator as the "speaker" in your RAG system. After the retriever finds relevant documents, the generator's job is to:

1. **Understand the context**: Read and comprehend the retrieved documents
2. **Find the answer**: Locate relevant information within that context
3. **Formulate a response**: Express the answer in natural, helpful language
4. **Stay grounded**: Only say what's supported by the provided context

This might sound straightforward, but there are many challenges. Let's explore them together.

### Why Fine-tune a Generator?

You might wonder: "Can't I just use a pre-trained model like BART or T5?" 

Yes, you can—and for many applications, that works well! However, fine-tuning offers several advantages:

**1. Domain Adaptation**: Pre-trained models know about general topics, but your application might use specialized terminology (medical, legal, technical). Fine-tuning helps the model learn your domain's language.

**2. Format Consistency**: Different applications have different output requirements. Some need concise answers, others need detailed explanations. Fine-tuning teaches the model your preferred style.

**3. Reduced Hallucination**: Generic models sometimes make things up. Fine-tuning on high-quality Q&A data teaches the model to stick to the provided context.

**4. Better Context Utilization**: A fine-tuned model learns which parts of retrieved documents matter most for your specific task.

**Realistic Expectations**: Fine-tuning typically improves performance by 10-25% compared to zero-shot usage, but it requires careful data preparation and compute resources. Weigh the benefits against your needs.

## 5.2 Model Architecture Selection

Before we start coding, let's understand the two main types of language models you can use as generators. Each has strengths and trade-offs.

### Encoder-Decoder Models (Recommended for Most RAG Tasks)

Encoder-decoder models (also called sequence-to-sequence or seq2seq models) have two components:
- **Encoder**: Processes the input (query + context) into a rich representation
- **Decoder**: Generates the output token-by-token based on that representation

**Popular Examples**: BART, T5, FLAN-T5, mT5

**Why They're Great for RAG**:
1. **Natural Fit**: The encoder handles long contexts well, while the decoder focuses on generation
2. **Training Efficiency**: Can be trained with standard teacher-forcing
3. **Proven Performance**: These models dominate Q&A benchmarks
4. **Flexible Input Length**: Can handle varying context sizes

Here's what working with an encoder-decoder looks like:

```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class RAGGenerator:
    """
    Generator using an encoder-decoder architecture.
    
    This class shows the basic pattern for using models like BART or T5.
    """
    def __init__(self, model_name='facebook/bart-large'):
        """
        Initialize with a pre-trained model.
        
        Args:
            model_name: Hugging Face model identifier
        """
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    def prepare_input(self, query: str, contexts: list[str], 
                     max_context_length: int = 2048):
        """
        Format query and contexts into model input.
        
        Key insight: How you format the input significantly impacts performance.
        Clear structure helps the model understand what's question vs. context.
        """
        # Concatenate all retrieved contexts
        combined_context = ' '.join(contexts)
        
        # Truncate if too long (important to avoid exceeding model limits)
        tokens = self.tokenizer.encode(combined_context, truncation=True, 
                                       max_length=max_context_length)
        combined_context = self.tokenizer.decode(tokens, skip_special_tokens=True)
        
        # Create structured input
        # The format matters! Be consistent between training and inference
        input_text = f"Question: {query}\nContext: {combined_context}\nAnswer:"
        return input_text
    
    def generate(self, query: str, contexts: list[str], 
                max_length: int = 256, num_beams: int = 4):
        """
        Generate an answer given query and retrieved contexts.
        
        Args:
            query: User's question
            contexts: List of retrieved document texts
            max_length: Maximum length of generated answer
            num_beams: Beam search width (higher = better quality, slower)
            
        Returns:
            Generated answer string
        """
        # Prepare formatted input
        input_text = self.prepare_input(query, contexts)
        
        # Tokenize
        inputs = self.tokenizer(
            input_text,
            return_tensors='pt',
            truncation=True,
            max_length=2048
        )
        
        # Generate with beam search
        # Beam search explores multiple possible sequences simultaneously
        outputs = self.model.generate(
            **inputs,
            max_length=max_length,
            num_beams=num_beams,
            early_stopping=True,  # Stop when all beams finish
            no_repeat_ngram_size=3  # Avoid repetitive phrases
        )
        
        # Decode back to text
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
```

**Understanding Generation Parameters**:
- `max_length`: Controls how long answers can be. Too short cuts off responses; too long wastes compute.
- `num_beams`: Beam search width. Higher values (4-8) improve quality but slow down generation.
- `early_stopping`: When True, stops as soon as all beams complete—saves time.
- `no_repeat_ngram_size`: Prevents the model from getting stuck in loops.

### Decoder-Only Models

Decoder-only models (also called causal language models) generate text by predicting the next token based on all previous tokens. They've become extremely popular with models like GPT, LLaMA, and Mistral.

**Popular Examples**: LLaMA, Mistral, GPT-J, Falcon

**When to Choose Decoder-Only**:
1. **You need a general-purpose model**: These excel at many tasks beyond Q&A
2. **Large-scale deployment**: Often more efficient at inference time
3. **Instruction following**: Modern variants are excellent at following complex instructions
4. **You want one model for everything**: Can handle retrieval, generation, and other tasks

**Trade-offs vs. Encoder-Decoder**:
- ✓ Better at open-ended generation
- ✓ More flexible prompting
- ✗ Can be harder to control (more hallucination risk)
- ✗ Typically larger and slower for pure Q&A tasks

Here's how to work with decoder-only models:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class CausalRAGGenerator:
    """
    Generator using a decoder-only (causal) architecture.
    
    Best for: Large models like LLaMA, Mistral that excel at instruction following.
    """
    def __init__(self, model_name='meta-llama/Llama-2-7b-hf'):
        """
        Initialize with a pre-trained causal LM.
        
        Note: Large models require significant GPU memory. Consider quantization
        or smaller variants for resource-constrained environments.
        """
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map='auto',  # Automatically use available GPUs
            torch_dtype=torch.float16  # Half precision saves memory
        )
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Set pad token (required for batched generation)
        self.tokenizer.pad_token = self.tokenizer.eos_token
    
    def create_prompt(self, query: str, contexts: list[str]):
        """
        Create an instruction-style prompt for the model.
        
        Key insight: Decoder-only models are sensitive to prompt format.
        Clear instructions help the model understand what's expected.
        """
        prompt_template = """
### Instruction:
Answer the following question using only the provided context. If the answer cannot be found in the context, state that you don't know.

### Context:
{context}

### Question:
{question}

### Answer:
"""
        combined_context = '\n'.join(contexts)
        return prompt_template.format(context=combined_context, question=query)
    
    def generate(self, query: str, contexts: list[str], **kwargs):
        """
        Generate an answer using sampling-based decoding.
        
        Unlike encoder-decoder models which often use beam search,
        decoder-only models typically use sampling for more natural outputs.
        """
        # Create the full prompt
        prompt = self.create_prompt(query, contexts)
        
        # Tokenize
        inputs = self.tokenizer(
            prompt,
            return_tensors='pt',
            truncation=True,
            max_length=4096  # Decoder-only models often support longer contexts
        ).to(self.model.device)
        
        # Generate with sampling
        # Sampling produces more diverse, natural-sounding text
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=256,  # Limit new tokens (not total length)
            do_sample=True,  # Enable sampling (not greedy)
            temperature=0.7,  # Controls randomness (higher = more creative)
            top_p=0.9,  # Nucleus sampling: sample from top 90% probability mass
            pad_token_id=self.tokenizer.eos_token_id
        )
        
        # Extract only the generated part (not the prompt)
        # This is important: we want just the answer, not question + context
        generated = outputs[0][inputs['input_ids'].shape[1]:]
        response = self.tokenizer.decode(generated, skip_special_tokens=True)
        
        return response.strip()
```

**Understanding Sampling Parameters**:
- `temperature`: Controls randomness. Lower (0.2-0.5) = more focused; Higher (0.7-1.0) = more creative
- `top_p` (nucleus sampling): Only sample from tokens comprising top P% of probability. Prevents weird outliers.
- `max_new_tokens`: Limits how much new text is generated (different from max_length!)
- `do_sample`: Must be True for temperature/top_p to have effect

**Encoder-Decoder vs. Decoder-Only: Quick Comparison**

| Aspect | Encoder-Decoder | Decoder-Only |
|--------|----------------|--------------|
| Best for | Focused Q&A tasks | General-purpose applications |
| Training | Easier to fine-tune | Requires more data/care |
| Inference speed | Faster for short answers | Slower but more flexible |
| Control | Easier to constrain | Needs careful prompting |
| Model size | Typically smaller | Often larger |
| Hallucination | Lower risk | Higher risk (needs mitigation) |

**Recommendation**: Start with encoder-decoder (like FLAN-T5) for pure Q&A. Use decoder-only if you need multi-task capabilities or are already invested in that ecosystem.

## 5.3 Preparing Generation Training Data

### Format for Fine-tuning

```python
from typing import List, Dict
import json

class RAGGenerationDataset:
    def __init__(self):
        self.data = []
    
    def add_example(self, query: str, contexts: List[str], 
                   answer: str, metadata: Dict = None):
        example = {
            'query': query,
            'contexts': contexts,
            'answer': answer,
            'metadata': metadata or {}
        }
        self.data.append(example)
    
    def create_training_pair(self, example: Dict) -> Dict:
        """Convert example to model input-output pair."""
        input_text = f"Question: {example['query']}\nContext: {' '.join(example['contexts'])}"
        output_text = example['answer']
        
        return {
            'input': input_text,
            'output': output_text
        }
    
    def save_to_jsonl(self, filepath: str):
        with open(filepath, 'w') as f:
            for example in self.data:
                f.write(json.dumps(example) + '\n')
    
    @classmethod
    def load_from_jsonl(cls, filepath: str):
        dataset = cls()
        with open(filepath, 'r') as f:
            for line in f:
                dataset.data.append(json.loads(line))
        return dataset
```

### Data Augmentation for Generation

```python
from transformers import pipeline

class GenerationDataAugmenter:
    def __init__(self):
        self.question_generator = pipeline(
            "text2text-generation",
            model="t5-base"
        )
    
    def generate_variants(self, query: str, context: str, 
                         answer: str, num_variants: int = 3):
        variants = []
        
        for i in range(num_variants):
            # Paraphrase the question
            paraphrased = self.question_generator(
                f"paraphrase: {query}",
                max_length=64
            )[0]['generated_text']
            
            variants.append({
                'query': paraphrased,
                'contexts': [context],
                'answer': answer
            })
        
        return variants
    
    def create_negative_examples(self, query: str, context: str, 
                                wrong_answer: str):
        """Create examples where answer is not in context."""
        return {
            'query': query,
            'contexts': [context],
            'answer': "I don't have enough information to answer this question based on the provided context."
        }
```

## 4.4 Fine-tuning Implementation

### Complete Training Pipeline

```python
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import (
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    TrainingArguments,
    Trainer,
    DataCollatorForSeq2Seq
)
from datasets import Dataset as HFDataset

class RAGFineTuningDataset(Dataset):
    def __init__(self, data: List[Dict], tokenizer, max_input_length: int = 2048,
                 max_output_length: int = 256):
        self.data = data
        self.tokenizer = tokenizer
        self.max_input_length = max_input_length
        self.max_output_length = max_output_length
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        example = self.data[idx]
        
        # Prepare input
        input_text = f"Question: {example['query']}\nContext: {' '.join(example['contexts'])}"
        
        # Tokenize input
        input_encodings = self.tokenizer(
            input_text,
            truncation=True,
            max_length=self.max_input_length,
            padding='max_length'
        )
        
        # Tokenize output
        output_encodings = self.tokenizer(
            example['answer'],
            truncation=True,
            max_length=self.max_output_length,
            padding='max_length'
        )
        
        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': output_encodings['input_ids']
        }

class RAGGeneratorTrainer:
    def __init__(self, model_name: str = 'facebook/bart-large',
                 learning_rate: float = 3e-5,
                 batch_size: int = 8,
                 num_epochs: int = 3,
                 max_input_length: int = 2048,
                 max_output_length: int = 256):
        
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.batch_size = batch_size
        self.num_epochs = num_epochs
        self.max_input_length = max_input_length
        self.max_output_length = max_output_length
        
        # Load model and tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        
        # Set pad token
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
            self.model.config.pad_token_id = self.tokenizer.eos_token_id
    
    def prepare_dataset(self, train_data: List[Dict], 
                       val_data: List[Dict] = None):
        train_dataset = RAGFineTuningDataset(
            train_data,
            self.tokenizer,
            self.max_input_length,
            self.max_output_length
        )
        
        val_dataset = None
        if val_data:
            val_dataset = RAGFineTuningDataset(
                val_data,
                self.tokenizer,
                self.max_input_length,
                self.max_output_length
            )
        
        return train_dataset, val_dataset
    
    def train(self, train_data: List[Dict], val_data: List[Dict] = None,
             output_dir: str = './rag_generator'):
        
        train_dataset, val_dataset = self.prepare_dataset(train_data, val_data)
        
        # Data collator
        data_collator = DataCollatorForSeq2Seq(
            self.tokenizer,
            model=self.model,
            padding=True
        )
        
        # Training arguments
        training_args = TrainingArguments(
            output_dir=output_dir,
            num_train_epochs=self.num_epochs,
            per_device_train_batch_size=self.batch_size,
            per_device_eval_batch_size=self.batch_size * 2,
            learning_rate=self.learning_rate,
            weight_decay=0.01,
            warmup_ratio=0.1,
            logging_steps=50,
            eval_strategy='epoch' if val_dataset else 'no',
            save_strategy='epoch',
            load_best_model_at_end=True,
            fp16=torch.cuda.is_available(),
            gradient_accumulation_steps=4,
            report_to='none'
        )
        
        # Initialize trainer
        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=val_dataset,
            data_collator=data_collator,
            tokenizer=self.tokenizer
        )
        
        # Train
        trainer.train()
        
        # Save model
        trainer.save_model(output_dir)
        self.tokenizer.save_pretrained(output_dir)
        
        return trainer
    
    def evaluate(self, test_data: List[Dict], metrics: List[str] = ['rouge', 'bleu']):
        from evaluate import load
        
        # Load metrics
        rouge_metric = load('rouge') if 'rouge' in metrics else None
        bleu_metric = load('bleu') if 'bleu' in metrics else None
        
        predictions = []
        references = []
        
        self.model.eval()
        with torch.no_grad():
            for example in test_data:
                input_text = f"Question: {example['query']}\nContext: {' '.join(example['contexts'])}"
                
                inputs = self.tokenizer(
                    input_text,
                    return_tensors='pt',
                    truncation=True,
                    max_length=self.max_input_length
                ).to(self.model.device)
                
                outputs = self.model.generate(
                    **inputs,
                    max_length=self.max_output_length,
                    num_beams=4,
                    early_stopping=True
                )
                
                pred = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
                predictions.append(pred)
                references.append(example['answer'])
        
        # Calculate metrics
        results = {}
        if rouge_metric:
            rouge_results = rouge_metric.compute(predictions=predictions, references=references)
            results.update(rouge_results)
        
        if bleu_metric:
            bleu_results = bleu_metric.compute(predictions=[predictions], references=[[ref] for ref in references])
            results['bleu'] = bleu_results['bleu']
        
        return results
```

## 4.5 Advanced Training Techniques

### Curriculum Learning

```python
class CurriculumLearningTrainer(RAGGeneratorTrainer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.curriculum_stage = 0
    
    def sort_by_difficulty(self, data: List[Dict]):
        """Sort examples by difficulty (context length + query complexity)."""
        def difficulty_score(example):
            context_length = sum(len(ctx.split()) for ctx in example['contexts'])
            query_length = len(example['query'].split())
            return context_length + query_length
        
        return sorted(data, key=difficulty_score)
    
    def train_with_curriculum(self, data: List[Dict], stages: int = 3):
        sorted_data = self.sort_by_difficulty(data)
        chunk_size = len(sorted_data) // stages
        
        for stage in range(stages):
            print(f"Training stage {stage + 1}/{stages}")
            
            # Gradually increase data
            end_idx = (stage + 1) * chunk_size
            stage_data = sorted_data[:end_idx]
            
            # Adjust learning rate
            self.learning_rate *= 0.8
            
            self.train(stage_data, output_dir=f'./stage_{stage + 1}')
```

### Multi-task Learning

```python
class MultiTaskRAGTrainer:
    def __init__(self, model_name: str):
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    def create_multi_task_data(self, qa_data: List[Dict], 
                              summarization_data: List[Dict],
                              entailment_data: List[Dict]):
        combined_data = []
        
        # QA task
        for item in qa_data:
            combined_data.append({
                'task': 'qa',
                'input': f"qa: {item['query']} | context: {' '.join(item['contexts'])}",
                'output': item['answer']
            })
        
        # Summarization task
        for item in summarization_data:
            combined_data.append({
                'task': 'summarize',
                'input': f"summarize: {item['text']}",
                'output': item['summary']
            })
        
        # Entailment task
        for item in entailment_data:
            combined_data.append({
                'task': 'entailment',
                'input': f"entailment: premise: {item['premise']} hypothesis: {item['hypothesis']}",
                'output': item['label']
            })
        
        return combined_data
```

## 4.6 Controlling Hallucination

### Constrained Decoding

```python
from transformers import LogitsProcessor, LogitsProcessorList

class ContextConstrainedLogitsProcessor(LogitsProcessor):
    def __init__(self, context_tokens: torch.Tensor, tokenizer, penalty_factor: float = -10.0):
        self.context_tokens = set(context_tokens.tolist())
        self.tokenizer = tokenizer
        self.penalty_factor = penalty_factor
    
    def __call__(self, input_ids: torch.Tensor, scores: torch.Tensor):
        # Penalize tokens not in context
        for batch_idx in range(scores.shape[0]):
            for token_idx in range(scores.shape[1]):
                if token_idx not in self.context_tokens:
                    scores[batch_idx, token_idx] += self.penalty_factor
        return scores

def generate_with_constraints(model, tokenizer, query: str, contexts: List[str]):
    # Tokenize context
    context_text = ' '.join(contexts)
    context_encoding = tokenizer(context_text, return_tensors='pt')
    context_tokens = context_encoding['input_ids'].squeeze()
    
    # Create processor
    processor = ContextConstrainedLogitsProcessor(context_tokens, tokenizer)
    
    # Generate
    input_text = f"Question: {query}\nContext: {context_text}"
    inputs = tokenizer(input_text, return_tensors='pt')
    
    outputs = model.generate(
        **inputs,
        max_length=256,
        logits_processor=LogitsProcessorList([processor])
    )
    
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
```

### Factual Consistency Training

```python
class FactualConsistencyLoss:
    def __init__(self, model, tokenizer, weight: float = 0.5):
        self.model = model
        self.tokenizer = tokenizer
        self.weight = weight
    
    def compute_nll_loss(self, input_ids, attention_mask, labels):
        outputs = self.model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            labels=labels
        )
        return outputs.loss
    
    def compute_consistency_loss(self, input_ids, attention_mask, 
                                generated_ids, context_ids):
        """Encourage model to attend to context."""
        # This is a simplified version
        # In practice, use more sophisticated methods
        outputs = self.model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            output_attentions=True
        )
        
        # Extract attention weights to context
        attentions = outputs.attentions[-1]  # Last layer
        context_attention = attentions[:, :, :, :context_ids.shape[1]].mean()
        
        # Higher attention to context = lower loss
        consistency_loss = -context_attention.log().mean()
        
        return consistency_loss
    
    def combined_loss(self, input_ids, attention_mask, labels, context_ids):
        nll_loss = self.compute_nll_loss(input_ids, attention_mask, labels)
        
        with torch.no_grad():
            generated_ids = self.model.generate(input_ids, max_length=labels.shape[1])
        
        consistency_loss = self.compute_consistency_loss(
            input_ids, attention_mask, generated_ids, context_ids
        )
        
        return nll_loss + self.weight * consistency_loss
```

## 4.7 Evaluation Metrics

### Comprehensive Evaluation Suite

```python
import evaluate
from nltk.translate.bleu_score import corpus_bleu
import numpy as np

class RAGEvaluationSuite:
    def __init__(self):
        self.rouge = evaluate.load('rouge')
        self.bleu = evaluate.load('bleu')
        self.bertscore = evaluate.load('bertscore')
        self.meteor = evaluate.load('meteor')
    
    def evaluate_all(self, predictions: List[str], references: List[str],
                    contexts: List[List[str]] = None):
        results = {}
        
        # ROUGE
        rouge_results = self.rouge.compute(predictions=predictions, references=references)
        results.update({f'rouge_{k}': v for k, v in rouge_results.items()})
        
        # BLEU
        bleu_results = self.bleu.compute(predictions=[predictions], 
                                        references=[[ref] for ref in references])
        results['bleu'] = bleu_results['bleu']
        
        # BERTScore
        bertscore_results = self.bertscore.compute(
            predictions=predictions, 
            references=references,
            lang='en'
        )
        results['bertscore_precision'] = np.mean(bertscore_results['precision'])
        results['bertscore_recall'] = np.mean(bertscore_results['recall'])
        results['bertscore_f1'] = np.mean(bertscore_results['f1'])
        
        # METEOR
        meteor_results = self.meteor.compute(predictions=predictions, references=references)
        results['meteor'] = meteor_results['meteor']
        
        # Faithfulness (if contexts provided)
        if contexts:
            faithfulness = self.evaluate_faithfulness(predictions, contexts)
            results['faithfulness'] = faithfulness
        
        return results
    
    def evaluate_faithfulness(self, predictions: List[str], 
                             contexts: List[List[str]]):
        """Measure how much of the prediction is supported by context."""
        from nltk import word_tokenize
        from collections import Counter
        
        faithfulness_scores = []
        
        for pred, ctx_list in zip(predictions, contexts):
            combined_context = ' '.join(ctx_list)
            
            pred_tokens = set(word_tokenize(pred.lower()))
            context_tokens = set(word_tokenize(combined_context.lower()))
            
            # Overlap ratio
            overlap = len(pred_tokens & context_tokens)
            faithfulness = overlap / len(pred_tokens) if pred_tokens else 0
            
            faithfulness_scores.append(faithfulness)
        
        return np.mean(faithfulness_scores)
```

## 4.8 Next Steps

With a trained generator, you can now:
- Combine with retrievers for end-to-end RAG
- Implement retrieval-augmented fine-tuning
- Deploy production RAG systems
- Optimize for latency and throughput

---

**Exercise 4.1**: Fine-tune BART on SQuAD dataset with retrieved contexts.

**Exercise 4.2**: Implement constrained decoding to reduce hallucination.

**Exercise 4.3**: Compare encoder-decoder vs decoder-only architectures for your use case.
