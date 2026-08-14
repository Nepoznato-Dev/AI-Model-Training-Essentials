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
#سی
C یک زبان برنامه نویسی همه منظوره و رویه ای است که توسط دنیس ریچی در آزمایشگاه های بل بین سال های 1969 تا 1973 ایجاد شد. این زبان برای پیاده سازی سیستم عامل یونیکس طراحی شد و پس از 50 سال یکی از پرکاربردترین زبان های برنامه نویسی باقی مانده است. C دسترسی به حافظه سطح پایین، یک کتابخانه استاندارد حداقل، و یک نقشه برداری تمیز به دستورالعمل های ماشین را فراهم می کند - که آن را پایه ای می کند که اکثر محاسبات مدرن بر روی آن ساخته شده اند.
C زبان پشت سیستم‌های عامل (لینوکس، هسته ویندوز، macOS)، سیستم‌های جاسازی شده، موتورهای پایگاه داده (SQLite، PostgreSQL)، کامپایلرها (CPython پایتون، MRI روبی)، و تقریباً هر زمان اجرای زبان برنامه‌نویسی دیگری است. درک C یعنی درک اینکه کامپیوترها واقعا چگونه کار می کنند.
---

## چرا C مهم است
- **نزدیک به سخت افزار**: C از نزدیک به کد ماشین نگاشت می شود. هیچ زباله گردی، سربار زمان اجرا، هیچ تخصیص پنهانی وجود ندارد.
- **Ubiquity**: از میکروکنترلرها گرفته تا ابررایانه ها، C در همه جا اجرا می شود.
- **بنیاد محاسبات**: لینوکس، ویندوز، هسته های macOS، مفسر پایتون، SQLite، Git -- همه به زبان C نوشته شده اند.
- **عملکرد**: سرعت اجرای تقریباً بهینه با کنترل کامل بر چیدمان حافظه.
- **تأثیر**: نحو و مفاهیم C (اشاره‌گرها، آرایه‌ها، ساختارها، توابع) C++، Java، C#، JavaScript، Go، Rust و بیشتر زبان‌های بعدی را شکل دادند.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **مدیریت دستی حافظه** | بدون زباله جمع کن -- شما خودتان حافظه را اختصاص داده و آزاد می کنید | استفاده دقیق از malloc/رایگان؛ الگوهای RAII در C++ |
| **سرریز بافر** | بدون محدودیت در آرایه ها - نوشتن پایان بافر گذشته آسان | به جای strcpy از strncpy استفاده کنید. فعال کردن هشدارهای کامپایلر |
| **بدون OOP داخلی ** | فقط رویه ای -- بدون کلاس، وراثت یا روش | استفاده از structs + نشانگرهای تابع. یا به C++ | تغییر دهید
| **کتابخانه استاندارد محدود** | حداقل عملکرد داخلی | کتابخانه های شخص ثالث یا خودتان بنویسید |
| **رفتار نامشخص** | بسیاری از اشتباهات خوب جمع آوری می شوند اما به طور غیرقابل پیش بینی خراب می شوند | استفاده از ضد عفونی کننده، آنالایزر استاتیک |
---

## اصول نحو
### ساختار اساسی
هر برنامه C از`main()`شروع می شود. زبان کامپایل می شود -- کد منبع از طریق یک کامپایلر (GCC، Clang، MSVC) به کد ماشین تبدیل می شود.
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

### متغیرها و انواع
C به صورت ایستا تایپ می شود -- هر متغیر دارای یک نوع ثابت است که در زمان کامپایل شناخته می شود.
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

### اشاره گر
اشاره گرها قوی ترین و اشتباه ترین ویژگی C هستند. یک اشاره گر یک آدرس حافظه را نگه می دارد.
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

### کنترل جریان
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

### توابع و پشته
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

## چیدمان حافظه
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

