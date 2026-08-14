<!--
---
# Metadata
title: "Go"
description: "Comprehensive reference for the Go programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
tags: [go, programming-language, syntax, ecosystem, coding-and-technology]
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

-->
#যাও
গো (প্রায়ই এটির আসল ডোমেন নামের পরে "গোলাং" বলা হয়) হল একটি স্ট্যাটিকলি টাইপ করা, সংকলিত প্রোগ্রামিং ভাষা যা Google-এ রবার্ট গ্রিজেমার, রব পাইক এবং কেন থম্পসন দ্বারা ডিজাইন করা হয়েছে। এটি প্রথম 2012 সালে সিস্টেম প্রোগ্রামিংয়ের জন্য একটি ভাল ভাষা হওয়ার সুস্পষ্ট লক্ষ্য নিয়ে প্রকাশিত হয়েছিল -- যেটি পাইথনের মতো গতিশীল ভাষার উত্পাদনশীলতার সাথে C-এর কর্মক্ষমতাকে একত্রিত করে। Go তার সরলতা, দ্রুত সংকলন, অন্তর্নির্মিত একযোগে (গোরুটিন এবং চ্যানেল) এবং চমৎকার টুলিংয়ের জন্য পরিচিত।
Go ক্লাউড ইনফ্রাস্ট্রাকচার ইকোসিস্টেমের বেশির ভাগকে ক্ষমতা দেয়: Docker, Kubernetes, Terraform, Prometheus, etcd এবং Go স্ট্যান্ডার্ড লাইব্রেরির HTTP সার্ভার সবই Go-তে লেখা। এটি ক্লাউড-নেটিভ ডেভেলপমেন্ট, মাইক্রোসার্ভিস এবং CLI টুলের জন্য ডিফল্ট ভাষা হয়ে উঠেছে।
---

## কেন যান ম্যাটারস
- **ডিজাইন অনুসারে সরলতা**: Go-তে মাত্র 25টি কীওয়ার্ড রয়েছে। ভাষাটি ইচ্ছাকৃতভাবে ছোট এবং শেখা সহজ।
- **দ্রুত সংকলন**: সেকেন্ডের মধ্যে সরাসরি মেশিন কোডে কম্পাইল করে, এমনকি বড় প্রকল্পের জন্যও।
- **বিল্ট-ইন কনকারেন্সি**: গোরুটিন এবং চ্যানেল সমসাময়িক প্রোগ্রামিংকে অ্যাক্সেসযোগ্য এবং দক্ষ করে তোলে।
- **চমৎকার স্ট্যান্ডার্ড লাইব্রেরি**: HTTP সার্ভার, JSON এনকোডিং, টেস্টিং, ক্রিপ্টোগ্রাফি -- সবই অন্তর্নির্মিত৷
- **স্ট্যাটিক বাইনারি**: কোনো বাহ্যিক নির্ভরতা ছাড়াই একটি একক বাইনারিতে কম্পাইল করে। স্থাপনা তুচ্ছ।
- **গুগল-স্কেল পেডিগ্রি**: প্রকৌশলীদের দ্বারা ডিজাইন করা হয়েছে যারা ইউনিক্স, UTF-8 এবং গুগলের অনেক অবকাঠামো তৈরি করেছেন।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **কোন যোগফল প্রকার / প্যাটার্ন মিলে না** | সম্পর্কিত তথ্যের সাথে কোন enums নেই, কোন বীজগণিতের প্রকার নেই | ইন্টারফেস এবং টাইপ সুইচ ব্যবহার করুন |
| **শব্দ পরিচালনায় ত্রুটি** | ভুল হলে স্পষ্ট!= শূন্য সর্বত্র চেক করে | প্যাটার্ন গ্রহণ করুন; এটি ত্রুটি পরিচালনা দৃশ্যমান করে তোলে |
| **ছোট ইকোসিস্টেম** | পাইথন, জাভা, বা জাভাস্ক্রিপ্টের চেয়ে কম লাইব্রেরি | স্ট্যান্ডার্ড লাইব্রেরি বেশিরভাগ চাহিদা কভার করে; কমিউনিটি প্যাকেজ বাড়ছে |
| **কোন GUI ফ্রেমওয়ার্ক নেই** | ডেস্কটপ বা মোবাইল UI এর জন্য উপযুক্ত নয় | ওয়েব-ভিত্তিক UIs (WASM) বা অন্য ভাষা ব্যবহার করুন |
| **আবর্জনা সংগ্রহকারী** | একটি GC আছে -- বিরতিগুলি ছোট কিন্তু শূন্য নয় | লেটেন্সি-সংবেদনশীল কাজের চাপের জন্য GC টিউন করুন; sync.Pool ব্যবহার করুন |
---

## সিনট্যাক্স মৌলিক
### মৌলিক কাঠামো
```go
package main

import (
    "fmt"
    "strings"
)

func main() {
    name := "World"
    fmt.Printf("Hello, %s!\n", name)

    age := 30
    score := 9.5
    active := true
    message := "Hello"

    upper := strings.ToUpper(message)
    fmt.Println(upper)
}
```

### ফাংশন
```go
// Multiple return values
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}

result, err := divide(10, 3)
if err != nil {
    fmt.Println("Error:", err)
    return
}

// Named return values
func split(sum int) (x, y int) {
    x = sum * 4 / 9
    y = sum - x
    return
}

// Variadic functions
func sum(nums ...int) int {
    total := 0
    for _, n := range nums {
        total += n
    }
    return total
}
```

