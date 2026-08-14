---
# Metadata
title: "Go"
description: "Comprehensive reference for the Go programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
    date: "2026-08-05"
    author: "AI Model Training Team"
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

#جاؤ
گو (جسے اکثر اس کے اصل ڈومین نام کے بعد "گولانگ" کہا جاتا ہے) ایک مستحکم طور پر ٹائپ شدہ، مرتب کردہ پروگرامنگ لینگویج ہے جو گوگل پر رابرٹ گریزیمر، روب پائیک اور کین تھامسن نے ڈیزائن کی ہے۔ یہ پہلی بار 2012 میں سسٹم پروگرامنگ کے لیے ایک بہتر زبان ہونے کے واضح ہدف کے ساتھ جاری کیا گیا تھا -- ایک جو C کی کارکردگی کو Python جیسی متحرک زبانوں کی پیداواری صلاحیت کے ساتھ جوڑتی ہے۔ گو اپنی سادگی، تیز تالیف، بلٹ ان کنکرنسی (گوروٹینز اور چینلز) اور بہترین ٹولنگ کے لیے جانا جاتا ہے۔
گو کلاؤڈ انفراسٹرکچر ایکو سسٹم کے زیادہ تر حصے کو طاقت دیتا ہے: Docker، Kubernetes، Terraform، Prometheus، etcd، اور Go اسٹینڈرڈ لائبریری کے HTTP سرور سبھی Go میں لکھے گئے ہیں۔ یہ کلاؤڈ-آبائی ترقی، مائیکرو سروسز، اور CLI ٹولز کے لیے پہلے سے طے شدہ زبان بن گئی ہے۔
---

## کیوں جانا پڑتا ہے۔
- **ڈیزائن کے لحاظ سے سادگی**: Go میں صرف 25 کلیدی الفاظ ہیں۔ زبان جان بوجھ کر چھوٹی اور سیکھنے میں آسان ہے۔
- **تیز تالیف**: سیکنڈوں میں براہ راست مشین کوڈ پر مرتب کرتا ہے، یہاں تک کہ بڑے پروجیکٹس کے لیے بھی۔
- **بلٹ ان کنکرنسی**: گوروٹینز اور چینلز سمورتی پروگرامنگ کو قابل رسائی اور موثر بناتے ہیں۔
- **بہترین معیاری لائبریری**: HTTP سرور، JSON انکوڈنگ، ٹیسٹنگ، خفیہ نگاری -- سب بلٹ ان۔
- **سٹیٹک بائنریز**: بغیر کسی بیرونی انحصار کے ایک واحد بائنری میں مرتب کرتا ہے۔ تعیناتی معمولی ہے۔
- **گوگل پیمانہ **: ان انجینئرز کے ذریعہ ڈیزائن کیا گیا جنہوں نے یونکس، UTF-8، اور گوگل کا زیادہ تر انفراسٹرکچر بنایا۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **کوئی قسم کی رقم / پیٹرن کی مماثلت نہیں** | متعلقہ اعداد و شمار کے ساتھ کوئی اینوم نہیں، کوئی الجبری قسم نہیں | انٹرفیس استعمال کریں اور سوئچ ٹائپ کریں |
| **فعلیت کو سنبھالنے میں خرابی** | اگر غلطی ہو تو واضح کریں != ہر جگہ صفر چیک کرتا ہے | پیٹرن کو قبول کریں؛ یہ غلطی سے نمٹنے کو نظر آتا ہے |
| **چھوٹا ماحولیاتی نظام** | Python، Java، یا JavaScript سے کم لائبریریاں | معیاری لائبریری زیادہ تر ضروریات کا احاطہ کرتی ہے۔ کمیونٹی پیکجز بڑھ رہے ہیں |
| **کوئی GUI فریم ورک نہیں** | ڈیسک ٹاپ یا موبائل UIs کے لیے موزوں نہیں ہے | ویب پر مبنی UIs (WASM) یا دوسری زبان استعمال کریں۔
| **کوڑا اٹھانے والا** | ایک GC ہے -- توقف چھوٹے ہیں لیکن غیر صفر | تاخیر سے متعلق حساس کام کے بوجھ کے لیے جی سی کو ٹیون کریں۔ استعمال کریں sync.Pool |
---

## نحوی بنیادی باتیں
### بنیادی ڈھانچہ
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

### افعال
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

### ڈھانچے اور انٹرفیس
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

### نقص کو ہینڈل کرنا
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

### ہم آہنگی -- گوروٹینز اور چینلز
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

