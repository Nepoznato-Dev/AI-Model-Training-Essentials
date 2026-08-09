---
# Metadata
title: "Scratch"
description: "Comprehensive reference for the Scratch programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [scratch, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "29 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# 스크래치
스크래치(Scratch)는 MIT 미디어 랩에서 개발되어 2007년에 처음 출시된 시각적 블록 기반 프로그래밍 언어입니다. 사용자는 텍스트 기반 코드를 작성하는 대신 색상 블록을 연결하여 프로그램을 만듭니다. 스크래치는 구문 오류의 장벽 없이 기본적인 프로그래밍 개념(루프, 조건부, 변수, 이벤트 및 함수)을 가르치기 위해 8~16세 어린이(모든 연령대의 학습자가 사용하지만)를 위해 특별히 설계되었습니다.
스크래치는 전 세계에서 가장 널리 사용되는 입문 프로그래밍 언어로, 1억 명 이상의 등록 사용자가 있고 70개 이상의 언어로 제공됩니다. 웹 브라우저에서 실행되며 무료입니다.
---

## 스크래치가 중요한 이유
- **프로그래밍에 대한 최고의 소개**: 구문 장벽을 완전히 제거합니다. 개념은 시각적 조작을 통해 가르칩니다.
- **컴퓨팅 사고**: 분해, 패턴 인식, 추상화 및 알고리즘 설계를 가르칩니다.
- **창의력 중심**: 아이들은 게임, 애니메이션, 스토리, 음악을 만듭니다. 자신이 좋아하는 것을 만들면서 프로그래밍을 배우게 됩니다.
- **글로벌 도달범위**: 전 세계 학교에서 사용됩니다. 70개 이상의 언어로 제공됩니다. 무료이며 브라우저 기반입니다.
- **커뮤니티**: 스크래치 온라인 커뮤니티에서는 공유, 리믹싱, 협력 학습을 가르칩니다.
## 절충안
| 제한사항 | 세부정보 | 일반적인 해결 방법 |
|------------|---------|------|
| **"실제" 프로그래밍 언어가 아님** | 프로덕션 소프트웨어, API 또는 시스템을 구축할 수 없음 | Python, JavaScript 또는 텍스트 기반 언어로 전환 |
| **제한된 기능** | 파일 I/O, 네트워킹 또는 고급 데이터 구조 없음 | 학습에 사용합니다. 실제 프로젝트를 위해 텍스트 언어로 전환 |
| **성능** | 복잡한 프로젝트의 경우 해석 속도가 느림 | 성능이 중요한 작업용으로 설계되지 않음 |
| **연령 인식** | 종종 "아이들만을 위한" 것으로 간주됨 | 스크래치는 전문 언어가 아닌 학습 도구입니다 |
---

## 스크래치 작동 방식
스크래치 프로그램("프로젝트"라고 함)은 스크립트에 함께 맞춰진 **블록**에 반응하는 **스프라이트**(문자/개체)로 구성됩니다.
### 핵심 개념(블록을 통해 학습)
| 개념 | 스크래치 블록 카테고리 | 예 |
|---------|---------|---------|
| **시퀀스** | 모션, 룩 | "10단계 이동" 후 "안녕하세요" |
| **루프** | 컨트롤(노란색) | "10번 반복", "영원히", "다음까지 반복" |
| **조건부** | 컨트롤(노란색) | "만약... 그렇다면", "만약... 그렇다면... 다른" |
| **변수** | 변수(주황색) | "점수를 0으로 설정", "점수를 1로 변경" |
| **이벤트** | 이벤트(노란색) | "녹색 플래그를 클릭했을 때", "키를 눌렀을 때" |
| **기능** | 마이 블록(맞춤형) | 재사용 가능한 블록 시퀀스 정의 |
| **목록(배열)** | 변수(주황색) | "목록에 추가", "목록의 항목" |
| **방송 중** | 이벤트 | 스프라이트 간에 메시지 보내기 |
### 예: 간단한 게임 로직
```
When green flag clicked:
  Set [score] to 0
  Forever:
    If <touching [enemy]?> then:
      Change [score] by -1
      Play sound [ouch]
    If <touching [coin]?> then:
      Change [score] by 1
      Go to random position
```

---

