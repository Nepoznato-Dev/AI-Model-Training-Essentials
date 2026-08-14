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
# Iść
Go (często nazywany „Golang” od oryginalnej nazwy domeny) to skompilowany język programowania ze statycznym typem, zaprojektowany w Google przez Roberta Griesemera, Roba Pike'a i Kena Thompsona. Został wydany po raz pierwszy w 2012 roku z wyraźnym celem bycia lepszym językiem do programowania systemowego - takim, który łączy wydajność C z produktywnością dynamicznych języków, takich jak Python. Go jest znane ze swojej prostoty, szybkiej kompilacji, wbudowanej współbieżności (goroutines i kanały) oraz doskonałego narzędzia.
Go obsługuje większość ekosystemu infrastruktury chmury: Docker, Kubernetes, Terraform, Prometheus itp. oraz serwer HTTP standardowej biblioteki Go są napisane w Go. Stał się domyślnym językiem programowania natywnego w chmurze, mikrousług i narzędzi CLI.
---

## Dlaczego warto działać
- **Prostota z założenia**: Go ma tylko 25 słów kluczowych. Język jest celowo mały i łatwy do nauczenia.
- **Szybka kompilacja**: Kompiluje się bezpośrednio do kodu maszynowego w ciągu kilku sekund, nawet w przypadku dużych projektów.
- **Wbudowana współbieżność**: Goroutines i kanały sprawiają, że programowanie współbieżne jest dostępne i wydajne.
- **Doskonała biblioteka standardowa**: serwer HTTP, kodowanie JSON, testowanie, kryptografia – wszystko wbudowane.
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
|-------------|--------|
| fmt | Sformatowane we/wy |
| sieć/http | Klient i serwer HTTP |
| kodowanie/json | Kodowanie/dekodowanie JSON |
| os | Operacje na poziomie systemu operacyjnego |
| io | Elementy podstawowe we/wy |
| stringi / strconv | Manipulacja ciągami |
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
| GUI dla komputerów stacjonarnych/mobilnych | Brak struktury GUI | Użyj interfejsu WWW lub języka natywnego |
| Systemy wbudowane | Zbyt ciężki (GC, czas wykonania) | C, rdza |
---

## Syntetyczne pytania i odpowiedzi
### P1: Dlaczego Go nie ma wyjątków? Jak mam postępować z błędami?
**O:** Go używa jawnych zwrotów błędów zamiast wyjątków. Każda funkcja, która może zakończyć się niepowodzeniem, zwraca`error`jako ostatnią wartość zwracaną. Zmusza to osobę wywołującą do jawnej obsługi błędów — bez cichych błędów i zapomnianych bloków catch. Wzorzec idiomatyczny to`if err != nil`. Użyj`fmt.Errorf`z`%w`do błędów zawijania i`errors.Is`/`errors.As`do sprawdzania typów błędów. W przypadku nieodwracalnych błędów (błędów programistycznych) użyj`panic`.
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

### P2: Czym są goroutiny i czym różnią się od wątków systemu operacyjnego?
**O:** Goroutines to lekkie wątki w przestrzeni użytkownika zarządzane przez środowisko wykonawcze Go. Zaczynają się od ~2 KB stosu (w porównaniu z ~1 MB dla wątków systemu operacyjnego), są multipleksowane na wątki systemu operacyjnego przez program planujący i można je tworzyć miliony na raz. Komunikacja między goroutines wykorzystuje kanały (lub prymitywy`sync`dla stanu współdzielonego). Zawsze używaj`sync.WaitGroup`lub anulowania kontekstu, aby uniknąć wycieków goroutine.
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

### P3: Kiedy powinienem używać kanałów zamiast muteksów w celu zapewnienia współbieżności?
**O:** Używaj kanałów, gdy goroutines muszą przekazywać dane — wymuszają one filozofię „dzielenia się pamięcią poprzez komunikację”. Użyj muteksów (`sync.Mutex`), gdy goroutines muszą chronić stan współdzielony (pamięć podręczna, liczniki, pule połączeń). Dobra zasada: jeśli dane są przesyłane pomiędzy goroutinami, używaj kanałów; jeśli dostęp do danych uzyskuje wiele procedur gor, użyj muteksu. W przypadku prostych operacji atomowych użyj`sync/atomic`.
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

