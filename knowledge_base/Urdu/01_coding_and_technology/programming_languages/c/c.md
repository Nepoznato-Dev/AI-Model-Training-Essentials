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
#C
C ایک عام مقصد کی پروگرامنگ زبان ہے جسے ڈینس رچی نے بیل لیبز میں 1969 اور 1973 کے درمیان تخلیق کیا تھا۔ اسے یونکس آپریٹنگ سسٹم کو نافذ کرنے کے لیے ڈیزائن کیا گیا تھا، اور یہ 50 سال بعد بھی سب سے زیادہ استعمال ہونے والی پروگرامنگ زبانوں میں سے ایک ہے۔ C نچلی سطح کی میموری تک رسائی، ایک کم سے کم معیاری لائبریری، اور مشین کی ہدایات کے لیے ایک صاف نقشہ سازی فراہم کرتا ہے -- اسے وہ بنیاد بناتا ہے جس پر جدید ترین کمپیوٹنگ بنائی گئی ہے۔
C آپریٹنگ سسٹمز (Linux، Windows kernel، macOS)، ایمبیڈڈ سسٹمز، ڈیٹا بیس انجن (SQLite، PostgreSQL)، کمپائلرز (Python's CPython، Ruby's MRI)، اور عملی طور پر ہر دوسری پروگرامنگ لینگویج کے رن ٹائم کے پیچھے زبان ہے۔ سی کو سمجھنا یہ سمجھنا ہے کہ کمپیوٹر اصل میں کیسے کام کرتے ہیں۔
---

## کیوں C اہمیت رکھتا ہے۔
- **ہارڈ ویئر سے قربت**: C نقشے مشین کوڈ کے قریب ہے۔ کوئی کوڑا اٹھانے والا نہیں ہے، کوئی رن ٹائم اوور ہیڈ نہیں، کوئی پوشیدہ مختص نہیں ہے۔
- **ہر جگہ**: مائیکرو کنٹرولرز سے لے کر سپر کمپیوٹرز تک، C ہر جگہ چلتا ہے۔
- **کمپیوٹنگ کی بنیاد**: لینکس، ونڈوز، میک او ایس کرنل، پائتھون انٹرپریٹر، ایس کیو ایلائٹ، گٹ -- سبھی سی میں لکھے گئے ہیں۔
- **کارکردگی**: میموری لے آؤٹ پر مکمل کنٹرول کے ساتھ قریب ترین عملدرآمد کی رفتار۔
- **اثر**: C کے نحو اور تصورات (پوائنٹرز، اری، سٹرکٹس، فنکشنز) کی شکل میں C++، Java، C#، JavaScript، Go، Rust، اور اس کے بعد آنے والی زیادہ تر زبانیں۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **دستی میموری کا انتظام** | کوئی کوڑا اٹھانے والا نہیں -- آپ خود مختص اور مفت میموری | malloc/free کا احتیاط سے استعمال؛ C++ میں RAII پیٹرن |
| **بفر اوور فلو** | صفوں پر کوئی حد نہیں ہے -- ماضی کے بفر کے اختتام کو لکھنے میں آسان | strcpy کے بجائے strncpy استعمال کریں؛ کمپائلر وارننگ کو فعال کریں |
| **کوئی بلٹ ان OOP** | صرف طریقہ کار -- کوئی کلاس، وراثت، یا طریقے نہیں | structs + فنکشن پوائنٹر استعمال کریں؛ یا C++ پر سوئچ کریں |
| **محدود معیاری لائبریری** | کم سے کم بلٹ ان فعالیت | تیسری پارٹی کی لائبریریاں یا خود لکھیں |
| **غیر متعینہ رویہ** | بہت سی غلطیاں ٹھیک مرتب کرتی ہیں لیکن غیر متوقع طور پر کریش ہوجاتی ہیں۔ سینیٹائزر، سٹیٹک اینالائزر استعمال کریں۔
---

## نحوی بنیادی باتیں
### بنیادی ڈھانچہ
ہر C پروگرام`main()`سے شروع ہوتا ہے۔ زبان مرتب کی گئی ہے -- سورس کوڈ ایک کمپائلر (GCC، Clang، MSVC) کے ذریعے مشین کوڈ بن جاتا ہے۔
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

