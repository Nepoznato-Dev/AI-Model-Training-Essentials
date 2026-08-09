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
# Iść
Go (często nazywany „Golang” od oryginalnej nazwy domeny) to skompilowany język programowania ze statycznym typem, zaprojektowany w Google przez Roberta Griesemera, Roba Pike'a i Kena Thompsona. Został wydany po raz pierwszy w 2012 roku z wyraźnym celem bycia lepszym językiem do programowania systemowego - takim, który łączy wydajność C z produktywnością dynamicznych języków, takich jak Python. Go jest znane ze swojej prostoty, szybkiej kompilacji, wbudowanej współbieżności (goroutines i kanały) oraz doskonałego oprzyrządowania.
Go obsługuje większość ekosystemu infrastruktury chmury: Docker, Kubernetes, Terraform, Prometheus itp. oraz serwer HTTP standardowej biblioteki Go są napisane w Go. Stał się domyślnym językiem programowania natywnego w chmurze, mikrousług i narzędzi CLI.
---

## Dlaczego warto działać
- **Prostota z założenia**: Go ma tylko 25 słów kluczowych. Język jest celowo mały i łatwy do nauczenia.
- **Szybka kompilacja**: Kompiluje się bezpośrednio do kodu maszynowego w ciągu kilku sekund, nawet w przypadku dużych projektów.
- **Wbudowana współbieżność**: Goroutines i kanały sprawiają, że programowanie współbieżne jest dostępne i wydajne.
- **Doskonała biblioteka standardowa**: serwer HTTP, kodowanie JSON, testowanie, kryptografia - wszystko wbudowane.
- **Statyczne pliki binarne**: Kompiluje się do pojedynczego pliku binarnego bez zewnętrznych zależności. Wdrożenie jest banalne.
- **Rodowód na skalę Google**: Zaprojektowany przez inżynierów, którzy zbudowali Unix, UTF-8 i większość infrastruktury Google.
## Kompromisy
| Ograniczenie | Szczegóły | Typowe obejście |
|----------|---------|--------------------------------|
| **Brak typów sum / dopasowań wzorców** | Żadnych wyliczeń z powiązanymi danymi, żadnych typów algebraicznych | Użyj interfejsów i przełączników typu |
| **Błąd obsługi szczegółowości** | Jawne, jeśli err != zero sprawdza wszędzie | Zaakceptuj wzór; sprawia, że ​​obsługa błędów staje się widoczna |
| **Mniejszy ekosystem** | Mniej bibliotek niż Python, Java lub JavaScript | Biblioteka standardowa zaspokaja większość potrzeb; pakiety społecznościowe rosną |
| **Brak struktury GUI** | Nie nadaje się do interfejsów użytkownika na komputerach stacjonarnych i urządzeniach mobilnych | Użyj internetowych interfejsów użytkownika (WASM) lub innego języka |
| **Kosz na śmieci** | Ma GC — przerwy są małe, ale niezerowe | Dostosuj GC do obciążeń wrażliwych na opóźnienia; użyj sync.Pool |
---

## Podstawy składni
### Podstawowa struktura
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

### Funkcje
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

### Struktury i interfejsy
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

### Obsługa błędów
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

### Współbieżność — Goroutines i kanały
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

## Zaawansowana składnia i wzorce
### Generics (Przejdź do wersji 1.18+)
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

### Zaawansowane dopasowywanie wzorców (przełączniki typu)
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

### Niestandardowe zawijanie błędów
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

## Współbieżność i równoległość (głębokie nurkowanie)
### Wzór puli pracowników
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

### Kontekst anulowania
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

### Wybierz dla multipleksowania
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

## Konfiguracja projektu i budowanie systemu
### Struktura projektu
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

### przejdź.mod
```
module github.com/example/my_project

go 1.22

require (
    github.com/gin-gonic/gin v1.10.0
    github.com/go-sql-driver/mysql v1.8.0
    go.uber.org/zap v1.27.0
)
```

### Podstawowe polecenia
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

### Potok CI/CD (akcje w GitHub)
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

