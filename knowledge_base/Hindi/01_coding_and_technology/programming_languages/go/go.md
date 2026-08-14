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

# जाना
गो (अक्सर इसके मूल डोमेन नाम के बाद इसे "गोलंग" कहा जाता है) एक स्थिर रूप से टाइप की गई, संकलित प्रोग्रामिंग भाषा है जिसे रॉबर्ट ग्रिसेमर, रॉब पाइक और केन थॉम्पसन द्वारा Google पर डिज़ाइन किया गया है। इसे पहली बार 2012 में सिस्टम प्रोग्रामिंग के लिए एक बेहतर भाषा होने के स्पष्ट लक्ष्य के साथ जारी किया गया था - एक जो सी के प्रदर्शन को पायथन जैसी गतिशील भाषाओं की उत्पादकता के साथ जोड़ती है। गो अपनी सादगी, तेज़ संकलन, अंतर्निर्मित समवर्ती (गोरोइन और चैनल) और उत्कृष्ट टूलींग के लिए जाना जाता है।
गो अधिकांश क्लाउड इंफ्रास्ट्रक्चर पारिस्थितिकी तंत्र को शक्ति प्रदान करता है: डॉकर, कुबेरनेट्स, टेराफॉर्म, प्रोमेथियस इत्यादि, और गो मानक लाइब्रेरी के HTTP सर्वर सभी गो में लिखे गए हैं। यह क्लाउड-नेटिव डेवलपमेंट, माइक्रोसर्विसेज और सीएलआई टूल्स के लिए डिफ़ॉल्ट भाषा बन गई है।
---

## जाना क्यों मायने रखता है
- **डिज़ाइन द्वारा सरलता**: गो में केवल 25 कीवर्ड हैं। भाषा जानबूझकर छोटी है और सीखने में आसान है।
- **तेज संकलन**: बड़ी परियोजनाओं के लिए भी सेकंडों में सीधे मशीन कोड में संकलित हो जाता है।
- **अंतर्निहित समवर्ती**: गोरआउट्स और चैनल समवर्ती प्रोग्रामिंग को सुलभ और कुशल बनाते हैं।
- **उत्कृष्ट मानक पुस्तकालय**: HTTP सर्वर, JSON एन्कोडिंग, परीक्षण, क्रिप्टोग्राफी - सभी अंतर्निहित।
- **स्टेटिक बायनेरिज़**: बिना किसी बाहरी निर्भरता के एकल बाइनरी में संकलित होता है। तैनाती तुच्छ है.
- **Google-स्केल वंशावली**: उन इंजीनियरों द्वारा डिज़ाइन किया गया जिन्होंने यूनिक्स, UTF-8 और Google के अधिकांश बुनियादी ढांचे का निर्माण किया।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **कोई योग प्रकार/पैटर्न मिलान नहीं** | संबंधित डेटा के साथ कोई गणना नहीं, कोई बीजगणितीय प्रकार नहीं | इंटरफेस और टाइप स्विच का उपयोग करें |
| **वर्बोसिटी को संभालने में त्रुटि** | यदि ग़लती हो तो स्पष्ट करें !=शून्य हर जगह जाँच करें | पैटर्न स्वीकार करें; यह त्रुटि प्रबंधन को दृश्यमान बनाता है |
| **छोटा पारिस्थितिकी तंत्र** | पायथन, जावा, या जावास्क्रिप्ट की तुलना में कम पुस्तकालय | मानक पुस्तकालय अधिकांश आवश्यकताओं को पूरा करता है; सामुदायिक पैकेज बढ़ रहे हैं |
| **कोई GUI ढाँचा नहीं** | डेस्कटॉप या मोबाइल यूआई के लिए उपयुक्त नहीं है | वेब-आधारित यूआई (डब्ल्यूएएसएम) या किसी अन्य भाषा का उपयोग करें |
| **कचरा संग्रहकर्ता** | एक GC है - विराम छोटे हैं लेकिन गैर-शून्य हैं | विलंबता-संवेदनशील कार्यभार के लिए GC ट्यून करें; सिंक.पूल का उपयोग करें |
---

## सिंटेक्स बुनियादी बातें
### बुनियादी संरचना
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

### कार्य
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

### संरचनाएं और इंटरफेस
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

### त्रुटि प्रबंधन
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

### संगामिति--गोरूटीन्स और चैनल
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

## उन्नत सिंटैक्स और पैटर्न
### जेनेरिक (जाओ 1.18+)
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

