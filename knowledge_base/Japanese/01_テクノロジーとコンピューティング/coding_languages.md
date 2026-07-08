<!-- 
This file was automatically translated from English to Japanese.
Source: coding_languages.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# プログラミング言語

## Python

Python は高レベル、インタプリタ型、動的型付けの汎用プログラミング言語です。可読性を重視し、インデントをブロックの区切りとして使用します。

### 構文の基本

```python
# 変数と型
name: str = "Alice"
age: int = 30
score: float = 9.5
active: bool = True

# 条件分岐
if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("child")

# ループ
for i in range(5):
    print(i)

while active:
    active = False
```

### 関数と型ヒント

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

### リスト内包表記

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### クラスと OOP

```python
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says woof"
```

### 一般的なパターン

- ファイル I/O には `with open(path) as f:` を使用
- `%` や `.format()` よりも f-strings (`f"hello {name}"`) を推奨
- データのみのクラスには `dataclasses.dataclass` を使用
- ファイルパスには `os.path` の代わりに `pathlib.Path` を使用

### ツール

- `pip install <package>` でパッケージをインストール
- `python -m venv .venv && source .venv/bin/activate` で仮想環境を作成
- `pip freeze > requirements.txt` で依存関係を保存
- `pip install -r requirements.txt` で依存関係を復元
- `pyproject.toml` がモダンなプロジェクト設定の標準

---

## JavaScript

JavaScript はウェブの主要言語です。ブラウザ上および Node.js を介してサーバー上で実行されます。動的型付けでプロトタイプベースです。

### モダン構文 (ES6+)

```javascript
// Variable declarations
const PI = 3.14159;
let counter = 0;

// Arrow functions
const add = (a, b) => a + b;

// Template literals
const greet = name => `Hello, ${name}!`;

// Destructuring
const { x, y } = point;
const [first, ...rest] = array;

// Spread
const merged = { ...defaults, ...overrides };
```

### 非同期プログラミング

```javascript
// Promises
fetch("/api/data")
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));

// Async / await
async function loadUser(id) {
  try {
    const res = await fetch(`/users/${id}`);
    return await res.json();
  } catch (err) {
    console.error(err);
  }
}
```

### 配列メソッド

```javascript
const doubled = [1, 2, 3].map(n => n * 2);
const evens   = [1, 2, 3, 4].filter(n => n % 2 === 0);
const sum     = [1, 2, 3].reduce((acc, n) => acc + n, 0);
```

### DOM 操作

```javascript
const btn = document.getElementById("submit");
btn.addEventListener("click", () => {
  document.querySelector(".result").textContent = "Done!";
});
```

### ツール

- `npm init -y` でプロジェクトを初期化
- `npm install <package>` で依存関係を追加
- `npm run <script>` で `package.json` に定義されたスクリプトを実行
- `node index.js` で Node.js スクリプトを実行

---

## TypeScript

TypeScript は JavaScript の静的型付けスーパーセットで、通常の JavaScript にコンパイルされます。型アノテーション、インターフェース、ジェネリクス、列挙型を追加します。

### 型アノテーション

```typescript
let username: string = "alice";
let count: number = 42;
let flags: boolean[] = [true, false];
let anything: unknown = "could be anything";
```

### インターフェースと型

```typescript
interface User {
  id: number;
  name: string;
  email?: string;   // optional property
}

type Status = "active" | "inactive" | "banned";
```

### ジェネリクス

```typescript
function identity<T>(value: T): T {
  return value;
}

function first<T>(arr: T[]): T | undefined {
  return arr[0];
}
```

### クラスとアクセス修飾子

```typescript
class Counter {
  private count: number = 0;

  increment(): void {
    this.count++;
  }

  get value(): number {
    return this.count;
  }
}
```

