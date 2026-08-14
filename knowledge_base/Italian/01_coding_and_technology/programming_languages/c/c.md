<!--
---
# Metadata
title: "C"
description: "Comprehensive reference for the C programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
tags: [c, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "35 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# C
C è un linguaggio di programmazione procedurale di uso generale creato da Dennis Ritchie ai Bell Labs tra il 1969 e il 1973. È stato progettato per implementare il sistema operativo Unix e rimane uno dei linguaggi di programmazione più utilizzati oltre 50 anni dopo. Il C fornisce accesso alla memoria di basso livello, una libreria standard minima e una mappatura pulita delle istruzioni della macchina, rendendolo la base su cui è costruita la maggior parte dei computer moderni.
C è il linguaggio alla base dei sistemi operativi (Linux, kernel di Windows, macOS), dei sistemi embedded, dei motori di database (SQLite, PostgreSQL), dei compilatori (CPython di Python, MRI di Ruby) e praticamente di ogni altro runtime del linguaggio di programmazione. Comprendere il C significa capire come funzionano effettivamente i computer.
---

## Perché C è importante
- **Vicinanza all'hardware**: il C è molto simile al codice macchina. Non esiste un garbage collector, nessun sovraccarico di runtime, nessuna allocazione nascosta.
- **Ubiquità**: dai microcontrollori ai supercomputer, il C funziona ovunque.
- **Fondamenti dell'informatica**: Linux, Windows, kernel macOS, interprete Python, SQLite, Git -- tutti scritti in C.
- **Prestazioni**: velocità di esecuzione quasi ottimale con controllo completo sul layout della memoria.
- **Influenza**: la sintassi e i concetti del C (puntatori, array, strutture, funzioni) hanno plasmato C++, Java, C#, JavaScript, Go, Rust e la maggior parte dei linguaggi successivi.
## I compromessi
| Limitazione | Dettagli | Soluzione tipica |
|-----------|---------|-------------|
| **Gestione manuale della memoria** | Nessun garbage collector: allochi e liberi tu stesso la memoria | Uso attento di malloc/free; Modelli RAII in C++ |
| **Buffer overflow** | Nessun limite di controllo sugli array: facile da scrivere oltre le estremità del buffer | Usa strncpy invece di strcpy; abilitare gli avvisi del compilatore |
| **Nessun OOP integrato** | Solo procedurale: nessuna classe, ereditarietà o metodo | Usa strutture + puntatori a funzione; o passare a C++ |
| **Libreria standard limitata** | Funzionalità integrate minime | Librerie di terze parti o scrivi le tue |
| **Comportamento indefinito** | Molti errori vengono compilati correttamente ma si bloccano in modo imprevedibile | Utilizzare disinfettanti, analizzatori statici |
---

## Fondamenti di sintassi
### Struttura di base
Ogni programma C inizia da`main()`. Il linguaggio viene compilato: il codice sorgente diventa codice macchina tramite un compilatore (GCC, Clang, MSVC).
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int add(int a, int b) {
    return a + b;
}

int main(void) {
    int result = add(3, 5);
    printf("Result: %d\n", result);
    return 0;
}
```

### Variabili e tipi
C è tipizzato staticamente: ogni variabile ha un tipo fisso noto in fase di compilazione.
```c
int count = 42;              // 4 bytes (typically)
float pi = 3.14159f;         // 4 bytes
double precise = 3.14159;    // 8 bytes
char letter = 'A';           // 1 byte
long big = 1000000L;         // 4 or 8 bytes depending on platform

#define MAX_SIZE 1024
const float GRAVITY = 9.81f;

int numbers[5] = {1, 2, 3, 4, 5};
char name[] = "Hello";       // Size inferred: 6 bytes (includes \0)

struct Point {
    float x;
    float y;
};
struct Point p;
p.x = 3.0f;
p.y = 4.0f;
```

### Puntatori
I puntatori sono la caratteristica più potente e più fraintesa del C. Un puntatore contiene un indirizzo di memoria.
```c
int value = 42;
int *ptr = &value;     // ptr holds the address of value

printf("%d\n", *ptr);  // Dereference: prints 42
printf("%p\n", ptr);   // Prints the memory address

// Pointers and arrays are closely related
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;          // p points to arr[0]
printf("%d\n", *(p+2)); // prints 30 (arr[2])

// Dynamic memory allocation
int *dynamic = (int *)malloc(10 * sizeof(int));
if (dynamic == NULL) {
    fprintf(stderr, "Memory allocation failed\n");
    exit(1);
}
dynamic[0] = 100;
free(dynamic);   // Always free what you malloc!
dynamic = NULL;  // Prevent use-after-free
```

### Flusso di controllo
```c
if (score >= 90) {
    grade = 'A';
} else if (score >= 80) {
    grade = 'B';
} else {
    grade = 'C';
}

for (int i = 0; i < 10; i++) {
    printf("%d ", i);
}

while (running) {
    process_input();
}

do {
    check_status();
} while (status == PENDING);

switch (command) {
    case START:   run();     break;
    case STOP:    halt();    break;
    case PAUSE:   suspend(); break;
    default:      printf("Unknown command\n");
}
```

### Funzioni e stack
```c
// Pass by value (default)
void increment(int x) {
    x++;  // Only modifies the local copy
}

// Pass by pointer -- function can modify the original
void increment_ptr(int *x) {
    (*x)++;
}

// Variadic functions (like printf)
#include <stdarg.h>
double average(int count, ...) {
    va_list args;
    va_start(args, count);
    double sum = 0;
    for (int i = 0; i < count; i++) {
        sum += va_arg(args, double);
    }
    va_end(args);
    return sum / count;
}
```

---

## Disposizione della memoria
```
+---------------------+ High addresses
|     Stack           | <- Local variables, function call frames
|       | grows       |   (automatically cleaned up when function returns)
+---------------------+
|       | grows       |
|      Heap           | <- malloc/calloc allocations
|                     |   (you must free() these manually)
+---------------------+
|  BSS segment        | <- Uninitialised global/static variables
+---------------------+
|  Data segment       | <- Initialised global/static variables
+---------------------+
|  Text segment       | <- Compiled machine code (read-only)
+---------------------+ Low addresses
```

| Regione | Cosa c'è | A vita | Chi lo gestisce |
|--------|----------------|----------|----------------|
| **Pila** | Variabili locali, parametri di funzione | Finché la funzione non restituisce | Compilatore (automatico) |
| **Mucchio** | allocazioni malloc/calloc | Finché non chiami free() | Tu (manuale) |
| **Dati/BSS** | Variabili globali e statiche | Durata intera del programma | Compilatore (automatico) |
| **Testo** | Codice macchina | Durata intera del programma | Sola lettura |
---

## La libreria standard
| Intestazione | Scopo | Funzioni comuni |
|--------|---------|-----------------|
| `<stdio.h>`| Ingresso/uscita | printf, scanf, fopen, fgets, fprintf |
| `<stdlib.h>`| Utilità generali | malloc, gratuito, esci, atoi, rand, qsort |
| `<string.h>`| Operazioni sulle stringhe | strlen, strcpy, strncpy, strcmp, memcpy |
| `<math.h>`| Matematica | sin, cos, sqrt, pow, fabs, ceil, floor |
| `<ctype.h>`| Classificazione dei caratteri | isalfa, iscifra, toupper, tolower |
| `<time.h>`| Data e ora | tempo, orologio, difftime, strftime |
| `<assert.h>`| Asserzioni di debug | asserire(condizione) |
| `<errno.h>`| Codici di errore | errno, perror, strerror |
---

## Sintassi e modelli avanzati
### Macro del preprocessore
```c
// Safe macro with do-while wrapper
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ARRAY_LEN(arr) (sizeof(arr) / sizeof((arr)[0]))

#define SAFE_COPY(dst, src, size) do { \
    if ((size) > 0) {                  \
        strncpy((dst), (src), (size)-1); \
        (dst)[(size)-1] = '\0';        \
    }                                  \
} while(0)

