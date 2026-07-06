# Code Smells

## Overview

Code smells are surface-level indications that usually correspond to a deeper problem in the software. They are not bugs per se, but rather characteristics that suggest the code may be difficult to maintain, extend, or understand. Recognizing code smells early helps prevent technical debt accumulation.

## When to Reference This Document

- Conducting code reviews
- Refactoring existing codebases
- Training developers on code quality
- Identifying areas for improvement
- Planning technical debt reduction

## Common Code Smells

### Duplicated Code

**Bad Example**:
```python
# File: user_service.py
def send_welcome_email(user):
    message = f"Welcome {user.name}!"
    smtp = SMTPServer("smtp.example.com")
    smtp.connect()
    smtp.send(user.email, message)
    smtp.disconnect()
    log_email_sent(user.id)

# File: order_service.py  
def send_order_confirmation(order):
    message = f"Order confirmed {order.customer.name}!"
    smtp = SMTPServer("smtp.example.com")
    smtp.connect()
    smtp.send(order.customer.email, message)
    smtp.disconnect()
    log_email_sent(order.customer.id)
```

**Why It's Bad**:
- Changes must be made in multiple places
- Increased risk of inconsistencies
- Harder to test
- Violates DRY (Don't Repeat Yourself) principle

**Solution**: Extract common logic
```python
class EmailService:
    def __init__(self):
        self.smtp = SMTPServer("smtp.example.com")
    
    def send_email(self, recipient, message, user_id):
        self.smtp.connect()
        self.smtp.send(recipient, message)
        self.smtp.disconnect()
        log_email_sent(user_id)

# Usage in both services
email_service.send_email(user.email, message, user.id)
```

### Long Method

**Bad Example**:
```python
def process_data(data):
    # 10 lines of validation
    # 20 lines of transformation
    # 15 lines of business logic
    # 10 lines of formatting
    # 5 lines of logging
    # Total: 60+ lines doing too much
    pass
```

**Why It's Bad**:
- Hard to understand at a glance
- Difficult to test comprehensively
- Multiple reasons to change
- Hidden dependencies

**Solution**: Break into smaller methods
```python
def process_data(data):
    validated = validate_data(data)
    transformed = transform_data(validated)
    result = apply_business_logic(transformed)
    formatted = format_output(result)
    log_processing(data, formatted)
    return formatted
```

### Large Class

**Bad Example**:
```java
public class UserService {
    // 50 fields
    // 30 methods for user management
    // 20 methods for authentication
    // 15 methods for reporting
    // 10 methods for email notifications
    // Total: 700+ lines
}
```

**Why It's Bad**:
- God object anti-pattern
- Too many responsibilities
- Difficult to instantiate and test
- Becomes a bottleneck

**Solution**: Split by responsibility
```java
UserRepository      // Data access
UserValidator       // Validation logic
AuthenticationService // Auth operations
UserReporter        // Reporting features
EmailNotificationService // Notifications
```

### Primitive Obsession

**Bad Example**:
```python
def calculate_area(width, height, unit):
    # unit is just a string like "cm", "in", "ft"
    if unit == "cm":
        return width * height
    elif unit == "in":
        return width * height * 6.4516
    # ... more conversions
```

**Why It's Bad**:
- Type safety lost
- Validation scattered
- Business logic hidden in primitives
- Easy to pass wrong values

**Solution**: Use value objects
```python
class Measurement:
    def __init__(self, value, unit):
        self.value = value
        self.unit = Unit(unit)  # Enum
    
    def to_cm(self):
        # Conversion logic encapsulated
        pass

class Rectangle:
    def __init__(self, width: Measurement, height: Measurement):
        self.width = width
        self.height = height
    
    def area(self) -> Measurement:
        # Calculation with proper units
        pass
```

### Switch Statements

**Bad Example**:
```java
public double getSalary(Employee e) {
    switch (e.getType()) {
        case ENGINEER:
            return e.getMonthlySalary() * 1.2;
        case MANAGER:
            return e.getMonthlySalary() * 1.5;
        case SALESMAN:
            return e.getMonthlySalary() + e.getCommission();
        default:
            return e.getMonthlySalary();
    }
}
```

**Why It's Bad**:
- Violates Open/Closed Principle
- Must modify when adding types
- Logic scattered across codebase
- Hard to test all branches

**Solution**: Use polymorphism
```java
abstract class Employee {
    abstract double getPay();
}

class Engineer extends Employee {
    double getPay() { return monthlySalary * 1.2; }
}

class Manager extends Employee {
    double getPay() { return monthlySalary * 1.5; }
}
```

### Temporary Field

**Bad Example**:
```python
class ReportGenerator:
    def __init__(self):
        self.temp_data = None  # Only used in one method
        self.cache = None      # Sometimes initialized, sometimes not
    
    def generate_report(self):
        self.temp_data = self.fetch_data()
        # ... use temp_data
        self.temp_data = None  # Reset after use
```

**Why It's Bad**:
- Confusing object state
- Wastes memory
- Unclear when field is valid
- Indicates misplaced responsibility

**Solution**: Extract method or class
```python
class ReportGenerator:
    def generate_report(self):
        data = self.fetch_data()
        return self._process_data(data)
    
    def _process_data(self, data):
        # Local variable, clear scope
        pass
```

## Detection Patterns

Watch for these indicators:
- Methods longer than 20 lines
- Classes with more than 10 methods
- Duplicate code blocks (3+ lines)
- Many parameters (4+) in method signatures
- Extensive use of primitive types for domain concepts
- Large switch/case statements
- Fields only used in one method

## Prevention Strategies

1. **Follow SOLID Principles**: Single responsibility, open/closed, etc.
2. **Refactor Continuously**: Small improvements regularly
3. **Code Reviews**: Catch smells before merging
4. **Automated Analysis**: Use tools like SonarQube, ESLint
5. **TDD**: Tests encourage better design
6. **Pair Programming**: Two sets of eyes catch issues

## Testing Checklist

- [ ] Are there duplicate code blocks?
- [ ] Do methods do one thing only?
- [ ] Are classes focused on single responsibility?
- [ ] Are primitives wrapped in domain types?
- [ ] Is polymorphism used instead of conditionals?
- [ ] Are all fields used throughout the object lifecycle?
- [ ] Can I explain each class's purpose in one sentence?

## Related Documents

- [[spaghetti_code]] - Unstructured code resulting from ignored smells
- [[bad_variable_names]] - Naming issues that hide problems
- [[poor_documentation]] - Lack of docs makes smells harder to spot
- [[circular_dependencies]] - Structural smell indicating design issues
