---
# Metadata
title: "Testing Methodologies"
description: "Unit, integration, E2E, TDD, BDD, test pyramids"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [testing, methodologies, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Testing Methodologies

Testing is how you gain confidence that your code works — and more importantly, that changes to it don't break what already works. Good testing catches bugs before users do, documents expected behaviour, and enables fearless refactoring. This file covers the full spectrum of testing strategies, from unit tests to end-to-end tests, and the principles that make testing effective.

---

## The Testing Pyramid

The testing pyramid describes the ideal distribution of tests in a project.

```
        /  E2E  \          ← Few; slow; expensive; test the whole system
       /─────────\
      / Integration\       ← Some; test how components work together
     /───────────────\
    /   Unit Tests    \    ← Many; fast; cheap; test individual functions
   /─────────────────────\
```

| Level | Count | Speed | Cost | What It Tests |
|-------|-------|-------|------|---------------|
| **Unit** | Many | Fast (ms) | Low | Individual functions, classes, methods |
| **Integration** | Some | Medium (100ms-s) | Medium | How components interact; database queries; API calls |
| **E2E** | Few | Slow (seconds-minutes) | High | Full user flows through the real system |

---

## Unit Testing

Testing individual units of code in isolation.

### Principles

| Principle | Description |
|-----------|-------------|
| **Fast** | Each test should run in milliseconds |
| **Isolated** | Tests don't depend on each other; no shared state |
| **Deterministic** | Same input → same output every time (no randomness, no time dependency) |
| **Self-checking** | Test passes or fails automatically; no manual inspection |
| **Timely** | Written alongside or before the code (TDD) |

### Anatomy of a Test

| Phase | Description |
|-------|-------------|
| **Arrange** | Set up the test data and dependencies |
| **Act** | Call the function or method being tested |
| **Assert** | Verify the result matches expectations |

### What to Test

| Category | Examples |
|----------|---------|
| **Happy path** | Normal inputs produce expected outputs |
| **Edge cases** | Empty input, null, zero, maximum values, single element |
| **Error cases** | Invalid input, missing data, permission denied |
| **Boundary conditions** | Off-by-one; exactly at limits |

### Mocking and Stubbing

| Term | Description | When to Use |
|------|-------------|-------------|
| **Mock** | A fake object that records how it was called | Verifying interactions (was this method called?) |
| **Stub** | A fake object that returns predetermined values | Providing test data (return this user from the database) |
| **Spy** | A wrapper that records calls to a real object | Partial verification |
| **Fake** | A simplified but working implementation | In-memory database for tests |

| Mocking Library | Language |
|----------------|--------|
| **unittest.mock** | Python |
| **Jest** | JavaScript/TypeScript |
| **Mockito** | Java |
| **Moq** | C# |
| **testify / gomock** | Go |

---

## Integration Testing

Testing how multiple components work together.

| What to Test | Example |
|-------------|---------|
| **Database queries** | Does the ORM produce correct SQL? Are indexes used? |
| **API endpoints** | Does the full request-response cycle work? |
| **Service interactions** | Does service A correctly call service B? |
| **External dependencies** | Does the payment gateway integration work? |

### Strategies

| Strategy | Description | Trade-off |
|----------|-------------|-----------|
| **Real dependencies** | Use a real database, real message queue | Most realistic; slower; harder to set up |
| **Test containers** | Spin up Docker containers for each test run | Good balance; reproducible |
| **In-memory alternatives** | H2 instead of PostgreSQL; in-memory message bus | Fast; may miss real-world issues |
| **Contract testing** | Verify that services honour their API contracts | Catches interface changes |

---

## End-to-End (E2E) Testing

Testing the complete system from the user's perspective.

| Tool | Type | Best For |
|------|------|----------|
| **Playwright** | Browser automation | Web applications; cross-browser |
| **Cypress** | Browser automation | Web applications; developer experience |
| **Selenium** | Browser automation | Legacy; wide language support |
| **Detox** | Mobile E2E | React Native apps |
| **Appium** | Mobile E2E | Native and hybrid mobile apps |
| **Maestro** | Mobile E2E | Mobile apps; simple YAML syntax |
| **k6 / Locust** | Load testing | Performance under load |

### E2E Best Practices

| Practice | Why |
|----------|-----|
| **Test critical paths only** | E2E tests are slow; focus on what matters most |
| **Use test data factories** | Create test data programmatically; don't rely on seed data |
| **Clean up after tests** | Each test should leave the system in a known state |
| **Avoid testing UI details** | Test behaviour, not CSS classes or element positions |
| **Run in CI** | E2E tests must run automatically on every change |

---

## Test-Driven Development (TDD)

Write the test first, then write the code to make it pass.

| Step | Description |
|------|-------------|
| **1. Red** | Write a failing test that describes the desired behaviour |
| **2. Green** | Write the minimum code to make the test pass |
| **3. Refactor** | Clean up the code while keeping tests green |

| Benefit | Description |
|---------|-------------|
| **Design feedback** | Tests force you to think about interfaces before implementation |
| **Regression safety** | Every bug gets a test; the bug can never return |
| **Documentation** | Tests serve as living documentation of expected behaviour |
| **Confidence** | High test coverage enables fearless refactoring |

---

## Behaviour-Driven Development (BDD)

BDD extends TDD by writing tests in natural language that describe behaviour from the user's perspective.

### Given-When-Then Format

```
Given a user with an empty shopping cart
When they add a "Python Book" priced at $29.99
Then the cart total should be $29.99
And the cart should contain 1 item
```

| Tool | Language |
|------|----------|
| **Cucumber** | Java, JavaScript, Ruby, and others |
| **Behave** | Python |
| **SpecFlow** | C# |
| **Jest** (with describe/it) | JavaScript |

---

## Other Testing Types

| Type | What It Tests | Tools |
|------|--------------|-------|
| **Performance/Load** | System behaviour under load | k6, JMeter, Locust, Gatling |
| **Security** | Vulnerabilities and attack vectors | OWASP ZAP, Burp Suite, Snyk |
| **Accessibility** | WCAG compliance | axe, Lighthouse, pa11y |
| **Contract** | API compatibility between services | Pact, Spring Cloud Contract |
| **Mutation** | Quality of the test suite itself | Stryker, mutmut, PIT |
| **Visual regression** | UI changes between versions | Percy, Chromatic, BackstopJS |
| **Chaos** | System resilience to failures | Chaos Monkey, Litmus, Gremlin |
| **Smoke** | Basic functionality after deployment | Custom scripts; health checks |
| **Soak** | System behaviour over extended time | Long-running load tests |

---

## Test Organisation

| Pattern | Description | When to Use |
|---------|-------------|-------------|
| **Co-located** | Tests next to the code they test (`src/utils.test.ts`) | Most projects; easy to find |
| **Separate directory** | Tests in a `tests/` or `__tests__/` folder | Large projects; clear separation |
| **Test fixtures** | Shared test data in a `fixtures/` directory | When multiple tests need the same data |
| **Test utilities** | Shared helpers in a `test-utils/` directory | When setup logic is complex |

---

## Code Coverage

| Metric | What It Measures | Limitation |
|--------|-----------------|------------|
| **Line coverage** | Percentage of code lines executed by tests | Doesn't measure quality of assertions |
| **Branch coverage** | Percentage of branches (if/else) taken | Better than line coverage; still doesn't catch all bugs |
| **Path coverage** | Percentage of execution paths taken | Most thorough; exponential in complex code |
| **Mutation score** | Percentage of mutations caught by tests | Best measure of test quality |

**Target**: 80% line coverage is a reasonable default. But coverage is a guide, not a goal — 100% coverage with weak assertions is worse than 70% coverage with thorough tests.

---

## Continuous Integration and Testing

| Practice | Description |
|----------|-------------|
| **Run all unit tests on every commit** | Fast feedback; catches regressions immediately |
| **Run integration tests on PR** | Catches issues that unit tests miss |
| **Run E2E tests nightly or on merge to main** | Slow but thorough |
| **Fail fast** | Stop the pipeline on first failure to save time |
| **Flaky test policy** | Quarantine or delete flaky tests immediately; never ignore |
| **Test parallelisation** | Run tests in parallel to reduce CI time |

---

## Practical Tips

- **Name tests clearly.** `test_calculates_tax_for_high_earner` tells you what broke. `test_1` tells you nothing.
- **One assertion per test (when practical).** Makes failures easy to diagnose.
- **Don't test implementation details.** Test behaviour. If you refactor internals, tests shouldn't break.
- **Avoid testing third-party code.** Mock external libraries; test your code's interaction with them.
- **Make tests fast.** If your test suite takes 10 minutes, developers will stop running it. Optimise relentlessly.
- **Delete dead tests.** Tests that always pass or test removed code are noise.
- **Treat test code like production code.** It should be readable, maintainable, and well-structured.

---

## Summary

Testing is not optional — it's how you build software that doesn't break. The testing pyramid guides you toward many fast unit tests, some integration tests, and a few E2E tests. TDD and BDD provide structured approaches. Mocking isolates units for testing. Code coverage measures breadth but not depth. The most important principle is this: if it isn't tested, it's broken — you just don't know it yet.