// Conditional compilation
#ifdef DEBUG
    #define LOG(fmt, ...) fprintf(stderr, fmt "\n", ##__VA_ARGS__)
#else
    #define LOG(fmt, ...) ((void)0)
#endif

// Stringify and concatenation
#define STR(x) #x
#define CONCAT(a, b) a##b
```

### Puntatori a funzioni e callback
```c
#include <stdio.h>

// Function pointer type
typedef int (*Comparator)(const void *, const void *);

// Using function pointers for callbacks
int ascending(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int descending(const void *a, const void *b) {
    return (*(int*)b - *(int*)a);
}

void print_array(int *arr, int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main(void) {
    int data[] = {5, 2, 8, 1, 9, 3};
    int n = ARRAY_LEN(data);

    // qsort uses function pointers for custom comparison
    qsort(data, n, sizeof(int), ascending);
    print_array(data, n);  // 1 2 3 5 8 9

    qsort(data, n, sizeof(int), descending);
    print_array(data, n);  // 9 8 5 3 2 1

    return 0;
}
```

### Modelli personalizzati di gestione degli errori
```c
#include <stdio.h>
#include <stdlib.h>

// Error code enum
typedef enum {
    ERR_OK = 0,
    ERR_NULL_PTR = -1,
    ERR_ALLOC = -2,
    ERR_IO = -3,
    ERR_INVALID_ARG = -4,
} ErrorCode;

// Error string lookup
const char *error_string(ErrorCode code) {
    switch (code) {
        case ERR_OK:           return "Success";
        case ERR_NULL_PTR:     return "Null pointer";
        case ERR_ALLOC:        return "Allocation failed";
        case ERR_IO:           return "IO error";
        case ERR_INVALID_ARG:  return "Invalid argument";
        default:               return "Unknown error";
    }
}

// Error propagation pattern (goto cleanup)
ErrorCode process_file(const char *path) {
    FILE *fp = NULL;
    char *buffer = NULL;
    ErrorCode err = ERR_OK;

    if (path == NULL) { err = ERR_NULL_PTR; goto cleanup; }

    fp = fopen(path, "r");
    if (!fp) { err = ERR_IO; goto cleanup; }

    buffer = (char *)malloc(4096);
    if (!buffer) { err = ERR_ALLOC; goto cleanup; }

    // ... process file ...

cleanup:
    free(buffer);
    if (fp) fclose(fp);
    if (err != ERR_OK)
        fprintf(stderr, "Error: %s\n", error_string(err));
    return err;
}
```

---

## Concorrenza e parallelismo
### Thread POSIX (pthread)
```c
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

// Thread function
void *worker(void *arg) {
    int id = *(int *)arg;
    printf("Thread %d running\n", id);
    return NULL;
}

int main(void) {
    pthread_t threads[5];
    int ids[5];

    for (int i = 0; i < 5; i++) {
        ids[i] = i;
        pthread_create(&threads[i], NULL, worker, &ids[i]);
    }

    for (int i = 0; i < 5; i++) {
        pthread_join(threads[i], NULL);
    }
    return 0;
}
```

### Mutex e stato condiviso
```c
#include <pthread.h>

typedef struct {
    int count;
    pthread_mutex_t lock;
} Counter;

void *increment(void *arg) {
    Counter *c = (Counter *)arg;
    for (int i = 0; i < 100000; i++) {
        pthread_mutex_lock(&c->lock);
        c->count++;
        pthread_mutex_unlock(&c->lock);
    }
    return NULL;
}

int main(void) {
    Counter counter = {0, PTHREAD_MUTEX_INITIALIZER};
    pthread_t t1, t2;

    pthread_create(&t1, NULL, increment, &counter);
    pthread_create(&t2, NULL, increment, &counter);
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    printf("Final count: %d\n", counter.count);
    pthread_mutex_destroy(&counter.lock);
    return 0;
}
```

### C11 Atomici e fili
```c
#include <stdatomic.h>
#include <threads.h>

atomic_int shared_count = 0;

int worker(void *arg) {
    for (int i = 0; i < 1000; i++) {
        atomic_fetch_add(&shared_count, 1);
    }
    return 0;
}

int main(void) {
    thrd_t t1, t2;
    thrd_create(&t1, worker, NULL);
    thrd_create(&t2, worker, NULL);
    thrd_join(t1, NULL);
    thrd_join(t2, NULL);
    printf("Count: %d\n", atomic_load(&shared_count));
    return 0;
}
```

---

## Configurazione del progetto e sistema di creazione
### Struttura del progetto
```
my_project/
+-- CMakeLists.txt        # CMake build configuration
+-- Makefile              # Alternative: Make build
+-- src/
|   +-- main.c
|   +-- utils.c
|   +-- utils.h
|   +-- parser.c
|   +-- parser.h
+-- include/
|   +-- config.h
|   +-- types.h
+-- tests/
|   +-- test_utils.c
|   +-- test_parser.c
+-- lib/                  # Third-party libraries
+-- build/                # Build output (gitignored)
+-- .clang-format         # Code style configuration
+-- .clang-tidy           # Linter configuration
```

### CMakeLists.txt
```cmake
cmake_minimum_required(VERSION 3.20)
project(my_project VERSION 1.0.0 LANGUAGES C)

set(CMAKE_C_STANDARD 17)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Compiler warnings
add_compile_options(-Wall -Wextra -Wpedantic)

# Source files
set(SOURCES
    src/main.c
    src/utils.c
    src/parser.c
)

# Main executable
add_executable(my_app ${SOURCES})
target_include_directories(my_app PRIVATE include)

# Link math library on Unix
if(UNIX)
    target_link_libraries(my_app m pthread)
endif()

# Release build optimisation
if(CMAKE_BUILD_TYPE STREQUAL "Release")
    target_compile_options(my_app PRIVATE -O2)
endif()

# Testing
enable_testing()
add_executable(test_utils tests/test_utils.c src/utils.c)
target_include_directories(test_utils PRIVATE include)
add_test(NAME UtilsTest COMMAND test_utils)
```

### Makefile
```makefile
CC = gcc
CFLAGS = -Wall -Wextra -std=c17 -Iinclude
LDFLAGS = -lm -lpthread

SRCS = src/main.c src/utils.c src/parser.c
OBJS = $(SRCS:.c=.o)
TARGET = my_app

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	find . -name "*.o" -delete
	find . -name "$(TARGET)" -delete

debug: CFLAGS += -g -DDEBUG -fsanitize=address
debug: clean all

.PHONY: all clean debug
```

### Pipeline CI/CD (azioni GitHub)
```yaml
name: C CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  build:
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - run: cmake -B build -DCMAKE_BUILD_TYPE=Debug
      - run: cmake --build build
      - run: ctest --test-dir build --output-on-failure
```

---

## Test
### Test unitari con un framework semplice
```c
#include <stdio.h>
#include <assert.h>
#include "utils.h"

// Simple test macros
#define TEST(name) void name(void)
#define ASSERT_EQ(a, b) do { \
    if ((a) != (b)) { \
        fprintf(stderr, "FAIL: %s:%d: %d != %d\n", __FILE__, __LINE__, (a), (b)); \
        exit(1); \
    } \
} while(0)

#define ASSERT_STR_EQ(a, b) do { \
    if (strcmp((a), (b)) != 0) { \
        fprintf(stderr, "FAIL: %s:%d: \"%s\" != \"%s\"\n", __FILE__, __LINE__, (a), (b)); \
        exit(1); \
    } \
} while(0)

