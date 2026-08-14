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
#ج
لغة C هي لغة برمجة إجرائية ذات أغراض عامة أنشأها دينيس ريتشي في مختبرات بيل بين عامي 1969 و1973. وقد تم تصميمها لتنفيذ نظام التشغيل يونكس، ولا تزال واحدة من لغات البرمجة الأكثر استخدامًا على نطاق واسع بعد أكثر من 50 عامًا. توفر لغة C وصولاً منخفض المستوى إلى الذاكرة، ومكتبة قياسية بسيطة، وتخطيطًا نظيفًا لتعليمات الآلة - مما يجعلها الأساس الذي بنيت عليه معظم الحوسبة الحديثة.
C هي اللغة وراء أنظمة التشغيل (Linux وWindows kernel وmacOS)، والأنظمة المدمجة، ومحركات قواعد البيانات (SQLite، وPostgreSQL)، والمترجمين (Python's CPython، وRuby's MRI)، وكل لغات البرمجة الأخرى تقريبًا. إن فهم لغة C هو فهم كيفية عمل أجهزة الكمبيوتر فعليًا.
---

## لماذا تعتبر لغة C مهمة؟
- **القرب من الأجهزة**: ترتبط لغة C بشكل وثيق برمز الجهاز. لا يوجد أداة تجميع البيانات المهملة، ولا يوجد حمل إضافي في وقت التشغيل، ولا توجد عمليات تخصيص مخفية.
- **التواجد المنتشر**: بدءًا من وحدات التحكم الدقيقة وحتى أجهزة الكمبيوتر العملاقة، تعمل لغة C في كل مكان.
- **أساسيات الحوسبة**: Linux، وWindows، وmacOS kernels، وPython Interpreter، وSQLite، وGit - جميعها مكتوبة بلغة C.
- **الأداء**: سرعة تنفيذ شبه مثالية مع تحكم كامل في تخطيط الذاكرة.
- **التأثير**: بناء جملة لغة C ومفاهيمها (المؤشرات، والمصفوفات، والبنيات، والوظائف) على شكل C++، وJava، وC#، وJavaScript، وGo، وRust، ومعظم اللغات التي تلت ذلك.
##المقايضات
| الحد | التفاصيل | الحل النموذجي |
|-----------|------------------------|---|
| **إدارة الذاكرة اليدوية** | لا يوجد أداة تجميع البيانات المهملة - يمكنك تخصيص الذاكرة وتحريرها بنفسك | الاستخدام الدقيق لـ malloc/free؛ أنماط RAII في C++ |
| ** تجاوز سعة المخزن المؤقت ** | لا يوجد حدود للتحقق من المصفوفات - من السهل كتابة نهايات المخزن المؤقت السابقة | استخدم strncpy بدلاً من strcpy؛ تمكين تحذيرات المترجم |
| ** لا يوجد OOP مدمج ** | إجرائية فقط - لا توجد فئات أو وراثة أو طرق | استخدام الهياكل + مؤشرات الوظيفة؛ أو قم بالتبديل إلى C++ |
| **مكتبة قياسية محدودة** | الحد الأدنى من الوظائف المضمنة | مكتبات الطرف الثالث أو اكتب مكتباتك الخاصة |
| **سلوك غير محدد** | يتم تجميع العديد من الأخطاء بشكل جيد ولكنها تتعطل بشكل غير متوقع | استخدم المطهرات والمحللات الساكنة |
---

## أساسيات بناء الجملة
### البنية الأساسية
يبدأ كل برنامج بلغة C عند `main()`. يتم تجميع اللغة - يصبح كود المصدر كود الآلة عبر مترجم (GCC، Clang، MSVC).
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

### المتغيرات والأنواع
تتم كتابة لغة C بشكل ثابت - كل متغير له نوع ثابت معروف في وقت الترجمة.
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

### المؤشرات
المؤشرات هي الميزة الأقوى والأكثر سوء فهم في لغة C. يحمل المؤشر عنوان الذاكرة.
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

### التحكم في التدفق
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

### الوظائف والمكدس
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

## تخطيط الذاكرة
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