## 고급 구문 및 패턴
### 블록 카테고리 자세히 보기
스크래치 3.0은 블록을 색상으로 구분된 카테고리로 구성합니다.
| 카테고리 | 색상 | 블록 유형 |
|----------|----------|-------------|
| **모션** | 블루 | 이동, 회전, 이동, 활공, 점, x/y 변경 |
| **룩** | 보라색 | 말하고, 생각하고, 의상을 바꾸고, 크기를 바꾸고, 표시/숨기기 |
| **소리** | 핑크 | 소리 재생, 소리 중지, 볼륨 변경, 피치 변경 |
| **이벤트** | 노란색 | 플래그를 클릭할 때, 키를 누를 때, 스프라이트를 클릭할 때 브로드캐스트 |
| **제어** | 골드 | 기다리다, 반복하다, 영원히, if, if-eld, 때까지 반복, 중지 |
| **센싱** | 라이트 블루 | 터치, 키 누름, 마우스, 거리, 질문/응답, 타이머 |
| **운영자** | 그린 | 수학 연산, 텍스트 연산, 비교 및/또는 아님, 무작위 |
| **변수** | 오렌지 | 변수 설정/변경, 목록 작업 |
| **내 블록** | 다크 레드 | 사용자 정의 블록 정의(함수) |
### 고급 블록 패턴
```
// Pattern: Timer-based movement (smooth animation)
When green flag clicked:
  Set [speed] to 5
  Forever:
    Change x by (speed)
    If <(x position) > 200> then
      Set [speed] to ((speed) * -1)
    If <(x position) < -200> then
      Set [speed] to ((speed) * -1)

// Pattern: State machine using variables
When green flag clicked:
  Set [game_state] to [menu]
  Forever:
    If <(game_state) = [menu]> then
      Show
      Go to x: 0 y: 0
    If <(game_state) = [playing]> then
      Hide
    If <(game_state) = [game_over]> then
      Say [Game Over!] for 2 secs

// Pattern: Object-oriented sprite (each sprite manages its own state)
When green flag clicked:
  Set [hp] to 100
  Set [max_hp] to 100
  Set [is_alive] to true
  Forever:
    If <(is_alive) = true> then
      If <touching [enemy]?> then
        Change [hp] by -10
        If <(hp) < 1> then
          Set [is_alive] to false
          Broadcast [player_dead]
```

### 사용자 정의 블록(기능)
```
// Define a custom block with parameters
Define: Jump (height) times (count)
  Repeat (count):
    Change y by (height)
    Wait 0.2 seconds
    Change y by ((height) * -1)
    Wait 0.2 seconds

// Usage:
When space key pressed:
  Jump height: 50 times: 3

// Custom block with "run without screen refresh" (optimization)
Define: Draw fractal (depth) (size)
  Run without screen refresh: true
  If <(depth) = 0> then
    Move (size) steps
  Else:
    Draw fractal depth: ((depth) - 1) size: ((size) / 2)
    Turn right 60 degrees
    Draw fractal depth: ((depth) - 1) size: ((size) / 2)
    Turn left 120 degrees
    Draw fractal depth: ((depth) - 1) size: ((size) / 2)
    Turn right 60 degrees
```

### 목록 작업(배열)
```
// Creating and using lists
When green flag clicked:
  Delete all of [scores]
  Add [100] to [scores]
  Add [85] to [scores]
  Add [92] to [scores]
  Add [78] to [scores]
  
  // Access items (1-indexed)
  Set [total] to 0
  Set [i] to 1
  Repeat (length of [scores]):
    Change [total] by (item (i) of [scores])
    Change [i] by 1
  
  Set [average] to ((total) / (length of [scores]))
  Say (join [Average: ] (average)) for 2 secs

// Sorting a list (bubble sort)
Define: Sort List
  Set [n] to (length of [scores])
  Repeat (n)
    Set [i] to 1
    Repeat ((n) - 1)
      If <(item (i) of [scores]) > (item ((i) + 1) of [scores])> then
        // Swap
        Set [temp] to (item (i) of [scores])
        Replace item (i) of [scores] with (item ((i) + 1) of [scores])
        Replace item ((i) + 1) of [scores] with (temp)
      Change [i] by 1
```

### 방송(스프라이트 간 통신)
```
// Sprite 1 (Player):
When space key pressed:
  Broadcast [fire_bullet]

// Sprite 2 (Bullet):
When I receive [fire_bullet]:
  Go to [Player]
  Show
  Repeat 50:
    Change y by 10
  Hide

// Sprite 3 (Enemy):
When I receive [fire_bullet]:
  If <touching [Bullet]?> then
    Change [hp] by -25
    If <(hp) < 1> then
      Broadcast [enemy_destroyed]
      Hide
```

