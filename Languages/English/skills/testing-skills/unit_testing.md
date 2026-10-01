---
# Metadata
title: "Unit Testing"
description: "Testing individual components or functions in isolation to verify correct behavior, enable confident refactoring, and catch bugs early."
category: "Testing Skills"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-01-15"
    author: "AI Model Training Team"
    changes: "Initial skill creation"

# Review
created: "2026-01-15"
last_modified: "2026-01-15"
review_date: "2026-07-15"
reviewed_by: "Testing Skills Team"
next_review: "2027-01-15"

# Classification
tags: [unit-testing, test-driven-development, mocking, code-coverage]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Unit Testing

## Overview

Unit testing is the practice of testing individual components or functions in isolation to verify they behave as expected. Well-written unit tests serve as documentation, enable confident refactoring, and catch bugs early in the development cycle.

This skill covers writing effective unit tests, test organization, mocking strategies, and best practices for maintaining a robust test suite.

## Core Competencies

- **Test Design**: Writing clear, focused, and maintainable tests
- **Assertions**: Choosing appropriate assertion methods
- **Test Doubles**: Mocks, stubs, spies, and fakes
- **Test Organization**: Structuring test files and suites
- **Code Coverage**: Measuring and improving test coverage
- **Parameterized Tests**: Testing multiple scenarios efficiently
- **Fixture Management**: Setup and teardown patterns
- **Test Naming**: Clear, descriptive test names

## When to Use

Unit testing is valuable when:
- ✅ Writing new features or functionality
- ✅ Refactoring existing code
- ✅ Fixing bugs (write test first, then fix)
- ✅ Working on shared libraries or APIs
- ✅ Building critical business logic
- ✅ Collaborating with other developers
- ✅ Maintaining legacy code

**Not ideal for:**
- ❌ Testing UI/UX elements (use integration or E2E tests)
- ❌ Testing database connections directly (use integration tests)
- ❌ Testing third-party library internals
- ❌ One-off scripts or prototypes

## The AAA Pattern

Arrange, Act, Assert is the standard structure for unit tests.

```python
def test_calculate_discount():
    # Arrange - Set up test data and conditions
    original_price = 100.0
    discount_percent = 20
    expected_price = 80.0
    
    # Act - Execute the code being tested
    result = calculate_discount(original_price, discount_percent)
    
    # Assert - Verify the outcome
    assert result == expected_price
```

## Test Organization

### File Structure

```
src/
├── calculator.py
├── user_service.py
└── payment_processor.py

tests/
├── test_calculator.py
├── test_user_service.py
└── test_payment_processor.py
```

### Test Class Structure

```python
import pytest
from src.calculator import Calculator

class TestCalculator:
    """Test suite for Calculator class."""
    
    def setup_method(self):
        """Run before each test method."""
        self.calc = Calculator()
    
    def teardown_method(self):
        """Run after each test method."""
        pass
    
    def test_addition(self):
        """Test that addition works correctly."""
        result = self.calc.add(2, 3)
        assert result == 5
    
    def test_division_by_zero(self):
        """Test that division by zero raises exception."""
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(10, 0)
```

## Mocking Strategies

### When to Mock

Mock external dependencies to:
- Isolate the unit under test
- Speed up test execution
- Test edge cases (errors, timeouts)
- Avoid side effects (database writes, API calls)

### Python Mocking Example

```python
from unittest.mock import Mock, patch, MagicMock
import pytest

def test_fetch_user_data():
    """Test with mocked HTTP request."""
    # Create mock response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'id': 1,
        'name': 'John Doe',
        'email': 'john@example.com'
    }
    
    # Patch the requests.get method
    with patch('requests.get', return_value=mock_response) as mock_get:
        result = fetch_user_data(1)
        
        assert result['name'] == 'John Doe'
        mock_get.assert_called_once_with('https://api.example.com/users/1')

def test_payment_processing():
    """Test with mocked payment gateway."""
    mock_gateway = MagicMock()
    mock_gateway.process_payment.return_value = {
        'success': True,
        'transaction_id': 'txn_12345'
    }
    
    processor = PaymentProcessor(mock_gateway)
    result = processor.charge(99.99, 'card_123')
    
    assert result['success'] is True
    mock_gateway.process_payment.assert_called_once_with(99.99, 'card_123')
```