| منطقه | آنچه آنجا می رود | طول عمر | چه کسی آن را مدیریت می کند |
|--------|---------------|---------|---------------|
| **پشته** | متغیرهای محلی، پارامترهای تابع | تا زمانی که تابع برگردد | کامپایلر (اتوماتیک) |
| **هپ** | تخصیص malloc/calloc | تا زمانی که تماس رایگان () | شما (راهنما) |
| **داده/BSS** | متغیرهای سراسری و استاتیک | کل طول عمر برنامه | کامپایلر (اتوماتیک) |
| **متن** | کد ماشین | کل طول عمر برنامه | فقط خواندنی |
---

## کتابخانه استاندارد
| سربرگ | هدف | توابع مشترک |
|--------|--------|-----------------|
| `<stdio.h>`| ورودی/خروجی | printf, scanf, fopen, fgets, fprintf |
| `<stdlib.h>`| خدمات عمومی | malloc, free, exit, atoi, rand, qsort |
| `<string.h>`| عملیات رشته | strlen، strcpy، strncpy، strcmp، memcpy |
| `<math.h>`| ریاضی | sin, cos, sqrt, pow, fabs, ceil, floor |
| `<ctype.h>`| طبقه بندی شخصیت | isalpha, isdigit, toupper, tolower |
| `<time.h>`| تاریخ و زمان | زمان، ساعت، زمان فاصله، زمان strftime |
| `<assert.h>`| اشکال زدایی اظهارات | اظهار (شرط) |
| `<errno.h>`| کدهای خطا | errno, perror, strerror |
---

## نحو و الگوهای پیشرفته
### ماکروهای پیش پردازنده
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

### تابع اشاره گر و تماس
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

### الگوهای مدیریت خطای سفارشی
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

## همزمانی و موازی
### رشته‌های POSIX (رشته‌ها)
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

### Mutex و Shared State
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

### C11 Atomics and Threads
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

## پیکربندی پروژه و سیستم ساخت
### ساختار پروژه
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

### خط لوله CI/CD (اقدامات GitHub)
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

## تست
### تست واحد با یک چارچوب ساده
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

## قابلیت همکاری
### فراخوانی C از پایتون (ctypes)
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

### تماس C از زبان های دیگر
| زبان | مکانیسم | مثال |
|----------|-----------|---------|
| پایتون | ctypes، cffi | `ctypes.CDLL("./lib.so")`|
| یاقوت | کمانچه | `Fiddle.dlopen("./lib.so")`|
| جاوا | JNI | `System.loadLibrary("mylib")`|
| C++ | خارجی "C" | `extern "C" void my_func();`|
| زنگ زدگی | خارجی "C" + FFI | `extern "C" { fn my_func(); }`|
---

## الگوهای طراحی
### اشاره گر مات (اصطلاح Pimpl به زبان C)
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

### جدول مجازی (OOP در C)
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

## عملکرد و بهینه سازی
### ابزارهای پروفایل
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

### تکنیک های بهینه سازی
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

## استقرار
### تالیف متقاطع
```bash
# Cross-compile for ARM (embedded)
arm-none-eabi-gcc -mcpu=cortex-m4 -o firmware.elf main.c

# Cross-compile for Windows from Linux
x86_64-w64-mingw32-gcc -o my_app.exe main.c

# Static linking (no shared library dependencies)
gcc -static -o my_app main.c
```

### استقرار داکر
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

## الگوها و اصطلاحات رایج
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

## تالیف و ابزار
```bash
gcc -Wall -Wextra -o myprogram myprogram.c      # Basic compile
gcc -g -Wall -o myprogram myprogram.c            # With debug symbols
gcc -O2 -Wall -o myprogram myprogram.c           # With optimisation
gcc -std=c17 -Wall -o myprogram myprogram.c      # Specific standard
make          # Runs the Makefile
make clean    # Removes build artifacts
```

| ابزار | هدف |
|------|---------|
| **GCC / Clang** | کامپایلر |
| **ساخت / CMake** | ساخت سیستم |
| **GDB** | دیباگر |
| **والگریند** | تشخیص خطای حافظه (نشت، دسترسی نامعتبر) |
| **AddressSanitizer** | بررسی حافظه زمان کامپایل |
| **cppcheck** | تجزیه و تحلیل استاتیک |
| **فرمت cang** | قالب بندی کد |
---

