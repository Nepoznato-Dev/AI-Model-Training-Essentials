<!-- 
このファイルは英語から日本語に自動翻訳されました。
ソース：coding_languages.md
注：技術用語、コード例、固有名詞は英語のままの場合があります。
精度の向上については、プルリクエストを通じて編集を貢献してください。
-->

# プログラミング言語

## Python

Python は、高レベル、インタプリタ型、動的型付けの汎用プログラミング言語です。可読性を重視し、ブロック区切りとして意味のあるインデントを使用します。

### 基本構文

```python
# 変数と型
name: str = "Alice"
age: int = 30
score: float = 9.5
active: bool = True

# 条件分岐
if age >= 18:
    print("大人")
elif age >= 13:
    print("ティーン")
else:
    print("子供")

# ループ
for i in range(5):
    print(i)

while active:
    active = False
```

### 関数と型アノテーション

```python
def greet(name: str, times: int = 1) -> str:
    return (f"こんにちは、{name}さん！ " * times).strip()
```

### リスト内包表記

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### クラスと OOP

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def introduce(self) -> str:
        return f"私の名前は{self.name}で、{self.age}歳です。"
```

## JavaScript

JavaScript は、インタプリタ型、オブジェクト指向、イベント駆動のプログラミング言語で、主にクライアント側およびサーバー側の Web 開発に使用されます。

### 基本構文

```javascript
// 変数と型
let name = "Alice";
const age = 30;
let score = 9.5;
let active = true;

// 条件分岐
if (age >= 18) {
    console.log("大人");
} else if (age >= 13) {
    console.log("ティーン");
} else {
    console.log("子供");
}

// ループ
for (let i = 0; i < 5; i++) {
    console.log(i);
}

while (active) {
    active = false;
}
```

### 関数

```javascript
function greet(name, times = 1) {
    return `こんにちは、${name}さん！ `.repeat(times).trim();
}

// アロー関数
const greetArrow = (name, times = 1) => {
    return `こんにちは、${name}さん！ `.repeat(times).trim();
};
```

### 配列操作

```javascript
const numbers = [1, 2, 3, 4, 5];
const squares = numbers.map(x => x ** 2);
const evens = numbers.filter(x => x % 2 === 0);
const sum = numbers.reduce((acc, x) => acc + x, 0);
```

## Java

Java は、コンパイル型、オブジェクト指向、プラットフォーム非依存のプログラミング言語で、エンタープライズアプリケーションや Android 開発で広く使用されています。

### 基本構文

```java
// 変数と型
String name = "Alice";
int age = 30;
double score = 9.5;
boolean active = true;

// 条件分岐
if (age >= 18) {
    System.out.println("大人");
} else if (age >= 13) {
    System.out.println("ティーン");
} else {
    System.out.println("子供");
}

// ループ
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

while (active) {
    active = false;
}
```

### クラスと OOP

```java
public class Person {
    private String name;
    private int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String introduce() {
        return "私の名前は " + name + " で、" + age + "歳です。";
    }
}
```

## C++

C++ は、コンパイル型、高性能、多用途のプログラミング言語で、システム、ビデオゲーム、クリティカルなアプリケーションに使用されます。

### 基本構文

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    // 変数と型
    string name = "Alice";
    int age = 30;
    double score = 9.5;
    bool active = true;
    
    // 条件分岐
    if (age >= 18) {
        cout << "大人" << endl;
    } else if (age >= 13) {
        cout << "ティーン" << endl;
    } else {
        cout << "子供" << endl;
    }
    
    // ループ
    for (int i = 0; i < 5; i++) {
        cout << i << endl;
    }
    
    while (active) {
        active = false;
    }
    
    return 0;
}
```

## コーディングの基礎（言語非依存）

プログラミングの基本概念はすべての言語に共通しています：

- **変数**: 名前付きデータストレージ
- **データ型**: データの性質の定義（数値、テキスト、ブール値など）
- **制御構造**: 条件分岐（if/else）とループ（for、while）
- **関数**: 再利用可能なコードブロック
- **データ構造**: 配列、リスト、辞書、セット
- **オブジェクト指向プログラミング**: クラス、オブジェクト、継承、ポリモーフィズム
- **エラーハンドリング**: Try/catch、例外
- **入出力**: データの読み書き

これらの基本概念は、選択されたプログラミング言語に関係なく適用されます。これらの基礎をマスターすることで、新しい言語をより簡単に学ぶことができます。
