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
# การเปรียบเทียบข้ามภาษา - เห็นพ้องต้องกันและความเท่าเทียม
## ภาพรวมโมเดลการทำงานพร้อมกัน
| ภาษา | รุ่น | กลไกสำคัญ | หน่วยความจำที่ใช้ร่วมกัน? |
|----------|-------|-------------------|----------------|
| หลาม | GIL + เธรด | `threading`,`asyncio`| ใช่ (GIL จำกัดความเท่าเทียม) |
| จาวาสคริปต์ | วนซ้ำเหตุการณ์ | สัญญา`async/await`| ไม่ (เธรดเดียว) |
| สนิม | ความเป็นเจ้าของ + ส่ง/ซิงค์ | `std::thread`,`async/await`, ช่อง | ความปลอดภัยในการคอมไพล์เวลา |
| ไป | กรูทีน | `go func()`, ช่อง | ไม่ (ส่งข้อความ) |
| ชวา | เธรด OS | `Thread`,`ExecutorService`,`CompletableFuture`| ใช่ |
| ประเภทสคริปต์ | วนซ้ำเหตุการณ์ | สัญญา`async/await`| ไม่ (เธรดเดียว) |
| ซี | กระทู้ POSIX | `pthread`, OpenMP | ใช่ (ซิงค์ด้วยตนเอง) |
| ซี++ | เธรด OS | `std::thread`,`std::async`, โครูทีน | ใช่ (ซิงค์ด้วยตนเอง) |
| ซี# | async/รอ | `Task`,`async/await`,`Parallel`| ใช่ |
| ทับทิม | GVL + เส้นใย | `Thread`,`Fiber`,`Ractor`(3.0+) | ใช่ (GVL) Ractor: ไม่ |
| สวิฟท์ | นักแสดง | `async/await`, นักแสดง,`Sendable`| ไม่ (การแยกตัวนักแสดง) |
| คอตลิน | โครูทีน | `suspend`,`launch`,`async`| ขึ้นอยู่กับผู้มอบหมายงาน |
| PHP | อิงตามกระบวนการ | `pcntl_fork`, ไฟเบอร์ (8.1+) | ไม่ (แยกกระบวนการ) |
| สกาล่า | เธรด JVM | `Future`, นักแสดง Akka, ZIO, Cats Effect | ใช่ (JVM) |
| ฮาสเคล | กระทู้สีเขียว | `forkIO`, STM,`async`| ใช่ (STM เพื่อความปลอดภัย) |
| หลัว | โครูทีน | `coroutine.create/resume/yield`| ไม่ (สหกรณ์) |
| อาร์ | ลำดับ + ขนาน | `parallel`,`future`| ไม่ (แยกกระบวนการ) |
| จูเลีย | งาน + เธรด | `@async`,`@threads`,`Distributed`| ใช่ (ประเภทเธรดที่ปลอดภัย) |
| โผ | แยก | `Isolate`,`async/await`| ไม่ (ส่งข้อความ) |
| เพิร์ล | ด้าย + ส้อม | `threads`,`fork`| ใช่ (เธรด) |
| MATLAB | สระคู่ขนาน | `parfor`,`spmd`,`gpuArray`| ไม่ (คนงาน) |
| เอสแอลแอล | ไม่มี | ฐานข้อมูลจัดการการทำงานพร้อมกัน (MVCC, ล็อค) | ไม่มี |
| เชลล์ | กระบวนการพื้นหลัง | `&`,`wait`,`xargs -P`| ไม่ (แยกกระบวนการ) |
| ฟอร์ทราน | Coarrays + OpenMP | `coarray`,`do concurrent`, OpenMP | ใช่ (หน่วยความจำที่ใช้ร่วมกัน) |
| เอด้า | งาน + ป้องกัน | `task`,`protected object`, นัดพบ | ใช่ (วัตถุที่ได้รับการคุ้มครอง) |
| ภาษาโคบอล | ไม่มี | การประมวลผลเป็นชุด ไม่มีการทำงานพร้อมกันแบบเนทิฟ | ไม่มี |
| อารัมภบท | ไม่มี | ตามลำดับ (การใช้งานบางอย่างมีเธรด) | ไม่มี |
| กระเพื่อม/Clojure | ตัวแทน STM + | `future`,`promise`,`core.async`, STM | Clojure: STM (อ้างอิง, อะตอม) |
| เออร์ลัง/Elixir | นายแบบนักแสดง | `spawn`การส่งข้อความ`receive`| ไม่ (ส่งข้อความ) |
| โอแคมล์ | โดเมน + เอฟเฟกต์ | `Domain.spawn`ตัวจัดการเอฟเฟกต์ (5.0+) | ไม่ (โดเมน) |
| การประกอบ | ไม่มี | ขึ้นอยู่กับระบบปฏิบัติการ (การขัดจังหวะ การเรียกระบบ) | ไม่มี |
| เดลฟี | กระทู้ | `TThread`,`TTask`| ใช่ (ซิงค์ด้วยตนเอง) |
| เกา | ขับเคลื่อนด้วยเหตุการณ์ | `when green flag clicked`, ออกอากาศ | ไม่ (การแยกสไปรท์) |
| วีบี | async/รอ | `Async/Await`,`Task`| ใช่ |
## การสร้างกระทู้
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

## รูปแบบการทำงานพร้อมกันที่สำคัญ
### ผู้ผลิต-ผู้บริโภค
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

### Mutex / การล็อค
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

## ตารางสรุป
| กระบวนทัศน์ | ภาษา |
|----------|-----------|
| **เธรด OS + หน่วยความจำที่ใช้ร่วมกัน** | C, C++, Java, C#, Fortran, Delphi, VB |
| **GIL/ล็อค + เธรด** | หลาม, รูบี้, เพิร์ล |
| **โกรูทีน + ช่อง** | ไป |
| **นายแบบนางแบบ** | Erlang, Elixir, Scala (Akka), Ruby (Ractor) |
| **async/await + ลูปเหตุการณ์** | JavaScript, TypeScript, Rust, Swift, C#, Kotlin, Dart |
| **STM (หน่วยความจำธุรกรรมซอฟต์แวร์)** | Haskell, Clojure |
| **โครูทีน (สหกรณ์)** | ลัวะ, คอตลิน |
| **แยก (ไม่มีหน่วยความจำที่ใช้ร่วมกัน)** | โผ, JavaScript, TypeScript |
| **ไม่มีการทำงานพร้อมกันแบบเนทิฟ** | COBOL, อารัมภบท, รอยขีดข่วน, SQL |