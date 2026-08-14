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
# ক্রস-ল্যাঙ্গুয়েজ তুলনা — কনকারেন্সি এবং প্যারালেলিজম
## কনকারেন্সি মডেল ওভারভিউ
| ভাষা | মডেল | কী মেকানিজম | ভাগ করা মেমরি? |
|------------|-------|------------------|----------------|
| পাইথন | GIL + থ্রেড | `threading`,`asyncio`| হ্যাঁ (জিআইএল সমান্তরালতাকে সীমাবদ্ধ করে) |
| জাভাস্ক্রিপ্ট | ইভেন্ট লুপ | প্রতিশ্রুতি,`async/await`| না (একক থ্রেডেড) |
| মরিচা | মালিকানা + পাঠান/সিঙ্ক | `std::thread`,`async/await`, চ্যানেল | কম্পাইল-সময় নিরাপত্তা |
| যান | গোরুটিন | `go func()`, চ্যানেল | না (বার্তা পাসিং) |
| জাভা | OS থ্রেড | `Thread`,`ExecutorService`,`CompletableFuture`| হ্যাঁ |
| টাইপস্ক্রিপ্ট | ইভেন্ট লুপ | প্রতিশ্রুতি,`async/await`| না (একক থ্রেডেড) |
| গ | POSIX থ্রেড | `pthread`, OpenMP | হ্যাঁ (ম্যানুয়াল সিঙ্ক) |
| সি++ | OS থ্রেড | `std::thread`,`std::async`, coroutines | হ্যাঁ (ম্যানুয়াল সিঙ্ক) |
| C# | async/await | `Task`,`async/await`,`Parallel`| হ্যাঁ |
| রুবি | GVL + ফাইবার | `Thread`,`Fiber`,`Ractor`(3.0+) | হ্যাঁ (GVL), Ractor: না |
| সুইফট | অভিনেতা | `async/await`, অভিনেতা,`Sendable`| না (অভিনেতা বিচ্ছিন্নতা) |
| কোটলিন | করুটিন | `suspend`,`launch`,`async`| প্রেরকের উপর নির্ভর করে |
| পিএইচপি | প্রক্রিয়া ভিত্তিক | `pcntl_fork`, ফাইবার (8.1+) | না (পৃথক প্রক্রিয়া) |
| স্কালা | JVM থ্রেড | `Future`, আক্কা অভিনেতা, ZIO, ক্যাটস ইফেক্ট | হ্যাঁ (JVM) |
| হাসকেল | সবুজ সুতো | `forkIO`, STM,`async`| হ্যাঁ (নিরাপত্তার জন্য STM) |
| লুয়া | করুটিন | `coroutine.create/resume/yield`| না (সমবায়) |
| আর | অনুক্রমিক + সমান্তরাল | `parallel`,`future`| না (পৃথক প্রক্রিয়া) |
| জুলিয়া | কার্য + থ্রেড | `@async`,`@threads`,`Distributed`| হ্যাঁ (থ্রেড-নিরাপদ প্রকার) |
| ডার্ট | বিচ্ছিন্ন | `Isolate`,`async/await`| না (বার্তা পাসিং) |
| পার্ল | থ্রেড + কাঁটা | `threads`,`fork`| হ্যাঁ (থ্রেড) |
| ম্যাটল্যাব | সমান্তরাল পুল | `parfor`,`spmd`,`gpuArray`| না (শ্রমিক) |
| এসকিউএল | N/A | ডাটাবেস কনকারেন্সি পরিচালনা করে (MVCC, লক) | N/A |
| শেল | পটভূমি প্রক্রিয়া | `&`,`wait`,`xargs -P`| না (পৃথক প্রক্রিয়া) |
| ফোর্টরান | Coarrays + OpenMP | `coarray`,`do concurrent`, OpenMP | হ্যাঁ (ভাগ মেমরি) |
| আদা | কার্য + সুরক্ষিত | `task`,`protected object`, মিলনস্থল | হ্যাঁ (সুরক্ষিত বস্তু) |
| COBOL | N/A | ব্যাচ প্রসেসিং, নেটিভ কনকারেন্সি নেই | N/A |
| প্রোলগ | N/A | অনুক্রমিক (কিছু বাস্তবায়নের থ্রেড আছে) | N/A |
| লিস্প/ক্লোজার | STM + এজেন্ট | `future`,`promise`,`core.async`, STM | ক্লোজার: STM (refs, পরমাণু) |
| এরলাং/এলিক্সির | অভিনেতা মডেল | `spawn`, বার্তা পাসিং,`receive`| না (বার্তা পাসিং) |
| OCaml | ডোমেন + প্রভাব | `Domain.spawn`, প্রভাব হ্যান্ডলার (5.0+) | না (ডোমেন) |
| সমাবেশ | N/A | OS-নির্ভর (ব্যঘাত, সিস্টেম কল) | N/A |
| ডেলফি | থ্রেড | `TThread`,`TTask`| হ্যাঁ (ম্যানুয়াল সিঙ্ক) |
| আঁচড় | ইভেন্ট-চালিত | `when green flag clicked`, সম্প্রচার | না (স্প্রাইট বিচ্ছিন্নতা) |
| ভিবি | async/await | `Async/Await`,`Task`| হ্যাঁ |
## থ্রেড তৈরি
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

## মূল সামঞ্জস্য নিদর্শন
### প্রযোজক-ভোক্তা
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

### মিউটেক্স / লকিং
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

## সারসংক্ষেপ টেবিল
| দৃষ্টান্ত | ভাষা |
|------------|------------|
| **ওএস থ্রেড + শেয়ার করা মেমরি** | C, C++, Java, C#, Fortran, Delphi, VB |
| **জিআইএল/লক + থ্রেড** | পাইথন, রুবি, পার্ল |
| **গোরুটিন + চ্যানেল** | যান |
| **অভিনেতা মডেল** | Erlang, Elixir, Scala (Akka), Ruby (Ractor) |
| **async/await + ইভেন্ট লুপ** | জাভাস্ক্রিপ্ট, টাইপস্ক্রিপ্ট, মরিচা, সুইফট, সি#, কোটলিন, ডার্ট |
| **STM (সফ্টওয়্যার লেনদেন মেমরি)** | Haskell, Clojure |
| **করোটিন (সমবায়)** | লুয়া, কোটলিন |
| **বিচ্ছিন্ন (কোন শেয়ার করা মেমরি নেই)** | ডার্ট, জাভাস্ক্রিপ্ট, টাইপস্ক্রিপ্ট |
| **কোন নেটিভ কনকারেন্সি** | COBOL, Prolog, Scratch, SQL |