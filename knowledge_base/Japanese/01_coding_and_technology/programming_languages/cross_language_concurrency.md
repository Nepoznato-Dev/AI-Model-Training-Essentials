---
# Metadata
title: "Cross-Language Comparison — Concurrency & Parallelism"
description: "Side-by-side comparison of concurrency models across 34 programming languages."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# 言語間の比較 — 同時実行性と並列性
## 同時実行モデルの概要
|言語 |モデル |キーの仕組み |共有メモリ? |
|----------|------|------|-----|
|パイソン | GIL + スレッド |  `threading`、`asyncio` |はい (GIL は並列処理を制限します) |
| JavaScript |イベントループ |約束、`async/await` |いいえ (シングルスレッド) |
|さび |所有権 + 送信/同期 | `std::thread`、`async/await`、チャンネル |コンパイル時の安全性 |
|行く |ゴルーチン | `go func()`、チャンネル |いいえ (メッセージパッシング) |
|ジャワ | OS スレッド |  `Thread`、`ExecutorService`、`CompletableFuture` |はい |
|タイプスクリプト |イベントループ |約束、`async/await` |いいえ (シングルスレッド) |
| C | POSIX スレッド |  `pthread`、OpenMP |はい (手動同期) |
| C++ | OS スレッド | `std::thread`、`std::async`、コルーチン |はい (手動同期) |
| C# |非同期/待機 |  `Task`、`async/await`、`Parallel` |はい |
|ルビー | GVL + 繊維 | `Thread`、`Fiber`、`Ractor`(3.0+) |はい (GVL)、ラクター: いいえ |
|スイフト |俳優 | `async/await`、俳優、`Sendable` |いいえ (アクターの分離) |
|コトリン |コルーチン |  `suspend`、`launch`、`async` |ディスパッチャに依存 |
| PHP |プロセスベース | `pcntl_fork`、ファイバー (8.1+) |いいえ (別のプロセス) |
|スカラ座 | JVM スレッド | `Future`、Akka アクター、ZIO、Cats Effect |はい (JVM) |
|ハスケル |緑の糸 |  `forkIO`、STM、`async` |はい (安全のため STM) |
|ルア |コルーチン | `coroutine.create/resume/yield`|いいえ（協力） |
| R |シーケンシャル + パラレル |  `parallel`、`future` |いいえ (別のプロセス) |
|ジュリア |タスク + スレッド |  `@async`、`@threads`、`Distributed` |はい (スレッドセーフなタイプ) |
|ダーツ |分離物 |  `Isolate`、`async/await` |いいえ (メッセージパッシング) |
|パール |スレッド + フォーク |  `threads`、`fork` |はい (ithreads) |
| MATLAB |並列プール |  `parfor`、`spmd`、`gpuArray` |いいえ (労働者) |
| SQL |該当なし |データベースは同時実行性を処理します (MVCC、ロック)。該当なし |
|シェル |バックグラウンドプロセス |  `&`、`wait`、`xargs -P` |いいえ (別のプロセス) |
|フォートラン | CoArray + OpenMP | `coarray`、`do concurrent`、 OpenMP |はい (共有メモリ) |
|エイダ |タスク + 保護された | `task`、`protected object`、ランデブー |はい (保護されたオブジェクト) |
|コボル |該当なし |バッチ処理、ネイティブ同時実行機能なし |該当なし |
|プロローグ |該当なし |シーケンシャル (一部の実装にはスレッドがあります) |該当なし |
| Lisp/Clojure | STM + エージェント |  `future`、`promise`、`core.async`、STM | Clojure: STM (参照、アトム) |
| Erlang/エリクサー |俳優モデル | `spawn`、メッセージパッシング、`receive` |いいえ (メッセージパッシング) |
| OCaml |ドメイン + 効果 | `Domain.spawn`、エフェクト ハンドラー (5.0+) |いいえ (ドメイン) |
|組み立て |該当なし | OS に依存 (割り込み、システム コール) |該当なし |
|デルフィ |スレッド |  `TThread`、`TTask` |はい (手動同期) |
|スクラッチ |イベント駆動型 |  `when green flag clicked`、ブロードキャスト |いいえ (スプライト分離) |
| VB |非同期/待機 |  `Async/Await`、`Task` |はい |
## スレッドの作成
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

## 主要な同時実行パターン
### 生産者と消費者
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

### ミューテックス / ロック
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

## サマリーテーブル
|パラダイム |言語 |
|----------|----------|
| **OS スレッド + 共有メモリ** | C、C++、Java、C#、Fortran、Delphi、VB |
| **GIL/ロック + スレッド** | Python、Ruby、Perl |
| **Goroutine + チャネル** |行く |
| **俳優モデル** | Erlang、Elixir、Scala (Akka)、Ruby (Ractor) |
| **非同期/待機 + イベント ループ** | JavaScript、TypeScript、Rust、Swift、C#、Kotlin、Dart |
| **STM (ソフトウェア トランザクション メモリ)** |ハスケル、Clojure |
| **コルーチン (協調)** | Lua、コトリン |
| **分離 (共有メモリなし)** | Dart、JavaScript、TypeScript |
| **ネイティブ同時実行機能なし** | COBOL、プロローグ、スクラッチ、SQL |