TEST(test_add) {
    ASSERT_EQ(add(2, 3), 5);
    ASSERT_EQ(add(-1, 1), 0);
    ASSERT_EQ(add(0, 0), 0);
}

TEST(test_string_trim) {
    char buf[64];
    strcpy(buf, "  hello  ");
    trim(buf);
    ASSERT_STR_EQ(buf, "hello");
}

int main(void) {
    test_add();
    printf("test_add passed\n");
    test_string_trim();
    printf("test_string_trim passed\n");
    printf("All tests passed!\n");
    return 0;
}
```

```bash
# Compile and run tests
gcc -Wall -o test_utils tests/test_utils.c src/utils.c -Iinclude
./test_utils

# Run with AddressSanitizer
gcc -fsanitize=address -g -o test_utils tests/test_utils.c src/utils.c -Iinclude
./test_utils
```

---

## Interoperabilità
### Chiamare C da Python (ctypes)
```c
// mathlib.c -- compile to shared library
// gcc -shared -fPIC -o libmathlib.so mathlib.c
int c_add(int a, int b) { return a + b; }
double c_sqrt(double x) {
    if (x < 0) return -1.0;
    // Newton's method
    double guess = x / 2.0;
    for (int i = 0; i < 100; i++)
        guess = (guess + x / guess) / 2.0;
    return guess;
}
```

```python
# Python side
import ctypes
lib = ctypes.CDLL("./libmathlib.so")
lib.c_add.argtypes = [ctypes.c_int, ctypes.c_int]
lib.c_add.restype = ctypes.c_int
print(lib.c_add(3, 5))  # 8
```

### Chiamare C da altre lingue
| Lingua | Meccanismo | Esempio |
|----------|-----------|---------|
| Pitone | ctypes, cffi | `ctypes.CDLL("./lib.so")`|
| Rubino | Violino | `Fiddle.dlopen("./lib.so")`|
| Giava | JNI | `System.loadLibrary("mylib")`|
| C++ | esterno "C" | `extern "C" void my_func();`|
| Ruggine | esterno "C" + FFI | `extern "C" { fn my_func(); }`|
---

## Modelli di progettazione
### Puntatore opaco (idioma Pimpl in C)
```c
// stack.h -- public interface (implementation hidden)
typedef struct Stack Stack;

