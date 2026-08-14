<!--
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

-->
# المقارنة بين اللغات - التحكم في التدفق
## عبارات إذا/آخر
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

## للحلقات
| اللغة | بناء الجملة |
|----------|--------|
| بايثون | `for i in range(10):`|
| جافا سكريبت | `for (let i = 0; i < 10; i++)`|
| الصدأ | `for i in 0..10`|
| اذهب | `for i := 0; i < 10; i++`|
| جافا | `for (int i = 0; i < 10; i++)`|
| سي/سي++ | `for (int i = 0; i < 10; i++)`|
| روبي | `10.times { \|i\| ... }`أو`(0..9).each { \|i\| ... }`|
| سويفت | `for i in 0..<10`|
| كوتلين | `for (i in 0 until 10)`|
| هاسكل | `mapM_ f [0..9]`|
| بيرل | `for my $i (0..9)`|
| ص | `for (i in 1:10)`|
| PHP | `for ($i = 0; $i < 10; $i++)`|
| SQL | N/A (معتمد على المجموعة، لا توجد حلقات في لغة SQL القياسية) |
| باش | `for i in {0..9}; do ... done`|
| لوا | `for i = 0, 9 do ... end`|
| ماتلاب | `for i = 1:10 ... end`|
| برولوج | غير متاح (العودة بدلاً من ذلك) |
| اللثغة | `(dotimes (i 10) ...)`|
| ادا | `for I in 0..9 loop ... end loop;`|
| كوبول | `PERFORM VARYING I FROM 0 BY 1 UNTIL I >= 10`|
| إرلانج | غير متاح (العودة + القوائم بدلاً من ذلك) |
| أوكامل | `for i = 0 to 9 do ... done`|
| الجمعية | حلقة يدوية مع CMP/JMP |
| دلفي | `for I := 0 to 9 do ... end;`|
| سكراتش | `repeat (10) ... end`|
| VB | `For i As Integer = 0 To 9 ... Next`|
| سكالا | `for (i <- 0 until 10) ...`|
| دارت | `for (var i = 0; i < 10; i++)`|
| جوليا | `for i in 0:9 ... end`|
| تايب سكريبت | `for (let i = 0; i < 10; i++)`|
| ج # | `for (int i = 0; i < 10; i++)`|
| فورتران | `do i = 1, 10 ... end do`|
## مطابقة الأنماط / التبديل
| اللغة | بناء |
|----------|----------|
| ج | `switch (x) { case 1: ... break; }`|
| جافا | `switch (x) { case 1 -> ... }`(جافا 14+) |
| الصدأ | `match x { 1 => ..., _ => ... }`|
| هاسكل | `case x of 1 -> ...; _ -> ...`|
| سكالا | `x match { case 1 => ... }`|
| سويفت | `switch x { case 1: ... default: ... }`|
| كوتلين | `when (x) { 1 -> ... else -> ... }`|
| أوكامل | `match x with 1 -> ... \| _ -> ...`|
| إرلانج | `case X of 1 -> ...; _ -> ... end`|
| الإكسير | `case x do 1 -> ...; _ -> ... end`|
| دارت | `switch (x) { 1 => ...; _ => ... }`(دارت 3.0) |
| PHP | `match($x) { 1 => ..., default => ... }`(PHP 8.0) |
| ج # | `x switch { 1 => ..., _ => ... }`(C#8+) |
| تايب سكريبت | لا توجد مطابقة للنمط الأصلي (استخدم if/else) |
| بايثون | `match x: case 1: ... case _: ...`(بايثون 3.10+) |
| برولوج | بنيت في مطابقة الجملة |
| اذهب | `switch x { case 1: ... default: ... }`|