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

# Andare
Go (spesso chiamato "Golang" dal nome del dominio originale) è un linguaggio di programmazione compilato e tipizzato staticamente progettato presso Google da Robert Griesemer, Rob Pike e Ken Thompson. È stato rilasciato per la prima volta nel 2012 con l'obiettivo esplicito di diventare un linguaggio migliore per la programmazione di sistemi, in grado di combinare le prestazioni del C con la produttività di linguaggi dinamici come Python. Go è noto per la sua semplicità, compilazione rapida, concorrenza integrata (goroutine e canali) e strumenti eccellenti.
Go alimenta gran parte dell'ecosistema dell'infrastruttura cloud: Docker, Kubernetes, Terraform, Prometheus, ecc. e il server HTTP della libreria standard Go sono tutti scritti in Go. È diventato il linguaggio predefinito per lo sviluppo nativo del cloud, i microservizi e gli strumenti CLI.
---

## Perché andare è importante
- **Semplicità grazie al design**: Go ha solo 25 parole chiave. La lingua è volutamente piccola e facile da imparare.
- **Compilazione veloce**: compila direttamente nel codice macchina in pochi secondi, anche per progetti di grandi dimensioni.
- **Concorrenza integrata**: goroutine e canali rendono la programmazione simultanea accessibile ed efficiente.
- **Eccellente libreria standard**: server HTTP, codifica JSON, test, crittografia: tutto integrato.
- **Binari statici**: compila in un singolo binario senza dipendenze esterne. La distribuzione è banale.
- **Pedigree su scala Google**: progettato da ingegneri che hanno creato Unix, UTF-8 e gran parte dell'infrastruttura di Google.
## I compromessi
| Limitazione | Dettagli | Soluzione tipica |
|-----------|---------|-------------|
| **Nessun tipo di somma/corrispondenza di pattern** | Nessuna enumerazione con dati associati, nessun tipo algebrico | Utilizzare le interfacce e digitare le opzioni |
| **Errore nella gestione della verbosità** | Esplicito se err != nil controlla ovunque | Accetta il modello; rende visibile la gestione degli errori |
| **Ecosistema più piccolo** | Meno librerie rispetto a Python, Java o JavaScript | La libreria standard copre la maggior parte delle esigenze; pacchetti comunitari in crescita |
| **Nessun framework GUI** | Non adatto per interfacce utente desktop o mobili | Utilizzare interfacce utente basate sul Web (WASM) o un'altra lingua |
| **Spazzino** | Ha un GC: le pause sono piccole ma diverse da zero | Ottimizza GC per carichi di lavoro sensibili alla latenza; utilizzare sync.Pool |
---

## Fondamenti di sintassi
### Struttura di base
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

### Funzioni
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

### Strutture e interfacce
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

### Gestione degli errori
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

### Concorrenza -- Goroutine e canali
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

## Sintassi e modelli avanzati
### Generici (Go 1.18+)
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

### Corrispondenza di pattern avanzata (switch di tipo)
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

### Wrapping personalizzato degli errori
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

## Concorrenza e parallelismo (Approfondimento)
### Modello del pool di lavoratori
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

### Contesto di cancellazione
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

### Selezionare per il multiplexing
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

## Configurazione del progetto e sistema di creazione
### Struttura del progetto
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

### vai.mod
```
module github.com/example/my_project

go 1.22

require (
    github.com/gin-gonic/gin v1.10.0
    github.com/go-sql-driver/mysql v1.8.0
    go.uber.org/zap v1.27.0
)
```

### Comandi essenziali
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

### Pipeline CI/CD (azioni GitHub)
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

## Test
### Test unitari
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

### Test HTTP guidati da tabelle
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

## Interoperabilità
### CGo (Chiamare C da Go)
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

### FFI con altre lingue
| Direzione | Meccanismo |
|-----------|-----------|
| Vai a chiamare C | cgo (`import "C"`) |
| Vai a chiamare C++ | cgo + funzioni wrapper C |
| C chiama Vai | Esporta le funzioni Go con`//export`|
| Vai a chiamare Python | Utilizzare gopy o sottoprocesso |
---

