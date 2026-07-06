# Bad Variable Names

Poor variable naming makes code harder to read, understand, and maintain. Good names serve as documentation and reduce cognitive load for developers.

---

## Why Variable Names Matter

Variable names are the primary way developers communicate intent in code. Good names:
- Explain what the data represents
- Indicate valid values and constraints
- Document usage without comments
- Reduce debugging time
- Make refactoring safer

---

## Common Naming Anti-Patterns

### Single Letter Names (Except Loop Counters)

**Bad Example:**
```python
def p(d, r, t):
    a = d * ((1 + r / 12) ** (12 * t))
    i = a - d
    return i
```

**Problems:**
- No indication of what parameters represent
- Requires reading implementation to understand
- Easy to mix up similar variables

**Better:**
```python
def calculate_compound_interest(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    months = 12 * years
    amount = principal * ((1 + monthly_rate) ** months)
    interest_earned = amount - principal
    return interest_earned
```

---

### Vague or Generic Names

**Bad Example:**
```python
data = get_data()
result = process(data)
temp = transform(result)
final = finalize(temp)
```

**Problems:**
- `data`, `result`, `temp`, `final` could mean anything
- No indication of what type of data
- Hard to track transformations

**Better:**
```python
user_records = fetch_user_records()
validated_users = validate_user_data(user_records)
enriched_users = add_subscription_info(validated_users)
user_profiles = format_for_display(enriched_users)
```

---

### Misleading Names

**Bad Example:**
```python
# Returns list, but name suggests single item
user = get_all_active_users()

# Actually modifies the list in place
new_list = sort_and_filter_users(user)

# Is this timestamp in seconds, milliseconds, or ISO string?
created_time = obj.created_time
```

**Problems:**
- Creates wrong mental model
- Leads to bugs when assumptions are violated
- Wastes time debugging incorrect assumptions

**Better:**
```python
active_users = get_all_active_users()
sort_and_filter_in_place(active_users)
created_timestamp_ms = obj.created_timestamp_ms
```

---

### Type in Name (Hungarian Notation)

**Bad Example:**
```python
str_name = "John"
i_count = 5
lst_items = [1, 2, 3]
dict_config = {"key": "value"}
```

**Problems:**
- Redundant with type hints
- Becomes wrong after refactoring
- Clutters names with implementation details

**Better:**
```python
name: str = "John"
count: int = 5
items: List[int] = [1, 2, 3]
config: Dict[str, str] = {"key": "value"}
```

---

### Abbreviations and Acronyms

**Bad Example:**
```python
usr_mgr = UserManager()
cfg = load_cfg()
req = create_req(params)
resp = send_req(req)
dt = get_curr_dt()
```

**Problems:**
- Unclear to new team members
- Multiple meanings possible (`dt` = datetime? data? delta?)
- Inconsistent abbreviations across codebase

**Better:**
```python
user_manager = UserManager()
config = load_config()
request = create_request(params)
response = send_request(request)
current_datetime = get_current_datetime()
```

**Acceptable Abbreviations:**
- Well-known: `id`, `url`, `http`, `api`
- Team-standard: Define in style guide
- Context-clear: `max`, `min` in numeric contexts

---

### Magic Numbers as Names

**Bad Example:**
```python
timeout_30 = 30
max_100 = 100
flag_1 = 1
flag_2 = 2
```

**Problems:**
- Number in name becomes stale if value changes
- Doesn't explain purpose
- Still a magic number in disguise

**Better:**
```python
SESSION_TIMEOUT_SECONDS = 30
MAX_ITEMS_PER_PAGE = 100
STATUS_ACTIVE = 1
STATUS_INACTIVE = 2
```

---

### Boolean Names Without Clarity

**Bad Example:**
```python
flag = True
status = False
ok = check_something()
```

**Problems:**
- Unclear what the boolean represents
- Hard to read in conditions
- May need to check definition to understand