### JavaScript/Jest Mocking Example

```javascript
// Mock axios HTTP client
jest.mock('axios');
import axios from 'axios';

test('fetches user data successfully', async () => {
  const mockData = {
    id: 1,
    name: 'John Doe'
  };
  
  axios.get.mockResolvedValue({ data: mockData });
  
  const result = await fetchUser(1);
  
  expect(result).toEqual(mockData);
  expect(axios.get).toHaveBeenCalledWith('/api/users/1');
});

// Mock a module
jest.mock('../services/paymentService', () => ({
  processPayment: jest.fn().mockResolvedValue({
    success: true,
    transactionId: 'txn_12345'
  })
}));
```

## Parameterized Tests

### Python pytest

```python
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (5, 5, 10),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300)
])
def test_addition(a, b, expected):
    """Test addition with multiple inputs."""
    assert add(a, b) == expected

@pytest.mark.parametrize("input,expected", [
    ("racecar", True),
    ("hello", False),
    ("", True),
    ("a", True),
    ("abba", True),
    ("abc", False)
])
def test_is_palindrome(input, expected):
    """Test palindrome detection."""
    assert is_palindrome(input) == expected
```

### JavaScript/Jest

```javascript
test.each([
  [1, 2, 3],
  [5, 5, 10],
  [-1, 1, 0],
  [0, 0, 0],
  [100, 200, 300]
])('add(%i, %i) returns %i', (a, b, expected) => {
  expect(add(a, b)).toBe(expected);
});

test.each([
  ['racecar', true],
  ['hello', false],
  ['', true],
  ['a', true],
  ['abba', true]
])('isPalindrome("%s") returns %s', (input, expected) => {
  expect(isPalindrome(input)).toBe(expected);
});
```

## Common Pitfalls

### 🚫 Testing Implementation Details

**Problem:** Tests break when implementation changes but behavior stays same.

**Solution:**
```python
# ❌ Bad: Testing internal state
def test_user_creation():
    user = User.create("john", "john@example.com")
    assert user._id is not None  # Testing private attribute
    assert user._created_at is not None

# ✅ Good: Testing observable behavior
def test_user_creation():
    user = User.create("john", "john@example.com")
    assert user.get_name() == "john"
    assert user.get_email() == "john@example.com"
    assert user.id is not None  # Public property
```

### 🚫 Over-Mocking

**Problem:** Mocking too much makes tests meaningless.

**Solution:**
```python
# ❌ Bad: Mocking everything
@patch('module.database')
@patch('module.cache')
@patch('module.logger')
@patch('module.config')
def test_process_order(mock_config, mock_logger, mock_cache, mock_db):
    # Test has no real value

# ✅ Good: Mock only external dependencies
@patch('module.payment_gateway')
def test_process_order(mock_gateway):
    # Test verifies actual business logic
```

### 🚫 Interdependent Tests

**Problem:** Tests depend on execution order or shared state.

**Solution:**
```python
# ❌ Bad: Tests share state
class TestShoppingCart:
    cart = ShoppingCart()  # Shared across all tests!
    
    def test_add_item(self):
        self.cart.add("item1")
        assert len(self.cart.items) == 1
    
    def test_remove_item(self):
        self.cart.remove("item1")  # Depends on previous test
        assert len(self.cart.items) == 0

# ✅ Good: Each test is independent
class TestShoppingCart:
    def test_add_item(self):
        cart = ShoppingCart()
        cart.add("item1")
        assert len(cart.items) == 1
    
    def test_remove_item(self):
        cart = ShoppingCart()
        cart.add("item1")
        cart.remove("item1")
        assert len(cart.items) == 0
```

### 🚫 Flaky Tests with Timing