### متغیرات اور اقسام
C کو مستحکم طور پر ٹائپ کیا جاتا ہے -- ہر متغیر کی ایک مقررہ قسم ہوتی ہے جو مرتب وقت پر معلوم ہوتی ہے۔
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

### پوائنٹرز
پوائنٹرز C کی سب سے طاقتور اور سب سے زیادہ غلط فہمی والی خصوصیت ہیں۔ ایک پوائنٹر میں میموری ایڈریس ہوتا ہے۔
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

### کنٹرول فلو
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

### افعال اور اسٹیک
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

## میموری لے آؤٹ
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

| علاقہ | وہاں کیا جاتا ہے | زندگی بھر | اس کا انتظام کون کرتا ہے |
|---------|----------------|-------------------------|----------------|
| **اسٹیک** | مقامی متغیرات، فنکشن پیرامیٹرز | فنکشن واپس آنے تک | مرتب کرنے والا (خودکار) |
| **ڈھیر** | malloc/calloc مختص | جب تک آپ مفت کال کریں () | آپ (دستی) |
| **ڈیٹا/BSS** | عالمی اور جامد متغیرات | پورا پروگرام لائف ٹائم | مرتب کرنے والا (خودکار) |
| **متن** | مشین کوڈ | پورا پروگرام لائف ٹائم | صرف پڑھنے کے لیے |
---

## معیاری لائبریری
| ہیڈر | مقصد | عام افعال |
|---------|---------|------|
| `<stdio.h>`| ان پٹ/آؤٹ پٹ | printf, scanf, fopen, fgets, fprintf |
| `<stdlib.h>`| عام افادیت | malloc, free, exit, atoi, rand, qsort |
| `<string.h>`| سٹرنگ آپریشنز | strlen, strcpy, strncpy, strcmp, memcpy |
| `<math.h>`| ریاضی | sin, cos, sqrt, pow, fabs, ceil, floor |
| `<ctype.h>`| کردار کی درجہ بندی | isalpha, isdigit, toupper, tolower |
| `<time.h>`| تاریخ اور وقت | وقت، گھڑی، فرق کا وقت، strftime |
| `<assert.h>`| ڈیبگنگ دعوے | assert(شرط) |
| `<errno.h>`| ایرر کوڈز | errno, perr, strerror |
---

## اعلی درجے کی نحو اور نمونے۔
### پری پروسیسر میکرو
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

### فنکشن پوائنٹرز اور کال بیکس
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

### اپنی مرضی کے مطابق خرابی کو سنبھالنے کے پیٹرنز
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

## ہم آہنگی اور ہم آہنگی
### POSIX تھریڈز (pthreads)
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

### Mutex اور مشترکہ ریاست
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

### C11 ایٹمکس اور تھریڈز
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### پروجیکٹ کا ڈھانچہ
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

### میک فائل
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

### CI/CD پائپ لائن (GitHub ایکشنز)
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

## ٹیسٹنگ
### ایک سادہ فریم ورک کے ساتھ یونٹ ٹیسٹنگ
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

## انٹرآپریبلٹی
### ازگر سے C کال کرنا (ٹائپس)
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

### دوسری زبانوں سے C کال کرنا
| زبان | میکانزم | مثال |
|------------|------------|---------|
| ازگر | ctypes, cffi | `ctypes.CDLL("./lib.so")`|
| روبی | فڈل | `Fiddle.dlopen("./lib.so")`|
| جاوا | JNI | `System.loadLibrary("mylib")`|
| C++ | extern "C" | `extern "C" void my_func();`|
| مورچا | extern "C" + FFI | `extern "C" { fn my_func(); }`|
---

## ڈیزائن پیٹرن
### مبہم پوائنٹر (Pimpl محاورہ C میں)
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

### ورچوئل ٹیبل (C میں OOP)
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

## کارکردگی اور اصلاح
### پروفائلنگ ٹولز
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

### اصلاح کی تکنیک
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

