# Test Automation

## Overview

Test automation is the practice of using software tools to execute pre-scripted tests on a software application before releasing it into production. Automated testing increases testing efficiency, coverage, and reliability while reducing manual effort and human error.

This skill covers strategies, frameworks, and best practices for implementing effective test automation across different testing levels.

## Core Competencies

- **Test Strategy Design**: Planning what to automate and when
- **Framework Selection**: Choosing appropriate testing frameworks
- **Test Pyramid Implementation**: Balancing unit, integration, and E2E tests
- **CI/CD Integration**: Automating test execution in pipelines
- **Test Data Management**: Creating and maintaining test data
- **Flaky Test Prevention**: Writing reliable, deterministic tests
- **Test Reporting & Analysis**: Interpreting and acting on test results
- **Maintenance Strategies**: Keeping tests up-to-date with code changes

## When to Use

Test automation is valuable when:
- ✅ Running repetitive tests across multiple environments
- ✅ Performing regression testing after code changes
- ✅ Executing load or performance tests
- ✅ Validating critical user journeys frequently
- ✅ Testing across multiple browsers or devices
- ✅ Needing fast feedback on code quality

**Not ideal for:**
- ❌ One-time tests that won't be re-run
- ❌ Exploratory testing requiring human intuition
- ❌ Usability testing requiring subjective judgment
- ❌ Tests where requirements change constantly

## The Test Automation Pyramid

```
                    /\
                   /  \
                  / E2E \        ← Few tests, slow, expensive
                 /--------\
                /          \
               /Integration \    ← Moderate number, medium speed
              /--------------\
             /                \
            /     Unit Tests    \   ← Many tests, fast, cheap
           /--------------------\
```

### Pyramid Levels

| Level | Purpose | Speed | Cost | Quantity |
|-------|---------|-------|------|----------|
| **Unit** | Test individual functions/methods | Fastest | Lowest | Most (70%) |
| **Integration** | Test component interactions | Medium | Medium | Moderate (20%) |
| **E2E** | Test complete user workflows | Slowest | Highest | Fewest (10%) |

## Framework Selection Guide

### By Testing Level

#### Unit Testing Frameworks

| Language | Framework | Best For |
|----------|-----------|----------|
| JavaScript/TypeScript | Jest, Vitest | Frontend, Node.js |
| Python | pytest, unittest | Backend, data science |
| Java | JUnit, TestNG | Enterprise applications |
| C# | xUnit, NUnit, MSTest | .NET applications |
| Ruby | RSpec, Minitest | Rails applications |
| Go | testing (built-in) | Go services |

#### Integration Testing Tools

| Tool | Type | Use Case |
|------|------|----------|
| Supertest | HTTP assertion | API testing |
| TestContainers | Container orchestration | Database, service integration |
| WireMock | Service mocking | External service simulation |
| Mountebank | Service virtualization | Complex dependency mocking |

#### E2E Testing Frameworks

| Tool | Language | Strengths |
|------|----------|-----------|
| Cypress | JavaScript | Developer experience, debugging |
| Playwright | Multi-language | Cross-browser, mobile |
| Selenium | Multi-language | Browser coverage, mature |
| Puppeteer | JavaScript | Chrome automation, scraping |
| Detox | JavaScript | Mobile app testing |

## Practical Templates

### Test File Structure Template

```javascript
// describe block for the feature/module
describe('FeatureName', () => {
  
  // Setup before all tests in this suite
  beforeAll(() => {
    // Global setup
  });

  // Setup before each test
  beforeEach(() => {
    // Test isolation setup
  });

  // Cleanup after each test
  afterEach(() => {
    // Clean up test state
  });

  // Cleanup after all tests
  afterAll(() => {
    // Global teardown
  });

  // Individual test cases
  describe('specificFunction', () => {
    it('should [expected behavior] when [condition]', async () => {
      // Arrange
      const input = ...;
      const expected = ...;

      // Act
      const result = await functionUnderTest(input);

      // Assert
      expect(result).toBe(expected);
    });

    it('should handle edge case: [description]', () => {
      // Test edge cases
    });

    it('should throw error when [invalid condition]', () => {
      // Test error handling
      expect(() => functionUnderTest(invalidInput)).toThrow();
    });
  });
});
```

### Page Object Model Template (E2E)