### কাঠামো এবং ইন্টারফেস
```go
type Animal struct {
    Name string
    Age  int
}

func (a Animal) Speak() string {
    return a.Name + " makes a sound"
}

// Embedding (composition, not inheritance)
type Dog struct {
    Animal
    Breed string
}

func (d Dog) Speak() string {
    return d.Name + " says woof"
}

// Interface -- implicitly satisfied
type Speaker interface {
    Speak() string
}

func announce(s Speaker) {
    fmt.Println(s.Speak())
}

dog := Dog{Animal: Animal{Name: "Rex"}, Breed: "Labrador"}
announce(dog)
```

### ত্রুটি হ্যান্ডলিং
```go
type InsufficientFundsError struct {
    Balance float64
    Amount  float64
}

func (e *InsufficientFundsError) Error() string {
    return fmt.Sprintf("cannot withdraw $%.2f from $%.2f", e.Amount, e.Balance)
}

func withdraw(balance, amount float64) (float64, error) {
    if amount > balance {
        return balance, &InsufficientFundsError{Balance: balance, Amount: amount}
    }
    return balance - amount, nil
}

newBalance, err := withdraw(100, 150)
if err != nil {
    var fundsErr *InsufficientFundsError
    if errors.As(err, &fundsErr) {
        fmt.Printf("Need $%.2f more\n", fundsErr.Amount-fundsErr.Balance)
    }
}
```

### সঙ্গতি -- গোরুটিন এবং চ্যানেল
```go
// Goroutine
go func() {
    fmt.Println("Running concurrently")
}()

// Channels
func producer(ch chan<- int) {
    for i := 0; i < 5; i++ { ch <- i }
    close(ch)
}

func consumer(ch <-chan int) {
    for value := range ch {
        fmt.Println("Received:", value)
    }
}

ch := make(chan int)
go producer(ch)
consumer(ch)

// WaitGroup
var wg sync.WaitGroup
for i := 0; i < 5; i++ {
    wg.Add(1)
    go func(id int) {
        defer wg.Done()
        fmt.Printf("Worker %d done\n", id)
    }(i)
}
wg.Wait()
```

---

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### জেনেরিক (গো 1.18+)
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
    ~int | ~float64 | ~float32
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

func (s *Set[T]) Add(item T)  { s.items[item] = struct{}{} }
func (s *Set[T]) Has(item T) bool {
    _, ok := s.items[item]
    return ok
}
```

### উন্নত প্যাটার্ন ম্যাচিং (টাইপ সুইচ)
```go
func describe(i interface{}) string {
    switch v := i.(type) {
    case int:
        return fmt.Sprintf("Integer: %d", v)
    case string:
        return fmt.Sprintf("String: %q", v)
    case bool:
        return fmt.Sprintf("Bool: %t", v)
    case []int:
        return fmt.Sprintf("Int slice of length %d", len(v))
    default:
        return fmt.Sprintf("Unknown type: %T", v)
    }
}

// Comma-ok idiom
var i interface{} = "hello"
s, ok := i.(string)
if ok {
    fmt.Println("String:", s)
}
```

### কাস্টম ত্রুটি মোড়ানো
```go
import "errors"

var (
    ErrNotFound    = errors.New("not found")
    ErrUnauthorized = errors.New("unauthorized")
)

type ValidationError struct {
    Field   string
    Message string
    Err     error
}

func (e *ValidationError) Error() string {
    return fmt.Sprintf("validation: %s: %s", e.Field, e.Message)
}

func (e *ValidationError) Unwrap() error { return e.Err }

func validateAge(age int) error {
    if age < 0 {
        return &ValidationError{
            Field: "age", Message: "must be non-negative",
        }
    }
    return nil
}

// Error wrapping and checking
func getUser(id int) (*User, error) {
    user, err := db.Find(id)
    if err != nil {
        return nil, fmt.Errorf("getUser(%d): %w", id, ErrNotFound)
    }
    return user, nil
}

// Usage
_, err := getUser(42)
if errors.Is(err, ErrNotFound) {
    fmt.Println("User not found")
}
```

---

## সামঞ্জস্য এবং সমান্তরালতা (গভীর ডুব)
### কর্মী পুল প্যাটার্ন
```go
func workerPool(jobs <-chan int, results chan<- int, workerCount int) {
    var wg sync.WaitGroup
    for w := 0; w < workerCount; w++ {
        wg.Add(1)
        go func(id int) {
            defer wg.Done()
            for j := range jobs {
                results <- j * 2  // Process job
            }
        }(w)
    }
    wg.Wait()
    close(results)
}