| المنطقة | ماذا يحدث هناك | العمر | من يديرها |
|--------|----------------|----------|----------------|
| **كومة** | المتغيرات المحلية، معلمات الدالة | حتى ترجع الدالة | مترجم (تلقائي) |
| ** كومة ** | تخصيصات مالوك/كالوك | حتى تتصل مجانًا () | أنت (دليل) |
| **البيانات/BSS** | المتغيرات العالمية والثابتة | عمر البرنامج بأكمله | مترجم (تلقائي) |
| **النص** | كود الآلة | عمر البرنامج بأكمله | للقراءة فقط |
---

## المكتبة القياسية
| رأس | الغرض | الوظائف المشتركة |
|--------|---------|----------------|
| `<stdio.h>`| الإدخال / الإخراج | printf، scanf، fopen، fgets، fprintf |
| `<stdlib.h>`| المرافق العامة | مالوك، مجاني، خروج، أتوي، راند، قسورت |
| `<string.h>`| عمليات السلسلة | strlen، strcpy، strncpy، strcmp، memcpy |
| `<math.h>`| الرياضيات | الخطيئة، كوس، الجذر التربيعي، الأسرى، القوات المسلحة البوروندية، السقف، الطابق |
| `<ctype.h>`| تصنيف الشخصيات | isalpha، isdigit، ممتاز، tolower |
| `<time.h>`| التاريخ والوقت | الوقت، الساعة، difftime، strftime |
| `<assert.h>`| تصحيح التأكيدات | تأكيد (الشرط) |
| `<errno.h>`| رموز الخطأ | خطأ، خطأ، خطأ |
---

## بناء الجملة والأنماط المتقدمة
### وحدات الماكرو للمعالج المسبق
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

### مؤشرات الوظائف وعمليات الاسترجاعات
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

### أنماط معالجة الأخطاء المخصصة
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

## التزامن والتوازي
### خيوط POSIX (pthreads)
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

### Mutex والدولة المشتركة
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

### الذرات والخيوط C11
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

## تكوين المشروع ونظام البناء
### هيكل المشروع
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

### ملف تعريفي
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

### خط أنابيب CI/CD (إجراءات GitHub)
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

## الاختبار
### اختبار الوحدة باستخدام إطار عمل بسيط
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

## إمكانية التشغيل البيني
### استدعاء C من بايثون (ctypes)
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

### الاتصال بـ C من لغات أخرى
| اللغة | آلية | مثال |
|----------|----------|---------|
| بايثون | أنواع، CFFI | `ctypes.CDLL("./lib.so")`|
| روبي | كمان | `Fiddle.dlopen("./lib.so")`|
| جافا | جيني | `System.loadLibrary("mylib")`|
| سي++ | خارجي "C" | `extern "C" void my_func();`|
| الصدأ | خارجي "C" + FFI | `extern "C" { fn my_func(); }`|
---

## أنماط التصميم
### مؤشر معتم (مصطلح Pimpl في لغة C)
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

### الجدول الافتراضي (OOP في لغة C)
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

## الأداء والتحسين
### أدوات التنميط
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

### تقنيات التحسين
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

## النشر
### التجميع المتقاطع
```bash
# Cross-compile for ARM (embedded)
arm-none-eabi-gcc -mcpu=cortex-m4 -o firmware.elf main.c

# Cross-compile for Windows from Linux
x86_64-w64-mingw32-gcc -o my_app.exe main.c

# Static linking (no shared library dependencies)
gcc -static -o my_app main.c
```

### نشر عامل الميناء
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

## الأنماط والتعابير الشائعة
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

## التجميع والأدوات
```bash
gcc -Wall -Wextra -o myprogram myprogram.c      # Basic compile
gcc -g -Wall -o myprogram myprogram.c            # With debug symbols
gcc -O2 -Wall -o myprogram myprogram.c           # With optimisation
gcc -std=c17 -Wall -o myprogram myprogram.c      # Specific standard
make          # Runs the Makefile
make clean    # Removes build artifacts
```

| أداة | الغرض |
|------|---------|
| ** مجلس التعاون الخليجي / كلانج ** | المجمعون |
| **جعل / CMake** | بناء الأنظمة |
| **جي دي بي** | المصحح |
| ** فالجريند ** | كاشف أخطاء الذاكرة (تسربات، وصول غير صالح) |
| **مطهر العنوان** | فحص الذاكرة في وقت الترجمة |
| **cppcheck** | التحليل الساكن |
| ** تنسيق الرنة ** | تنسيق الكود |
---