**Problem:** Tests fail intermittently due to timing issues.

**Solution:**
```python
# ❌ Bad: Using sleep
def test_async_operation():
    start_operation()
    time.sleep(5)  # Flaky!
    assert operation_complete()

# ✅ Good: Wait for condition
def test_async_operation():
    start_operation()
    wait_until(lambda: operation_complete(), timeout=10)
    assert operation_complete()
```

## Best Practices

### ✅ Do

- Write tests before or during implementation (TDD)
- Keep tests simple and focused
- Use descriptive test names that explain the scenario
- Test one thing per test method
- Mock external dependencies (APIs, databases, file systems)
- Clean up resources in teardown methods
- Run tests frequently (locally and in CI/CD)
- Maintain high code coverage (>80% for critical paths)
- Review tests in code reviews
- Update tests when requirements change

### ❌ Don't

- Write tests after implementation (often leads to poor tests)
- Test multiple things in one test
- Use vague test names like "test1" or "test_basic"
- Share state between tests
- Mock the unit you're testing
- Ignore failing tests
- Test private methods directly
- Hard-code test data without explanation
- Skip error case testing
- Commit tests that don't pass

## Tools & Resources

### Testing Frameworks

| Language | Framework | Best For |
|----------|-----------|----------|
| **Python** | pytest, unittest | General purpose |
| **JavaScript** | Jest, Mocha, Vitest | Frontend/Node.js |
| **Java** | JUnit, TestNG | Enterprise applications |
| **C#** | xUnit, NUnit, MSTest | .NET applications |
| **Ruby** | RSpec, Minitest | Rails applications |
| **Go** | testing (built-in) | Go services |
| **TypeScript** | Jest, Vitest | TypeScript projects |

### Assertion Libraries

| Library | Language | Features |
|---------|----------|----------|
| **AssertJ** | Java | Fluent assertions |
| **Chai** | JavaScript | BDD/TDD assertions |
| **Hamcrest** | Java, Python | Matcher objects |
| **Shouldly** | C# | Should-style assertions |

### Mocking Libraries

| Library | Language | Description |
|---------|----------|-------------|
| **unittest.mock** | Python | Built-in mocking |
| **Mockito** | Java | Popular Java mocking |
| **Sinon.JS** | JavaScript | Spies, stubs, mocks |
| **Moq** | C# | .NET mocking |
| **gomock** | Go | Go mocking framework |

### Coverage Tools

| Tool | Language | Purpose |
|------|----------|---------|
| **Coverage.py** | Python | Code coverage |
| **Istanbul/nyc** | JavaScript | JS coverage |
| **JaCoCo** | Java | Java coverage |
| **Coverlet** | C# | .NET coverage |

## Examples

### Example 1: Testing a Service Layer

```python
# tests/test_user_service.py
import pytest
from unittest.mock import Mock, patch
from src.user_service import UserService
from src.exceptions import UserNotFoundError, EmailAlreadyExistsError

class TestUserService:
    
    @pytest.fixture
    def mock_repository(self):
        return Mock()
    
    @pytest.fixture
    def mock_email_service(self):
        return Mock()
    
    @pytest.fixture
    def user_service(self, mock_repository, mock_email_service):
        return UserService(mock_repository, mock_email_service)
    
    def test_create_user_success(self, user_service, mock_repository, mock_email_service):
        """Test successful user creation."""
        # Arrange
        user_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'password': 'securepass123'
        }
        mock_repository.find_by_email.return_value = None
        mock_repository.save.return_value = {'id': 1, **user_data}
        
        # Act
        result = user_service.create_user(user_data)
        
        # Assert
        assert result['id'] == 1
        assert result['email'] == user_data['email']
        mock_repository.save.assert_called_once()
        mock_email_service.send_welcome_email.assert_called_once_with(
            user_data['email'],
            user_data['name']
        )
    
    def test_create_user_duplicate_email(self, user_service, mock_repository):
        """Test that duplicate email raises exception."""
        # Arrange
        user_data = {'email': 'existing@example.com'}
        mock_repository.find_by_email.return_value = {'id': 999}
        
        # Act & Assert
        with pytest.raises(EmailAlreadyExistsError):
            user_service.create_user(user_data)
        
        mock_repository.save.assert_not_called()
    
    def test_get_user_by_id_found(self, user_service, mock_repository):
        """Test retrieving existing user."""
        # Arrange
        expected_user = {'id': 1, 'name': 'John', 'email': 'john@example.com'}
        mock_repository.find_by_id.return_value = expected_user
        
        # Act
        result = user_service.get_user(1)
        
        # Assert
        assert result == expected_user
        mock_repository.find_by_id.assert_called_once_with(1)
    
    def test_get_user_by_id_not_found(self, user_service, mock_repository):
        """Test that missing user raises exception."""
        # Arrange
        mock_repository.find_by_id.return_value = None
        
        # Act & Assert
        with pytest.raises(UserNotFoundError):
            user_service.get_user(999)
```

