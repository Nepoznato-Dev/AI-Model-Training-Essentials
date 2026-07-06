# Cognitive Biases

## Overview

Cognitive biases are systematic patterns of deviation from norm or rationality in judgment and decision-making. In software development and AI systems, cognitive biases can lead to poor design decisions, flawed requirements gathering, incorrect debugging approaches, and biased model behavior. Understanding these biases helps teams make better decisions and build more reliable systems.

## When to Reference This Document

- Making architectural decisions
- Conducting code reviews
- Gathering requirements
- Debugging complex issues
- Designing AI/ML systems
- Planning project timelines

## Common Cognitive Biases in Development

### Confirmation Bias

**Bad Example**:
```python
# Developer believes their algorithm is O(n log n)
def analyze_complexity(code):
    # Only looks for evidence supporting O(n log n)
    sees_divide_and_conquer = True
    sees_recursion = True
    
    # Ignores contradictory evidence
    nested_loop_present = True  # Actually makes it O(n²)
    redundant_computation = True  # Adds extra factor
    
    # Conclusion: "It's definitely O(n log n)"
    return "O(n log n)"  # Wrong! It's O(n² log n)

# During debugging:
# - Dismisses test failures as "test bugs"
# - Only runs tests that pass
# - Ignores error logs that contradict hypothesis
```

**Why It's Bad**:
- Misses critical bugs
- Incorrect complexity analysis
- Wasted time on wrong solutions
- Poor code quality

**Solution**: Actively seek disconfirming evidence
```python
def analyze_complexity(code):
    # List all complexity contributors
    complexities = []
    
    # Check for nested loops
    if has_nested_loops(code):
        complexities.append("O(n²)")
    
    # Check for sorting
    if has_sorting(code):
        complexities.append("O(n log n)")
    
    # Check for recursion depth
    if has_recursion(code):
        complexities.append(calculate_recursive_complexity(code))
    
    # Take the worst case
    return max(complexities)

# During debugging:
# - Try to prove your hypothesis wrong
# - Run failing tests first
# - Assume the bug is in your code, not tests
# - Ask someone else to review your reasoning
```

### Sunk Cost Fallacy

**Bad Example**:
```
Project Manager: "We've spent 6 months on this architecture."
Developer: "But it's not working and needs complete redesign."
PM: "We can't abandon it now, we've invested too much."

Result: Continue throwing good money after bad
Final outcome: 12 months wasted instead of 6
```

**Why It's Bad**:
- Continues failing projects
- Prevents course correction
- Wastes more resources
- Opportunity cost of better alternatives

**Solution**: Make decisions based on future value
```python
def decide_whether_to_continue(project):
    # Ignore past investment
    sunk_cost = project.time_spent  # Irrelevant!
    
    # Focus on future
    future_cost = estimate_remaining_work(project)
    future_value = estimate_future_value(project)
    
    # Consider alternatives
    alternative_value = estimate_value_of_best_alternative()
    
    # Decision based on future ROI
    if future_value - future_cost < alternative_value:
        return "Pivot or cancel"
    else:
        return "Continue"

# Ask: "If we weren't already working on this, would we start it today?"
```

### Anchoring Bias

**Bad Example**:
```
Estimation meeting:
Senior Dev: "I think this will take about 2 weeks."

Everyone else anchors to 2 weeks:
- Junior dev: "Maybe 10 days?"
- PM: "Can we do 12 days?"
- Final estimate: 12 days (anchored to initial 2 weeks)

Reality: Task takes 6 weeks because:
- Initial estimate was off by 3x
- All discussion revolved around the anchor
- No one considered it might take 2 months
```

**Why It's Bad**:
- Inaccurate estimates
- Poor planning
- Missed deadlines
- Team frustration

**Solution**: Use estimation techniques that avoid anchoring
```python
def estimate_task(task):
    # Delphi method: everyone estimates independently first
    estimates = []
    for team_member in team:
        estimate = team_member.estimate_independently(task)
        estimates.append(estimate)
    
    # Discuss outliers
    min_estimate = min(estimates)
    max_estimate = max(estimates)
    
    if max_estimate > min_estimate * 3:
        # Large disagreement - discuss assumptions
        discuss_assumptions(min_estimate, max_estimate)
        # Re-estimate after discussion
        estimates = [member.reestimate(task) for member in team]
    
    # Use median or average
    return statistics.median(estimates)

# Or use planning poker with simultaneous reveal
```

### Availability Heuristic

**Bad Example**:
```python
# Recent production incident with database
last_week_incident = "Database connection pool exhausted"

# Architect over-indexes on recent event
class NewSystemDesign:
    def __init__(self):
        # Over-engineer database connection handling
        self.connection_pool_size = 1000  # Way too large
        self.connection_timeout = 300     # Too long
        
        # Under-engineer other important aspects
        self.input_validation = "minimal"      # Not recently failed
        self.error_handling = "basic"          # Not recently failed
        self.monitoring = "database_only"      # Focused on last incident
```

**Why It's Bad**:
- Misaligned priorities
- Over-correction on recent issues
- Neglect of other important areas
- Imbalanced system design