Stack *stack_create(void);
void stack_destroy(Stack *s);
void stack_push(Stack *s, int value);
int stack_pop(Stack *s);
int stack_is_empty(const Stack *s);

// stack.c -- private implementation
struct Stack {
    int *data;
    int top;
    int capacity;
};

Stack *stack_create(void) {
    Stack *s = malloc(sizeof(Stack));
    s->data = malloc(16 * sizeof(int));
    s->top = -1;
    s->capacity = 16;
    return s;
}

void stack_push(Stack *s, int value) {
    if (++s->top == s->capacity) {
        s->capacity *= 2;
        s->data = realloc(s->data, s->capacity * sizeof(int));
    }
    s->data[s->top] = value;
}
```

### Tabella virtuale (OOP in C)
```c
typedef struct {
    void (*speak)(const void *self);
    void (*destroy)(void *self);
} AnimalVTable;

typedef struct {
    const AnimalVTable *vtable;
    char name[64];
} Animal;

void animal_speak(const Animal *a) { a->vtable->speak(a); }

// Dog implementation
typedef struct { Animal base; int trick_count; } Dog;
void dog_speak(const void *self) { printf("Woof!\n"); }
void dog_destroy(void *self) { free(self); }

static const AnimalVTable dog_vtable = { dog_speak, dog_destroy };
Animal *dog_create(const char *name) {
    Dog *d = calloc(1, sizeof(Dog));
    d->base.vtable = &dog_vtable;
    strncpy(d->base.name, name, 63);
    return (Animal *)d;
}
```

---

## Prestazioni e ottimizzazione
### Strumenti di profilazione
```bash
# GCC profiling with gprof
gcc -pg -O2 -o my_app main.c
./my_app
gprof my_app gmon.out > profile.txt

# perf (Linux)
perf record -g ./my_app
perf report

# Valgrind for cache profiling
valgrind --tool=cachegrind ./my_app

# Memory leak detection
valgrind --tool=memcheck --leak-check=full ./my_app

# AddressSanitizer (compile-time)
gcc -fsanitize=address,undefined -g -o my_app main.c
```

### Tecniche di ottimizzazione
```c
// Struct packing to reduce memory
#pragma pack(push, 1)
typedef struct {
    uint8_t type;
    uint32_t id;
    uint16_t value;
} PackedRecord;  // 7 bytes instead of 12 (with padding)
#pragma pack(pop)

// Cache-friendly access patterns (row-major order)
for (int i = 0; i < rows; i++)
    for (int j = 0; j < cols; j++)
        matrix[i][j] = 0;  // Sequential memory access

// Branch prediction hints
#define LIKELY(x)   __builtin_expect(!!(x), 1)
#define UNLIKELY(x) __builtin_expect(!!(x), 0)

if (LIKELY(ptr != NULL)) {
    // Fast path
}
```

---

## Distribuzione
### Compilazione incrociata
```bash
# Cross-compile for ARM (embedded)
arm-none-eabi-gcc -mcpu=cortex-m4 -o firmware.elf main.c

# Cross-compile for Windows from Linux
x86_64-w64-mingw32-gcc -o my_app.exe main.c

# Static linking (no shared library dependencies)
gcc -static -o my_app main.c
```

### Distribuzione Docker
```dockerfile
FROM gcc:13 AS builder
WORKDIR /app
COPY src/ ./
RUN gcc -O2 -Wall -o my_app main.c utils.c

FROM debian:bookworm-slim
COPY --from=builder /app/my_app /usr/local/bin/my_app
CMD ["my_app"]
```

---

## Modelli e modi di dire comuni
```c
// Safe string copy (prevents buffer overflow)
#define SAFE_COPY(dst, src, size) do { \
    if ((size) > 0) {                  \
        strncpy((dst), (src), (size)-1); \
        (dst)[(size)-1] = '\0';        \
    }                                  \
} while(0)

// Macro for array length
#define ARRAY_LEN(arr) (sizeof(arr) / sizeof((arr)[0]))

// Typedef for cleaner struct usage
typedef struct {
    float x, y, z;
} Vec3;

