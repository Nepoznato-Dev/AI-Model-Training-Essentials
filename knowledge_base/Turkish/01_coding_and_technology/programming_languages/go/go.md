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
# Gitmek
Go (orijinal alan adından dolayı genellikle "Golang" olarak anılır), Google'da Robert Griesemer, Rob Pike ve Ken Thompson tarafından tasarlanan statik olarak yazılmış, derlenmiş bir programlama dilidir. İlk olarak 2012 yılında sistem programlama için daha iyi bir dil olma hedefiyle piyasaya sürüldü; C'nin performansını Python gibi dinamik dillerin üretkenliğiyle birleştiren bir dil. Go, basitliği, hızlı derlemesi, yerleşik eşzamanlılığı (goroutinler ve kanallar) ve mükemmel araçlarıyla tanınır.
Go, bulut altyapısı ekosisteminin büyük bir kısmına güç sağlar: Docker, Kubernetes, Terraform, Prometheus vb. ve Go standart kitaplığının HTTP sunucusunun tümü Go'da yazılmıştır. Bulutta yerel geliştirme, mikro hizmetler ve CLI araçları için varsayılan dil haline geldi.
---

## Gitmek Neden Önemlidir
- **Tasarım gereği basitlik**: Go'da yalnızca 25 anahtar kelime vardır. Dil kasıtlı olarak küçüktür ve öğrenmesi kolaydır.
- **Hızlı derleme**: Büyük projeler için bile saniyeler içinde doğrudan makine koduna derlenir.
- **Yerleşik eşzamanlılık**: Goroutinler ve kanallar eşzamanlı programlamayı erişilebilir ve verimli hale getirir.
- **Mükemmel standart kitaplık**: HTTP sunucusu, JSON kodlaması, test etme, şifreleme - hepsi yerleşik.
- **Statik ikili dosyalar**: Harici bağımlılıklar olmadan tek bir ikili dosyaya derlenir. Dağıtım önemsizdir.
- **Google ölçeğinde soyağacı**: Unix, UTF-8 ve Google altyapısının çoğunu oluşturan mühendisler tarafından tasarlanmıştır.
## Takaslar
| Sınırlama | Ayrıntılar | Tipik Geçici Çözüm |
|-----------|------------|-----------|
| **Toplam türü/örüntü eşleşmesi yok** | İlişkili verilere sahip numaralandırma yok, cebirsel tür yok | Arayüzleri kullanın ve anahtarları yazın |
| **Ayrıntıların işlenmesinde hata oluştu** | Açık if err != nil her yeri kontrol eder | Deseni kabul edin; hata işlemeyi görünür hale getirir |
| **Daha küçük ekosistem** | Python, Java veya JavaScript'ten daha az kitaplık | Standart kütüphane çoğu ihtiyacı karşılar; topluluk paketleri büyüyor |
| **GUI çerçevesi yok** | Masaüstü veya mobil kullanıcı arayüzleri için uygun değildir | Web tabanlı kullanıcı arayüzlerini (WASM) veya başka bir dili kullanın |
| **Çöp toplayıcı** | GC'si var -- duraklamalar küçük ama sıfır değil | Gecikmeye duyarlı iş yükleri için GC'yi ayarlayın; senkronizasyon havuzunu kullanın |
---

## Söz Diziminin Temelleri
### Temel Yapı
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

### İşlevler
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

### Yapılar ve Arayüzler
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

### Hata İşleme
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

### Eşzamanlılık -- Goroutinler ve Kanallar
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

## Gelişmiş Sözdizimi ve Desenler
### Jenerikler (1.18+ sürümüne geçin)
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

### Gelişmiş Desen Eşleştirme (Tip Anahtarları)
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

### Özel Hata Sarma
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

## Eşzamanlılık ve Paralellik (Derin İnceleme)
### İşçi Havuzu Modeli
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

### İptal İçeriği
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

### Çoğullama için seçin
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

## Proje Yapılandırması ve Oluşturma Sistemi
### Proje Yapısı
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

### Temel Komutlar
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

### CI/CD İşlem Hattı (GitHub Eylemleri)
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