**Solution**: Base decisions on comprehensive data
```python
def design_system(requirements):
    # Analyze all historical incidents, not just recent ones
    all_incidents = get_all_incidents(timeframe="1 year")
    incident_patterns = analyze_patterns(all_incidents)
    
    # Consider industry best practices
    best_practices = get_industry_standards()
    
    # Risk-based prioritization
    risks = assess_all_risks(requirements)
    prioritized_risks = sort_by_impact_and_likelihood(risks)
    
    # Balanced design addressing top risks
    design = create_balanced_design(prioritized_risks[:10])
    
    return design
```

### Overconfidence Bias

**Bad Example**:
```python
# Developer estimating task
def estimate():
    # Best case scenario only
    coding_time = 2 days      # Assumes no bugs
    testing_time = 0 days     # "I'll test as I go"
    code_review_time = 0      # "My code doesn't need review"
    deployment_time = 0       # "Should be automatic"
    
    # Total: 2 days
    # With buffer? "I don't need a buffer, I'm confident"
    
    return "2 days"
    # Reality: 5 days (bugs found, review feedback, deployment issues)
```

**Why It's Bad**:
- Unrealistic timelines
- Insufficient testing
- Skipped code reviews
- Missed deadlines

**Solution**: Calibrate confidence with evidence
```python
def estimate_with_calibration(task):
    # Break down into subtasks
    subtasks = decompose(task)
    
    # Estimate each subtask
    estimates = [estimate_subtask(t) for t in subtasks]
    
    # Add contingency based on uncertainty
    uncertainty_factor = calculate_uncertainty(task)
    contingency = sum(estimates) * uncertainty_factor
    
    # Reference class forecasting
    similar_tasks = find_similar_past_tasks(task)
    historical_ratio = actual_vs_estimated(similar_tasks)
    
    base_estimate = sum(estimates) + contingency
    calibrated_estimate = base_estimate * historical_ratio
    
    # Express as range with confidence
    return {
        "optimistic": calibrated_estimate * 0.8,
        "likely": calibrated_estimate,
        "pessimistic": calibrated_estimate * 1.5,
        "confidence": calculate_confidence(task)
    }
```

### Status Quo Bias

**Bad Example**:
```
Team discussion about adopting new technology:

Dev A: "We should consider migrating to Kubernetes."
Dev B: "Our current VM setup works fine."
Dev C: "Migration would be disruptive."
Dev D: "We've always used VMs."

Decision: Keep using VMs despite:
- Kubernetes offering 40% cost reduction
- Better scalability
- Industry standard
- Team members want to learn it

Reason: "If it ain't broke, don't fix it"
```

**Why It's Bad**:
- Misses improvement opportunities
- Technical debt accumulation
- Falling behind industry
- Team skill stagnation

**Solution**: Evaluate changes objectively
```python
def evaluate_change(proposed_change):
    # Current state costs
    current_costs = {
        "operational": calculate_operational_costs(),
        "opportunity": calculate_opportunity_costs(),
        "risk": calculate_current_risks(),
        "team_satisfaction": measure_team_satisfaction()
    }
    
    # Proposed state costs
    proposed_costs = {
        "migration": calculate_migration_effort(),
        "operational": calculate_new_operational_costs(),
        "risk": calculate_new_risks(),
        "learning": calculate_learning_curve()
    }
    
    # Compare over time horizon
    timeframe = "3 years"
    current_total = sum_costs_over_time(current_costs, timeframe)
    proposed_total = sum_costs_over_time(proposed_costs, timeframe)
    
    # Decision based on net benefit
    if proposed_total < current_total * 0.8:  # 20% improvement threshold
        return "Adopt change"
    else:
        return "Maintain status quo"
```

## Real-World Scenarios

### Scenario 1: Security Vulnerability
Confirmation bias causes security team to dismiss vulnerability reports that don't match their threat model, leading to data breach.

### Scenario 2: Project Failure
Sunk cost fallacy keeps failing project alive for 18 months, wasting $2M that could have built successful alternative.

### Scenario 3: Production Outage
Availability heuristic causes team to over-protect against last outage cause while missing the actual vulnerability.

## Detection Patterns

Watch for these warning signs:
- "We've always done it this way"
- Dismissing contradictory evidence
- Estimates without ranges or confidence
- Continuing despite mounting failures
- Decisions based on recent events only
- Unwillingness to consider alternatives

## Prevention Strategies

1. **Devil's Advocate**: Assign someone to challenge assumptions
2. **Pre-mortem**: Imagine project failed, work backwards to find why
3. **Reference Class Forecasting**: Base estimates on similar past projects
4. **Blind Reviews**: Evaluate code/decisions without knowing author
5. **Diverse Teams**: Different perspectives reduce groupthink
6. **Document Reasoning**: Write down why decisions were made
7. **Regular Retrospectives**: Learn from past biases and mistakes

## Testing Checklist

- [ ] Have we sought disconfirming evidence?
- [ ] Are we continuing due to past investment?
- [ ] Were estimates made independently before discussion?
- [ ] Are we over-weighting recent events?
- [ ] Do estimates include confidence ranges?
- [ ] Have we considered alternatives objectively?
- [ ] Would we make the same decision starting fresh?

## Related Documents

- [[confirmation_bias]] - Detailed exploration of confirmation bias
- [[logical_fallacies]] - Related reasoning errors
- [[bad_dataset_examples]] - How biases affect training data
- [[misinformation_examples]] - Biases in information processing
