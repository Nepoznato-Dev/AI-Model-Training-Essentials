---
# Metadata
title: "C"
description: "Comprehensive reference for the C programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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

# C
Ang C ay isang general-purpose, procedural programming language na nilikha ni Dennis Ritchie sa Bell Labs sa pagitan ng 1969 at 1973. Ito ay idinisenyo upang ipatupad ang Unix operating system, at ito ay nananatiling isa sa pinakamalawak na ginagamit na programming language pagkalipas ng 50 taon. Ang C ay nagbibigay ng mababang antas ng pag-access sa memorya, isang minimal na karaniwang library, at isang malinis na pagmamapa sa mga tagubilin sa makina -- ginagawa itong pundasyon kung saan itinayo ang karamihan sa modernong computing.
Ang C ay ang wika sa likod ng mga operating system (Linux, Windows kernel, macOS), naka-embed na system, database engine (SQLite, PostgreSQL), compiler (Python's CPython, Ruby's MRI), at halos lahat ng iba pang programming language runtime. Ang pag-unawa sa C ay pag-unawa kung paano gumagana ang mga computer.
---

## Bakit Mahalaga ang C
- **Malapit sa hardware**: Ang C ay malapit na nagmamapa sa machine code. Walang basurero, walang runtime overhead, walang nakatagong alokasyon.
- **Ubiquity**: Mula sa mga microcontroller hanggang sa mga supercomputer, tumatakbo ang C kahit saan.
- **Foundation ng computing**: Linux, Windows, macOS kernels, Python interpreter, SQLite, Git -- lahat ay nakasulat sa C.
- **Pagganap**: Malapit sa pinakamainam na bilis ng pagpapatupad na may ganap na kontrol sa layout ng memorya.
- **Impluwensiya**: Ang syntax at mga konsepto ng C (mga pointer, array, struct, function) na hugis C++, Java, C#, JavaScript, Go, Rust, at karamihan sa mga sumunod na wika.
## Ang mga Trade-off
| Limitasyon | Mga Detalye | Karaniwang Workaround |
|-----------|---------|-------------------|
| **Manwal na pamamahala ng memory** | Walang basurero -- ikaw mismo ang maglalaan at magbakante ng memorya | Maingat na paggamit ng malloc/libre; Mga pattern ng RAII sa C++ |
| **Umapaw ang buffer** | Walang hangganang pagsuri sa mga array -- madaling isulat ang mga nakalipas na buffer ends | Gumamit ng strncpy sa halip na strcpy; paganahin ang mga babala ng compiler |
| **Walang built-in na OOP** | Pamamaraan lamang -- walang mga klase, mana, o pamamaraan | Gumamit ng mga struct + function pointer; o lumipat sa C++ |
| **Limitadong karaniwang library** | Minimal na built-in na functionality | Mga aklatan ng third-party o sumulat ng sarili mong |
| **Hindi natukoy na gawi** | Maraming pagkakamali ang nag-compile ng maayos ngunit hindi nahuhulaang bumagsak | Gumamit ng mga sanitizer, static analyzer |
---

## Syntax Fundamentals
### Pangunahing Istruktura
Ang bawat C program ay nagsisimula sa`main()`. Ang wika ay pinagsama-sama -- ang source code ay nagiging machine code sa pamamagitan ng isang compiler (GCC, Clang, MSVC).
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

### Mga Variable at Uri
Ang C ay statically typed -- bawat variable ay may nakapirming uri na kilala sa oras ng compile.
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

### Mga pointer
Ang mga pointer ay ang pinaka-makapangyarihan at pinaka-hindi nauunawaang feature ng C. Ang isang pointer ay mayroong memory address.
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

### Kontrol na Daloy
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

### Mga Pag-andar at ang Stack
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

## Layout ng Memory
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

