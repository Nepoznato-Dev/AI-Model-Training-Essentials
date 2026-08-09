---
# मेटाडेटा
शीर्षक: "सी"
विवरण: "सी प्रोग्रामिंग भाषा के लिए व्यापक संदर्भ जिसमें अवलोकन, ट्रेड-ऑफ़, सिंटैक्स फंडामेंटल, इकोसिस्टम और इसका उपयोग कब करना है।"
श्रेणी: "कोडिंग और प्रौद्योगिकी"
संस्करण: "1.0.0"
स्थिति: "सक्रिय"
#योगदान
लेखक:
  - नाम: "एआई मॉडल ट्रेनिंग टीम"
    ईमेल: ""
    भूमिका: "मूल_लेखक"
योगदानकर्ता: []
चेंजलॉग:
  - संस्करण: "1.0.0"
    दिनांक: "2026-08-05"
    लेखक: "एआई मॉडल ट्रेनिंग टीम"
    परिवर्तन: "योगदानकर्ता ट्रैकिंग के लिए YAML फ्रंटमैटर मेटाडेटा जोड़ा गया"
#समीक्षा
बनाया गया: "2026-08-05"
अंतिम_संशोधित: "2026-08-05"
समीक्षा दिनांक: "2027-02-05"
इनके द्वारा समीक्षा: "कोडिंग और प्रौद्योगिकी ज्ञान आधार टीम"
अगली_समीक्षा: "2027-08-05"
#वर्गीकरण
टैग: [सी, प्रोग्रामिंग-भाषा, सिंटैक्स, पारिस्थितिकी तंत्र, कोडिंग-और-प्रौद्योगिकी]
कठिनाई_स्तर: "मध्यवर्ती"
पूर्वावश्यकताएँ: []
अनुमानित_पढ़ने_का समय: "35 मिनट"
# योगदान मार्गदर्शिका
योगदान:
  लाइसेंस: "एमआईटी"
  फीडबैक_चैनल: "गिटहब मुद्दे"
  कैसे_तो_योगदान करें: "परिवर्तनों के साथ एक पीआर सबमिट करें और चेंजलॉग अपडेट करें"
  समीक्षा_प्रक्रिया: "विलय से पहले श्रेणी अनुरक्षकों द्वारा परिवर्तनों की समीक्षा की जाती है"
---
# सी
सी एक सामान्य-प्रयोजन, प्रक्रियात्मक प्रोग्रामिंग भाषा है जिसे 1969 और 1973 के बीच बेल लैब्स में डेनिस रिची द्वारा बनाया गया था। इसे यूनिक्स ऑपरेटिंग सिस्टम को लागू करने के लिए डिज़ाइन किया गया था, और यह 50 वर्षों के बाद भी सबसे व्यापक रूप से उपयोग की जाने वाली प्रोग्रामिंग भाषाओं में से एक बनी हुई है। सी निम्न-स्तरीय मेमोरी एक्सेस, एक न्यूनतम मानक लाइब्रेरी और मशीन निर्देशों के लिए एक साफ मैपिंग प्रदान करता है - जिससे यह वह आधार बन जाता है जिस पर अधिकांश आधुनिक कंप्यूटिंग का निर्माण किया जाता है।
C ऑपरेटिंग सिस्टम (लिनक्स, विंडोज कर्नेल, macOS), एम्बेडेड सिस्टम, डेटाबेस इंजन (SQLite, PostgreSQL), कंपाइलर (पायथन का CPython, रूबी का MRI), और वस्तुतः हर अन्य प्रोग्रामिंग भाषा रनटाइम के पीछे की भाषा है। सी को समझने का मतलब यह समझना है कि कंप्यूटर वास्तव में कैसे काम करते हैं।
---