## اعلی درجے کی نحو اور نمونے۔
### عمومیات (1.18+ پر جائیں)
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

### ایڈوانسڈ پیٹرن میچنگ (قسم سوئچز)
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

### کسٹم ایرر ریپنگ
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

## ہم آہنگی اور ہم آہنگی (گہرا غوطہ)
### ورکر پول پیٹرن
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

### منسوخی کے لیے سیاق و سباق
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

### ملٹی پلیکسنگ کے لیے منتخب کریں۔
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### پروجیکٹ کا ڈھانچہ
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

### ضروری احکام
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

### CI/CD پائپ لائن (GitHub ایکشنز)
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

## ٹیسٹنگ
### یونٹ ٹیسٹ
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

### ٹیبل سے چلنے والے HTTP ٹیسٹ
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

## انٹرآپریبلٹی
### CGo (C کو Go سے کال کرنا)
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

### دیگر زبانوں کے ساتھ FFI
| سمت | میکانزم |
|------------|------------|
| C کال کرنے جاؤ | cgo (`import "C"`) |
| C++ | کال کریں۔ cgo + C ریپر فنکشنز |
| C کالنگ گو |`//export`کے ساتھ گو فنکشنز کو ایکسپورٹ کریں۔
| Python کو کال کرنے جاؤ | گوپی یا ذیلی عمل کا استعمال کریں |
---

## ڈیزائن پیٹرن
### مڈل ویئر پیٹرن (HTTP)
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

### اختیارات کا پیٹرن
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

## کارکردگی اور اصلاح
### پروفائلنگ
```bash
go test -cpuprofile=cpu.prof -bench=. ./...
go tool pprof cpu.prof
go test -memprofile=mem.prof -bench=. ./...
go tool pprof mem.prof
```

### اصلاح کی تجاویز
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

## تعیناتی۔
### کراس تالیف
```bash
GOOS=linux GOARCH=amd64 go build -o myapp-linux
GOOS=windows GOARCH=amd64 go build -o myapp.exe
GOOS=darwin GOARCH=arm64 go build -o myapp-mac
```

### ڈاکر کی تعیناتی۔
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

## معیاری لائبریری
| پیکیج | مقصد |
|---------|---------|
| fmt | فارمیٹ شدہ I/O |
| net/http | HTTP کلائنٹ اور سرور |
| انکوڈنگ/json | JSON انکوڈنگ/ڈی کوڈنگ |
| os | OS سطح کے آپریشنز |
| io | I/O قدیم |
| strings / strconv | سٹرنگ ہیرا پھیری |
| مطابقت پذیری | Mutex، WaitGroup، ایک بار |
| سیاق و سباق | ڈیڈ لائن، منسوخی |
| ٹیسٹنگ | بلٹ ان ٹیسٹنگ فریم ورک |
| log/log/slog | لاگنگ |
| وقت | وقت اور دورانیہ |
| کرپٹو | خفیہ نگاری (TLS، hashing) |
| database/sql | ڈیٹا بیس خلاصہ |
---

## ٹولنگ
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

## Go کب استعمال کریں۔
| منظر نامہ | کیوں جاؤ | بہتر متبادل |
|------------|---------|-------------------|
| کلاؤڈ مقامی خدمات / مائیکرو سروسز | تیز، چھوٹی بائنریز، بہترین HTTP | زیادہ سے زیادہ کارکردگی کے لیے مورچا |
| CLI ٹولز | تیز تالیف، واحد بائنری | پیچیدہ CLIs کے لیے مورچا |
| ویب سرورز / APIs | بلٹ ان HTTP، تیز، سادہ | تیزی سے پروٹو ٹائپنگ کے لیے Node.js/Express |
| DevOps ٹولنگ | Docker، Kubernetes، Terraform ہیں Go | اسکرپٹنگ کے لیے ازگر |
| سمورتی نظام | Goroutines ہلکے اور خوبصورت ہیں | ایرلنگ/ایلیکسیر برائے غلطی برداشت کرنے والی ہم آہنگی |
| نیٹ ورک پروگرامنگ | بہترین نیٹ پیکج | کم ترین سطح کے کنٹرول کے لیے C/C++ |
| ڈیٹا سائنس / ایم ایل | صحیح ماحولیاتی نظام نہیں | ازگر، آر |
| ڈیسک ٹاپ/موبائل GUI | کوئی GUI فریم ورک نہیں | ویب فرنٹ اینڈ یا مادری زبان استعمال کریں۔
| ایمبیڈڈ سسٹمز | بہت بھاری (GC، رن ٹائم) | سی، زنگ |
---

