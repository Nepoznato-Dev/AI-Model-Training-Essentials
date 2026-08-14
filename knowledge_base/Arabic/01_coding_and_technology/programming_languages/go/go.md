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
# يذهب
Go (غالبًا ما تسمى "Golang" بعد اسم المجال الأصلي الخاص بها) هي لغة برمجة مجمعة ومكتوبة بشكل ثابت تم تصميمها في Google بواسطة Robert Griesemer وRob Pike وKen Thompson. تم إصدارها لأول مرة في عام 2012 بهدف واضح وهو أن تكون لغة أفضل لبرمجة الأنظمة - لغة تجمع بين أداء لغة C وإنتاجية اللغات الديناميكية مثل Python. تشتهر Go ببساطتها وتجميعها السريع والتزامن المدمج (goroutines والقنوات) والأدوات الممتازة.
تعمل Go على تشغيل جزء كبير من النظام البيئي للبنية التحتية السحابية: Docker، وKubernetes، وTerraform، وPrometheus، وما إلى ذلك، وخادم HTTP الخاص بمكتبة Go القياسية كلها مكتوبة بلغة Go. لقد أصبحت اللغة الافتراضية للتطوير السحابي الأصلي والخدمات الصغيرة وأدوات CLI.
---

## لماذا يعتبر الذهاب مهمًا؟
- **البساطة في التصميم**: يحتوي تطبيق Go على 25 كلمة رئيسية فقط. اللغة صغيرة عمدا وسهلة التعلم.
- **تجميع سريع**: يتم التجميع مباشرةً إلى كود الجهاز في ثوانٍ، حتى بالنسبة للمشاريع الكبيرة.
- **التزامن المدمج**: تجعل إجراءات Goroutines والقنوات البرمجة المتزامنة متاحة وفعالة.
- **مكتبة قياسية ممتازة**: خادم HTTP، وترميز JSON، والاختبار، والتشفير - كلها مدمجة.
- **الثنائيات الثابتة**: يتم تجميعها إلى ثنائي واحد بدون تبعيات خارجية. النشر أمر تافه.
- **النسب على نطاق Google**: تم تصميمه بواسطة مهندسين قاموا ببناء Unix وUTF-8 والكثير من البنية التحتية لـ Google.
##المقايضات
| الحد | التفاصيل | الحل النموذجي |
|-----------|------------------------|---|
| ** لا توجد أنواع مجموع / مطابقة الأنماط ** | لا توجد تعدادات مع البيانات المرتبطة، ولا توجد أنواع جبرية | استخدم الواجهات واكتب المفاتيح |
| ** خطأ في التعامل مع الإسهاب ** | صريح إذا أخطأت != لا شيء يتحقق في كل مكان | قبول النمط؛ يجعل معالجة الأخطاء مرئية |
| **نظام بيئي أصغر** | مكتبات أقل من Python أو Java أو JavaScript | المكتبة القياسية تغطي معظم الاحتياجات؛ حزم المجتمع المتنامية |
| ** لا يوجد إطار واجهة المستخدم الرسومية ** | غير مناسب لواجهات مستخدم سطح المكتب أو الهاتف المحمول | استخدم واجهات المستخدم المستندة إلى الويب (WASM) أو لغة أخرى |
| **جامع القمامة** | لديه GC - فترات التوقف صغيرة ولكنها غير صفرية | ضبط GC لأحمال العمل الحساسة لزمن الوصول؛ استخدم sync.Pool |
---

## أساسيات بناء الجملة
### البنية الأساسية
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

### الوظائف
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

### الهياكل والواجهات
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

### معالجة الأخطاء
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

### التزامن - Goroutines والقنوات
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

## بناء الجملة والأنماط المتقدمة
### الأدوية العامة (الإصدار 1.18+)
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

### مطابقة الأنماط المتقدمة (مفاتيح الكتابة)
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

### التفاف الخطأ المخصص
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

## التزامن والتوازي (الغوص العميق)
### نمط تجمع العمال
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

### سياق الإلغاء
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

### اختر للتعدد
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

## تكوين المشروع ونظام البناء
### هيكل المشروع
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

### اذهب.MOD
```
module github.com/example/my_project

go 1.22

require (
    github.com/gin-gonic/gin v1.10.0
    github.com/go-sql-driver/mysql v1.8.0
    go.uber.org/zap v1.27.0
)
```

### الأوامر الأساسية
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

### خط أنابيب CI/CD (إجراءات GitHub)
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

## الاختبار
### اختبارات الوحدة
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

### اختبارات HTTP المستندة إلى الجداول
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

## إمكانية التشغيل البيني
### CGo (الاتصال بـ C من Go)
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