| Rehiyon | Ano ang Pupunta Doon | Habambuhay | Sino ang Namamahala Nito |
|--------|----------------|------------------------|----------------|
| **Stack** | Mga lokal na variable, mga parameter ng function | Hanggang sa bumalik ang function | Compiler (awtomatiko) |
| **Bunton** | malloc/calloc allocations | Hanggang sa tumawag ka ng free() | Ikaw (manual) |
| **Data/BSS** | Global at static na mga variable | Buong buhay ng programa | Compiler (awtomatiko) |
| **Text** | Code ng makina | Buong buhay ng programa | Read-only |
---

## Ang Standard Library
| Header | Layunin | Mga Karaniwang Paggana |
|--------|---------|----------------|
| `<stdio.h>`| Input/output | printf, scanf, fopen, fgets, fprintf |
| `<stdlib.h>`| Mga pangkalahatang kagamitan | malloc, libre, exit, atoi, rand, qsort |
| `<string.h>`| Mga pagpapatakbo ng string | strlen, strcpy, strncpy, strcmp, memcpy |
| `<math.h>`| Matematika | kasalanan, cos, sqrt, pow, fabs, ceil, floor |
| `<ctype.h>`| Pag-uuri ng karakter | isalpha, isdigit, toupper, tolower |
| `<time.h>`| Petsa at oras | oras, orasan, difftime, strftime |
| `<assert.h>`| Pag-debug ng mga pahayag | igiit(kondisyon) |
| `<errno.h>`| Mga error code | errno, perror, strerror |
---

## Advanced na Syntax at Mga Pattern
### Mga Macro ng Preprocessor
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

### Mga Function Pointer at Callback
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

### Custom na Mga Pattern ng Paghawak ng Error
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

## Concurrency at Paralelismo
### POSIX Thread (pthreads)
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

### Mutex at Shared State
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

### C11 Atomics at Thread
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

## Project Configuration at Build System
### Istraktura ng Proyekto
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

### CI/CD Pipeline (GitHub Actions)
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

## Pagsubok
### Unit Testing na may Simple Framework
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

## Interoperability
### Pagtawag sa C mula sa Python (ctypes)
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

### Tinatawagan si C mula sa Iba pang mga Wika
| Wika | Mekanismo | Halimbawa |
|----------|-----------|---------|
| Python | ctypes, cffi | `ctypes.CDLL("./lib.so")`|
| Ruby | Fiddle | `Fiddle.dlopen("./lib.so")`|
| Java | JNI | `System.loadLibrary("mylib")`|
| C++ | panlabas na "C" | `extern "C" void my_func();`|
| kalawang | panlabas na "C" + FFI | `extern "C" { fn my_func(); }`|
---

## Mga Pattern ng Disenyo
### Opaque Pointer (Pimpl Idiom sa C)
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

### Virtual Table (OOP sa C)
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

## Pagganap at Pag-optimize
### Mga Tool sa Pag-profile
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

### Mga Teknik sa Pag-optimize
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

## Deployment
### Cross-Compilation
```bash
# Cross-compile for ARM (embedded)
arm-none-eabi-gcc -mcpu=cortex-m4 -o firmware.elf main.c

# Cross-compile for Windows from Linux
x86_64-w64-mingw32-gcc -o my_app.exe main.c

# Static linking (no shared library dependencies)
gcc -static -o my_app main.c
```

### Docker Deployment
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

## Mga Karaniwang Pattern at Idiom
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

## Compilation at Tooling
```bash
gcc -Wall -Wextra -o myprogram myprogram.c      # Basic compile
gcc -g -Wall -o myprogram myprogram.c            # With debug symbols
gcc -O2 -Wall -o myprogram myprogram.c           # With optimisation
gcc -std=c17 -Wall -o myprogram myprogram.c      # Specific standard
make          # Runs the Makefile
make clean    # Removes build artifacts
```