## چه زمانی از C استفاده کنیم
| سناریو | چرا C | جایگزین بهتر |
|----------|-------|-------------------|
| سیستم عامل | دسترسی مستقیم به سخت افزار، بدون سربار زمان اجرا | -- |
| سیستم های جاسازی شده / میکروکنترلر | حداقل ردپا، اجرا بر روی هر چیزی | زنگ برای ایمنی حیاتی تعبیه شده |
| موتورهای پایگاه داده | حداکثر عملکرد، کنترل حافظه کامل | -- |
| کامپایلر و مفسر | سریع، قابل حمل، قابل درک | C++ برای پروژه های کامپایلر بزرگتر |
| درایورهای دستگاه | مورد نیاز اکثر APIهای هسته سیستم عامل | -- |
| کتابخانه های حیاتی عملکرد | سرعت تقریبا بهینه | زنگ برای ایمنی تضمین شده حافظه |
| توسعه برنامه عمومی | کار دستی زیاد | پایتون، جاوا، برو، سی شارپ |
| توسعه وب | ابزار کاملا اشتباه | جاوا اسکریپت، برو، پایتون |
| علم داده / ML | هیچ اکوسیستمی برای این | پایتون، آر، جولیا |
---

## استانداردهای C
| استاندارد | سال | اضافات کلیدی |
|----------|------|--------------|
| C89/C90 | 1989/1990 | ANSI C اصلی -- هنوز خط پایه |
| C99 | 1999 | // نظرات، نوع bool، آرایه های با طول متغیر، inline، stdint.h |
| C11 | 2011 | عملیات اتمی، رشته ها، ساختارهای ناشناس، _Generic |
| C17 | 2018 | رفع اشکال و شفاف سازی (بدون ویژگی جدید) |
| C23 | 2024 | nullptr، typeof، constexpr، پیش پردازنده بهبود یافته |
اکثر کدهای تولیدی C11 یا C17 را هدف قرار می دهند. C23 امکانات مدرن را به ارمغان می آورد، اما پذیرش زمان می برد.
---

## پرسش و پاسخ مصنوعی
### Q1: تفاوت بین اشاره گر و آرایه در C چیست؟
**A:** آرایه ها و اشاره گرها به هم مرتبط هستند اما متمایز هستند. آرایه یک بلوک پیوسته از حافظه با اندازه ثابتی است که در زمان کامپایل شناخته شده است. اشاره گر متغیری است که آدرس حافظه را نگه می دارد. وقتی به توابع ارسال می شود، آرایه ها به اشاره گرها تحلیل می روند، اما`sizeof(array)`اندازه کل را نشان می دهد در حالی که`sizeof(pointer)`فقط اندازه اشاره گر (4 یا 8 بایت) را می دهد. نام آرایه ها مقادیر قابل تغییر نیستند - نمی توانید`arr++`را انجام دهید.
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

### Q2: چگونه حافظه را به درستی مدیریت کنم و از نشت جلوگیری کنم؟
**A:** هر`malloc`/`calloc`باید یک`free`مربوطه داشته باشد. اشتباهات رایج: فراموش کردن آزاد کردن (نشت)، دوبار آزاد کردن (رفتار تعریف نشده)، استفاده از حافظه پس از آزادسازی (استفاده پس از آزاد شدن)، و بررسی نکردن مقدار بازگشتی`malloc`(NULL در صورت خرابی). بهترین روش: در یک ماژول تخصیص داده و آزاد کنید، از الگوی "goto cleanup" برای مدیریت خطا استفاده کنید و همیشه نشانگرهای آزاد شده را روی NULL قرار دهید.
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

### Q3: بهترین روش ها برای مدیریت خطا در C چیست؟
**A:** C هیچ استثنایی ندارد. مدیریت خطا از مقادیر بازگشتی (کدهای خطا، نشانگرهای NULL، مقادیر منفی) استفاده می کند. الگوی استاندارد: توابع در صورت خرابی یک کد وضعیت یا NULL را برمی‌گردانند و`errno`را برای تماس‌های سیستمی تنظیم می‌کنند. برای پاکسازی منابع در مورد خطاها از الگوی "goto cleanup" استفاده کنید. همیشه مقادیر بازگشتی `malloc`،`fopen`و سایر توابع که ممکن است خراب شوند را بررسی کنید.
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