---

## 아키텍처 및 시스템 설계
### 이벤트 중심 설계
스크래치는 이벤트 기반 아키텍처를 사용합니다. 모든 스크립트는 이벤트 블록(hat 블록)으로 시작하고 해당 이벤트에 대한 응답으로 실행됩니다.
```
Event Types:
+-------------------------------------------+
| when [green flag] clicked    (startup)     |
| when [space] key pressed     (keyboard)    |
| when this sprite clicked     (mouse)       |
| when [backdrop] switches to  (stage event) |
| when [loudness] > [10]       (sound)       |
| when I receive [message]     (broadcast)   |
| when video motion > [10]     (camera)      |
+-------------------------------------------+
```

### 프로젝트 구조
```
scratch-project/
├── project.sb3              * Saved project file (ZIP format)
├── sprites/
│   ├── Player/              * Player sprite
│   │   ├── costumes/        * Costume images
│   │   └── sounds/          * Sound files
│   ├── Enemy/
│   │   ├── costumes/
│   │   └── sounds/
│   └── Bullet/
├── stage/
│   ├── backdrops/           * Background images
│   └── sounds/              * Stage sounds
└── README.md
```

### 클론 시스템(객체 생성)
```
// Creating clones (like creating object instances)
When green flag clicked:
  Forever:
    Wait 1 seconds
    Create clone of [Enemy]

When I start as a clone:
  Go to random position
  Show
  Set [hp] to 3
  Forever:
    Change y by -3
    If <(y position) < -170> then
      Delete this clone
    If <touching [Bullet]?> then
      Change [hp] by -1
      If <(hp) < 1> then
        Change [score] by 10
        Delete this clone
```

---

## 프로젝트 구성 및 빌드 시스템
### 스크래치 확장
스크래치는 기능을 추가하는 공식 및 커뮤니티 확장을 지원합니다.
| 확장 | 목적 |
|------------|---------|
| **펜** | 무대에 선과 모양 그리기 |
| **영상 감지** | 동작 감지를 위해 웹캠 사용 |
| **텍스트 음성 변환** | 텍스트를 음성 오디오로 변환 |
| **번역** | 언어 간 텍스트 번역 |
| **메이키 메이키** | 물리적 객체를 입력으로 연결 |
| **마이크로:비트** | BBC micro:bit 하드웨어 연결 |
| **레고 마인드스톰** | LEGO 로봇 제어 |
| **음악** | 음표 및 악기 연주 |
### 스크래치 파일 형식
```
Scratch 3.0 projects (.sb3) are ZIP archives containing:
├── project.json             * All scripts, sprites, and metadata
├── [md5hash].svg           * Costume images (SVG or PNG)
├── [md5hash].png           * Additional costumes
└── [md5hash].wav           * Sound files

The project.json contains:
{
  "targets": [
    {
      "isStage": true,
      "name": "Stage",
      "costumes": [...],
      "sounds": [...],
      "blocks": {...}
    },
    {
      "isStage": false,
      "name": "Sprite1",
      "position": {"x": 0, "y": 0},
      "blocks": {...}
    }
  ],
  "monitors": [...],
  "meta": {"semver": "3.0.0"}
}
```

### 오프라인 편집기
```
Scratch Desktop (offline editor) available for:
- Windows 10+ (Microsoft Store or direct download)
- macOS 10.13+
- ChromeOS

Installation:
1. Download from https://scratch.mit.edu/download
2. Install and run — no internet required
3. Projects save as .sb3 files locally
```

---

