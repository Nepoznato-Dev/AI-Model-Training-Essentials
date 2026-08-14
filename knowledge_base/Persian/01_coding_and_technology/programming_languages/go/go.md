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
#برو
Go (اغلب به نام دامنه اصلی آن "Golang" نامیده می شود) یک زبان برنامه نویسی تایپ شده و کامپایل شده است که در گوگل توسط رابرت گریزمر، راب پایک و کن تامپسون طراحی شده است. این اولین بار در سال 2012 با هدف صریح این که زبانی بهتر برای برنامه نویسی سیستم باشد منتشر شد -- زبانی که عملکرد زبان C را با بهره وری زبان های پویا مانند پایتون ترکیب می کند. Go به دلیل سادگی، کامپایل سریع، همزمانی داخلی (گوروتین ها و کانال ها) و ابزار عالی شناخته شده است.
Go بخش عمده ای از اکوسیستم زیرساخت ابری را تامین می کند: Docker، Kubernetes، Terraform، Prometheus، etcd، و سرور HTTP کتابخانه استاندارد Go همگی در Go نوشته شده اند. این زبان به زبان پیش‌فرض برای توسعه ابری، میکروسرویس‌ها و ابزارهای CLI تبدیل شده است.
---

## چرا برو مهم است
- **سادگی با طراحی **: Go تنها 25 کلمه کلیدی دارد. این زبان عمداً کوچک است و یادگیری آن آسان است.
- **کامپایل سریع**: مستقیماً در چند ثانیه به کد ماشین کامپایل می شود، حتی برای پروژه های بزرگ.
- ** همزمانی داخلی**: گوروتین ها و کانال ها برنامه نویسی همزمان را در دسترس و کارآمد می کنند.
- **کتابخانه استاندارد عالی**: سرور HTTP، رمزگذاری JSON، تست، رمزنگاری -- همه داخلی.
- **باینری های استاتیک**: به یک باینری واحد بدون وابستگی خارجی کامپایل می شود. استقرار بی اهمیت است.
- **تبار در مقیاس Google**: توسط مهندسانی طراحی شده است که یونیکس، UTF-8 و بسیاری از زیرساخت های گوگل را ساخته اند.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **بدون نوع مجموع / تطبیق الگو** | بدون فهرست با داده های مرتبط، بدون انواع جبری | استفاده از اینترفیس و تایپ سوئیچ |
| **خطا در رسیدگی به پرحرفی** | صریح اگر err != صفر همه جا را بررسی می کند | الگو را بپذیرید؛ مدیریت خطا را قابل مشاهده می کند |
| **اکوسیستم کوچکتر** | کتابخانه های کمتری نسبت به پایتون، جاوا یا جاوا اسکریپت | کتابخانه استاندارد اکثر نیازها را پوشش می دهد. بسته های اجتماعی در حال رشد |
| **بدون چارچوب رابط کاربری گرافیکی** | برای رابط کاربری دسکتاپ یا موبایل مناسب نیست | از UI های مبتنی بر وب (WASM) یا زبان دیگر | استفاده کنید
| ** زباله جمع کن** | دارای GC -- مکث ها کوچک اما غیر صفر هستند | GC را برای بارهای کاری حساس به تأخیر تنظیم کنید. استفاده از sync.Pool |
---

## اصول نحو
### ساختار اساسی
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

### توابع
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

### ساختارها و رابط ها
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

### رسیدگی به خطا
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

### همزمانی -- برنامه ها و کانال ها
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

## نحو و الگوهای پیشرفته
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

### تطبیق الگوی پیشرفته (سوئیچ‌های نوع)
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

### بسته بندی خطای سفارشی
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

## همزمانی و موازی (شیرجه عمیق)
### الگوی استخر کارگران
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

### زمینه برای لغو
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

### را برای Multiplexing انتخاب کنید
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

## پیکربندی پروژه و سیستم ساخت
### ساختار پروژه
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

### دستورات ضروری
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

### خط لوله CI/CD (اقدامات GitHub)
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

## تست
### تست های واحد
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

### تست های HTTP مبتنی بر جدول
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

## قابلیت همکاری
### CGo (تماس با C از Go)
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

### FFI با زبان های دیگر
| جهت | مکانیسم |
|-----------|-----------|
| با C | تماس بگیرید cgo (`import "C"`) |
| با C++ تماس بگیرید | توابع cgo + C wrapper |
| C در حال فراخوانی برو | صادرات توابع Go با`//export`|
| با پایتون تماس بگیرید | استفاده از gopy یا subprocess |
---

