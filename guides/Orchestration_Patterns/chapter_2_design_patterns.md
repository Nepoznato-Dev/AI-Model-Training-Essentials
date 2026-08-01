# Chapter 2: Workflow Design Patterns

## 🎯 Learning Objectives

By the end of this chapter, you will:
- Understand and implement 6 essential orchestration patterns
- Know when to use each pattern
- Combine patterns for complex workflows
- Avoid common anti-patterns
- Build production-ready workflow architectures

---

## 2.1 Why Patterns Matter

### The Problem

Imagine you're building workflows for different scenarios:

1. **Customer onboarding**: Verify email → Create account → Send welcome → Assign mentor
2. **Data pipeline**: Extract → Transform → Load → Validate → Notify
3. **A/B testing**: Split users → Run variant A + B → Compare results → Deploy winner

Each seems unique, but they share common structures!

**Patterns** are reusable solutions to recurring problems. Instead of reinventing the wheel, you apply proven patterns.

### Benefits of Using Patterns

✅ **Faster development**: Don't start from scratch  
✅ **Fewer bugs**: Patterns are battle-tested  
✅ **Better communication**: "Let's use fan-out here" is clearer than explaining from scratch  
✅ **Easier maintenance**: Others recognize the structure  
✅ **Scalability**: Patterns often include scaling considerations  

---

## 2.2 The Chain Pattern (Sequential)

### What It Is

The simplest pattern: steps execute one after another in a straight line.

```
Step A → Step B → Step C → Step D
```

### When to Use

✅ Simple linear processes  
✅ Each step depends on the previous output  
✅ No parallelization opportunities  
✅ Clear start-to-finish flow  

### When NOT to Use