func main() {
    jobs := make(chan int, 100)
    results := make(chan int, 100)

    go workerPool(jobs, results, 5)

    for j := 1; j <= 20; j++ {
        jobs <- j
    }
    close(jobs)

    for r := range results {
        fmt.Println("Result:", r)
    }
}
```

### বাতিল করার প্রসঙ্গ
```go
func fetchWithTimeout(ctx context.Context, url string) ([]byte, error) {
    ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
    defer cancel()

    req, err := http.NewRequestWithContext(ctx, "GET", url, nil)
    if err != nil {
        return nil, err
    }

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        return nil, err
    }
    defer resp.Body.Close()
    return io.ReadAll(resp.Body)
}
```

### মাল্টিপ্লেক্সিংয়ের জন্য নির্বাচন করুন
```go
func fanIn(ch1, ch2 <-chan string) <-chan string {
    merged := make(chan string)
    go func() {
        for {
            select {
            case v := <-ch1:
                merged <- v
            case v := <-ch2:
                merged <- v
            }
        }
    }()
    return merged
}
```

---

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### প্রকল্পের কাঠামো
```
my_project/
+-- go.mod
+-- go.sum
+-- main.go
+-- internal/
|   +-- handlers/
|   |   +-- api.go
|   +-- models/
|   |   +-- user.go
|   +-- service/
|       +-- user_service.go
+-- pkg/
|   +-- utils/
|       +-- helpers.go
+-- cmd/
|   +-- server/
|       +-- main.go
|   +-- cli/
|       +-- main.go
+-- api/
|   +-- openapi.yaml
+-- configs/
|   +-- config.yaml
+-- deployments/
|   +-- Dockerfile
+-- .golangci.yml
```

### go.mod
```
module github.com/example/my_project

go 1.22

require (
    github.com/gin-gonic/gin v1.10.0
    github.com/go-sql-driver/mysql v1.8.0
    go.uber.org/zap v1.27.0
)
```

### অত্যাবশ্যকীয় আদেশ
```bash
go mod init myproject         # Initialise module
go mod tidy                   # Download and clean dependencies
go build -o myapp             # Build binary
go run main.go                # Run without building
go test ./...                 # Run all tests
go vet ./...                  # Static analysis
gofmt -w .                    # Format code
go generate ./...             # Run code generators
```

### CI/CD পাইপলাইন (GitHub অ্যাকশন)
```yaml
name: Go CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v5
        with:
          go-version: '1.22'
      - run: go vet ./...
      - run: go test -race -coverprofile=coverage.out ./...
      - run: go build ./...
```

---

## পরীক্ষা
### ইউনিট পরীক্ষা
```go
// math_test.go
package math

import "testing"

func TestAdd(t *testing.T) {
    tests := []struct {
        name     string
        a, b     int
        expected int
    }{
        {"positive", 2, 3, 5},
        {"negative", -1, -2, -3},
        {"zero", 0, 0, 0},
        {"mixed", -1, 1, 0},
    }
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            result := Add(tt.a, tt.b)
            if result != tt.expected {
                t.Errorf("Add(%d, %d) = %d; want %d", tt.a, tt.b, result, tt.expected)
            }
        })
    }
}

func BenchmarkAdd(b *testing.B) {
    for i := 0; i < b.N; i++ {
        Add(2, 3)
    }
}
```

### টেবিল-চালিত HTTP পরীক্ষা
```go
func TestHandler(t *testing.T) {
    req := httptest.NewRequest("GET", "/health", nil)
    w := httptest.NewRecorder()
    healthHandler(w, req)

    if w.Code != http.StatusOK {
        t.Errorf("expected 200, got %d", w.Code)
    }
}
```

```bash
go test ./...                    # All tests
go test -v ./...                 # Verbose
go test -race ./...              # Race detector
go test -cover ./...             # Coverage
go test -bench=. ./...           # Benchmarks
go test -fuzz=Fuzz ./...         # Fuzz testing
```

---

## ইন্টারঅপারেবিলিটি
### CGo (গো থেকে C কল করা)
```go
package main

// #include <stdio.h>
// #include <stdlib.h>
//
// void print_hello() {
//     printf("Hello from C!\n");
// }
import "C"
import "unsafe"

func main() {
    C.print_hello()

    // Passing strings to C
    cs := C.CString("Hello from Go")
    defer C.free(unsafe.Pointer(cs))
    // Use cs in C function calls
}
```

### অন্যান্য ভাষার সাথে এফএফআই
| দিকনির্দেশ | মেকানিজম |
|------------|------------|
| C কল করতে যান | cgo (`import "C"`) |
| C++ | কল করতে যান cgo + C wrapper ফাংশন |
| সি কলিং গো |`//export`এর সাথে Go ফাংশন রপ্তানি করুন |
| পাইথন কল করতে যান | গোপি বা সাবপ্রসেস ব্যবহার করুন |
---

## ডিজাইন প্যাটার্ন
### মিডলওয়্যার প্যাটার্ন (HTTP)
```go
type Middleware func(http.Handler) http.Handler

func Logging(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        start := time.Now()
        next.ServeHTTP(w, r)
        log.Printf("%s %s %v", r.Method, r.URL.Path, time.Since(start))
    })
}

func Auth(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        token := r.Header.Get("Authorization")
        if token == "" {
            http.Error(w, "Unauthorized", http.StatusUnauthorized)
            return
        }
        next.ServeHTTP(w, r)
    })
}

func Chain(h http.Handler, middlewares ...Middleware) http.Handler {
    for i := len(middlewares) - 1; i >= 0; i-- {
        h = middlewares[i](h)
    }
    return h
}
```

### বিকল্প প্যাটার্ন
```go
type Server struct {
    host    string
    port    int
    timeout time.Duration
}

type Option func(*Server)

func WithHost(host string) Option    { return func(s *Server) { s.host = host } }
func WithPort(port int) Option       { return func(s *Server) { s.port = port } }
func WithTimeout(d time.Duration) Option { return func(s *Server) { s.timeout = d } }

func NewServer(opts ...Option) *Server {
    s := &Server{host: "localhost", port: 8080, timeout: 30 * time.Second}
    for _, opt := range opts { opt(s) }
    return s
}

srv := NewServer(WithHost("0.0.0.0"), WithPort(3000))
```

