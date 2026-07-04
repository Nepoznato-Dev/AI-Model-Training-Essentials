# Programming Fundamentals Skill

## Overview

Programming fundamentals encompass the core concepts, principles, and practices that form the foundation of software development. These universal concepts apply across programming languages and paradigms, enabling developers to write clean, efficient, and maintainable code regardless of the specific technology stack.

## When to Use

- Learning a new programming language or paradigm
- Writing production code for applications and services
- Reviewing and refactoring existing codebases
- Teaching or mentoring junior developers
- Conducting code reviews and technical interviews
- Designing software architecture and components
- Debugging and troubleshooting code issues
- Building scalable and maintainable systems

## Core Competencies

### Syntax & Semantics
- Variables and data types (primitive, composite, custom)
- Operators (arithmetic, logical, comparison, assignment)
- Control flow (conditionals, loops, branching)
- Functions and methods (parameters, return values, scope)
- Error handling (exceptions, try-catch, error codes)
- Comments and documentation conventions
- Language-specific idioms and best practices

### Data Structures
- Arrays and lists (dynamic, static, linked)
- Stacks and queues (LIFO, FIFO)
- Hash tables and dictionaries
- Trees (binary, BST, balanced trees)
- Graphs (directed, undirected, weighted)
- Sets and maps
- Tuples and records
- Choosing appropriate structures for use cases

### Algorithms
- Searching (linear, binary, hash-based)
- Sorting (bubble, merge, quick, heap)
- Recursion and iteration
- Dynamic programming
- Greedy algorithms
- Divide and conquer
- Time and space complexity analysis (Big O notation)
- Algorithm optimization techniques

### Object-Oriented Programming (OOP)
- Classes and objects
- Encapsulation and information hiding
- Inheritance and composition
- Polymorphism (overloading, overriding)
- Abstraction and interfaces
- Design patterns (Singleton, Factory, Observer, etc.)
- SOLID principles
- Object lifecycle management

### Functional Programming Concepts
- Pure functions and immutability
- First-class and higher-order functions
- Lambda expressions and closures
- Function composition
- Map, filter, reduce operations
- Currying and partial application
- Monads and functors (advanced)
- State management without mutation

### Memory Management
- Stack vs heap allocation
- Garbage collection principles
- Manual memory management (malloc/free, new/delete)
- Memory leaks and detection
- Reference counting
- Smart pointers (unique_ptr, shared_ptr)
- Buffer overflows and prevention
- Performance implications of memory choices

## Design Principles

### SOLID Principles
- **Single Responsibility Principle (SRP)**: A class should have one reason to change
- **Open/Closed Principle (OCP)**: Open for extension, closed for modification
- **Liskov Substitution Principle (LSP)**: Subtypes must be substitutable for base types
- **Interface Segregation Principle (ISP)**: Many specific interfaces better than one general
- **Dependency Inversion Principle (DIP)**: Depend on abstractions, not concretions

### DRY (Don't Repeat Yourself)
- Eliminate duplication through abstraction
- Extract common logic into reusable functions
- Use templates and generics
- Create utility libraries
- Balance against premature abstraction

### KISS (Keep It Simple, Stupid)
- Prefer simple solutions over complex ones
- Avoid unnecessary abstraction layers
- Write self-explanatory code
- Minimize cognitive load for readers
- Simplicity enables maintainability

### YAGNI (You Ain't Gonna Need It)
- Don't add functionality until necessary
- Avoid speculative features
- Build for current requirements
- Refactor when needs emerge
- Resist over-engineering

### Separation of Concerns
- Divide program into distinct sections
- Each section addresses separate concern
- Modular architecture
- Clear boundaries between components
- Independent testability

## Frameworks & Methods

### Development Methodologies
- **Test-Driven Development (TDD)**: Red-Green-Refactor cycle
- **Behavior-Driven Development (BDD)**: Given-When-Then specifications
- **Domain-Driven Design (DDD)**: Model driven by business domain
- **Extreme Programming (XP)**: Pair programming, continuous feedback
- **Clean Code**: Readable, maintainable code practices

### Code Organization Patterns
- **Layered Architecture**: Presentation, business logic, data access
- **Model-View-Controller (MVC)**: Separation of data, UI, control logic
- **Repository Pattern**: Abstract data access layer
- **Service Layer**: Business logic encapsulation
- **Dependency Injection**: Externalize dependencies

