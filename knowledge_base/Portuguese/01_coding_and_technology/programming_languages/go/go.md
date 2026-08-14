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
# Ir
Go (muitas vezes chamado de "Golang" devido ao seu nome de domínio original) é uma linguagem de programação compilada e digitada estaticamente, projetada no Google por Robert Griesemer, Rob Pike e Ken Thompson. Foi lançado pela primeira vez em 2012 com o objetivo explícito de ser uma linguagem melhor para programação de sistemas – uma que combine o desempenho de C com a produtividade de linguagens dinâmicas como Python. Go é conhecido por sua simplicidade, compilação rápida, simultaneidade integrada (goroutines e canais) e excelentes ferramentas.
Go potencializa grande parte do ecossistema de infraestrutura em nuvem: Docker, Kubernetes, Terraform, Prometheus, etcd e o servidor HTTP da biblioteca padrão Go são todos escritos em Go. Tornou-se a linguagem padrão para desenvolvimento nativo da nuvem, microsserviços e ferramentas CLI.
---

## Por que ir é importante
- **Simplicidade por design**: Go tem apenas 25 palavras-chave. A linguagem é deliberadamente pequena e fácil de aprender.
- **Compilação rápida**: compila diretamente em código de máquina em segundos, mesmo para projetos grandes.
- **Simultaneidade integrada**: Goroutines e canais tornam a programação simultânea acessível e eficiente.
- **Excelente biblioteca padrão**: servidor HTTP, codificação JSON, testes, criptografia - tudo integrado.
- **Binários estáticos**: Compila em um único binário sem dependências externas. A implantação é trivial.
- **Pedigree em escala do Google**: projetado por engenheiros que criaram Unix, UTF-8 e grande parte da infraestrutura do Google.
## As compensações
| Limitação | Detalhes | Solução alternativa típica |
|-------|---------|-------------------|
| **Sem tipos de soma/correspondência de padrões** | Sem enums com dados associados, sem tipos algébricos | Use interfaces e digite switches |
| **Erro ao lidar com verbosidade** | Explícito if err != nil verifica em todos os lugares | Aceite o padrão; torna visível o tratamento de erros |
| **Ecossistema menor** | Menos bibliotecas que Python, Java ou JavaScript | A biblioteca padrão cobre a maioria das necessidades; pacotes comunitários crescendo |
| **Sem estrutura GUI** | Não adequado para interfaces de usuário de desktop ou dispositivos móveis | Use UIs baseadas na web (WASM) ou outro idioma |
| **Coletor de lixo** | Tem um GC – as pausas são pequenas, mas diferentes de zero | Ajuste o GC para cargas de trabalho sensíveis à latência; usar sincronização.Pool |
---

## Fundamentos de sintaxe
### Estrutura Básica
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

### Funções
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

### Estruturas e Interfaces
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

### Tratamento de erros
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

### Simultaneidade – Goroutines e Canais
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

## Sintaxe e padrões avançados
### Genéricos (versão 1.18+)
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

### Correspondência avançada de padrões (chaves de tipo)
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

### Envolvimento de erro personalizado
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

## Simultaneidade e paralelismo (aprofundamento)
### Padrão de pool de trabalhadores
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

### Contexto para cancelamento
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

### Selecione para multiplexação
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

## Configuração do projeto e sistema de construção
### Estrutura do Projeto
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

###go.mod
```
module github.com/example/my_project

go 1.22

require (
    github.com/gin-gonic/gin v1.10.0
    github.com/go-sql-driver/mysql v1.8.0
    go.uber.org/zap v1.27.0
)
```

### Comandos essenciais
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

### Pipeline de CI/CD (ações do GitHub)
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

## Teste
### Testes unitários
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

### Testes HTTP baseados em tabela
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

## Interoperabilidade
### CGo (chamando C de Go)
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

### FFI com outros idiomas
| Direção | Mecanismo |
|-----------|-----------|
| Vá ligando para C | cgo (`import "C"`) |
| Vá chamando C++ | funções de wrapper cgo + C |
| C chamando Vai | Exportar funções Go com`//export`|
| Vá chamando Python | Use gopy ou subprocesso |
---

## Padrões de Projeto
### Padrão de middleware (HTTP)
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

### Padrão de opções
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

## Desempenho e otimização
### Perfil
```bash
go test -cpuprofile=cpu.prof -bench=. ./...
go tool pprof cpu.prof
go test -memprofile=mem.prof -bench=. ./...
go tool pprof mem.prof
```

### Dicas de otimização
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

## Implantação
### Compilação Cruzada
```bash
GOOS=linux GOARCH=amd64 go build -o myapp-linux
GOOS=windows GOARCH=amd64 go build -o myapp.exe
GOOS=darwin GOARCH=arm64 go build -o myapp-mac
```

### Implantação do Docker
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

