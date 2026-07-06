# Spaghetti Code

## Overview

Spaghetti code refers to unstructured and difficult-to-maintain source code. It gets its name from the tangled, twisted nature of the code flow, resembling a plate of spaghetti. This anti-pattern typically results from excessive use of goto statements, nested conditionals, inconsistent indentation, and lack of modularization.

## When to Reference This Document

- Reviewing legacy codebases with poor structure
- Refactoring complex, hard-to-follow code
- Training developers on code organization best practices
- Identifying technical debt indicators
- Planning code restructuring initiatives

## Characteristics of Spaghetti Code

### Excessive Nesting

**Bad Example**:
```python
def process_order(order):
    if order:
        if order.items:
            if len(order.items) > 0:
                for item in order.items:
                    if item.in_stock:
                        if item.price > 0:
                            if order.customer:
                                if order.customer.active:
                                    if order.customer.verified:
                                        # Finally process the order
                                        pass
                                    else:
                                        return "Customer not verified"
                                else:
                                    return "Customer not active"
                            else:
                                return "No customer"
                        else:
                            return "Invalid price"
                    else:
                        return "Item out of stock"
            else:
                return "No items"
        else:
            return "Empty items list"
    else:
        return "No order"
```

**Why It's Bad**:
- Deep nesting makes code hard to read
- Difficult to follow the execution flow
- Hard to test individual conditions
- Prone to bugs when modifying

**Solution**: Use early returns and guard clauses
```python
def process_order(order):
    if not order:
        return "No order"
    
    if not order.items or len(order.items) == 0:
        return "No items"
    
    for item in order.items:
        if not item.in_stock:
            return "Item out of stock"
        if item.price <= 0:
            return "Invalid price"
    
    if not order.customer:
        return "No customer"
    if not order.customer.active:
        return "Customer not active"
    if not order.customer.verified:
        return "Customer not verified"
    
    # Process the order
    return "Order processed"
```

### Goto Statements and Jump Logic

**Bad Example**:
```python
def validate_user(data):
    i = 0
    start:
    if i >= len(data):
        goto end
    
    if data[i] < 0:
        goto error
    
    if data[i] > 100:
        i += 1
        goto start
    
    # More scattered logic
    error:
    print("Error at index", i)
    return False
    
    end:
    return True
```

**Why It's Bad**:
- Breaks structured programming principles
- Makes control flow unpredictable
- Nearly impossible to debug
- Cannot be easily refactored

**Solution**: Use proper control structures
```python
def validate_user(data):
    for i, value in enumerate(data):
        if value < 0:
            print(f"Error at index {i}")
            return False
        if value > 100:
            continue
    return True
```

### Mixed Concerns

**Bad Example**:
```javascript
function handleRequest(req, res) {
    // Database connection
    const db = connectDB();
    
    // Validation
    if (!req.body.email) {
        res.send(400);
        return;
    }
    
    // Business logic
    const user = db.query('SELECT * FROM users WHERE email = ?', req.body.email);
    
    // More validation
    if (!user) {
        // Logging
        console.log('User not found:', req.body.email);
        res.send(404);
        return;
    }
    
    // Authentication
    if (!checkPassword(req.body.password, user.hash)) {
        res.send(401);
        return;
    }
    
    // More business logic
    const token = generateToken(user);
    
    // Response formatting
    res.json({ token: token, user: user });
    
    // Cleanup
    db.close();
}
```

**Why It's Bad**:
- Multiple responsibilities in one function
- Hard to test individual concerns
- Difficult to modify without breaking other parts
- No separation of concerns

**Solution**: Separate into focused functions
```javascript
async function handleRequest(req, res) {
    try {
        const validatedData = validateRequest(req.body);
        const user = await findUserByEmail(validatedData.email);
        await authenticateUser(user, validatedData.password);
        const token = generateToken(user);
        res.json(formatResponse(token, user));
    } catch (error) {
        handleError(error, res);
    }
}
```

## Real-World Scenarios

### Scenario 1: Legacy Financial System
A banking application with 2000-line functions containing hundreds of nested if-statements. Any modification takes weeks because developers cannot predict side effects.

### Scenario 2: Game Development
A game engine where rendering, physics, input handling, and AI logic are all intertwined in the same update loop, making it impossible to optimize individual systems.

### Scenario 3: E-commerce Platform
Checkout process with payment validation, inventory checks, shipping calculations, and email notifications all in one massive function with multiple exit points.

## Detection Patterns

Look for these warning signs:
- Functions longer than 50 lines
- Nesting depth greater than 3 levels
- Multiple return statements scattered throughout
- Comments like "HACK" or "FIXME" every few lines
- Variables with generic names like `temp`, `data`, `flag`
- Copy-pasted code blocks with minor variations

## Prevention Strategies

1. **Follow Single Responsibility Principle**: Each function should do one thing
2. **Use Early Returns**: Reduce nesting with guard clauses
3. **Extract Methods**: Break large functions into smaller ones
4. **Consistent Indentation**: Enforce coding standards
5. **Code Reviews**: Catch spaghetti code before merging
6. **Automated Linting**: Use tools to detect complexity
7. **Refactor Continuously**: Don't let technical debt accumulate

## Testing Checklist

- [ ] Can I explain what this function does in one sentence?
- [ ] Is the maximum nesting depth 3 or less?
- [ ] Are there fewer than 20 lines per function?
- [ ] Does each function have a single responsibility?
- [ ] Can I test this function in isolation?
- [ ] Is the control flow linear and predictable?
- [ ] Are variable names descriptive and meaningful?

## Related Documents

- [[code_smells]] - Other indicators of poor code quality
- [[bad_variable_names]] - Naming issues that contribute to confusion
- [[poor_documentation]] - Lack of documentation compounds spaghetti code problems
- [[circular_dependencies]] - Structural issues that create tangled code
