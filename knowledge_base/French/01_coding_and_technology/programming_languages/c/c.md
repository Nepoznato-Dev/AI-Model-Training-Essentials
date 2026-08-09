---
# Métadonnées
titre : "C"
description : "Référence complète sur le langage de programmation C couvrant la présentation, les compromis, les principes fondamentaux de la syntaxe, l'écosystème et quand l'utiliser."
catégorie : "Codage et technologie"
version : "1.0.0"
statut : "actif"
# Contribution
auteurs :
  - nom : « Équipe de formation des modèles IA »
    email: ""
    rôle : "original_author"
contributeurs : []
journal des modifications :
  - version : "1.0.0"
    date : "05/08/2026"
    auteur : « Équipe de formation des modèles IA »
    modifications : « Ajout des métadonnées de premier plan YAML pour le suivi des contributeurs »
# Révision
créé : "2026-08-05"
last_modified : "05/08/2026"
date_de_revue : "05/02/2027"
review_by : "Équipe de base de connaissances en matière de codage et de technologie"
next_review : "2027-08-05"
#Classement
balises : [c, langage de programmation, syntaxe, écosystème, codage et technologie]
niveau de difficulté : "intermédiaire"
prérequis : []
estimate_reading_time : "35 min"
# Guide des contributions
apport :
  licence : "MIT"
  feedback_channel : "Problèmes GitHub"
  how_to_contribute : "Soumettez un PR avec les modifications et mettez à jour le journal des modifications"
  review_process : "Les modifications sont examinées par les responsables de la catégorie avant la fusion"
---
#C
C est un langage de programmation procédural à usage général créé par Dennis Ritchie aux Bell Labs entre 1969 et 1973. Il a été conçu pour implémenter le système d'exploitation Unix et reste l'un des langages de programmation les plus utilisés plus de 50 ans plus tard. C fournit un accès mémoire de bas niveau, une bibliothèque standard minimale et un mappage clair aux instructions machine, ce qui en fait la base sur laquelle repose la plupart des ordinateurs modernes.
C est le langage derrière les systèmes d'exploitation (Linux, noyau Windows, macOS), les systèmes embarqués, les moteurs de bases de données (SQLite, PostgreSQL), les compilateurs (CPython de Python, MRI de Ruby) et pratiquement tous les autres langages d'exécution de programmation. Comprendre C, c'est comprendre comment fonctionnent réellement les ordinateurs.
---

## Pourquoi C est important
- **Proximité du matériel** : C correspond étroitement au code machine. Il n'y a pas de garbage collector, pas de surcharge d'exécution, pas d'allocations cachées.
- **Ubiquité** : des microcontrôleurs aux superordinateurs, le C fonctionne partout.
- **Fondements de l'informatique** : Linux, Windows, noyaux macOS, interpréteur Python, SQLite, Git -- tous écrits en C.
- **Performances** : vitesse d'exécution quasi optimale avec un contrôle total sur la disposition de la mémoire.
- **Influence** : la syntaxe et les concepts du C (pointeurs, tableaux, structures, fonctions) ont façonné C++, Java, C#, JavaScript, Go, Rust et la plupart des langages qui ont suivi.
## Les compromis
| Limitation | Détails | Solution de contournement typique |
|-----------|---------|-------------------|
| **Gestion manuelle de la mémoire** | Pas de garbage collector : vous allouez et libérez de la mémoire vous-même | Utilisation prudente de malloc/free ; Modèles RAII en C++ |
| **Débordements de tampon** | Aucune limite de vérification sur les tableaux -- écriture facile au-delà des extrémités du tampon | Utilisez strncpy au lieu de strcpy ; activer les avertissements du compilateur |
| **Pas de POO intégrée** | Procédure uniquement – ​​pas de classes, d'héritage ou de méthodes | Utilisez des structures + des pointeurs de fonction ; ou passez à C++ |
| **Bibliothèque standard limitée** | Fonctionnalité intégrée minimale | Bibliothèques tierces ou écrivez la vôtre |
| **Comportement non défini** | De nombreuses erreurs se compilent correctement mais plantent de manière imprévisible | Utiliser des désinfectants, des analyseurs statiques |
---

## Fondamentaux de la syntaxe
### Structure de base
Chaque programme C commence à`main()`. Le langage est compilé : le code source devient du code machine via un compilateur (GCC, Clang, MSVC).
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

### Variables et types
C est typé statiquement : chaque variable a un type fixe connu au moment de la compilation.
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

### Pointeurs
Les pointeurs sont la fonctionnalité la plus puissante et la plus mal comprise du C. Un pointeur contient une adresse mémoire.
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

### Flux de contrôle
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

### Fonctions et pile
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

## Disposition de la mémoire
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

| Région | Que s'y passe-t-il | Durée de vie | Qui le gère |
|--------|----------------|----------|----------------|
| **Pile** | Variables locales, paramètres de fonction | Jusqu'à ce que la fonction revienne | Compilateur (automatique) |
| **Tas** | allocations malloc/calloc | Jusqu'à ce que vous appeliez gratuitement() | Vous (manuel) |
| **Données/BSS** | Variables globales et statiques | Durée de vie complète du programme | Compilateur (automatique) |
| **Texte** | Code machine | Durée de vie complète du programme | Lecture seule |
---

