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
# Aller
Go (souvent appelé « Golang » d'après son nom de domaine d'origine) est un langage de programmation compilé à typage statique conçu chez Google par Robert Griesemer, Rob Pike et Ken Thompson. Il a été publié pour la première fois en 2012 dans le but explicite de devenir un meilleur langage pour la programmation système, combinant les performances du C avec la productivité des langages dynamiques comme Python. Go est connu pour sa simplicité, sa compilation rapide, sa concurrence intégrée (goroutines et canaux) et ses excellents outils.
Go alimente une grande partie de l'écosystème de l'infrastructure cloud : Docker, Kubernetes, Terraform, Prometheus, etcd, ainsi que le serveur HTTP de la bibliothèque standard Go sont tous écrits en Go. Il est devenu le langage par défaut pour le développement cloud natif, les microservices et les outils CLI.
---

## Pourquoi y aller est important
- **Simplicité dès la conception** : Go n'a que 25 mots-clés. La langue est volontairement petite et facile à apprendre.
- **Compilation rapide** : Compile directement en code machine en quelques secondes, même pour les grands projets.
- **Concurrence intégrée** : les Goroutines et les canaux rendent la programmation simultanée accessible et efficace.
- **Excellente bibliothèque standard** : serveur HTTP, encodage JSON, tests, cryptographie - le tout intégré.
- **Binaires statiques** : compile en un seul binaire sans dépendances externes. Le déploiement est trivial.
- **Pedigree à l'échelle de Google** : conçu par des ingénieurs qui ont construit Unix, UTF-8 et une grande partie de l'infrastructure de Google.
## Les compromis
| Limitation | Détails | Solution de contournement typique |
|-----------|---------|-------------------|
| **Aucun type de somme/correspondance de modèle** | Pas d'énumérations avec données associées, pas de types algébriques | Utiliser des interfaces et des commutateurs de type |
| **Erreur de gestion de la verbosité** | Explicite si err != nil vérifie partout | Acceptez le modèle ; cela rend visible la gestion des erreurs |
| **Écosystème plus petit** | Moins de bibliothèques que Python, Java ou JavaScript | La bibliothèque standard couvre la plupart des besoins ; les packages communautaires se développent |
| **Pas de framework GUI** | Ne convient pas aux interfaces utilisateur de bureau ou mobiles | Utiliser des interfaces utilisateur Web (WASM) ou une autre langue |
| **Éboueur** | Possède un GC -- les pauses sont petites mais non nulles | Optimisez GC pour les charges de travail sensibles à la latence ; utiliser sync.Pool |
---

## Fondamentaux de la syntaxe
### Structure de base
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

### Fonctions
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

### Structures et interfaces
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

### Gestion des erreurs
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

### Concurrence - Goroutines et canaux
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

## Syntaxe et modèles avancés
### Génériques (Go 1.18+)
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

### Correspondance de modèle avancée (commutateurs de type)
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

### Emballage d'erreur personnalisé
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

## Concurrence et parallélisme (immersion approfondie)
### Modèle de pool de travailleurs
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

### Contexte de l'annulation
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

### Sélectionner pour le multiplexage
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

## Configuration du projet et système de construction
### Structure du projet
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

### Commandes essentielles
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

### Pipeline CI/CD (actions GitHub)
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

## Tests
### Tests unitaires
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

### Tests HTTP basés sur des tables
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

## Interopérabilité
### CGo (Appeler C depuis Go)
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

### FFI avec d'autres langues
| Itinéraire | Mécanisme |
|-----------|---------------|
| Allez appeler C | cgo (`import "C"`) |
| Allez appeler C++ | fonctions wrapper cgo + C |
| C appelant Go | Exporter les fonctions Go avec`//export`|
| Allez appeler Python | Utilisez gopy ou subprocess |
---

## Modèles de conception
### Modèle de middleware (HTTP)
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

### Modèle d'options
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