---

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### প্রোফাইলিং
```bash
go test -cpuprofile=cpu.prof -bench=. ./...
go tool pprof cpu.prof
go test -memprofile=mem.prof -bench=. ./...
go tool pprof mem.prof
```

### অপ্টিমাইজেশান টিপস
```go
// Pre-allocate slices when size is known
result := make([]int, 0, 1000)

// Use sync.Pool for frequently allocated objects
var bufPool = sync.Pool{
    New: func() interface{} { return new(bytes.Buffer) },
}

// Avoid string concatenation in loops
var b strings.Builder
for i := 0; i < 1000; i++ {
    b.WriteString("hello")
}
result := b.String()
```

---

## স্থাপনা
### ক্রস-সংকলন
```bash
GOOS=linux GOARCH=amd64 go build -o myapp-linux
GOOS=windows GOARCH=amd64 go build -o myapp.exe
GOOS=darwin GOARCH=arm64 go build -o myapp-mac
```

### ডকার স্থাপনা
```dockerfile
FROM golang:1.22-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY src/ ./
RUN CGO_ENABLED=0 go build -o myapp .

FROM alpine:latest
COPY --from=builder /app/myapp /usr/local/bin/myapp
CMD ["myapp"]
```

---

## স্ট্যান্ডার্ড লাইব্রেরি
| প্যাকেজ | উদ্দেশ্য |
|---------|---------|
| fmt | বিন্যাসিত I/O |
| নেট/http | HTTP ক্লায়েন্ট এবং সার্ভার |
| এনকোডিং/json | JSON এনকোডিং/ডিকোডিং |
| os | OS-স্তরের অপারেশন |
| io | I/O আদিম |
| স্ট্রিং / strconv | স্ট্রিং ম্যানিপুলেশন |
| সিঙ্ক | Mutex, WaitGroup, একবার |
| প্রসঙ্গ | সময়সীমা, বাতিলকরণ |
| পরীক্ষা | বিল্ট-ইন টেস্টিং ফ্রেমওয়ার্ক |
| log/log/slog | লগিং |
| সময় | সময় এবং সময়কাল |
| ক্রিপ্টো | ক্রিপ্টোগ্রাফি (TLS, হ্যাশিং) |
| ডাটাবেস/sql | ডাটাবেস বিমূর্ততা |
---

## টুলিং
```bash
go mod init myproject
go run main.go
go build -o myapp
go test ./...
gofmt -w .
go vet ./...
go mod tidy
```

---

## কখন Go ব্যবহার করবেন
| দৃশ্যকল্প | কেন যান | ভাল বিকল্প |
|------------|---------|---------|
| ক্লাউড-নেটিভ সার্ভিস/মাইক্রো সার্ভিসেস | দ্রুত, ছোট বাইনারি, চমৎকার HTTP | সর্বোচ্চ কর্মক্ষমতা জন্য মরিচা |
| CLI টুলস | দ্রুত সংকলন, একক বাইনারি | জটিল CLI এর জন্য মরিচা |
| ওয়েব সার্ভার / APIs | অন্তর্নির্মিত HTTP, দ্রুত, সহজ | দ্রুত প্রোটোটাইপিংয়ের জন্য Node.js/Express |
| DevOps টুলিং | ডকার, কুবারনেটস, টেরাফর্ম গো | স্ক্রিপ্টিংয়ের জন্য পাইথন |
| সমবর্তী সিস্টেম | গোরুটিনগুলি লাইটওয়েট এবং মার্জিত | এরলাং/এলিক্সির দোষ-সহনশীল সঙ্গতি জন্য |
| নেটওয়ার্ক প্রোগ্রামিং | চমৎকার নেট প্যাকেজ | সর্বনিম্ন-স্তরের নিয়ন্ত্রণের জন্য C/C++ |
| ডেটা সায়েন্স / এমএল | সঠিক বাস্তুতন্ত্র নয় | পাইথন, আর |
| ডেস্কটপ/মোবাইল GUI | কোন GUI ফ্রেমওয়ার্ক নেই | একটি ওয়েব ফ্রন্টএন্ড বা স্থানীয় ভাষা ব্যবহার করুন |
| এমবেডেড সিস্টেম | খুব ভারী (GC, রানটাইম) | সি, মরিচা |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: কেন Go এর ব্যতিক্রম নেই? আমি কিভাবে ত্রুটি পরিচালনা করা উচিত?
**A:** Go ব্যতিক্রমের পরিবর্তে স্পষ্ট ত্রুটি রিটার্ন ব্যবহার করে। ব্যর্থ হতে পারে এমন প্রতিটি ফাংশন তার শেষ রিটার্ন মান হিসাবে একটি`error`প্রদান করে। এটি কলারকে স্পষ্টভাবে ত্রুটিগুলি পরিচালনা করতে বাধ্য করে — কোনও নীরব ব্যর্থতা বা ভুলে যাওয়া ক্যাচ ব্লক নেই। ইডিওম্যাটিক প্যাটার্ন হল `if err != nil`। মোড়ানো ত্রুটির জন্য`%w`এর সাথে`fmt.Errorf`এবং ত্রুটির ধরন পরীক্ষা করার জন্য`errors.Is`/`errors.As`ব্যবহার করুন৷ পুনরুদ্ধারযোগ্য ত্রুটির জন্য (প্রোগ্রামিং বাগ),`panic`ব্যবহার করুন।
```go
func readConfig(path string) (Config, error) {
    data, err := os.ReadFile(path)
    if err != nil {
        return Config{}, fmt.Errorf("reading config %s: %w", path, err)
    }
    var cfg Config
    if err := json.Unmarshal(data, &cfg); err != nil {
        return Config{}, fmt.Errorf("parsing config %s: %w", path, err)
    }
    return cfg, nil
}
```

