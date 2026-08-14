---
# Metadata
title: "C — Common Mistakes & Anti-Patterns"
description: "Comprehensive guide to common pitfalls, traps, and anti-patterns in C that catch even experienced developers, with explanations and corrections."
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Initial common mistakes document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [c, common-mistakes, anti-patterns, pitfalls, memory-safety, best-practices, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# C — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্ন
এই নথিটি সি-তে সবচেয়ে সাধারণ ভুল, ফাঁদ, এবং অ্যান্টি-প্যাটার্নগুলি ক্যাটালগ করে। প্রতিটি এন্ট্রি ভুল পদ্ধতি দেখায়, কেন এটি ব্যর্থ হয় তা ব্যাখ্যা করে এবং সঠিক সমাধান প্রদান করে। C আপনাকে সম্পূর্ণ নিয়ন্ত্রণ দেয় — যার অর্থ মেমরি নিরাপত্তা, সীমানা পরীক্ষা এবং অনির্ধারিত আচরণের জন্য সম্পূর্ণ দায়িত্ব।
---

## 1.`gets()`/`strcpy()`এর সাথে বাফার ওভারফ্লো
```c
// ❌ WRONG — no bounds checking
char buffer[64];
gets(buffer);           // NEVER use gets() — removed in C11
strcpy(buffer, input);  // overflow if input > 63 chars

// ✅ CORRECT — use bounded functions
fgets(buffer, sizeof(buffer), stdin);
strncpy(buffer, input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // ensure null termination

// ✅ BEST — use snprintf
snprintf(buffer, sizeof(buffer), "%s", input);
```

---

## 2. ঝুলন্ত পয়েন্টার
```c
// ❌ WRONG — pointer to freed memory
int *ptr = malloc(sizeof(int));
*ptr = 42;
free(ptr);
printf("%d", *ptr);  // undefined behavior!

// ✅ CORRECT — set pointer to NULL after free
free(ptr);
ptr = NULL;

// ❌ WRONG — returning pointer to local variable
int *get_value() {
    int x = 42;
    return &x;  // x is destroyed when function returns
}

// ✅ CORRECT — allocate on heap or use output parameter
int *get_value() {
    int *x = malloc(sizeof(int));
    *x = 42;
    return x;  // caller must free
}
```

---

## 3. অফ-বাই-ওয়ান ত্রুটি
```c
// ❌ WRONG — writing past array bounds
int arr[10];
for (int i = 0; i <= 10; i++) {  // i=10 is out of bounds!
    arr[i] = 0;
}

// ✅ CORRECT — use < not <=
for (int i = 0; i < 10; i++) {
    arr[i] = 0;
}

// ✅ CORRECT — use sizeof for array length
for (size_t i = 0; i < sizeof(arr) / sizeof(arr[0]); i++) {
    arr[i] = 0;
}
```

---

## 4. অপ্রচলিত ভেরিয়েবল
```c
// ❌ WRONG — using uninitialized memory
int x;
if (condition) x = 42;
printf("%d", x);  // undefined if condition is false

// ✅ CORRECT — always initialize
int x = 0;
if (condition) x = 42;
printf("%d", x);
```

---

## 5.`scanf()`প্রস্থ সীমা ছাড়াই
```c
// ❌ WRONG — buffer overflow
char name[20];
scanf("%s", name);  // no limit on input length

// ✅ CORRECT — specify maximum width
scanf("%19s", name);  // leaves room for null terminator
```

---

## 6. ইন্টিজার ওভারফ্লো
```c
// ❌ WRONG — no overflow check
int a = INT_MAX;
int b = a + 1;  // undefined behavior (signed overflow)

// ✅ CORRECT — check before operation
if (a > INT_MAX - 1) {
    fprintf(stderr, "Overflow detected\n");
    // handle error
}
int result = a + 1;

// ✅ CORRECT — use unsigned for wrapping behavior
unsigned int a = UINT_MAX;
unsigned int b = a + 1;  // well-defined: wraps to 0
```

---

## 7. মেমরি লিক
```c
// ❌ WRONG — forgetting to free
void process() {
    int *data = malloc(1000 * sizeof(int));
    // ... use data ...
    return;  // memory leaked!
}

// ✅ CORRECT — free before every return
void process() {
    int *data = malloc(1000 * sizeof(int));
    if (!data) return;
    // ... use data ...
    free(data);
}

// ✅ CORRECT — use goto cleanup pattern
void process() {
    int *data = NULL;
    int *result = NULL;

    data = malloc(1000 * sizeof(int));
    if (!data) goto cleanup;

    result = malloc(500 * sizeof(int));
    if (!result) goto cleanup;

    // ... use data and result ...

cleanup:
    free(data);
    free(result);
}
```

---

## 8. ফর্ম্যাট স্ট্রিং দুর্বলতা
```c
// ❌ WRONG — user input as format string
char *user_input = get_input();
printf(user_input);  // attacker can use %x, %n

// ✅ CORRECT — always use format string literal
printf("%s", user_input);
```

---

## 9. শর্তে`=`এবং`==`বিভ্রান্তিকর
```c
// ❌ WRONG — assignment instead of comparison
if (x = 5) {  // always true, assigns 5 to x
    printf("x is 5");
}

// ✅ CORRECT — use comparison
if (x == 5) {
    printf("x is 5");
}

// ✅ DEFENSIVE — Yoda condition (compiler catches typo)
if (5 == x) {
    // if you write if (5 = x), compiler error
}
```

---

## 10. পয়েন্টার পাটিগণিত না বোঝা
```c
// ❌ WRONG — treating pointer arithmetic as byte arithmetic
int arr[5] = {1, 2, 3, 4, 5};
int *p = arr;
p = p + 1;  // advances by sizeof(int), not 1 byte!

// ❌ WRONG — arithmetic on void pointers
void *vp = arr;
vp = vp + 1;  // undefined behavior (void has no size)

// ✅ CORRECT — cast void pointer first
int *ip = (int *)vp;
ip = ip + 1;  // advances by sizeof(int)
```

---

## 11. অ্যান্টি-প্যাটার্ন: ম্যাজিক নম্বর
```c
// ❌ WRONG — unexplained constants
if (status == 42) { ... }
char buffer[16384];

// ✅ CORRECT — use named constants or enums
#define MAX_BUFFER_SIZE 16384
#define STATUS_SUCCESS 42

enum { MAX_BUFFER_SIZE = 16384, STATUS_SUCCESS = 42 };
```

---

## 12. `switch`-এ`break`অনুপস্থিত
```c
// ❌ WRONG — fall-through (often unintentional)
switch (grade) {
    case 'A': printf("Excellent");
    case 'B': printf("Good");     // falls through from A!
    case 'C': printf("Average");  // falls through from B!
    default:  printf("Fail");
}

// ✅ CORRECT — explicit break or fall-through comment
switch (grade) {
    case 'A': printf("Excellent"); break;
    case 'B': printf("Good");      break;
    case 'C': printf("Average");   break;
    default:  printf("Fail");      break;
}
```

---

## সারাংশ
C এর বিপদগুলি সুপরিচিত কিন্তু সর্বদা বর্তমান: বাফার ওভারফ্লো, ড্যাংলিং পয়েন্টার, ইন্টিজার ওভারফ্লো, ফরম্যাট স্ট্রিং আক্রমণ এবং মেমরি লিক। শৃঙ্খলা হল: সর্বদা রিটার্ন মান পরীক্ষা করুন, আপনি যা বরাদ্দ করেন তা সর্বদা বিনামূল্যে, সর্বদা বাউন্ডেড ফাংশন ব্যবহার করুন (`snprintf`,`strncpy`,`fgets`), কখনই`gets()`ব্যবহার করবেন না, সমস্ত ভেরিয়েবল শুরু করবেন না এবং Valgrind এবং Address এর মতো সরঞ্জামগুলি ব্যবহার করুন৷ C যত্নশীল প্রোগ্রামারদের অতুলনীয় কর্মক্ষমতা এবং নিয়ন্ত্রণের সাথে পুরস্কৃত করে — কিন্তু অনির্ধারিত আচরণ এবং নিরাপত্তা দুর্বলতার সাথে অসতর্কতার শাস্তি দেয়।