| Tool | Layunin |
|------|---------|
| **GCC / Clang** | Mga Compiler |
| **Gumawa / CMake** | Bumuo ng mga system |
| **GDB** | Debugger |
| **Valgrind** | Memory error detector (leak, invalid access) |
| **AddressSanitizer** | Pagsusuri ng memorya ng oras ng pag-compile |
| **cppcheck** | Static na pagsusuri |
| **clang-format** | Pag-format ng code |
---

## Kailan Gamitin ang C
| Sitwasyon | Bakit C | Mas mahusay na Alternatibo |
|----------|-------|-------------------|
| Mga operating system | Direktang pag-access sa hardware, walang runtime overhead | -- |
| Mga naka-embed na system / microcontroller | Minimal footprint, tumatakbo sa kahit ano | kalawang para sa kaligtasan-kritikal na naka-embed |
| Mga makina ng database | Pinakamataas na pagganap, buong kontrol sa memorya | -- |
| Mga compiler at interpreter | Mabilis, portable, mahusay na nauunawaan | C++ para sa mas malalaking proyekto ng compiler |
| Mga driver ng device | Kinakailangan ng karamihan sa mga OS kernel API | -- |
| Mga aklatan na kritikal sa pagganap | Malapit sa pinakamainam na bilis | kalawang para sa garantisadong kaligtasan ng memorya |
| Pangkalahatang pag-unlad ng application | Masyadong maraming manu-manong trabaho | Python, Java, Go, C# |
| Pagbuo ng web | Ganap na maling tool | JavaScript, Go, Python |
| Data science / ML | Walang ecosystem para dito | Python, R, Julia |
---

## C Pamantayan
| Pamantayan | Taon | Mga Pangunahing Pagdaragdag |
|----------|------|--------------|
| C89/C90 | 1989/1990 | Ang orihinal na ANSI C -- pa rin ang baseline |
| C99 | 1999 | // komento, uri ng bool, variable-length array, inline, stdint.h |
| C11 | 2011 | Atomic operations, threads, anonymous structs, _Generic |
| C17 | 2018 | Mga pag-aayos ng bug at paglilinaw (walang mga bagong feature) |
| C23 | 2024 | nullptr, typeof, constexpr, pinahusay na preprocessor |
Karamihan sa production code ay nagta-target ng C11 o C17. Ang C23 ay nagdadala ng mga modernong kaginhawahan ngunit ang pag-aampon ay nangangailangan ng oras.
---

## Synthetic na Q&A
### Q1: Ano ang pagkakaiba sa pagitan ng mga pointer at array sa C?
**A:** Ang mga array at pointer ay magkakaugnay ngunit naiiba. Ang array ay isang magkadikit na bloke ng memorya na may nakapirming laki na kilala sa oras ng pag-compile. Ang pointer ay isang variable na mayroong memory address. Ang mga array ay nabubulok sa mga pointer kapag ipinasa sa mga function, ngunit ang`sizeof(array)`ay nagbibigay ng kabuuang laki habang ang`sizeof(pointer)`ay nagbibigay lamang ng pointer size (4 o 8 bytes). Ang mga pangalan ng array ay hindi nababago lvalues ​​— hindi mo magagawa ang`arr++`.
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

### Q2: Paano ko mapapamahalaan nang maayos ang memorya at maiiwasan ang mga pagtagas?
**A:** Ang bawat`malloc`/`calloc`ay dapat may katumbas na`free`. Mga karaniwang pagkakamali: nakakalimutang magbakante (leak), dalawang beses na nagpapalaya (hindi natukoy na pag-uugali), gumagamit ng memorya pagkatapos ng paglaya (use-after-free), at hindi nagsuri ng`malloc`return value (NULL on failure). Pinakamahusay na kasanayan: maglaan at libre sa parehong module, gamitin ang pattern na "goto cleanup" para sa paghawak ng error, at palaging itakda ang mga freed pointer sa NULL.
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