## Testowanie
### Testy jednostkowe
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

### Testy HTTP oparte na tabelach
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

## Interoperacyjność
### CGo (wywoływanie C z poziomu Go)
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

### FFI z innymi językami
| Kierunek | Mechanizm |
|----------|-----------|
| Idź i zadzwoń do C | cgo (`import "C"`) |
| Idź zadzwonić do C++ | funkcje opakowania cgo + C |
| C dzwoni do Go | Eksportuj funkcje Go za pomocą`//export`|
| Idź i zadzwoń do Pythona | Użyj gopy lub podprocesu |
---

## Wzorce projektowe
### Wzorzec oprogramowania pośredniego (HTTP)
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

### Opcje Wzorzec
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

## Wydajność i optymalizacja
### Profilowanie
```bash
go test -cpuprofile=cpu.prof -bench=. ./...
go tool pprof cpu.prof
go test -memprofile=mem.prof -bench=. ./...
go tool pprof mem.prof
```

### Wskazówki dotyczące optymalizacji
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

## Zastosowanie
### Kompilacja krzyżowa
```bash
GOOS=linux GOARCH=amd64 go build -o myapp-linux
GOOS=windows GOARCH=amd64 go build -o myapp.exe
GOOS=darwin GOARCH=arm64 go build -o myapp-mac
```

### Wdrożenie Dockera
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

## Biblioteka standardowa
| Pakiet | Cel |
|--------|---------|
| fmt | Sformatowane we/wy |
| sieć/http | Klient i serwer HTTP |
| kodowanie/json | Kodowanie/dekodowanie JSON |
| os | Operacje na poziomie systemu operacyjnego |
| io | Elementy podstawowe we/wy |
| stringi / strconv | Manipulacja ciągiem |
| synchronizacja | Mutex, grupa oczekiwania, raz |
| kontekst | Terminy, anulowanie |
| testowanie | Wbudowane środowisko testowe |
| log / log/zadyszka | Rejestrowanie |
| czas | Czas i czas trwania |
| krypto | Kryptografia (TLS, haszowanie) |
| baza danych/sql | Abstrakcja bazy danych |
---

## Oprzyrządowanie
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

## Kiedy używać opcji Idź
| Scenariusz | Dlaczego warto iść | Lepsza alternatywa |
|---------|--------|--------------------------------|
| Usługi/mikroserwisy natywne w chmurze | Szybkie, małe pliki binarne, doskonały HTTP | Rdza dla maksymalnej wydajności |
| Narzędzia CLI | Szybka kompilacja, pojedynczy plik binarny | Rdza dla złożonych interfejsów CLI |
| Serwery WWW / API | Wbudowany protokół HTTP, szybki, prosty | Node.js/Express do szybkiego prototypowania |
| Narzędzia DevOps | Docker, Kubernetes, Terraform to Go | Python do pisania skryptów |
| Systemy współbieżne | Goroutines są lekkie i eleganckie | Erlang/Elixir dla współbieżności odpornej na błędy |
| Programowanie sieciowe | Doskonały pakiet netto | C/C++ dla kontroli najniższego poziomu |
| Nauka o danych / ML | Niewłaściwy ekosystem | Python, R |
| GUI dla komputerów stacjonarnych/mobilnych | Brak struktury GUI | Użyj interfejsu internetowego lub języka natywnego |
| Systemy wbudowane | Zbyt ciężki (GC, czas wykonania) | C, rdza |
---

## Streszczenie
Go to język, który świadomie przedkłada prostotę nad funkcjonalność. Ma mniej konstrukcji niż większość języków — nie ma dziedziczenia, nie przeciąża metod, nie ma wyjątków, nie ma makr — i to jest jego siła. Rezultatem jest kod, który jest łatwy do odczytania, łatwy do napisania i łatwy w utrzymaniu. Model współbieżności Go (goroutines i kanały) jest jednym z najlepiej zaprojektowanych w dowolnym języku. W przypadku infrastruktury chmurowej, mikrousług, narzędzi CLI i programowania sieciowego Go jest doskonałym wyborem.