## 테스트 및 디버깅
### 내장 디버깅 도구
스크래치는 프로젝트 디버깅을 위한 몇 가지 내장 도구를 제공합니다.
| 도구 | 사용방법 |
|------|------------|
| **거북이 모드** | 스프라이트를 마우스 오른쪽 버튼으로 클릭하고 "디버그 표시"를 선택하여 좌표를 확인하세요 |
| **가변 모니터** | 변수를 마우스 오른쪽 버튼으로 클릭하고 "표시"를 선택하면 해당 값이 실시간으로 표시됩니다. |
| **모니터 나열** | 일반, 행 또는 열 표시로 목록 내용 보기 |
| **터보 모드** | 더 빠른 실행을 위해 녹색 플래그를 클릭하는 동안 Shift를 누르세요 |
| **단일 단계 모드** | "단일 단계"에 대한 녹색 플래그를 마우스 오른쪽 버튼으로 클릭(실행 속도 저하) |
### 디버깅 패턴
```
// Debug: Display variable values on sprite
When green flag clicked:
  Forever:
    Say (join [Score: ] (score))

// Debug: Visual boundary checking
When green flag clicked:
  Forever:
    If <(x position) > 240> then
      Say [TOO FAR RIGHT!] for 0.5 secs
      Set x to 240
    If <(x position) < -240> then
      Say [TOO FAR LEFT!] for 0.5 secs
      Set x to -240

// Debug: Frame counter
When green flag clicked:
  Set [frames] to 0
  Forever:
    Change [frames] by 1
    If <(frames) mod 30 = 0> then
      Say (join [FPS: ] ((frames) / (timer))) for 0.1 secs
```

### 일반적인 문제
| 문제 | 원인 | 솔루션 |
|---------|-------|----------|
| 스프라이트가 응답하지 않음 | 이벤트 없음 모자 블록 | "녹색 깃발을 클릭할 때" 또는 기타 이벤트 추가 |
| 클론이 작동하지 않음 | 클론이 생성되었지만 표시되지 않음 | "복제본으로 시작할 때" 뒤에 "표시" 블록 추가 |
| 스프라이트 간에 공유되는 변수 | 전역 변수와 지역 변수 혼동 | "이 스프라이트에만 해당" 옵션 사용 |
| 방송이 수신되지 않음 | 잘못된 메시지 이름 | 브로드캐스트 및 수신 이름이 정확히 일치하는지 확인 |
| 무한 루프 정지 | 기다림 없이 "영원히" | 긴밀한 루프에 작은 "대기" 블록 추가 |
---

## 상호 운용성
### 하드웨어 확장
스크래치는 확장을 통해 물리적 하드웨어에 연결할 수 있습니다.
```
Supported Hardware:
├── micro:bit
│   ├── Accelerometer/gyroscope input
│   ├── LED matrix display output
│   ├── Button input
│   └── Radio communication
├── LEGO Education
│   ├── SPIKE Prime / Essential
│   ├── EV3 (older)
│   └── Motors and sensors
├── Makey Makey
│   ├── Capacitive touch input
│   ├── Any conductive object as button
│   └── USB connection (no drivers needed)
├── Arduino (via extensions)
│   ├── GPIO pin control
│   ├── Sensor readings
│   └── Motor control
└── Camera / Webcam
    ├── Video sensing (motion detection)
    └── Face detection (via extensions)
```

### 스크래치 확장 API(맞춤 확장)
```javascript
// Custom Scratch extension (JavaScript)
class MyExtension {
  getInfo() {
    return {
      id: 'myExtension',
      name: 'My Extension',
      blocks: [
        {
          opcode: 'greet',
          blockType: Scratch.BlockType.REPORTER,
          text: 'greet [NAME]',
          arguments: {
            NAME: { type: Scratch.ArgumentType.STRING, defaultValue: 'World' }
          }
        },
        {
          opcode: 'addNumbers',
          blockType: Scratch.BlockType.REPORTER,
          text: '[A] + [B]',
          arguments: {
            A: { type: Scratch.ArgumentType.NUMBER, defaultValue: 1 },
            B: { type: Scratch.ArgumentType.NUMBER, defaultValue: 2 }
          }
        }
      ]
    };
  }
  greet(args) { return 'Hello, ' + args.NAME + '!'; }
  addNumbers(args) { return Number(args.A) + Number(args.B); }
}
Scratch.extensions.register(new MyExtension());
```
---

## 디자인 패턴
### 패턴 1: 플랫폼 게임 움직임
```
When green flag clicked:
  Set [gravity] to -1
  Set [velocity_y] to 0
  Set [speed] to 5
  Set [is_jumping] to false
  Forever:
    // Horizontal movement
    If <key [right arrow] pressed?> then
      Change x by (speed)
    If <key [left arrow] pressed?> then
      Change x by ((speed) * -1)
    // Jumping
    If <key [space] pressed?> then
      If <(is_jumping) = false> then
        Set [velocity_y] to 12
        Set [is_jumping] to true
    // Gravity
    Change [velocity_y] by (gravity)
    Change y by (velocity_y)
    // Ground collision
    If <(y position) < -100> then
      Set y to -100
      Set [velocity_y] to 0
      Set [is_jumping] to false
```