### P4: Jaka jest różnica pomiędzy plasterkami/mapami`nil`a pustymi?
**A:** Plasterek`nil`(`var s []int`) nie ma podstawowej tablicy, długość 0, pojemność 0. Pusty plasterek (`s := []int{}`lub`make([]int, 0)`) ma bazową tablicę, ale długość 0. Obydwa działają identycznie z`append`,`len`,`cap`i`range`. Kierowanie JSON różni się: plasterki zerowe stają się`null`, puste plasterki stają się`[]`. Najlepsza praktyka: preferuj wycinki zerowe dla wartości zwracanych (oznaczają „brak danych”), puste wycinki, gdy liczy się wynik JSON.
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

### P5: Jak działają interfejsy w Go i czym jest pusty interfejs?
**A:** Interfejsy Go są spełnione w sposób dorozumiany — typ implementuje interfejs poprzez implementację jego metod, bez słowa kluczowego `implements`. Umożliwia to oddzielenie i kompozycję. Pusty interfejs`interface{}`(lub`any`w Go 1.18+) jest obsługiwany przez każdy typ — używaj go oszczędnie (generyczne są często lepsze). Wartości interfejsu są parami:`(type, value)`. Interfejs zerowy ma oba jako zero.
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

## Rozwiązywanie problemów na podstawie łańcucha myślowego
### Problem 1: Zbuduj współbieżny skrobak sieciowy z ograniczeniem szybkości
**Opis problemu:** Stwórz program Go, który jednocześnie pobiera adresy URL z listy, wyodrębnia tytuły stron, przestrzega limitu 10 żądań na sekundę i zbiera wyniki bez wyścigów danych.
**Krok 1 — Zrozum problem:**
Potrzebujemy: (1) jednoczesnego pobierania HTTP z goroutines, (2) ograniczania szybkości, aby uniknąć przeciążenia serwerów, (3) gromadzenia wyników bez wyścigów, (4) właściwej obsługi błędów w przypadku nieudanych żądań. Prymitywy współbieżności Go (goroutines, kanały, `errgroup`) są do tego idealne.
**Krok 2 — Zidentyfikuj podejście:**
- Użyj`golang.org/x/time/rate`do ograniczenia szybkości wiadra tokenów.
- Użyj`sync.WaitGroup`lub`errgroup.Group`do zarządzania goroutines.
- Użyj kanału wyników, aby bezpiecznie gromadzić dane wyjściowe.
- Użyj`context.Context`do anulowania i przekroczenia limitu czasu.
**Krok 3 — Wdróż rozwiązanie:**
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

**Krok 4 — Weryfikacja i optymalizacja:**
- Brak wyścigów danych: każda goroutine zapisuje do własnego indeksu w`results`- nie jest potrzebny muteks.
-`errgroup.SetLimit`ogranicza współbieżność niezależnie od ogranicznika szybkości.
-`io.LimitReader`zapobiega czytaniu zbyt dużych stron.
-`http.NewRequestWithContext`zapewnia anulowanie żądań po zakończeniu kontekstu.
— W przypadku produkcji: dodaj logikę ponawiania prób z wykładniczym wycofywaniem, dostrajaniem puli połączeń i metrykami.
### Problem 2: Zaimplementuj ogólną pamięć podręczną LRU
**Opis problemu:** Zaimplementuj bezpieczną wątkowo, ogólną pamięć podręczną LRU (najmniej ostatnio używaną) w Go, używając generycznych (Go 1.18+). Powinien obsługiwać`Get`,`Set`i`Delete`ze złożonością czasową O(1).
**Krok 1 — Zrozum problem:**
Pamięć podręczna LRU wymaga wyszukiwania O(1) (mapa skrótów) i aktualizacji porządkowania O(1) (lista podwójnie połączona). Na `Get`: przesuń element na przód. W `Set`: wkładka z przodu; eksmituj z powrotem, jeśli przekroczysz pojemność. Bezpieczeństwo wątków wymaga muteksu.
**Krok 2 — Zidentyfikuj podejście:**
- Użyj`container/list`(lista podwójnie połączona) dla O(1) przesunięcia do przodu i usunięcia z tyłu.
- Użyj`map[K]*list.Element`do wyszukiwania O(1).
- Użyj`sync.Mutex`dla bezpieczeństwa gwintu.
- Generics (`[K comparable, V any]`) dla bezpieczeństwa typu.
**Krok 3 — Wdróż rozwiązanie:**
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

