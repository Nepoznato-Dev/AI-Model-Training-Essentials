---
# Metadata
title: "Go — Syntax Reference"
description: "Detailed syntax reference for Go covering operators, control flow, functions, data structures, interfaces, concurrency, error handling, and advanced features."
category: "Coding and Technology"
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [go, golang, syntax-reference, operators, control-flow, concurrency, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Go — odwołanie do składni
Ten dokument zawiera kompleksowe, uporządkowane omówienie składni języka Go. Uzupełnia główne odniesienia do Go, koncentrując się na wyczerpujących wzorcach składni, tabelach operatorów i wewnętrznej mechanice goroutines, kanałów i interfejsów.
---

## Operatory i wyrażenia
### Operatory arytmetyczne
| Operator | Imię | Przykład | Wynik | Notatki |
|---------|------|---------|--------|-------|
| `+`| Dodatek | `3 + 2`| `5`| Również łączenie ciągów |
| `-`| Odejmowanie | `3 - 2`| `1`| |
| `*`| Mnożenie | `3 * 2`| `6`| |
| `/`| Podział | `7 / 2`| `3`| Dzielenie liczb całkowitych dla int |
| `%`| Reszta | `7 % 2`| `1`| Znak pasuje do dywidendy |
| `&`| Bitowe ORAZ | `5 & 3`| `1`| |
| `\|`| Bitowe LUB | `5 \| 3`| `7`| |
| `^`| Bitowy XOR | `5 ^ 3`| `6`| Również uzupełnienie bitowe (jednoargumentowe) |
| `&^`| Trochę jasne (I NIE) | `5 &^ 3`| `4`| Wyjątkowe, aby przejść |
| `<<`| Lewy Shift | `5 << 1`| `10`| |
| `>>`| Prawy Shift | `5 >> 1`| `2`| |
### Operatory porównania
| Operator | Imię | Przykład | Notatki |
|---------|------|---------|-------|
| `==`| Równe | `x == y`| Tylko porównywalne typy |
| `!=`| Nierówne | `x != y`| |
| `<`,`>`,`<=`,`>=`| Zamawianie | `x >= y`| Ciągi porównane leksykograficznie |
### Operatory logiczne
| Operator | Imię | Przykład | Notatki |
|---------|------|---------|-------|
| `&&`| Logiczne ORAZ | `a && b`| Zwarcie |
| `\|\|`| Logiczne LUB | `a \|\| b`| Zwarcie |
| `!`| Logiczne NIE | `!true`| `false`|
### Pierwszeństwo operatora (od najwyższego do najniższego)
| Pierwszeństwo | Operatorzy |
|------------|-----------|
| 5 (najwyższy) | `*``/``%``<<``>>``&``&^`|
| 4 | `+``-``\|``^` |
| 3 | `==``!=``<``<=``>``>=` |
| 2 | `&&`|
| 1 (najniższy) | `\|\|`|
---

## Kontroluj przepływ
### Instrukcje warunkowe
```go
// Basic if/else
if score >= 90 {
    grade = "A"
} else if score >= 80 {
    grade = "B"
} else {
    grade = "F"
}

// If with initialization (variable scoped to if block)
if err := doSomething(); err != nil {
    log.Printf("Error: %v", err)
}
// err is not accessible here

// Switch — no fall-through by default
switch day {
case "Monday":
    fmt.Println("Start of week")
case "Friday":
    fmt.Println("Almost weekend")
case "Saturday", "Sunday":
    fmt.Println("Weekend")
default:
    fmt.Println("Midweek")
}

// Switch with no condition (if/else chain)
switch {
case score >= 90:
    grade = "A"
case score >= 80:
    grade = "B"
default:
    grade = "F"
}

// Type switch
func describe(i interface{}) string {
    switch v := i.(type) {
    case int:
        return fmt.Sprintf("integer: %d", v)
    case string:
        return fmt.Sprintf("string: %q", v)
    case bool:
        return fmt.Sprintf("bool: %t", v)
    default:
        return fmt.Sprintf("unknown: %T", i)
    }
}

// Fall-through (explicit)
switch {
case x > 100:
    fmt.Println("big")
    fallthrough
case x > 10:
    fmt.Println("medium")  // Also prints if x > 100
}
```

### Pętle
```go
// Go has only one loop keyword: for

// Classic for loop
for i := 0; i < 10; i++ {
    fmt.Println(i)
}

// While-style loop
for count < 10 {
    count++
}

// Infinite loop
for {
    if done { break }
}

// For-range over slice
for i, v := range []string{"a", "b", "c"} {
    fmt.Printf("%d: %s\n", i, v)
}

// For-range over map (random order!)
for key, value := range myMap {
    fmt.Printf("%s = %v\n", key, value)
}

// For-range over string (iterates runes, not bytes)
for i, r := range "Hello 世界" {
    fmt.Printf("%d: %c\n", i, r)
}

// For-range over channel
for item := range ch {
    process(item)
}

// Skip index or value with _
for _, value := range items {
    process(value)
}
for index := range items {
    fmt.Println(index)
}

// Loop control
for i := 0; i < 100; i++ {
    if i%2 == 0 { continue }
    if i > 50 { break }
    fmt.Println(i)
}

// Labeled loops (break/continue outer loop)
outer:
for i := 0; i < 5; i++ {
    for j := 0; j < 5; j++ {
        if i*j > 6 {
            break outer
        }
    }
}
```

---

## Funkcje
### Składnia funkcji
```go
// Basic function
func add(a int, b int) int {
    return a + b
}

// Multiple return values
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}

// Named return values
func split(sum int) (x, y int) {
    x = sum * 4 / 9
    y = sum - x
    return  // "naked" return — returns x and y
}

// Variadic function
func sum(nums ...int) int {
    total := 0
    for _, n := range nums {
        total += n
    }
    return total
}
sum(1, 2, 3, 4)  // 10

// Pass slice to variadic
values := []int{1, 2, 3}
sum(values...)

// Function as value
apply := func(f func(int) int, x int) int {
    return f(x)
}
double := func(x int) int { return x * 2 }
result := apply(double, 5)  // 10

// Closures
func counter() func() int {
    count := 0
    return func() int {
        count++
        return count
    }
}
c := counter()
c()  // 1
c()  // 2
c()  // 3

// Defer — execute when surrounding function returns
func readFile(path string) ([]byte, error) {
    f, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer f.Close()  // Guaranteed to run

    return io.ReadAll(f)
}

// Multiple defers — execute in LIFO order
func example() {
    defer fmt.Println("third")
    defer fmt.Println("second")
    defer fmt.Println("first")
}
```

### Metody
```go
// Value receiver — does not modify the original
func (p Point) Distance() float64 {
    return math.Sqrt(p.X*p.X + p.Y*p.Y)
}

// Pointer receiver — modifies the original
func (p *Point) Scale(factor float64) {
    p.X *= factor
    p.Y *= factor
}

// Method on custom type
type Celsius float64
func (c Celsius) Fahrenheit() float64 {
    return float64(c)*9/5 + 32
}
func (c Celsius) String() string {
    return fmt.Sprintf("%.1f°C", c)
}
```

---

## Struktury danych
### Tablice i plasterki
```go
// Arrays — fixed size, value type
var arr [5]int           // [0, 0, 0, 0, 0]
arr2 := [3]int{1, 2, 3}
arr3 := [...]int{10, 20, 30}  // Compiler counts elements

// Slices — dynamic, reference to underlying array
var s []int                    // nil slice
s2 := []int{1, 2, 3}          // Literal
s3 := make([]int, 5)           // len=5, cap=5, zeroed
s4 := make([]int, 5, 10)       // len=5, cap=10
s5 := make([]int, 0, 100)      // Empty but pre-allocated

// Slicing
sub := s2[1:3]    // [2, 3] — shares backing array
head := s2[:2]    // [1, 2]
tail := s2[1:]    // [2, 3]
full := s2[:]     // [1, 2, 3]

// append — may reallocate
s = append(s, 4, 5, 6)
s = append(s, otherSlice...)  // Append another slice

// copy — independent copy
dst := make([]int, len(src))
copy(dst, src)

// Common patterns
// Filter
evens := make([]int, 0)
for _, v := range nums {
    if v%2 == 0 { evens = append(evens, v) }
}

// Map
doubled := make([]int, len(nums))
for i, v := range nums {
    doubled[i] = v * 2
}

// Reduce
sum := 0
for _, v := range nums {
    sum += v
}
```

### Mapy
```go
// Creation
var m map[string]int                  // nil map — can read, cannot write
m2 := make(map[string]int)            // Empty, ready to use
m3 := map[string]int{"a": 1, "b": 2} // Literal

// Access
val := m["key"]           // Zero value if missing
val, ok := m["key"]       // Check existence
if !ok { val = 0 }        // Handle missing

// Mutation
m["key"] = 42             // Set
delete(m, "key")           // Delete

// Iteration (random order!)
for key, value := range m {
    fmt.Printf("%s: %d\n", key, value)
}

// Sorted iteration
keys := make([]string, 0, len(m))
for k := range m { keys = append(keys, k) }
sort.Strings(keys)
for _, k := range keys {
    fmt.Printf("%s: %d\n", k, m[k])
}

// Group by pattern
groups := make(map[string][]Person)
for _, p := range people {
    groups[p.City] = append(groups[p.City], p)
}
```

### Struktury
```go
// Struct definition
type User struct {
    ID        int       `json:"id"`
    Name      string    `json:"name"`
    Email     string    `json:"email,omitempty"`
    CreatedAt time.Time `json:"created_at"`
}

// Creation
u := User{ID: 1, Name: "Alice", Email: "alice@example.com"}
u2 := User{}                           // Zero values
u3 := new(User)                        // *User — pointer to zero value

// Embedded structs (composition, not inheritance)
type Employee struct {
    User                           // Embedded — promotes User's fields
    Department string
    Salary     float64
}

emp := Employee{
    User:       User{ID: 1, Name: "Bob"},
    Department: "Engineering",
    Salary:     95000,
}
fmt.Println(emp.Name)   // "Bob" — promoted from User

// Struct tags
type Config struct {
    Host    string `json:"host" yaml:"host" env:"DB_HOST"`
    Port    int    `json:"port" yaml:"port" env:"DB_PORT"`
    Timeout time.Duration `json:"timeout" yaml:"timeout"`
}
```

---

## Interfejsy
```go
// Interface definition
type Reader interface {
    Read(p []byte) (n int, err error)
}

type Writer interface {
    Write(p []byte) (n int, err error)
}

// Composition
type ReadWriter interface {
    Reader
    Writer
}

// Empty interface — satisfied by any type
// Go 1.18+: prefer 'any' alias
func printAny(v any) {
    fmt.Println(v)
}

// Type assertion
var i interface{} = "hello"
s := i.(string)           // Panics if not string
s, ok := i.(string)       // Safe — ok is false if wrong type

// Type switch (see Control Flow section)

// Interface satisfaction check (compile-time)
var _ io.Reader = (*MyReader)(nil)  // Fails if MyReader doesn't implement io.Reader

// Common standard interfaces
// io.Reader, io.Writer, io.Closer
// fmt.Stringer — String() string
// error — Error() string
// sort.Interface — Len(), Less(i,j int) bool, Swap(i,j int)
// context.Context — Deadline(), Done(), Err(), Value()
```

---

## Współbieżność
### Goroutiny
```go
// Launch a goroutine
go func() {
    fmt.Println("running concurrently")
}()

// With named function
go processItem(item)

// WaitGroup — wait for goroutines to finish
var wg sync.WaitGroup
for i := 0; i < 10; i++ {
    wg.Add(1)
    go func(id int) {
        defer wg.Done()
        process(id)
    }(i)
}
wg.Wait()
```

### Kanały
```go
// Unbuffered channel — synchronous
ch := make(chan int)
ch <- 42        // Send (blocks until receiver ready)
val := <-ch     // Receive (blocks until sender ready)

// Buffered channel — asynchronous up to capacity
ch := make(chan int, 100)
ch <- 42        // Non-blocking if buffer not full
val := <-ch     // Receive from buffer

// Directional channels
func producer(out chan<- int) { /* send only */ }
func consumer(in <-chan int) { /* receive only */ }

// Select — multiplex channel operations
select {
case msg := <-ch1:
    handle(msg)
case ch2 <- data:
    sent()
case <-time.After(5 * time.Second):
    timeout()
default:
    // Non-blocking — runs if no case ready
}

// Fan-out / Fan-in pattern
func fanOut(input <-chan int, workers int) []<-chan int {
    channels := make([]<-chan int, workers)
    for i := 0; i < workers; i++ {
        ch := make(chan int)
        go func() {
            for n := range input {
                ch <- n * 2
            }
            close(ch)
        }()
        channels[i] = ch
    }
    return channels
}

// Close and range
close(ch)        // Signal no more values
for v := range ch {  // Exits when channel is closed and empty
    fmt.Println(v)
}
```

### Synchronizuj elementy podstawowe
```go
// Mutex
var mu sync.Mutex
mu.Lock()
shared++
mu.Unlock()

// RWMutex — multiple readers OR one writer
var rw sync.RWMutex
rw.RLock()    // Multiple goroutines can hold this
_ = data
rw.RUnlock()
rw.Lock()     // Exclusive
data = newValue
rw.Unlock()

// Once — execute function exactly once
var once sync.Once
once.Do(func() {
    initializeExpensiveResource()
})

// WaitGroup (see Goroutines section)

// atomic — lock-free operations
var count atomic.Int64
count.Add(1)
val := count.Load()

// Map — concurrent-safe map
var m sync.Map
m.Store("key", "value")
val, ok := m.Load("key")
```

---

## Obsługa błędów
```go
// Error interface
type error interface {
    Error() string
}

// Custom error type
type NotFoundError struct {
    Resource string
    ID       string
}
func (e *NotFoundError) Error() string {
    return fmt.Sprintf("%s not found: %s", e.Resource, e.ID)
}

// Sentinel errors
var (
    ErrNotFound    = errors.New("not found")
    ErrUnauthorized = errors.New("unauthorized")
)

// Error wrapping
func getUser(id string) (*User, error) {
    user, err := db.Find(id)
    if err != nil {
        return nil, fmt.Errorf("getUser(%s): %w", id, err)
    }
    return user, nil
}

// Error checking
if errors.Is(err, ErrNotFound) {
    handleNotFound()
}
var nfe *NotFoundError
if errors.As(err, &nfe) {
    fmt.Printf("Resource: %s, ID: %s\n", nfe.Resource, nfe.ID)
}

// Panic and Recover (use sparingly)
func safeProcess() (err error) {
    defer func() {
        if r := recover(); r != nil {
            err = fmt.Errorf("panic recovered: %v", r)
        }
    }()
    panic("something terrible")
}
```

---

## Generics (Przejdź do wersji 1.18+)
```go
// Generic function
func Map[T any, U any](s []T, f func(T) U) []U {
    result := make([]U, len(s))
    for i, v := range s {
        result[i] = f(v)
    }
    return result
}

// Type constraints
type Number interface {
    ~int | ~int32 | ~int64 | ~float32 | ~float64
}

func Sum[T Number](nums []T) T {
    var total T
    for _, n := range nums {
        total += n
    }
    return total
}

// Generic struct
type Set[T comparable] struct {
    items map[T]struct{}
}

func NewSet[T comparable]() *Set[T] {
    return &Set[T]{items: make(map[T]struct{})}
}

func (s *Set[T]) Add(item T)    { s.items[item] = struct{}{} }
func (s *Set[T]) Contains(item T) bool {
    _, ok := s.items[item]
    return ok
}

// Constraint: ordered types
type Ordered interface {
    ~int | ~int32 | ~int64 | ~float32 | ~float64 | ~string
}

func Min[T Ordered](a, b T) T {
    if a < b { return a }
    return b
}
```

---

## Pakiety i moduły
```go
// Package declaration
package mypackage

// Exported names start with uppercase
func PublicFunc() {}    // Exported
func privateFunc() {}   // Unexported (package-private)

// Import
import (
    "fmt"
    "net/http"
    "myproject/internal/utils"
)

// go.mod
module github.com/user/project

go 1.22

require (
    github.com/gin-gonic/gin v1.9.1
    golang.org/x/sync v0.6.0
)

// Common standard library packages
// fmt        — formatted I/O
// net/http   — HTTP client and server
// encoding/json — JSON encoding/decoding
// os         — OS functionality
// io         — I/O primitives
// sync       — synchronization primitives
// context    — deadlines, cancellation
// testing    — unit testing
// log/slog   — structured logging (Go 1.21+)
```

---

## Streszczenie
Składnia Go jest celowo minimalna — bez dziedziczenia, bez przeciążania metod, bez wyjątków i bez makr. Pozostaje czysty, ortogonalny zestaw konstrukcji: struktury i interfejsy do kompozycji, goroutines i kanały dla współbieżności oraz jawna obsługa błędów zapewniająca niezawodność. Siła języka nie wynika ze złożonej składni, ale z eleganckiej interakcji prostych elementów pierwotnych. Generics (Go 1.18+) zwiększa elastyczność typów bez utraty charakterystycznej przejrzystości Go.