## Modelli di progettazione
### Modello middleware (HTTP)
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

### Modello opzioni
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

## Prestazioni e ottimizzazione
### Profilazione
```bash
go test -cpuprofile=cpu.prof -bench=. ./...
go tool pprof cpu.prof
go test -memprofile=mem.prof -bench=. ./...
go tool pprof mem.prof
```

### Suggerimenti per l'ottimizzazione
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

## Distribuzione
### Compilazione incrociata
```bash
GOOS=linux GOARCH=amd64 go build -o myapp-linux
GOOS=windows GOARCH=amd64 go build -o myapp.exe
GOOS=darwin GOARCH=arm64 go build -o myapp-mac
```

### Distribuzione Docker
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

## La libreria standard
| Pacchetto | Scopo |
|---------|---------|
| fmt | I/O formattato |
| rete/http | Client e server HTTP |
| codifica/json | Codifica/decodifica JSON |
| os | Operazioni a livello di sistema operativo |
| io | Primitive di I/O |
| stringhe / strconv | Manipolazione delle stringhe |
| sincronizza | Mutex, WaitGroup, Una volta |
| contesto | Scadenze, cancellazione |
| prove | Quadro di test integrato |
| registro / registro/slog | Registrazione |
| tempo | Tempo e durata |
| criptovaluta | Crittografia (TLS, hashing) |
| base di dati/sql | Astrazione del database |
---

## Utensili
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

## Quando utilizzare Go
| Scenario | Perché andare | Alternativa migliore |
|----------|--------|-------------|
| Servizi/microservizi nativi del cloud | File binari veloci e piccoli, HTTP eccellente | Ruggine per le massime prestazioni |
| Strumenti CLI | Compilazione veloce, binario singolo | Rust per CLI complesse |
| Server Web/API | HTTP integrato, veloce, semplice | Node.js/Express per la prototipazione rapida |
| Strumenti DevOps | Docker, Kubernetes, Terraform sono Go | Python per lo scripting |
| Sistemi concorrenti | Le goroutine sono leggere ed eleganti | Erlang/Elixir per concorrenza tollerante agli errori |
| Programmazione di rete | Ottimo pacchetto netto | C/C++ per il controllo di livello più basso |
| Scienza dei dati/ML | Non è l'ecosistema giusto | Pitone, R |
| GUI desktop/mobile | Nessun framework GUI | Utilizza un frontend web o un linguaggio nativo |
| Sistemi integrati | Troppo pesante (GC, runtime) | C, Ruggine |
---

## Domande e risposte sintetiche
### D1: Perché Go non prevede eccezioni? Come devo gestire gli errori?
**R:** Go utilizza ritorni di errore espliciti invece di eccezioni. Ogni funzione che può fallire restituisce`error`come ultimo valore restituito. Ciò costringe il chiamante a gestire gli errori in modo esplicito, senza errori silenziosi o blocchi catch dimenticati. Il modello idiomatico è`if err != nil`. Utilizzare`fmt.Errorf`con`%w`per gli errori di disposizione e`errors.Is`/`errors.As`per controllare i tipi di errore. Per errori irreversibili (bug di programmazione), utilizzare`panic`.
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

### D2: Cosa sono le goroutine e in cosa differiscono dai thread del sistema operativo?
**R:** Le goroutine sono thread leggeri nello spazio utente gestiti dal runtime Go. Iniziano con ~ 2 KB di stack (rispetto a ~ 1 MB per i thread del sistema operativo), vengono multiplexati sui thread del sistema operativo dallo scheduler e possono essere creati milioni alla volta. La comunicazione tra goroutine utilizza canali (o primitive`sync`per lo stato condiviso). Utilizzare sempre`sync.WaitGroup`o la cancellazione del contesto per evitare perdite di goroutine.
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