## تعیناتی۔
### کراس تالیف
```bash
# Cross-compile for ARM (embedded)
arm-none-eabi-gcc -mcpu=cortex-m4 -o firmware.elf main.c

# Cross-compile for Windows from Linux
x86_64-w64-mingw32-gcc -o my_app.exe main.c

# Static linking (no shared library dependencies)
gcc -static -o my_app main.c
```

### ڈاکر کی تعیناتی۔
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

## مشترکہ نمونے اور محاورے۔
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

## تالیف اور ٹولنگ
```bash
gcc -Wall -Wextra -o myprogram myprogram.c      # Basic compile
gcc -g -Wall -o myprogram myprogram.c            # With debug symbols
gcc -O2 -Wall -o myprogram myprogram.c           # With optimisation
gcc -std=c17 -Wall -o myprogram myprogram.c      # Specific standard
make          # Runs the Makefile
make clean    # Removes build artifacts
```

| ٹول | مقصد |
|------|---------|
| **GCC / بجنا** | مرتب کرنے والے |
| **میک / سی میک** | سسٹمز بنائیں |
| **GDB** | ڈیبگر |
| **والگرینڈ** | میموری کی خرابی کا پتہ لگانے والا (لیک، غلط رسائی) |
| **ایڈریس سینیٹائزر** | کمپائل ٹائم میموری چیکنگ |
| **سی پی پی چیک** | جامد تجزیہ |
| **کلنگ فارمیٹ** | کوڈ فارمیٹنگ |
---

## سی کب استعمال کریں۔
| منظر نامہ | کیوں C | بہتر متبادل |
|------------|---------|-------------------|
| آپریٹنگ سسٹمز | براہ راست ہارڈ ویئر تک رسائی، کوئی رن ٹائم اوور ہیڈ نہیں | -- |
| ایمبیڈڈ سسٹم / مائیکرو کنٹرولرز | کم سے کم قدموں کا نشان، کسی بھی چیز پر چلتا ہے | حفاظت کے لئے مورچا-اہم ایمبیڈڈ |
| ڈیٹا بیس انجن | زیادہ سے زیادہ کارکردگی، مکمل میموری کنٹرول | -- |
| مرتب کرنے والے اور ترجمان | تیز، پورٹیبل، اچھی طرح سے سمجھا جاتا ہے | بڑے کمپائلر پروجیکٹس کے لیے C++ |
| ڈیوائس ڈرائیورز | زیادہ تر OS کرنل APIs کے لیے درکار ہے | -- |
| کارکردگی کے لحاظ سے اہم لائبریریاں | قریب ترین رفتار | یادداشت کی حفاظت کی ضمانت کے لیے مورچا |
| عام درخواست کی ترقی | بہت زیادہ دستی کام | Python, Java, Go, C# |
| ویب ڈویلپمنٹ | غلط ٹول مکمل طور پر | JavaScript, Go, Python |
| ڈیٹا سائنس / ایم ایل | اس کے لیے کوئی ماحولیاتی نظام نہیں ہے | ازگر، آر، جولیا |
---

## سی معیارات
| معیاری | سال | کلیدی اضافہ |
|------------|------|---------------|
| C89/C90 | 1989/1990 | اصل ANSI C -- اب بھی بنیادی لائن |
| C99 | 1999 | // تبصرے، bool کی قسم، متغیر لمبائی کی صفیں، ان لائن، stdint.h |
| C11 | 2011 | اٹامک آپریشنز، تھریڈز، گمنام ڈھانچہ، _Generic |
| C17 | 2018 | بگ کی اصلاحات اور وضاحتیں (کوئی نئی خصوصیات نہیں) |
| C23 | 2024 | nullptr، typeof، constexpr، بہتر پری پروسیسر |
زیادہ تر پروڈکشن کوڈ C11 یا C17 کو نشانہ بناتے ہیں۔ C23 جدید سہولتیں لاتا ہے لیکن اپنانے میں وقت لگتا ہے۔
---