## Performances et optimisation
### Profilage
```bash
go test -cpuprofile=cpu.prof -bench=. ./...
go tool pprof cpu.prof
go test -memprofile=mem.prof -bench=. ./...
go tool pprof mem.prof
```

### Conseils d'optimisation
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

## Déploiement
### Compilation croisée
```bash
GOOS=linux GOARCH=amd64 go build -o myapp-linux
GOOS=windows GOARCH=amd64 go build -o myapp.exe
GOOS=darwin GOARCH=arm64 go build -o myapp-mac
```

### Déploiement de Docker
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

## La bibliothèque standard
| Forfait | Objectif |
|---------|---------|
| fmt | E/S formatées |
| net/http | Client et serveur HTTP |
| encodage/json | Encodage/décodage JSON |
| système d'exploitation | Opérations au niveau du système d'exploitation |
| io | Primitives d'E/S |
| chaînes / strconv | Manipulation de chaînes |
| synchroniser | Mutex, WaitGroup, Une fois |
| contexte | Délais, annulation |
| tests | Cadre de test intégré |
| journal / journal/slog | Journalisation |
| temps | Heure et durée |
| crypto-monnaie | Cryptographie (TLS, hachage) |
| base de données/sql | Abstraction de la base de données |
---

## Outillage
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

## Quand utiliser Go
| Scénario | Pourquoi y aller | Meilleure alternative |
|--------------|--------|---------|
| Services/microservices cloud natifs | Rapides, petits binaires, excellent HTTP | Rouille pour des performances maximales |
| Outils CLI | Compilation rapide, binaire unique | Rust pour les CLI complexes |
| Serveurs Web / API | HTTP intégré, rapide, simple | Node.js/Express pour le prototypage rapide |
| Outils DevOps | Docker, Kubernetes et Terraform sont Go | Python pour les scripts |
| Systèmes simultanés | Les Goroutines sont légères et élégantes | Erlang/Elixir pour une concurrence tolérante aux pannes |
| Programmation réseau | Excellent paquet net | C/C++ pour le contrôle de niveau le plus bas |
| Science des données / ML | Pas le bon écosystème | Python, R |
| Interface graphique de bureau/mobile | Pas de framework GUI | Utiliser une interface Web ou une langue maternelle |
| Systèmes embarqués | Trop lourd (GC, runtime) | C, Rouille |
---

## Questions et réponses synthétiques
### Q1 : Pourquoi Go n'a-t-il pas d'exceptions ? Comment dois-je gérer les erreurs ?
**R :** Go utilise des retours d'erreur explicites au lieu d'exceptions. Chaque fonction qui peut échouer renvoie un`error`comme dernière valeur de retour. Cela oblige l’appelant à gérer les erreurs explicitement – ​​pas d’échecs silencieux ni de blocs catch oubliés. Le modèle idiomatique est`if err != nil`. Utilisez`fmt.Errorf`avec`%w`pour envelopper les erreurs et`errors.Is`/`errors.As`pour vérifier les types d'erreurs. Pour les erreurs irrécupérables (bugs de programmation), utilisez`panic`.
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

### Q2 : Que sont les goroutines et en quoi sont-elles différentes des threads du système d'exploitation ?
**R :** Les Goroutines sont des threads légers dans l'espace utilisateur, gérés par le runtime Go. Ils commencent avec ~ 2 Ko de pile (contre ~ 1 Mo pour les threads du système d'exploitation), sont multiplexés sur les threads du système d'exploitation par le planificateur et peuvent être créés par millions à la fois. La communication entre les goroutines utilise des canaux (ou des primitives`sync`pour l'état partagé). Utilisez toujours`sync.WaitGroup`ou l'annulation de contexte pour éviter les fuites de goroutines.
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