### Q3: Ano ang mga pinakamahusay na kasanayan para sa paghawak ng error sa C?
**A:** Walang exception si C. Gumagamit ang paghawak ng error ng mga return value (mga error code, NULL pointer, negatibong value). Ang karaniwang pattern: ang mga function ay nagbabalik ng status code o NULL kapag nabigo, at itinakda ang`errno`para sa mga system call. Gamitin ang pattern na "goto cleanup" para sa paglilinis ng mapagkukunan sa mga error. Palaging suriin ang mga return value ng`malloc`,`fopen`, at iba pang function na maaaring mabigo.
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

### Q4: Paano naiiba ang mga istruktura, unyon, at bitfield sa layout ng memorya?
**A:** Ang mga istruktura ay naglatag ng mga miyembro nang sunud-sunod na may posibleng padding para sa pagkakahanay. Ang mga unyon ay nag-overlay sa lahat ng miyembro sa parehong lokasyon ng memorya — ang laki ay katumbas ng pinakamalaking miyembro. Ang mga Bitfield ay nag-pack ng maraming mga halaga sa isang solong integer. Ang mga istruktura ay para sa heterogenous na data, mga unyon para sa type-punning o pagtitipid ng espasyo kapag isang field lang ang aktibo, at mga bitfield para sa compact na storage ng flag.
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

### Q5: Ano ang mga function pointer, at kailan ko dapat gamitin ang mga ito?
**A:** Ang mga function pointer ay nag-iimbak ng address ng isang function at pinapagana ang mga callback, polymorphism, at mga arkitektura ng plugin. Ang mga ito ang pundasyon ng diskarte ng C sa mga function na mas mataas ang pagkakasunud-sunod (tulad ng`qsort`,`bsearch`). Ipahayag ang mga ito gamit ang syntax:`return_type (*name)(parameter_types)`.
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