// Linked list node
typedef struct Node {
    int data;
    struct Node *next;
} Node;
```

---

## Compilazione e strumenti
```bash
gcc -Wall -Wextra -o myprogram myprogram.c      # Basic compile
gcc -g -Wall -o myprogram myprogram.c            # With debug symbols
gcc -O2 -Wall -o myprogram myprogram.c           # With optimisation
gcc -std=c17 -Wall -o myprogram myprogram.c      # Specific standard
make          # Runs the Makefile
make clean    # Removes build artifacts
```

| Strumento | Scopo |
|------|---------|
| **GCC / Clang** | Compilatori |
| **Crea / CMake** | Costruisci sistemi |
| **GDB** | Debug |
| **Valgrind** | Rilevatore di errori di memoria (perdite, accesso non valido) |
| **IndirizzoSanitizer** | Controllo della memoria in fase di compilazione |
| **cppcheck** | Analisi statica |
| **formato clang** | Formattazione del codice |
---

## Quando utilizzare C
| Scenario | Perché C | Alternativa migliore |
|----------|-------|-------------|
| Sistemi operativi | Accesso diretto all'hardware, nessun sovraccarico di runtime | -- |
| Sistemi embedded/microcontrollori | Ingombro minimo, funziona con qualsiasi cosa | Ruggine per incorporati critici per la sicurezza |
| Motori di database | Massime prestazioni, controllo completo della memoria | -- |
| Compilatori e interpreti | Veloce, portatile, ben compreso | C++ per progetti di compilatori più grandi |
| Driver di dispositivo | Richiesto dalla maggior parte delle API del kernel del sistema operativo | -- |
| Librerie critiche per le prestazioni | Velocità quasi ottimale | Ruggine per la sicurezza della memoria garantita |
| Sviluppo di applicazioni generali | Troppo lavoro manuale | Python, Java, Go, C# |
| Sviluppo web | Strumento completamente sbagliato | JavaScript, Go, Python |
| Scienza dei dati/ML | Nessun ecosistema per questo | Pitone, R, Julia |
---

## Standard C
| Norma | Anno | Aggiunte chiave |
|----------|------|--------------|
| C89/C90 | 1989/1990| L'ANSI C originale - ancora la linea di base |
| C99 | 1999 | // commenti, tipo bool, array a lunghezza variabile, inline, stdint.h |
| C11 | 2011 | Operazioni atomiche, thread, strutture anonime, _Generic |
| C17 | 2018 | Correzioni di bug e chiarimenti (nessuna nuova funzionalità) |
| C23 | 2024 | nullptr, typeof, constexpr, preprocessore migliorato |
La maggior parte del codice di produzione ha come target C11 o C17. C23 offre comodità moderne ma l'adozione richiede tempo.
---

## Domande e risposte sintetiche
### D1: Qual è la differenza tra puntatori e array in C?
**R:** Array e puntatori sono correlati ma distinti. Un array è un blocco di memoria contiguo con una dimensione fissa nota in fase di compilazione. Un puntatore è una variabile che contiene un indirizzo di memoria. Gli array decadono in puntatori quando vengono passati alle funzioni, ma`sizeof(array)`fornisce la dimensione totale mentre`sizeof(pointer)`fornisce solo la dimensione del puntatore (4 o 8 byte). I nomi degli array non sono lvalue modificabili: non puoi fare`arr++`.
```c
int arr[5] = {1, 2, 3, 4, 5};
int *ptr = arr;       // Array decays to pointer to first element

printf("%zu\n", sizeof(arr));   // 20 (5 * sizeof(int))
printf("%zu\n", sizeof(ptr));   // 8 (on 64-bit system)

// arr++;        // Error: array is not a modifiable lvalue
ptr++;           // OK: pointer arithmetic

// They behave the same for indexing
printf("%d\n", arr[2]);   // 3
printf("%d\n", ptr[2]);   // 3
printf("%d\n", *(arr + 2)); // 3 — pointer arithmetic
```

### D2: Come posso gestire correttamente la memoria ed evitare perdite di dati?
**R:** Ogni`malloc`/`calloc`deve avere un`free`corrispondente. Errori comuni: dimenticare di liberare (perdita), liberare due volte (comportamento non definito), utilizzare la memoria dopo la liberazione (use-after-free) e non controllare il valore restituito`malloc`(NULL in caso di errore). Procedura consigliata: allocare e liberare nello stesso modulo, utilizzare il modello "goto cleanup" per la gestione degli errori e impostare sempre i puntatori liberati su NULL.
```c
// Proper allocation pattern with cleanup
char *load_file(const char *path) {
    FILE *f = fopen(path, "r");
    if (!f) return NULL;

    fseek(f, 0, SEEK_END);
    long size = ftell(f);
    rewind(f);

    char *buf = malloc(size + 1);
    if (!buf) {
        fclose(f);
        return NULL;
    }

    if (fread(buf, 1, size, f) != (size_t)size) {
        free(buf);
        buf = NULL;   // Prevent dangling pointer
        fclose(f);
        return NULL;
    }
    buf[size] = '\0';

    fclose(f);
    return buf;
}

// Usage
char *data = load_file("config.txt");
if (data) {
    process(data);
    free(data);
    data = NULL;  // Defensive: catch use-after-free
}
```

### D3: Quali sono le migliori pratiche per la gestione degli errori in C?
**A:** C non ha eccezioni. La gestione degli errori utilizza valori restituiti (codici di errore, puntatori NULL, valori negativi). Il modello standard: le funzioni restituiscono un codice di stato o NULL in caso di errore e impostano`errno`per le chiamate di sistema. Utilizzare il modello "goto cleanup" per la pulizia delle risorse in caso di errori. Controlla sempre i valori restituiti di`malloc`,`fopen`e altre funzioni che possono fallire.
```c
#include <errno.h>
#include <string.h>

// Error code pattern
typedef enum {
    OK = 0,
    ERR_NULL_PTR = -1,
    ERR_NOT_FOUND = -2,
    ERR_IO = -3,
} Status;

