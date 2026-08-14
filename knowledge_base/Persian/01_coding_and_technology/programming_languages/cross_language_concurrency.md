<!--
---
# Metadata
title: "Cross-Language Comparison — Concurrency & Parallelism"
description: "Side-by-side comparison of concurrency models across 34 programming languages."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cross-language comparison"
tags: [concurrency, parallelism, cross-language, comparison, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# مقایسه بین زبانی - همزمانی و موازی
## بررسی اجمالی مدل های همزمان
| زبان | مدل | مکانیسم کلیدی | حافظه مشترک؟ |
|----------|-------|--------------|----------------|
| پایتون | GIL + موضوعات | `threading`,`asyncio`| بله (GIL موازی سازی را محدود می کند) |
| جاوا اسکریپت | حلقه رویداد | Promises,`async/await`| بدون (تک نخ) |
| زنگ زدگی | مالکیت + ارسال/همگام سازی | `std::thread`,`async/await`, کانال های | کامپایل ایمنی زمان |
| برو | گوروتین ها | `go func()`, کانال های | خیر (پیام عبور می کند) |
| جاوا | موضوعات سیستم عامل | `Thread`,`ExecutorService`,`CompletableFuture`| بله |
| TypeScript | حلقه رویداد | Promises,`async/await`| بدون (تک نخ) |
| ج | موضوعات POSIX |  `pthread`، OpenMP | بله (همگام سازی دستی) |
| C++ | موضوعات سیستم عامل | `std::thread`,`std::async`, coroutines | بله (همگام سازی دستی) |
| سی شارپ | async/انتظار | `Task`,`async/await`,`Parallel`| بله |
| یاقوت | GVL + الیاف | `Thread`,`Fiber`,`Ractor`(3.0+) | بله (GVL)، راکتور: نه |
| سویفت | بازیگران | `async/await`, بازیگران,`Sendable`| خیر (انزوای بازیگر) |
| کاتلین | روتین ها | `suspend`,`launch`,`async`| بستگی به دیسپچر دارد |
| پی اچ پی | مبتنی بر فرآیند |  `pcntl_fork`، الیاف (8.1+) | خیر (فرایندهای جداگانه) |
| اسکالا | موضوعات JVM |  `Future`، بازیگران Akka، ZIO، Cats Effect | بله (JVM) |
| هاسکل | نخ های سبز | `forkIO`, STM,`async`| بله (STM برای ایمنی) |
| لوا | روتین ها | `coroutine.create/resume/yield`| خیر (تعاونی) |
| R | ترتیبی + موازی | `parallel`,`future`| خیر (فرایندهای جداگانه) |
| جولیا | وظایف + موضوعات | `@async`,`@threads`,`Distributed`| بله (انواع رزوه ایمن) |
| دارت | جدا شده | `Isolate`,`async/await`| خیر (پیام عبور می کند) |
| پرل | نخ + چنگال | `threads`,`fork`| بله (رشته ها) |
| متلب | استخر موازی | `parfor`,`spmd`,`gpuArray`| خیر (کارگران) |
| SQL | N/A | پایگاه داده کنترل همزمانی (MVCC، قفل) | N/A |
| پوسته | فرآیندهای پس زمینه | `&`,`wait`,`xargs -P`| خیر (فرایندهای جداگانه) |
| فرترن | Coarrays + OpenMP | `coarray`,`do concurrent`, OpenMP | بله (حافظه مشترک) |
| آدا | وظایف + محافظت شده | `task`,`protected object`, قرار ملاقات | بله (اشیاء محافظت شده) |
| COBOL | N/A | پردازش دسته ای، بدون همزمانی بومی | N/A |
| پرولوگ | N/A | ترتیبی (برخی از پیاده سازی ها دارای نخ هستند) | N/A |
| Lisp/Clojure | عوامل STM + | `future`,`promise`,`core.async`, STM | کلژور: STM (refs، اتم) |
| ارلنگ/اکسیر | مدل بازیگر | `spawn`, ارسال پیام,`receive`| خیر (پیام عبور می کند) |
| OCaml | دامنه + افکت |  `Domain.spawn`، کنترل کننده های افکت (5.0+) | بدون (دامنه) |
| مونتاژ | N/A | وابسته به سیستم عامل (وقفه ها، تماس های سیستمی) | N/A |
| دلفی | موضوعات | `TThread`,`TTask`| بله (همگام سازی دستی) |
| خراش | رویداد محور | `when green flag clicked`, پخش | خیر (جداسازی اسپریت) |
| VB | async/انتظار | `Async/Await`,`Task`| بله |
## ایجاد موضوع
```python
# Python: threading
import threading
t = threading.Thread(target=worker, args=(data,))
t.start()
t.join()

# Python: asyncio
import asyncio
async def main():
    await asyncio.gather(task1(), task2())
asyncio.run(main())
```

```javascript
// JavaScript: Promises
const result = await Promise.all([task1(), task2()]);

// JavaScript: Web Workers
const worker = new Worker('worker.js');
worker.postMessage(data);
worker.onmessage = (e) => console.log(e.data);
```

```rust
// Rust: threads
use std::thread;
let handle = thread::spawn(|| {
    println!("Hello from thread!");
});
handle.join().unwrap();

// Rust: async (tokio)
#[tokio::main]
async fn main() {
    let task = tokio::spawn(async { /* work */ });
    task.await.unwrap();
}
```

```go
// Go: goroutines
go func() {
    fmt.Println("Hello from goroutine!")
}()

// Go: channels
ch := make(chan int)
go func() { ch <- 42 }()
value := <-ch
```

```java
// Java: threads
Thread t = new Thread(() -> System.out.println("Hello!"));
t.start();
t.join();

// Java: CompletableFuture
CompletableFuture.supplyAsync(() -> compute())
    .thenAccept(System.out::println);
```

```c
// C: POSIX threads
#include <pthread.h>
void* worker(void* arg) {
    printf("Hello from thread!\n");
    return NULL;
}
pthread_t t;
pthread_create(&t, NULL, worker, NULL);
pthread_join(t, NULL);
```

```go
// Go: worker pool pattern
func worker(id int, jobs <-chan int, results chan<- int) {
    for j := range jobs {
        results <- j * 2
    }
}
jobs := make(chan int, 100)
results := make(chan int, 100)
for w := 0; w < 3; w++ {
    go worker(w, jobs, results)
}
```

```erlang
% Erlang: spawn + message passing
Pid = spawn(fun() ->
    receive
        {From, Msg} -> From ! {response, Msg}
    end
end),
Pid ! {self(), hello},
receive
    {Pid, Response} -> io:format("~p~n", [Response])
end.
```

```elixir
# Elixir: Task (built on Erlang processes)
task = Task.async(fn -> compute() end)
result = Task.await(task)

# Elixir: GenServer (OTP behavior)
defmodule Worker do
  use GenServer
  def start_link(args), do: GenServer.start_link(__MODULE__, args)
  def handle_call(:work, _from, state), do: {:reply, result, state}
end
```

```swift
// Swift: async/await + actors
actor Counter {
    var count = 0
    func increment() { count += 1 }
}

let counter = Counter()
Task {
    await counter.increment()
}

// Swift: TaskGroup
await withTaskGroup(of: Int.self) { group in
    for i in 0..<10 {
        group.addTask { return i * i }
    }
}
```

```kotlin
// Kotlin: coroutines
import kotlinx.coroutines.*

runBlocking {
    val deferred = async { computeAsync() }
    println(deferred.await())
}

// Kotlin: coroutine scope
CoroutineScope(Dispatchers.Default).launch {
    val result = withContext(Dispatchers.IO) { fetchData() }
}
```

## الگوهای همزمانی کلیدی
### تولید کننده-مصرف کننده
```go
// Go: channels
func producer(ch chan<- int) {
    for i := 0; i < 10; i++ { ch <- i }
    close(ch)
}
func consumer(ch <-chan int) {
    for v := range ch { fmt.Println(v) }
}
ch := make(chan int)
go producer(ch)
consumer(ch)
```

```rust
// Rust: channels (mpsc)
use std::sync::mpsc;
use std::thread;
let (tx, rx) = mpsc::channel();
thread::spawn(move || {
    for i in 0..10 { tx.send(i).unwrap(); }
});
for val in rx { println!("{}", val); }
```

```erlang
% Erlang: message passing
producer(Pid, 0) -> Pid ! done;
producer(Pid, N) -> Pid ! {data, N}, producer(Pid, N-1).

consumer() ->
    receive
        done -> ok;
        {data, N} -> io:format("~p~n", [N]), consumer()
    end.
```

### Mutex / قفل
```java
// Java: synchronized
synchronized (lock) {
    sharedResource++;
}

// Java: ReentrantLock
ReentrantLock lock = new ReentrantLock();
lock.lock();
try { sharedResource++; }
finally { lock.unlock(); }
```

```python
# Python: threading.Lock
import threading
lock = threading.Lock()
with lock:
    shared_resource += 1
```

```rust
// Rust: Mutex (compile-time safety)
use std::sync::{Arc, Mutex};
let counter = Arc::new(Mutex::new(0));
let c = counter.clone();
thread::spawn(move || {
    let mut num = c.lock().unwrap();
    *num += 1;
});
```

```csharp
// C#: lock
lock (lockObj) {
    sharedResource++;
}

// C#: SemaphoreSlim
await semaphoreSlim.WaitAsync();
try { /* critical section */ }
finally { semaphoreSlim.Release(); }
```

## جدول خلاصه
| پارادایم | زبان ها |
|----------|-----------|
| ** موضوعات سیستم عامل + حافظه مشترک ** | C, C++, Java, C#, Fortran, Delphi, VB |
| **GIL/Lock + Threads** | پایتون، روبی، پرل |
| **مجموعه ها + کانال** | برو |
| **مدل بازیگر** | ارلنگ، اکسیر، اسکالا (آکا)، روبی (راکتور) |
| **ناهمگام/انتظار + حلقه رویداد** | JavaScript، TypeScript، Rust، Swift، C#، Kotlin، Dart |
| **STM (حافظه معاملاتی نرم افزار)** | Haskell، Clojure |
| **کوروتین (تعاونی)** | لوا، کوتلین |
| **ایزوله (بدون حافظه مشترک)** | دارت، جاوا اسکریپت، تایپ اسکریپت |
| **بدون همزمانی بومی** | COBOL، Prolog، Scratch، SQL |