---
# Metadata
title: "Cross-Language Comparison — Control Flow"
description: "Side-by-side comparison of control flow constructs across 34 programming languages."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cross-language comparison"
tags: [control-flow, cross-language, comparison, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# مقایسه بین زبانی - جریان کنترل
## اظهارات If/Else
```python
# Python
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")
```

```javascript
// JavaScript
if (x > 0) {
    console.log("positive");
} else if (x === 0) {
    console.log("zero");
} else {
    console.log("negative");
}
```

```rust
// Rust
if x > 0 {
    println!("positive");
} else if x == 0 {
    println!("zero");
} else {
    println!("negative");
}
```

```go
// Go
if x > 0 {
    fmt.Println("positive")
} else if x == 0 {
    fmt.Println("zero")
} else {
    fmt.Println("negative")
}
```

```java
// Java
if (x > 0) {
    System.out.println("positive");
} else if (x == 0) {
    System.out.println("zero");
} else {
    System.out.println("negative");
}
```

```c
// C
if (x > 0) {
    printf("positive\n");
} else if (x == 0) {
    printf("zero\n");
} else {
    printf("negative\n");
}
```

```ruby
# Ruby
if x > 0
  puts "positive"
elsif x == 0
  puts "zero"
else
  puts "negative"
end
```

```haskell
-- Haskell
result | x > 0     = "positive"
       | x == 0    = "zero"
       | otherwise = "negative"
```

```swift
// Swift
if x > 0 {
    print("positive")
} else if x == 0 {
    print("zero")
} else {
    print("negative")
}
```

```kotlin
// Kotlin
when {
    x > 0 -> println("positive")
    x == 0 -> println("zero")
    else -> println("negative")
}
```

```perl
# Perl
if ($x > 0) {
    say "positive";
} elsif ($x == 0) {
    say "zero";
} else {
    say "negative";
}
```

```r
# R
if (x > 0) {
    cat("positive\n")
} else if (x == 0) {
    cat("zero\n")
} else {
    cat("negative\n")
}
```

```sql
-- SQL (CASE expression)
SELECT CASE
    WHEN x > 0 THEN 'positive'
    WHEN x = 0 THEN 'zero'
    ELSE 'negative'
END;
```

```bash
# Bash
if [ "$x" -gt 0 ]; then
    echo "positive"
elif [ "$x" -eq 0 ]; then
    echo "zero"
else
    echo "negative"
fi
```

```prolog
% Prolog
classify(X, positive) :- X > 0.
classify(0, zero).
classify(X, negative) :- X < 0.
```

```lisp
;; Lisp/Clojure
(if (> x 0)
  "positive"
  (if (= x 0)
    "zero"
    "negative"))

;; Clojure cond
(cond
  (> x 0) "positive"
  (= x 0) "zero"
  :else   "negative")
```

```ada
-- Ada
if X > 0 then
   Put_Line("positive");
elsif X = 0 then
   Put_Line("zero");
else
   Put_Line("negative");
end if;
```

```cobol
      * COBOL
       EVALUATE TRUE
           WHEN X > 0
               DISPLAY 'positive'
           WHEN X = 0
               DISPLAY 'zero'
           WHEN OTHER
               DISPLAY 'negative'
       END-EVALUATE
```

```erlang
% Erlang
case X > 0 of
    true  -> io:format("positive~n");
    false -> case X =:= 0 of
        true  -> io:format("zero~n");
        false -> io:format("negative~n")
    end
end.
```

```ocaml
(* OCaml *)
if x > 0 then print_endline "positive"
else if x = 0 then print_endline "zero"
else print_endline "negative"
```

```matlab
% MATLAB
if x > 0
    disp('positive')
elseif x == 0
    disp('zero')
else
    disp('negative')
end
```

```lua
-- Lua
if x > 0 then
    print("positive")
elseif x == 0 then
    print("zero")
else
    print("negative")
end
```

```assembly
; x86 Assembly (NASM)
    cmp eax, 0
    jg positive
    je zero
    ; negative
    jmp done
positive:
    ; print "positive"
    jmp done
zero:
    ; print "zero"
done:
```

```delphi
// Delphi/Object Pascal
if X > 0 then
  WriteLn('positive')
else if X = 0 then
  WriteLn('zero')
else
  WriteLn('negative');
```

```vb
' Visual Basic
If x > 0 Then
    Console.WriteLine("positive")
ElseIf x = 0 Then
    Console.WriteLine("zero")
Else
    Console.WriteLine("negative")
End If
```

```scala
// Scala
if (x > 0) println("positive")
else if (x == 0) println("zero")
else println("negative")

// Scala match
val result = x match {
  case n if n > 0 => "positive"
  case 0          => "zero"
  case _          => "negative"
}
```

```dart
// Dart
if (x > 0) {
  print('positive');
} else if (x == 0) {
  print('zero');
} else {
  print('negative');
}
```

```julia
# Julia
if x > 0
    println("positive")
elseif x == 0
    println("zero")
else
    println("negative")
end
```

```typescript
// TypeScript
if (x > 0) {
    console.log("positive");
} else if (x === 0) {
    console.log("zero");
} else {
    console.log("negative");
}
```

```csharp
// C#
if (x > 0) {
    Console.WriteLine("positive");
} else if (x == 0) {
    Console.WriteLine("zero");
} else {
    Console.WriteLine("negative");
}

// C# 8+ switch expression
var result = x switch {
    > 0 => "positive",
    0   => "zero",
    _   => "negative"
};
```

```php
<?php
// PHP
if ($x > 0) {
    echo "positive";
} elseif ($x == 0) {
    echo "zero";
} else {
    echo "negative";
}

// PHP 8+ match
$result = match(true) {
    $x > 0 => 'positive',
    $x == 0 => 'zero',
    default => 'negative',
};
```

```fortran
! Fortran
if (x > 0) then
    print *, 'positive'
else if (x == 0) then
    print *, 'zero'
else
    print *, 'negative'
end if
```

```scratch
// Scratch (blocks)
if <(x) > (0)> then
    say [positive]
else
    if <(x) = (0)> then
        say [zero]
    else
        say [negative]
    end
end
```

## برای حلقه ها
| زبان | نحو |
|----------|--------|
| پایتون | `for i in range(10):`|
| جاوا اسکریپت | `for (let i = 0; i < 10; i++)`|
| زنگ زدگی | `for i in 0..10`|
| برو | `for i := 0; i < 10; i++`|
| جاوا | `for (int i = 0; i < 10; i++)`|
| C/C++ | `for (int i = 0; i < 10; i++)`|
| یاقوت | `10.times { \|i\| ... }`یا`(0..9).each { \|i\| ... }`|
| سویفت | `for i in 0..<10`|
| کاتلین | `for (i in 0 until 10)`|
| هاسکل | `mapM_ f [0..9]`|
| پرل | `for my $i (0..9)`|
| R | `for (i in 1:10)`|
| پی اچ پی | `for ($i = 0; $i < 10; $i++)`|
| SQL | N/A (مبتنی بر مجموعه، بدون حلقه در SQL استاندارد) |
| باش | `for i in {0..9}; do ... done`|
| لوا | `for i = 0, 9 do ... end`|
| متلب | `for i = 1:10 ... end`|
| پرولوگ | N/A (به جای بازگشت) |
| لیسپ | `(dotimes (i 10) ...)`|
| آدا | `for I in 0..9 loop ... end loop;`|
| COBOL | `PERFORM VARYING I FROM 0 BY 1 UNTIL I >= 10`|
| ارلنگ | N/A (بازگشت + لیست به جای آن) |
| OCaml | `for i = 0 to 9 do ... done`|
| مونتاژ | حلقه دستی با CMP/JMP |
| دلفی | `for I := 0 to 9 do ... end;`|
| خراش | `repeat (10) ... end`|
| VB | `For i As Integer = 0 To 9 ... Next`|
| اسکالا | `for (i <- 0 until 10) ...`|
| دارت | `for (var i = 0; i < 10; i++)`|
| جولیا | `for i in 0:9 ... end`|
| TypeScript | `for (let i = 0; i < 10; i++)`|
| سی شارپ | `for (int i = 0; i < 10; i++)`|
| فرترن | `do i = 1, 10 ... end do`|
## تطبیق الگو / سوئیچ
| زبان | ساخت |
|----------|-----------|
| ج | `switch (x) { case 1: ... break; }`|
| جاوا | `switch (x) { case 1 -> ... }`(جاوا 14+) |
| زنگ زدگی | `match x { 1 => ..., _ => ... }`|
| هاسکل | `case x of 1 -> ...; _ -> ...`|
| اسکالا | `x match { case 1 => ... }`|
| سویفت | `switch x { case 1: ... default: ... }`|
| کاتلین | `when (x) { 1 -> ... else -> ... }`|
| OCaml | `match x with 1 -> ... \| _ -> ...`|
| ارلنگ | `case X of 1 -> ...; _ -> ... end`|
| اکسیر | `case x do 1 -> ...; _ -> ... end`|
| دارت | `switch (x) { 1 => ...; _ => ... }`(دارت 3.0) |
| پی اچ پی | `match($x) { 1 => ..., default => ... }`(PHP 8.0) |
| سی شارپ | `x switch { 1 => ..., _ => ... }`(C# 8+) |
| TypeScript | بدون تطبیق الگوی بومی (استفاده از if/else) |
| پایتون | `match x: case 1: ... case _: ...`(Python 3.10+) |
| پرولوگ | تعبیه شده در مطابقت بند |
| برو | `switch x { case 1: ... default: ... }`|