### FFI مع لغات أخرى
| الاتجاه | آلية |
|-----------|-----------|
| اذهب للاتصال بـ C | سيغو (`import "C"`) |
| اذهب للاتصال بـ C++ | وظائف المجمع CGO + C |
| C يدعو الذهاب | تصدير وظائف Go باستخدام`//export`|
| اذهب للاتصال ببايثون | استخدم gopy أو العملية الفرعية |
---

## أنماط التصميم
### نمط البرامج الوسيطة (HTTP)
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

### نمط الخيارات
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

## الأداء والتحسين
### التنميط
```bash
go test -cpuprofile=cpu.prof -bench=. ./...
go tool pprof cpu.prof
go test -memprofile=mem.prof -bench=. ./...
go tool pprof mem.prof
```

### نصائح للتحسين
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

## النشر
### التجميع المتقاطع
```bash
GOOS=linux GOARCH=amd64 go build -o myapp-linux
GOOS=windows GOARCH=amd64 go build -o myapp.exe
GOOS=darwin GOARCH=arm64 go build -o myapp-mac
```

### نشر عامل الميناء
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

## المكتبة القياسية
| الحزمة | الغرض |
|---------|--------|
| فمت | تنسيق الإدخال/الإخراج |
| صافي/http | عميل وخادم HTTP |
| ترميز/json | ترميز/فك تشفير JSON |
| نظام التشغيل | العمليات على مستوى نظام التشغيل |
| ايو | عناصر الإدخال/الإخراج الأولية |
| سلاسل / strconv | التلاعب بالسلسلة |
| مزامنة | Mutex، WaitGroup، مرة واحدة |
| السياق | المواعيد النهائية، الإلغاء |
| اختبار | إطار اختبار مدمج |
| سجل / سجل / سجل | تسجيل |
| الوقت | الوقت والمدة |
| التشفير | التشفير (TLS، التجزئة) |
| قاعدة البيانات / SQL | تجريد قاعدة البيانات |
---

## الأدوات
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

## متى يجب استخدام Go
| السيناريو | لماذا تذهب | البديل الأفضل |
|----------|-------|------------------|
| الخدمات السحابية الأصلية / الخدمات الصغيرة | ثنائيات سريعة وصغيرة، HTTP | ممتاز الصدأ للحصول على أقصى قدر من الأداء |
| أدوات سطر الأوامر | تجميع سريع، ثنائي واحد | الصدأ لـ CLIs المعقدة |
| خوادم الويب / واجهات برمجة التطبيقات | HTTP مدمج وسريع وبسيط | Node.js/Express للنماذج الأولية السريعة |
| أدوات DevOps | Docker وKubernetes وTerraform هي Go | بايثون للبرمجة النصية |
| الأنظمة المتزامنة | Goroutines خفيفة الوزن وأنيقة | Erlang/Elixir للتزامن المتسامح مع الأخطاء |
| برمجة الشبكات | باقة نت ممتازة | C/C++ للتحكم في المستوى الأدنى |
| علم البيانات / تعلم الآلة | ليس النظام البيئي الصحيح | بايثون، ر |
| واجهة المستخدم الرسومية لسطح المكتب/الهاتف المحمول | لا يوجد إطار واجهة المستخدم الرسومية | استخدم واجهة ويب أو لغة أصلية |
| الأنظمة المدمجة | ثقيل جدًا (GC، وقت التشغيل) | ج، الصدأ |
---

## أسئلة وأجوبة اصطناعية
### س1: لماذا لا يوجد استثناءات في Go؟ كيف يجب أن أتعامل مع الأخطاء؟
**أ:** يستخدم Go إرجاع الأخطاء الصريحة بدلاً من الاستثناءات. تقوم كل دالة يمكن أن تفشل بإرجاع`error`كقيمة الإرجاع الأخيرة. وهذا يجبر المتصل على التعامل مع الأخطاء بشكل صريح - لا توجد حالات فشل صامتة أو كتل التقاط منسية. النمط الاصطلاحي هو`if err != nil`. استخدم`fmt.Errorf`مع`%w`لتغليف الأخطاء، و`errors.Is` /`errors.As`للتحقق من أنواع الأخطاء. بالنسبة للأخطاء غير القابلة للاسترداد (أخطاء البرمجة)، استخدم`panic`.
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

### السؤال الثاني: ما هي goroutines، وكيف تختلف عن سلاسل عمليات نظام التشغيل؟
**ج:** Goroutines عبارة عن سلاسل رسائل خفيفة الوزن تُدار في مساحة المستخدم بواسطة وقت تشغيل Go. تبدأ بـ ~ 2 كيلو بايت من المكدس (مقابل ~ 1 ميجابايت لسلاسل نظام التشغيل)، ويتم مضاعفة إرسالها إلى سلاسل عمليات نظام التشغيل بواسطة المجدول، ويمكن إنشاؤها بالملايين في المرة الواحدة. يستخدم الاتصال بين goroutines القنوات (أو عناصر`sync`الأولية للحالة المشتركة). استخدم دائمًا`sync.WaitGroup`أو إلغاء السياق لتجنب تسربات goroutine.
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

