---
# मेटाडेटा
शीर्षक: "जाओ"
विवरण: "गो प्रोग्रामिंग भाषा के लिए व्यापक संदर्भ जिसमें अवलोकन, ट्रेड-ऑफ़, सिंटैक्स बुनियादी बातें, पारिस्थितिकी तंत्र और इसका उपयोग कब करना है।"
श्रेणी: "कोडिंग और प्रौद्योगिकी"
संस्करण: "1.0.0"
स्थिति: "सक्रिय"
#योगदान
लेखक:
  - नाम: "एआई मॉडल ट्रेनिंग टीम"
    ईमेल: ""
    भूमिका: "मूल_लेखक"
योगदानकर्ता: []
चेंजलॉग:
  - संस्करण: "1.0.0"
    दिनांक: "2026-08-05"
    लेखक: "एआई मॉडल ट्रेनिंग टीम"
    परिवर्तन: "योगदानकर्ता ट्रैकिंग के लिए YAML फ्रंटमैटर मेटाडेटा जोड़ा गया"
#समीक्षा
बनाया गया: "2026-08-05"
अंतिम_संशोधित: "2026-08-05"
समीक्षा दिनांक: "2027-02-05"
इनके द्वारा समीक्षा: "कोडिंग और प्रौद्योगिकी ज्ञान आधार टीम"
अगली_समीक्षा: "2027-08-05"
#वर्गीकरण
टैग: [जाओ, प्रोग्रामिंग-भाषा, वाक्यविन्यास, पारिस्थितिकी तंत्र, कोडिंग-और-प्रौद्योगिकी]
कठिनाई_स्तर: "मध्यवर्ती"
पूर्वावश्यकताएँ: []
अनुमानित_पढ़ने_का समय: "30 मिनट"
# योगदान मार्गदर्शिका
योगदान:
  लाइसेंस: "एमआईटी"
  फीडबैक_चैनल: "गिटहब मुद्दे"
  कैसे_तो_योगदान करें: "परिवर्तनों के साथ एक पीआर सबमिट करें और चेंजलॉग अपडेट करें"
  समीक्षा_प्रक्रिया: "विलय से पहले श्रेणी अनुरक्षकों द्वारा परिवर्तनों की समीक्षा की जाती है"
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
| सी कॉलिंग गो |`//export`| के साथ एक्सपोर्ट गो फ़ंक्शन
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

## सारांश
गो एक ऐसी भाषा है जो जानबूझकर सुविधाओं के स्थान पर सरलता को चुनती है। इसमें अधिकांश भाषाओं की तुलना में कम संरचनाएं हैं - कोई विरासत नहीं, कोई विधि ओवरलोडिंग नहीं, कोई अपवाद नहीं, कोई मैक्रोज़ नहीं - और यह एक ताकत है। परिणाम वह कोड है जिसे पढ़ना आसान है, लिखना आसान है और बनाए रखना आसान है। गो का समवर्ती मॉडल (गोरआउट्स और चैनल) किसी भी भाषा में सबसे अच्छे डिज़ाइन में से एक है। क्लाउड इंफ्रास्ट्रक्चर, माइक्रोसर्विसेज, सीएलआई टूल्स और नेटवर्क प्रोग्रामिंग के लिए, गो एक उत्कृष्ट विकल्प है।