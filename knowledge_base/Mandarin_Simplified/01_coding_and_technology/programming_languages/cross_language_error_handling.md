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
# 跨语言比较——错误处理
## 错误处理模型概述
|型号|语言 |机制|
|--------|---------|------------|
| **异常（尝试/捕获）** | Java、C++、C#、Python、Ruby、PHP、JavaScript、TypeScript、Kotlin、Swift、Dart、Scala、VB、Delphi | `try { } catch (e) { }`|
| **结果/选项类型** | Rust、Haskell、OCaml、Scala（也）|  `Result<T, E>`、`Maybe a` |
| **多个返回值** |走吧，卢阿 | `value, err := f()`|
| **错误代码** | C、Fortran |返回错误码，手动检查 |
| **模式匹配错误** | Elixir、Erlang | `{:ok, value}`/`{:error, reason}`|
| **条件（可重新启动）** |通用 Lisp |  `restart-case`、`handler-bind` |
| **无错误处理** | Scratch、SQL（基础）|不适用 |
| **合同** |艾达，埃菲尔 |  `Pre`、`Post` 条件 |
## 基于异常的错误处理
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

## 总结：错误处理范例
|范式|方法|优点 |缺点 |
|----------|----------|------|-----|
| **例外** |投掷/接住|干净的快乐路径，堆栈痕迹|可被遗忘、控制流滥用|
| **结果类型** |返回`Ok`/`Err`|显式的，不能忽略错误 |需要详细的`?`运算符 |
| **错误代码** |返回 int 状态 |简单，C 兼容 |容易被忽视，没有上下文|
| **多次回报** | `value, err := f()`|明确、惯用 |可以忘记检查`err` |
| **模式匹配** | `{:ok, v}`/`{:error, r}`|详尽、实用 |没有`with`的详细信息 |
| **条件** |可重新启动的处理程序 |最强大，可恢复|复杂，很少被理解 |