## सी क्यों मायने रखता है
- **हार्डवेयर से निकटता**: सी मशीन कोड के करीब मैप करता है। कोई कचरा संग्रहकर्ता नहीं है, कोई रनटाइम ओवरहेड नहीं है, कोई छिपा हुआ आवंटन नहीं है।
- **सर्वव्यापकता**: माइक्रोकंट्रोलर से लेकर सुपर कंप्यूटर तक, C हर जगह चलता है।
- **कंप्यूटिंग का आधार**: Linux, Windows, macOS कर्नेल, Python इंटरप्रेटर, SQLite, Git - सभी C में लिखे गए हैं।
- **प्रदर्शन**: मेमोरी लेआउट पर पूर्ण नियंत्रण के साथ लगभग इष्टतम निष्पादन गति।
- **प्रभाव**: सी के सिंटैक्स और अवधारणाओं (पॉइंटर्स, एरे, स्ट्रक्चर्स, फ़ंक्शंस) ने सी++, जावा, सी#, जावास्क्रिप्ट, गो, रस्ट और उसके बाद आने वाली अधिकांश भाषाओं को आकार दिया।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **मैन्युअल मेमोरी प्रबंधन** | कोई कचरा संग्रहकर्ता नहीं - आप स्वयं मेमोरी आवंटित और मुक्त करते हैं | मॉलोक/फ्री का सावधानीपूर्वक उपयोग; C++ में RAII पैटर्न |
| **बफर ओवरफ्लो** | सरणियों पर जाँच की कोई सीमा नहीं - पिछले बफ़र सिरों को लिखना आसान है | strcpy के बजाय strncpy का प्रयोग करें; संकलक चेतावनियाँ सक्षम करें |
| **कोई अंतर्निहित OOP नहीं** | केवल प्रक्रियात्मक -- कोई वर्ग, वंशानुक्रम या विधियाँ नहीं | स्ट्रक्चर्स + फ़ंक्शन पॉइंटर्स का उपयोग करें; या C++ पर स्विच करें |
| **सीमित मानक पुस्तकालय** | न्यूनतम अंतर्निहित कार्यक्षमता | तृतीय-पक्ष पुस्तकालय या अपना स्वयं का लिखें |
| **अपरिभाषित व्यवहार** | कई गलतियाँ ठीक से संकलित होती हैं लेकिन अप्रत्याशित रूप से क्रैश हो जाती हैं | सैनिटाइज़र, स्टेटिक एनालाइज़र का उपयोग करें |
---

## सिंटेक्स बुनियादी बातें
### बुनियादी संरचना
प्रत्येक C प्रोग्राम`main()`से शुरू होता है। भाषा संकलित की जाती है - स्रोत कोड एक कंपाइलर (जीसीसी, क्लैंग, एमएसवीसी) के माध्यम से मशीन कोड बन जाता है।
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

### चर और प्रकार
C स्थिर रूप से टाइप किया गया है - प्रत्येक वेरिएबल का एक निश्चित प्रकार होता है जिसे संकलन समय पर जाना जाता है।
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

### सूचक
पॉइंटर्स सी की सबसे शक्तिशाली और सबसे गलत समझी जाने वाली विशेषता है। एक पॉइंटर एक मेमोरी एड्रेस रखता है।
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

### प्रवाह को नियंत्रित करें
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

### फ़ंक्शंस और स्टैक
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

## मेमोरी लेआउट
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

| क्षेत्र | वहां क्या होता है | जीवनकाल | इसका प्रबंधन कौन करता है |
|--------|----------------|-------|----------------|
| **स्टैक** | स्थानीय चर, फ़ंक्शन पैरामीटर | फ़ंक्शन वापस आने तक | कंपाइलर (स्वचालित) |
| **ढेर** | मॉलोक/कैलोक आवंटन | जब तक आप free() | पर कॉल नहीं करते आप (मैनुअल) |
| **डेटा/बीएसएस** | वैश्विक और स्थैतिक चर | संपूर्ण कार्यक्रम जीवनकाल | कंपाइलर (स्वचालित) |
| **पाठ** | मशीन कोड | संपूर्ण कार्यक्रम जीवनकाल | केवल पढ़ने के लिए |
---