## مصنوعی سوال و جواب
### Q1: C میں پوائنٹرز اور arrays میں کیا فرق ہے؟
**A:** ارے اور پوائنٹر ایک دوسرے سے متعلق ہیں لیکن الگ الگ۔ ایک سرنی میموری کا ایک متصل بلاک ہے جس کا ایک مقررہ سائز کمپائل کے وقت جانا جاتا ہے۔ پوائنٹر ایک متغیر ہے جو میموری ایڈریس رکھتا ہے۔ فنکشنز کے پاس بھیجے جانے پر ارییں پوائنٹرز میں کٹ جاتی ہیں، لیکن`sizeof(array)`کل سائز دیتا ہے جبکہ`sizeof(pointer)`صرف پوائنٹر سائز (4 یا 8 بائٹس) دیتا ہے۔ صف کے نام قابل ترمیم نہیں ہیں - آپ`arr++`نہیں کر سکتے۔
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

### Q2: میں میموری کا صحیح طریقے سے انتظام کیسے کرسکتا ہوں اور لیک ہونے سے کیسے بچ سکتا ہوں؟
**A:** ہر`malloc`/`calloc`میں ایک متعلقہ`free`ہونا ضروری ہے۔ عام غلطیاں: فری کرنا بھولنا (لیک)، دو بار آزاد کرنا (غیر متعینہ رویہ)، فری کرنے کے بعد میموری کا استعمال کرنا (آفٹر فری استعمال)، اور`malloc`واپسی کی قیمت (ناکامی پر NULL) کی جانچ نہ کرنا۔ بہترین عمل: ایک ہی ماڈیول میں مختص اور مفت، غلطی سے نمٹنے کے لیے "گوٹو کلین اپ" پیٹرن کا استعمال کریں، اور ہمیشہ آزاد پوائنٹرز کو NULL پر سیٹ کریں۔
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

### Q3: C میں غلطی سے نمٹنے کے بہترین طریقے کیا ہیں؟
**A:** C میں کوئی استثنا نہیں ہے۔ خرابی سے نمٹنے میں واپسی کی قدریں استعمال ہوتی ہیں (خرابی کوڈز، NULL پوائنٹرز، منفی اقدار)۔ معیاری پیٹرن: فنکشنز ناکامی پر اسٹیٹس کوڈ یا NULL واپس کرتے ہیں، اور سسٹم کالز کے لیے`errno`سیٹ کرتے ہیں۔ غلطیوں پر وسائل کی صفائی کے لیے "گوٹو کلین اپ" پیٹرن کا استعمال کریں۔ ہمیشہ`malloc`,`fopen`اور دوسرے فنکشنز کی واپسی کی قدروں کو چیک کریں جو ناکام ہو سکتے ہیں۔
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

### Q4: سٹرکٹس، یونینز اور بٹ فیلڈز میموری لے آؤٹ میں کیسے مختلف ہیں؟
**A:** سٹرکٹس ترتیب وار ترتیب کے ساتھ ممکنہ پیڈنگ کے ساتھ ترتیب دیتے ہیں۔ یونینز تمام ممبروں کو ایک ہی میموری والے مقام پر اوورلے کرتی ہیں — سائز سب سے بڑے ممبر کے برابر ہوتا ہے۔ بٹ فیلڈز متعدد اقدار کو ایک عدد میں پیک کرتے ہیں۔ سٹرکٹس متضاد ڈیٹا کے لیے ہیں، صرف ایک فیلڈ فعال ہونے پر ٹائپ پننگ یا اسپیس بچانے کے لیے یونین، اور کمپیکٹ فلیگ اسٹوریج کے لیے بٹ فیلڈز۔
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

