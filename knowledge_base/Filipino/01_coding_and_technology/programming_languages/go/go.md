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
# Go
Ang Go (kadalasang tinatawag na "Golang" pagkatapos ng orihinal nitong domain name) ay isang statically typed, compiled programming language na dinisenyo sa Google nina Robert Griesemer, Rob Pike, at Ken Thompson. Una itong inilabas noong 2012 na may tahasang layunin na maging isang mas mahusay na wika para sa mga system programming -- isa na pinagsasama ang pagganap ng C sa pagiging produktibo ng mga dynamic na wika tulad ng Python. Kilala ang Go sa pagiging simple nito, mabilis na compilation, built-in na concurrency (goroutine at channel), at mahusay na tooling.
Pinapalakas ng Go ang karamihan sa ecosystem ng imprastraktura ng ulap: Ang Docker, Kubernetes, Terraform, Prometheus, etcd, at ang HTTP server ng Go standard library ay nakasulat lahat sa Go. Ito ay naging default na wika para sa cloud-native development, microservices, at CLI tool.
---

## Bakit Mahalaga ang Go
- **Pagiging simple ayon sa disenyo**: May 25 keyword lang ang Go. Ang wika ay sadyang maliit at madaling matutunan.
- **Mabilis na compilation**: Direktang nagko-compile sa machine code sa ilang segundo, kahit para sa malalaking proyekto.
- **Built-in concurrency**: Ginagawang accessible at mahusay ng mga Goroutine at channel ang magkasabay na programming.
- **Mahusay na karaniwang library**: HTTP server, JSON encoding, testing, cryptography -- built in lahat.
- **Mga static na binary**: Nag-compile sa isang binary na walang mga external na dependency. Ang deployment ay walang halaga.
- **Google-scale pedigree**: Dinisenyo ng mga inhinyero na bumuo ng Unix, UTF-8, at karamihan sa imprastraktura ng Google.
## Ang mga Trade-off
| Limitasyon | Mga Detalye | Karaniwang Workaround |
|-----------|---------|-------------------|
| **Walang mga uri ng kabuuan / pagtutugma ng pattern** | Walang mga enum na may nauugnay na data, walang mga uri ng algebraic | Gumamit ng mga interface at uri ng switch |
| **Error sa paghawak ng verbosity** | Tahasang kung mali != nil check sa lahat ng dako | Tanggapin ang pattern; ginagawa nitong nakikita ang paghawak ng error |
| **Mas maliit na ecosystem** | Mas kaunting mga aklatan kaysa sa Python, Java, o JavaScript | Ang karaniwang aklatan ay sumasaklaw sa karamihan ng mga pangangailangan; lumalaki ang mga pakete ng komunidad |
| **Walang GUI framework** | Hindi angkop para sa desktop o mobile na mga UI | Gumamit ng mga web-based na UI (WASM) o ibang wika |
| **Basura** | May GC -- maliit ang mga pag-pause ngunit hindi zero | I-tune ang GC para sa mga latency-sensitive na workload; gamitin ang sync.Pool |
---

## Syntax Fundamentals
### Pangunahing Istruktura
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

### Mga Pag-andar
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

### Mga Struct at Interface
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

### Error sa Paghawak
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

### Concurrency -- Mga Goroutine at Channel
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

## Advanced na Syntax at Mga Pattern
### Generics (Go 1.18+)
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

### Advanced na Pagtutugma ng Pattern (Mga Lilipat ng Uri)
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

### Custom Error Wrapping
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

## Concurrency at Parallelism (Deep Dive)
### Pattern ng Worker Pool
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

### Konteksto para sa Pagkansela
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

### Pumili para sa Multiplexing
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

## Project Configuration at Build System
### Istraktura ng Proyekto
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

### Mahahalagang Utos
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

### CI/CD Pipeline (GitHub Actions)
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

## Pagsubok
### Mga Pagsusuri sa Yunit
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

### Mga Pagsusuri sa HTTP na Batay sa Talahanayan
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

## Interoperability
### CGo (Tinatawag si C mula kay Go)
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

### FFI kasama ang Iba pang mga Wika
| Direksyon | Mekanismo |
|-----------|-----------|
| Tawagan si C | cgo (`import "C"`) |
| Tumawag sa C++ | cgo + C wrapper function |
| C tumatawag sa Go | I-export ang mga function ng Go na may`//export`|
| Tumawag sa Python | Gumamit ng gopy o subprocess |
---