## متى يجب استخدام لغة C
| السيناريو | لماذا ج | البديل الأفضل |
|----------|-------|------------------|
| أنظمة التشغيل | الوصول المباشر إلى الأجهزة، بدون أي تكاليف تشغيل إضافية | -- |
| الأنظمة المدمجة / المتحكمات الدقيقة | الحد الأدنى من البصمة، يعمل على أي شيء | الصدأ للسلامة الحرجة المضمنة |
| محركات قواعد البيانات | أقصى أداء، تحكم كامل في الذاكرة | -- |
| مترجمون ومترجمون فوريون | سريع ومحمول ومفهوم جيدًا | C++ لمشاريع المترجم الأكبر |
| برامج تشغيل الأجهزة | مطلوب من قبل معظم واجهات برمجة تطبيقات kernel لنظام التشغيل | -- |
| مكتبات الأداء الحرجة | السرعة شبه المثالية | الصدأ لضمان سلامة الذاكرة |
| تطوير التطبيقات العامة | كثرة العمل اليدوي | بايثون، جافا، غو، C# |
| تطوير الويب | أداة خاطئة تمامًا | جافا سكريبت، اذهب، بايثون |
| علم البيانات / تعلم الآلة | لا يوجد نظام بيئي لهذا | بايثون، ر، جوليا |
---

## معايير ج
| قياسي | سنة | الإضافات الرئيسية |
|----------|------|--------------|
| C89/C90 | 1989/1990 | ANSI C الأصلي - لا يزال خط الأساس |
| C99 | 1999 | // التعليقات، النوع المنطقي، المصفوفات ذات الطول المتغير، المضمنة، stdint.h |
| ج11 | 2011 | العمليات الذرية، المواضيع، الهياكل المجهولة، _عام |
| ج17 | 2018 | إصلاحات الأخطاء وتوضيحاتها (لا توجد ميزات جديدة) |
| ج23 | 2024 | nullptr، typeof، constexpr، معالج مسبق محسّن |
تستهدف معظم أكواد الإنتاج C11 أو C17. يوفر C23 وسائل الراحة الحديثة ولكن اعتمادها يستغرق وقتًا.
---

## أسئلة وأجوبة اصطناعية
### س1: ما الفرق بين المؤشرات والمصفوفات في لغة C؟
**أ:** المصفوفات والمؤشرات مرتبطة ببعضها البعض ولكنها مختلفة. المصفوفة عبارة عن كتلة متجاورة من الذاكرة ذات حجم ثابت معروف في وقت الترجمة. المؤشر هو متغير يحمل عنوان الذاكرة. تتحلل المصفوفات إلى مؤشرات عند تمريرها إلى الوظائف، لكن`sizeof(array)`يعطي الحجم الإجمالي بينما يعطي`sizeof(pointer)`حجم المؤشر فقط (4 أو 8 بايت). أسماء المصفوفات ليست قيمًا قابلة للتعديل - لا يمكنك فعل`arr++`.
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

### س2: كيف يمكنني إدارة الذاكرة بشكل صحيح وتجنب التسريبات؟
**أ:** يجب أن يكون لكل`malloc`/`calloc``free` المطابق. الأخطاء الشائعة: نسيان التحرير (تسرب)، التحرير مرتين (سلوك غير محدد)، استخدام الذاكرة بعد التحرير (الاستخدام بعد التحرير)، وعدم التحقق من القيمة المرجعة`malloc`(NULL عند الفشل). أفضل الممارسات: التخصيص والتحرير في نفس الوحدة، واستخدام نمط "goto cleanup" لمعالجة الأخطاء، وتعيين المؤشرات المحررة دائمًا على NULL.
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

### س3: ما هي أفضل الممارسات لمعالجة الأخطاء في لغة C؟
**أ:** C ليس له استثناءات. تستخدم معالجة الأخطاء قيم الإرجاع (رموز الخطأ، مؤشرات NULL، القيم السالبة). النمط القياسي: تقوم الوظائف بإرجاع رمز الحالة أو NULL عند الفشل، وتعيين`errno`لاستدعاءات النظام. استخدم نمط "goto cleanup" لتنظيف الموارد عند حدوث أخطاء. تحقق دائمًا من قيم الإرجاع الخاصة بـ`malloc`و`fopen`والوظائف الأخرى التي يمكن أن تفشل.
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