## Test etme
### Birim Testleri
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

### Tabloya Dayalı HTTP Testleri
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

## Birlikte Çalışabilirlik
### CGo (Go'dan C'yi çağırmak)
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

### Diğer Dillerle FFI
| Yön | Mekanizma |
|-----------|---------------|
| C'yi aramaya gidin | cgo (`import "C"`) |
| C++'ı aramaya başlayın | cgo + C sarmalayıcı işlevleri |
| C Go'yu arıyor | Go işlevlerini`//export`ile dışa aktarın |
| Python'u aramaya gidin | Gopy veya alt işlemi kullanın |
---

## Tasarım Desenleri
### Ara Yazılım Kalıbı (HTTP)
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

### Seçenek Deseni
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

## Performans ve Optimizasyon
### Profil Oluşturma
```bash
go test -cpuprofile=cpu.prof -bench=. ./...
go tool pprof cpu.prof
go test -memprofile=mem.prof -bench=. ./...
go tool pprof mem.prof
```

### Optimizasyon İpuçları
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

## Dağıtım
### Çapraz Derleme
```bash
GOOS=linux GOARCH=amd64 go build -o myapp-linux
GOOS=windows GOARCH=amd64 go build -o myapp.exe
GOOS=darwin GOARCH=arm64 go build -o myapp-mac
```

### Docker Dağıtımı
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

## Standart Kütüphane
| Paket | Amaç |
|-----------|-----------|
| fmt | Biçimlendirilmiş G/Ç |
| ağ/http | HTTP istemcisi ve sunucusu |
| kodlama/json | JSON kodlama/kod çözme |
| işletim sistemi | İşletim sistemi düzeyinde işlemler |
| io | G/Ç temelleri |
| dizeler / strconv | Dize manipülasyonu |
| senkronizasyon | Mutex, WaitGroup, Bir Kez |
| bağlam | Son teslim tarihleri, iptal |
| test etme | Yerleşik test çerçevesi |
| günlük / günlük/slog | Günlük |
| zaman | Zaman ve süre |
| kripto | Kriptografi (TLS, karma) |
| veritabanı/sql | Veritabanı soyutlaması |
---

## Takımlama
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

## Go Ne Zaman Kullanılmalı?
| Senaryo | Neden Gitmelisiniz | Daha İyi Alternatif |
|----------|------------|-----|
| Bulutta yerel hizmetler / mikro hizmetler | Hızlı, küçük ikili dosyalar, mükemmel HTTP | Maksimum performans için pas |
| CLI araçları | Hızlı derleme, tek ikili | Karmaşık CLI'ler için pas |
| Web sunucuları / API'ler | Yerleşik HTTP, hızlı, basit | Hızlı prototip oluşturma için Node.js/Express |
| DevOps araçları | Docker, Kubernetes, Terraform Yayında | Komut dosyası yazmak için Python |
| Eşzamanlı sistemler | Goroutinler hafif ve zariftir | Hataya dayanıklı eşzamanlılık için Erlang/Elixir |
| Ağ programlama | Mükemmel net paket | En düşük düzey kontrol için C/C++ |
| Veri bilimi / ML | Doğru ekosistem değil | Python, R |
| Masaüstü/mobil GUI | GUI çerçevesi yok | Bir web ön ucu veya yerel dil kullanın |
| Gömülü sistemler | Çok ağır (GC, çalışma zamanı) | C, Pas |
---

## Özet
Go, özellikler yerine basitliği bilinçli olarak seçen bir dildir. Çoğu dilden daha az yapıya sahiptir; kalıtım yoktur, aşırı yöntem yüklemesi yoktur, istisna yoktur, makro yoktur ve bu güçlü bir yöndür. Sonuç, okunması kolay, yazılması kolay ve bakımı kolay bir koddur. Go'nun eşzamanlılık modeli (goroutinler ve kanallar) herhangi bir dilde en iyi tasarlanmış modellerden biridir. Bulut altyapısı, mikro hizmetler, CLI araçları ve ağ programlama için Go mükemmel bir seçimdir.