### প্রশ্ন 2: গরউটিনগুলি কী এবং কীভাবে তারা OS থ্রেড থেকে আলাদা?
**A:** গোরুটিনগুলি হালকা ওজনের, ব্যবহারকারী-স্পেস থ্রেডগুলি Go রানটাইম দ্বারা পরিচালিত হয়৷ এগুলি ~2KB স্ট্যাক দিয়ে শুরু হয় (OS থ্রেডের জন্য বনাম ~1MB), শিডিউলারের দ্বারা OS থ্রেডগুলিতে মাল্টিপ্লেক্স করা হয় এবং একবারে লক্ষ লক্ষ তৈরি করা যায়৷ গোরুটিনের মধ্যে যোগাযোগ চ্যানেল ব্যবহার করে (অথবা শেয়ার্ড স্টেটের জন্য`sync`আদিম)। গোরুটিন ফাঁস এড়াতে সর্বদা`sync.WaitGroup`বা প্রসঙ্গ বাতিলকরণ ব্যবহার করুন।
```go
// Launch thousands of goroutines — perfectly fine
var wg sync.WaitGroup
for i := 0; i < 10000; i++ {
    wg.Add(1)
    go func(id int) {
        defer wg.Done()
        process(id)
    }(i)
}
wg.Wait()
```

### প্রশ্ন 3: আমি কখন চ্যানেল বনাম মিউটেক্স ব্যবহার করব?
**A:** চ্যানেলগুলি ব্যবহার করুন যখন গোরুটিনের ডেটা যোগাযোগের প্রয়োজন হয় — তারা "যোগাযোগের মাধ্যমে মেমরি ভাগ করে নেওয়া" দর্শন প্রয়োগ করে৷ মিউটেক্স ব্যবহার করুন (`sync.Mutex`) যখন goroutineগুলিকে শেয়ার করা অবস্থা (ক্যাশে, কাউন্টার, সংযোগ পুল) রক্ষা করতে হবে। একটি ভাল নিয়ম: যদি গোরুটিনের মধ্যে ডেটা পাস করা হয় তবে চ্যানেলগুলি ব্যবহার করুন; যদি একাধিক গোরুটিন দ্বারা ডেটা অ্যাক্সেস করা হয় তবে একটি মিউটেক্স ব্যবহার করুন। সাধারণ পারমাণবিক অপারেশনের জন্য,`sync/atomic`ব্যবহার করুন।
```go
// Channel pattern — pipeline
func producer(nums chan<- int) {
    for i := 0; i < 10; i++ { nums <- i }
    close(nums)
}
func consumer(nums <-chan int, results chan<- int) {
    for n := range nums { results <- n * n }
    close(results)
}

// Mutex pattern — shared cache
type SafeCache struct {
    mu    sync.RWMutex
    items map[string]string
}
func (c *SafeCache) Get(key string) (string, bool) {
    c.mu.RLock()
    defer c.mu.RUnlock()
    v, ok := c.items[key]
    return v, ok
}
```

### প্রশ্ন 4:`nil`স্লাইস/মানচিত্র এবং খালিগুলির মধ্যে পার্থক্য কী?
**A:** একটি`nil`স্লাইস (`var s []int`) এর কোনো অন্তর্নিহিত অ্যারে নেই, দৈর্ঘ্য 0, ক্ষমতা 0। একটি খালি স্লাইস (`s := []int{}`বা`make([]int, 0)`) এর একটি অন্তর্নিহিত অ্যারে রয়েছে কিন্তু দৈর্ঘ্য 0। উভয়ই XZQZMARKER5 এর সাথে একইভাবে কাজ করে `len`, `cap`, এবং `range`। JSON মার্শালিং আলাদা: শূন্য স্লাইস`null`হয়ে যায়, খালি স্লাইস`[]`হয়ে যায়। সর্বোত্তম অনুশীলন: রিটার্ন মানের জন্য শূন্য স্লাইস পছন্দ করুন (তারা "কোন তথ্য নেই" নির্দেশ করে), খালি স্লাইস যখন JSON আউটপুট গুরুত্বপূর্ণ।
```go
var nilSlice []int          // nil, len=0, cap=0
emptySlice := []int{}       // not nil, len=0, cap=0

// Both work with append
nilSlice = append(nilSlice, 1)   // Now len=1
emptySlice = append(emptySlice, 1) // Now len=1

// JSON difference
json.Marshal(nilSlice)     // "null"
json.Marshal(emptySlice)   // "[]"
```