### tsconfig.json の基本

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "CommonJS",
    "strict": true,
    "outDir": "dist",
    "rootDir": "src"
  }
}
```

### ツール

- `npm install -g typescript` でコンパイラをインストール
- `tsc` でプロジェクトをコンパイル
- `ts-node src/index.ts` で TypeScript を直接実行

---

## Rust

Rust は安全性、速度、並行性に焦点を当てたシステムプログラミング言語です。所有権システムにより、コンパイル時にメモリー安全性のバグを防止します。

### 所有権と借用

Rust では、すべての値は正確に 1 つの所有者を持ちます。所有者がスコープを出ると、その値はドロップされます。借用は、所有権を移譲せずに参照を許可します。

```rust
fn main() {
    let s = String::from("hello");  // s owns the string
    let len = calculate_length(&s); // borrow s
    println!("{} has length {}", s, len); // s still valid
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```

可変借用（`&mut T`）は、同時に他の借用が存在しないことを要求します。

### ライフタイム

ライフタイムは、参照が指し先のデータより長く存続しないことを保証します。

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

### 列挙型とパターンマッチング

```rust
enum Shape {
    Circle(f64),
    Rectangle(f64, f64),
}

fn area(shape: &Shape) -> f64 {
    match shape {
        Shape::Circle(r)       => std::f64::consts::PI * r * r,
        Shape::Rectangle(w, h) => w * h,
    }
}
```

### エラーハンドリング

```rust
use std::fs;

fn read_file(path: &str) -> Result<String, std::io::Error> {
    fs::read_to_string(path)
}

fn main() {
    match read_file("data.txt") {
        Ok(content) => println!("{}", content),
        Err(e)      => eprintln!("Error: {}", e),
    }
}
```

`?` 演算子は、`Result` を返す関数内でエラーを自動的に伝播します。

### ツール (Cargo)

- `cargo new project_name` で新しいプロジェクトを作成
- `cargo build` でコンパイル
- `cargo run` でコンパイルして実行
- `cargo test` でテストを実行
- `cargo add <crate>` で `Cargo.toml` に依存関係を追加
- `cargo fmt` でコードをフォーマット。`cargo clippy` でリント

---

## Go

Go（Golang）は、シンプルさと高性能な並行プログラムのために設計された静的型付けのコンパイル言語です。

### 基本

```go
package main

import "fmt"

func main() {
    name := "world"          // short variable declaration
    fmt.Printf("Hello, %s!\n", name)
}
```

### 関数と複数の戻り値

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}
```

### インターフェース

```go
type Speaker interface {
    Speak() string
}

type Dog struct{ Name string }

func (d Dog) Speak() string { return d.Name + " says woof" }
```

インターフェースのすべてのメソッドを実装する型は、明示的な宣言なしにそのインターフェースを満たします。

### ゴルーチンとチャネル

```go
func worker(id int, jobs <-chan int, results chan<- int) {
    for j := range jobs {
        results <- j * j
    }
}

func main() {
    jobs    := make(chan int, 5)
    results := make(chan int, 5)

    go worker(1, jobs, results)

    for i := 1; i <= 5; i++ {
        jobs <- i
    }
    close(jobs)

    for i := 0; i < 5; i++ {
        fmt.Println(<-results)
    }
}
```

### Defer

```go
func readFile(path string) error {
    f, err := os.Open(path)
    if err != nil {
        return err
    }
    defer f.Close()   // runs when function returns
    // … process f …
    return nil
}
```

### ツール

- `go mod init module/name` でモジュールを初期化
- `go get ./...` で依存関係をダウンロード
- `go build ./...` でコンパイル
- `go test ./...` でテストを実行
- `go fmt ./...` でコードをフォーマット
- `go vet ./...` で一般的なミスをチェック

---

## C と C++

C は低レベルのコンパイル型プロシージャル言語です。C++ は C をクラス、テンプレート、標準テンプレートライブラリ（STL）で拡張します。

### C の基本

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int x = 42;
    printf("x = %d\n", x);

    /* Dynamic memory */
    int *arr = malloc(5 * sizeof(int));
    for (int i = 0; i < 5; i++) arr[i] = i;
    free(arr);   /* always free what you malloc */

    return 0;
}
```

### ポインタ

ポインタは別の変数のメモリアドレスを格納します。`*ptr` で参照外しを行い、`&var` でアドレスを取得します。

```c
int a = 10;
int *p = &a;
*p = 20;   /* a is now 20 */
```

### C++ クラスと RAII

```cpp
#include <string>
#include <iostream>

class Person {
public:
    Person(std::string name, int age) : name_(name), age_(age) {}

    void greet() const {
        std::cout << "Hi, I'm " << name_ << "\n";
    }

private:
    std::string name_;
    int age_;
};
```

RAII（Resource Acquisition Is Initialization）は、リソースのライフタイムをオブジェクトのライフタイムに結びつけ、デストラクタで自動的にクリーンアップが行われることを保証します。

### STL コンテナ

```cpp
#include <vector>
#include <map>
#include <algorithm>

std::vector<int> v = {3, 1, 4, 1, 5, 9};
std::sort(v.begin(), v.end());

std::map<std::string, int> scores;
scores["Alice"] = 95;
scores["Bob"]   = 87;
```

### モダン C++（C++17 / C++20）のハイライト

- `auto` 型推論
- 範囲ベースの `for` ループ：`for (auto& item : container)`
- スマートポインタ：`std::unique_ptr`、`std::shared_ptr` — 生の `new`/`delete` は避ける
- 構造化束縛：`auto [key, val] = pair;`
- `std::optional`、`std::variant`、`std::string_view`

### コンパイル

- `gcc main.c -o main` で C をコンパイル
- `g++ -std=c++20 -Wall main.cpp -o main` で C++ をコンパイル
- `make` は `Makefile` を介してマルチファイルビルドを自動化
- `cmake` は大規模プロジェクトの標準ビルドシステムジェネレーター

---

## Swift

Swift は Apple が iOS、macOS、watchOS、tvOS 用に開発したモダンな静的型付けプログラミング言語です。Linux でも利用可能です。

### 基本

```swift
let greeting = "Hello, world!"   // constant (immutable)
var counter  = 0                  // variable (mutable)
counter += 1