## الگوهای طراحی
### الگوی میان افزار (HTTP)
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

### الگوی گزینه ها
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

## عملکرد و بهینه سازی
### پروفایل
```bash
go test -cpuprofile=cpu.prof -bench=. ./...
go tool pprof cpu.prof
go test -memprofile=mem.prof -bench=. ./...
go tool pprof mem.prof
```

### نکات بهینه سازی
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

## استقرار
### تالیف متقاطع
```bash
GOOS=linux GOARCH=amd64 go build -o myapp-linux
GOOS=windows GOARCH=amd64 go build -o myapp.exe
GOOS=darwin GOARCH=arm64 go build -o myapp-mac
```

### استقرار داکر
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

## کتابخانه استاندارد
| پکیج | هدف |
|---------|---------|
| fmt | I/O فرمت شده |
| net/http | سرویس گیرنده و سرور HTTP |
| encoding/json | رمزگذاری/رمزگشایی JSON |
| سیستم عامل | عملیات سطح سیستم عامل |
| io | ورودی/خروجی های اولیه |
| رشته ها / strconv | دستکاری رشته |
| همگام سازی | Mutex، WaitGroup، Once |
| زمینه | مهلت، لغو |
| تست | چارچوب تست داخلی |
| log / log/slog | ورود به سیستم |
| زمان | زمان و مدت |
| رمزنگاری | رمزنگاری (TLS، هش) |
| پایگاه داده/sql | چکیده پایگاه داده |
---

## ابزار
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

## چه زمانی از Go استفاده کنیم
| سناریو | چرا برو | جایگزین بهتر |
|----------|--------|-------------------|
| خدمات / میکروسرویس های بومی ابری | باینری های سریع، کوچک، HTTP عالی | زنگ زدگی برای حداکثر کارایی |
| ابزارهای CLI | کامپایل سریع، تک باینری | زنگ برای CLI های پیچیده |
| وب سرورها / API ها | HTTP داخلی، سریع، ساده | Node.js/Express برای نمونه سازی سریع |
| ابزار DevOps | Docker، Kubernetes، Terraform هستند Go | پایتون برای اسکریپت نویسی |
| سیستم های همزمان | گوروتین ها سبک و ظریف هستند | Erlang/Elixir برای همزمانی تحمل خطا |
| برنامه نویسی شبکه | پکیج نت عالی | C/C++ برای کنترل در پایین ترین سطح |
| علم داده / ML | نه اکوسیستم مناسب | پایتون، R |
| رابط کاربری گرافیکی دسکتاپ/موبایل | بدون چارچوب رابط کاربری گرافیکی | از یک صفحه وب یا زبان مادری استفاده کنید |
| سیستم های تعبیه شده | خیلی سنگین (GC، زمان اجرا) | ج، زنگ |
---

## پرسش و پاسخ مصنوعی
### Q1: چرا Go استثنا ندارد؟ چگونه باید با خطاها برخورد کنم؟
**A:** Go از برگرداندن خطاهای صریح به جای استثناها استفاده می کند. هر تابعی که ممکن است شکست بخورد، یک`error`را به عنوان آخرین مقدار بازگشتی خود برمی‌گرداند. این باعث می‌شود تماس‌گیرنده به‌طور صریح با خطاها رسیدگی کند - بدون شکست بی‌صدا یا بلوک‌های فراموش‌شده. الگوی اصطلاحی`if err != nil`است. از`fmt.Errorf`با`%w`برای بسته بندی خطاها و`errors.Is`/`errors.As`برای بررسی انواع خطاها استفاده کنید. برای خطاهای غیرقابل جبران (اشکالات برنامه نویسی)، از`panic`استفاده کنید.
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

### Q2: گوروتین ها چیست و چه تفاوتی با رشته های سیستم عامل دارند؟
**A:** گوروتین ها رشته های سبک وزن و فضای کاربر هستند که توسط زمان اجرا Go مدیریت می شوند. آنها با ~ 2 کیلوبایت پشته شروع می شوند (در مقابل ~ 1 مگابایت برای رشته های سیستم عامل)، توسط زمان بندی بر روی رشته های سیستم عامل مالتی پلکس می شوند و می توانند میلیون ها نفر در یک زمان ایجاد شوند. ارتباط بین گوروتین ها از کانال ها (یا`sync`اولیه برای حالت اشتراکی) استفاده می کند. همیشه از`sync.WaitGroup`یا لغو متن استفاده کنید تا از نشت گوروتین جلوگیری کنید.
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