### س 4: كيف تختلف البنيات والاتحادات وحقول البت في تخطيط الذاكرة؟
**أ:** تقوم الهياكل بوضع الأعضاء بشكل تسلسلي مع وجود حشوة محتملة للمحاذاة. تتراكب الاتحادات مع جميع الأعضاء في نفس موقع الذاكرة — الحجم يساوي أكبر عضو. تقوم حقول Bitfield بجمع قيم متعددة في عدد صحيح واحد. الهياكل مخصصة للبيانات غير المتجانسة، والاتحادات لضبط النوع أو توفير المساحة عندما يكون حقل واحد فقط نشطًا، وحقول البت لتخزين العلم المضغوط.
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

### س5: ما هي المؤشرات الوظيفية ومتى يجب استخدامها؟
**أ:** تقوم مؤشرات الوظائف بتخزين عنوان الوظيفة وتمكين عمليات الاسترجاعات وتعدد الأشكال وبنيات المكونات الإضافية. إنها أساس نهج لغة C في التعامل مع الوظائف ذات الترتيب الأعلى (مثل`qsort`و`bsearch`). قم بتعريفها باستخدام بناء الجملة:`return_type (*name)(parameter_types)`.
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

## حل المشكلات المتعلقة بسلسلة الأفكار
### المشكلة الأولى: تنفيذ مصفوفة ديناميكية (متجه)
**بيان المشكلة:** تنفيذ مصفوفة ديناميكية في لغة C تنمو تلقائيًا عند إضافة عناصر، وتدعم إلحاق O(1) المطفأ، وتوفر التنظيف المناسب. هذا هو المعادل C لـ C++ `std::vector`.
**الخطوة الأولى — فهم المشكلة:**
يحتاج المصفوفة الديناميكية إلى: (1) مخزن مؤقت مخصص للكومة، (2) تتبع الحجم (العناصر المستخدمة) والسعة (الفتحات المخصصة)، (3) إعادة التخصيص عندما يصل الحجم إلى السعة، (4) تنظيف الذاكرة بشكل مناسب. عامل النمو 2x يعطي إلحاق O (1) المطفأ.
**الخطوة الثانية — تحديد النهج:**
- استخدم`malloc`للتخصيص الأولي، و`realloc` للنمو.
- تخزين مؤشر البيانات وحجمها وسعتها في البنية.
- النمو بمضاعفة القدرة عند`size == capacity`.
- توفير عمليات`push`و`pop` و`get` و`set` و`free`.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- دفع O(1) المطفأ: المضاعفة تعني أنه يتم نسخ كل عنصر بحد أقصى O(log n) مرات.
- يقوم فحص الحدود في`vec_get`و`vec_pop` باكتشاف الأخطاء مبكرًا - وهو أمر ضروري في لغة C حيث لا توجد شبكة أمان أثناء التشغيل.
- الذاكرة: بعد 100 دفعة ابتداء من السعة 4 تصل السعة إلى 128 (4→8→16→32→64→128).
- الإنتاج: استخدم`shrink_to_fit`(إعادة تخصيص الحجم الدقيق) عند الانتهاء من النمو لاستعادة الذاكرة غير المستخدمة.
### المشكلة الثانية: إنشاء جدول تجزئة بسيط
**بيان المشكلة:** قم بتنفيذ جدول التجزئة باستخدام مفاتيح السلسلة وقيم الأعداد الصحيحة باستخدام تسلسل منفصل لحل التصادم. دعم عمليات الإدراج والبحث والحذف.
**الخطوة الأولى — فهم المشكلة:**
يقوم جدول التجزئة بتعيين المفاتيح لصفيف المؤشرات عبر وظيفة التجزئة. يتم حل التصادمات (تعيين مفاتيح مختلفة لنفس الفهرس) من خلال تسلسل منفصل: كل مجموعة عبارة عن قائمة مرتبطة من الإدخالات. نحتاج إلى: وظيفة التجزئة، والإدراج، والبحث، والحذف، والتنظيف.
**الخطوة الثانية — تحديد النهج:**
- استخدم تجزئة FNV-1a للتوزيع الجيد لمفاتيح السلسلة.
- مجموعة من مؤشرات الدلو (رؤوس القائمة المرتبطة).
- تتبع عامل الحمولة؛ تغيير الحجم عندما يتجاوز عامل الحمولة الحد الأدنى.
- جميع العمليات هي O(1) في المتوسط، وO(n) في أسوأ الحالات.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- متوسط O(1) للإدراج/البحث/الحذف مع وظيفة تجزئة جيدة وعامل تحميل معقول.
- يوفر FNV-1a توزيعًا ممتازًا لمفاتيح السلسلة بأقل قدر من الحساب.
- تتعامل تقنية المؤشر إلى المؤشر (`Entry **pp`) في`hashmap_remove`بشكل أنيق مع حذف رأس القائمة وحذف القائمة الوسطى بدون حالات خاصة.
- الإنتاج: أضف إعادة صياغة عندما يتجاوز عامل الحمولة الحد الأدنى. استخدم العنونة المفتوحة (الفحص الخطي) لتحسين أداء ذاكرة التخزين المؤقت.
### المشكلة 3: تنفيذ المخزن المؤقت الحلقي للمنتج والمستهلك
**بيان المشكلة:** تنفيذ مخزن مؤقت حلقي لمستهلك واحد ومنتج واحد وخالي من القفل في لغة C للاتصال بين الخيوط عالي الأداء دون تخصيص ديناميكي أثناء التشغيل.
**الخطوة الأولى — فهم المشكلة:**
يستخدم المخزن المؤقت الحلقي (المخزن المؤقت الدائري) مصفوفة ذات حجم ثابت مع مؤشرات القراءة والكتابة. عند امتلاء المخزن المؤقت، يقوم الكاتب بحظر النص أو الكتابة فوقه. بالنسبة إلى SPSC (منتج واحد ومستهلك واحد)، يمكننا استخدام العمليات الذرية بدلاً من الأقفال لتحقيق أقصى قدر من الإنتاجية.
**الخطوة الثانية — تحديد النهج:**
- يتم تخصيص مصفوفة ذات حجم ثابت مرة واحدة عند التهيئة.
-`head`(موضع القراءة) و`tail` (موضع الكتابة) كمؤشرات ذرية.
- منتج يتقدم`tail`; تقدم المستهلك`head`.
- المخزن المؤقت فارغ عندما يكون `head == tail`؛ ممتلئ عند`(tail + 1) % capacity == head`.
- استخدم ذرات C11 مع ترتيب الذاكرة المناسب.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- خالية من القفل: العمليات الذرية فقط - لا توجد كائنات المزامنة، ولا توجد مفاتيح تبديل للسياق.
- ترتيب الذاكرة: يضمن`release`عند الكتابة أن البيانات مرئية قبل تحديث الفهرس؛  يضمن`acquire`عند القراءة رؤية البيانات بعد قراءة الفهرس.
- سعة Power-of-2: تمكن`& (capacity - 1)`بدلاً من`% capacity`- بشكل أسرع بشكل ملحوظ.
- الإنتاجية: مليارات العمليات في الثانية على الأجهزة الحديثة.
- الإنتاج: أضف حشوة بين`head`و`tail` لمنع المشاركة الخاطئة (كل على سطر ذاكرة التخزين المؤقت الخاص به).
---

## ملخص
لغة C هي حجر الأساس للحوسبة الحديثة. فهو يمنحك أقصى قدر من التحكم في الأجهزة مع الحد الأدنى من الحمل التجريدي. تكلفة هذا التحكم هي المسؤولية - فأنت تدير الذاكرة وتتحقق من الحدود وتتعامل مع الأخطاء بنفسك. بالنسبة لبرمجة الأنظمة، والتطوير المضمن، وفي أي مكان يهم فيه الأداء وقيود الموارد، تظل لغة C لا مثيل لها. بالنسبة لكل شيء آخر، عادةً ما تكون اللغات ذات المستوى الأعلى المبنية على لغة C خيارات أكثر إنتاجية.