**Better:**
```python
is_authenticated = True
has_pending_changes = False
is_valid = check_validation()

# Clear in context
if is_authenticated and has_pending_changes:
    ...
```

---

### Off-by-One Confusion

**Bad Example:**
```python
# Is this inclusive or exclusive?
for i in range(0, count):
    process(items[i])

# What does 'last' mean here?
last_index = len(items) - 1
last_item = items[last_index]
```

**Better:**
```python
# Clear iteration
for index in range(len(items)):
    process(items[index])

# Or Pythonic
for item in items:
    process(item)

# Explicit about boundaries
final_index = len(items) - 1  # Last valid index
last_item = items[-1]  # Python's negative indexing
```

---

### Collection Names Without Plurals

**Bad Example:**
```python
user = get_all_users()  # Actually a list
order = orders  # Swapped names
for user in user:  # Confusing
    ...
```

**Better:**
```python
users = get_all_users()
orders_list = orders  # If 'orders' is ambiguous
for user in users:
    ...
```

---

### Context-Loss in Scope

**Bad Example:**
```python
def process_user_data(user_data):
    data = user_data  # Redundant
    info = data  # Even more vague
    result = analyze(info)
    output = format_result(result)
    return output
```

**Better:**
```python
def process_user_data(user_data):
    validated_data = validate(user_data)
    analysis_results = analyze(validated_data)
    formatted_report = format_analysis(analysis_results)
    return formatted_report
```

---

## Naming Guidelines by Context

### Functions/Methods

Use verb phrases that describe action:
```python
# Good
get_user_by_id()
calculate_total_price()
validate_input()
is_eligible_for_discount()
has_required_permissions()

# Bad
user()
total()
check()
ok()
verify()
```

### Classes

Use nouns that describe responsibility:
```python
# Good
UserRepository
PaymentProcessor
ConfigurationManager
HttpRequestBuilder

# Bad
UserDataStuff
PaymentThingy
Manager
Helper
```

### Constants

Use UPPER_SNAKE_CASE with descriptive names:
```python
# Good
MAX_RETRY_ATTEMPTS = 3
DEFAULT_PAGE_SIZE = 50
API_VERSION = "v2"

# Bad
MAX = 3
SIZE = 50
VERSION = "v2"
```

### Loop Variables

Single letters acceptable for simple loops:
```python
# Acceptable
for i in range(10):
    for j in range(10):
        ...

# Better for complex iterations
for user_index, user in enumerate(users):
    for order in user.orders:
        ...
```

---

## Naming Checklist

```markdown
## Variable Naming Quality Checklist

- [ ] Name describes what the data IS, not how it's used
- [ ] Name indicates units where relevant (seconds, meters, bytes)
- [ ] Boolean names answer yes/no questions (is_, has_, can_)
- [ ] Collections use plural names (users, not user)
- [ ] No misleading implications about type or content
- [ ] Abbreviations are team-standard or well-known
- [ ] Names remain accurate after refactoring
- [ ] Search-friendly (not easily confused with other terms)
- [ ] Pronounceable (can discuss in code review)
- [ ] Length proportional to scope (longer for wider scope)
```

---

## Refactoring Bad Names

### Before:
```python
def d(f, t):
    r = []
    for i in f:
        if i['a'] > 18:
            r.append(i)
    return r
```

### After:
```python
def filter_adults(users):
    """Return only users who are 18 or older."""
    adults = []
    for user in users:
        if user['age'] >= 18:
            adults.append(user)
    return adults
```

Or even better:
```python
def filter_adults(users: List[User]) -> List[User]:
    """Return only users who are 18 or older."""
    return [user for user in users if user.age >= 18]
```

---

## Related Documents

- [[poor_documentation]] - Documentation mistakes
- [[bad_api_design]] - API design anti-patterns
- [[unsafe_code]] - Code quality issues
- [[09_bad_examples_and_failures]] - General anti-patterns