**Krok 4 — Weryfikacja i optymalizacja:**
- O(1) dla`Get`,`Set`,`Delete`: przeglądanie mapy jest średnie O(1); operacje na listach (`MoveToFront`,`PushFront`,`Remove`,`Back`) to O(1).
- Bezpieczeństwo wątków:`sync.Mutex`zapewnia, że ​​tylko jedna goroutine uzyskuje dostęp do pamięci podręcznej na raz. W przypadku obciążeń wymagających dużego odczytu użyj`sync.RWMutex`.
- Generics:`[K comparable, V any]`zapewnia obsługę kluczy`==`(wymagane dla kluczy mapy), podczas gdy wartości mogą być dowolnego typu.
- Produkcja: rozważ`github.com/hashicorp/golang-lru/v2`— przetestowany w boju z obsługą TTL i shardingiem w celu ograniczenia rywalizacji o blokady.
### Problem 3: Zbuduj serwer czatu TCP
**Opis problemu:** Zbuduj współbieżny serwer czatów TCP, z którym klienci mogą się łączyć, transmitować wiadomości do wszystkich innych podłączonych klientów i bezpiecznie się rozłączać. Obsługuj powolnych klientów bez blokowania innych.
**Krok 1 — Zrozum problem:**
Potrzebujemy: (1) akceptowania połączeń TCP, (2) jednej procedury goroutine na klienta do odczytu, (3) mechanizmu rozgłoszeniowego do wysyłania wiadomości do wszystkich klientów, (4) obsługi rozłączeń i wolnych klientów. Jest to klasyczny wzór wachlarzowy.
**Krok 2 — Zidentyfikuj podejście:**
- Użyj`net.Listener`dla połączeń TCP.
- Użyj centralnej goroutine`hub`z kanałami do rejestracji/wyrejestrowania/nadawania klienta.
- Każdy klient otrzymuje dedykowaną procedurę zapisu z buforowanym kanałem - powolni klienci nie blokują innych.
- Użyj `context.Context`, aby bezpiecznie zamknąć system.
**Krok 3 — Wdróż rozwiązanie:**
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

**Krok 4 — Weryfikacja i optymalizacja:**
- Powolna obsługa klienta:`select`z`default`w transmisji zapobiega blokowaniu. Powolni klienci są rozłączani, jeśli ich bufor się zapełni.
- Brak wyścigów: goroutine piasty jest jedynym autorem mapy `clients`; `mu`chroni odczyty podczas transmisji.
- Płynne zamykanie: dodaj`context.Context`i moduł obsługi sygnału, aby zamknąć odbiornik i opróżnić połączenia.
- Produkcja: rozważ użycie`golang.org/x/net/websocket`dla klientów przeglądarkowych i dodaj uwierzytelnianie, historię wiadomości i pokoje.
---

## Streszczenie
Go to język, który świadomie przedkłada prostotę nad funkcjonalność. Ma mniej konstrukcji niż większość języków — nie ma dziedziczenia, nie przeciąża metod, nie ma wyjątków, nie ma makr — i to jest jego siła. Rezultatem jest kod, który jest łatwy do odczytania, łatwy do napisania i łatwy w utrzymaniu. Model współbieżności Go (goroutines i kanały) jest jednym z najlepiej zaprojektowanych w dowolnym języku. W przypadku infrastruktury chmurowej, mikrousług, narzędzi CLI i programowania sieciowego Go jest doskonałym wyborem.