```javascript
// pages/LoginPage.js
class LoginPage {
  constructor(page) {
    this.page = page;
    this.usernameInput = page.locator('#username');
    this.passwordInput = page.locator('#password');
    this.submitButton = page.locator('button[type="submit"]');
    this.errorMessage = page.locator('.error-message');
  }

  async goto() {
    await this.page.goto('/login');
  }

  async login(username, password) {
    await this.usernameInput.fill(username);
    await this.passwordInput.fill(password);
    await this.submitButton.click();
  }

  async getErrorMessage() {
    return await this.errorMessage.textContent();
  }

  async isLoggedIn() {
    const url = this.page.url();
    return url.includes('/dashboard');
  }
}

module.exports = { LoginPage };

// tests/login.spec.js
const { test, expect } = require('@playwright/test');
const { LoginPage } = require('../pages/LoginPage');

test.describe('Login Flow', () => {
  let loginPage;

  test.beforeEach(async ({ page }) => {
    loginPage = new LoginPage(page);
    await loginPage.goto();
  });

  test('successful login redirects to dashboard', async () => {
    await loginPage.login('validUser', 'validPassword');
    await expect(loginPage.isLoggedIn()).resolves.toBe(true);
  });

  test('invalid credentials shows error message', async () => {
    await loginPage.login('invalidUser', 'wrongPassword');
    await expect(loginPage.getErrorMessage()).resolves.toContain('Invalid credentials');
  });
});
```

### Test Data Factory Template

```javascript
// factories/userFactory.js
const { faker } = require('@faker-js/faker');

class UserFactory {
  static create(overrides = {}) {
    return {
      id: faker.string.uuid(),
      email: faker.internet.email(),
      username: faker.internet.userName(),
      password: faker.internet.password({ length: 12 }),
      firstName: faker.person.firstName(),
      lastName: faker.person.lastName(),
      role: 'user',
      createdAt: new Date(),
      ...overrides
    };
  }

  static admin(overrides = {}) {
    return this.create({
      role: 'admin',
      permissions: ['read', 'write', 'delete'],
      ...overrides
    });
  }

  static guest(overrides = {}) {
    return this.create({
      role: 'guest',
      permissions: ['read'],
      ...overrides
    });
  }
}

module.exports = { UserFactory };

// Usage in tests
const user = UserFactory.create({ email: 'test@example.com' });
const admin = UserFactory.admin();
```

### CI/CD Pipeline Test Configuration

```yaml
# .github/workflows/test.yml
name: Test Suite

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        node-version: [18, 20, 22]
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run unit tests with coverage
        run: npm run test:unit -- --coverage
      
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v4
        with:
          file: ./coverage/lcov.info

  integration-tests:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: test_db
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run database migrations
        run: npm run db:migrate:test
      
      - name: Run integration tests
        run: npm run test:integration
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/test_db

  e2e-tests:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Install Playwright browsers
        run: npx playwright install --with-deps
      
      - name: Build application
        run: npm run build
      
      - name: Start application
        run: npm run start &
      
      - name: Wait for application
        run: npx wait-on http://localhost:3000
      
      - name: Run E2E tests
        run: npm run test:e2e
      
      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: playwright-report
          path: playwright-report/
```

## Common Pitfalls

### 🚫 Anti-Patterns to Avoid

1. **Testing Implementation Instead of Behavior**
   ```javascript
   // ❌ Bad: Testing internal implementation
   expect(component.state.isOpen).toBe(true);
   
   // ✅ Good: Testing observable behavior
   expect(screen.getByRole('menu')).toBeVisible();
   ```

2. **Over-Mocking Dependencies**
   ```javascript
   // ❌ Bad: Mocking everything
   jest.mock('../services/api');
   jest.mock('../utils/helpers');
   jest.mock('../constants');
   
   // ✅ Good: Mock only external dependencies
   jest.mock('../services/api');
   ```

3. **Interdependent Tests**
   ```javascript
   // ❌ Bad: Tests depend on execution order
   test('first test creates user', () => { /* ... */ });
   test('second test uses created user', () => { /* ... */ });
   
   // ✅ Good: Each test is independent
   test('creates user successfully', () => {
     const user = createUser();
     expect(user.id).toBeDefined();
   });
   ```

4. **Flaky Tests with Timing Issues**
   ```javascript
   // ❌ Bad: Using arbitrary waits
   await page.waitForTimeout(5000);
   
   // ✅ Good: Waiting for specific conditions
   await expect(page.locator('.loaded')).toBeVisible();
   ```

