<!--
---
# Metadata
title: "Cross-Language Comparison — Error Handling"
description: "Side-by-side comparison of error handling patterns across 34 programming languages."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cross-language comparison"
tags: [error-handling, cross-language, comparison, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# 언어 간 비교 — 오류 처리
## 오류 처리 모델 개요
| 모델 | 언어 | 메커니즘 |
|-------|------------|------------|
| **예외(시도/캐치)** | Java, C++, C#, Python, Ruby, PHP, JavaScript, TypeScript, Kotlin, Swift, Dart, Scala, VB, Delphi | `try { } catch (e) { }`|
| **결과/옵션 유형** | Rust, Haskell, OCaml, Scala (또한) |  `Result<T, E>`,`Maybe a`|
| **여러 반환 값** | 가, 루아 | `value, err := f()`|
| **오류 코드** | C, 포트란 | 오류 코드 반환, 수동으로 확인 |
| **패턴 일치 오류** | 엘릭서, 얼랑 | `{:ok, value}`/`{:error, reason}`|
| **조건(재시작 가능)** | 커먼 리스프 | `restart-case`,`handler-bind`|
| **오류 처리 없음** | 스크래치, SQL(기본) | 해당 없음 |
| **계약** | 에이다, 에펠 | `Pre`,`Post`조건 |
## 예외 기반 오류 처리
```python
# Python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError):
    print("Type or value error")
else:
    print("No error")  # runs if no exception
finally:
    print("Always runs")

# Custom exception
class AppError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code
```

```java
// Java
try {
    int result = 10 / 0;
} catch (ArithmeticException e) {
    System.err.println("Error: " + e.getMessage());
} catch (Exception e) {
    System.err.println("General error");
} finally {
    System.out.println("Always runs");
}

// Custom exception
class AppException extends Exception {
    private int code;
    public AppException(String msg, int code) {
        super(msg);
        this.code = code;
    }
}
```

```javascript
// JavaScript
try {
    const result = riskyOperation();
} catch (error) {
    console.error("Error:", error.message);
} finally {
    cleanup();
}

// Custom error
class AppError extends Error {
    constructor(message, code) {
        super(message);
        this.code = code;
    }
}
throw new AppError("Something failed", 500);
```

```csharp
// C#
try {
    int result = 10 / 0;
} catch (DivideByZeroException ex) {
    Console.Error.WriteLine($"Error: {ex.Message}");
} catch (Exception ex) when (ex is not InvalidOperationException) {
    Console.Error.WriteLine("General error");
} finally {
    Cleanup();
}
```

```rust
// Rust: Result type (no exceptions)
fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err("Division by zero".to_string())
    } else {
        Ok(a / b)
    }
}

match divide(10.0, 0.0) {
    Ok(result) => println!("Result: {}", result),
    Err(e) => eprintln!("Error: {}", e),
}

// ? operator (propagate errors)
fn compute() -> Result<f64, String> {
    let a = divide(10.0, 2.0)?;
    let b = divide(a, 0.0)?;  // returns Err immediately
    Ok(b)
}
```

```go
// Go: multiple return values
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}

result, err := divide(10, 0)
if err != nil {
    log.Fatal(err)
}
fmt.Println(result)

// Custom error type
type AppError struct {
    Code    int
    Message string
}
func (e *AppError) Error() string { return e.Message }
```

```c
// C: error codes
#include <errno.h>
int divide(double a, double b, double *result) {
    if (b == 0.0) {
        errno = EDOM;
        return -1;  // error
    }
    *result = a / b;
    return 0;  // success
}

double result;
if (divide(10, 0, &result) != 0) {
    perror("Division error");
}
```

```haskell
-- Haskell: Maybe and Either
safeDivide :: Double -> Double -> Maybe Double
safeDivide _ 0 = Nothing
safeDivide a b = Just (a / b)

-- Either (with error info)
safeDivideE :: Double -> Double -> Either String Double
safeDivideE _ 0 = Left "Division by zero"
safeDivideE a b = Right (a / b)

-- Usage
case safeDivideE 10 0 of
    Right result -> print result
    Left err     -> putStrLn $ "Error: " ++ err
```

```elixir
# Elixir: {:ok, value} / {:error, reason}
case divide(10, 0) do
  {:ok, result}    -> IO.puts("Result: #{result}")
  {:error, reason} -> IO.puts("Error: #{reason}")
end

# Raising errors
def divide(a, 0), do: raise ArithmeticError, message: "division by zero"
def divide(a, b), do: a / b

# Rescue
try do
  divide(10, 0)
rescue
  e in ArithmeticError -> IO.puts("Error: #{e.message}")
end
```

```erlang
% Erlang: try/catch or {ok, Error}
case safe_divide(10, 0) of
    {ok, Result}    -> io:format("~p~n", [Result]);
    {error, Reason} -> io:format("Error: ~p~n", [Reason])
end

% try/catch
try
    10 / 0
catch
    error:badarith -> io:format("Division error~n");
    _:_ -> io:format("Unknown error~n")
end.
```

```swift
// Swift: throws/do-catch
enum AppError: Error {
    case divisionByZero
    case invalidInput(String)
}

func divide(_ a: Double, _ b: Double) throws -> Double {
    guard b != 0 else { throw AppError.divisionByZero }
    return a / b
}

do {
    let result = try divide(10, 0)
    print(result)
} catch AppError.divisionByZero {
    print("Cannot divide by zero")
} catch {
    print("Unexpected error: \(error)")
}
```

```kotlin
// Kotlin: try/catch
try {
    val result = 10 / 0
} catch (e: ArithmeticException) {
    println("Error: ${e.message}")
} catch (e: Exception) {
    println("General error")
} finally {
    println("Always runs")
}

// Kotlin: Result type
val result: Result<Int> = runCatching { 10 / 0 }
result.onSuccess { println(it) }
      .onFailure { println("Error: ${it.message}") }
```

```ruby
# Ruby: begin/rescue
begin
    result = 10 / 0
rescue ZeroDivisionError => e
    puts "Error: #{e.message}"
rescue StandardError => e
    puts "General error: #{e.message}"
else
    puts "No error"
ensure
    puts "Always runs"
end

# Custom exception
class AppError < StandardError
    attr_reader :code
    def initialize(message, code)
        super(message)
        @code = code
    end
end
```

```perl
# Perl: eval/die
eval {
    die "Something went wrong" if $error;
    # risky code
};
if ($@) {
    warn "Error: $@";
}

# Modern Perl: try/catch (5.34+)
use experimental 'try';
try {
    risky_operation();
}
catch ($e) {
    warn "Error: $e";
}
```

```ada
-- Ada: exception handling
begin
   Result := 10 / Divisor;
exception
   when Constraint_Error =>
      Put_Line("Division error");
   when others =>
      Put_Line("Unexpected error");
end;
```

```cobol
      * COBOL: error handling via status codes
       READ EMPLOYEE-FILE
           AT END
               MOVE 'YES' TO END-OF-FILE
           NOT AT END
               PERFORM PROCESS-RECORD
       END-READ

      * Modern COBOL: EXCEPTION handling
       TRY
           PERFORM RISKY-OPERATION
       CATCH EXCEPTION
           DISPLAY 'Error occurred'
       END-TRY
```

```prolog
% Prolog: throw/catch
:- catch(
     (X is 10 / 0),
     error(E, _),
     format('Error: ~w~n', [E])
   ).
```

```lisp
;; Common Lisp: condition system (restartable!)
(handler-case
    (/ 10 0)
  (division-by-zero (c)
    (format t "Error: ~a~%" c)))

;; Restartable conditions
(restart-case
    (error 'file-not-found :filename "data.txt")
  (use-alternate-file ()
    :report "Use alternate file"
    "backup.txt"))
```

```lua
-- Lua: pcall (protected call)
local ok, result = pcall(function()
    return risky_operation()
end)
if not ok then
    print("Error: " .. result)  -- result is the error message
end

-- Custom error
error("Something went wrong", 2)  -- level 2 = caller's line
```

## 요약: 오류 처리 패러다임
| 패러다임 | 접근 | 장점 | 단점 |
|----------|------------|------|------|
| **예외** | 던지기/잡기 | 행복한 경로 정리, 스택 추적 | 잊어버릴 수 있음, 제어 흐름 남용 |
| **결과 유형** |`Ok`/`Err`반환 | 명시적이며 오류를 무시할 수 없습니다 | 자세한 정보,`?`연산자 필요 |
| **오류 코드** | 정수 상태 반환 | 단순하고 C 호환 가능 | 무시하기 쉽고 맥락이 없음 |
| **복수 반품** | `value, err := f()`| 명시적, 관용적 | `err`를 확인하는 것을 잊을 수 있습니다 |
| **패턴 매칭** | `{:ok, v}`/`{:error, r}`| 철저하고 기능적 |`with`없이 장황하게 표시 |
| **조건** | 재시작 가능한 핸들러 | 가장 강력하고 복구 가능 | 복잡하고 거의 이해되지 않음 |