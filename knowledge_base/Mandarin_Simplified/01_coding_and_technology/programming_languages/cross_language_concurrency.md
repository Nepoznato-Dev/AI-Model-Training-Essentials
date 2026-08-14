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
# 跨语言比较——并发与并行
## 并发模型概述
|语言 |型号|关键机制|共享内存？ |
|----------|------|----------------|----------------|
|蟒蛇 | GIL + 线程 | `threading`,`asyncio`|是（GIL 限制并行性）|
| JavaScript |事件循环|承诺，`async/await` |否（单线程）|
|铁锈|所有权+发送/同步|  `std::thread`、`async/await`、通道 |编译时安全 |
|去 | Goroutines |  `go func()`，频道 |否（消息传递）|
|爪哇 |操作系统线程 |  `Thread`、`ExecutorService`、`CompletableFuture` |是的 |
|打字稿 |事件循环|承诺，`async/await` |否（单线程）|
| C | POSIX 线程 |  `pthread`，OpenMP |是（手动同步）|
| C++ |操作系统线程 | `std::thread`、`std::async`、协程 |是（手动同步）|
| C# |异步/等待 |  `Task`、`async/await`、`Parallel` |是的 |
|红宝石 | GVL + 纤维 |  `Thread`、`Fiber`、`Ractor` (3.0+) |是（GVL），Ractor：否 |
|斯威夫特 |演员 | `async/await`, 演员,`Sendable`|否（演员隔离）|
|科特林 |协程 |  `suspend`、`launch`、`async` |取决于调度员 |
| PHP |基于流程|  `pcntl_fork`，纤维（8.1+）|否（单独的进程）|
|斯卡拉 | JVM 线程 |  `Future`、Akka 演员、ZIO、猫效果 |是（JVM）|
|哈斯克尔 |绿色线程|  `forkIO`、STM、`async` |是（STM 为了安全）|
|卢阿 |协程 | `coroutine.create/resume/yield`|否（合作）|
|右 |顺序+并行|  `parallel`、`future` |否（单独的进程）|
|朱莉娅 |任务+线程|  `@async`、`@threads`、`Distributed` |是（线程安全类型）|
|飞镖 |隔离 |  `Isolate`、`async/await` |否（消息传递）|
|珀尔|线程+叉|  `threads`、`fork` |是（ithreads）|
| MATLAB |平行池|  `parfor`、`spmd`、`gpuArray` |否（工人）|
| SQL |不适用 |数据库处理并发（MVCC、锁）|不适用 |
|壳牌|后台进程|  `&`、`wait`、`xargs -P` |否（单独的进程）|
|语言 | Coarrays + OpenMP |  `coarray`、`do concurrent`、OpenMP |是（共享内存）|
|艾达 |任务+受保护| `task`,`protected object`, 会合 |是（受保护对象）|
|科博尔 |不适用 |批处理，无原生并发 |不适用 |
|序言|不适用 |顺序（某些实现有线程）|不适用 |
| Lisp/Clojure | STM+代理商|  `future`、`promise`、`core.async`、STM | Clojure：STM（引用、原子）|
| Erlang/Elixir |演员模型| `spawn`，消息传递，`receive` |否（消息传递）|
| OCaml |领域+效果| `Domain.spawn`，效果处理程序 (5.0+) |否（域）|
|组装|不适用 |依赖于操作系统（中断、系统调用）|不适用 |
|德尔福|主题 |  `TThread`、`TTask` |是（手动同步）|
|刮刮|事件驱动|  `when green flag clicked`，广播|否（精灵隔离）|
| VB |异步/等待 |  `Async/Await`、`Task` |是的 |
## 线程创建
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

## 关键并发模式
### 生产者-消费者
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

### 互斥/锁定
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

## 汇总表
|范式|语言 |
|----------|------------|
| **操作系统线程 + 共享内存** | C、C++、Java、C#、Fortran、Delphi、VB |
| **GIL/锁 + 线程** | Python、Ruby、Perl |
| **Goroutine + 通道** |去 |
| **演员模特** | Erlang、Elixir、Scala (Akka)、Ruby (Ractor) |
| **异步/等待+事件循环** | JavaScript、TypeScript、Rust、Swift、C#、Kotlin、Dart |
| **STM（软件事务内存）** | Haskell、Clojure |
| **协程（合作）** | Lua、Kotlin |
| **隔离（无共享内存）** | Dart、JavaScript、TypeScript |
| **没有本机并发** | COBOL、Prolog、Scratch、SQL |