5. **Hard-Coded Test Data**
   ```javascript
   // ❌ Bad: Hard-coded values
   const user = { email: 'test@test.com', name: 'Test User' };
   
   // ✅ Good: Generated unique data
   const user = { 
     email: `user_${Date.now()}@test.com`,
     name: faker.person.fullName()
   };
   ```

6. **Too Many Assertions Per Test**
   ```javascript
   // ❌ Bad: Testing everything in one test
   it('handles user registration', () => {
     // 20+ assertions...
   });
   
   // ✅ Good: Focused tests
   it('creates user record', () => { /* ... */ });
   it('sends welcome email', () => { /* ... */ });
   it('returns user data', () => { /* ... */ });
   ```

## Best Practices

### ✅ Recommended Approaches

1. **Follow the Test Pyramid**
   - Write more unit tests than integration tests
   - Write more integration tests than E2E tests
   - Keep E2E tests focused on critical paths only

2. **Use Descriptive Test Names**
   ```javascript
   // Clear intention
   it('returns 404 when user not found', () => { /* ... */ });
   it('increments login attempt counter on failed login', () => { /* ... */ });
   ```

3. **Arrange-Act-Assert Pattern**
   ```javascript
   it('calculates total price correctly', () => {
     // Arrange
     const cart = new Cart();
     cart.addItem({ price: 10, quantity: 2 });
     cart.addItem({ price: 5, quantity: 3 });
     
     // Act
     const total = cart.calculateTotal();
     
     // Assert
     expect(total).toBe(35);
   });
   ```

4. **Test Edge Cases Explicitly**
   - Empty inputs
   - Null/undefined values
   - Maximum boundary values
   - Special characters
   - Concurrent operations

5. **Keep Tests Fast**
   - Mock external services
   - Use in-memory databases for unit tests
   - Parallelize test execution
   - Avoid unnecessary setup/teardown

6. **Make Tests Deterministic**
   - Seed random number generators
   - Freeze time for date-dependent tests
   - Isolate test environments
   - Clean up after each test

7. **Version Control Test Data**
   - Store fixtures in version control
   - Document data dependencies
   - Use factories for dynamic data

8. **Monitor Test Health**
   - Track flaky test rate
   - Monitor test execution time trends
   - Review test coverage regularly
   - Remove obsolete tests

## Tools & Resources

### Testing Frameworks

| Category | Tools |
|----------|-------|
| **Unit Testing** | Jest, Vitest, pytest, JUnit, xUnit, RSpec |
| **Integration** | Supertest, TestContainers, WireMock |
| **E2E** | Playwright, Cypress, Selenium, Puppeteer |
| **Performance** | k6, Artillery, JMeter, Locust |
| **Visual Regression** | Percy, Chromatic, Loki |
| **API Testing** | Postman, Insomnia, REST Assured |

### Supporting Tools

| Purpose | Tools |
|---------|-------|
| **Coverage** | Istanbul/nyc, Coverage.py, JaCoCo |
| **Mocking** | Sinon, MSW, Mockito, unittest.mock |
| **Assertions** | Chai, AssertJ, Hamcrest |
| **Test Data** | Faker, FactoryBot, Fixtures |
| **CI/CD** | GitHub Actions, GitLab CI, Jenkins, CircleCI |
| **Reporting** | Allure, ReportPortal, Mochawesome |

### Learning Resources

