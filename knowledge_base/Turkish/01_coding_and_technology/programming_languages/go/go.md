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
# Gitmek
Go (orijinal alan adından dolayı genellikle "Golang" olarak anılır), Google'da Robert Griesemer, Rob Pike ve Ken Thompson tarafından tasarlanan statik olarak yazılmış, derlenmiş bir programlama dilidir. İlk olarak 2012 yılında sistem programlama için daha iyi bir dil olma hedefiyle piyasaya sürüldü; C'nin performansını Python gibi dinamik dillerin üretkenliğiyle birleştiren bir dil. Go, basitliği, hızlı derlemesi, yerleşik eşzamanlılığı (goroutinler ve kanallar) ve mükemmel araçlarıyla tanınır.
Go, bulut altyapısı ekosisteminin büyük bir kısmına güç verir: Docker, Kubernetes, Terraform, Prometheus, vb. ve Go standart kitaplığının HTTP sunucusunun tümü Go'da yazılmıştır. Bulutta yerel geliştirme, mikro hizmetler ve CLI araçları için varsayılan dil haline geldi.
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

### Gelişmiş Desen Eşleştirme (Tür Anahtarları)
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
| C Go'yu arıyor |`//export`ile Go işlevlerini dışa aktarın |
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

## Sentetik Soru-Cevap
### S1: Go'nun neden istisnaları yok? Hataları nasıl ele almalıyım?
**C:** Go, istisnalar yerine açık hata dönüşlerini kullanır. Başarısız olabilecek her işlev, son dönüş değeri olarak bir`error`döndürür. Bu, arayan kişiyi hataları açıkça ele almaya zorlar; sessiz hatalar veya unutulmuş yakalama blokları olmaz. Deyimsel kalıp `if err != nil`'dir. Sarma hataları için`fmt.Errorf`ile `%w`'yi ve hata türlerini kontrol etmek için`errors.Is`/ `errors.As`'yi kullanın. Kurtarılamaz hatalar (programlama hataları) için`panic`kullanın.
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