## Mga Pattern ng Disenyo
### Pattern ng Middleware (HTTP)
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

### Pattern ng Mga Pagpipilian
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

## Pagganap at Pag-optimize
### Pag-profile
```bash
go test -cpuprofile=cpu.prof -bench=. ./...
go tool pprof cpu.prof
go test -memprofile=mem.prof -bench=. ./...
go tool pprof mem.prof
```

### Mga Tip sa Pag-optimize
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

## Deployment
### Cross-Compilation
```bash
GOOS=linux GOARCH=amd64 go build -o myapp-linux
GOOS=windows GOARCH=amd64 go build -o myapp.exe
GOOS=darwin GOARCH=arm64 go build -o myapp-mac
```

### Docker Deployment
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

## Ang Standard Library
| Package | Layunin |
|---------|---------|
| fmt | Naka-format na I/O |
| net/http | HTTP client at server |
| encoding/json | JSON encoding/decoding |
| os | Mga operasyon sa antas ng OS |
| io | I/O primitives |
| mga string / strconv | Pagmamanipula ng string |
| i-sync | Mutex, WaitGroup, Minsan |
| konteksto | Mga deadline, pagkansela |
| pagsubok | Built-in na balangkas ng pagsubok |
| log / log/slog | Pag-log |
| oras | Oras at tagal |
| crypto | Cryptography (TLS, hashing) |
| database/sql | abstraction ng database |
---

## Tooling
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

## Kailan Gamitin ang Go
| Sitwasyon | Bakit Pumunta | Mas mahusay na Alternatibo |
|----------|--------|--------------------|
| Cloud-native na serbisyo / microservices | Mabilis, maliliit na binary, mahusay na HTTP | kalawang para sa maximum na pagganap |
| Mga tool sa CLI | Mabilis na compilation, single binary | kalawang para sa mga kumplikadong CLI |
| Mga web server / API | Built-in na HTTP, mabilis, simple | Node.js/Express para sa mabilis na prototyping |
| DevOps tooling | Docker, Kubernetes, Terraform ay Go | Python para sa scripting |
| Kasabay na mga sistema | Ang mga Goroutine ay magaan at eleganteng | Erlang/Elixir para sa fault-tolerant concurrency |
| Network programming | Napakahusay na net package | C/C++ para sa pinakamababang antas ng kontrol |
| Data science / ML | Hindi ang tamang ecosystem | Python, R |
| Desktop/mobile GUI | Walang balangkas ng GUI | Gumamit ng web frontend o katutubong wika |
| Mga naka-embed na system | Masyadong mabigat (GC, runtime) | C, kalawang |
---

## Synthetic na Q&A
### Q1: Bakit walang mga exception ang Go? Paano ko dapat panghawakan ang mga error?
**S:** Gumagamit si Go ng tahasang pagbabalik ng error sa halip na mga exception. Bawat function na maaaring mabigo ay nagbabalik ng`error`bilang huling halaga ng pagbabalik nito. Pinipilit nito ang tumatawag na hawakan ang mga error nang tahasan — walang tahimik na pagkabigo o nakalimutang catch block. Ang idiomatic pattern ay`if err != nil`. Gumamit ng`fmt.Errorf`na may`%w`para sa mga error sa pagbabalot, at`errors.Is`/`errors.As`para sa pagsuri sa mga uri ng error. Para sa mga hindi mababawi na error (programming bug), gamitin ang`panic`.
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

### Q2: Ano ang mga goroutine, at paano sila naiiba sa mga OS thread?
**A:** Ang mga Goroutine ay magaan, mga thread ng user-space na pinamamahalaan ng runtime ng Go. Nagsisimula ang mga ito sa ~2KB ng stack (kumpara sa ~1MB para sa mga OS thread), ay multiplexed sa mga OS thread ng scheduler, at maaaring gawin ng milyun-milyon sa isang pagkakataon. Ang komunikasyon sa pagitan ng mga goroutines ay gumagamit ng mga channel (o`sync`primitives para sa shared state). Palaging gumamit ng`sync.WaitGroup`o pagkansela ng konteksto upang maiwasan ang mga pagtagas ng goroutine.
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

