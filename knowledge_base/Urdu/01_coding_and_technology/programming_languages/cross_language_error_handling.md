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
# کراس لینگویج کمپاریزن — ایرر ہینڈلنگ
## ماڈلز کا جائزہ لینے میں خرابی
| ماڈل | زبانیں | میکانزم |
|---------|------------|------------|
| **استثنیات (کوشش/پکڑنے)** | Java, C++, C#, Python, Ruby, PHP, JavaScript, TypeScript, Kotlin, Swift, Dart, Scala, VB, Delphi | `try { } catch (e) { }`|
| **نتائج/اختیار کی اقسام** | زنگ، ہاسکل، OCaml، Scala (بھی) | `Result<T, E>`,`Maybe a`|
| **ایک سے زیادہ واپسی اقدار** | جاؤ، لوا | `value, err := f()`|
| **خرابی کوڈز** | سی، فورٹران | غلطی کا کوڈ واپس کریں، دستی طور پر چیک کریں |
| **پیٹرن مماثل غلطیاں** | ایلیکسیر، ایرلنگ | `{:ok, value}`/`{:error, reason}`|
| **حالات (دوبارہ شروع کرنے کے قابل)** | کامن لِسپ | `restart-case`,`handler-bind`|
| **کوئی غلطی ہینڈلنگ نہیں** | سکریچ، SQL (بنیادی) | N/A |
| **معاہدے** | اڈا، ایفل | `Pre`,`Post`شرائط |
## استثنیٰ پر مبنی خرابی کو ہینڈل کرنا
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

## خلاصہ: پیراڈیمز کو سنبھالنے میں خرابی۔
| تمثیل | نقطہ نظر | پیشہ | Cons |
|------------|---------|------|------|
| **استثنیات** | پھینک / پکڑ | صاف ستھرا راستہ، اسٹیک نشانات | بھول جا سکتا ہے، کنٹرول بہاؤ غلط استعمال |
| **نتائج کی اقسام** | واپسی`Ok`/`Err`| واضح، غلطیوں کو نظر انداز نہیں کیا جا سکتا | Verbose,`?`آپریٹر کی ضرورت ہے |
| **خرابی کوڈز** | int اسٹیٹس واپس کریں | سادہ، سی مطابقت پذیر | نظر انداز کرنا آسان، کوئی سیاق و سباق نہیں |
| **متعدد واپسی** | `value, err := f()`| واضح، محاوراتی |`err`چیک کرنا بھول سکتے ہیں |
| **پیٹرن میچنگ** | `{:ok, v}`/`{:error, r}`| مکمل، فعال |`with`کے بغیر فعل |
| **شرائط** | دوبارہ شروع کرنے کے قابل ہینڈلرز | سب سے زیادہ طاقتور، قابل بازیافت | پیچیدہ، شاذ و نادر ہی سمجھا جاتا ہے |