## مصنوعی سوال و جواب
### سوال 1: گو میں استثنا کیوں نہیں ہے؟ مجھے غلطیوں کو کیسے ہینڈل کرنا چاہئے؟
**A:** Go مستثنیات کے بجائے واضح غلطی کی واپسی کا استعمال کرتا ہے۔ ہر فنکشن جو ناکام ہو سکتا ہے ایک`error`کو اس کی آخری واپسی قدر کے طور پر واپس کرتا ہے۔ یہ کال کرنے والے کو غلطیوں کو واضح طور پر ہینڈل کرنے پر مجبور کرتا ہے — کوئی خاموش ناکامی یا بھولے ہوئے کیچ بلاکس نہیں۔ محاورہ کا نمونہ`if err != nil`ہے۔ ریپنگ کی غلطیوں کے لیے`fmt.Errorf`کو`%w`کے ساتھ اور`errors.Is`/`errors.As`کو غلطی کی اقسام کی جانچ کے لیے استعمال کریں۔ ناقابل بازیافت غلطیوں (پروگرامنگ بگز) کے لیے، استعمال کریں`panic`۔
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

### Q2: گوروٹینز کیا ہیں، اور وہ OS تھریڈز سے کیسے مختلف ہیں؟
**A:** Goroutines ہلکے وزن والے، یوزر اسپیس تھریڈز ہیں جن کا انتظام Go رن ٹائم کے ذریعے کیا جاتا ہے۔ وہ ~2KB کے اسٹیک سے شروع ہوتے ہیں (OS تھریڈز کے لیے بمقابلہ ~1MB)، شیڈیولر کے ذریعے OS تھریڈز پر ملٹی پلیکس کیے جاتے ہیں، اور ایک وقت میں لاکھوں بنائے جا سکتے ہیں۔ گوروٹینز کے درمیان مواصلت چینلز کا استعمال کرتی ہے (یا مشترکہ ریاست کے لیے`sync`قدیم)۔ گوروٹین لیکس سے بچنے کے لیے ہمیشہ`sync.WaitGroup`یا سیاق و سباق کی منسوخی کا استعمال کریں۔
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

### Q3: مجھے کنکرنسی کے لیے چینلز بمقابلہ mutexes کب استعمال کرنا چاہیے؟
**A:** چینلز کا استعمال کریں جب گوروٹینز کو ڈیٹا کو مواصلت کرنے کی ضرورت ہو — وہ "مواصلات کرکے میموری کو شیئر کریں" کے فلسفے کو نافذ کرتے ہیں۔ mutexes (`sync.Mutex`) استعمال کریں جب گوروٹینز کو مشترکہ حالت (کیچز، کاؤنٹرز، کنکشن پولز) کی حفاظت کرنے کی ضرورت ہو۔ ایک اچھا اصول: اگر ڈیٹا کو گوروٹینز کے درمیان منتقل کیا جا رہا ہے، تو چینلز کا استعمال کریں۔ اگر متعدد گوروٹینز کے ذریعے ڈیٹا تک رسائی حاصل کی جا رہی ہے، تو ایک mutex استعمال کریں۔ سادہ جوہری کارروائیوں کے لیے،`sync/atomic`استعمال کریں۔
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

### Q4:`nil`سلائسس/نقشے اور خالی میں کیا فرق ہے؟
**A:** ایک`nil`سلائس (`var s []int`) میں کوئی بنیادی صف نہیں ہے، لمبائی 0، گنجائش 0۔ ایک خالی سلائس (`s := []int{}`یا`make([]int, 0)`) میں ایک بنیادی صف ہے لیکن لمبائی 0 ہے۔ دونوں XQZMARKER کے ساتھ یکساں طور پر کام کرتے ہیں۔`len`,`cap`, اور`range`. JSON مارشلنگ مختلف ہے: صفر کے ٹکڑے`null`بن جاتے ہیں، خالی سلائسیں`[]`بن جاتی ہیں۔ بہترین عمل: واپسی کی قدروں کے لیے صفر سلائسز کو ترجیح دیں (وہ "کوئی ڈیٹا نہیں" کی نشاندہی کرتے ہیں)، JSON آؤٹ پٹ کی اہمیت ہونے پر خالی سلائسز۔
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