### Q4: ساختارها، اتحادها و فیلدهای بیتی در چیدمان حافظه چگونه متفاوت هستند؟
**A:** سازه ها اعضا را به صورت متوالی با بالشتک های احتمالی برای تراز قرار می دهند. اتحادیه ها همه اعضا را در یک مکان حافظه قرار می دهند - اندازه برابر با بزرگترین عضو است. فیلدهای بیتی چندین مقدار را در یک عدد صحیح بسته بندی می کنند. ساختارها برای داده‌های ناهمگن، اتحادیه‌ها برای تایپ کردن یا صرفه‌جویی در فضا زمانی که تنها یک فیلد فعال است، و فیلدهای بیت برای ذخیره‌سازی پرچم فشرده هستند.
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

### Q5: نشانگرهای تابع چیست و چه زمانی باید از آنها استفاده کنم؟
**الف:** نشانگرهای تابع آدرس یک تابع را ذخیره می کنند و بازخوانی، چند شکلی و معماری پلاگین را فعال می کنند. آنها پایه و اساس رویکرد C به توابع درجه بالاتر (مانند `qsort`، `bsearch`) هستند. آنها را با نحو اعلان کنید: `return_type (*name)(parameter_types)`.
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

## حل مسئله زنجیره ای از فکر
### مسئله 1: پیاده سازی یک آرایه پویا (بردار)
**بیانیه مشکل:** یک آرایه پویا در C پیاده سازی کنید که به طور خودکار با اضافه شدن عناصر رشد می کند، از ضمیمه استهلاک O(1) پشتیبانی می کند و پاکسازی مناسب را فراهم می کند. این معادل C C++`std::vector`است.
** مرحله 1 - مشکل را درک کنید:**
یک آرایه پویا به این موارد نیاز دارد: (1) یک بافر تخصیص داده شده از پشته، (2) ردیابی اندازه (عناصر استفاده شده) و ظرفیت (اسلات اختصاص داده شده)، (3) تخصیص مجدد زمانی که اندازه به ظرفیت برسد، (4) پاکسازی مناسب حافظه. ضریب رشد 2x به O(1) اضافه می شود.
** مرحله 2 - شناسایی رویکرد: **
- از`malloc`برای تخصیص اولیه و`realloc`برای رشد استفاده کنید.
- نشانگر داده، اندازه و ظرفیت را در یک ساختار ذخیره کنید.
- با دو برابر شدن ظرفیت در زمان`size == capacity`رشد کنید.
- عملیات `push`، `pop`، `get`، `set`، و`free`را ارائه دهید.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- فشار O(1) مستهلک شده: دو برابر شدن به این معنی است که هر عنصر حداکثر O(log n) برابر کل کپی می شود.
- بررسی مرزها در`vec_get`و`vec_pop`خطاها را زود تشخیص می دهد - در C که در آن شبکه ایمنی زمان اجرا وجود ندارد ضروری است.
- حافظه: پس از 100 فشار با شروع از ظرفیت 4، ظرفیت به 128 می رسد (4→8→16→32→64→128).
- تولید: از`shrink_to_fit`(realloc به اندازه دقیق) برای بازیابی حافظه استفاده نشده استفاده کنید.
### مسئله 2: یک جدول هش ساده بسازید
**بیانیه مشکل:** یک جدول هش با کلیدهای رشته و مقادیر صحیح با استفاده از زنجیره جداگانه برای تفکیک برخورد پیاده سازی کنید. پشتیبانی از عملیات درج، جستجو و حذف.
** مرحله 1 - مشکل را درک کنید:**
یک جدول هش کلیدها را برای آرایه کردن شاخص ها از طریق یک تابع درهم نگاشت می کند. برخوردها (کلیدهای مختلف که به یک شاخص نگاشت می‌شوند) با زنجیره‌بندی جداگانه حل می‌شوند: هر سطل یک لیست مرتبط از ورودی‌ها است. ما نیاز داریم: تابع هش، درج، جستجو، حذف و پاکسازی.
** مرحله 2 - شناسایی رویکرد: **
- از هش FNV-1a برای توزیع خوب کلیدهای رشته ای استفاده کنید.
- آرایه ای از نشانگرهای سطل (سرهای لیست مرتبط).
- ردیابی فاکتور بار؛ وقتی فاکتور بار از آستانه فراتر رفت، اندازه را تغییر دهید.
- همه عملیات O(1) متوسط، O(n) بدترین حالت هستند.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- میانگین O(1) برای درج/جستجو/حذف با یک تابع هش خوب و ضریب بار معقول.
- FNV-1a توزیع عالی را برای کلیدهای رشته ای با حداقل محاسبات فراهم می کند.
- تکنیک اشاره گر به اشاره گر (`Entry **pp`) در`hashmap_remove`به زیبایی حذف سرفصل و میان لیست را بدون موارد خاص مدیریت می کند.
- تولید: هنگامی که ضریب بار از آستانه فراتر رفت، هش مجدد را اضافه کنید. برای عملکرد بهتر کش از آدرس دهی باز (کاوش خطی) استفاده کنید.
### مشکل 3: یک بافر حلقه برای تولید کننده-مصرف کننده پیاده سازی کنید
**بیانیه مشکل:** برای ارتباط بین رشته ای با کارایی بالا بدون تخصیص دینامیک در حین کار، یک بافر حلقه تک تولید کننده تک مصرف کننده بدون قفل را در C اجرا کنید.
** مرحله 1 - مشکل را درک کنید:**
یک بافر حلقه (بافر دایره ای) از یک آرایه با اندازه ثابت با شاخص های خواندن و نوشتن استفاده می کند. هنگامی که بافر پر است، نویسنده مسدود یا بازنویسی می کند. برای SPSC (تک تولید کننده تک مصرف کننده)، می توانیم از عملیات اتمی به جای قفل برای حداکثر توان استفاده کنیم.
** مرحله 2 - شناسایی رویکرد: **
- آرایه با اندازه ثابت یک بار در زمان اولیه تخصیص داده می شود.
-`head`(موقعیت خواندن) و`tail`(موقعیت نوشتن) به عنوان شاخص های اتمی.
- پیشرفت های تولید کننده`tail`; پیشرفت های مصرف کننده `head`.
- زمانی که`head == tail`بافر خالی است. پر وقتی`(tail + 1) % capacity == head`.
- از اتم های C11 با ترتیب حافظه مناسب استفاده کنید.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- بدون قفل: فقط عملیات اتمی - بدون mutexes، بدون سوئیچ زمینه.
- مرتب سازی حافظه:`release`در نوشتن تضمین می کند که داده ها قبل از به روز رسانی فهرست قابل مشاهده هستند. `acquire`در خواندن تضمین می کند که ما داده ها را پس از خواندن ایندکس می بینیم.
- ظرفیت توان 2:`& (capacity - 1)`را به جای`% capacity`فعال می کند — بسیار سریعتر.
- توان عملیاتی: میلیاردها عملیات در ثانیه بر روی سخت افزار مدرن.
- تولید: برای جلوگیری از اشتراک گذاری نادرست (هر کدام در خط کش مخصوص به خود) بالشتک بین`head`و`tail`اضافه کنید.
---

## خلاصه
C پایه محاسبات مدرن است. حداکثر کنترل را بر روی سخت افزار با حداقل هزینه انتزاعی به شما می دهد. هزینه این کنترل مسئولیت است -- شما حافظه را مدیریت می کنید، محدوده ها را بررسی می کنید و خطاها را خودتان مدیریت می کنید. برای برنامه نویسی سیستم، توسعه تعبیه شده، و هر جایی که عملکرد و محدودیت منابع مهم باشد، C بی بدیل باقی می ماند. برای هر چیز دیگری، زبان های سطح بالاتر ساخته شده در بالای C معمولاً انتخاب های سازنده تری هستند.