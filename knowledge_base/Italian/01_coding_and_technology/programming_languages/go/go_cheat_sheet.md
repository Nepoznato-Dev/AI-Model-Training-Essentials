---
# Metadata
title: "Go — Cheat Sheet"
description: "Quick-reference cheat sheet for Go syntax, concurrency, and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [go, golang, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Vai: foglio informativo
## Nozioni di base
```go
// Variables
var x int = 42
var y = "hello"          // type inferred
name := "Alice"          // short declaration
const Pi = 3.14159
const MaxRetries = 3

// Basic types
var i int     = -42
var u uint    = 100
var f float64 = 3.14
var b bool    = true
var s string  = "hello"
var c byte    = 'A'

// Zero values
var n int       // 0
var str string  // ""
var ptr *int    // nil

// Type conversion
n := 42
f := float64(n)
s := strconv.Itoa(n)
n, _ = strconv.Atoi("42")
```

## Strutture dati
```go
// Slice
s := []int{1, 2, 3}
s = append(s, 4)
s = append(s, []int{5, 6}...)
sub := s[1:3]          // [2, 3]
copy(dst, src)

// Make slice with capacity
s := make([]int, 0, 10)  // len=0, cap=10

// Map
m := map[string]int{
    "alice": 90,
    "bob":   85,
}
m["charlie"] = 78
val, ok := m["alice"]    // val=90, ok=true
delete(m, "bob")

// Struct
type User struct {
    Name  string
    Age   int
    Email string `json:"email"`
}
u := User{Name: "Alice", Age: 30}
u.Name = "Bob"
```

## Flusso di controllo
```go
if condition {
    // ...
} else if other {
    // ...
} else {
    // ...
}

// If with init
if err := doSomething(); err != nil {
    log.Fatal(err)
}

// Switch
switch day {
case "Mon", "Tue", "Wed", "Thu", "Fri":
    fmt.Println("weekday")
case "Sat", "Sun":
    fmt.Println("weekend")
default:
    fmt.Println("unknown")
}

// Switch without expression
switch {
case score >= 90: grade = "A"
case score >= 80: grade = "B"
default: grade = "C"
}

// Loops (Go only has for)
for i := 0; i < 10; i++ { ... }
for condition { ... }           // while
for { ... }                     // infinite
for i, v := range slice { ... }
for k, v := range myMap { ... }
for _, v := range slice { ... } // value only
```

## Funzioni
```go
// Basic
func add(a, b int) int {
    return a + b
}

// Multiple return values
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("division by zero")
    }
    return a / b, nil
}

// Named returns
func split(sum int) (x, y int) {
    x = sum * 4 / 9
    y = sum - x
    return  // naked return
}

// Variadic
func sum(nums ...int) int {
    total := 0
    for _, n := range nums { total += n }
    return total
}

// Closures
counter := func() func() int {
    n := 0
    return func() int { n++; return n }
}()
```

## Interfacce
```go
type Writer interface {
    Write(p []byte) (n int, err error)
}

// Implicit implementation
type File struct{}
func (f File) Write(p []byte) (int, error) { ... }
// File now implements Writer — no "implements" keyword

// Type assertion
var w io.Writer = File{}
f := w.(File)          // panic if not File
f, ok := w.(File)      // safe assertion

// Type switch
switch v := val.(type) {
case int:
    fmt.Println("int:", v)
case string:
    fmt.Println("string:", v)
default:
    fmt.Printf("unknown: %T\n", v)
}

// Empty interface (any type) — Go 1.18+ use any
var x any = 42
```

## Concorrenza
```go
// Goroutine
go func() {
    fmt.Println("running concurrently")
}()

// Channel
ch := make(chan int)
ch <- 42           // send
val := <-ch        // receive

// Buffered channel
ch := make(chan int, 100)

// Select
select {
case msg := <-ch1:
    handle(msg)
case ch2 <- data:
    fmt.Println("sent")
case <-time.After(5 * time.Second):
    fmt.Println("timeout")
}

// WaitGroup
var wg sync.WaitGroup
for i := 0; i < 5; i++ {
    wg.Add(1)
    go func(id int) {
        defer wg.Done()
        process(id)
    }(i)
}
wg.Wait()

// Mutex
var mu sync.Mutex
mu.Lock()
counter++
mu.Unlock()
```

## Gestione degli errori
```go
// Custom error
type NotFoundError struct {
    ID string
}
func (e *NotFoundError) Error() string {
    return fmt.Sprintf("not found: %s", e.ID)
}

// Wrapping (Go 1.13+)
if err != nil {
    return fmt.Errorf("process %s: %w", name, err)
}

// errors.Is / errors.As
if errors.Is(err, os.ErrNotExist) { ... }
var nfe *NotFoundError
if errors.As(err, &nfe) { ... }
```

## Generici (Go 1.18+)
```go
func Map[T any, U any](s []T, f func(T) U) []U {
    result := make([]U, len(s))
    for i, v := range s {
        result[i] = f(v)
    }
    return result
}

type Set[T comparable] struct {
    items map[T]struct{}
}
```