### Q5: Go میں انٹرفیس کیسے کام کرتے ہیں، اور خالی انٹرفیس کیا ہے؟
**A:** Go انٹرفیس واضح طور پر مطمئن ہیں — ایک قسم اپنے طریقوں کو لاگو کرکے ایک انٹرفیس کو لاگو کرتی ہے، بغیر کسی`implements`کلیدی لفظ کے۔ یہ ڈیکپلنگ اور کمپوزیشن کو قابل بناتا ہے۔ خالی انٹرفیس`interface{}`(یا Go 1.18+ میں `any`) ہر قسم سے مطمئن ہے — اسے تھوڑا سا استعمال کریں (جنرک اکثر بہتر ہوتے ہیں)۔ انٹرفیس اقدار جوڑے ہیں:`(type, value)`۔ ایک صفر انٹرفیس میں دونوں صفر ہوتے ہیں۔
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

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: شرح کی حد بندی کے ساتھ ایک سمورتی ویب سکریپر بنائیں
**مسئلہ کا بیان:** ایک ایسا گو پروگرام بنائیں جو بیک وقت فہرست سے یو آر ایل حاصل کرتا ہے، صفحہ کے عنوانات کو نکالتا ہے، فی سیکنڈ 10 درخواستوں کی شرح کی حد کا احترام کرتا ہے، اور ڈیٹا کی دوڑ کے بغیر نتائج جمع کرتا ہے۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں ضرورت ہے: (1) گوروٹینز کے ساتھ ہم آہنگ HTTP بازیافت، (2) حد سے زیادہ سرورز سے بچنے کے لیے شرح کو محدود کرنا، (3) ریس کے بغیر نتیجہ جمع کرنا، (4) ناکام درخواستوں کے لیے مناسب غلطی سے نمٹنے۔ گو کے کنکرنسی پرائمیٹوز (گورٹائنز، چینلز،`errgroup`) اس کے لیے مثالی ہیں۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- ٹوکن-بکٹ ریٹ کو محدود کرنے کے لیے`golang.org/x/time/rate`استعمال کریں۔
- گوروٹینز کا انتظام کرنے کے لیے`sync.WaitGroup`یا`errgroup.Group`استعمال کریں۔
- آؤٹ پٹس کو محفوظ طریقے سے جمع کرنے کے لیے رزلٹ چینل کا استعمال کریں۔
- منسوخی اور ٹائم آؤٹ کے لیے`context.Context`استعمال کریں۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- کوئی ڈیٹا ریس نہیں: ہر گوروٹین`results`میں اپنے اپنے انڈیکس پر لکھتا ہے - کسی mutex کی ضرورت نہیں ہے۔
-`errgroup.SetLimit`ریٹ محدود کرنے والے سے آزادانہ طور پر ہم آہنگی کا پابند ہے۔
-`io.LimitReader`ضرورت سے زیادہ بڑے صفحات کو پڑھنے سے روکتا ہے۔
-`http.NewRequestWithContext`اس بات کو یقینی بناتا ہے کہ سیاق و سباق کے مکمل ہونے پر درخواستیں منسوخ ہو جائیں۔
- پیداوار کے لیے: ایکسپونینشل بیک آف، کنکشن پولنگ ٹیوننگ، اور میٹرکس کے ساتھ دوبارہ کوشش کی منطق شامل کریں۔
### مسئلہ 2: ایک عام LRU کیشے کو لاگو کریں۔
**مسئلہ کا بیان:** generics (Go 1.18+) کا استعمال کرتے ہوئے Go میں تھریڈ سے محفوظ، عام LRU (سب سے کم حال میں استعمال شدہ) کیشے کو لاگو کریں۔ اسے O(1) وقت کی پیچیدگی کے ساتھ `Get`، `Set`، اور`Delete`کو سپورٹ کرنا چاہیے۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ایک LRU کیشے کو O(1) تلاش (ہیش میپ) اور O(1) آرڈرنگ اپڈیٹس کی ضرورت ہوتی ہے (دوگنا منسلک فہرست)۔`Get`پر: آئٹم کو سامنے لے جائیں۔`Set`پر: سامنے داخل کریں؛ گنجائش سے زیادہ ہونے پر پیچھے سے بے دخل کریں۔ دھاگے کی حفاظت کے لیے ایک mutex کی ضرورت ہے۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- O(1) آگے بڑھنے اور پیچھے سے ہٹانے کے لیے`container/list`(دوہری منسلک فہرست) کا استعمال کریں۔
- O(1) تلاش کے لیے`map[K]*list.Element`استعمال کریں۔
- دھاگے کی حفاظت کے لیے`sync.Mutex`استعمال کریں۔
- قسم کی حفاظت کے لیے جنرک (`[K comparable, V any]`)۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- O(1) `Get`، `Set`،`Delete`کے لیے: نقشہ تلاش کرنا O(1) اوسط ہے؛ فہرست کی کارروائیاں (`MoveToFront`,`PushFront`,`Remove`,`Back`) تمام O(1) ہیں۔
- تھریڈ سیفٹی:`sync.Mutex`یقینی بناتا ہے کہ ایک وقت میں صرف ایک گوروٹین کیشے تک رسائی حاصل کرے۔ پڑھنے والے بھاری کام کے بوجھ کے لیے،`sync.RWMutex`استعمال کریں۔
- عمومیات:`[K comparable, V any]`چابیاں`==`(نقشہ کی چابیاں کے لیے درکار) کی حمایت کو یقینی بناتی ہیں جبکہ قدریں کسی بھی قسم کی ہو سکتی ہیں۔
- پروڈکشن:`github.com/hashicorp/golang-lru/v2`پر غور کریں — TTL سپورٹ اور کم لاک تنازعہ کے لیے شارڈنگ کے ساتھ جنگ ​​کا تجربہ۔
### مسئلہ 3: ایک TCP چیٹ سرور بنائیں
**مسئلہ کا بیان:** ایک ہم آہنگ TCP چیٹ سرور بنائیں جہاں کلائنٹ جڑ سکیں، دوسرے تمام منسلک کلائنٹس کو پیغامات نشر کر سکیں، اور خوبصورتی سے منقطع کر سکیں۔ دوسروں کو بلاک کیے بغیر سست گاہکوں کو ہینڈل کریں۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں ضرورت ہے: (1) TCP کنکشنز کو قبول کریں، (2) پڑھنے کے لیے فی کلائنٹ ایک گوروٹین، (3) تمام کلائنٹس کو پیغامات بھیجنے کے لیے ایک براڈکاسٹ میکانزم، (4) منقطع اور سست کلائنٹس کو ہینڈل کریں۔ یہ ایک کلاسک فین آؤٹ پیٹرن ہے۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- TCP کنکشنز کے لیے`net.Listener`استعمال کریں۔
- کلائنٹ کی رجسٹریشن/ڈیرجسٹریشن/براڈکاسٹنگ کے لیے چینلز کے ساتھ مرکزی`hub`گوروٹین استعمال کریں۔
- ہر کلائنٹ کو بفر شدہ چینل کے ساتھ ایک وقف تحریری گوروٹین ملتا ہے - سست کلائنٹس دوسروں کو بلاک نہیں کرتے ہیں۔
- شاندار بند کے لیے`context.Context`استعمال کریں۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- آہستہ کلائنٹ ہینڈلنگ: براڈکاسٹ میں`select`کے ساتھ`default`بلاک ہونے سے روکتا ہے۔ سست کلائنٹس کا رابطہ منقطع ہو جاتا ہے اگر ان کا بفر بھر جاتا ہے۔
- کوئی ریس نہیں: حب گوروٹین`clients`نقشہ کا واحد مصنف ہے۔ `mu`نشریات کے دوران پڑھنے کی حفاظت کرتا ہے۔
- خوبصورت شٹ ڈاؤن: سننے والے اور ڈرین کنکشن کو بند کرنے کے لیے`context.Context`اور ایک سگنل ہینڈلر شامل کریں۔
- پیداوار: براؤزر کلائنٹس کے لیے`golang.org/x/net/websocket`استعمال کرنے پر غور کریں، اور تصدیق، پیغام کی سرگزشت، اور کمرے شامل کریں۔
---

## خلاصہ
گو ایک ایسی زبان ہے جو جان بوجھ کر خصوصیات پر سادگی کا انتخاب کرتی ہے۔ اس میں زیادہ تر زبانوں سے کم تعمیرات ہیں -- کوئی وراثت نہیں، کوئی طریقہ اوورلوڈنگ نہیں، کوئی استثناء نہیں، میکرو نہیں -- اور یہ ایک طاقت ہے۔ نتیجہ یہ کوڈ ہے جو پڑھنے میں آسان، لکھنے میں آسان اور برقرار رکھنے میں آسان ہے۔ گو کا کنکرنسی ماڈل (گوروٹینز اور چینلز) کسی بھی زبان میں بہترین ڈیزائن کردہ میں سے ایک ہے۔ کلاؤڈ انفراسٹرکچر، مائیکرو سروسز، سی ایل آئی ٹولز، اور نیٹ ورک پروگرامنگ کے لیے، گو ایک بہترین انتخاب ہے۔