### 패턴 2: 스크롤 배경
```
// Background sprite scrolls left to create side-scrolling effect
When green flag clicked:
  Forever:
    Change x by -5
    If <(x position) < -240> then
      Set x to 240

// Or use two copies for seamless scrolling
When I start as a clone:
  Forever:
    Change x by -5
    If <(x position) < -480> then
      Change x by 960
```

### 패턴 3: 스프라이트 따라가기(Chase AI)
```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### 패턴 4: 목록이 포함된 재고 시스템
```
When green flag clicked:
  Delete all of [inventory]
  Add [Sword] to [inventory]
  Add [Shield] to [inventory]
  Add [Potion] to [inventory]

When key [i] pressed:
  // Display inventory
  Set [display] to []
  Set [idx] to 1
  Repeat (length of [inventory]):
    Set [display] to (join (display) (join (item (idx) of [inventory]) [
]))
    Change [idx] by 1
  Say (display) for 3 secs

When key [1] pressed:
  // Use first item
  If <(length of [inventory]) > 0> then
    Set [used_item] to (item 1 of [inventory])
    Delete 1 of [inventory]
    Say (join [Used: ] (used_item)) for 1 secs
```

### 패턴 5: 클론이 포함된 파티클 시스템
```
// Create particles on click
When this sprite clicked:
  Repeat 10:
    Create clone of [Particle]

// Each particle moves randomly and fades
When I start as a clone:
  Go to [mouse-pointer]
  Point in direction (pick random 0 to 360)
  Set [size] to (pick random 20 to 50)
  Set [ghost] to 0
  Show
  Repeat 20:
    Move 5 steps
    Change [ghost] by 5
  Hide
  Delete this clone
```

---

## 성능 및 최적화
### 스프라이트 최적화
| 기술 | 영향 | 설명 |
|------------|---------|-------------|
| **클론 최소화** | 높음 | 각 클론은 메모리를 소비합니다. 완료되면 삭제 |
| **의상 줄이기** | 중간 | 의상 스위치가 적다는 것은 렌더링 오버헤드가 적다는 것을 의미합니다 |
| **"화면 새로 고침 없이 실행" 사용** | 높음 | 화면 새로 고침이 없는 사용자 정의 블록이 더 빠르게 실행됩니다 |
| **"말하기" 차단을 제한하세요** | 중간 | 말풍선으로 인해 렌더링 오버헤드 발생 |
| **모든 스프라이트에서 "영원히"를 피하세요** | 중간 | 지속적인 폴링 대신 브로드캐스트 및 이벤트 사용 |
### 클론 관리
```
// BAD: Creating clones without cleanup
When green flag clicked:
  Forever:
    Create clone of [Enemy]
    Wait 0.1 secs
    // Clones pile up and slow everything down

// GOOD: Limit active clones
When green flag clicked:
  Set [max_enemies] to 10
  Forever:
    If <(enemy_count) < (max_enemies)> then
      Create clone of [Enemy]
      Change [enemy_count] by 1
    Wait 1 secs

When I start as a clone:
  // ... enemy behaviour ...
  // When done:
  Change [enemy_count] by -1
  Delete this clone
```

### 최적화 체크리스트
| 기술 | 영향 | 설명 |
|------------|---------|-------------|
| **화면 새로 고침 없이 실행** | 매우 높음 | 사용자 정의 블록은 속도를 위해 렌더링을 건너뜁니다. |
| **활성 클론 최소화** | 높음 | 더 이상 필요하지 않은 클론 삭제 |
| **방송을 자제하여 사용** | 중간 | 프레임당 브로드캐스트가 너무 많아 지연이 발생함 |
| **의상 단순화** | 중간 | 작은 이미지가 더 빠르게 렌더링됩니다 |
| **목록 작업 감소** | 중간 | 매 프레임마다 큰 목록을 스캔하지 마세요 |
| **"대기" 블록 사용** | 낮음 | 무한 루프에서 CPU 호깅 방지 |
---

## 배포 및 실제 사용
### 프로젝트 공유
```
Deployment Options:
├── Scratch Community (online)
│   ├── Upload to scratch.mit.edu
│   ├── Share with community
│   └── Allow remixing by others
├── Local sharing
│   ├── Save as .sb3 file
│   ├── Share via email/USB/cloud
│   └── Open in Scratch Desktop or web editor
├── Embedding
│   ├── Embed on websites via iframe
│   └── <iframe src="https://scratch.mit.edu/projects/embed/PROJECT_ID">
└── Standalone apps (via third-party tools)
    ├── TurboWarp (desktop packaging)
    ├── Electron-based wrappers
    └── HTML5 export tools
