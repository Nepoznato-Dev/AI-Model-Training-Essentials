---
# فراداده
عنوان: "برو"
توضیحات: "مرجع جامع برای زبان برنامه نویسی Go شامل مرور کلی، مبادلات، اصول نحو، اکوسیستم و زمان استفاده از آن."
دسته بندی: "کدنویسی و فناوری"
نسخه: "1.0.0"
وضعیت: "فعال"
# مشارکت
نویسندگان:
  - نام: "تیم آموزشی مدل AI"
    ایمیل: ""
    نقش: "نویسنده_اصلی"
مشارکت کنندگان: []
تغییرات ثبت شده:
  - نسخه: "1.0.0"
    تاریخ: "05-08-2026"
    نویسنده: "تیم آموزشی مدل هوش مصنوعی"
    تغییرات: "فراداده YAML frontmatter برای ردیابی مشارکت کنندگان اضافه شد"
# نقد و بررسی
ایجاد شده: "05-08-2026"
last_modified: "05-08-2026"
بازبینی_تاریخ: "05-02-2027"
reviewed_by: "تیم پایگاه دانش کدنویسی و فناوری"
next_review: "05-08-2027"
# طبقه بندی
برچسب‌ها: [برو، زبان برنامه‌نویسی، نحو، اکوسیستم، کدنویسی و فناوری]
سطح سختی: "متوسط"
پیش نیاز: []
تخمینی_زمان_خواندن: "30 دقیقه"
# راهنمای مشارکت
مشارکت:
  مجوز: "MIT"
  feedback_channel: "مشکلات GitHub"
  how_to_contribute: "ارسال روابط عمومی با تغییرات و به روز رسانی تغییرات"
  review_process: "تغییرات توسط نگهبانان دسته قبل از ادغام بررسی می شود"
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

## خلاصه
Go زبانی است که به عمد سادگی را به ویژگی ها ترجیح می دهد. ساختارهای کمتری نسبت به بسیاری از زبان‌ها دارد - بدون وراثت، بدون بارگذاری روش، بدون استثنا، بدون ماکرو - و این یک نقطه قوت است. نتیجه کدی است که خواندن آن آسان، نوشتن آسان و نگهداری آسان است. مدل همزمانی Go (گوروتین ها و کانال ها) یکی از بهترین طراحی شده در هر زبانی است. برای زیرساخت های ابری، میکروسرویس ها، ابزارهای CLI و برنامه نویسی شبکه، Go یک انتخاب عالی است.