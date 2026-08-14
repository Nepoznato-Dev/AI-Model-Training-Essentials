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
# کراس لینگویج کا موازنہ — ہم آہنگی اور ہم آہنگی۔
## کنکرنسی ماڈلز کا جائزہ
| زبان | ماڈل | کلیدی طریقہ کار | مشترکہ میموری؟ |
|------------|---------|----------------------------|----------------|
| ازگر | GIL + تھریڈز | `threading`,`asyncio`| ہاں (جی آئی ایل متوازی کو محدود کرتا ہے) |
| جاوا اسکرپٹ | ایونٹ لوپ | وعدے،`async/await`| نہیں (سنگل تھریڈڈ) |
| مورچا | ملکیت + بھیجیں / مطابقت پذیری | `std::thread`,`async/await`, چینلز | مرتب وقت کی حفاظت |
| جاؤ | گوروٹینز | `go func()`, چینلز | نہیں (پیغام گزرنا) |
| جاوا | OS تھریڈز | `Thread`,`ExecutorService`,`CompletableFuture`| جی ہاں |
| TypeScript | ایونٹ لوپ | وعدے،`async/await`| نہیں (سنگل تھریڈڈ) |
| سی | پوسکس تھریڈز | `pthread`, OpenMP | ہاں (دستی مطابقت پذیری) |
| C++ | OS تھریڈز | `std::thread`,`std::async`, coroutines | ہاں (دستی مطابقت پذیری) |
| C# | async/await | `Task`,`async/await`,`Parallel`| جی ہاں |
| روبی | GVL + فائبرز | `Thread`,`Fiber`,`Ractor`(3.0+) | ہاں (جی وی ایل)، ریکٹر: نہیں |
| سوئفٹ | اداکار | `async/await`, اداکار،`Sendable`| نہیں (اداکار تنہائی) |
| کوٹلن | کوروٹینز | `suspend`,`launch`,`async`| ڈسپیچر پر منحصر ہے |
| پی ایچ پی | عمل پر مبنی | `pcntl_fork`, فائبر (8.1+) | نہیں (علیحدہ عمل) |
| سکالا | JVM تھریڈز |  `Future`، اکا اداکار، ZIO، Cats Effect | ہاں (JVM) |
| ہاسکل | سبز دھاگے | `forkIO`, STM,`async`| ہاں (حفاظت کے لیے STM) |
| لوا | کوروٹینز | `coroutine.create/resume/yield`| نہیں (کوآپریٹو) |
| آر | ترتیب وار + متوازی | `parallel`,`future`| نہیں (علیحدہ عمل) |
| جولیا | ٹاسکس + تھریڈز | `@async`,`@threads`,`Distributed`| ہاں (دھاگے سے محفوظ اقسام) |
| ڈارٹ | الگ تھلگ | `Isolate`,`async/await`| نہیں (پیغام گزرنا) |
| پرل | دھاگے + کانٹا | `threads`,`fork`| ہاں (تھریڈز) |
| MATLAB | متوازی پول | `parfor`,`spmd`,`gpuArray`| نہیں (کارکنان) |
| ایس کیو ایل | N/A | ڈیٹا بیس کنکرنسی کو ہینڈل کرتا ہے (MVCC، تالے) | N/A |
| شیل | پس منظر کے عمل | `&`,`wait`,`xargs -P`| نہیں (علیحدہ عمل) |
| فورٹران | Coarrays + OpenMP | `coarray`,`do concurrent`, OpenMP | ہاں (مشترکہ میموری) |
| اڈا | ٹاسکس + محفوظ | `task`,`protected object`, ملاقات | ہاں (محفوظ اشیاء) |
| کوبول | N/A | بیچ پروسیسنگ، کوئی مقامی ہم آہنگی نہیں | N/A |
| پرولوگ | N/A | ترتیب وار (کچھ نفاذ میں تھریڈز ہوتے ہیں) | N/A |
| Lisp/Clojure | STM + ایجنٹس | `future`,`promise`,`core.async`, STM | بندش: STM (refs, atoms) |
| Erlang/Elixir | اداکار ماڈل | `spawn`, پیغام پاس کرنا,`receive`| نہیں (پیغام گزرنا) |
| OCaml | ڈومین + اثر | `Domain.spawn`, اثر ہینڈلرز (5.0+) | نہیں (ڈومینز) |
| اسمبلی | N/A | OS پر منحصر (انٹرپٹس، سسٹم کالز) | N/A |
| ڈیلفی | دھاگے | `TThread`,`TTask`| ہاں (دستی مطابقت پذیری) |
| سکریچ | واقعہ پر مبنی | `when green flag clicked`, براڈکاسٹ | نہیں (اسپرائٹ تنہائی) |
| VB | async/await | `Async/Await`,`Task`| جی ہاں |
## دھاگے کی تخلیق
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

## کنکرنسی کے کلیدی نمونے۔
### پروڈیوسر-صارف
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

### Mutex / لاکنگ
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

## خلاصہ ٹیبل
| تمثیل | زبانیں |
|------------|------------|
| **OS تھریڈز + مشترکہ میموری** | C, C++, Java, C#, Fortran, Delphi, VB |
| **GIL/Lock + Threads** | ازگر، روبی، پرل |
| **گوروٹینز + چینلز** | جاؤ |
| **اداکار ماڈل** | ایرلنگ، ایلیکسیر، اسکالا (اکا)، روبی (ریکٹر) |
| **async/await + ایونٹ لوپ** | JavaScript, TypeScript, Rust, Swift, C#, Kotlin, Dart |
| **STM (سافٹ ویئر ٹرانزیکشنل میموری)** | ہاسکل، کلوجور |
| **کورٹائنز (کوآپریٹو)** | لوا، کوٹلن |
| ** الگ تھلگ (کوئی مشترکہ میموری نہیں)** | ڈارٹ، جاوا اسکرپٹ، ٹائپ اسکرپٹ |
| **کوئی مقامی ہم آہنگی نہیں** | COBOL، Prolog، سکریچ، SQL |