## Paglutas ng Problema ng Chain-of-Thought
### Problema 1: Magpatupad ng Dynamic Array (Vector)
**Problem Statement:** Magpatupad ng dynamic na array sa C na awtomatikong lumalaki kapag nagdagdag ng mga elemento, sumusuporta sa O(1) amortized na append, at nagbibigay ng wastong paglilinis. Ito ang katumbas ng C ng C++`std::vector`.
**Hakbang 1 — Unawain ang Problema:**
Ang isang dynamic na array ay nangangailangan ng: (1) isang heap-allocated buffer, (2) tracking ng laki (ginamit na mga elemento) at kapasidad (allocated slots), (3) relocation kapag ang laki ay umabot sa kapasidad, (4) wastong memory cleanup. Ang Growth Factor na 2x ay nagbibigay ng O(1) amortized append.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Gamitin ang`malloc`para sa paunang alokasyon,`realloc`para sa paglago.
- Mag-imbak ng data pointer, laki, at kapasidad sa isang struct.
- Palakihin sa pamamagitan ng pagdodoble ng kapasidad kapag`size == capacity`.
- Magbigay ng mga operasyong`push`,`pop`,`get`,`set`, at `free`.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Amortized O(1) push: ang pagdodoble ay nangangahulugan na ang bawat elemento ay kinokopya nang hindi hihigit sa O(log n) beses sa kabuuan.
- Ang bounds checking sa`vec_get`at`vec_pop`ay maagang nakakakuha ng mga error — mahalaga sa C kung saan walang runtime safety net.
- Memorya: pagkatapos ng 100 na pagtulak simula sa kapasidad 4, ang kapasidad ay umabot sa 128 (4→8→16→32→64→128).
- Produksyon: gumamit ng`shrink_to_fit`(realloc sa eksaktong sukat) kapag tapos na sa paglaki upang mabawi ang hindi nagamit na memorya.
### Problema 2: Bumuo ng Simple Hash Table
**Problem Statement:** Magpatupad ng hash table na may mga string key at integer value gamit ang hiwalay na chaining para sa collision resolution. Suportahan ang pagpasok, paghahanap, at pagtanggal ng mga operasyon.
**Hakbang 1 — Unawain ang Problema:**
Ang hash table ay nagmamapa ng mga susi sa array index sa pamamagitan ng hash function. Ang mga banggaan (iba't ibang key na pagmamapa sa parehong index) ay nireresolba sa hiwalay na pag-chain: ang bawat bucket ay isang naka-link na listahan ng mga entry. Kailangan namin ng: hash function, insert, lookup, delete, at cleanup.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Gumamit ng FNV-1a hash para sa mahusay na pamamahagi ng mga string key.
- Array ng mga bucket pointer (naka-link na mga ulo ng listahan).
- Pagsubaybay sa salik ng pag-load; baguhin ang laki kapag lumampas ang load factor sa threshold.
- Lahat ng mga operasyon ay O(1) average, O(n) pinakamasama kaso.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Average na O(1) para sa insert/lookup/delete na may magandang hash function at makatwirang load factor.
- Nagbibigay ang FNV-1a ng mahusay na pamamahagi para sa mga string key na may kaunting pagkalkula.
- Ang pointer-to-pointer technique (`Entry **pp`) sa`hashmap_remove`ay eleganteng pinangangasiwaan ang head-of-list at mid-list na pagtanggal nang walang mga espesyal na kaso.
- Produksyon: magdagdag ng rehashing kapag lumampas ang load factor sa threshold. Gumamit ng open addressing (linear probing) para sa mas mahusay na pagganap ng cache.
### Problema 3: Magpatupad ng Ring Buffer para sa Producer-Consumer
**Pahayag ng Problema:** Magpatupad ng walang lock na single-producer single-consumer ring buffer sa C para sa mataas na pagganap ng inter-thread na komunikasyon nang walang dynamic na alokasyon sa panahon ng operasyon.
**Hakbang 1 — Unawain ang Problema:**
Gumagamit ang ring buffer (circular buffer) ng fixed-size na array na may mga indeks ng read at write. Kapag puno na ang buffer, bina-block o ino-overwrite ng writer. Para sa SPSC (single-producer single-consumer), maaari naming gamitin ang atomic operations sa halip na mga lock para sa maximum throughput.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Fixed-size array na inilalaan nang isang beses sa pagsisimula.
-`head`(read position) at`tail`(write position) bilang atomic index.
- Producer advances`tail`; sumusulong ang mamimili`head`.
- Walang laman ang buffer kapag`head == tail`; puno kapag`(tail + 1) % capacity == head`.
- Gumamit ng C11 atomics na may naaangkop na pag-order ng memorya.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Lock-free: atomic operations lang — walang mutex, walang context switch.
- Pag-order ng memorya: Tinitiyak ng`release`sa pagsulat na ang data ay makikita bago ang pag-update ng index;  Tinitiyak ng`acquire`na binasa na makikita natin ang data pagkatapos basahin ang index.
- Power-of-2 na kapasidad: pinapagana ang`& (capacity - 1)`sa halip na`% capacity`— mas mabilis.
- Throughput: bilyun-bilyong operasyon bawat segundo sa modernong hardware.
- Produksyon: magdagdag ng padding sa pagitan ng`head`at`tail`upang maiwasan ang maling pagbabahagi (bawat isa ay nasa sarili nitong linya ng cache).
---

## Buod
Ang C ay ang pundasyon ng modernong computing. Nagbibigay ito sa iyo ng maximum na kontrol sa hardware na may kaunting abstraction overhead. Ang halaga ng kontrol na iyon ay pananagutan -- pinamamahalaan mo ang memorya, sinusuri ang mga hangganan, at ikaw mismo ang humahawak ng mga error. Para sa programming ng mga system, naka-embed na pag-unlad, at kahit saan mahalaga ang pagganap at mga hadlang sa mapagkukunan, nananatiling walang kaparis ang C. Para sa lahat ng iba pa, ang mga mas mataas na antas ng wika na binuo sa itaas ng C ay karaniwang mas produktibong mga pagpipilian.