## A Biblioteca Padrão
| Pacote | Finalidade |
|--------|---------|
| fmt | E/S formatada |
| rede/http | Cliente e servidor HTTP |
| codificação/json | Codificação/decodificação JSON |
| os | Operações em nível de sistema operacional |
| eu | Primitivas de E/S |
| strings/strconv | Manipulação de strings |
| sincronizar | Mutex, WaitGroup, uma vez |
| contexto | Prazos, cancelamento |
| testes | Estrutura de teste integrada |
| log / log/slog | Registro |
| tempo | Tempo e duração |
| criptografia | Criptografia (TLS, hash) |
| banco de dados/sql | Abstração de banco de dados |
---

## Ferramentas
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

## Quando usar Go
| Cenário | Por que ir | Melhor Alternativa |
|----------|--------|-------------------|
| Serviços/microsserviços nativos da nuvem | Binários pequenos e rápidos, HTTP excelente | Ferrugem para desempenho máximo |
| Ferramentas CLI | Compilação rápida, binário único | Ferrugem para CLIs complexos |
| Servidores Web/APIs | HTTP integrado, rápido, simples | Node.js/Express para prototipagem rápida |
| Ferramentas DevOps | Docker, Kubernetes e Terraform estão em alta | Python para scripts |
| Sistemas concorrentes | Goroutines são leves e elegantes | Erlang/Elixir para simultaneidade tolerante a falhas |
| Programação de rede | Excelente pacote líquido | C/C++ para controle de nível mais baixo |
| Ciência de dados / ML | Não é o ecossistema certo | Pitão, R |
| GUI para desktop/móvel | Nenhuma estrutura GUI | Use um front-end da web ou idioma nativo |
| Sistemas embarcados | Muito pesado (GC, tempo de execução) | C, ferrugem |
---

## Perguntas e respostas sintéticas
### Q1: Por que Go não tem exceções? Como devo lidar com erros?
**R:** Go usa retornos de erro explícitos em vez de exceções. Cada função que pode falhar retorna um`error`como seu último valor de retorno. Isso força o chamador a tratar os erros explicitamente – sem falhas silenciosas ou blocos catch esquecidos. O padrão idiomático é`if err != nil`. Use`fmt.Errorf`com`%w`para agrupar erros e `errors.Is`/`errors.As` para verificar tipos de erros. Para erros irrecuperáveis ​​(bugs de programação), use`panic`.
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

### Q2: O que são goroutines e como elas são diferentes dos threads do sistema operacional?
**R:** Goroutines são threads leves no espaço do usuário gerenciados pelo tempo de execução Go. Eles começam com aproximadamente 2 KB de pilha (vs. ~ 1 MB para threads do sistema operacional), são multiplexados em threads do sistema operacional pelo agendador e podem ser criados milhões de cada vez. A comunicação entre goroutines usa canais (ou primitivas`sync`para estado compartilhado). Sempre use`sync.WaitGroup`ou cancelamento de contexto para evitar vazamentos de goroutine.
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

### Q3: Quando devo usar canais versus mutexes para simultaneidade?
**R:** Use canais quando goroutines precisarem comunicar dados — eles reforçam a filosofia de "compartilhar memória através da comunicação". Use mutexes (`sync.Mutex`) quando goroutines precisarem proteger o estado compartilhado (caches, contadores, pools de conexões). Uma boa regra: se dados estiverem sendo passados ​​entre goroutines, use canais; se os dados estiverem sendo acessados ​​por vários goroutines, use um mutex. Para operações atômicas simples, use`sync/atomic`.
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

### Q4: Qual é a diferença entre fatias/mapas`nil`e fatias vazias?
**R:** Uma fatia`nil`(`var s []int`) não tem matriz subjacente, comprimento 0, capacidade 0. Uma fatia vazia (`s := []int{}`ou`make([]int, 0)`) tem uma matriz subjacente, mas comprimento 0. Ambas funcionam de forma idêntica com`append`,`len`,`cap`e`range`. O marshaling JSON é diferente: fatias nulas tornam-se`null`, fatias vazias tornam-se`[]`. Prática recomendada: prefira fatias nulas para valores de retorno (eles indicam "sem dados"), fatias vazias quando a saída JSON for importante.
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

### Q5: Como as interfaces funcionam no Go e qual é a interface vazia?
**R:** As interfaces Go são satisfeitas implicitamente — um tipo implementa uma interface implementando seus métodos, sem nenhuma palavra-chave `implements`. Isso permite dissociação e composição. A interface vazia`interface{}`(ou`any`no Go 1.18+) é satisfeita por todos os tipos — use-a com moderação (os genéricos geralmente são melhores). Os valores da interface são pares:`(type, value)`. Uma interface nula tem ambos como nulos.
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