### Version Control Practices
- Commit frequently with meaningful messages
- Feature branch workflow
- Pull request code reviews
- Semantic versioning
- Tagging releases
- Resolving merge conflicts
- Git bisect for debugging

### Documentation Standards
- Inline comments for complex logic
- Function/method docstrings
- README files for projects
- API documentation (OpenAPI/Swagger)
- Architecture decision records (ADRs)
- Changelog maintenance
- Code examples and tutorials

## Practical Templates

### Function Template
```python
def function_name(param1: Type1, param2: Type2) -> ReturnType:
    """
    Brief description of what the function does.
    
    Args:
        param1: Description of parameter 1
        param2: Description of parameter 2
    
    Returns:
        Description of return value
    
    Raises:
        ExceptionType: When this exception might be raised
    
    Example:
        >>> function_name(arg1, arg2)
        expected_result
    """
    # Implementation here
    pass
```

### Class Template
```python
class ClassName:
    """
    Brief description of the class purpose.
    
    Attributes:
        attribute1: Description of attribute 1
        attribute2: Description of attribute 2
    """
    
    def __init__(self, param1: Type1, param2: Type2):
        """Initialize the class with required parameters."""
        self._attribute1 = param1
        self._attribute2 = param2
    
    def public_method(self, param: Type) -> ReturnType:
        """Public method description."""
        pass
    
    def _private_method(self) -> None:
        """Private helper method description."""
        pass
    
    def __str__(self) -> str:
        """String representation of the object."""
        return f"ClassName(attr1={self._attribute1})"
```

### Error Handling Template
```python
try:
    result = risky_operation()
    validate_result(result)
except SpecificError as e:
    logger.error(f"Specific error occurred: {e}")
    handle_specific_error(e)
except GeneralError as e:
    logger.error(f"General error occurred: {e}")
    raise CustomException("Operation failed", original_exception=e)
else:
    logger.info("Operation completed successfully")
    return process_result(result)
finally:
    cleanup_resources()
```

### Code Review Checklist
- [ ] Code follows style guidelines
- [ ] Functions are small and focused
- [ ] Variable names are descriptive
- [ ] No duplicate code (DRY)
- [ ] Error handling is comprehensive
- [ ] Tests cover edge cases
- [ ] Documentation is clear
- [ ] No security vulnerabilities
- [ ] Performance considerations addressed
- [ ] Backward compatibility maintained

## Common Pitfalls

### Off-by-One Errors
**Problem**: Loop boundaries or array indices off by one.
**Solution**: Use clear boundary conditions, prefer `<` over `<=`, write tests for edge cases.

### Null Pointer Exceptions
**Problem**: Accessing properties/methods on null references.
**Solution**: Use null checks, Optional types, null object pattern, defensive programming.

### Memory Leaks
**Problem**: Unreleased memory causing application slowdown or crash.
**Solution**: Proper resource cleanup, use smart pointers, profile memory usage, avoid circular references.

### Race Conditions
**Problem**: Concurrent access to shared resources causing unpredictable behavior.
**Solution**: Use synchronization primitives, immutable data, thread-safe collections, proper locking strategies.

### Premature Optimization
**Problem**: Optimizing before identifying actual bottlenecks.
**Solution**: Profile first, optimize hot paths, prioritize readability, measure impact of changes.

### Magic Numbers and Strings
**Problem**: Hardcoded values scattered throughout code.
**Solution**: Use named constants, configuration files, enums, centralized settings.

### Tight Coupling
**Problem**: Components overly dependent on each other.
**Solution**: Use interfaces, dependency injection, event-driven architecture, loose coupling patterns.

### Ignoring Edge Cases
**Problem**: Code fails with unexpected inputs or boundary conditions.
**Solution**: Write comprehensive tests, consider empty/null/invalid inputs, test boundary values.

## Best Practices

### Do
- Write self-documenting code with clear names
- Keep functions small (< 50 lines ideally)
- Handle errors explicitly and gracefully
- Write unit tests for critical logic
- Use version control for all code
- Refactor regularly to reduce technical debt
- Follow consistent coding standards
- Document complex algorithms and decisions
- Validate all external inputs
- Log meaningfully for debugging