### প্রশ্ন 5: গো-তে ইন্টারফেসগুলি কীভাবে কাজ করে এবং খালি ইন্টারফেস কী?
**A:** Go ইন্টারফেসগুলি পরোক্ষভাবে সন্তুষ্ট হয় — একটি প্রকার`implements`কীওয়ার্ড ছাড়াই তার পদ্ধতিগুলি প্রয়োগ করে একটি ইন্টারফেস প্রয়োগ করে৷ এটি ডিকপলিং এবং কম্পোজিশন সক্ষম করে। খালি ইন্টারফেস`interface{}`(অথবা Go 1.18+ এ `any`) প্রতিটি প্রকারের দ্বারা সন্তুষ্ট — এটি সামান্য ব্যবহার করুন (জেনারিক প্রায়শই ভাল)। ইন্টারফেস মান জোড়া: `(type, value)`। একটি শূন্য ইন্টারফেস উভয়ই শূন্য।
```go
// Implicit interface satisfaction
type Writer interface {
    Write(p []byte) (n int, err error)
}

// MyWriter implements Writer without declaring it
type MyWriter struct { buf *bytes.Buffer }
func (w *MyWriter) Write(p []byte) (int, error) { return w.buf.Write(p) }

// Type assertion and type switch
func describe(i interface{}) string {
    switch v := i.(type) {
    case int:
        return fmt.Sprintf("integer: %d", v)
    case string:
        return fmt.Sprintf("string: %q", v)
    default:
        return fmt.Sprintf("unknown: %T", v)
    }
}
```