### S2: Goroutinler nedir ve bunların işletim sistemi iş parçacıklarından farkı nedir?
**C:** Goroutinler, Go çalışma zamanı tarafından yönetilen hafif, kullanıcı alanı iş parçacıklarıdır. ~2KB yığınla başlarlar (işletim sistemi iş parçacıkları için ~1MB'a karşılık), zamanlayıcı tarafından işletim sistemi iş parçacıklarına çoğullanırlar ve bir kerede milyonlarca oluşturulabilirler. Goroutinler arasındaki iletişim kanalları (veya paylaşılan durum için`sync`temel öğelerini) kullanır. Goroutine sızıntılarını önlemek için her zaman`sync.WaitGroup`veya bağlam iptalini kullanın.
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

### S3: Eşzamanlılık için kanalları ve muteksleri ne zaman kullanmalıyım?
**C:** Goroutinlerin veri iletmesi gerektiğinde kanalları kullanın; bunlar "iletişim kurarak hafızayı paylaş" felsefesini uygular. Goroutinlerin paylaşılan durumu (önbellekler, sayaçlar, bağlantı havuzları) koruması gerektiğinde muteksleri (`sync.Mutex`) kullanın. İyi bir kural: Goroutinler arasında veri aktarılıyorsa kanalları kullanın; eğer verilere birden fazla goroutin tarafından erişiliyorsa, bir muteks kullanın. Basit atomik işlemler için`sync/atomic`kullanın.
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

### S4:`nil`dilimleri/haritaları ile boş dilimler/haritalar arasındaki fark nedir?
**A:** Bir`nil`diliminin (`var s []int`) temel dizisi yoktur, uzunluğu 0, kapasitesi 0'dır. Boş bir dilimin (`s := []int{}`veya`make([]int, 0)`) temel dizisi vardır ancak uzunluğu 0'dır. Her ikisi de`append`,`len`,`cap`ile aynı şekilde çalışır ve`range`. JSON sıralaması farklıdır: sıfır dilimler`null`olur, boş dilimler`[]`olur. En iyi uygulama: dönüş değerleri için sıfır dilimleri tercih edin ("veri olmadığını" belirtirler), JSON çıktısı önemli olduğunda boş dilimleri tercih edin.
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

### S5: Go'da arayüzler nasıl çalışır ve boş arayüz nedir?
**C:** Go arayüzleri örtülü olarak karşılanır; bir tür,`implements`anahtar sözcüğü olmadan, kendi yöntemlerini uygulayarak bir arayüzü uygular. Bu, ayrıştırmayı ve kompozisyonu mümkün kılar. Boş arayüz`interface{}`(veya Go 1.18+ sürümünde `any`) her tür tarafından karşılanır; onu dikkatli kullanın (jenerikler genellikle daha iyidir). Arayüz değerleri çiftlerdir:`(type, value)`. Sıfır bir arayüzde her ikisi de sıfırdır.
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

## Düşünce Zinciri Problem Çözme
### Sorun 1: Hız Sınırlamayla Eşzamanlı bir Web Kazıyıcı Oluşturun
**Sorun Açıklaması:** Eş zamanlı olarak bir listeden URL'ler getiren, sayfa başlıklarını çıkaran, saniyede 10 isteklik hız sınırına uyan ve verileri veri yarışı olmadan toplayan bir Go programı oluşturun.
**1. Adım — Sorunu Anlayın:**
Şunlara ihtiyacımız var: (1) goroutinlerle eş zamanlı HTTP alma, (2) sunucuların aşırı yüklenmesini önlemek için hız sınırlama, (3) yarışsız sonuç toplama, (4) başarısız istekler için uygun hata işleme. Go'nun eşzamanlılık temelleri (goroutinler, kanallar, `errgroup`) bunun için idealdir.
**2. Adım — Yaklaşımı Belirleyin:**
- Belirteç kovası hızı sınırlaması için`golang.org/x/time/rate`kullanın.
- Goroutinleri yönetmek için`sync.WaitGroup`veya`errgroup.Group`kullanın.
- Çıktıları güvenli bir şekilde toplamak için bir sonuç kanalı kullanın.
- İptal ve molalar için`context.Context`kullanın.
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
- Veri yarışı yok: her goroutine `results`'de kendi dizinine yazar — mutekse gerek yoktur.
-`errgroup.SetLimit`eşzamanlılığı hız sınırlayıcıdan bağımsız olarak sınırlar.
-`io.LimitReader`aşırı büyük sayfaların okunmasını engeller.
- `http.NewRequestWithContext`, bağlam tamamlandığında isteklerin iptal edilmesini sağlar.
- Üretim için: üstel geri çekilme, bağlantı havuzu oluşturma ayarı ve ölçümlerle yeniden deneme mantığı ekleyin.
### Sorun 2: Genel bir LRU Önbelleği Uygulama
**Sorun Açıklaması:** Jenerikleri (Go 1.18+) kullanarak Go'da iş parçacığı açısından güvenli, genel bir LRU (En Son Kullanılan) önbellek uygulayın. O(1) zaman karmaşıklığıyla `Get`,`Set`ve `Delete`'yi desteklemelidir.
**1. Adım — Sorunu Anlayın:**
Bir LRU önbelleğinin O(1) aramasına (karma haritası) ve O(1) sipariş güncellemelerine (çift bağlantılı liste) ihtiyacı vardır. `Get`'de: öğeyi öne taşı. `Set`'de: ön tarafa takın; kapasitenin üzerindeyse arkadan tahliye edin. İş parçacığı güvenliği bir muteks gerektirir.
**2. Adım — Yaklaşımı Belirleyin:**
- O(1) öne doğru hareket etme ve arkadan kaldırma için`container/list`(çift bağlantılı liste) kullanın.
- O(1) araması için`map[K]*list.Element`kullanın.
- İplik güvenliği için`sync.Mutex`kullanın.
- Tip güvenliği için jenerikler (`[K comparable, V any]`).
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
-`Get`,`Set`,`Delete`için O(1): harita araması O(1) ortalamasıdır; liste işlemlerinin (`MoveToFront`,`PushFront`,`Remove`,`Back`) tümü O(1)'dir.
- İş parçacığı güvenliği: `sync.Mutex`, önbelleğe aynı anda yalnızca bir goroutine erişmesini sağlar. Okuma ağırlıklı iş yükleri için`sync.RWMutex`kullanın.
- Jenerikler: `[K comparable, V any]`, anahtarların`==`(harita anahtarları için gerekli) desteğini sağlarken değerler herhangi bir türde olabilir.
- Üretim: `github.com/hashicorp/golang-lru/v2`'yi düşünün — daha az kilit çekişmesi için TTL desteği ve parçalama ile savaşta test edilmiştir.
### Sorun 3: TCP Sohbet Sunucusu Oluşturun
**Sorun Açıklaması:** İstemcilerin bağlanabileceği, diğer tüm bağlı istemcilere mesaj yayınlayabileceği ve bağlantıyı sorunsuz bir şekilde kesebileceği eşzamanlı bir TCP sohbet sunucusu oluşturun. Yavaş istemcileri başkalarını engellemeden yönetin.
**1. Adım — Sorunu Anlayın:**
Şunlara ihtiyacımız var: (1) TCP bağlantılarını kabul etmek, (2) istemci başına okumak için bir goroutine, (3) tüm istemcilere mesaj göndermek için bir yayın mekanizması, (4) bağlantı kesintilerini ve yavaş istemcileri ele almak. Bu klasik bir yelpazeleme modelidir.
**2. Adım — Yaklaşımı Belirleyin:**
- TCP bağlantıları için`net.Listener`kullanın.
- İstemci kaydı/kayıt silme/yayın için kanallarla merkezi bir`hub`goroutine kullanın.
- Her istemci, ara belleğe alınmış bir kanala sahip özel bir yazma yordamı alır; yavaş istemciler diğerlerini engellemez.
- Sorunsuz bir kapatma için`context.Context`kullanın.
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
- Yavaş istemci kullanımı: Yayında`default`içeren `select`, engellemeyi önler. Yavaş istemcilerin ara bellekleri dolarsa bağlantıları kesilir.
- Yarış yok: Hub goroutine,`clients`haritasının tek yazarıdır; `mu`yayın sırasında okumaları korur.
- Sorunsuz kapatma: dinleyiciyi ve drenaj bağlantılarını kapatmak için`context.Context`ve bir sinyal işleyici ekleyin.
- Üretim: Tarayıcı istemcileri için`golang.org/x/net/websocket`kullanmayı düşünün ve kimlik doğrulama, mesaj geçmişi ve odalar ekleyin.
---

## Özet
Go, özellikler yerine basitliği bilinçli olarak seçen bir dildir. Çoğu dilden daha az yapıya sahiptir; kalıtım yoktur, aşırı yöntem yüklemesi yoktur, istisna yoktur, makro yoktur ve bu güçlü bir yöndür. Sonuç, okunması kolay, yazılması kolay ve bakımı kolay bir koddur. Go'nun eşzamanlılık modeli (goroutinler ve kanallar) herhangi bir dilde en iyi tasarlanmış modellerden biridir. Bulut altyapısı, mikro hizmetler, CLI araçları ve ağ programlama için Go mükemmel bir seçimdir.