### Don't
- Write functions longer than a screen
- Use cryptic variable names (i, x, temp)
- Ignore compiler warnings or linter errors
- Comment out code instead of removing it
- Hardcode credentials or sensitive data
- Catch exceptions without handling them
- Optimize before profiling
- Copy-paste code without understanding
- Commit without testing
- Break backward compatibility without notice

## Tools & Resources

### Integrated Development Environments (IDEs)
- **Visual Studio Code** - Lightweight, extensible editor
- **IntelliJ IDEA** - Java/Kotlin powerhouse
- **PyCharm** - Python-specific IDE
- **Eclipse** - Enterprise Java development
- **Xcode** - macOS/iOS development
- **Visual Studio** - .NET and C++ development

### Code Quality Tools
- **SonarQube** - Continuous code quality inspection
- **ESLint** - JavaScript linting
- **Pylint/Flake8** - Python linting
- **Checkstyle** - Java code standards
- **RuboCop** - Ruby code analysis
- **Prettier** - Code formatting

### Testing Frameworks
- **JUnit** - Java unit testing
- **pytest** - Python testing framework
- **Jest** - JavaScript testing
- **RSpec** - Ruby testing
- **xUnit/nUnit** - .NET testing
- **Go test** - Go built-in testing

### Debugging Tools
- **GDB** - GNU debugger for C/C++
- **pdb** - Python debugger
- **Chrome DevTools** - Web debugging
- **Visual Studio Debugger** - Multi-language debugging
- **Wireshark** - Network protocol analysis
- **Valgrind** - Memory debugging

### Build & Dependency Management
- **Maven/Gradle** - Java build tools
- **npm/yarn** - JavaScript package managers
- **pip/poetry** - Python package management
- **Cargo** - Rust package manager
- **Make/CMake** - Build automation
- **Docker** - Containerization

## Real-World Examples

### REST API Endpoint
```python
from flask import Flask, request, jsonify
from typing import Dict, Any, Optional

app = Flask(__name__)

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id: int) -> tuple[Dict[str, Any], int]:
    """
    Retrieve user by ID with proper error handling.
    
    Returns JSON response with appropriate HTTP status code.
    """
    try:
        user = user_repository.find_by_id(user_id)
        
        if user is None:
            return jsonify({'error': 'User not found'}), 404
        
        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'created_at': user.created_at.isoformat()
        }), 200
        
    except DatabaseError as e:
        logger.error(f"Database error retrieving user {user_id}: {e}")
        return jsonify({'error': 'Internal server error'}), 500
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400
```

### Data Processing Pipeline
```python
def process_data_pipeline(raw_data: List[Dict]) -> ProcessingResult:
    """
    Process raw data through validation, transformation, and aggregation.
    
    Demonstrates functional programming patterns with map/filter/reduce.
    """
    # Filter invalid records
    valid_records = filter(is_valid_record, raw_data)
    
    # Transform to standard format
    normalized = map(normalize_record, valid_records)
    
    # Group by category
    grouped = group_by(normalized, key=lambda r: r['category'])
    
    # Aggregate statistics per group
    results = {
        category: calculate_statistics(records)
        for category, records in grouped.items()
    }
    
    return ProcessingResult(
        total_processed=len(raw_data),
        valid_count=len(valid_records),
        aggregated_results=results,
        timestamp=datetime.utcnow()
    )
```

### Design Pattern Implementation
**Observer Pattern Example**:
```python
from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self, subject: 'Subject') -> None:
        pass

class Subject:
    def __init__(self):
        self._observers: List[Observer] = []
        self._state: Any = None
    
    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)
    
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
    
    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)
    
    def set_state(self, state: Any) -> None:
        self._state = state
        self.notify()
```

## Metrics for Success

### Code Quality Metrics
- Cyclomatic complexity < 10 per function
- Code coverage > 80% for critical paths
- Technical debt ratio < 5%
- Duplication rate < 3%
- Maintainability index > 65

### Performance Metrics
- Response time within SLA requirements
- Memory usage within allocated limits
- CPU utilization optimized (< 70% average)
- Database query performance (index usage, execution time)
- Throughput meets business requirements

### Productivity Metrics
- Lead time for changes (commit to deploy)
- Deployment frequency
- Mean time to recovery (MTTR)
- Change failure rate
- Code review turnaround time

