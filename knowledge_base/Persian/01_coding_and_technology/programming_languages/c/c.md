---
# فراداده
عنوان: "C"
توضیحات: "مرجع جامع برای زبان برنامه نویسی C شامل مرور کلی، مبادلات، اصول نحو، اکوسیستم و زمان استفاده از آن."
دسته بندی: "کدنویسی و فناوری"
نسخه: "1.0.0"
وضعیت: "فعال"
# مشارکت
نویسندگان:
  - نام: "تیم آموزشی مدل AI"
    ایمیل: ""
    نقش: "نویسنده_اصلی"
مشارکت کنندگان: []
تغییرات ثبت شده:
  - نسخه: "1.0.0"
    تاریخ: "05-08-2026"
    نویسنده: "تیم آموزشی مدل هوش مصنوعی"
    تغییرات: "فراداده YAML frontmatter برای ردیابی مشارکت کنندگان اضافه شد"
# نقد و بررسی
ایجاد شده: "05-08-2026"
last_modified: "05-08-2026"
بازبینی_تاریخ: "05-02-2027"
reviewed_by: "تیم پایگاه دانش کدنویسی و فناوری"
next_review: "05-08-2027"
# طبقه بندی
برچسب‌ها: [c، زبان برنامه‌نویسی، نحو، اکوسیستم، کدگذاری و فناوری]
سطح سختی: "متوسط"
پیش نیاز: []
تخمینی_زمان_خواندن: "35 دقیقه"
# راهنمای مشارکت
مشارکت:
  مجوز: "MIT"
  feedback_channel: "مشکلات GitHub"
  how_to_contribute: "ارسال روابط عمومی با تغییرات و به روز رسانی تغییرات"
  review_process: "تغییرات توسط نگهبانان دسته قبل از ادغام بررسی می شود"
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
| **بدون OOP داخلی ** | فقط رویه ای -- بدون کلاس، وراثت یا روش | استفاده از structs + نشانگرهای تابع. یا به C++ |
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
|  __محافظت شده_1__ | خدمات عمومی | malloc, free, exit, atoi, rand, qsort |
| `<string.h>`| عملیات رشته | strlen، strcpy، strncpy، strcmp، memcpy |
|  __محافظت شده_3__ | ریاضی | sin, cos, sqrt, pow, fabs, ceil, floor |
| `<ctype.h>`| طبقه بندی شخصیت | isalpha, isdigit, toupper, tolower |
| `<time.h>`| تاریخ و زمان | زمان، ساعت، زمان فاصله، زمان strftime |
|  __محافظت شده_6__ | اشکال زدایی اظهارات | اظهار (شرط) |
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
| یاقوت | کمانچه |  __محافظت شده_1__ |
| جاوا | JNI | `System.loadLibrary("mylib")`|
| C++ | خارجی "C" |  __محافظت شده_3__ |
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

## خلاصه
C پایه محاسبات مدرن است. حداکثر کنترل را بر روی سخت افزار با حداقل هزینه انتزاعی به شما می دهد. هزینه این کنترل مسئولیت است -- شما حافظه را مدیریت می کنید، محدوده ها را بررسی می کنید و خطاها را خودتان مدیریت می کنید. برای برنامه نویسی سیستم، توسعه تعبیه شده، و هر جایی که عملکرد و محدودیت منابع مهم باشد، C بی بدیل باقی می ماند. برای هر چیز دیگری، زبان های سطح بالاتر ساخته شده در بالای C معمولاً انتخاب های سازنده تری هستند.