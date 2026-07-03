<!-- 
This file was automatically translated from English to Korean.
Source: python_syntax.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Python 구문 치트시트

빠른 참조를 위한 Python 3.x 구문과 일반적인 패턴.

---

## 기본 구문

### 변수와 데이터 타입
```python
# 변수 할당 (선언 불필요)
x = 5
name = "Alice"
is_active = True
price = 19.99

# 타입 검사
type(x)           # <class 'int'>
isinstance(x, int)  # True

# 타입 변환
int("5")          # 5
str(5)            # "5"
float(5)          # 5.0
bool(1)           # True
```

### 문자열
```python
s = "Hello, World!"

# 슬라이싱
s[0]              # 'H'
s[-1]             # '!'
s[0:5]            # 'Hello'
s[7:]             # 'World!'
s[::-1]           # 문자열 뒤집기

# 메서드
s.lower()         # 'hello, world!'
s.upper()         # 'HELLO, WORLD!'
s.split(",")      # ['Hello', ' World!']
s.replace("World", "Python")
s.strip()         # 공백 제거
f"Value: {x}"     # f-string 형식 지정
```

---

## 제어 흐름

### 조건문
```python
if x > 10:
    print("Greater than 10")
elif x == 10:
    print("Equals 10")
else:
    print("Less than 10")

# 삼항 연산자
result = "yes" if condition else "no"
```

### 반복문
```python
# for 반복문
for i in range(5):      # 0부터 4까지
    print(i)

for item in [1, 2, 3]:
    print(item)

for key, value in dict.items():
    print(key, value)

# while 반복문
while x < 10:
    x += 1

# 반복 제어
break       # 반복문 종료
continue    # 다음 반복으로 건너뜀
else:       # break 없이 반복이 끝나면 실행
```

---

## 데이터 구조

### 리스트
```python
lst = [1, 2, 3, 4, 5]

lst.append(6)           # 끝에 추가
lst.insert(0, 0)        # 지정한 위치에 삽입
lst.remove(3)           # 값으로 삭제
lst.pop()               # 마지막 항목 삭제 후 반환
lst.pop(0)              # 첫 항목 삭제 후 반환
lst.index(2)            # 값의 인덱스 찾기
lst.count(2)            # 등장 횟수 세기
lst.sort()              # 제자리 정렬
sorted(lst)             # 정렬된 복사본 반환
lst.reverse()           # 제자리 뒤집기
lst[1:4]                # 슬라이스
[i*2 for i in lst]      # 리스트 컴프리헨션
```

### 딕셔너리
```python
d = {"name": "Alice", "age": 30}

d["age"]                # 값에 접근
d.get("age", 0)         # 기본값으로 안전하게 접근
d.keys()                # 모든 키 가져오기
d.values()              # 모든 값 가져오기
d.items()               # 키-값 쌍 가져오기
d.update({"city": "NYC"})
del d["age"]            # 키 삭제

{k: v*2 for k, v in d.items()}  # 딕셔너리 컴프리헨션
```

### 집합
```python
s = {1, 2, 3, 3, 4}     # {1, 2, 3, 4} - 중복 제거됨

s.add(5)
s.remove(3)
s.discard(10)           # 있으면 제거 (오류 없음)
s.union({4, 5, 6})      # 집합 결합
s.intersection({2, 3})  # 공통 원소
s.difference({3, 4})    # s 에는 있지만 다른 집합에는 없는 원소
```

### 튜플
```python
t = (1, 2, 3)
t[0]                    # 접근 (불변)
x, y, z = t             # 언패킹
```

---

## 함수

### 정의
```python
def greet(name, greeting="Hello"):
    """독스트링: 함수 설명"""
    return f"{greeting}, {name}!"

# 위치 인자와 키워드 인자로 호출
greet("Alice")
greet("Bob", greeting="Hi")

# 가변 인자
def sum_all(*args):
    return sum(args)

def print_all(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")
```

### 람다 함수
```python
square = lambda x: x ** 2
sorted(lst, key=lambda x: x[1])
```

---

## 클래스

```python
class Person:
    def __init__(self, name, age):
        self.name = name      # 인스턴스 변수
        self.age = age
    
    def greet(self):          # 인스턴스 메서드
        return f"Hi, I'm {self.name}"
    
    @classmethod
    def from_birth_year(cls, name, year):
        age = 2025 - year
        return cls(name, age)
    
    @staticmethod
    def is_adult(age):
        return age >= 18

# 상속
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
```

---

## 파일 입출력

```python
# 파일 읽기
with open("file.txt", "r") as f:
    content = f.read()        # 파일 전체 읽기
    lines = f.readlines()     # 줄 목록으로 읽기

# 파일 쓰기
with open("file.txt", "w") as f:
    f.write("Hello\n")

# 추가 모드
with open("file.txt", "a") as f:
    f.write("More content\n")
```

---

## 예외 처리

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"오류: {e}")
except (TypeError, ValueError):
    print("형식 또는 값 오류")
except Exception as e:
    print(f"일반 오류: {e}")
else:
    print("오류가 발생하지 않았습니다")
finally:
    print("항상 실행됩니다")

# 예외 발생시키기
raise ValueError("Invalid value")
```

---

## 모듈과 import

```python
import math
from datetime import datetime
from collections import defaultdict, Counter
import numpy as np
from mymodule import my_function as mf

# 일반적인 표준 라이브러리 모듈
os, sys, json, re, random, itertools, functools, pathlib
```

---

## 일반적인 패턴

### 리스트 연산
```python
# 필터
evens = [x for x in lst if x % 2 == 0]

# 맵
squares = [x**2 for x in lst]

# zip
list(zip([1, 2], ['a', 'b']))  # [(1, 'a'), (2, 'b')]

# enumerate
for i, val in enumerate(lst):
    print(f"{i}: {val}")
```

### 문자열 연산
```python
# 문자열 목록 결합
", ".join(["a", "b", "c"])  # "a, b, c"

# 문자열 분리
"a,b,c".split(",")          # ['a', 'b', 'c']

# 부분 문자열 확인
"test" in "this is a test"  # True

# 문자열 형식 지정
"{} {}".format("Hello", "World")
f"{value:.2f}"              # 소수점 두 자리
```

### 딕셔너리 연산
```python
# 딕셔너리 병합
{**d1, **d2}
d1 | d2                     # Python 3.9+

# 기본값
d.get("key", default_value)

# 순회
for k, v in d.items():
    pass
```

---

## 내장 함수

```python
len(), str(), int(), float(), bool()
range(), enumerate(), zip()
map(), filter(), reduce()   # reduce from functools
sorted(), reversed()
min(), max(), sum()
abs(), round(), pow()
dir(), help(), type()
isinstance(), issubclass()
any(), all()
```

---

## 빠른 팁

- `#` 는 한 줄 주석에 사용
- `"""triple quotes"""` 는 독스트링과 여러 줄 문자열에 사용
- 들여쓰기는 중요함 (보통 4칸)
- 명명 규칙: 변수/함수는 `snake_case`, 클래스는 `PascalCase`
- 스크립트가 직접 실행되었는지 확인할 때 `__name__ == "__main__"` 사용
- 프로젝트 격리를 위해 `virtualenv` 또는 `venv` 사용
- 패키지 설치는 `pip install package_name` 사용

---

*최종 업데이트: 2025년 6월 | Python 3.x*
