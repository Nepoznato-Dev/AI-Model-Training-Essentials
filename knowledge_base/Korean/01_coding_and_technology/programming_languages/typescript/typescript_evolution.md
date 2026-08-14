---
# Metadata
title: "TypeScript — Version History & Evolution"
description: "Comprehensive version history and evolution of TypeScript from 0.8 to modern TypeScript."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [typescript, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# TypeScript — 버전 기록 및 진화
## 타임라인
| 버전 | 출시일 | 주요 테마 |
|---------|-------------|------------|
| 0.8 | 2012년 10월 | 최초 공개 릴리스(Anders Hejlsberg) |
| 0.9 | 2013년 4월 | 제네릭 |
| 1.0 | 2014년 4월 | 첫 번째 안정 릴리스 |
| 1.1 | 2014년 11월 | 컴파일러 성능 |
| 1.4 | 2015년 1월 | 템플릿 리터럴 유형(기본),`let`|
| 1.5 | 2015년 7월 | `namespace`,`destructuring`,`for...of`|
| 1.6 | 2015년 9월 | `abstract`클래스, JSX 지원 |
| 1.7 | 2015년 11월 | `async/await`(ES2017 대상) |
| 1.8 | 2016년 2월 | 태그가 지정된 템플릿 문자열,`--strictNullChecks`|
| 2.0 | 2016년 9월 | **주요**: 합집합/교차점 유형,`never`,`keyof`,`protected`|
| 2.1 | 2016년 12월 | `keyof`, 매핑된 유형,`async`생성기 |
| 2.2 | 2017년 2월 | `object`유형,`this`개선 |
| 2.3 | 2017년 4월 | 일반 기본값,`--strict`모드 |
| 2.4 | 2017년 6월 | 약한 유형, 문자열 열거형 |
| 2.5 | 2017년 9월 | 선택적 캐치 바인딩 |
| 2.6 | 2017년 10월 | 엄격한 함수 유형,`--strictFunctionTypes`|
| 2.7 | 2018년 1월 | 한정 할당(`!`),`const`열거형 |
| 2.8 | 2018년 3월 | **조건부 유형**,`Exclude`,`Extract`|
| 2.9 | 2018년 6월 |  숫자/기호용 `keyof`,`import()`유형 |
| 3.0 | 2018년 7월 | **주요**: 나머지 튜플, `unknown`, 프로젝트 참조 |
| 3.1 | 2018년 9월 | 튜플의 매핑된 유형,`readonly`배열 |
| 3.2 | 2018년 11월 | `bigint`,`object`스프레드 |
| 3.4 | 2019년 3월 | `const`어설션, 고차 유형 추론 |
| 3.5 | 2019년 5월 | `Omit`도우미 유형 |
| 3.7 | 2019년 11월 | **선택적 연결**, nullish 병합, 재귀 유형 |
| 3.8 | 2020년 2월 | `type-only`가져오기/내보내기,`#private`필드 |
| 3.9 | 2020년 5월 |  `// @ts-expect-error`, 향상된 추론 |
| 4.0 | 2020년 8월 | **주요**: 가변 튜플, 레이블이 있는 튜플, 템플릿 리터럴 유형 |
| 4.1 | 2020년 11월 | **템플릿 리터럴 유형**, 키 재매핑, 재귀 조건부 |
| 4.2 | 2021년 2월 | 매핑된 유형의 추상 속성,`~`|
| 4.3 | 2021년 6월 | 별도의 쓰기 유형,`override`키워드 |
| 4.4 | 2021년 8월 | 기호/색인 서명, 제어 흐름 축소 |
| 4.5 | 2021년 11월 |  `.js`의 `.d.ts`, `.d.ts`의`await`|
| 4.6 | 2022년 2월 | 블록 범위 기능 검사, 객체 나머지 정확한 유형 |
| 4.7 | 2022년 5월 |  `infer`, `.ts`의 ESM에 대한`extends`제약 조건 |
| 4.8 | 2022년 8월 | 교차로 감소 개선,`--strictNullChecks`수정 |
| 4.9 | 2022년 11월 | **`satisfies`연산자**,`in`축소 |
| 5.0 | 2023년 3월 | **주요**:`const`유형 매개변수, 데코레이터,`enum`점검 |
| 5.1 | 2023년 6월 | 관련 없는 유형 설정자,`--exactOptionalPropertyTypes`|
| 5.2 | 2023년 8월 | `using`선언(명시적 리소스 관리) |
| 5.3 | 2023년 11월 | 가져오기 속성,`switch true`축소 |
| 5.4 | 2024년 3월 | `NoInfer`유틸리티, 좁은 폐쇄 매개변수 |
| 5.5 | 2024년 6월 | 유추된 유형 술어, regex에 대한`@`|
| 5.6 | 2024년 9월 | `--erasableSyntaxOnly`, 반복자 도우미 |
| 5.7 | 2024년 11월 |  `--noCheck`, 경로 완성 |
| 5.8 | 2025년 2월 | 향상된`isolatedDeclarations`|
## 주요 이정표
### 초기(2012~2015)
- **0.8(2012)**: Anders Hejlsberg(C# 작성자)가 Microsoft에서 TypeScript를 이끌고 있습니다.
- **1.0(2014)**: 안정적인 릴리스; 클래스, 인터페이스, 기본 유형
- **1.5(2015)**: ES6 기능 — 구조 분해, 네임스페이스, `for...of`
### 유형 혁명(2016~2018)
- **2.0 (2016)**: 공용체 유형, 교차 유형,`never`,`keyof`— TypeScript의 유형 시스템이 고유해졌습니다.
- **2.8(2018)**: 조건부 유형 - 고급 유형 수준 프로그래밍의 기초
- **3.0 (2018)**: 나머지 매개변수의 튜플,`unknown`유형, 프로젝트 참조
### 최신 TypeScript(2019~현재)
- **3.7(2019)**: 선택적 연결`?.`및 nullish 병합 `??`(JS 표준 이전!)
- **4.0 (2020)**: 가변 튜플, 템플릿 리터럴 유형
- **4.1(2020)**: 템플릿 리터럴 유형 — 유형 수준 문자열 조작
- **4.9 (2022)**:`satisfies`연산자 — 확장 없이 유형 검사
- **5.0 (2023)**:`const`유형 매개변수, 데코레이터(3단계)
- **5.2(2023)**:`using`선언 — 명시적 리소스 관리
## 유형 시스템 진화
```
2012: Basic types, classes, interfaces
2014: Generics, enums
2016: Union types, intersection types, discriminated unions
2018: Conditional types, mapped types, keyof, infer
2020: Template literal types, variadic tuples
2022: satisfies operator
2023: const type parameters
2023: using declarations
```

## 데코레이터의 진화
```
2014: TypeScript experimental decorators (legacy)
2022: TC39 stage 3 decorators proposal
2023: TypeScript 5.0 — standard decorators (stage 3)
2024: Both legacy and standard decorators supported
```

## 구성의 진화
```
2014: Basic tsconfig.json
2016: --strict flag introduced
2017: --strictFunctionTypes, --strictNullChecks
2018: --strict mode becomes recommended
2020: --strictPropertyInitialization
2023: --exactOptionalPropertyTypes
2024: --erasableSyntaxOnly, --noCheck
```

## 생태계 성장
```
2012: TypeScript launches — few adopters
2014: Angular 2 built with TypeScript
2016: VS Code (built with TS) drives adoption
2018: TypeScript overtakes Flow (React community)
2020: TypeScript used by most npm packages
2023: TypeScript 5.0 — decorators, const generics
2025: TypeScript — de facto standard for large JS projects
```

## 주요 설계 결정
```
1. Structural typing (not nominal) — duck typing for types
2. Gradual adoption — any type, type widening
3. Erased types — no runtime overhead
4. JS compatibility — all valid JS is valid TS
5. Declaration files (.d.ts) — types for JS libraries
6. Playground — interactive type exploration
```