### Q5: فنکشن پوائنٹرز کیا ہیں، اور مجھے انہیں کب استعمال کرنا چاہیے؟
**A:** فنکشن پوائنٹرز فنکشن کا ایڈریس اسٹور کرتے ہیں اور کال بیکس، پولیمورفزم، اور پلگ ان آرکیٹیکچرز کو فعال کرتے ہیں۔ وہ اعلیٰ ترتیب والے افعال (جیسے `qsort`،`bsearch`) کے لیے C کے نقطہ نظر کی بنیاد ہیں۔ نحو کے ساتھ ان کا اعلان کریں:`return_type (*name)(parameter_types)`۔
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

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: ایک متحرک صف کو لاگو کریں (ویکٹر)
**مسئلہ کا بیان:** C میں ایک متحرک صف کو لاگو کریں جو عناصر کے شامل ہونے پر خود بخود بڑھ جاتی ہے، O(1) کو سپورٹ کرتی ہے، اور مناسب صفائی فراہم کرتی ہے۔ یہ C++`std::vector`کے برابر ہے۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ایک متحرک صف کی ضرورت ہے: (1) ایک ڈھیر سے مختص بفر، (2) سائز (استعمال شدہ عناصر) اور صلاحیت (مختص کردہ سلاٹس) کی ٹریکنگ، (3) جب سائز صلاحیت تک پہنچ جائے تو دوبارہ جگہ، (4) مناسب میموری کی صفائی۔ 2x کا گروتھ فیکٹر O(1) کو ایمورٹائزڈ اپنڈ دیتا ہے۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- ابتدائی مختص کے لیے `malloc`، ترقی کے لیے`realloc`استعمال کریں۔
- ایک ڈھانچے میں ڈیٹا پوائنٹر، سائز اور صلاحیت کو اسٹور کریں۔
- جب`size == capacity`صلاحیت کو دوگنا کر کے بڑھیں۔
- `push`، `pop`، `get`، `set`، اور`free`آپریشنز فراہم کریں۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- Amortized O(1) push: دوگنا ہونے کا مطلب ہے کہ ہر عنصر کو زیادہ سے زیادہ O(log n) اوقات میں کاپی کیا جاتا ہے۔
-`vec_get`اور`vec_pop`میں باؤنڈز کی جانچ پڑتال غلطیوں کو جلد پکڑ لیتی ہے - C میں ضروری ہے جہاں رن ٹائم سیفٹی نیٹ نہیں ہے۔
- میموری: گنجائش 4 سے شروع ہونے والے 100 دھکے کے بعد، صلاحیت 128 تک پہنچ جاتی ہے (4→8→16→32→64→128)۔
- پیداوار: غیر استعمال شدہ میموری کو دوبارہ حاصل کرنے کے لیے بڑھنے کے بعد`shrink_to_fit`(صحیح سائز کے لیے realloc) کا استعمال کریں۔
### مسئلہ 2: ایک سادہ ہیش ٹیبل بنائیں
**مسئلہ کا بیان:** تصادم کے حل کے لیے الگ چیننگ کا استعمال کرتے ہوئے سٹرنگ کیز اور عددی اقدار کے ساتھ ایک ہیش ٹیبل لاگو کریں۔ داخل کرنے، تلاش کرنے اور حذف کرنے کی کارروائیوں کی حمایت کریں۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ایک ہیش ٹیبل ہیش فنکشن کے ذریعے انڈیکس کو صف میں لانے کے لیے کلیدوں کا نقشہ بناتا ہے۔ تصادم (ایک ہی انڈیکس میں مختلف کیز میپنگ) کو الگ الگ چیننگ کے ساتھ حل کیا جاتا ہے: ہر بالٹی اندراجات کی ایک منسلک فہرست ہے۔ ہمیں ضرورت ہے: ہیش فنکشن، داخل کریں، تلاش کریں، حذف کریں، اور صفائی کریں۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- سٹرنگ کیز کی اچھی تقسیم کے لیے FNV-1a ہیش استعمال کریں۔
- بالٹی پوائنٹرز کی صف (منسلک فہرست کے سر)۔
- لوڈ فیکٹر ٹریکنگ؛ جب لوڈ فیکٹر حد سے تجاوز کر جائے تو سائز تبدیل کریں۔
- تمام آپریشنز O(1) اوسط، O(n) بدترین کیس ہیں۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- ایک اچھے ہیش فنکشن اور معقول لوڈ فیکٹر کے ساتھ داخل/لوک اپ/ڈیلیٹ کے لیے اوسط O(1)۔
- FNV-1a کم سے کم حساب کے ساتھ سٹرنگ کیز کے لیے بہترین تقسیم فراہم کرتا ہے۔
-`hashmap_remove`میں پوائنٹر ٹو پوائنٹر تکنیک (`Entry **pp` ) بغیر کسی خاص کیس کے ہیڈ آف لسٹ اور درمیانی فہرست کو حذف کرنے کو خوبصورتی سے ہینڈل کرتی ہے۔
- پیداوار: جب بوجھ کا عنصر حد سے تجاوز کر جائے تو دوبارہ ہیشنگ شامل کریں۔ کیشے کی بہتر کارکردگی کے لیے اوپن ایڈریسنگ (لکیری پروبنگ) کا استعمال کریں۔
### مسئلہ 3: پروڈیوسر-صارف کے لیے ایک رنگ بفر لاگو کریں۔
**مسئلہ کا بیان:** آپریشن کے دوران ڈائنامک ایلوکیشن کے بغیر اعلی کارکردگی والے انٹر تھریڈ کمیونیکیشن کے لیے C میں لاک فری سنگل پروڈیوسر سنگل کنزیومر رِنگ بفر لاگو کریں۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ایک رنگ بفر (سرکلر بفر) پڑھنے اور لکھنے کے انڈیکس کے ساتھ ایک مقررہ سائز کی صف کا استعمال کرتا ہے۔ جب بفر بھر جاتا ہے تو مصنف بلاک یا اوور رائٹ کرتا ہے۔ SPSC (سنگل پروڈیوسر سنگل کنزیومر) کے لیے، ہم زیادہ سے زیادہ تھرو پٹ کے لیے تالے کے بجائے ایٹم آپریشنز استعمال کر سکتے ہیں۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- فکسڈ سائز کی صف شروع کرنے پر ایک بار مختص کی گئی۔
-`head`(پڑھنے کی پوزیشن) اور`tail`(لکھنے کی پوزیشن) بطور ایٹم انڈیکس۔
- پروڈیوسر ترقی کرتا ہے`tail`؛ صارفین کی ترقی `head`
- بفر خالی ہے جب `head == tail`؛ مکمل جب`(tail + 1) % capacity == head`.
- مناسب میموری ترتیب کے ساتھ C11 جوہری استعمال کریں۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- لاک فری: صرف جوہری آپریشنز - کوئی میوٹیکس نہیں، کوئی سیاق و سباق سوئچ نہیں ہے۔
- میموری آرڈرنگ: لکھنے پر`release`یقینی بناتا ہے کہ انڈیکس اپ ڈیٹ سے پہلے ڈیٹا نظر آئے۔ `acquire`آن ریڈ اس بات کو یقینی بناتا ہے کہ ہم انڈیکس کو پڑھنے کے بعد ڈیٹا دیکھیں۔
- پاور آف 2 صلاحیت:`% capacity`کی بجائے`& (capacity - 1)`کو قابل بناتا ہے — نمایاں طور پر تیز۔
- تھرو پٹ: جدید ہارڈ ویئر پر فی سیکنڈ اربوں آپریشن۔
- پیداوار: غلط شیئرنگ کو روکنے کے لیے`head`اور`tail`کے درمیان پیڈنگ شامل کریں (ہر ایک اپنی کیش لائن پر)۔
---

## خلاصہ
C جدید کمپیوٹنگ کی بنیاد ہے۔ یہ آپ کو کم سے کم تجرید اوور ہیڈ کے ساتھ ہارڈ ویئر پر زیادہ سے زیادہ کنٹرول فراہم کرتا ہے۔ اس کنٹرول کی لاگت ذمہ داری ہے -- آپ میموری کا انتظام کرتے ہیں، حدود کو چیک کرتے ہیں، اور غلطیوں کو خود ہینڈل کرتے ہیں۔ سسٹم پروگرامنگ، ایمبیڈڈ ڈیولپمنٹ، اور کہیں بھی کارکردگی اور وسائل کی رکاوٹوں کے لیے، C بے مثال ہے۔ ہر چیز کے لیے، C کے اوپر بنی ہوئی اعلیٰ سطحی زبانیں عام طور پر زیادہ نتیجہ خیز انتخاب ہوتی ہیں۔