### Q3 : Quand dois-je utiliser des canaux plutôt que des mutex pour la simultanéité ?
**R :** Utilisez des canaux lorsque les goroutines ont besoin de communiquer des données : ils appliquent la philosophie « partager la mémoire en communiquant ». Utilisez des mutex (`sync.Mutex`) lorsque les goroutines doivent protéger l'état partagé (caches, compteurs, pools de connexions). Une bonne règle : si des données sont transmises entre des goroutines, utilisez des canaux ; si les données sont accessibles par plusieurs goroutines, utilisez un mutex. Pour des opérations atomiques simples, utilisez`sync/atomic`.
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

### Q4 : Quelle est la différence entre les tranches/cartes`nil`et les tranches vides ?
**R :** Une tranche`nil`(`var s []int`) n'a pas de tableau sous-jacent, longueur 0, capacité 0. Une tranche vide (`s := []int{}`ou`make([]int, 0)`) a un tableau sous-jacent mais longueur 0. Les deux fonctionnent de manière identique avec`append`,`len`,`cap`et`range`. Le marshaling JSON diffère : les tranches nulles deviennent`null`, les tranches vides deviennent`[]`. Bonne pratique : préférez les tranches nulles pour les valeurs de retour (elles indiquent "aucune donnée"), les tranches vides lorsque la sortie JSON est importante.
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

### Q5 : Comment fonctionnent les interfaces dans Go et qu'est-ce que l'interface vide ?
**R :** Les interfaces Go sont satisfaites implicitement : un type implémente une interface en implémentant ses méthodes, sans mot-clé `implements`. Cela permet le découplage et la composition. L'interface vide`interface{}`(ou`any`dans Go 1.18+) est satisfaite par tous les types — utilisez-la avec parcimonie (les génériques sont souvent meilleurs). Les valeurs d'interface sont des paires :`(type, value)`. Une interface nulle a les deux comme nuls.
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

## Résolution de problèmes en chaîne de pensée
### Problème 1 : Créer un grattoir Web simultané avec limitation de débit
**Énoncé du problème :** Créez un programme Go qui récupère simultanément les URL d'une liste, extrait les titres des pages, respecte une limite de débit de 10 requêtes par seconde et collecte les résultats sans courses de données.
**Étape 1 — Comprendre le problème :**
Nous avons besoin de : (1) une récupération HTTP simultanée avec des goroutines, (2) une limitation du débit pour éviter de surcharger les serveurs, (3) une collecte des résultats sans courses, (4) une gestion appropriée des erreurs pour les requêtes ayant échoué. Les primitives de concurrence de Go (goroutines, canaux,`errgroup`) sont idéales pour cela.
**Étape 2 — Identifiez l'approche :**
- Utilisez`golang.org/x/time/rate`pour limiter le débit des compartiments de jetons.
- Utilisez`sync.WaitGroup`ou`errgroup.Group`pour gérer les goroutines.
- Utiliser un canal de résultats pour collecter les résultats en toute sécurité.
- Utilisez`context.Context`pour l'annulation et les délais d'attente.
**Étape 3 — Mettre en œuvre la solution :**
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

**Étape 4 – Vérifier et optimiser :**
- Pas de courses de données : chaque goroutine écrit dans son propre index dans`results`— aucun mutex n'est nécessaire.
-`errgroup.SetLimit`limite la concurrence indépendamment du limiteur de débit.
-`io.LimitReader`empêche la lecture de pages trop volumineuses.
-`http.NewRequestWithContext`garantit que les demandes sont annulées lorsque le contexte est terminé.
- Pour la production : ajoutez une logique de nouvelle tentative avec une interruption exponentielle, un réglage du pool de connexions et des métriques.
### Problème 2 : implémenter un cache LRU générique
**Énoncé du problème :** Implémentez un cache LRU générique (le moins récemment utilisé) thread-safe dans Go à l'aide de génériques (Go 1.18+). Il doit prendre en charge`Get`,`Set`et`Delete`avec une complexité temporelle O(1).
**Étape 1 — Comprendre le problème :**
Un cache LRU nécessite une recherche O(1) (carte de hachage) et des mises à jour de commande O(1) (liste doublement chaînée). Sur`Get`: déplacer l'élément vers l'avant. Sur`Set`: insert à l'avant ; expulser de l'arrière en cas de surcapacité. La sécurité des threads nécessite un mutex.
**Étape 2 — Identifiez l'approche :**
- Utilisez`container/list`(liste doublement chaînée) pour le déplacement O(1) vers l'avant et la suppression de l'arrière.
- Utilisez`map[K]*list.Element`pour la recherche O(1).
- Utilisez`sync.Mutex`pour la sécurité du filetage.
- Génériques (`[K comparable, V any]`) pour la sécurité de type.
**Étape 3 — Mettre en œuvre la solution :**
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