Status read_config(const char *path, Config *out) {
    if (!path || !out) return ERR_NULL_PTR;

    FILE *f = fopen(path, "r");
    if (!f) {
        fprintf(stderr, "Cannot open %s: %s\n", path, strerror(errno));
        return ERR_IO;
    }

    // ... parse config ...

    fclose(f);
    return OK;
}

// Usage
Config cfg;
Status s = read_config("app.conf", &cfg);
if (s != OK) {
    fprintf(stderr, "Config error: %d\n", s);
    exit(EXIT_FAILURE);
}
```

### D4: In che modo le strutture, le unioni e i bitfield differiscono nel layout della memoria?
**R:** Le strutture dispongono i membri in sequenza con possibile riempimento per l'allineamento. Le unioni si sovrappongono a tutti i membri nella stessa posizione di memoria: la dimensione è uguale al membro più grande. I bitfield racchiudono più valori in un singolo numero intero. Le strutture sono per dati eterogenei, unioni per il type-punning o per risparmiare spazio quando è attivo un solo campo e bitfield per l'archiviazione di flag compatti.
```c
// Struct — sequential layout with padding
struct Point {
    double x;  // offset 0, 8 bytes
    double y;  // offset 8, 8 bytes
};               // sizeof = 16

// Union — overlapping storage
union Value {
    int    i;
    float  f;
    char   s[8];
};               // sizeof = 8 (largest member)

// Tagged union — safe union usage
typedef enum { TYPE_INT, TYPE_FLOAT, TYPE_STRING } ValueType;

struct TaggedValue {
    ValueType type;
    union {
        int   i;
        float f;
        char  s[32];
    } data;
};

// Bitfields — pack flags into minimal space
struct Flags {
    unsigned int read    : 1;  // 1 bit
    unsigned int write   : 1;
    unsigned int execute : 1;
    unsigned int sticky  : 1;
    unsigned int reserved : 4;  // 4 bits padding
};  // Total: 1 byte instead of 4 ints
```

### D5: Cosa sono i puntatori a funzione e quando dovrei usarli?
**R:** I puntatori a funzione memorizzano l'indirizzo di una funzione e abilitano callback, polimorfismo e architetture di plug-in. Sono il fondamento dell'approccio del C alle funzioni di ordine superiore (come`qsort`,`bsearch`). Dichiarali con la sintassi:`return_type (*name)(parameter_types)`.
```c
// Function pointer declaration
int (*operation)(int, int);

int add(int a, int b) { return a + b; }
int mul(int a, int b) { return a * b; }

operation = add;
printf("%d\n", operation(3, 4));  // 7
operation = mul;
printf("%d\n", operation(3, 4));  // 12

// Callback pattern — qsort
int compare_ints(const void *a, const void *b) {
    int ia = *(const int *)a;
    int ib = *(const int *)b;
    return (ia > ib) - (ia < ib);
}

int arr[] = {5, 2, 8, 1, 9, 3};
qsort(arr, 6, sizeof(int), compare_ints);
// arr is now {1, 2, 3, 5, 8, 9}

// Strategy pattern
struct Strategy {
    void (*init)(void);
    void (*process)(const char *data);
    void (*cleanup)(void);
};

void run_pipeline(const struct Strategy *s, const char *data) {
    s->init();
    s->process(data);
    s->cleanup();
}
```

---

## Risoluzione dei problemi basati sulla catena di pensiero
### Problema 1: implementare un array dinamico (vettoriale)
**Dichiarazione del problema:** Implementa un array dinamico in C che cresce automaticamente quando vengono aggiunti elementi, supporta l'aggiunta ammortizzata O(1) e fornisce una pulizia adeguata. Questo è l'equivalente C di C++`std::vector`.
**Passaggio 1: comprendere il problema:**
Un array dinamico necessita di: (1) un buffer allocato nell'heap, (2) tracciamento delle dimensioni (elementi utilizzati) e della capacità (slot allocati), (3) riallocazione quando le dimensioni raggiungono la capacità, (4) corretta pulizia della memoria. Il fattore di crescita di 2x fornisce l'appendice ammortizzata O(1).
**Passaggio 2: identificare l'approccio:**
- Utilizzare`malloc`per l'allocazione iniziale,`realloc`per la crescita.
- Memorizza puntatore dati, dimensione e capacità in una struttura.
- Crescere raddoppiando la capacità quando`size == capacity`.
- Fornire operazioni `push`, `pop`, `get`,`set`e `free`.
**Passaggio 3: implementa la soluzione:**
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int    *data;
    size_t  size;
    size_t  capacity;
} IntVec;

// Initialize with default capacity
void vec_init(IntVec *v, size_t initial_capacity) {
    v->data = malloc(initial_capacity * sizeof(int));
    if (!v->data) { perror("malloc"); exit(EXIT_FAILURE); }
    v->size = 0;
    v->capacity = initial_capacity;
}

// Ensure capacity for at least one more element
static void vec_grow(IntVec *v) {
    if (v->size < v->capacity) return;
    size_t new_cap = v->capacity * 2;
    int *new_data = realloc(v->data, new_cap * sizeof(int));
    if (!new_data) { perror("realloc"); exit(EXIT_FAILURE); }
    v->data = new_data;
    v->capacity = new_cap;
}

// Append element — O(1) amortized
void vec_push(IntVec *v, int value) {
    vec_grow(v);
    v->data[v->size++] = value;
}

// Remove last element — O(1)
int vec_pop(IntVec *v) {
    if (v->size == 0) { fprintf(stderr, "pop from empty vector\n"); exit(EXIT_FAILURE); }
    return v->data[--v->size];
}

// Access element
int vec_get(const IntVec *v, size_t index) {
    if (index >= v->size) { fprintf(stderr, "index %zu out of bounds (size %zu)\n", index, v->size); exit(EXIT_FAILURE); }
    return v->data[index];
}

// Free all memory
void vec_free(IntVec *v) {
    free(v->data);
    v->data = NULL;
    v->size = v->capacity = 0;
}

// Usage
int main(void) {
    IntVec v;
    vec_init(&v, 4);

    for (int i = 0; i < 100; i++) {
        vec_push(&v, i * i);
    }

    printf("Size: %zu, Capacity: %zu\n", v.size, v.capacity);
    printf("Last: %d\n", vec_get(&v, v.size - 1));  // 9801

    vec_free(&v);
    return 0;
}
```