### Example 2: Testing React Component

```javascript
// tests/UserProfile.test.jsx
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { UserProfile } from '../components/UserProfile';
import * as api from '../api/userApi';

// Mock the API module
jest.mock('../api/userApi');

describe('UserProfile', () => {
  const mockUser = {
    id: 1,
    name: 'John Doe',
    email: 'john@example.com',
    bio: 'Software developer'
  };

  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('displays loading state initially', () => {
    api.fetchUser.mockImplementation(() => new Promise(() => {}));
    
    render(<UserProfile userId={1} />);
    
    expect(screen.getByText(/loading/i)).toBeInTheDocument();
  });

  it('displays user data after successful fetch', async () => {
    api.fetchUser.mockResolvedValue(mockUser);
    
    render(<UserProfile userId={1} />);
    
    await waitFor(() => {
      expect(screen.getByText('John Doe')).toBeInTheDocument();
      expect(screen.getByText('john@example.com')).toBeInTheDocument();
      expect(screen.getByText('Software developer')).toBeInTheDocument();
    });
  });

  it('displays error message on fetch failure', async () => {
    api.fetchUser.mockRejectedValue(new Error('Failed to fetch'));
    
    render(<UserProfile userId={1} />);
    
    await waitFor(() => {
      expect(screen.getByText(/error/i)).toBeInTheDocument();
    });
  });

  it('calls onSave with updated user data', async () => {
    api.fetchUser.mockResolvedValue(mockUser);
    const onSave = jest.fn();
    
    render(<UserProfile userId={1} onSave={onSave} />);
    
    await waitFor(() => {
      expect(screen.getByText('John Doe')).toBeInTheDocument();
    });
    
    const nameInput = screen.getByLabelText(/name/i);
    fireEvent.change(nameInput, { target: { value: 'Jane Doe' } });
    
    const saveButton = screen.getByRole('button', { name: /save/i });
    fireEvent.click(saveButton);
    
    expect(onSave).toHaveBeenCalledWith({
      ...mockUser,
      name: 'Jane Doe'
    });
  });
});
```

## Success Indicators

### Proficiency Levels

- **Beginner:** Can write basic unit tests with simple assertions
- **Intermediate:** Uses mocking effectively, writes parameterized tests, achieves good coverage
- **Advanced:** Designs testable code, implements TDD, mentors others on testing
- **Expert:** Establishes testing strategy, optimizes test suites, contributes to testing tools

### Quality Metrics

- Code coverage > 80% for critical paths
- Test execution time < 5 minutes for full suite
- Flaky test rate < 1%
- Bug detection rate in development > 90%
- Tests run on every commit in CI/CD

## Related Skills

- [Test Automation](test_automation.md) - Broader testing strategies
- [Code Review](../collaboration-skills/code_review.md) - Reviewing test quality
- [Debugging](../behavior-skills/debugging.md) - Investigating test failures

## Version Information

---
version: 1.0.0
last_updated: 2026-01-15
reviewed_by: Testing Skills Team
next_review: 2026-07-15
---