- 📚 ["Testing JavaScript" by Kent C. Dodds](https://testingjavascript.com/)
- 📚 ["The Art of Unit Testing" by Roy Osherove](https://www.manning.com/books/the-art-of-unit-testing-third-edition)
- 📚 ["Growing Object-Oriented Software, Guided by Tests"](https://www.gooseo.com/)
- 🎥 [Google Testing on the Toilet](https://testing.googleblog.com/)
- 📖 [Martin Fowler's Testing Blog](https://martinfowler.com/tags/testing.html)
- 🏛️ [Microsoft Testing Principles](https://docs.microsoft.com/en-us/dotnet/core/testing/)

## Examples

### Example 1: Testing a React Component

```javascript
// Button.test.jsx
import { render, screen, fireEvent } from '@testing-library/react';
import { Button } from './Button';

describe('Button', () => {
  it('renders with correct text', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByRole('button', { name: 'Click me' })).toBeInTheDocument();
  });

  it('calls onClick handler when clicked', () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>Click me</Button>);
    
    fireEvent.click(screen.getByRole('button'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('is disabled when disabled prop is true', () => {
    render(<Button disabled>Click me</Button>);
    expect(screen.getByRole('button')).toBeDisabled();
  });

  it('shows loading state when loading prop is true', () => {
    render(<Button loading>Submit</Button>);
    expect(screen.getByRole('button')).toHaveTextContent('Loading...');
    expect(screen.getByRole('button')).toBeDisabled();
  });
});
```

### Example 2: Testing an API Endpoint

```javascript
// users.api.test.js
const request = require('supertest');
const app = require('../app');
const { UserFactory } = require('./factories/userFactory');

describe('POST /api/users', () => {
  it('creates a new user with valid data', async () => {
    const userData = UserFactory.create();
    
    const response = await request(app)
      .post('/api/users')
      .send(userData)
      .expect(201);
    
    expect(response.body).toMatchObject({
      id: expect.any(String),
      email: userData.email,
      username: userData.username,
      createdAt: expect.any(String)
    });
  });

  it('returns 400 for invalid email', async () => {
    const userData = UserFactory.create({ email: 'invalid-email' });
    
    const response = await request(app)
      .post('/api/users')
      .send(userData)
      .expect(400);
    
    expect(response.body.errors).toContainEqual(
      expect.objectContaining({ field: 'email' })
    );
  });

  it('returns 409 for duplicate email', async () => {
    const userData = UserFactory.create();
    
    // Create first user
    await request(app).post('/api/users').send(userData);
    
    // Try to create duplicate
    const response = await request(app)
      .post('/api/users')
      .send(userData)
      .expect(409);
    
    expect(response.body.message).toContain('already exists');
  });
});
```

### Example 3: E2E Test for Checkout Flow

```javascript
// checkout.spec.js
const { test, expect } = require('@playwright/test');

test.describe('Checkout Flow', () => {
  test('completes purchase successfully', async ({ page }) => {
    // Navigate to product page
    await page.goto('/products/laptop-pro');
    
    // Add to cart
    await page.click('[data-testid="add-to-cart"]');
    await expect(page.locator('[data-testid="cart-count"]'))
      .toHaveText('1');
    
    // Proceed to checkout
    await page.click('[data-testid="checkout-button"]');
    
    // Fill shipping information
    await page.fill('#shipping-name', 'John Doe');
    await page.fill('#shipping-address', '123 Main St');
    await page.fill('#shipping-city', 'San Francisco');
    await page.selectOption('#shipping-state', 'CA');
    await page.fill('#shipping-zip', '94102');
    
    // Enter payment details
    await page.fill('#card-number', '4242424242424242');
    await page.fill('#card-expiry', '12/25');
    await page.fill('#card-cvc', '123');
    
    // Place order
    await page.click('[data-testid="place-order"]');
    
    // Verify order confirmation
    await expect(page).toHaveURL(/\/order-confirmation/);
    await expect(page.locator('[data-testid="order-success"]'))
      .toBeVisible();
    await expect(page.locator('[data-testid="order-number"]'))
      .toHaveText(/ORD-\d+/);
  });
});
```

## Success Indicators

You've mastered test automation when you can:

- ✅ Design a test strategy aligned with project needs
- ✅ Select appropriate frameworks for different testing levels
- ✅ Write tests that are fast, reliable, and maintainable
- ✅ Achieve meaningful code coverage (>80% for critical paths)
- ✅ Keep flaky test rate below 1%
- ✅ Integrate tests seamlessly into CI/CD pipelines
- ✅ Reduce bug escape rate to production
- ✅ Enable confident refactoring through comprehensive test coverage
- ✅ Mentor others on testing best practices
- ✅ Balance test coverage with development velocity

## Related Skills

- [[Code Review]](../collaboration-skills/code_review.md) - Reviewing test quality
- [[Debugging]](../behavior-skills/debugging.md) - Investigating test failures
- [[Planning]](../behavior-skills/planning.md) - Planning test coverage
- [[System Architecture]](../designing-skills/system_architecture.md) - Designing testable systems

---

*Version: 1.0.0 | Last Updated: 2024 | Next Review: Q2 2025*