**Passaggio 4: verifica e ottimizzazione:**
- Push O(1) ammortizzato: raddoppiare significa che ogni elemento viene copiato al massimo O(log n) volte in totale.
- Il controllo dei limiti in`vec_get`e`vec_pop`rileva tempestivamente gli errori: essenziale in C dove non esiste una rete di sicurezza di runtime.
- Memoria: dopo 100 spinte a partire dalla capacità 4, la capacità arriva a 128 (4→8→16→32→64→128).
- Produzione: utilizza`shrink_to_fit`(riallocazione alla dimensione esatta) al termine della crescita per recuperare la memoria inutilizzata.
### Problema 2: creare una semplice tabella hash
**Dichiarazione del problema:** Implementa una tabella hash con chiavi stringa e valori interi utilizzando concatenamenti separati per la risoluzione delle collisioni. Supporta operazioni di inserimento, ricerca ed eliminazione.
**Passaggio 1: comprendere il problema:**
Una tabella hash associa le chiavi agli indici dell'array tramite una funzione hash. Le collisioni (chiavi diverse mappate allo stesso indice) vengono risolte con concatenamenti separati: ogni bucket è un elenco collegato di voci. Abbiamo bisogno di: funzione hash, inserimento, ricerca, eliminazione e pulizia.
**Passaggio 2: identificare l'approccio:**
- Utilizzare l'hash FNV-1a per una buona distribuzione delle chiavi delle stringhe.
- Matrice di puntatori a bucket (teste di elenchi collegati).
- Monitoraggio del fattore di carico; ridimensionare quando il fattore di carico supera la soglia.
- Tutte le operazioni sono O(1) media, O(n) caso peggiore.
**Passaggio 3: implementa la soluzione:**
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INITIAL_BUCKETS 64
#define LOAD_FACTOR_THRESHOLD 0.75

typedef struct Entry {
    char *key;
    int   value;
    struct Entry *next;
} Entry;

typedef struct {
    Entry  **buckets;
    size_t   num_buckets;
    size_t   size;
} HashMap;

// FNV-1a hash function
static unsigned long hash(const char *key) {
    unsigned long h = 14695981039346656037ULL;
    while (*key) {
        h ^= (unsigned char)*key++;
        h *= 1099511628211ULL;
    }
    return h;
}

void hashmap_init(HashMap *m) {
    m->num_buckets = INITIAL_BUCKETS;
    m->buckets = calloc(m->num_buckets, sizeof(Entry *));
    m->size = 0;
}

// Insert or update
void hashmap_put(HashMap *m, const char *key, int value) {
    size_t idx = hash(key) % m->num_buckets;

    // Check if key already exists
    for (Entry *e = m->buckets[idx]; e; e = e->next) {
        if (strcmp(e->key, key) == 0) {
            e->value = value;
            return;
        }
    }

    // New entry — prepend to bucket
    Entry *entry = malloc(sizeof(Entry));
    entry->key = strdup(key);
    entry->value = value;
    entry->next = m->buckets[idx];
    m->buckets[idx] = entry;
    m->size++;
}

// Lookup — returns 1 if found, 0 if not
int hashmap_get(const HashMap *m, const char *key, int *out_value) {
    size_t idx = hash(key) % m->num_buckets;
    for (Entry *e = m->buckets[idx]; e; e = e->next) {
        if (strcmp(e->key, key) == 0) {
            *out_value = e->value;
            return 1;
        }
    }
    return 0;
}

// Delete — returns 1 if removed, 0 if not found
int hashmap_remove(HashMap *m, const char *key) {
    size_t idx = hash(key) % m->num_buckets;
    Entry **pp = &m->buckets[idx];

    while (*pp) {
        if (strcmp((*pp)->key, key) == 0) {
            Entry *to_free = *pp;
            *pp = to_free->next;
            free(to_free->key);
            free(to_free);
            m->size--;
            return 1;
        }
        pp = &(*pp)->next;
    }
    return 0;
}

// Cleanup
void hashmap_free(HashMap *m) {
    for (size_t i = 0; i < m->num_buckets; i++) {
        Entry *e = m->buckets[i];
        while (e) {
            Entry *next = e->next;
            free(e->key);
            free(e);
            e = next;
        }
    }
    free(m->buckets);
    m->buckets = NULL;
    m->size = m->num_buckets = 0;
}

