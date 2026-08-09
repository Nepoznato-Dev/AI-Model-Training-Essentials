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
# Pergi
Go (sering disebut "Golang" setelah nama domain aslinya) adalah bahasa pemrograman terkompilasi yang diketik secara statis dan dirancang di Google oleh Robert Griesemer, Rob Pike, dan Ken Thompson. Ini pertama kali dirilis pada tahun 2012 dengan tujuan eksplisit untuk menjadi bahasa yang lebih baik untuk pemrograman sistem -- bahasa yang menggabungkan kinerja C dengan produktivitas bahasa dinamis seperti Python. Go terkenal karena kesederhanaannya, kompilasi yang cepat, konkurensi bawaan (goroutine dan saluran), dan perkakas yang sangat baik.
Go mendukung sebagian besar ekosistem infrastruktur cloud: Docker, Kubernetes, Terraform, Prometheus, dll, dan server HTTP perpustakaan standar Go semuanya ditulis di Go. Ini telah menjadi bahasa default untuk pengembangan cloud-native, layanan mikro, dan alat CLI.
---

## Mengapa Go Penting
- **Kesederhanaan berdasarkan desain**: Go hanya memiliki 25 kata kunci. Bahasanya sengaja dibuat kecil dan mudah dipelajari.
- **Kompilasi cepat**: Mengkompilasi langsung ke kode mesin dalam hitungan detik, bahkan untuk proyek besar.
- **Konkurensi bawaan**: Goroutine dan saluran membuat pemrograman serentak dapat diakses dan efisien.
- **Perpustakaan standar yang luar biasa**: Server HTTP, pengkodean JSON, pengujian, kriptografi -- semuanya sudah ada di dalamnya.
- **Biner statis**: Mengkompilasi ke biner tunggal tanpa ketergantungan eksternal. Penempatan itu sepele.
- **silsilah berskala Google**: Dirancang oleh para insinyur yang membangun Unix, UTF-8, dan sebagian besar infrastruktur Google.
## Pengorbanan
| Batasan | Detail | Solusi Khas |
|-----------|---------|-------------------|
| **Tidak ada penjumlahan tipe/pola yang cocok** | Tidak ada enum dengan data terkait, tidak ada tipe aljabar | Gunakan antarmuka dan ketik switch |
| **Kesalahan menangani verbositas** | Eksplisit if err != nil cek di mana-mana | Terima polanya; itu membuat penanganan kesalahan terlihat |
| **Ekosistem yang lebih kecil** | Lebih sedikit perpustakaan dibandingkan Python, Java, atau JavaScript | Perpustakaan standar mencakup sebagian besar kebutuhan; paket komunitas berkembang |
| **Tanpa kerangka GUI** | Tidak cocok untuk UI desktop atau seluler | Gunakan UI berbasis web (WASM) atau bahasa lain |
| **Pemungut sampah** | Memiliki GC -- jedanya kecil namun bukan nol | Sesuaikan GC untuk beban kerja yang sensitif terhadap latensi; gunakan sinkronisasi.Pool |
---

## Dasar Sintaks
### Struktur Dasar
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

### Fungsi
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

### Struktur dan Antarmuka
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

### Penanganan Kesalahan
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

### Konkurensi -- Goroutine dan Saluran
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

## Sintaks & Pola Tingkat Lanjut
### Generik (Go 1.18+)
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

### Pencocokan Pola Tingkat Lanjut (Sakelar Tipe)
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

### Pembungkusan Kesalahan Khusus
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

## Konkurensi & Paralelisme (Menyelami Lebih Dalam)
### Pola Kelompok Pekerja
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

### Konteks Pembatalan
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

### Pilih untuk Multiplexing
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

## Konfigurasi Proyek & Sistem Pembangunan
### Struktur Proyek
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

### pergi.mod
```
module github.com/example/my_project

go 1.22

require (
    github.com/gin-gonic/gin v1.10.0
    github.com/go-sql-driver/mysql v1.8.0
    go.uber.org/zap v1.27.0
)
```