### Q3: متى يجب علي استخدام القنوات مقابل كائنات المزامنة للتزامن؟
**ج:** استخدم القنوات عندما تحتاج أدوات goroutines إلى توصيل البيانات - فهي تفرض فلسفة "مشاركة الذاكرة عن طريق الاتصال". استخدم كائنات المزامنة (`sync.Mutex`) عندما تحتاج goroutines إلى حماية الحالة المشتركة (ذاكرة التخزين المؤقت، والعدادات، وتجمعات الاتصال). قاعدة جيدة: إذا تم تمرير البيانات بين goroutines، استخدم القنوات؛ إذا تم الوصول إلى البيانات من خلال goroutines متعددة، فاستخدم كائن المزامنة (mutex). للعمليات الذرية البسيطة، استخدم`sync/atomic`.
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

### السؤال الرابع: ما الفرق بين شرائح/خرائط`nil`والخرائط الفارغة؟
**A:** لا تحتوي شريحة`nil`(`var s []int`) على مصفوفة أساسية، الطول 0، السعة 0. تحتوي الشريحة الفارغة (`s := []int{}`أو`make([]int, 0)`) على مصفوفة أساسية ولكن الطول 0. يعمل كلاهما بشكل متماثل مع`append`,`len`,`cap`, و`range`. يختلف تنظيم JSON: تصبح الشرائح الخالية `null`، وتصبح الشرائح الفارغة `[]`. أفضل الممارسات: تفضيل الشرائح الصفرية للقيم المرجعة (فهي تشير إلى "لا توجد بيانات")، والشرائح الفارغة عندما يكون إخراج JSON مهمًا.
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

### س5: كيف تعمل الواجهات في Go وما هي الواجهة الفارغة؟
**أ:** يتم تلبية واجهات Go ضمنيًا — النوع الذي ينفذ واجهة من خلال تنفيذ أساليبه، بدون كلمة رئيسية `implements`. وهذا يتيح الفصل والتكوين. الواجهة الفارغة`interface{}`(أو`any`في Go 1.18+) راضية عن كل نوع - استخدمها باعتدال (الأدوية العامة غالبًا ما تكون أفضل). قيم الواجهة عبارة عن أزواج:`(type, value)`. واجهة nil لها كلا الأمرين nil.
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