## Resolução de problemas por cadeia de pensamento
### Problema 1: Construa um Web Scraper Simultâneo com Limitação de Taxa
**Declaração do problema:** Crie um programa Go que busque URLs de uma lista simultaneamente, extraia títulos de páginas, respeite um limite de taxa de 10 solicitações por segundo e colete resultados sem corridas de dados.
**Etapa 1 — Entenda o problema:**
Precisamos de: (1) busca HTTP simultânea com goroutines, (2) limitação de taxa para evitar servidores sobrecarregados, (3) coleta de resultados sem corridas, (4) tratamento adequado de erros para solicitações com falha. As primitivas de simultaneidade do Go (goroutines, canais,`errgroup`) são ideais para isso.
**Etapa 2 — Identifique a abordagem:**
- Use`golang.org/x/time/rate`para limitação de taxa de token-bucket.
- Use`sync.WaitGroup`ou`errgroup.Group`para gerenciar goroutines.
- Use um canal de resultados para coletar resultados com segurança.
- Use`context.Context`para cancelamento e tempos limite.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- Sem corridas de dados: cada goroutine grava em seu próprio índice em`results`— não é necessário mutex.
-`errgroup.SetLimit`limita a simultaneidade independentemente do limitador de taxa.
-`io.LimitReader`evita a leitura de páginas excessivamente grandes.
-`http.NewRequestWithContext`garante que as solicitações sejam canceladas quando o contexto for concluído.
- Para produção: adicione lógica de repetição com espera exponencial, ajuste de pool de conexões e métricas.
### Problema 2: Implementar um cache LRU genérico
**Declaração do problema:** Implemente um cache LRU (menos usado recentemente) genérico e seguro para threads em Go usando genéricos (Go 1.18+). Deve suportar`Get`,`Set`e`Delete`com complexidade de tempo O(1).
**Etapa 1 — Entenda o problema:**
Um cache LRU precisa de pesquisa O(1) (mapa hash) e atualizações de ordenação O(1) (lista duplamente vinculada). Em `Get`: mova o item para a frente. Em `Set`: inserir na frente; despejar de trás se estiver acima da capacidade. A segurança do thread requer um mutex.
**Etapa 2 — Identifique a abordagem:**
- Use`container/list`(lista duplamente vinculada) para O(1) mover para frente e remover de trás.
- Use`map[K]*list.Element`para pesquisa O(1).
- Use`sync.Mutex`para segurança de thread.
- Genéricos (`[K comparable, V any]`) para segurança de tipo.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- O(1) para`Get`,`Set`,`Delete`: a pesquisa do mapa é média O(1); operações de lista (`MoveToFront`,`PushFront`,`Remove`,`Back`) são todas O(1).
- Segurança de thread:`sync.Mutex`garante que apenas uma goroutine acesse o cache por vez. Para cargas de trabalho com muita leitura, use`sync.RWMutex`.
- Genéricos:`[K comparable, V any]`garante que as chaves suportem`==`(obrigatório para chaves de mapa), enquanto os valores podem ser de qualquer tipo.
- Produção: considere`github.com/hashicorp/golang-lru/v2`— testado em batalha com suporte TTL e fragmentação para redução de contenção de bloqueio.
### Problema 3: Construa um servidor de bate-papo TCP
**Declaração do problema:** Construa um servidor de bate-papo TCP simultâneo onde os clientes possam se conectar, transmitir mensagens para todos os outros clientes conectados e desconectar-se normalmente. Lide com clientes lentos sem bloquear outros.
**Etapa 1 — Entenda o problema:**
Precisamos de: (1) aceitar conexões TCP, (2) uma goroutine por cliente para leitura, (3) um mecanismo de broadcast para enviar mensagens a todos os clientes, (4) lidar com desconexões e clientes lentos. Este é um padrão clássico de fan-out.
**Etapa 2 — Identifique a abordagem:**
- Use`net.Listener`para conexões TCP.
- Use uma goroutine central`hub`com canais para registro/cancelamento de registro/transmissão de clientes.
- Cada cliente recebe uma rotina de gravação dedicada com um canal em buffer - clientes lentos não bloqueiam outros.
- Use`context.Context`para um desligamento normal.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- Tratamento lento do cliente: o`select`com`default`em broadcast impede o bloqueio. Clientes lentos serão desconectados se o buffer ficar cheio.
- Sem corridas: o hub goroutine é o único escritor do mapa `clients`; `mu`protege leituras durante a transmissão.
- Desligamento normal: adicione`context.Context`e um manipulador de sinal para fechar o ouvinte e drenar conexões.
- Produção: considere usar`golang.org/x/net/websocket`para clientes de navegador e adicione autenticação, histórico de mensagens e salas.
---

## Resumo
Go é uma linguagem que escolhe deliberadamente a simplicidade em vez dos recursos. Ela tem menos construções que a maioria das linguagens – sem herança, sem sobrecarga de métodos, sem exceções, sem macros – e isso é um ponto forte. O resultado é um código fácil de ler, escrever e manter. O modelo de simultaneidade do Go (goroutines e canais) é um dos mais bem projetados em qualquer linguagem. Para infraestrutura em nuvem, microsserviços, ferramentas CLI e programação de rede, Go é uma excelente escolha.