### Q3: چه زمانی باید از کانال ها در مقابل mutexes برای همزمانی استفاده کنم؟
**A:** از کانال ها در زمانی که گوروتین ها نیاز به برقراری ارتباط دارند استفاده کنید - آنها فلسفه "اشتراک گذاری حافظه از طریق برقراری ارتباط" را تقویت می کنند. هنگامی که گوروتین ها نیاز به محافظت از حالت مشترک (کش، شمارنده، مخزن های اتصال) دارند، از mutexes (`sync.Mutex`) استفاده کنید. یک قانون خوب: اگر داده ها بین گوروتین ها ارسال می شود، از کانال ها استفاده کنید. اگر داده ها توسط چندین گوروتین قابل دسترسی هستند، از یک mutex استفاده کنید. برای عملیات اتمی ساده، از`sync/atomic`استفاده کنید.
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

### Q4: تفاوت بین برش ها/نقشه های`nil`و برش های خالی چیست؟
**A:** یک برش`nil`(`var s []int`) هیچ آرایه زیرینی ندارد، طول 0، ظرفیت 0. یک برش خالی (`s := []int{}` یا `make([]int, 0)`) دارای یک آرایه زیرین اما طول آن 0 است. هر دو با XQZ MARKER یکسان هستند. `len`، `cap`، و `range`. JSON marshaling متفاوت است: برش های صفر تبدیل به `null`، برش های خالی تبدیل به`[]`می شوند. بهترین روش: برش‌های صفر را برای مقادیر بازگشتی ترجیح دهید (آنها «بدون داده» را نشان می‌دهند)، برش‌های خالی زمانی که خروجی JSON اهمیت دارد.
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

### Q5: اینترفیس ها در Go چگونه کار می کنند و رابط خالی چیست؟
**A:** رابط های Go به طور ضمنی برآورده می شوند - یک نوع یک رابط را با پیاده سازی روش های خود، بدون کلمه کلیدی`implements`پیاده سازی می کند. این امر جداسازی و ترکیب را امکان پذیر می کند. رابط خالی`interface{}`(یا`any`در Go 1.18+) با هر نوع راضی است - از آن کم استفاده کنید (عمومی ها اغلب بهتر هستند). مقادیر رابط جفت هستند: `(type, value)`. یک رابط nil هر دو را به عنوان صفر دارد.
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

