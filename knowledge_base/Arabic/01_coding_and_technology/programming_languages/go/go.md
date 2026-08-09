---
# البيانات الوصفية
العنوان: "اذهب"
الوصف: "مرجع شامل للغة برمجة Go يغطي النظرة العامة والمقايضات وأساسيات بناء الجملة والنظام البيئي ومتى يتم استخدامها."
الفئة: "البرمجة والتكنولوجيا"
الإصدار: "1.0.0"
الحالة: "نشط"
#مساهمة
المؤلفين:
  - الاسم: "فريق تدريب نموذج الذكاء الاصطناعي"
    البريد الإلكتروني: ""
    الدور: "original_author"
المساهمين: []
سجل التغيير:
  - الإصدار: "1.0.0"
    التاريخ: "2026-08-05"
    المؤلف: "فريق تدريب نموذج الذكاء الاصطناعي"
    التغييرات: "تمت إضافة بيانات تعريف YAML الأمامية لتتبع المساهمين"
# مراجعة
تم الإنشاء: "05-08-2026"
آخر_تعديل: "05-08-2026"
تاريخ_المراجعة: "05-02-2027"
تمت المراجعة بواسطة: "فريق قاعدة معارف البرمجة والتكنولوجيا"
next_review: "2027-08-05"
# التصنيف
العلامات: [اذهب، لغة البرمجة، بناء الجملة، النظام البيئي، الترميز والتكنولوجيا]
مستوى الصعوبة: "متوسط"
المتطلبات الأساسية: []
وقت_القراءة المقدر: "30 دقيقة"
# دليل المساهمة
المساهمة:
  الترخيص: "MIT"
  Feedback_channel: "مشكلات GitHub"
  how_to_contribute: "أرسل رسالة عامة تحتوي على التغييرات وقم بتحديث سجل التغييرات"
  review_process: "تتم مراجعة التغييرات بواسطة مشرفي الفئة قبل الدمج"
---
# يذهب
Go (غالبًا ما تسمى "Golang" بعد اسم المجال الأصلي الخاص بها) هي لغة برمجة مجمعة ومكتوبة بشكل ثابت تم تصميمها في Google بواسطة Robert Griesemer وRob Pike وKen Thompson. تم إصدارها لأول مرة في عام 2012 بهدف واضح وهو أن تكون لغة أفضل لبرمجة الأنظمة - لغة تجمع بين أداء لغة C وإنتاجية اللغات الديناميكية مثل Python. تشتهر Go ببساطتها وتجميعها السريع والتزامن المدمج (goroutines والقنوات) والأدوات الممتازة.
تعمل Go على تشغيل جزء كبير من النظام البيئي للبنية التحتية السحابية: Docker، وKubernetes، وTerraform، وPrometheus، وما إلى ذلك، وخادم HTTP الخاص بمكتبة Go القياسية كلها مكتوبة بلغة Go. لقد أصبحت اللغة الافتراضية للتطوير السحابي الأصلي والخدمات الصغيرة وأدوات CLI.
---

## لماذا يعتبر الذهاب مهمًا؟
- **البساطة في التصميم**: يحتوي تطبيق Go على 25 كلمة رئيسية فقط. اللغة صغيرة عمدا وسهلة التعلم.
- **تجميع سريع**: يتم التجميع مباشرةً إلى كود الجهاز في ثوانٍ، حتى بالنسبة للمشاريع الكبيرة.
- **التزامن المدمج**: تعمل إجراءات Goroutines والقنوات على جعل البرمجة المتزامنة متاحة وفعالة.
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
| اذهب للاتصال بـ C | cgo (`import "C"`) |
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

## ملخص
Go هي لغة تختار البساطة عمدًا على الميزات. لديها بنيات أقل من معظم اللغات - لا وراثة، لا يوجد تحميل زائد للطرق، لا استثناءات، لا وحدات ماكرو - وهذه نقطة قوة. والنتيجة هي رمز سهل القراءة والكتابة وسهل الصيانة. يعد نموذج التزامن الخاص بـ Go (المجموعات والقنوات) واحدًا من أفضل النماذج تصميمًا بأي لغة. بالنسبة للبنية التحتية السحابية والخدمات الصغيرة وأدوات واجهة سطر الأوامر (CLI) وبرمجة الشبكات، يعد Go خيارًا ممتازًا.