---
# Metadata
title: "Go — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, idiomatic Go code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [go, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "16 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Go — Mga Idiomatic Pattern at Pinakamahuhusay na Kasanayan
Sinasaklaw ng gabay na ito ang mga idiomatic pattern at pinakamahuhusay na kagawian para sa pagsusulat ng malinis at idiomatic na Go code.
---

## Error sa Paghawak
```go
// ✅ Always check errors
result, err := doSomething()
if err != nil {
    return fmt.Errorf("doSomething: %w", err)
}

// ✅ Wrap errors with context
func (s *UserService) FindUser(id int64) (*User, error) {
    user, err := s.repo.FindByID(id)
    if err != nil {
        return nil, fmt.Errorf("find user %d: %w", id, err)
    }
    return user, nil
}

// ✅ Sentinel errors
var (
    ErrNotFound    = errors.New("not found")
    ErrUnauthorized = errors.New("unauthorized")
)

// ✅ errors.Is / errors.As
if errors.Is(err, ErrNotFound) {
    http.Error(w, "not found", http.StatusNotFound)
}

var valErr *ValidationError
if errors.As(err, &valErr) {
    // handle validation error
}

// ✅ Custom error types
type NotFoundError struct {
    Entity string
    ID     any
}

func (e *NotFoundError) Error() string {
    return fmt.Sprintf("%s %v not found", e.Entity, e.ID)
}
```

---

## Mga Interface
```go
// ✅ Accept interfaces, return structs
func Save(w io.Writer, data []byte) error {
    _, err := w.Write(data)
    return err
}

// ✅ Small interfaces (1-3 methods)
type Reader interface {
    Read(p []byte) (n int, err error)
}

type Store interface {
    Get(ctx context.Context, key string) ([]byte, error)
    Set(ctx context.Context, key string, value []byte) error
}

// ✅ Interface satisfaction (compile-time check)
var _ Store = (*MemoryStore)(nil)

// ✅ Define interfaces where they're used, not where implemented
type UserFinder interface {
    FindByID(ctx context.Context, id int64) (*User, error)
}
```

---

## Mga Istraktura at Paraan
```go
// ✅ Receiver: value for read-only, pointer for mutation
type User struct {
    Name  string
    Email string
}

func (u User) DisplayName() string {  // value receiver
    return u.Name
}

func (u *User) SetEmail(email string) {  // pointer receiver
    u.Email = email
}

// ✅ Constructor function
func NewUser(name, email string) *User {
    return &User{Name: name, Email: email}
}

// ✅ Unexported fields
type Config struct {
    Host     string  // exported
    port     int     // unexported (private)
    password string  // unexported
}
```

---

## Kasabay
```go
// ✅ Goroutines with context
func processAll(ctx context.Context, items []Item) error {
    g, ctx := errgroup.WithContext(ctx)
    
    for _, item := range items {
        item := item  // capture loop variable
        g.Go(func() error {
            return process(ctx, item)
        })
    }
    
    return g.Wait()
}

// ✅ Channels for communication
func fanIn(ctx context.Context, channels ...<-chan string) <-chan string {
    out := make(chan string)
    var wg sync.WaitGroup
    
    for _, ch := range channels {
        wg.Add(1)
        go func(c <-chan string) {
            defer wg.Done()
            for v := range c {
                select {
                case out <- v:
                case <-ctx.Done():
                    return
                }
            }
        }(ch)
    }
    
    go func() { wg.Wait(); close(out) }()
    return out
}

// ✅ Select for multiplexing
select {
case result := <-ch:
    handle(result)
case <-ctx.Done():
    return ctx.Err()
case <-time.After(5 * time.Second):
    return errors.New("timeout")
}
```

---

## Mga hiwa at Mapa
```go
// ✅ Pre-allocate slices
results := make([]User, 0, len(ids))
for _, id := range ids {
    results = append(results, findUser(id))
}

// ✅ Copy slices explicitly
dst := make([]int, len(src))
copy(dst, src)

// ✅ Map access with ok check
value, ok := m[key]
if !ok {
    value = defaultValue
}

// ✅ Map iteration order is random — sort if needed
keys := make([]string, 0, len(m))
for k := range m {
    keys = append(keys, k)
}
sort.Strings(keys)
for _, k := range keys {
    fmt.Println(k, m[k])
}
```

---

## Generics (Go 1.18+)
```go
// ✅ Generic functions
func Map[T any, U any](items []T, fn func(T) U) []U {
    result := make([]U, len(items))
    for i, item := range items {
        result[i] = fn(item)
    }
    return result
}

// ✅ Generic with constraints
func Min[T constraints.Ordered](a, b T) T {
    if a < b { return a }
    return b
}

// ✅ Generic types
type Set[T comparable] struct {
    items map[T]struct{}
}

func NewSet[T comparable]() *Set[T] {
    return &Set[T]{items: make(map[T]struct{})}
}

func (s *Set[T]) Add(item T) { s.items[item] = struct{}{} }
func (s *Set[T]) Contains(item T) bool { _, ok := s.items[item]; return ok }
```

---

## Organisasyon ng Package
```go
// ✅ Package naming
package user      // not: userpackage, user_package, userPackage

// ✅ File naming
user_service.go   // not: UserService.go, user-service.go

// ✅ Avoid package-level init()
// ❌
func init() { setupDatabase() }

// ✅ Explicit initialization
func NewApp(cfg Config) (*App, error) {
    db, err := setupDatabase(cfg)
    if err != nil { return nil, err }
    return &App{db: db}, nil
}

// ✅ go vet, staticcheck, golangci-lint
// go vet ./...
// staticcheck ./...
// golangci-lint run
```

---

## Pagsubok
```go
// ✅ Table-driven tests
func TestAdd(t *testing.T) {
    tests := []struct {
        name     string
        a, b     int
        expected int
    }{
        {"positive", 2, 3, 5},
        {"negative", -1, -2, -3},
        {"zero", 0, 0, 0},
    }
    
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got := Add(tt.a, tt.b)
            if got != tt.expected {
                t.Errorf("Add(%d, %d) = %d, want %d", tt.a, tt.b, got, tt.expected)
            }
        })
    }
}

// ✅ Use testify for assertions
assert.Equal(t, expected, actual)
require.NoError(t, err)
```

---

## Buod
Binibigyang-diin ng mga idyoma ng Go ang: pagiging simple, tahasang paghawak ng error, maliliit na interface, komposisyon sa mana, mga goroutine na may konteksto, at "tanggapin ang mga interface, ibalik ang mga istruktura." Sundin ang`gofmt`para sa pag-format,`golangci-lint`para sa linting, at ang opisyal na gabay sa Go Code Review Comments. Pinahahalagahan ng komunidad ng Go ang pagiging madaling mabasa, pagiging simple, at "ang malinaw na paraan upang gawin ito." Iwasan ang matalinong code — Dapat ay boring at predictable ang Go code.