❌ Steps can run independently  
❌ Need fault tolerance (one failure stops everything)  
❌ Performance is critical (can't parallelize)  

### Implementation

```python
class ChainPattern:
    """
    Executes steps in strict sequence.
    
    If any step fails, the chain stops.
    """
    
    def __init__(self, engine: WorkflowEngine):
        self.engine = engine
    
    def add_step(self, name: str, action: callable, 
                 retry_count: int = 0) -> 'ChainPattern':
        """Add next step in chain"""
        
        # Get the last step name (if any)
        dependencies = []
        if self.engine.steps:
            # Find steps with no dependents yet
            all_deps = set()
            for step in self.engine.steps.values():
                all_deps.update(step.dependencies)
            
            # Last step is one that nothing depends on yet
            for step_name in self.engine.steps:
                if step_name not in all_deps:
                    dependencies = [step_name]
                    break
        
        self.engine.add_step(Step(
            name=name,
            action=action,
            dependencies=dependencies,
            retry_count=retry_count
        ))
        
        return self
    
    def build(self) -> WorkflowEngine:
        """Return the configured engine"""
        return self.engine

# Usage Example: Document Processing Pipeline
def load_document(context):
    """Load document from storage"""
    time.sleep(0.3)
    return {"content": "document text...", "size": 1024}

def extract_text(context):
    """Extract text from document"""
    doc = context.get("load_document_output", {})
    time.sleep(0.4)
    return {"text": doc.get("content", ""), "word_count": 150}

def analyze_sentiment(context):
    """Analyze sentiment of text"""
    extracted = context.get("extract_text_output", {})
    time.sleep(0.3)
    return {"sentiment": "positive", "confidence": 0.87}

def store_results(context):
    """Store analysis results"""
    analysis = context.get("analyze_sentiment_output", {})
    time.sleep(0.2)
    return {"stored": True, "id": "DOC_123"}

# Build the chain
engine = WorkflowEngine()
chain = ChainPattern(engine)
chain.add_step("load_document", load_document) \
     .add_step("extract_text", extract_text) \
     .add_step("analyze_sentiment", analyze_sentiment) \
     .add_step("store_results", store_results)

# Run
results = engine.run()
```

### Real-World Example: ETL Pipeline

```python
# Extract → Transform → Load pipeline
def extract_from_api(context):
    """Fetch data from source API"""
    import requests
    response = requests.get("https://api.example.com/data")
    return response.json()

def transform_data(context):
    """Clean and transform data"""
    raw_data = context.get("extract_from_api_output", [])
    
    transformed = []
    for item in raw_data:
        transformed.append({
            "id": item["id"],
            "value": float(item["value"]),
            "timestamp": parse_date(item["date"])
        })
    
    return transformed

def load_to_database(context):
    """Insert transformed data into database"""
    data = context.get("transform_data_output", [])
    
    # Database insert logic
    inserted_count = len(data)
    
    return {"inserted": inserted_count, "status": "success"}

# Chain them together
etl_engine = WorkflowEngine()
ChainPattern(etl_engine) \
    .add_step("extract", extract_from_api, retry_count=3) \
    .add_step("transform", transform_data) \
    .add_step("load", load_to_database)

etl_engine.run()
```

---

## 2.3 The Parallel Pattern

### What It Is

Multiple independent steps run simultaneously, then results are combined.

```
         Step A
        ↙       ↘
    Process A   Process B
        ↘       ↙
         Combine
```

### When to Use

✅ Steps are independent (no dependencies between them)  
✅ Need to reduce total execution time  
✅ Same operation on different data partitions  
✅ Calling multiple external services  

### When NOT to Use

❌ Steps have dependencies on each other  
❌ Limited resources (CPU, API rate limits)  
❌ Steps must run in specific order  

### Implementation

```python
class ParallelPattern:
    """
    Runs multiple steps concurrently, then combines results.
    """
    
    def __init__(self, engine: WorkflowEngine, branch_name: str = "parallel"):
        self.engine = engine
        self.branch_name = branch_name
        self.parallel_steps = []
        self._setup_step = None
        self._teardown_step = None
    
    def setup(self, name: str, action: callable) -> 'ParallelPattern':
        """Optional: Step to run before parallel branches"""
        self._setup_step = (name, action)
        return self
    
    def add_branch(self, name: str, action: callable) -> 'ParallelPattern':
        """Add a parallel branch"""
        self.parallel_steps.append((name, action))
        return self
    
    def teardown(self, name: str, action: callable) -> 'ParallelPattern':
        """Optional: Step to run after all branches complete"""
        self._teardown_step = (name, action)
        return self
    
    def build(self) -> WorkflowEngine:
        """Configure the workflow"""
        
        # Add setup step if provided
        if self._setup_step:
            self.engine.add_step(Step(
                name=self._setup_step[0],
                action=self._setup_step[1]
            ))
        
        # Add parallel branches
        dependencies = [self._setup_step[0]] if self._setup_step else []
        
        for name, action in self.parallel_steps:
            self.engine.add_step(Step(
                name=name,
                action=action,
                dependencies=dependencies.copy()
            ))
        
        # Add teardown step if provided
        if self._teardown_step:
            self.engine.add_step(Step(
                name=self._teardown_step[0],
                action=self._teardown_step[1],
                dependencies=[name for name, _ in self.parallel_steps]
            ))
        
        return self.engine

# Usage Example: Multi-Source Data Aggregation
def fetch_from_source_a(context):
    """Fetch data from API A"""
    time.sleep(0.5)  # Simulate network call
    return {"source": "A", "data": [1, 2, 3]}

def fetch_from_source_b(context):
    """Fetch data from API B"""
    time.sleep(0.6)  # Simulate network call
    return {"source": "B", "data": [4, 5, 6]}

def fetch_from_source_c(context):
    """Fetch data from API C"""
    time.sleep(0.4)  # Simulate network call
    return {"source": "C", "data": [7, 8, 9]}

def combine_results(context):
    """Combine all fetched data"""
    all_data = []
    
    for key in context:
        if key.endswith("_output") and "fetch_from" in key:
            result = context[key]
            all_data.extend(result.get("data", []))
    
    return {
        "combined": all_data,
        "total_items": len(all_data),
        "sources_used": 3
    }

# Build parallel workflow
engine = WorkflowEngine()
parallel = ParallelPattern(engine, branch_name="data_fetch")
parallel.setup("authenticate", lambda ctx: {"token": "abc123"}) \
          .add_branch("fetch_a", fetch_from_source_a) \
          .add_branch("fetch_b", fetch_from_source_b) \
          .add_branch("fetch_c", fetch_from_source_c) \
          .teardown("combine", combine_results)

# Run and measure time
import time
start = time.time()
results = engine.run()
elapsed = time.time() - start

print(f"\n⏱️  Total time: {elapsed:.2f}s")
print(f"   (Sequential would take: ~1.5s, Parallel took: ~0.6s)")
```

### Real-World Example: Model Ensemble

```python
# Run multiple models in parallel and ensemble their predictions

def model_v1_predict(context):
    """Run model version 1"""
    input_data = context.get("input_data")
    time.sleep(0.3)
    return {"model": "v1", "prediction": 0.75, "confidence": 0.82}

def model_v2_predict(context):
    """Run model version 2"""
    input_data = context.get("input_data")
    time.sleep(0.4)
    return {"model": "v2", "prediction": 0.78, "confidence": 0.88}

def model_v3_predict(context):
    """Run model version 3"""
    input_data = context.get("input_data")
    time.sleep(0.35)
    return {"model": "v3", "prediction": 0.72, "confidence": 0.79}

def ensemble_predictions(context):
    """Combine predictions using weighted average"""
    predictions = []
    
    for key in context:
        if key.endswith("_output") and "model_" in key:
            pred = context[key]
            weight = pred.get("confidence", 0.5)
            predictions.append({
                "value": pred["prediction"],
                "weight": weight
            })
    
    # Weighted average
    total_weight = sum(p["weight"] for p in predictions)
    ensemble_pred = sum(p["value"] * p["weight"] for p in predictions) / total_weight
    
    return {
        "final_prediction": ensemble_pred,
        "models_used": len(predictions),
        "individual_predictions": predictions
    }

# Build ensemble workflow
engine = WorkflowEngine()
ParallelPattern(engine) \
    .add_branch("model_v1", model_v1_predict) \
    .add_branch("model_v2", model_v2_predict) \
    .add_branch("model_v3", model_v3_predict) \
    .teardown("ensemble", ensemble_predictions)

engine.run(initial_context={"input_data": "sample input"})
```

---

## 2.4 The Conditional Pattern (Branching)

### What It Is

Execute different paths based on data or conditions.

```
         Check Condition
        ↙               ↘
    If True           If False
      Path A            Path B
        ↘               ↙
         Merge Results
```

### When to Use

✅ Different logic for different scenarios  
✅ Feature flags or A/B tests  
✅ Handle special cases differently  
✅ Dynamic routing based on input  

### When NOT to Use

❌ All inputs follow same path  
❌ Conditions are expensive to evaluate  
❌ Logic is too complex (consider separate workflows)  

### Implementation

First, let's extend our Step class to support conditions:

```python
@dataclass
class ConditionalStep(Step):
    """Step that only runs if condition is met"""
    condition: Callable = None  # Function returning bool
    else_action: Callable = None  # Alternative action if condition false
    
    def should_run(self, context: Dict) -> bool:
        """Check if this step should execute"""
        if self.condition is None:
            return True
        try:
            return self.condition(context)
        except Exception:
            return False

class ConditionalWorkflowEngine(WorkflowEngine):
    """Extended engine supporting conditional steps"""
    
    def _execute_conditional_step(self, step: ConditionalStep, 
                                   context: Dict) -> StepResult:
        """Execute step with condition checking"""
        
        # Check condition
        if isinstance(step, ConditionalStep) and step.condition:
            should_run = step.should_run(context)
            
            if not should_run:
                # Run else_action if provided
                if step.else_action:
                    try:
                        output = step.else_action(context)
                        return StepResult(
                            step_name=step.name,
                            status=StepStatus.SUCCESS,
                            output=output,
                            duration=0.0
                        )
                    except Exception as e:
                        return StepResult(
                            step_name=step.name,
                            status=StepStatus.FAILED,
                            error=f"Else action failed: {str(e)}"
                        )
                
                # Skip this step
                return StepResult(
                    step_name=step.name,
                    status=StepStatus.SKIPPED,
                    error="Condition not met"
                )
        
        # Normal execution
        return self._execute_step_with_retry(step, context)
    
    def _execute_step_with_retry(self, step: Step, context: Dict) -> StepResult:
        """Override to use conditional execution"""
        if isinstance(step, ConditionalStep):
            return self._execute_conditional_step(step, context)
        
        # Original implementation for regular steps
        return super()._execute_step_with_retry(step, context)

# Usage Example: Premium vs Free User Flow
def is_premium_user(context):
    """Check if user has premium subscription"""
    user = context.get("get_user_output", {})
    return user.get("tier") == "premium"

def show_premium_features(context):
    """Display premium features"""
    return {"features": ["advanced_analytics", "priority_support", "custom_branding"]}

def show_basic_features(context):
    """Display basic features (else action)"""
    return {"features": ["basic_analytics", "community_support"]}

def upgrade_prompt(context):
    """Show upgrade prompt for free users"""
    return {"message": "Upgrade to premium for more features!", "discount": "20%"}

# Build conditional workflow
engine = ConditionalWorkflowEngine()

# Get user info first
engine.add_step(Step(name="get_user", action=lambda ctx: {
    "user_id": 123,
    "name": "Alice",
    "tier": "free"  # Change to "premium" to see different path
}))

# Conditional step
engine.add_step(ConditionalStep(
    name="show_features",
    action=show_premium_features,
    condition=is_premium_user,
    else_action=show_basic_features,
    dependencies=["get_user"]
))

# Only free users see upgrade prompt
def is_free_user(context):
    user = context.get("get_user_output", {})
    return user.get("tier") != "premium"

engine.add_step(ConditionalStep(
    name="upgrade_prompt",
    action=upgrade_prompt,
    condition=is_free_user,
    dependencies=["show_features"]
))

results = engine.run()

print("\n📊 Results:")
for name, result in results.items():
    print(f"  {name}: {result.status.value}")
    if result.output:
        print(f"    → {result.output}")
```

### Real-World Example: Fraud Detection

```python
def check_transaction_amount(context):
    """High-value transactions need extra verification"""
    transaction = context.get("get_transaction_output", {})
    amount = transaction.get("amount", 0)
    return amount > 10000  # High value threshold

def standard_processing(context):
    """Normal transaction processing"""
    return {"status": "approved", "processing_time": "instant"}

def enhanced_verification(context):
    """Extra verification for high-value transactions"""
    time.sleep(0.5)
    return {
        "status": "pending_review",
        "verification_required": True,
        "steps": ["identity_check", "source_of_funds"]
    }

def notify_customer(context):
    """Send notification based on processing result"""
    result = context.get("process_transaction_output", {})
    
    if result.get("status") == "approved":
        return {"notification": "Transaction approved!"}
    else:
        return {"notification": "Transaction under review. We'll contact you."}

# Build fraud detection workflow
engine = ConditionalWorkflowEngine()

engine.add_step(Step(name="get_transaction", action=lambda ctx: {
    "id": "TXN_789",
    "amount": 15000,  # High value!
    "customer": "John Doe"
}))

engine.add_step(ConditionalStep(
    name="process_transaction",
    action=enhanced_verification,  # For high value
    condition=check_transaction_amount,
    else_action=standard_processing,  # For normal value
    dependencies=["get_transaction"]
))

engine.add_step(Step(
    name="notify",
    action=notify_customer,
    dependencies=["process_transaction"]
))

results = engine.run()
```

---

## 2.5 The Fan-Out/Fan-In Pattern

### What It Is

Split work across many parallel workers, then combine results.

```
              Split
            ↙   ↓   ↘
          Worker1 Worker2 Worker3
            ↘   ↓   ↙
             Combine
```

Similar to Parallel pattern, but specifically for **same operation on different data**.

### When to Use

✅ Process large datasets in chunks  
✅ Same computation on many items  
✅ Embarrassingly parallel workloads  
✅ Map-reduce style operations  

### When NOT to Use

❌ Each item needs different processing  
❌ Items have dependencies on each other  
❌ Overhead exceeds benefits  

### Implementation

```python
class FanOutFanInPattern:
    """
    Splits work across multiple workers, then combines results.
    """
    
    def __init__(self, engine: WorkflowEngine):
        self.engine = engine
        self._split_step = None
        self._worker_action = None
        self._worker_count = 3
        self._combine_step = None
    
    def split(self, name: str, action: callable) -> 'FanOutFanInPattern':
        """
        Define how to split the work.
        
        Action should return a list of work items.
        """
        self._split_step = (name, action)
        return self
    
    def workers(self, count: int, action: callable) -> 'FanOutFanInPattern':
        """
        Define worker action and count.
        
        Action processes one work item.
        """
        self._worker_action = action
        self._worker_count = count
        return self
    
    def combine(self, name: str, action: callable) -> 'FanOutFanInPattern':
        """Define how to combine worker results"""
        self._combine_step = (name, action)
        return self
    
    def build(self) -> WorkflowEngine:
        """Configure the workflow"""
        
        if not all([self._split_step, self._worker_action, self._combine_step]):
            raise ValueError("Must define split, workers, and combine steps")
        
        # Add split step
        self.engine.add_step(Step(
            name=self._split_step[0],
            action=self._split_step[1]
        ))
        
        # Add worker steps
        for i in range(self._worker_count):
            worker_name = f"worker_{i}"
            
            def make_worker(idx, worker_action):
                def worker(context):
                    # Get split results
                    split_result = context.get(f"{self._split_step[0]}_output", [])
                    
                    # Divide work among workers
                    chunk_size = len(split_result) // self._worker_count
                    start_idx = idx * chunk_size
                    end_idx = start_idx + chunk_size if idx < self._worker_count - 1 else len(split_result)
                    
                    work_chunk = split_result[start_idx:end_idx]
                    
                    # Process chunk
                    results = []
                    for item in work_chunk:
                        result = worker_action({"item": item})
                        results.append(result)
                    
                    return {"worker_id": idx, "results": results, "processed": len(results)}
                
                return worker
            
            self.engine.add_step(Step(
                name=worker_name,
                action=make_worker(i, self._worker_action),
                dependencies=[self._split_step[0]]
            ))
        
        # Add combine step
        self.engine.add_step(Step(
            name=self._combine_step[0],
            action=self._combine_step[1],
            dependencies=[f"worker_{i}" for i in range(self._worker_count)]
        ))
        
        return self.engine

# Usage Example: Batch Image Processing
def split_images(context):
    """Get list of images to process"""
    # In reality, this might query a database
    return [f"image_{i}.jpg" for i in range(100)]

def process_image(context):
    """Process a single image"""
    item = context.get("item")
    time.sleep(0.01)  # Simulate processing
    
    return {
        "image": item,
        "thumbnail": f"thumb_{item}",
        "metadata": {"size": 1024, "format": "jpg"}
    }

def combine_results(context):
    """Combine all worker results"""
    all_results = []
    total_processed = 0
    
    for key in context:
        if key.startswith("worker_") and key.endswith("_output"):
            worker_result = context[key]
            all_results.extend(worker_result.get("results", []))
            total_processed += worker_result.get("processed", 0)
    
    return {
        "total_images": total_processed,
        "thumbnails_created": len(all_results),
        "sample_results": all_results[:5]  # First 5 for preview
    }

# Build fan-out/fan-in workflow
engine = WorkflowEngine()
fanout = FanOutFanInPattern(engine)
fanout.split("get_images", split_images) \
        .workers(count=4, action=process_image) \
        .combine("finalize", combine_results)

start = time.time()
results = engine.run()
elapsed = time.time() - start

print(f"\n⏱️  Processed {results['finalize'].output['total_images']} images in {elapsed:.2f}s")
```

### Real-World Example: Distributed Model Training

```python
def split_training_data(context):
    """Split dataset into chunks for distributed training"""
    # Simulate dataset with 10000 samples
    dataset_size = 10000
    return list(range(dataset_size))

def train_on_chunk(context):
    """Train model on data chunk"""
    item = context.get("item")  # This is actually a range of indices
    
    # Simulate training
    time.sleep(0.1)
    
    # Return mock metrics
    return {
        "chunk": item,
        "loss": 0.1 + random.random() * 0.05,
        "accuracy": 0.85 + random.random() * 0.05,
        "samples_processed": 2500
    }

def aggregate_metrics(context):
    """Aggregate metrics from all workers"""
    all_metrics = []
    
    for key in context:
        if key.startswith("worker_") and key.endswith("_output"):
            all_metrics.append(context[key])
    
    avg_loss = sum(m["loss"] for m in all_metrics) / len(all_metrics)
    avg_accuracy = sum(m["accuracy"] for m in all_metrics) / len(all_metrics)
    total_samples = sum(m["samples_processed"] for m in all_metrics)
    
    return {
        "final_loss": avg_loss,
        "final_accuracy": avg_accuracy,
        "total_samples": total_samples,
        "workers_completed": len(all_metrics)
    }

# Build distributed training workflow
engine = WorkflowEngine()
FanOutFanInPattern(engine) \
    .split("prepare_data", split_training_data) \
    .workers(count=4, action=train_on_chunk) \
    .combine("aggregate", aggregate_metrics)

results = engine.run()
final = results["aggregate"].output

print(f"\n📊 Training Complete!")
print(f"   Final Loss: {final['final_loss']:.4f}")
print(f"   Final Accuracy: {final['final_accuracy']:.4f}")
print(f"   Samples Processed: {final['total_samples']}")
```

---

## 2.6 The Loop Pattern

### What It Is

Repeat steps until a condition is met.

```
    Start
      ↓
    [Condition?] ─No─→ Do Work ──┐
      ↓                          │
     Yes                         │
      ↓                          │
    Continue                     └──
```

### When to Use

✅ Retry until success  
✅ Process until queue is empty  
✅ Iterative refinement  
✅ Polling for completion  

### When NOT to Use

❌ Fixed number of iterations (use simple sequence)  
❌ Risk of infinite loops  
❌ Better alternatives exist (webhooks instead of polling)  

### Implementation

```python
class LoopPattern:
    """
    Repeats steps until condition is met.
    """
    
    def __init__(self, engine: WorkflowEngine):
        self.engine = engine
        self._condition_step = None
        self._body_steps = []
        self._max_iterations = 10
    
    def condition(self, name: str, action: callable) -> 'LoopPattern':
        """
        Define loop condition.
        
        Action should return True to continue, False to stop.
        """
        self._condition_step = (name, action)
        return self
    
    def body(self, name: str, action: callable) -> 'LoopPattern':
        """Add a step to the loop body"""
        self._body_steps.append((name, action))
        return self
    
    def max_iterations(self, count: int) -> 'LoopPattern':
        """Set maximum iterations (safety limit)"""
        self._max_iterations = count
        return self
    
    def build(self) -> WorkflowEngine:
        """Configure the workflow"""
        
        if not self._condition_step:
            raise ValueError("Must define condition step")
        
        if not self._body_steps:
            raise ValueError("Must define at least one body step")
        
        # Create a custom workflow that handles looping
        iteration = 0
        
        def loop_orchestrator(context):
            nonlocal iteration
            
            while iteration < self._max_iterations:
                iteration += 1
                
                # Check condition
                cond_name, cond_action = self._condition_step
                should_continue = cond_action(context)
                
                if not should_continue:
                    return {
                        "status": "complete",
                        "iterations": iteration,
                        "reason": "condition_met"
                    }
                
                # Execute body steps
                for step_name, step_action in self._body_steps:
                    result = step_action(context)
                    context[f"{step_name}_iter_{iteration}"] = result
                
                context["loop_iteration"] = iteration
            
            return {
                "status": "stopped",
                "iterations": iteration,
                "reason": "max_iterations_reached"
            }
        
        # Add as a single step that handles the loop internally
        self.engine.add_step(Step(
            name="loop_executor",
            action=loop_orchestrator
        ))
        
        return self.engine

# Usage Example: Retry Until Success
def check_service_health(context):
    """Check if service is healthy"""
    attempt = context.get("loop_iteration", 0)
    
    # Simulate service becoming healthy after 3 attempts
    is_healthy = attempt >= 3
    
    print(f"  Health check #{attempt}: {'✅ Healthy' if is_healthy else '❌ Unhealthy'}")
    
    return not is_healthy  # Continue loop while unhealthy

def wait_and_retry(context):
    """Wait before retrying"""
    time.sleep(0.5)
    return {"waited": True}

# Build retry loop
engine = WorkflowEngine()
LoopPattern(engine) \
    .condition("health_check", check_service_health) \
    .body("wait", wait_and_retry) \
    .max_iterations(10)

results = engine.run()
loop_result = results["loop_executor"].output

print(f"\n🔄 Loop completed after {loop_result['iterations']} iterations")
print(f"   Reason: {loop_result['reason']}")
```

### Real-World Example: Data Pipeline with Backoff

```python
def has_more_records(context):
    """Check if there are more records to process"""
    processed = context.get("total_processed", 0)
    target = context.get("target_records", 100)
    
    has_more = processed < target
    print(f"  Processed {processed}/{target} records")
    
    return has_more

def fetch_batch(context):
    """Fetch next batch of records"""
    current = context.get("total_processed", 0)
    batch_size = 10
    
    # Simulate fetching
    time.sleep(0.1)
    
    new_count = current + batch_size
    context["total_processed"] = new_count
    
    return {
        "batch_start": current,
        "batch_end": new_count,
        "records_fetched": batch_size
    }

def process_batch(context):
    """Process the fetched batch"""
    batch = context.get("fetch_batch_output", {})
    
    # Simulate processing
    time.sleep(0.05)
    
    return {
        "processed": batch.get("records_fetched", 0),
        "errors": 0
    }

# Build pagination loop
engine = WorkflowEngine()
engine.add_step(Step(name="init", action=lambda ctx: {
    "total_processed": 0,
    "target_records": 50
}))

LoopPattern(engine) \
    .condition("check_remaining", has_more_records) \
    .body("fetch", fetch_batch) \
    .body("process", process_batch) \
    .max_iterations(20)

results = engine.run()
```

---

## 2.7 The Circuit Breaker Pattern

### What It Is

Stop trying when a service is consistently failing, to prevent cascading failures.

```
    [Closed] ──failures──→ [Open]
       ↑                      │
       │                      ↓
       └────timeout────[Half-Open]
```

**States:**
- **Closed**: Normal operation, requests go through
- **Open**: Service is failing, reject requests immediately
- **Half-Open**: Testing if service recovered

### When to Use

✅ Calling unreliable external services  
✅ Prevent cascade failures  
✅ Give failing services time to recover  
✅ Protect your system from overload  

### When NOT to Use

❌ Highly reliable internal services  
❌ Every request is critical (no fallback)  
❌ Service never recovers without intervention  

### Implementation

```python
from enum import Enum
from datetime import datetime, timedelta

class CircuitState(Enum):
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Failing, reject requests
    HALF_OPEN = "half_open"  # Testing recovery

class CircuitBreaker:
    """
    Circuit breaker for protecting against cascading failures.
    """
    
    def __init__(self, failure_threshold: int = 3, 
                 recovery_timeout: float = 30.0,
                 half_open_max_calls: int = 1):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.half_open_max_calls = half_open_max_calls
        
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.last_failure_time = None
        self.half_open_calls = 0
    
    def call(self, func: callable, *args, **kwargs):
        """Execute function with circuit breaker protection"""
        
        if self.state == CircuitState.OPEN:
            # Check if we should try half-open
            if self._should_attempt_reset():
                self.state = CircuitState.HALF_OPEN
                self.half_open_calls = 0
                print("  🔶 Circuit: HALF-OPEN (testing recovery)")
            else:
                raise Exception("Circuit breaker is OPEN - service unavailable")
        
        if self.state == CircuitState.HALF_OPEN:
            if self.half_open_calls >= self.half_open_max_calls:
                raise Exception("Circuit breaker half-open limit reached")
            self.half_open_calls += 1
        
        # Execute the function
        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise
    
    def _on_success(self):
        """Handle successful call"""
        self.failure_count = 0
        if self.state == CircuitState.HALF_OPEN:
            self.state = CircuitState.CLOSED
            print("  🟢 Circuit: CLOSED (recovered)")
    
    def _on_failure(self):
        """Handle failed call"""
        self.failure_count += 1
        self.last_failure_time = datetime.now()
        
        if self.state == CircuitState.HALF_OPEN:
            self.state = CircuitState.OPEN
            print("  🔴 Circuit: OPEN (recovery failed)")
        elif self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN
            print(f"  🔴 Circuit: OPEN (threshold reached: {self.failure_count})")
    
    def _should_attempt_reset(self) -> bool:
        """Check if enough time has passed to try recovery"""
        if self.last_failure_time is None:
            return True
        
        elapsed = (datetime.now() - self.last_failure_time).total_seconds()
        return elapsed >= self.recovery_timeout

# Wrapper for workflow steps
class CircuitProtectedStep(Step):
    """Step wrapped with circuit breaker"""
    
    def __init__(self, circuit_breaker: CircuitBreaker, **kwargs):
        super().__init__(**kwargs)
        self.circuit_breaker = circuit_breaker
        self.original_action = kwargs.get('action')
        
        def protected_action(context):
            return self.circuit_breaker.call(self.original_action, context)
        
        self.action = protected_action

# Usage Example: Protecting External API Calls
flaky_api_breaker = CircuitBreaker(
    failure_threshold=3,
    recovery_timeout=10.0  # Try again after 10 seconds
)

def call_flaky_api(context):
    """Simulate unreliable API"""
    # Simulate random failures
    import random
    if random.random() < 0.7:  # 70% failure rate
        raise ConnectionError("API timeout")
    
    return {"data": "success", "timestamp": time.time()}

# Build workflow with circuit breaker
engine = WorkflowEngine()

# Add circuit-protected step
engine.add_step(CircuitProtectedStep(
    circuit_breaker=flaky_api_breaker,
    name="call_api",
    action=call_flaky_api,
    retry_count=1
))

# Fallback step if circuit is open
def fallback_action(context):
    """Use cached data when API is unavailable"""
    print("  💾 Using cached data as fallback")
    return {"data": "cached", "source": "fallback"}

engine.add_step(ConditionalStep(
    name="fallback_if_needed",
    action=fallback_action,
    condition=lambda ctx: False,  # Never run normally
    else_action=fallback_action,  # Always run as fallback
    dependencies=["call_api"]
))

# Run multiple times to see circuit breaker in action
print("🔄 Running API calls...\n")
for i in range(5):
    print(f"\n--- Call {i+1} ---")
    try:
        fresh_engine = WorkflowEngine()
        fresh_engine.add_step(CircuitProtectedStep(
            circuit_breaker=flaky_api_breaker,
            name="call_api",
            action=call_flaky_api
        ))
        fresh_engine.run()
    except Exception as e:
        print(f"  ⚠️  Request rejected: {e}")
```

---

## 2.8 Combining Patterns

Real-world workflows often combine multiple patterns.

### Example: E-commerce Order Processing

```python
# Complex workflow combining multiple patterns

def validate_order(context):
    """Validate order details"""
    order = context.get("order")
    return {"valid": True, "order_id": order["id"]}

def check_inventory_parallel(context):
    """Check inventory for all items in parallel"""
    order = context.get("order")
    items = order.get("items", [])
    
    results = {}
    for item in items:
        # Simulate inventory check
        results[item["id"]] = {"available": True, "quantity": 10}
    
    return results

def process_payment(context):
    """Process payment"""
    # Could fail, needs circuit breaker
    time.sleep(0.3)
    return {"payment_id": "PAY_123", "status": "approved"}

def schedule_shipping(context):
    """Schedule shipment"""
    return {"tracking": "TRK_789", "carrier": "FedEx"}

def send_confirmation(context):
    """Send confirmation email"""
    return {"email_sent": True}

def handle_failure(context):
    """Handle order processing failure"""
    return {"status": "failed", "refund_initiated": True}

# Build complex workflow
engine = ConditionalWorkflowEngine()

# Step 1: Validate (Chain start)
engine.add_step(Step(name="validate", action=validate_order))

# Step 2-4: Check inventory, payment, shipping (Parallel after validation)
ParallelPattern(engine) \
    .setup("prep", lambda ctx: ctx) \
    .add_branch("inventory", check_inventory_parallel) \
    .add_branch("payment", process_payment) \
    .add_branch("shipping", schedule_shipping) \
    .teardown("confirm", send_confirmation)

# Conditional: Send different notifications based on outcome
def is_successful(context):
    confirm = context.get("confirm_output", {})
    return confirm.get("email_sent", False)

engine.add_step(ConditionalStep(
    name="success_notification",
    action=lambda ctx: {"notification": "Order confirmed!"},
    condition=is_successful,
    else_action=handle_failure,
    dependencies=["confirm"]
))

print("📦 E-commerce Order Processing Workflow")
print("=" * 50)

results = engine.run(initial_context={
    "order": {
        "id": "ORD_456",
        "items": [
            {"id": "ITEM_1", "qty": 2},
            {"id": "ITEM_2", "qty": 1}
        ],
        "total": 99.99
    }
})

print("\n📊 Final Results:")
for name, result in results.items():
    icon = "✅" if result.status == StepStatus.SUCCESS else "⚠️"
    print(f"  {icon} {name}: {result.status.value}")
```

---

## 📚 Glossary

| Term | Definition |
|------|------------|
| **Chain Pattern** | Sequential execution: A → B → C |
| **Parallel Pattern** | Concurrent execution of independent steps |
| **Conditional Pattern** | Branch execution based on conditions |
| **Fan-Out/Fan-In** | Split work, process in parallel, combine results |
| **Loop Pattern** | Repeat steps until condition is met |
| **Circuit Breaker** | Stop calling failing services to prevent cascade |
| **Map-Reduce** | Functional programming pattern similar to fan-out/fan-in |
| **Idempotent** | Operation that can be applied multiple times safely |
| **Backoff** | Increasing wait time between retries |
| **Fallback** | Alternative action when primary fails |

---

## 🎓 Exercises

### Exercise 1: Build a News Aggregator

Create a workflow that:
1. Fetches news from 3 different APIs (parallel)
2. Filters articles by topic (conditional)
3. Ranks articles by relevance
4. Combines top 10 articles
5. Sends digest email

**Bonus:** Add circuit breakers for each API.

### Exercise 2: Implement Smart Retry with Backoff

Extend the circuit breaker to implement exponential backoff:
- First retry: wait 1 second
- Second retry: wait 2 seconds
- Third retry: wait 4 seconds
- etc.

### Exercise 3: Create a Workflow Template Library

Build reusable templates for common patterns:
```python
templates = WorkflowTemplates()

# Pre-built templates
etl_workflow = templates.etl_pipeline(
    source=my_api,
    transform=my_transform,
    destination=my_db
)

retry_workflow = templates.retry_with_backoff(
    action=risky_call,
    max_retries=5
)
```

---

## 🔍 Self-Assessment Checklist

Before moving to Chapter 3, ensure you can:

- [ ] Explain when to use each of the 6 patterns
- [ ] Implement Chain, Parallel, and Conditional patterns
- [ ] Build Fan-Out/Fan-In for batch processing
- [ ] Create loops with proper termination conditions
- [ ] Implement circuit breaker to protect services
- [ ] Combine multiple patterns in one workflow
- [ ] Identify anti-patterns and avoid them
- [ ] Choose the right pattern for a given scenario

---

## 🚀 What's Next?

Chapter 3 covers **Advanced Orchestration**:
- Scaling to thousands of concurrent workflows
- Distributed orchestration across multiple machines
- Monitoring and observability
- Fault tolerance and recovery
- State persistence
- Rate limiting and throttling

You'll learn how to take these patterns to production scale!