// Usage
int main(void) {
    HashMap m;
    hashmap_init(&m);

    hashmap_put(&m, "alice", 95);
    hashmap_put(&m, "bob", 87);
    hashmap_put(&m, "charlie", 92);

    int score;
    if (hashmap_get(&m, "alice", &score)) {
        printf("Alice: %d\n", score);  // Alice: 95
    }

    hashmap_remove(&m, "bob");
    hashmap_free(&m);
    return 0;
}
```

**Passaggio 4: verifica e ottimizzazione:**
- O(1) medio per inserimento/ricerca/eliminazione con una buona funzione hash e un fattore di carico ragionevole.
- FNV-1a fornisce un'eccellente distribuzione per le chiavi stringa con un calcolo minimo.
- La tecnica puntatore a puntatore (`Entry **pp`) in`hashmap_remove`gestisce elegantemente sia l'eliminazione dell'inizio dell'elenco che quella della metà dell'elenco senza casi speciali.
- Produzione: aggiungi il rehashing quando il fattore di carico supera la soglia. Utilizzare l'indirizzamento aperto (sondaggio lineare) per migliori prestazioni della cache.
### Problema 3: implementare un Ring Buffer per produttore-consumatore
**Dichiarazione del problema:** Implementare un buffer ad anello monoproduttore e singolo consumatore senza blocchi in C per la comunicazione inter-thread ad alte prestazioni senza allocazione dinamica durante il funzionamento.
**Passaggio 1: comprendere il problema:**
Un buffer ad anello (buffer circolare) utilizza un array di dimensione fissa con indici di lettura e scrittura. Quando il buffer è pieno, il writer si blocca o sovrascrive. Per SPSC (singolo produttore e singolo consumatore), possiamo utilizzare operazioni atomiche invece di blocchi per il massimo rendimento.
**Passaggio 2: identificare l'approccio:**
- Array di dimensione fissa allocato una volta al momento dell'inizializzazione.
-`head`(leggi posizione) e`tail`(scrivi posizione) come indici atomici.
- Il produttore anticipa`tail`; i consumatori avanzano`head`.
- Il buffer è vuoto quando`head == tail`; pieno quando`(tail + 1) % capacity == head`.
- Utilizzare gli atomi C11 con l'ordinamento della memoria appropriato.
**Passaggio 3: implementa la soluzione:**
```c
#include <stdio.h>
#include <stdatomic.h>
#include <stdlib.h>
#include <string.h>
#include <threads.h>

typedef struct {
    int              *buffer;
    size_t            capacity;  // Must be power of 2
    atomic_size_t     head;      // Consumer reads from here
    atomic_size_t     tail;      // Producer writes to here
} RingBuffer;

void ring_init(RingBuffer *rb, size_t capacity) {
    // Round up to power of 2 for efficient modulo
    size_t cap = 1;
    while (cap < capacity) cap <<= 1;
    rb->buffer = malloc(cap * sizeof(int));
    rb->capacity = cap;
    atomic_store(&rb->head, 0);
    atomic_store(&rb->tail, 0);
}

// Producer: try to push an item. Returns 1 on success, 0 if full.
int ring_push(RingBuffer *rb, int value) {
    size_t tail = atomic_load_explicit(&rb->tail, memory_order_relaxed);
    size_t next_tail = (tail + 1) & (rb->capacity - 1);  // Fast modulo

    if (next_tail == atomic_load_explicit(&rb->head, memory_order_acquire)) {
        return 0;  // Buffer full
    }

    rb->buffer[tail] = value;
    atomic_store_explicit(&rb->tail, next_tail, memory_order_release);
    return 1;
}

// Consumer: try to pop an item. Returns 1 on success, 0 if empty.
int ring_pop(RingBuffer *rb, int *out) {
    size_t head = atomic_load_explicit(&rb->head, memory_order_relaxed);

    if (head == atomic_load_explicit(&rb->tail, memory_order_acquire)) {
        return 0;  // Buffer empty
    }

    *out = rb->buffer[head];
    atomic_store_explicit(&rb->head, (head + 1) & (rb->capacity - 1),
                          memory_order_release);
    return 1;
}

void ring_free(RingBuffer *rb) {
    free(rb->buffer);
    rb->buffer = NULL;
}

// Producer thread
int producer_thread(void *arg) {
    RingBuffer *rb = arg;
    for (int i = 0; i < 1000000; i++) {
        while (!ring_push(rb, i)) {
            // Spin — buffer full
            thrd_yield();
        }
    }
    return 0;
}

// Consumer thread
int consumer_thread(void *arg) {
    RingBuffer *rb = arg;
    long long sum = 0;
    int count = 0;
    int val;
    while (count < 1000000) {
        if (ring_pop(rb, &val)) {
            sum += val;
            count++;
        } else {
            thrd_yield();  // Spin — buffer empty
        }
    }
    printf("Consumed %d items, sum = %lld\n", count, sum);
    return 0;
}
```

**Passaggio 4: verifica e ottimizzazione:**
- Senza lock: solo operazioni atomiche: nessun mutex, nessun cambio di contesto.
- Ordine della memoria:`release`in scrittura garantisce che i dati siano visibili prima dell'aggiornamento dell'indice; `acquire`in lettura garantisce la visualizzazione dei dati dopo aver letto l'indice.
- Capacità Power-of-2: abilita`& (capacity - 1)`invece di`% capacity`— molto più veloce.
- Throughput: miliardi di operazioni al secondo su hardware moderno.
- Produzione: aggiungi riempimento tra`head`e`tail`per evitare false condivisioni (ciascuno sulla propria linea di cache).
---

## Riepilogo
C è il fondamento dell'informatica moderna. Ti offre il massimo controllo sull'hardware con un sovraccarico di astrazione minimo. Il costo di tale controllo è la responsabilità: gestisci la memoria, controlli i limiti e gestisci tu stesso gli errori. Per la programmazione di sistemi, lo sviluppo integrato e ovunque i vincoli in termini di prestazioni e risorse siano importanti, C rimane ineguagliato. Per tutto il resto, i linguaggi di livello superiore basati sul C sono solitamente scelte più produttive.