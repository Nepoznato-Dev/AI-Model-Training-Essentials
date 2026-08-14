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
# 언어 간 비교 — 동시성 및 병렬성
## 동시성 모델 개요
| 언어 | 모델 | 주요 메커니즘 | 공유 메모리? |
|------------|---------|---------------|---|
| 파이썬 | GIL + 스레드 |  `threading`,`asyncio`| 예(GIL은 병렬성을 제한함) |
| 자바스크립트 | 이벤트 루프 | 약속,`async/await`| 아니요(단일 스레드) |
| 녹 | 소유권 + 보내기/동기화 | `std::thread`,`async/await`, 채널 | 컴파일 시간 안전성 |
| 이동 | 고루틴 | `go func()`, 채널 | 아니요(메시지 전달) |
| 자바 | OS 스레드 | `Thread`,`ExecutorService`,`CompletableFuture`| 예 |
| 타입스크립트 | 이벤트 루프 | 약속,`async/await`| 아니요(단일 스레드) |
| 다 | POSIX 스레드 |  `pthread`, 오픈MP | 예(수동 동기화) |
| C++ | OS 스레드 | `std::thread`,`std::async`, 코루틴 | 예(수동 동기화) |
| C# | 비동기/대기 | `Task`,`async/await`,`Parallel`| 예 |
| 루비 | GVL + 섬유 | `Thread`,`Fiber`,`Ractor`(3.0+) | 예(GVL), Ractor: 아니요 |
| 스위프트 | 배우 | `async/await`, 배우,`Sendable`| 아니요(배우 격리) |
| 코틀린 | 코루틴 | `suspend`,`launch`,`async`| 디스패처에 따라 다름 |
| PHP | 프로세스 기반 | `pcntl_fork`, 섬유(8.1+) | 아니요(별도의 프로세스) |
| 스칼라 | JVM 스레드 | `Future`, 아카배우들, ZIO, 캣츠이펙트 | 예(JVM) |
| 하스켈 | 녹색 스레드 |  `forkIO`, STM,`async`| 있음(안전을 위한 STM) |
| 루아 | 코루틴 | `coroutine.create/resume/yield`| 아니요(협동) |
| R | 순차 + 병렬 | `parallel`,`future`| 아니요(별도의 프로세스) |
| 줄리아 | 작업 + 스레드 | `@async`,`@threads`,`Distributed`| 예(스레드로부터 안전한 유형) |
| 다트 | 분리 | `Isolate`,`async/await`| 아니요(메시지 전달) |
| 펄 | 스레드 + 포크 | `threads`,`fork`| 예(스레드) |
| MATLAB | 병렬 풀 | `parfor`,`spmd`,`gpuArray`| 아니오 (근로자) |
| SQL | 해당 없음 | 데이터베이스 처리 동시성(MVCC, 잠금) | 해당 없음 |
| 쉘 | 백그라운드 프로세스 | `&`,`wait`,`xargs -P`| 아니요(별도의 프로세스) |
| 포트란 | Coarrays + OpenMP | `coarray`,`do concurrent`, 오픈MP | 예(공유 메모리) |
| 에이다 | 작업 + 보호됨 | `task`,`protected object`, 랑데부 | 예(보호 개체) |
| 코볼 | 해당 없음 | 일괄 처리, 기본 동시성 없음 | 해당 없음 |
| 프롤로그 | 해당 없음 | 순차(일부 구현에는 스레드가 있음) | 해당 없음 |
| 리스프/클로저 | STM + 에이전트 | `future`,`promise`,`core.async`, STM | 클로저: STM(참조, 원자) |
| 얼랭/엘릭서 | 배우 모델 | `spawn`, 메시지 전달,`receive`| 아니요(메시지 전달) |
| 오캠 | 도메인 + 효과 | `Domain.spawn`, 효과 핸들러(5.0+) | 아니요(도메인) |
| 조립 | 해당 없음 | OS 종속(인터럽트, 시스템 호출) | 해당 없음 |
| 델파이 | 스레드 | `TThread`,`TTask`| 예(수동 동기화) |
| 스크래치 | 이벤트 중심 |  `when green flag clicked`, 방송 | 아니요(스프라이트 격리) |
| VB | 비동기/대기 | `Async/Await`,`Task`| 예 |
## 스레드 생성
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

## 주요 동시성 패턴
### 생산자-소비자
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

### 뮤텍스/잠금
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

## 요약표
| 패러다임 | 언어 |
|----------|-----------|
| **OS 스레드 + 공유 메모리** | C, C++, 자바, C#, 포트란, 델파이, VB |
| **GIL/잠금 + 스레드** | 파이썬, 루비, 펄 |
| **고루틴 + 채널** | 이동 |
| **배우 모델** | Erlang, Elixir, Scala(Akka), Ruby(Ractor) |
| **비동기/대기 + 이벤트 루프** | JavaScript, TypeScript, Rust, Swift, C#, Kotlin, Dart |
| **STM(소프트웨어 트랜잭션 메모리)** | 하스켈, 클로저 |
| **코루틴(협동)** | 루아, 코틀린 |
| **분리(공유 메모리 없음)** | 다트, 자바스크립트, 타입스크립트 |
| **기본 동시성 없음** | COBOL, 프롤로그, 스크래치, SQL |