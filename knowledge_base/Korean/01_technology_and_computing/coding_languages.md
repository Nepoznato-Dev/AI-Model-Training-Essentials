<!-- 
이 파일은 영어에서 한국어로 자동 번역되었습니다.
소스: coding_languages.md
참고: 기술 용어, 코드 예제 및 고유 명사는 영어로 남을 수 있습니다.
정확성 개선을 위해 pull request 를 통해 편집을 기여해 주세요.
-->

# 프로그래밍 언어

## Python

Python 은 고수준, 인터프리터 방식, 동적 타입의 범용 프로그래밍 언어입니다. 가독성을 중시하며 블록 구분자로 의미 있는 들여쓰기를 사용합니다.

### 기본 문법

```python
# 변수와 타입
name: str = "Alice"
age: int = 30
score: float = 9.5
active: bool = True

# 조건문
if age >= 18:
    print("성인")
elif age >= 13:
    print("청소년")
else:
    print("어린이")

# 루프
for i in range(5):
    print(i)

while active:
    active = False
```

### 함수와 타입 주석

```python
def greet(name: str, times: int = 1) -> str:
    return (f"안녕하세요, {name}님! " * times).strip()
```

### 리스트 컴프리헨션

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### 클래스와 OOP

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def introduce(self) -> str:
        return f"제 이름은 {self.name} 이고, {self.age} 세입니다."
```

## JavaScript

JavaScript 는 인터프리터 방식, 객체 지향, 이벤트 기반의 프로그래밍 언어로, 주로 클라이언트 측 및 서버 측 웹 개발에 사용됩니다.

### 기본 문법

```javascript
// 변수와 타입
let name = "Alice";
const age = 30;
let score = 9.5;
let active = true;

// 조건문
if (age >= 18) {
    console.log("성인");
} else if (age >= 13) {
    console.log("청소년");
} else {
    console.log("어린이");
}

// 루프
for (let i = 0; i < 5; i++) {
    console.log(i);
}

while (active) {
    active = false;
}
```

### 함수

```javascript
function greet(name, times = 1) {
    return `안녕하세요, ${name}님! `.repeat(times).trim();
}

// 화살표 함수
const greetArrow = (name, times = 1) => {
    return `안녕하세요, ${name}님! `.repeat(times).trim();
};
```

### 배열 조작

```javascript
const numbers = [1, 2, 3, 4, 5];
const squares = numbers.map(x => x ** 2);
const evens = numbers.filter(x => x % 2 === 0);
const sum = numbers.reduce((acc, x) => acc + x, 0);
```

## Java

Java 는 컴파일 방식, 객체 지향, 플랫폼 독립적인 프로그래밍 언어로, 엔터프라이즈 애플리케이션과 Android 개발에서 널리 사용됩니다.

### 기본 문법

```java
// 변수와 타입
String name = "Alice";
int age = 30;
double score = 9.5;
boolean active = true;

// 조건문
if (age >= 18) {
    System.out.println("성인");
} else if (age >= 13) {
    System.out.println("청소년");
} else {
    System.out.println("어린이");
}

// 루프
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

while (active) {
    active = false;
}
```

### 클래스와 OOP

```java
public class Person {
    private String name;
    private int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String introduce() {
        return "제 이름은 " + name + " 이고, " + age + "세입니다.";
    }
}
```

## C++

C++ 는 컴파일 방식, 고성능, 다목적 프로그래밍 언어로, 시스템, 비디오 게임, 중요한 애플리케이션에 사용됩니다.

### 기본 문법

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    // 변수와 타입
    string name = "Alice";
    int age = 30;
    double score = 9.5;
    bool active = true;
    
    // 조건문
    if (age >= 18) {
        cout << "성인" << endl;
    } else if (age >= 13) {
        cout << "청소년" << endl;
    } else {
        cout << "어린이" << endl;
    }
    
    // 루프
    for (int i = 0; i < 5; i++) {
        cout << i << endl;
    }
    
    while (active) {
        active = false;
    }
    
    return 0;
}
```

## 코딩의 기초 (언어 비종속)

프로그래밍의 기본 개념은 모든 언어에 공통적입니다:

- **변수**: 이름 붙은 데이터 저장소
- **데이터 타입**: 데이터의 성질 정의 (숫자, 텍스트, 부울 등)
- **제어 구조**: 조건문 (if/else) 과 루프 (for, while)
- **함수**: 재사용 가능한 코드 블록
- **데이터 구조**: 배열, 리스트, 딕셔너리, 집합
- **객체 지향 프로그래밍**: 클래스, 객체, 상속, 다형성
- **오류 처리**: Try/catch, 예외
- **입출력**: 데이터 읽기 및 쓰기

이러한 기본 개념은 선택한 프로그래밍 언어와 관계없이 적용됩니다. 이러한 기초를 마스터하면 새로운 언어를 더 쉽게 배울 수 있습니다.