## حل مسئله زنجیره ای از فکر
### مشکل 1: ساختن یک Web Scraper همزمان با Rate Limiting
**بیانیه مشکل:** یک برنامه Go بسازید که URL ها را همزمان از یک لیست واکشی می کند، عناوین صفحات را استخراج می کند، محدودیت نرخ 10 درخواست در ثانیه را رعایت می کند و نتایج را بدون مسابقه داده جمع آوری می کند.
** مرحله 1 - مشکل را درک کنید:**
ما به این موارد نیاز داریم: (1) واکشی همزمان HTTP با گوروتین ها، (2) محدود کردن نرخ برای جلوگیری از زیاد شدن سرورها، (3) جمع آوری نتایج بدون مسابقه، (4) مدیریت صحیح خطا برای درخواست های ناموفق. مقدمات همزمانی Go (گوروتین ها، کانال ها، `errgroup`) برای این کار ایده آل هستند.
** مرحله 2 - شناسایی رویکرد: **
- از`golang.org/x/time/rate`برای محدود کردن نرخ توکن-سطل استفاده کنید.
- از`sync.WaitGroup`یا`errgroup.Group`برای مدیریت گوروتین ها استفاده کنید.
- از یک کانال نتایج برای جمع آوری ایمن خروجی ها استفاده کنید.
- از`context.Context`برای لغو و وقفه استفاده کنید.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- بدون مسابقه داده: هر گوروتین به شاخص خود در`results`می نویسد - بدون نیاز به mutex.
-`errgroup.SetLimit`همزمانی را مستقل از محدود کننده نرخ محدود می کند.
-`io.LimitReader`از خواندن صفحات بیش از حد بزرگ جلوگیری می کند.
-`http.NewRequestWithContext`تضمین می کند که درخواست ها پس از اتمام متن لغو می شوند.
- برای تولید: منطق امتحان مجدد را با عقب نشینی نمایی، تنظیم ادغام اتصال و معیارها اضافه کنید.
### مشکل 2: یک کش عمومی LRU را پیاده سازی کنید
**بیانیه مشکل:** یک حافظه پنهان عمومی (کمترین استفاده اخیر) در Go با استفاده از ژنریک (Go 1.18+) ایمن و عمومی را اجرا کنید. باید از `Get`، `Set`، و`Delete`با پیچیدگی زمانی O(1) پشتیبانی کند.
** مرحله 1 - مشکل را درک کنید:**
یک حافظه پنهان LRU به جستجوی O(1) (نقشه هش) و O(1) سفارش به روز رسانی (لیست پیوندی دوگانه) نیاز دارد. در `Get`: مورد را به جلو منتقل کنید. در `Set`: درج در جلو. اخراج از پشت در صورت بیش از ظرفیت. ایمنی نخ نیاز به mutex دارد.
** مرحله 2 - شناسایی رویکرد: **
- از`container/list`(فهرست با پیوند دوگانه) برای حرکت O(1) به جلو و حذف از پشت استفاده کنید.
- از`map[K]*list.Element`برای جستجوی O(1) استفاده کنید.
- برای ایمنی نخ از`sync.Mutex`استفاده کنید.
- ژنریک (`[K comparable, V any]`) برای ایمنی نوع.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- O(1) برای `Get`، `Set`، `Delete`: جستجوی نقشه O(1) متوسط است. عملیات فهرست (`MoveToFront`، `PushFront`، `Remove`، `Back`) همه O(1) هستند.
- ایمنی رشته:`sync.Mutex`تضمین می کند که فقط یک گوروتین در یک زمان به حافظه پنهان دسترسی دارد. برای بارهای کاری سنگین، از`sync.RWMutex`استفاده کنید.
- Generics:`[K comparable, V any]`تضمین می کند که کلیدها از`==`(برای کلیدهای نقشه مورد نیاز) پشتیبانی می کنند، در حالی که مقادیر می توانند هر نوع باشند.
- تولید:`github.com/hashicorp/golang-lru/v2`را در نظر بگیرید - آزمایش شده با پشتیبانی TTL و شاردینگ برای کاهش اختلاف قفل.
### مشکل 3: یک سرور چت TCP بسازید
**بیانیه مشکل:** یک سرور چت TCP همزمان بسازید که در آن کلاینت‌ها می‌توانند متصل شوند، پیام‌ها را به سایر کلاینت‌های متصل پخش کنند، و ارتباط را به خوبی قطع کنند. مشتریان کند را بدون مسدود کردن دیگران مدیریت کنید.
** مرحله 1 - مشکل را درک کنید:**
ما نیاز داریم: (1) اتصالات TCP را بپذیریم، (2) یک گوروتین به ازای هر کلاینت برای خواندن، (3) یک مکانیسم پخش برای ارسال پیام به همه کلاینت ها، (4) مدیریت قطع ارتباط و کلاینت های کند. این یک الگوی کلاسیک فن بیرون است.
** مرحله 2 - شناسایی رویکرد: **
- از`net.Listener`برای اتصالات TCP استفاده کنید.
- از یک گوروتین مرکزی`hub`با کانال هایی برای ثبت نام / لغو ثبت / پخش مشتری استفاده کنید.
- هر مشتری یک برنامه نوشتن اختصاصی با یک کانال بافر دریافت می کند - مشتریان کند دیگران را مسدود نمی کنند.
- از`context.Context`برای خاموش کردن برازنده استفاده کنید.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- مدیریت کند مشتری:`select`با`default`در پخش از مسدود شدن جلوگیری می کند. اگر بافر آنها پر شود، کلاینت های کند قطع می شوند.
- بدون مسابقه: گوروتین هاب نویسنده تک نقشه`clients`است. `mu`از خواندن در حین پخش محافظت می کند.
- خاموش شدن برازنده:`context.Context`و کنترل کننده سیگنال را برای بستن شنونده و تخلیه اتصالات اضافه کنید.
- تولید: استفاده از`golang.org/x/net/websocket`را برای مشتریان مرورگر در نظر بگیرید و احراز هویت، تاریخچه پیام و اتاق‌ها را اضافه کنید.
---

## خلاصه
Go زبانی است که به عمد سادگی را به ویژگی ها ترجیح می دهد. ساختارهای کمتری نسبت به بسیاری از زبان‌ها دارد - بدون وراثت، بدون بارگذاری روش، بدون استثنا، بدون ماکرو - و این یک نقطه قوت است. نتیجه کدی است که خواندن آن آسان، نوشتن آسان و نگهداری آسان است. مدل همزمانی Go (گوروتین ها و کانال ها) یکی از بهترین طراحی شده در هر زبانی است. برای زیرساخت های ابری، میکروسرویس ها، ابزارهای CLI و برنامه نویسی شبکه، Go یک انتخاب عالی است.