### Q3: Kailan ko dapat gamitin ang mga channel vs mutex para sa concurrency?
**A:** Gumamit ng mga channel kapag kailangan ng mga goroutine na makipag-ugnayan ng data — ipinapatupad nila ang pilosopiyang "magbahagi ng memorya sa pamamagitan ng pakikipag-usap." Gumamit ng mga mutex (`sync.Mutex`) kapag kailangan ng mga goroutine na protektahan ang nakabahaging estado (mga cache, counter, mga pool ng koneksyon). Isang magandang panuntunan: kung ang data ay ipinapasa sa pagitan ng mga goroutine, gumamit ng mga channel; kung ang data ay ina-access ng maraming goroutine, gumamit ng mutex. Para sa simpleng atomic operations, gamitin ang`sync/atomic`.
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

### Q4: Ano ang pagkakaiba sa pagitan ng mga hiwa/mapa ng`nil`at mga walang laman?
**A:** Ang isang`nil`slice (`var s []int`) ay walang pinagbabatayan na array, haba 0, kapasidad 0. Ang isang walang laman na slice (`s := []int{}`o`make([]int, 0)`) ay may pinagbabatayan na array ngunit ang haba ay 0. Parehong gumagana ang parehong`append`, XXZQZMAR, at XQZQZMAR`range`. Naiiba ang JSON marshaling: ang nil slice ay nagiging`null`, ang mga walang laman na slice ay nagiging`[]`. Pinakamahusay na kasanayan: mas gusto ang nil slice para sa mga return value (ipinapahiwatig nila ang "walang data"), mga walang laman na slice kapag mahalaga ang output ng JSON.
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

### Q5: Paano gumagana ang mga interface sa Go, at ano ang walang laman na interface?
**A:** Ang mga interface ng Go ay ganap na nasisiyahan — ang isang uri ay nagpapatupad ng isang interface sa pamamagitan ng pagpapatupad ng mga pamamaraan nito, na walang`implements`na keyword. Ito ay nagbibigay-daan sa decoupling at komposisyon. Ang walang laman na interface na`interface{}`(o`any`sa Go 1.18+) ay nasisiyahan sa bawat uri — gamitin ito nang matipid (madalas na mas mahusay ang mga generic). Ang mga halaga ng interface ay mga pares:`(type, value)`. Ang isang nil interface ay pareho bilang nil.
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