### उन्नत पैटर्न मिलान (प्रकार स्विच)
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

### कस्टम त्रुटि रैपिंग
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

## समवर्ती एवं समांतरता (गहरा गोता)
### वर्कर पूल पैटर्न
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

### रद्द करने का संदर्भ
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

### मल्टीप्लेक्सिंग के लिए चयन करें
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना संरचना
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

### गो.मॉड
```
module github.com/example/my_project

go 1.22

require (
    github.com/gin-gonic/gin v1.10.0
    github.com/go-sql-driver/mysql v1.8.0
    go.uber.org/zap v1.27.0
)
```

### आवश्यक आदेश
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

### सीआई/सीडी पाइपलाइन (गिटहब क्रियाएँ)
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

## परीक्षण
### यूनिट परीक्षण
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

### टेबल-संचालित HTTP परीक्षण
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

## अंतरसंचालनीयता
### सीजीओ (गो से सी को कॉल करना)
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

### अन्य भाषाओं के साथ एफएफआई
| दिशा | तंत्र |
|----|----|
| जाओ C को बुलाओ | सीजीओ (`import "C"`) |
| C++ पर कॉल करें | सीजीओ + सी रैपर फ़ंक्शन |
| सी कॉलिंग गो |`//export`| के साथ निर्यात गो फ़ंक्शन
| जाओ पाइथॉन को बुलाओ | गोपी या उपप्रक्रिया का प्रयोग करें |
---

## डिज़ाइन पैटर्न
### मिडलवेयर पैटर्न (HTTP)
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

### विकल्प पैटर्न
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

## प्रदर्शन एवं अनुकूलन
### प्रोफ़ाइलिंग
```bash
go test -cpuprofile=cpu.prof -bench=. ./...
go tool pprof cpu.prof
go test -memprofile=mem.prof -bench=. ./...
go tool pprof mem.prof
```

### अनुकूलन युक्तियाँ
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

## तैनाती
### क्रॉस-संकलन
```bash
GOOS=linux GOARCH=amd64 go build -o myapp-linux
GOOS=windows GOARCH=amd64 go build -o myapp.exe
GOOS=darwin GOARCH=arm64 go build -o myapp-mac
```

### डॉकर परिनियोजन
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

## मानक पुस्तकालय
| पैकेज | उद्देश्य |
|---------|---------|
| एफएमटी | स्वरूपित I/O |
| नेट/एचटीटीपी | HTTP क्लाइंट और सर्वर |
| एन्कोडिंग/जेसन | JSON एन्कोडिंग/डिकोडिंग |
| ओएस | ओएस-स्तरीय संचालन |
| आईओ | I/O आदिम |
| स्ट्रिंग्स / strconv | स्ट्रिंग हेरफेर |
| सिंक | म्यूटेक्स, वेटग्रुप, वन्स |
| प्रसंग | समय सीमा, रद्दीकरण |
| परीक्षण | अंतर्निहित परीक्षण ढाँचा |
| लॉग / लॉग / स्लॉग | लॉगिंग |
| समय | समय एवं अवधि |
| क्रिप्टो | क्रिप्टोग्राफी (टीएलएस, हैशिंग) |
| डेटाबेस/एसक्यूएल | डेटाबेस अमूर्तन |
---

## टूलींग
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

## गो का उपयोग कब करें
| परिदृश्य | क्यों जाएं | बेहतर विकल्प |
|---|--------|-----|
| क्लाउड-नेटिव सेवाएँ / माइक्रोसर्विसेज | तेज़, छोटी बायनेरिज़, उत्कृष्ट HTTP | अधिकतम प्रदर्शन के लिए जंग |
| सीएलआई उपकरण | तेज़ संकलन, एकल बाइनरी | जटिल सीएलआई के लिए जंग |
| वेब सर्वर/एपीआई | अंतर्निहित HTTP, तेज़, सरल | रैपिड प्रोटोटाइप के लिए Node.js/Express |
| DevOps टूलींग | डॉकर, कुबेरनेट्स, टेराफॉर्म गो हैं | स्क्रिप्टिंग के लिए पायथन |
| समवर्ती प्रणालियाँ | गोरोइन हल्के और सुरुचिपूर्ण हैं | दोष-सहिष्णु संगामिति के लिए एर्लैंग/एलिक्सिर |
| नेटवर्क प्रोग्रामिंग | उत्कृष्ट नेट पैकेज | निम्नतम स्तर के नियंत्रण के लिए C/C++ |
| डेटा साइंस/एमएल | सही पारिस्थितिकी तंत्र नहीं | पायथन, आर |
| डेस्कटॉप/मोबाइल जीयूआई | कोई GUI ढांचा नहीं | वेब फ्रंटएंड या मूल भाषा का उपयोग करें |
| एंबेडेड सिस्टम | बहुत भारी (जीसी, रनटाइम) | सी, जंग |
---