### Perintah Penting
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

### Saluran CI/CD (Tindakan GitHub)
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

## Pengujian
### Pengujian Satuan
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

### Pengujian HTTP Berdasarkan Tabel
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

## Interoperabilitas
### CGo (Memanggil C dari Go)
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

### FFI dengan Bahasa Lain
| Arah | Mekanisme |
|-----------|-----------|
| Pergi menelepon C | cgo (`import "C"`) |
| Hubungi C++ | fungsi pembungkus cgo + C |
| C memanggil Pergi | Ekspor fungsi Go dengan`//export`|
| Panggil Python | Gunakan gopy atau subproses |
---

## Pola Desain
### Pola Middleware (HTTP)
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

### Pola Opsi
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

## Kinerja & Optimasi
### Pembuatan profil
```bash
go test -cpuprofile=cpu.prof -bench=. ./...
go tool pprof cpu.prof
go test -memprofile=mem.prof -bench=. ./...
go tool pprof mem.prof
```

### Kiat Pengoptimalan
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

## Penerapan
### Kompilasi Silang
```bash
GOOS=linux GOARCH=amd64 go build -o myapp-linux
GOOS=windows GOARCH=amd64 go build -o myapp.exe
GOOS=darwin GOARCH=arm64 go build -o myapp-mac
```

### Penerapan Docker
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

## Perpustakaan Standar
| Paket | Tujuan |
|---------|---------|
| fmt | I/O yang diformat |
| bersih/http | Klien dan server HTTP |
| pengkodean/json | Pengkodean/penguraian JSON |
| os | Operasi tingkat OS |
| io | I/O primitif |
| string / strkonv | Manipulasi string |
| sinkronisasi | Mutex, Grup Tunggu, Sekali |
| konteks | Batas waktu, pembatalan |
| pengujian | Kerangka pengujian bawaan |
| log / log/kerja keras | Pencatatan |
| waktu | Waktu dan durasi |
| kripto | Kriptografi (TLS, hashing) |
| basis data/sql | Abstraksi basis data |
---

## Perkakas
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

## Kapan Menggunakan Go
| Skenario | Mengapa Pergi | Alternatif Lebih Baik |
|----------|--------|-------------------|
| Layanan cloud-native/layanan mikro | Biner cepat, kecil, HTTP | Karat untuk performa maksimal |
| Alat CLI | Kompilasi cepat, biner tunggal | Karat untuk CLI yang kompleks |
| Server web / API | HTTP bawaan, cepat, sederhana | Node.js/Express untuk pembuatan prototipe cepat |
| Perkakas DevOps | Docker, Kubernetes, Terraform adalah Go | Python untuk skrip |
| Sistem bersamaan | Goroutine ringan dan elegan | Erlang/Elixir untuk konkurensi yang toleran terhadap kesalahan |
| Pemrograman jaringan | Paket bersih luar biasa | C/C++ untuk kontrol tingkat terendah |
| Ilmu data / ML | Bukan ekosistem yang tepat | Piton, R |
| GUI desktop/seluler | Tidak ada kerangka GUI | Gunakan antarmuka web atau bahasa asli |
| Sistem tertanam | Terlalu berat (GC, runtime) | C, Karat |
---

## Ringkasan
Go adalah bahasa yang sengaja memilih kesederhanaan dibandingkan fitur. Ia memiliki konstruksi yang lebih sedikit dibandingkan kebanyakan bahasa -- tidak ada pewarisan, tidak ada metode yang berlebihan, tidak ada pengecualian, tidak ada makro -- dan ini merupakan kelebihannya. Hasilnya adalah kode yang mudah dibaca, mudah ditulis, dan mudah dipelihara. Model konkurensi Go (goroutine dan saluran) adalah salah satu model yang dirancang terbaik dalam bahasa apa pun. Untuk infrastruktur cloud, layanan mikro, alat CLI, dan pemrograman jaringan, Go adalah pilihan yang tepat.