## Paglutas ng Problema ng Chain-of-Thought
### Problema 1: Bumuo ng Kasabay na Web Scraper na may Paglilimita sa Rate
**Pahayag ng Problema:** Bumuo ng programang Go na kumukuha ng mga URL mula sa isang listahan nang sabay-sabay, kumukuha ng mga pamagat ng page, nirerespeto ang limitasyon sa rate na 10 kahilingan sa bawat segundo, at nangongolekta ng mga resulta nang walang mga karera ng data.
**Hakbang 1 — Unawain ang Problema:**
Kailangan namin ng: (1) sabay-sabay na pagkuha ng HTTP na may mga goroutine, (2) paglilimita sa rate para maiwasan ang napakaraming server, (3) pangongolekta ng resulta nang walang mga karera, (4) wastong paghawak ng error para sa mga nabigong kahilingan. Ang mga concurrency primitives ng Go (goroutines, channel,`errgroup`) ay mainam para dito.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Gamitin ang`golang.org/x/time/rate`para sa paglilimita sa rate ng token-bucket.
- Gamitin ang`sync.WaitGroup`o`errgroup.Group`upang pamahalaan ang mga goroutine.
- Gumamit ng channel ng mga resulta upang ligtas na mangolekta ng mga output.
- Gamitin ang`context.Context`para sa pagkansela at mga timeout.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Walang mga karera ng data: nagsusulat ang bawat goroutine sa sarili nitong index sa`results`— walang mutex na kailangan.
-`errgroup.SetLimit`bounds concurrency nang hiwalay sa rate limiter.
- Pinipigilan ng`io.LimitReader`ang pagbabasa ng labis na malalaking pahina.
- Tinitiyak ng`http.NewRequestWithContext`na nakansela ang mga kahilingan kapag tapos na ang konteksto.
- Para sa produksyon: magdagdag ng retry logic na may exponential backoff, connection pooling tuning, at mga sukatan.
### Problema 2: Magpatupad ng Generic LRU Cache
**Problem Statement:** Magpatupad ng thread-safe, generic na LRU (Least Recently Used) cache sa Go gamit ang generics (Go 1.18+). Dapat itong suportahan ang`Get`,`Set`, at`Delete`na may O(1) na pagiging kumplikado ng oras.
**Hakbang 1 — Unawain ang Problema:**
Ang LRU cache ay nangangailangan ng O(1) lookup (hash map) at O(1) pag-order ng mga update (double linked list). Sa`Get`: ilipat ang item sa harap. Sa`Set`: ipasok sa harap; paalisin sa likod kung sobra sa kapasidad. Ang kaligtasan ng thread ay nangangailangan ng mutex.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Gumamit ng`container/list`(double linked list) para sa O(1) na paglipat-sa-harap at alisin-sa-likod.
- Gamitin ang`map[K]*list.Element`para sa O(1) lookup.
- Gamitin ang`sync.Mutex`para sa kaligtasan ng thread.
- Generics (`[K comparable, V any]`) para sa kaligtasan ng uri.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- O(1) para sa`Get`,`Set`,`Delete`: ang paghahanap ng mapa ay O(1) average; mga pagpapatakbo ng listahan (`MoveToFront`,`PushFront`,`Remove`,`Back`) lahat ay O(1).
- Kaligtasan ng thread: Tinitiyak ng`sync.Mutex`na isang goroutine lang ang makaka-access sa cache sa bawat pagkakataon. Para sa mga read-heavy workloads, gamitin ang`sync.RWMutex`.
- Generics: Tinitiyak ng`[K comparable, V any]`na sinusuportahan ng mga key ang`==`(kinakailangan para sa mga key ng mapa) habang ang mga value ay maaaring anumang uri.
- Produksyon: isaalang-alang ang`github.com/hashicorp/golang-lru/v2`— nasubok sa labanan na may suporta sa TTL at sharding para sa pinababang pagtatalo sa lock.
### Problema 3: Bumuo ng TCP Chat Server
**Pahayag ng Problema:** Bumuo ng kasabay na TCP chat server kung saan maaaring kumonekta ang mga kliyente, mag-broadcast ng mga mensahe sa lahat ng iba pang konektadong kliyente, at magaling na magdiskonekta. Pangasiwaan ang mga mabagal na kliyente nang hindi hinaharangan ang iba.
**Hakbang 1 — Unawain ang Problema:**
Kailangan namin ng: (1) tumanggap ng mga koneksyon sa TCP, (2) isang goroutine bawat kliyente para sa pagbabasa, (3) isang mekanismo ng pagsasahimpapawid upang magpadala ng mga mensahe sa lahat ng mga kliyente, (4) paghawak ng mga disconnection at mabagal na mga kliyente. Ito ay isang klasikong fan-out pattern.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Gumamit ng`net.Listener`para sa mga koneksyon sa TCP.
- Gumamit ng sentral na`hub`goroutine na may mga channel para sa pagpaparehistro/pag-deregister/pag-broadcast ng kliyente.
- Ang bawat kliyente ay nakakakuha ng nakalaang write goroutine na may buffered channel — ang mga mabagal na kliyente ay hindi humaharang sa iba.
- Gamitin ang`context.Context`para sa magandang pagsara.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Mabagal na paghawak ng kliyente: pinipigilan ng`select`na may`default`sa broadcast ang pagharang. Ang mga mabagal na kliyente ay madidiskonekta kung mapupuno ang kanilang buffer.
- Walang mga karera: ang hub goroutine ay ang nag-iisang manunulat sa mapa ng `clients`;  Pinoprotektahan ng`mu`ang mga nabasa habang nag-broadcast.
- Mahusay na pagsara: magdagdag ng`context.Context`at isang tagapangasiwa ng signal upang isara ang tagapakinig at maubos ang mga koneksyon.
- Produksyon: isaalang-alang ang paggamit ng`golang.org/x/net/websocket`para sa mga kliyente ng browser, at magdagdag ng pagpapatunay, kasaysayan ng mensahe, at mga silid.
---

## Buod
Ang Go ay isang wika na sadyang pinipili ang pagiging simple kaysa sa mga feature. Ito ay may mas kaunting mga konstruksyon kaysa sa karamihan ng mga wika -- walang mana, walang paraan ng overloading, walang eksepsiyon, walang macro -- at ito ay isang lakas. Ang resulta ay code na madaling basahin, madaling isulat, at madaling mapanatili. Ang concurrency model ni Go (goroutine at channels) ay isa sa pinakamahusay na disenyo sa anumang wika. Para sa cloud infrastructure, microservices, CLI tools, at network programming, ang Go ay isang mahusay na pagpipilian.