## सिंथेटिक प्रश्नोत्तर
### Q1: गो में अपवाद क्यों नहीं हैं? मुझे त्रुटियों को कैसे संभालना चाहिए?
**ए:** गो अपवादों के बजाय स्पष्ट त्रुटि रिटर्न का उपयोग करता है। प्रत्येक फ़ंक्शन जो विफल हो सकता है वह अपने अंतिम रिटर्न मान के रूप में एक`error`लौटाता है। यह कॉल करने वाले को त्रुटियों को स्पष्ट रूप से संभालने के लिए मजबूर करता है - कोई मूक विफलता या भूले हुए कैच ब्लॉक नहीं। मुहावरेदार पैटर्न`if err != nil`है। रैपिंग त्रुटियों के लिए`%w`के साथ`fmt.Errorf`का उपयोग करें, और त्रुटि प्रकारों की जाँच के लिए`errors.Is`/`errors.As`का उपयोग करें। पुनर्प्राप्त न की जा सकने वाली त्रुटियों (प्रोग्रामिंग बग) के लिए,`panic`का उपयोग करें।
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

### Q2: गोरूटाइन क्या हैं, और वे ओएस थ्रेड से कैसे भिन्न हैं?
**ए:** गोरूटाइन हल्के वजन वाले, उपयोगकर्ता-स्पेस थ्रेड हैं जिन्हें गो रनटाइम द्वारा प्रबंधित किया जाता है। वे ~2KB स्टैक (बनाम OS थ्रेड के लिए ~1MB) से शुरू होते हैं, शेड्यूलर द्वारा OS थ्रेड पर मल्टीप्लेक्स किए जाते हैं, और एक समय में लाखों बनाए जा सकते हैं। गोरोइन के बीच संचार चैनल (या साझा स्थिति के लिए`sync`प्राइमेटिव) का उपयोग करता है। गोरोइन लीक से बचने के लिए हमेशा`sync.WaitGroup`या संदर्भ रद्दीकरण का उपयोग करें।
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

### Q3: मुझे समवर्तीता के लिए चैनल बनाम म्यूटेक्स का उपयोग कब करना चाहिए?
**ए:** जब गोरआउट्स को डेटा संचार करने की आवश्यकता होती है तो चैनलों का उपयोग करें - वे "संचार करके मेमोरी साझा करें" दर्शन को लागू करते हैं। जब गोरआउट्स को साझा स्थिति (कैश, काउंटर, कनेक्शन पूल) की सुरक्षा की आवश्यकता होती है तो म्यूटेक्स (`sync.Mutex`) का उपयोग करें। एक अच्छा नियम: यदि डेटा गोरआउट्स के बीच पारित किया जा रहा है, तो चैनलों का उपयोग करें; यदि डेटा को एकाधिक गोरआउट्स द्वारा एक्सेस किया जा रहा है, तो म्यूटेक्स का उपयोग करें। सरल परमाणु संचालन के लिए,`sync/atomic`का उपयोग करें।
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

### Q4:`nil`स्लाइस/मानचित्र और खाली वाले के बीच क्या अंतर है?
**ए:** एक`nil`स्लाइस (`var s []int`) में कोई अंतर्निहित सरणी नहीं है, लंबाई 0, क्षमता 0. एक खाली स्लाइस (`s := []int{}` या `make([]int, 0)`) में एक अंतर्निहित सरणी है लेकिन लंबाई 0 है। दोनों `append`,`cap`, और`range`. JSON मार्शलिंग अलग है: शून्य स्लाइस`null`बन जाते हैं, खाली स्लाइस`[]`बन जाते हैं। सर्वोत्तम अभ्यास: रिटर्न मानों के लिए शून्य स्लाइस को प्राथमिकता दें (वे "कोई डेटा नहीं" दर्शाते हैं), जब JSON आउटपुट मायने रखता है तो खाली स्लाइस को प्राथमिकता दें।
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