---

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: রেট লিমিটিং সহ একটি সমবর্তী ওয়েব স্ক্র্যাপার তৈরি করুন
**সমস্যা বিবৃতি:** একটি গো প্রোগ্রাম তৈরি করুন যা একই সাথে একটি তালিকা থেকে ইউআরএল নিয়ে আসে, পৃষ্ঠার শিরোনাম বের করে, প্রতি সেকেন্ডে 10 অনুরোধের হারের সীমাকে সম্মান করে এবং ডেটা রেস ছাড়াই ফলাফল সংগ্রহ করে।
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের প্রয়োজন: (1) গরউটিনগুলির সাথে সমসাময়িক HTTP আনা, (2) অপ্রতিরোধ্য সার্ভার এড়াতে হার সীমিত করা, (3) রেস ছাড়াই ফলাফল সংগ্রহ, (4) ব্যর্থ অনুরোধগুলির জন্য সঠিক ত্রুটি পরিচালনা। গো-এর সঙ্গতি আদিম (গোরুটিন, চ্যানেল,`errgroup`) এর জন্য আদর্শ।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- টোকেন-বালতি হার সীমিত করার জন্য`golang.org/x/time/rate`ব্যবহার করুন।
- গোরুটিনগুলি পরিচালনা করতে`sync.WaitGroup`বা`errgroup.Group`ব্যবহার করুন৷
- নিরাপদে আউটপুট সংগ্রহ করতে একটি ফলাফল চ্যানেল ব্যবহার করুন।
- বাতিলকরণ এবং সময়সীমার জন্য`context.Context`ব্যবহার করুন।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
```go
package main

import (
    "context"
    "fmt"
    "io"
    "net/http"
    "regexp"
    "sync"
    "time"

    "golang.org/x/sync/errgroup"
    "golang.org/x/time/rate"
)

type Result struct {
    URL   string
    Title string
    Error error
}

var titleRegex = regexp.MustCompile(`<title[^>]*>(.*?)</title>`)

func fetchTitle(ctx context.Context, client *http.Client, url string) Result {
    req, err := http.NewRequestWithContext(ctx, "GET", url, nil)
    if err != nil {
        return Result{URL: url, Error: err}
    }
    resp, err := client.Do(req)
    if err != nil {
        return Result{URL: url, Error: err}
    }
    defer resp.Body.Close()

    body, err := io.ReadAll(io.LimitReader(resp.Body, 1<<20)) // 1MB limit
    if err != nil {
        return Result{URL: url, Error: err}
    }

    matches := titleRegex.FindSubmatch(body)
    if matches == nil {
        return Result{URL: url, Title: "(no title)"}
    }
    return Result{URL: url, Title: string(matches[1])}
}

func scrapeAll(ctx context.Context, urls []string, rps int) []Result {
    limiter := rate.NewLimiter(rate.Limit(rps), rps)
    client := &http.Client{Timeout: 10 * time.Second}
    results := make([]Result, len(urls))

    g, ctx := errgroup.WithContext(ctx)
    g.SetLimit(20) // Max 20 concurrent goroutines

    for i, url := range urls {
        i, url := i, url // Capture loop variables
        g.Go(func() error {
            if err := limiter.Wait(ctx); err != nil {
                return err
            }
            results[i] = fetchTitle(ctx, client, url)
            return nil
        })
    }

    if err := g.Wait(); err != nil {
        fmt.Fprintf(os.Stderr, "Error: %v\n", err)
    }
    return results
}
```

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- কোনও ডেটা রেস নেই: প্রতিটি গোরুটিন `results`-এ নিজস্ব সূচকে লেখে — কোনও মিউটেক্সের প্রয়োজন নেই।
-`errgroup.SetLimit`রেট লিমিটার থেকে স্বাধীনভাবে সঙ্গতি সীমাবদ্ধ করে।
-`io.LimitReader`অত্যধিক বড় পৃষ্ঠা পড়তে বাধা দেয়।
-`http.NewRequestWithContext`নিশ্চিত করে যে প্রসঙ্গটি সম্পন্ন হলে অনুরোধগুলি বাতিল করা হয়েছে৷
- উৎপাদনের জন্য: সূচকীয় ব্যাকঅফ, সংযোগ পুলিং টিউনিং এবং মেট্রিক্স সহ পুনরায় চেষ্টা যুক্তি যোগ করুন।
### সমস্যা 2: একটি জেনেরিক LRU ক্যাশে প্রয়োগ করুন
**সমস্যা বিবৃতি:** জেনেরিক (Go 1.18+) ব্যবহার করে গো-তে একটি থ্রেড-সেফ, জেনেরিক এলআরইউ (সর্বনিম্ন সম্প্রতি ব্যবহৃত) ক্যাশে প্রয়োগ করুন। এটি O(1) সময়ের জটিলতার সাথে`Get`,`Set`, এবং`Delete`সমর্থন করবে৷
**ধাপ 1 — সমস্যাটি বুঝুন:**
একটি LRU ক্যাশের জন্য প্রয়োজন O(1) লুকআপ (হ্যাশ ম্যাপ) এবং O(1) অর্ডার আপডেট (দ্বিগুণ লিঙ্কযুক্ত তালিকা)।`Get`এ: আইটেমটিকে সামনে নিয়ে যান।`Set`এ: সামনে সন্নিবেশ করান; ক্ষমতার বেশি হলে পিছন থেকে উচ্ছেদ করুন। থ্রেড নিরাপত্তা একটি mutex প্রয়োজন.
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- O(1) এর জন্য`container/list`(দ্বিগুণ লিঙ্কযুক্ত তালিকা) ব্যবহার করুন সামনের দিকে সরান এবং পিছনে থেকে সরিয়ে দিন।
- O(1) লুকআপের জন্য`map[K]*list.Element`ব্যবহার করুন।
- থ্রেড নিরাপত্তার জন্য`sync.Mutex`ব্যবহার করুন।
- প্রকার নিরাপত্তার জন্য জেনেরিক (`[K comparable, V any]`)।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
```go
type entry[K comparable, V any] struct {
    key   K
    value V
}

type LRUCache[K comparable, V any] struct {
    capacity int
    items    map[K]*list.Element
    order    *list.List
    mu       sync.Mutex
}

func NewLRU[K comparable, V any](capacity int) *LRUCache[K, V] {
    return &LRUCache[K, V]{
        capacity: capacity,
        items:    make(map[K]*list.Element),
        order:    list.New(),
    }
}

func (c *LRUCache[K, V]) Get(key K) (V, bool) {
    c.mu.Lock()
    defer c.mu.Unlock()

    if elem, ok := c.items[key]; ok {
        c.order.MoveToFront(elem)
        return elem.Value.(*entry[K, V]).value, true
    }
    var zero V
    return zero, false
}

func (c *LRUCache[K, V]) Set(key K, value V) {
    c.mu.Lock()
    defer c.mu.Unlock()

    if elem, ok := c.items[key]; ok {
        c.order.MoveToFront(elem)
        elem.Value.(*entry[K, V]).value = value
        return
    }

    if c.order.Len() >= c.capacity {
        oldest := c.order.Back()
        if oldest != nil {
            c.order.Remove(oldest)
            delete(c.items, oldest.Value.(*entry[K, V]).key)
        }
    }

    e := &entry[K, V]{key: key, value: value}
    elem := c.order.PushFront(e)
    c.items[key] = elem
}

func (c *LRUCache[K, V]) Delete(key K) bool {
    c.mu.Lock()
    defer c.mu.Unlock()

    if elem, ok := c.items[key]; ok {
        c.order.Remove(elem)
        delete(c.items, key)
        return true
    }
    return false
}

func (c *LRUCache[K, V]) Len() int {
    c.mu.Lock()
    defer c.mu.Unlock()
    return c.order.Len()
}
```

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
-`Get`,`Set`,`Delete`এর জন্য O(1): মানচিত্রের সন্ধান হল O(1) গড়; তালিকা অপারেশনগুলি (`MoveToFront`,`PushFront`,`Remove`,`Back`) হল সমস্ত O(1)৷
- থ্রেড নিরাপত্তা:`sync.Mutex`নিশ্চিত করে যে একবারে শুধুমাত্র একটি গোরুটিন ক্যাশে অ্যাক্সেস করে। পড়া-ভারী কাজের চাপের জন্য,`sync.RWMutex`ব্যবহার করুন।
- জেনেরিক:`[K comparable, V any]`নিশ্চিত করে কী সমর্থন করে`==`(মানচিত্র কীগুলির জন্য প্রয়োজনীয়) যখন মানগুলি যে কোনও ধরণের হতে পারে৷
- উত্পাদন:`github.com/hashicorp/golang-lru/v2`বিবেচনা করুন — TTL সমর্থন এবং কম লক বিরোধের জন্য শার্ডিংয়ের সাথে যুদ্ধ-পরীক্ষিত।
### সমস্যা 3: একটি TCP চ্যাট সার্ভার তৈরি করুন
**সমস্যা বিবৃতি:** একটি সমসাময়িক TCP চ্যাট সার্ভার তৈরি করুন যেখানে ক্লায়েন্টরা সংযোগ করতে পারে, অন্য সমস্ত সংযুক্ত ক্লায়েন্টদের কাছে বার্তা সম্প্রচার করতে পারে এবং সুন্দরভাবে সংযোগ বিচ্ছিন্ন করতে পারে। অন্যদের ব্লক না করে ধীরগতির ক্লায়েন্টদের হ্যান্ডেল করুন।
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের প্রয়োজন: (1) টিসিপি সংযোগ গ্রহণ করুন, (2) পড়ার জন্য প্রতি ক্লায়েন্টের জন্য একটি গোরুটিন, (3) সমস্ত ক্লায়েন্টকে বার্তা পাঠানোর জন্য একটি সম্প্রচার ব্যবস্থা, (4) সংযোগ বিচ্ছিন্ন করা এবং ধীর ক্লায়েন্টদের পরিচালনা করা। এটি একটি ক্লাসিক ফ্যান-আউট প্যাটার্ন।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- TCP সংযোগের জন্য`net.Listener`ব্যবহার করুন।
- ক্লায়েন্ট রেজিস্ট্রেশন/রেজিস্ট্রেশন/সম্প্রচারের জন্য চ্যানেলগুলির সাথে একটি কেন্দ্রীয়`hub`গোরুটিন ব্যবহার করুন৷
- প্রতিটি ক্লায়েন্ট একটি বাফার করা চ্যানেলের সাথে একটি ডেডিকেটেড লেখার গোরুটিন পায় — ধীর ক্লায়েন্টরা অন্যদের ব্লক করে না।
- সুন্দর শাটডাউনের জন্য`context.Context`ব্যবহার করুন।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
```go
package main

import (
    "bufio"
    "fmt"
    "log"
    "net"
    "sync"
)

type Client struct {
    conn net.Conn
    name string
    send chan string
}

type Hub struct {
    clients    map[*Client]bool
    broadcast  chan string
    register   chan *Client
    unregister chan *Client
    mu         sync.RWMutex
}

func NewHub() *Hub {
    return &Hub{
        clients:    make(map[*Client]bool),
        broadcast:  make(chan string, 256),
        register:   make(chan *Client),
        unregister: make(chan *Client),
    }
}

func (h *Hub) Run() {
    for {
        select {
        case client := <-h.register:
            h.mu.Lock()
            h.clients[client] = true
            h.mu.Unlock()
            h.broadcast <- fmt.Sprintf("[system] %s joined", client.name)

        case client := <-h.unregister:
            h.mu.Lock()
            if _, ok := h.clients[client]; ok {
                delete(h.clients, client)
                close(client.send)
            }
            h.mu.Unlock()
            h.broadcast <- fmt.Sprintf("[system] %s left", client.name)

        case msg := <-h.broadcast:
            h.mu.RLock()
            for client := range h.clients {
                select {
                case client.send <- msg:
                default:
                    // Slow client — disconnect
                    go func(c *Client) {
                        h.unregister <- c
                        c.conn.Close()
                    }(client)
                }
            }
            h.mu.RUnlock()
        }
    }
}

func handleClient(hub *Hub, conn net.Conn) {
    defer conn.Close()
    scanner := bufio.NewScanner(conn)

    // Read first line as name
    if !scanner.Scan() { return }
    name := scanner.Text()

    client := &Client{
        conn: conn,
        name: name,
        send: make(chan string, 64),
    }
    hub.register <- client
    defer func() { hub.unregister <- client }()

    // Write goroutine
    go func() {
        for msg := range client.send {
            fmt.Fprintf(conn, "%s\n", msg)
        }
    }()

    // Read loop
    for scanner.Scan() {
        text := scanner.Text()
        hub.broadcast <- fmt.Sprintf("[%s] %s", name, text)
    }
}

func main() {
    hub := NewHub()
    go hub.Run()

    listener, err := net.Listen("tcp", ":8080")
    if err != nil { log.Fatal(err) }
    log.Println("Chat server listening on :8080")

    for {
        conn, err := listener.Accept()
        if err != nil { log.Println(err); continue }
        go handleClient(hub, conn)
    }
}
```

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- ধীরগতির ক্লায়েন্ট হ্যান্ডলিং: সম্প্রচারে`select`সহ`default`ব্লক করা প্রতিরোধ করে৷ ধীরগতির ক্লায়েন্টদের বাফার পূর্ণ হলে সংযোগ বিচ্ছিন্ন করা হয়।
- কোন রেস নেই: হাব গোরুটিন হল`clients`মানচিত্রের একক লেখক; `mu`সম্প্রচারের সময় পঠন রক্ষা করে।
- সুন্দর শাটডাউন: শ্রোতা এবং ড্রেন সংযোগ বন্ধ করতে`context.Context`এবং একটি সংকেত হ্যান্ডলার যোগ করুন।
- উত্পাদন: ব্রাউজার ক্লায়েন্টদের জন্য`golang.org/x/net/websocket`ব্যবহার করার কথা বিবেচনা করুন এবং প্রমাণীকরণ, বার্তা ইতিহাস এবং রুম যোগ করুন।
---

## সারাংশ
গো এমন একটি ভাষা যা ইচ্ছাকৃতভাবে বৈশিষ্ট্যের চেয়ে সরলতা বেছে নেয়। বেশিরভাগ ভাষার তুলনায় এটির কম গঠন রয়েছে -- কোনো উত্তরাধিকার নেই, কোনো পদ্ধতি ওভারলোডিং নেই, কোনো ব্যতিক্রম নেই, কোনো ম্যাক্রো নেই -- এবং এটি একটি শক্তি। ফলাফল হল কোড যা পড়া সহজ, লিখতে সহজ এবং বজায় রাখা সহজ। Go-এর কনকারেন্সি মডেল (গোরুটিন এবং চ্যানেল) যে কোনো ভাষায় সেরা ডিজাইন করা হয়। ক্লাউড অবকাঠামো, মাইক্রোসার্ভিস, সিএলআই টুলস এবং নেটওয়ার্ক প্রোগ্রামিংয়ের জন্য, গো একটি চমৎকার পছন্দ।