**Étape 4 – Vérifier et optimiser :**
- O(1) pour`Get`,`Set`,`Delete`: la recherche de carte est en moyenne O(1) ; les opérations de liste (`MoveToFront`,`PushFront`,`Remove`,`Back`) sont toutes O(1).
- Sécurité des threads :`sync.Mutex`garantit qu'une seule goroutine accède au cache à la fois. Pour les charges de travail lourdes en lecture, utilisez`sync.RWMutex`.
- Génériques :`[K comparable, V any]`garantit que les clés prennent en charge`==`(obligatoire pour les clés de carte) tandis que les valeurs peuvent être de n'importe quel type.
- Production : pensez à `github.com/hashicorp/golang-lru/v2` – testé au combat avec prise en charge TTL et partitionnement pour réduire les conflits de verrouillage.
### Problème 3 : Créer un serveur de discussion TCP
**Énoncé du problème :** Créez un serveur de discussion TCP simultané sur lequel les clients peuvent se connecter, diffuser des messages à tous les autres clients connectés et se déconnecter en douceur. Gérez les clients lents sans en bloquer les autres.
**Étape 1 — Comprendre le problème :**
Nous avons besoin de : (1) accepter les connexions TCP, (2) une goroutine par client pour la lecture, (3) un mécanisme de diffusion pour envoyer des messages à tous les clients, (4) gérer les déconnexions et les clients lents. Il s’agit d’un modèle de répartition classique.
**Étape 2 — Identifiez l'approche :**
- Utilisez`net.Listener`pour les connexions TCP.
- Utilisez une goroutine centrale`hub`avec des canaux pour l'enregistrement/désenregistrement/diffusion des clients.
- Chaque client dispose d'une goroutine d'écriture dédiée avec un canal tamponné — les clients lents ne bloquent pas les autres.
- Utilisez`context.Context`pour un arrêt en douceur.
**Étape 3 — Mettre en œuvre la solution :**
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

**Étape 4 – Vérifier et optimiser :**
- Gestion client lente : le`select`avec`default`en diffusion évite le blocage. Les clients lents sont déconnectés si leur tampon se remplit.
- Pas de courses : le hub goroutine est le seul rédacteur de la carte `clients` ; `mu`protège les lectures pendant la diffusion.
- Arrêt progressif : ajoutez`context.Context`et un gestionnaire de signal pour fermer les connexions d'écoute et de drainage.
- Production : envisagez d'utiliser`golang.org/x/net/websocket`pour les clients de navigateur et ajoutez l'authentification, l'historique des messages et les salles.
---

## Résumé
Go est un langage qui choisit délibérément la simplicité plutôt que les fonctionnalités. Il a moins de constructions que la plupart des langages – pas d’héritage, pas de surcharge de méthode, pas d’exceptions, pas de macros – et c’est une force. Le résultat est un code facile à lire, facile à écrire et facile à maintenir. Le modèle de concurrence de Go (goroutines et canaux) est l'un des mieux conçus dans tous les langages. Pour l'infrastructure cloud, les microservices, les outils CLI et la programmation réseau, Go est un excellent choix.