### Q5: गो में इंटरफेस कैसे काम करते हैं, और खाली इंटरफ़ेस क्या है?
**ए:** गो इंटरफेस पूरी तरह से संतुष्ट हैं - एक प्रकार बिना किसी`implements`कीवर्ड के अपने तरीकों को लागू करके एक इंटरफ़ेस लागू करता है। यह वियुग्मन और संयोजन को सक्षम बनाता है। खाली इंटरफ़ेस`interface{}`(या Go 1.18+ में `any`) हर प्रकार से संतुष्ट है - इसे संयम से उपयोग करें (जेनेरिक अक्सर बेहतर होते हैं)। इंटरफ़ेस मान जोड़े हैं: `(type, value)`। शून्य इंटरफ़ेस में दोनों शून्य हैं।
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

## चेन-ऑफ़-थॉट समस्या का समाधान
### समस्या 1: दर सीमा के साथ एक समवर्ती वेब स्क्रैपर बनाएं
**समस्या कथन:** एक गो प्रोग्राम बनाएं जो एक साथ सूची से यूआरएल लाता है, पेज शीर्षक निकालता है, प्रति सेकंड 10 अनुरोधों की दर सीमा का सम्मान करता है, और डेटा दौड़ के बिना परिणाम एकत्र करता है।
**चरण 1 - समस्या को समझें:**
हमें चाहिए: (1) गोरआउट्स के साथ समवर्ती HTTP फ़ेचिंग, (2) भारी सर्वर से बचने के लिए दर सीमित करना, (3) दौड़ के बिना परिणाम संग्रह, (4) विफल अनुरोधों के लिए उचित त्रुटि प्रबंधन। गो के समवर्ती प्रिमिटिव (गोरआउटिन, चैनल, `errgroup`) इसके लिए आदर्श हैं।
**चरण 2 - दृष्टिकोण को पहचानें:**
- टोकन-बकेट दर सीमित करने के लिए`golang.org/x/time/rate`का उपयोग करें।
- गोरआउट्स को प्रबंधित करने के लिए`sync.WaitGroup`या`errgroup.Group`का उपयोग करें।
- आउटपुट को सुरक्षित रूप से एकत्र करने के लिए परिणाम चैनल का उपयोग करें।
- रद्दीकरण और टाइमआउट के लिए`context.Context`का उपयोग करें।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- कोई डेटा दौड़ नहीं: प्रत्येक गोरोइन`results`में अपने स्वयं के सूचकांक को लिखता है - किसी म्यूटेक्स की आवश्यकता नहीं है।
-`errgroup.SetLimit`दर सीमक से स्वतंत्र रूप से संगामिति को सीमित करता है।
-`io.LimitReader`अत्यधिक बड़े पृष्ठों को पढ़ने से रोकता है।
-`http.NewRequestWithContext`यह सुनिश्चित करता है कि संदर्भ पूरा होने पर अनुरोध रद्द कर दिए जाएं।
- उत्पादन के लिए: घातीय बैकऑफ़, कनेक्शन पूलिंग ट्यूनिंग और मेट्रिक्स के साथ पुनः प्रयास तर्क जोड़ें।
### समस्या 2: जेनेरिक एलआरयू कैश लागू करें
**समस्या कथन:** जेनेरिक (गो 1.18+) का उपयोग करके गो में थ्रेड-सुरक्षित, जेनेरिक एलआरयू (कम से कम हाल ही में प्रयुक्त) कैश लागू करें। इसे O(1) समय जटिलता के साथ`Get`,`Set`और`Delete`का समर्थन करना चाहिए।
**चरण 1 - समस्या को समझें:**
LRU कैश को O(1) लुकअप (हैश मैप) और O(1) ऑर्डरिंग अपडेट (दोगुनी लिंक्ड सूची) की आवश्यकता होती है।`Get`पर: आइटम को सामने ले जाएं।`Set`पर: सामने डालें; क्षमता से अधिक होने पर पीछे से बेदखल करें। थ्रेड सुरक्षा के लिए म्यूटेक्स की आवश्यकता होती है।
**चरण 2 - दृष्टिकोण को पहचानें:**
- O(1) को आगे से आगे ले जाने और पीछे से हटाने के लिए`container/list`(दोगुनी लिंक की गई सूची) का उपयोग करें।
- O(1) लुकअप के लिए`map[K]*list.Element`का उपयोग करें।
- थ्रेड सुरक्षा के लिए`sync.Mutex`का उपयोग करें।
- प्रकार की सुरक्षा के लिए जेनरिक (`[K comparable, V any]`)।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
-`Get`,`Set`,`Delete`के लिए O(1) : मानचित्र लुकअप O(1) औसत है; सूची संचालन (`MoveToFront`, `PushFront`, `Remove`, `Back`) सभी O(1) हैं।
- थ्रेड सुरक्षा:`sync.Mutex`यह सुनिश्चित करता है कि एक समय में केवल एक गोरोइन कैश तक पहुंच सके। भारी कार्यभार के लिए,`sync.RWMutex`का उपयोग करें।
- जेनेरिक्स:`[K comparable, V any]`सुनिश्चित करता है कि कुंजियाँ`==`(मानचित्र कुंजियों के लिए आवश्यक) का समर्थन करती हैं, जबकि मान किसी भी प्रकार के हो सकते हैं।
- उत्पादन:`github.com/hashicorp/golang-lru/v2`पर विचार करें - कम लॉक विवाद के लिए टीटीएल समर्थन और शार्डिंग के साथ युद्ध-परीक्षण किया गया।
### समस्या 3: एक टीसीपी चैट सर्वर बनाएं
**समस्या कथन:** एक समवर्ती टीसीपी चैट सर्वर बनाएं जहां क्लाइंट कनेक्ट हो सकें, अन्य सभी कनेक्टेड क्लाइंट्स को संदेश प्रसारित कर सकें, और शानदार तरीके से डिस्कनेक्ट कर सकें। दूसरों को रोके बिना धीमे ग्राहकों को संभालें।
**चरण 1 - समस्या को समझें:**
हमें चाहिए: (1) टीसीपी कनेक्शन स्वीकार करें, (2) पढ़ने के लिए प्रति ग्राहक एक गोरोइन, (3) सभी ग्राहकों को संदेश भेजने के लिए एक प्रसारण तंत्र, (4) डिस्कनेक्शन और धीमे क्लाइंट को संभालना। यह एक क्लासिक फैन-आउट पैटर्न है।
**चरण 2 - दृष्टिकोण को पहचानें:**
- टीसीपी कनेक्शन के लिए`net.Listener`का उपयोग करें।
- ग्राहक पंजीकरण/पंजीकरण/प्रसारण के लिए चैनलों के साथ एक केंद्रीय`hub`गोरोइन का उपयोग करें।
- प्रत्येक क्लाइंट को बफ़र किए गए चैनल के साथ एक समर्पित राइट गोरोइन मिलता है - धीमे क्लाइंट दूसरों को ब्लॉक नहीं करते हैं।
- सुंदर शटडाउन के लिए`context.Context`का उपयोग करें।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- धीमी क्लाइंट हैंडलिंग: प्रसारण में`default`के साथ`select`ब्लॉकिंग को रोकता है। यदि धीमे क्लाइंट का बफ़र भर जाता है तो वे डिस्कनेक्ट हो जाते हैं।
- कोई दौड़ नहीं: हब गोरोइन`clients`मानचित्र का एकल लेखक है; `mu`प्रसारण के दौरान पढ़ने की सुरक्षा करता है।
- शानदार शटडाउन: श्रोता और ड्रेन कनेक्शन को बंद करने के लिए`context.Context`और एक सिग्नल हैंडलर जोड़ें।
- उत्पादन: ब्राउज़र क्लाइंट के लिए`golang.org/x/net/websocket`का उपयोग करने पर विचार करें, और प्रमाणीकरण, संदेश इतिहास और कमरे जोड़ें।
---

## सारांश
गो एक ऐसी भाषा है जो जानबूझकर सुविधाओं के स्थान पर सरलता को चुनती है। इसमें अधिकांश भाषाओं की तुलना में कम संरचनाएं हैं - कोई विरासत नहीं, कोई विधि ओवरलोडिंग नहीं, कोई अपवाद नहीं, कोई मैक्रोज़ नहीं - और यह एक ताकत है। परिणाम वह कोड है जिसे पढ़ना आसान है, लिखना आसान है और बनाए रखना आसान है। गो का समवर्ती मॉडल (गोरआउट्स और चैनल) किसी भी भाषा में सबसे अच्छे डिज़ाइन में से एक है। क्लाउड इंफ्रास्ट्रक्चर, माइक्रोसर्विसेज, सीएलआई टूल्स और नेटवर्क प्रोग्रामिंग के लिए, गो एक उत्कृष्ट विकल्प है।