```

### 실제 교육 활용
| 컨텍스트 | 스크래치가 사용되는 방법 | 규모 |
|---------|------|-------|
| **K-12 학교** | CS 수업의 프로그래밍 소개 | 190개 이상의 국가에서 사용됨 |
| **코딩클럽** | 스크래치 클럽 / CoderDojo 워크샵 | 전세계 3000개 이상의 클럽 |
| **도서관** | 방과후 프로그래밍 프로그램 | 공공 도서관 시스템 |
| **홈스쿨링** | 자기 주도형 프로그래밍 교육 | 수백만 명의 가정 학습자 |
| **대학 CS0** | 비전공 CS입문과정 | 대학 브리지 프로그램 |
| **접근성** | 시각장애인 프로그래밍 교육 | 스크린 리더 지원 |
| **치료** | 인지 및 운동 능력 개발 | 작업치료 |
### 교육 연구의 스크래치
연구에 따르면 스크래치가 효과적으로 다음을 가르치는 것으로 나타났습니다.
- **순차적 사고**: 문제를 순차적인 단계로 나누기
- **디버깅 기술**: 논리 오류 찾아 수정
- **창의적 표현**: 미술, 음악, 프로그래밍의 결합
- **협업**: 다른 사람의 프로젝트를 리믹스하고 구축
- **지속성**: 개선을 위해 프로젝트를 반복합니다.
---

## 처음부터 전환하기
스크래치를 학습한 후 일반적인 다음 단계는 다음과 같습니다.
| 다음 언어 | 왜 |
|---------------|------|
| **파이썬** | 가장 자연스러운 전환 - 읽기 쉬운 구문, 유사한 논리 개념 |
| **자바스크립트** | 웹/게임에 관심이 있는 경우 - 즉각적인 시각적 피드백 |
| **루아(Roblox/Love2D를 통해)** | 게임 개발에 관심이 있다면 |
| **앱 발명가** | Android 앱용 시각적 블록(동일한 MIT 계보) |
| **블록하게** | Google의 시각적 프로그래밍 라이브러리(유사 개념) |
### 개념 매핑: 스크래치에서 Python으로
| 스크래치 개념 | Python과 동일 |
|---|------|
|  __보호됨_0__ |  __보호됨_1__ |
|  __보호됨_2__ |  __보호됨_3__ |
|  __보호됨_4__ |  __보호됨_5__ |
|  __보호_6__ |  __보호_7__ |
|  __보호됨_8__ |  __보호_9__ |
|  __보호됨_10__ | 함수 호출 또는 이벤트 시스템 |
|  __보호됨_11__ |  __보호됨_12__ |
|  __보호_13__ |  __보호됨_14__ |
|  __보호_15__ | `list[0]`(0-인덱스!) |
|  __보호됨_17__ |  __보호됨_18__ |
---

## 스크래치를 사용해야 하는 경우
| 시나리오 | 스크래치가 필요한 이유 | 더 나은 대안 |
|----------|------------|------|
| 어린이(8~16세)에게 코드 교육 | 이를 위해 특별히 설계되었습니다 | — |
| 컴퓨팅 사고력 소개 | 시각적, 구문 오류 없음 | — |
| 학교 워크숍/코딩 동아리 | 무료, 브라우저 기반, 설정 없음 | — |
| 게임 아이디어를 시각적으로 프로토타이핑하기 | 빠른 반복 | — |
| 전문성 개발 | 이를 위해 설계되지 않았습니다 | Python, JavaScript, 모든 텍스트 언어 |
| 대학수준의 CS교육 | 너무 단순함 | 파이썬, 자바, C |
---

## 요약
스크래치는 전통적인 의미의 프로그래밍 언어가 아니라 학습 환경입니다. 이 게임의 천재성은 어린이와 상호 작용하는 무언가를 만드는 기쁨 사이의 모든 장벽을 제거하는 것입니다. 구문보다는 개념에 초점을 맞춤으로써 스크래치는 모든 언어로 변환되는 프로그래밍의 기본을 가르칩니다. 어린 학습자에게 프로그래밍을 소개하는 데 있어 스크래치는 최고의 표준입니다.