## मानक पुस्तकालय
| हेडर | उद्देश्य | सामान्य कार्य |
|--------|--------||
|  __संरक्षित_0__ | इनपुट/आउटपुट | प्रिंटफ, स्कैनएफ, फॉपेन, एफगेट्स, एफप्रिंटफ |
|  __संरक्षित_1__ | सामान्य उपयोगिताएँ | मॉलोक, फ्री, एग्जिट, एटोई, रैंड, क्यूसॉर्ट |
|  __संरक्षित_2__ | स्ट्रिंग ऑपरेशन | स्ट्रलेन, स्ट्रैपी, स्ट्रंकपी, स्ट्रैम्प, मेम्सीपीई |
|  __संरक्षित_3__ | गणित | पाप, क्योंकि, sqrt, पाउ, फैब्स, छत, फर्श |
|  __संरक्षित_4__ | चरित्र वर्गीकरण | इसाल्फा, इसडिजिट, टॉपर, टोलोअर |
|  __संरक्षित_5__ | दिनांक और समय | समय, घड़ी, अंतरसमय, स्ट्रफ़टाइम |
|  __संरक्षित_6__ | डिबगिंग दावे | जोर (शर्त) |
|  __संरक्षित_7__ | त्रुटि कोड | इरनो, पेररर, स्ट्रेरर |
---

## उन्नत सिंटैक्स और पैटर्न
### प्रीप्रोसेसर मैक्रोज़
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

### फ़ंक्शन पॉइंटर्स और कॉलबैक
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

### कस्टम त्रुटि प्रबंधन पैटर्न
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

## समवर्ती एवं समांतरता
### POSIX थ्रेड्स (pthreads)
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

### म्यूटेक्स और साझा स्थिति
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

### C11 परमाणु और धागे
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना संरचना
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

### मेकफ़ाइल
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

### सीआई/सीडी पाइपलाइन (गिटहब क्रियाएँ)
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

## परीक्षण
### एक सरल रूपरेखा के साथ इकाई परीक्षण
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

## अंतरसंचालनीयता
### पायथन से C को कॉल करना (ctypes)
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

### अन्य भाषाओं से C को कॉल करना
| भाषा | तंत्र | उदाहरण |
|---|----|---|
| पायथन | सीटाइप्स, सीएफएफआई |  __संरक्षित_0__ |
| रूबी | बेला |  __संरक्षित_1__ |
| जावा | जेएनआई |  __संरक्षित_2__ |
| सी++ | बाहरी "सी" |  __संरक्षित_3__ |
| जंग | बाहरी "सी" + एफएफआई |  __संरक्षित_4__ |
---

## डिज़ाइन पैटर्न
### अपारदर्शी सूचक (सी में पिंपल मुहावरा)
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

### वर्चुअल टेबल (सी में ओओपी)
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

## प्रदर्शन एवं अनुकूलन
### प्रोफाइलिंग उपकरण
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

### अनुकूलन तकनीकें
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

## तैनाती
### क्रॉस-संकलन
```bash
# Cross-compile for ARM (embedded)
arm-none-eabi-gcc -mcpu=cortex-m4 -o firmware.elf main.c

# Cross-compile for Windows from Linux
x86_64-w64-mingw32-gcc -o my_app.exe main.c

# Static linking (no shared library dependencies)
gcc -static -o my_app main.c
```

### डॉकर परिनियोजन
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

## सामान्य पैटर्न और मुहावरे
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

## संकलन और टूलींग
```bash
gcc -Wall -Wextra -o myprogram myprogram.c      # Basic compile
gcc -g -Wall -o myprogram myprogram.c            # With debug symbols
gcc -O2 -Wall -o myprogram myprogram.c           # With optimisation
gcc -std=c17 -Wall -o myprogram myprogram.c      # Specific standard
make          # Runs the Makefile
make clean    # Removes build artifacts
```