## La bibliothèque standard
| En-tête | Objectif | Fonctions communes |
|--------|---------|-----------------|
| `<stdio.h>`| Entrée/sortie | printf, scanf, fopen, fgets, fprintf |
| `<stdlib.h>`| Utilitaires généraux | malloc, gratuit, sortie, atoi, rand, qsort |
| `<string.h>`| Opérations sur les chaînes | strlen, strcpy, strncpy, strcmp, memcpy |
| `<math.h>`| Mathématiques | sin, cos, sqrt, pow, fabs, plafond, sol |
| `<ctype.h>`| Classement des caractères | isalpha, isdigit, toupper, tolower |
| `<time.h>`| Date et heure | heure, horloge, difftime, strftime |
| `<assert.h>`| Débogage des assertions | affirmer(condition) |
| `<errno.h>`| Codes d'erreur | erreur, perror, strerror |
---

## Syntaxe et modèles avancés
### Macros de préprocesseur
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

### Pointeurs de fonction et rappels
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

### Modèles de gestion des erreurs personnalisés
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

## Concurrence et parallélisme
### Fils de discussion POSIX (pthreads)
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

### Mutex et état partagé
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

### C11 Atomiques et fils
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

## Configuration du projet et système de construction
### Structure du projet
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

### Pipeline CI/CD (actions GitHub)
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

## Tests
### Tests unitaires avec un framework simple
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

## Interopérabilité
### Appel de C depuis Python (ctypes)
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

### Appeler C depuis d'autres langues
| Langue | Mécanisme | Exemple |
|----------|-----------|---------|
| Python | types, cffi | `ctypes.CDLL("./lib.so")`|
| Rubis | Violon | `Fiddle.dlopen("./lib.so")`|
| Java | JNI | `System.loadLibrary("mylib")`|
| C++ | externe "C" | `extern "C" void my_func();`|
| Rouille | externe "C" + FFI | `extern "C" { fn my_func(); }`|
---

## Modèles de conception
### Pointeur opaque (idiome Pimpl en C)
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

### Table virtuelle (POO en C)
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

## Performances et optimisation
### Outils de profilage
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

### Techniques d'optimisation
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

## Déploiement
### Compilation croisée
```bash
# Cross-compile for ARM (embedded)
arm-none-eabi-gcc -mcpu=cortex-m4 -o firmware.elf main.c

# Cross-compile for Windows from Linux
x86_64-w64-mingw32-gcc -o my_app.exe main.c

# Static linking (no shared library dependencies)
gcc -static -o my_app main.c
```

### Déploiement de Docker
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

## Modèles et expressions idiomatiques courants
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

## Compilation et outillage
```bash
gcc -Wall -Wextra -o myprogram myprogram.c      # Basic compile
gcc -g -Wall -o myprogram myprogram.c            # With debug symbols
gcc -O2 -Wall -o myprogram myprogram.c           # With optimisation
gcc -std=c17 -Wall -o myprogram myprogram.c      # Specific standard
make          # Runs the Makefile
make clean    # Removes build artifacts
```

| Outil | Objectif |
|------|--------------|
| **GCC / Clang** | Compilateurs |
| **Faire / CMake** | Construire des systèmes |
| **GDB** | Débogueur |
| **Valgrind** | Détecteur d'erreur mémoire (fuites, accès invalide) |
| **AdresseSanitizer** | Vérification de la mémoire au moment de la compilation |
| **cppcheck** | Analyse statique |
| **format clang** | Formatage des codes |
---

## Quand utiliser C
| Scénario | Pourquoi C | Meilleure alternative |
|--------------|-------|---------|
| Systèmes d'exploitation | Accès direct au matériel, pas de surcharge d'exécution | -- |
| Systèmes embarqués / microcontrôleurs | Encombrement minimal, fonctionne sur n'importe quoi | Rouille pour les éléments critiques pour la sécurité |
| Moteurs de bases de données | Performances maximales, contrôle total de la mémoire | -- |
| Compilateurs et interprètes | Rapide, portable, bien compris | C++ pour les grands projets de compilateur |
| Pilotes de périphérique | Requis par la plupart des API du noyau du système d'exploitation | -- |
| Bibliothèques critiques en termes de performances | Vitesse presque optimale | Rust pour une sécurité de mémoire garantie |
| Développement d'applications générales | Trop de travail manuel | Python, Java, Go, C# |
| Développement Web | Mauvais outil entièrement | JavaScript, Go, Python |
| Science des données / ML | Pas d'écosystème pour ça | Python, R, Julia |
---

## Normes C
| Norme | Année | Ajouts clés |
|--------------|------|--------------|
| C89/C90 | 1989/1990 | L'ANSI C original – toujours la référence |
| C99 | 1999 | // commentaires, type booléen, tableaux de longueur variable, en ligne, stdint.h |
| C11 | 2011 | Opérations atomiques, threads, structures anonymes, _Generic |
| C17 | 2018 | Corrections de bugs et clarifications (pas de nouvelles fonctionnalités) |
| C23 | 2024 | nullptr, typeof, constexpr, préprocesseur amélioré |
La plupart des codes de production ciblent C11 ou C17. Le C23 apporte des commodités modernes, mais son adoption prend du temps.
---

## Résumé
C est le fondement de l’informatique moderne. Il vous donne un contrôle maximal sur le matériel avec une surcharge d'abstraction minimale. Le coût de ce contrôle est celui de la responsabilité : vous gérez la mémoire, vérifiez les limites et gérez vous-même les erreurs. Pour la programmation de systèmes, le développement embarqué et partout où les contraintes de performances et de ressources sont importantes, le C reste inégalé. Pour tout le reste, les langages de niveau supérieur construits sur C sont généralement des choix plus productifs.