### D3: Quando dovrei utilizzare i canali anziché i mutex per la concorrenza?
**R:** Utilizza i canali quando le goroutine devono comunicare dati: applicano la filosofia "condividi la memoria comunicando". Utilizza i mutex (`sync.Mutex`) quando le goroutine devono proteggere lo stato condiviso (cache, contatori, pool di connessioni). Una buona regola: se i dati vengono passati tra goroutine, utilizzare i canali; se più goroutine accedono ai dati, utilizzare un mutex. Per operazioni atomiche semplici, utilizzare`sync/atomic`.
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

### D4: Qual è la differenza tra le porzioni/mappe`nil`e quelle vuote?
**R:** Una sezione`nil`(`var s []int`) non ha un array sottostante, lunghezza 0, capacità 0. Una sezione vuota (`s := []int{}`o`make([]int, 0)`) ha un array sottostante ma lunghezza 0. Entrambi funzionano in modo identico con`append`,`len`,`cap`e`range`. Il marshalling JSON è diverso: le fette nulle diventano`null`, le fette vuote diventano`[]`. Procedura consigliata: preferire sezioni nulle per i valori restituiti (indicano "nessun dato"), sezioni vuote quando l'output JSON è importante.
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

### D5: Come funzionano le interfacce in Go e qual è l'interfaccia vuota?
**R:** Le interfacce Go sono soddisfatte implicitamente: un tipo implementa un'interfaccia implementando i suoi metodi, senza la parola chiave `implements`. Ciò consente il disaccoppiamento e la composizione. L'interfaccia vuota`interface{}`(o`any`in Go 1.18+) è soddisfatta da ogni tipo: usala con parsimonia (i generici sono spesso migliori). I valori dell'interfaccia sono coppie:`(type, value)`. Un'interfaccia nulla ha entrambi come nulli.
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

## Risoluzione dei problemi basati sulla catena di pensiero
### Problema 1: creare un web scraper simultaneo con limitazione della velocità
**Dichiarazione del problema:** Crea un programma Go che recuperi gli URL da un elenco contemporaneamente, estragga i titoli delle pagine, rispetti un limite di velocità di 10 richieste al secondo e raccolga risultati senza gare di dati.
**Passaggio 1: comprendere il problema:**
Abbiamo bisogno di: (1) recupero HTTP simultaneo con goroutine, (2) limitazione della velocità per evitare server sovraccarichi, (3) raccolta dei risultati senza gare, (4) corretta gestione degli errori per richieste non riuscite. Le primitive di concorrenza di Go (goroutine, canali,`errgroup`) sono ideali per questo.
**Passaggio 2: identificare l'approccio:**
- Utilizzare`golang.org/x/time/rate`per limitare la velocità del bucket di token.
- Utilizza`sync.WaitGroup`o`errgroup.Group`per gestire le goroutine.
- Utilizzare un canale di risultati per raccogliere i risultati in modo sicuro.
- Utilizzare`context.Context`per cancellazioni e timeout.
**Passaggio 3: implementa la soluzione:**
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

**Passaggio 4: verifica e ottimizzazione:**
- Nessuna competizione tra i dati: ogni goroutine scrive sul proprio indice in`results`— non è necessario il mutex.
-`errgroup.SetLimit`limita la concorrenza indipendentemente dal limitatore di velocità.
-`io.LimitReader`impedisce la lettura di pagine eccessivamente grandi.
-`http.NewRequestWithContext`garantisce che le richieste vengano annullate al termine del contesto.
- Per la produzione: aggiunta della logica dei tentativi con backoff esponenziale, ottimizzazione del pool di connessioni e metriche.
### Problema 2: implementare una cache LRU generica
**Dichiarazione del problema:** Implementa una cache LRU (Least Recently Used) generica e thread-safe in Go utilizzando i generici (Go 1.18+). Dovrebbe supportare`Get`,`Set`e`Delete`con complessità temporale O(1).
**Passaggio 1: comprendere il problema:**
Una cache LRU necessita di ricerca O(1) (mappa hash) e aggiornamenti di ordinamento O(1) (elenco doppiamente collegato). Su `Get`: sposta l'elemento in primo piano. Su `Set`: inserto anteriore; sfrattare dal retro se la capacità è eccessiva. La sicurezza del thread richiede un mutex.
**Passaggio 2: identificare l'approccio:**
- Utilizzare`container/list`(elenco doppiamente collegato) per O(1) spostare in avanti e rimuovere dal retro.
- Utilizzare`map[K]*list.Element`per la ricerca O(1).
- Utilizzare`sync.Mutex`per la sicurezza del filo.
- Generici (`[K comparable, V any]`) per la sicurezza del tipo.
**Passaggio 3: implementa la soluzione:**
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