| उपकरण | उद्देश्य |
|------|---------|
| **जीसीसी/क्लैंग** | संकलक |
| **बनाओ/सीमेक** | सिस्टम बनाएं |
| **जीडीबी** | डिबगर |
| **वालग्रिंड** | मेमोरी त्रुटि डिटेक्टर (लीक, अमान्य पहुंच) |
| **एड्रेस सेनिटाइजर** | संकलन-समय स्मृति जाँच |
| **cppcheck** | स्थैतिक विश्लेषण |
| **क्लैंग-प्रारूप** | कोड फ़ॉर्मेटिंग |
---

## सी का उपयोग कब करें
| परिदृश्य | क्यों सी | बेहतर विकल्प |
|---|-------|-------------------|
| ऑपरेटिंग सिस्टम | डायरेक्ट हार्डवेयर एक्सेस, कोई रनटाइम ओवरहेड नहीं | -- |
| एंबेडेड सिस्टम/माइक्रोकंट्रोलर | न्यूनतम पदचिह्न, किसी भी चीज़ पर चलता है | सुरक्षा के लिए जंग-महत्वपूर्ण एम्बेडेड |
| डेटाबेस इंजन | अधिकतम प्रदर्शन, पूर्ण मेमोरी नियंत्रण | -- |
| संकलनकर्ता और दुभाषिए | तेज़, पोर्टेबल, अच्छी तरह से समझा गया | बड़े कंपाइलर प्रोजेक्ट के लिए C++ |
| डिवाइस ड्राइवर | अधिकांश OS कर्नेल API द्वारा आवश्यक | -- |
| प्रदर्शन-महत्वपूर्ण पुस्तकालय | लगभग-इष्टतम गति | गारंटीशुदा स्मृति सुरक्षा के लिए जंग |
| सामान्य अनुप्रयोग विकास | बहुत ज्यादा मैन्युअल काम | पायथन, जावा, गो, सी# |
| वेब विकास | पूरी तरह से गलत उपकरण | जावास्क्रिप्ट, गो, पायथन |
| डेटा साइंस/एमएल | इसके लिए कोई पारिस्थितिकी तंत्र नहीं | पायथन, आर, जूलिया |
---

## सी मानक
| मानक | वर्ष | मुख्य परिवर्धन |
|---|------|----|
| C89/C90 | 1989/1990 | मूल एएनएसआई सी - अभी भी आधार रेखा |
| C99 | 1999 | // टिप्पणियाँ, बूल प्रकार, चर-लंबाई सरणियाँ, इनलाइन, stdint.h |
| सी11 | 2011 | परमाणु संचालन, धागे, अनाम संरचनाएं, _जेनेरिक |
| सी17 | 2018 | बग समाधान और स्पष्टीकरण (कोई नई सुविधाएँ नहीं) |
| सी23 | 2024 | nullptr, typeof, constexpr, बेहतर प्रीप्रोसेसर |
अधिकांश उत्पादन कोड C11 या C17 को लक्षित करते हैं। C23 आधुनिक सुविधाएं लाता है लेकिन अपनाने में समय लगता है।
---

## सारांश
सी आधुनिक कंप्यूटिंग का आधार है। यह आपको न्यूनतम अमूर्त ओवरहेड के साथ हार्डवेयर पर अधिकतम नियंत्रण प्रदान करता है। उस नियंत्रण की लागत जिम्मेदारी है - आप मेमोरी का प्रबंधन करते हैं, सीमाओं की जांच करते हैं, और त्रुटियों को स्वयं संभालते हैं। सिस्टम प्रोग्रामिंग, एंबेडेड डेवलपमेंट और कहीं भी प्रदर्शन और संसाधन की कमी के मामले में, सी बेजोड़ है। बाकी सभी चीज़ों के लिए, C के शीर्ष पर निर्मित उच्च-स्तरीय भाषाएँ आमतौर पर अधिक उत्पादक विकल्प होती हैं।