## حل المشكلات المتعلقة بسلسلة الأفكار
### المشكلة 1: إنشاء مكشطة ويب متزامنة مع تحديد المعدل
**بيان المشكلة:** أنشئ برنامج Go الذي يجلب عناوين URL من القائمة بشكل متزامن، ويستخرج عناوين الصفحات، ويحترم حد المعدل الذي يبلغ 10 طلبات في الثانية، ويجمع النتائج دون سباقات البيانات.
**الخطوة الأولى — فهم المشكلة:**
نحتاج إلى: (1) جلب HTTP متزامن مع goroutines، (2) تحديد المعدل لتجنب إرهاق الخوادم، (3) جمع النتائج بدون سباقات، (4) معالجة الأخطاء بشكل صحيح للطلبات الفاشلة. تعتبر أساسيات التزامن الخاصة بـ Go (goroutines،channels، `errgroup`) مثالية لهذا الغرض.
**الخطوة الثانية — تحديد النهج:**
- استخدم`golang.org/x/time/rate`لتحديد معدل دلو الرمز المميز.
- استخدم`sync.WaitGroup`أو`errgroup.Group`لإدارة goroutines.
- استخدم قناة النتائج لجمع المخرجات بشكل آمن.
- استخدم`context.Context`للإلغاء والمهلة.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- لا توجد سباقات بيانات: كل goroutine يكتب إلى فهرسه الخاص في`results`- لا حاجة إلى كائن المزامنة (mutex).
- يحد`errgroup.SetLimit`التزامن بشكل مستقل عن محدد المعدل.
- يمنع`io.LimitReader`قراءة الصفحات الكبيرة جدًا.
- يضمن`http.NewRequestWithContext`إلغاء الطلبات عند انتهاء السياق.
- بالنسبة للإنتاج: أضف منطق إعادة المحاولة مع التراجع الأسي وضبط تجميع الاتصال والمقاييس.
### المشكلة الثانية: تنفيذ ذاكرة تخزين مؤقت LRU عامة
** بيان المشكلة: ** قم بتنفيذ ذاكرة تخزين مؤقت LRU عامة (الأقل استخدامًا مؤخرًا) في Go باستخدام الأدوية العامة (Go 1.18+). يجب أن يدعم`Get`و`Set`و`Delete`مع التعقيد الزمني O(1).
**الخطوة الأولى — فهم المشكلة:**
تحتاج ذاكرة التخزين المؤقت LRU إلى بحث O(1) (خريطة التجزئة) وتحديثات ترتيب O(1) (قائمة مرتبطة بشكل مزدوج). على `Get`: انقل العنصر إلى الأمام. في `Set`: أدخل في المقدمة؛ طرد من الخلف إذا كان أكثر من القدرة. تتطلب سلامة الخيط كائن المزامنة (mutex).
**الخطوة الثانية — تحديد النهج:**
- استخدم`container/list`(القائمة المرتبطة بشكل مزدوج) للانتقال O(1) إلى الأمام والإزالة من الخلف.
- استخدم`map[K]*list.Element`للبحث عن O(1).
- استخدم`sync.Mutex`لسلامة الخيط.
- الأدوية العامة (`[K comparable, V any]`) للسلامة النوعية.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- O(1) لـ `Get`، `Set`، `Delete`: البحث عن الخريطة هو متوسط O(1)؛ عمليات القائمة (`MoveToFront`,`PushFront`,`Remove`,`Back`) كلها O(1).
- سلامة الخيط: يضمن`sync.Mutex`وصول goroutine واحد فقط إلى ذاكرة التخزين المؤقت في المرة الواحدة. بالنسبة لأحمال العمل كثيفة القراءة، استخدم`sync.RWMutex`.
- الأدوية العامة: يضمن`[K comparable, V any]`دعم المفاتيح لـ`==`(مطلوب لمفاتيح الخريطة) بينما يمكن أن تكون القيم من أي نوع.
- الإنتاج: فكر في`github.com/hashicorp/golang-lru/v2`— الذي تم اختباره في المعركة مع دعم TTL والتقسيم لتقليل تنافس القفل.
### المشكلة 3: إنشاء خادم دردشة TCP
**بيان المشكلة:** أنشئ خادم دردشة TCP متزامنًا حيث يمكن للعملاء الاتصال وبث الرسائل إلى جميع العملاء الآخرين المتصلين وقطع الاتصال بأمان. التعامل مع العملاء البطيئين دون حظر الآخرين.
**الخطوة الأولى — فهم المشكلة:**
نحتاج إلى: (1) قبول اتصالات TCP، (2) نظام goroutine واحد لكل عميل للقراءة، (3) آلية بث لإرسال الرسائل إلى جميع العملاء، (4) التعامل مع حالات انقطاع الاتصال والعملاء البطيئين. هذا هو النمط الكلاسيكي للمروحة.
**الخطوة الثانية — تحديد النهج:**
- استخدم`net.Listener`لاتصالات TCP.
- استخدم نظام`hub`المركزي مع القنوات لتسجيل العميل/إلغاء التسجيل/البث.
- يحصل كل عميل على نظام كتابة مخصص مع قناة مخزنة مؤقتًا - العملاء البطيئون لا يحظرون الآخرين.
- استخدم`context.Context`لإيقاف التشغيل بسلاسة.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- التعامل البطيء مع العميل: يمنع البث`select`مع`default`الحظر. يتم قطع اتصال العملاء البطيئين في حالة امتلاء المخزن المؤقت الخاص بهم.
- لا توجد سباقات: محور goroutine هو الكاتب الوحيد لخريطة `clients`؛ `mu`يحمي عمليات القراءة أثناء البث.
- إيقاف التشغيل بسلاسة: أضف`context.Context`ومعالج الإشارة لإغلاق اتصالات المستمع واستنزافها.
- الإنتاج: فكر في استخدام`golang.org/x/net/websocket`لعملاء المتصفح، وأضف المصادقة وسجل الرسائل والغرف.
---

## ملخص
Go هي لغة تختار البساطة عمدًا على الميزات. لديها بنيات أقل من معظم اللغات - لا وراثة، لا يوجد تحميل زائد للطرق، لا استثناءات، لا وحدات ماكرو - وهذه نقطة قوة. والنتيجة هي رمز سهل القراءة، وسهل الكتابة، وسهل الصيانة. يعد نموذج التزامن الخاص بـ Go (المجموعات والقنوات) واحدًا من أفضل النماذج تصميمًا بأي لغة. بالنسبة للبنية التحتية السحابية والخدمات الصغيرة وأدوات واجهة سطر الأوامر (CLI) وبرمجة الشبكات، يعد Go خيارًا ممتازًا.