### Defect Metrics
- Bug density (bugs per KLOC)
- Defect escape rate (bugs found in production)
- Time to fix critical bugs
- Regression rate after changes

## Practice Exercises

### Beginner
1. Implement classic algorithms (binary search, bubble sort)
2. Build a calculator with proper error handling
3. Create a todo list application with file persistence
4. Solve coding challenges on LeetCode/HackerRank (easy level)
5. Refactor poorly written code for readability

### Intermediate
1. Build a REST API with authentication and database integration
2. Implement common design patterns (Factory, Observer, Strategy)
3. Create a multi-threaded web scraper
4. Optimize slow code using profiling tools
5. Write comprehensive unit tests for existing codebase

### Advanced
1. Design and implement a distributed system component
2. Contribute to open-source projects
3. Build a compiler or interpreter for a simple language
4. Implement concurrent data structures
5. Optimize algorithm complexity from O(n²) to O(n log n)

## Getting Started

### Learning Path
1. **Choose First Language**: Python, JavaScript, or Java recommended
2. **Master Basics**: Variables, loops, functions, basic data structures
3. **Learn OOP**: Classes, objects, inheritance, polymorphism
4. **Study Algorithms**: Sorting, searching, complexity analysis
5. **Practice Regularly**: Daily coding challenges and projects
6. **Read Code**: Study well-written open-source projects
7. **Build Projects**: Apply learning to real applications
8. **Get Feedback**: Code reviews, pair programming, mentoring

### Recommended Resources
- Books: "Clean Code" by Robert C. Martin
- Books: "Introduction to Algorithms" by Cormen et al.
- Books: "Design Patterns" by Gang of Four
- Courses: Coursera "Algorithms Specialization"
- Platforms: LeetCode, HackerRank, Exercism
- Documentation: Official language docs and style guides

### First Project Ideas
- Personal portfolio website
- Weather app using public API
- Expense tracker with data visualization
- Chat application with WebSocket
- Blog platform with CRUD operations
- Automation script for repetitive tasks

## Quick Reference Card

### Big O Complexity Hierarchy
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)

### Common Data Structure Operations
| Structure | Access | Search | Insert | Delete |
|-----------|--------|--------|--------|--------|
| Array | O(1) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1)* | O(1)* |
| Hash Table | N/A | O(1)* | O(1)* | O(1)* |
| Binary Search Tree | O(log n) | O(log n) | O(log n) | O(log n) |
| Heap | O(1) | O(n) | O(log n) | O(log n) |
*Average case

### SOLID Acronym
- **S** - Single Responsibility Principle
- **O** - Open/Closed Principle
- **L** - Liskov Substitution Principle
- **I** - Interface Segregation Principle
- **D** - Dependency Inversion Principle

### Common Design Patterns
- **Creational**: Singleton, Factory, Builder, Prototype
- **Structural**: Adapter, Decorator, Facade, Proxy
- **Behavioral**: Observer, Strategy, Command, Iterator

### Debugging Steps
1. Reproduce the issue consistently
2. Check logs and error messages
3. Isolate the problematic code
4. Add debug statements/breakpoints
5. Form hypothesis about cause
6. Test hypothesis
7. Implement and verify fix
8. Add test to prevent regression

## Mastery Tips

1. **Read Code Daily**: Study well-written code from experienced developers
2. **Write Tests First**: TDD improves design and catches bugs early
3. **Refactor Ruthlessly**: Code is never done, continuously improve it
4. **Understand Before Changing**: Don't modify code you don't understand
5. **Learn Multiple Paradigms**: OOP, functional, procedural各有优势
6. **Master Your Tools**: IDE shortcuts, debugging, profiling save hours
7. **Teach Others**: Explaining concepts deepens your understanding
8. **Stay Curious**: Technology evolves, keep learning new languages and tools
9. **Focus on Fundamentals**: Languages change, core concepts endure
10. **Build Things**: Theory is important, but practice makes mastery

## Related Skills

- **Algorithm Design** - Efficient algorithm implementation
- **Data Structures** - Choosing and implementing appropriate data structures
- **System Design** - Designing scalable software systems
- **Code Quality** - Writing clean, maintainable code
- **Debugging** - Finding and fixing code defects
- **Testing** - Verifying code correctness
- **Software Architecture** - High-level system organization

---

*This skill document is part of the Skills Repository. For more skills, visit the main repository.*