let pi: Double = 3.14159
```

### オプショナル

オプショナル（`T?`）は、値が存在する場合としない場合の両方を表します。

```swift
var name: String? = nil
name = "Alice"

// Safe unwrapping
if let n = name {
    print("Hello, \(n)")
}

// Nil-coalescing
let display = name ?? "Guest"

// Optional chaining
let length = name?.count
```

### 関数とクロージャ

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let multiply: (Int, Int) -> Int = { $0 * $1 }
```

### クラスと構造体

Swift にはクラス（参照型）と構造体（値型）の両方があります。シンプルなデータモデルには構造体を推奨します。

```swift
struct Point {
    var x: Double
    var y: Double
}

class Vehicle {
    var speed: Double = 0.0
    func accelerate(by amount: Double) { speed += amount }
}
```

### プロトコル

```swift
protocol Describable {
    var description: String { get }
}

struct Cat: Describable {
    var name: String
    var description: String { "Cat named \(name)" }
}
```

### Codable（JSON エンコード/デコード）

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

let json = """{"id":1,"name":"Alice","email":"a@example.com"}"""
let user = try JSONDecoder().decode(User.self, from: json.data(using: .utf8)!)
```

### SwiftUI の基本

```swift
import SwiftUI

struct ContentView: View {
    @State private var count = 0

    var body: some View {
        VStack {
            Text("Count: \(count)")
            Button("Increment") { count += 1 }
        }
    }
}
```

### ツール

- `swift build` で Swift Package Manager プロジェクトをコンパイル
- `swift run` でプロジェクトを実行
- `swift test` でテストを実行
- `swift package init --type executable` で新しい実行可能プロジェクトを作成
- Xcode は Apple プラットフォーム開発の主要 IDE

---

## コーディングの基礎（言語に依存しない）

### 問題解決のワークフロー

1. コードを書く前に、入力、出力、制約を定義する
2. タスクをより小さなサブ問題に分割する
3. シンプルで正しいソリューションから始め、必要に応じて最適化する
4. テスト、エッジケース、現実的な入力で検証する

### 基本的なデータ構造

- **配列/リスト**: 順序付きコレクション、高速なインデックス読み取り
- **ハッシュマップ/辞書**: キー値ストア、平均 O(1) のルックアップ
- **セット**: 一意の値、メンバーシップチェックに便利
- **スタック**: LIFO（後入れ先出し）、パーシングや再帰で一般的
- **キュー**: FIFO（先入れ先出し）、スケジューリングや BFS に便利
- **木/グラフ**: 階層的およびネットワークスタイルの関係

### アルゴリズムの計算量（Big O）

- Big O は、実行時間またはメモリが入力サイズとともにどのように増加するかを記述する
- 代表的なコスト：
  - O(1): 定数時間のルックアップ（例：ハッシュマップアクセス）
  - O(log n): 二分探索
  - O(n): データの単一パス
  - O(n log n): 効率的なソート
  - O(n²): 同サイズの入力に対するネステッドループ
- プロファイリングでボトルネックが示されない限り、明確で保守しやすいコードを推奨

### デバッグの原則

- まずバグを確実に再現する
- 失敗するケースを最小化して原因を特定する
- ログ、入力、仮定を検証する
- テスト中は一度に 1 つの変数だけを変更する
- 同じバグが戻らないように回帰テストを追加する

### テストのピラミッド

- **単体テスト**: 小さなロジックユニットの高速で焦点を絞ったチェック
- **統合テスト**: モジュール/サービス間の相互作用を検証
- **エンドツーエンドテスト**: 現実的な環境でユーザーフローを検証
- バランスの取れたスイートは、多くの単体テストと少数の遅いエンドツーエンドテストを持つ

### コード品質のプラクティス

- 意味のある名前と小さく焦点を絞った関数を使用する
- 実用的な場合は純粋な関数（副作用が少ない）を推奨
- モジュールを凝集させ、インターフェースを明示的に保つ
- 一貫性のためにリンター/フォーマッターを使用する
- 正しさ、明確さ、セキュリティのためにコードをレビューする

### 開発者のためのセキュリティ基本

- 外部入力を検証しサニタイズする
- SQL インジェクションを防ぐためにパラメータ化クエリを使用する
- パスワードは強力なハッシュアルゴリズム（例：Argon2、bcrypt）で保存する
- ソースコードにシークレットを埋め込まない
- 認証情報とサービスには最小権限を適用する
