# Poor Documentation

Poor documentation is a critical failure that increases maintenance costs, slows onboarding, and creates knowledge silos. Good documentation is essential for code maintainability and team collaboration.

---

## Why Documentation Matters

Documentation serves multiple purposes:
- **Onboarding**: Helps new team members understand the codebase
- **Maintenance**: Enables future developers (including yourself) to understand decisions
- **API Contracts**: Defines how components interact
- **Troubleshooting**: Provides guidance for debugging issues
- **Knowledge Transfer**: Prevents bus factor risks

---

## Types of Poor Documentation

### Missing Documentation

**Bad Example:**
```python
def calc(a, b, c):
    x = a * 2 + b
    y = x / c if c != 0 else 1
    return y * 1.15
```

**Problems:**
- No docstring explaining purpose
- Unclear parameter names
- Magic numbers without explanation
- Unknown return value meaning

**Better:**
```python
def calculate_final_price_with_tax(base_price: float, 
                                    discount_percent: float, 
                                    tax_rate: float) -> float:
    """
    Calculate the final price after applying discount and tax.
    
    Args:
        base_price: Original price before any adjustments
        discount_percent: Discount as percentage (0-100)
        tax_rate: Tax rate as decimal (e.g., 0.08 for 8%)
    
    Returns:
        Final price including tax, rounded to 2 decimal places
    
    Raises:
        ValueError: If discount_percent is outside 0-100 range
    """
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
    
    discounted_price = base_price * (1 - discount_percent / 100)
    final_price = discounted_price * (1 + tax_rate)
    
    return round(final_price, 2)
```

---

### Outdated Documentation

**Bad Example:**
```markdown
# API Documentation

## Get User Endpoint

**URL:** `/api/v1/users/{id}`
**Method:** GET
**Response Format:** XML

Example:
<user>
  <id>123</id>
  <name>John</name>
</user>
```

**Reality:** The API was migrated to JSON six months ago, but documentation wasn't updated.

**Problems:**
- Wastes developer time
- Causes integration failures
- Erodes trust in documentation

---

### Overly Verbose Documentation

**Bad Example:**
```python
def add(a, b):
    """
    This function adds two numbers together.
    
    Addition is one of the four basic operations of arithmetic.
    When we add two numbers, we get a sum.
    
    Parameters:
        a: The first number to add. This should be a numeric type.
        b: The second number to add. This should also be a numeric type.
    
    Returns:
        The result of adding a and b together.
    
    Example:
        >>> add(2, 3)
        5
        
    Note:
        This function works with integers, floats, and other numeric types.
        It does not work with strings or other non-numeric types.
    """
    return a + b
```

**Problems:**
- States the obvious
- Wastes reader's time
- Makes finding useful information harder

**Better:**
```python
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers."""
    return a + b
```

---

### Inconsistent Documentation

**Bad Example:**
```python
# File 1: Uses Google style
def process_data(data):
    """
    Args:
        data: The input data
    
    Returns:
        Processed result
    """

# File 2: Uses NumPy style  
def transform_data(data):
    """
    Parameters
    ----------
    data : array-like
        Input data
    
    Returns
    -------
    result : array-like
    """

# File 3: No style at all
def clean_data(data):
    """cleans the data"""
```

**Problems:**
- Confusing for readers
- Harder to maintain
- Looks unprofessional

---

### README Anti-Patterns

**Bad Example:**
```markdown
# Project

## Installation
run the script

## Usage
just use it

## Contributing
contact me
```

**Problems:**
- No actual instructions
- Assumes prior knowledge
- Unwelcoming to contributors

**Better:**
```markdown
# Project Name

Brief description of what this project does.

## Prerequisites
- Python 3.9+
- PostgreSQL 14+

## Installation

```bash
git clone https://github.com/username/project.git
cd project
pip install -r requirements.txt
```

## Usage

```python
from project import main
result = main.run(config_path="config.yaml")
```

## Configuration

Copy `config.example.yaml` to `config.yaml` and adjust settings.

## Testing

```bash
pytest tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
```

---

## Documentation Best Practices

### Code Comments

**Do:**
```python
# Using binary search for O(log n) performance
# See: https://en.wikipedia.org/wiki/Binary_search_algorithm
index = binary_search(sorted_array, target)
```

**Don't:**
```python
# Loop through array
for i in array:
    # Check if equal to target
    if i == target:
        # Return index
        return i
```

---

### API Documentation

Include:
- Purpose and behavior
- Parameter types and constraints
- Return values and types
- Exceptions that may be raised
- Example usage
- Performance characteristics (if relevant)

```python
def search_users(query: str, 
                 limit: int = 10,
                 include_inactive: bool = False) -> List[User]:
    """
    Search for users by name or email.
    
    Performs case-insensitive partial match on name and email fields.
    Results are ordered by relevance score.
    
    Args:
        query: Search term (minimum 3 characters)
        limit: Maximum results to return (1-100, default 10)
        include_inactive: Whether to include deactivated accounts
    
    Returns:
        List of matching User objects, sorted by relevance
    
    Raises:
        ValueError: If query is less than 3 characters
        ValidationError: If limit is outside valid range
    
    Time Complexity: O(n log n) where n is number of users
    
    Example:
        >>> users = search_users("john", limit=5)
        >>> len(users)
        3
    """
```

---

### Architecture Documentation

Document:
- System overview and components
- Data flow diagrams
- Decision records (why choices were made)
- Dependencies and their versions
- Deployment architecture

```markdown
## Architecture Decision Record: Database Choice

**Date:** 2024-01-15
**Status:** Accepted

### Context
We need a database for user session storage with high write throughput.

### Options Considered
1. PostgreSQL - Reliable, ACID compliant
2. Redis - Fast, in-memory
3. MongoDB - Flexible schema

### Decision
Use Redis for session storage with PostgreSQL persistence.

### Rationale
- Redis provides sub-millisecond read/write for active sessions
- PostgreSQL backup ensures durability
- Combination handles our peak load of 10k requests/second

### Consequences
- Added operational complexity (two databases)
- Need to handle cache invalidation
- Session data limited to Redis memory capacity
```

---

## Documentation Checklist

```markdown
## Documentation Quality Checklist

### README
- [ ] Project description and purpose
- [ ] Installation instructions
- [ ] Usage examples
- [ ] Configuration guide
- [ ] Contribution guidelines
- [ ] License information

### Code
- [ ] Public functions have docstrings
- [ ] Complex logic has explanatory comments
- [ ] Parameter types and return types documented
- [ ] Examples provided for non-obvious usage

### API
- [ ] Endpoint documentation complete
- [ ] Request/response schemas defined
- [ ] Error codes documented
- [ ] Authentication requirements specified
- [ ] Rate limits documented

### Architecture
- [ ] System diagram available
- [ ] Component responsibilities defined
- [ ] Data flow documented
- [ ] Key decisions recorded
- [ ] Dependencies listed
```

---

## Related Documents

- [[bad_variable_names]] - Poor naming conventions
- [[bad_api_design]] - API design mistakes
- [[unsafe_code]] - Security vulnerabilities in code
- [[09_bad_examples_and_failures]] - General anti-patterns