**Passaggio 4: verifica e ottimizzazione:**
- O(1) per`Get`,`Set`,`Delete`: la ricerca della mappa è media O(1); le operazioni sugli elenchi (`MoveToFront`,`PushFront`,`Remove`,`Back`) sono tutte O(1).
- Sicurezza del thread:`sync.Mutex`garantisce che solo una goroutine alla volta acceda alla cache. Per carichi di lavoro con operazioni di lettura pesanti, utilizzare`sync.RWMutex`.
- Generici:`[K comparable, V any]`garantisce che le chiavi supportino`==`(richiesto per le chiavi della mappa) mentre i valori possono essere di qualsiasi tipo.
- Produzione: considera `github.com/hashicorp/golang-lru/v2`: testato in battaglia con supporto TTL e sharding per ridurre i conflitti di blocco.
### Problema 3: creare un server di chat TCP
**Dichiarazione del problema:** Crea un server di chat TCP simultaneo in cui i client possano connettersi, trasmettere messaggi a tutti gli altri client connessi e disconnettersi con garbo. Gestisci i client lenti senza bloccarne altri.
**Passaggio 1: comprendere il problema:**
Abbiamo bisogno di: (1) accettare connessioni TCP, (2) una goroutine per client per la lettura, (3) un meccanismo di trasmissione per inviare messaggi a tutti i client, (4) gestire le disconnessioni e i client lenti. Questo è un classico modello a ventaglio.
**Passaggio 2: identificare l'approccio:**
- Utilizzare`net.Listener`per le connessioni TCP.
- Utilizzare una goroutine centrale`hub`con canali per la registrazione/cancellazione/trasmissione del cliente.
- Ogni client riceve una goroutine di scrittura dedicata con un canale bufferizzato: i client lenti non bloccano gli altri.
- Utilizza`context.Context`per uno spegnimento ordinato.
**Passaggio 3: implementa la soluzione:**
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

**Passaggio 4: verifica e ottimizzazione:**
- Gestione client lenta:`select`con`default`in trasmissione impedisce il blocco. I client lenti vengono disconnessi se il buffer si riempie.
- Nessuna gara: la goroutine dell'hub è l'unico scrittore della mappa `clients`; `mu`protegge le letture durante la trasmissione.
- Spegnimento ordinato: aggiungi`context.Context`e un gestore di segnale per chiudere l'ascoltatore e drenare le connessioni.
- Produzione: considera l'utilizzo di`golang.org/x/net/websocket`per i client browser e aggiungi l'autenticazione, la cronologia dei messaggi e le stanze virtuali.
---

## Riepilogo
Go è un linguaggio che sceglie deliberatamente la semplicità rispetto alle funzionalità. Ha meno costrutti della maggior parte dei linguaggi: nessuna ereditarietà, nessun sovraccarico dei metodi, nessuna eccezione, nessuna macro, e questo è un punto di forza. Il risultato è un codice facile da leggere, facile da scrivere e facile da mantenere. Il modello di concorrenza di Go (goroutine e canali) è uno dei meglio progettati in qualsiasi linguaggio. Per l'infrastruttura cloud, i microservizi, gli strumenti CLI e la programmazione di rete, Go è una scelta eccellente.