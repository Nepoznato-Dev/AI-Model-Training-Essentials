---
# Metadata
title: "Scratch"
description: "Comprehensive reference for the Scratch programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
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
# Cào
Scratch là ngôn ngữ lập trình dựa trên khối, trực quan được phát triển bởi MIT Media Lab và phát hành lần đầu tiên vào năm 2007. Thay vì viết mã dựa trên văn bản, người dùng ghép các khối màu lại với nhau để tạo chương trình. Scratch được thiết kế dành riêng cho trẻ em từ 8-16 tuổi (mặc dù người học ở mọi lứa tuổi đều sử dụng nó) để dạy các khái niệm lập trình cơ bản — vòng lặp, điều kiện, biến, sự kiện và hàm — mà không gặp phải lỗi cú pháp.
Scratch là ngôn ngữ lập trình cơ bản được sử dụng rộng rãi nhất trên thế giới, với hơn 100 triệu người dùng đã đăng ký và có sẵn hơn 70 ngôn ngữ. Nó chạy trong trình duyệt web và miễn phí.
---

## Tại sao Scratch lại quan trọng
- **Giới thiệu hay nhất về lập trình**: Loại bỏ hoàn toàn rào cản cú pháp. Các khái niệm được dạy thông qua thao tác trực quan.
- **Tư duy tính toán**: Dạy phân tích, nhận dạng mẫu, trừu tượng hóa và thiết kế thuật toán.
- **Thúc đẩy sự sáng tạo**: Trẻ em tạo ra trò chơi, hoạt hình, câu chuyện và âm nhạc — học lập trình như một sản phẩm phụ của quá trình tạo ra những thứ chúng quan tâm.
- **Phạm vi tiếp cận toàn cầu**: Được sử dụng trong các trường học trên toàn thế giới. Có sẵn trong hơn 70 ngôn ngữ. Miễn phí và dựa trên trình duyệt.
- **Cộng đồng**: Cộng đồng trực tuyến Scratch dạy cách chia sẻ, phối hợp và học tập hợp tác.
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Không phải ngôn ngữ lập trình "thực"** | Không thể xây dựng phần mềm sản xuất, API hoặc hệ thống | Chuyển đổi sang ngôn ngữ Python, JavaScript hoặc dựa trên văn bản |
| **Khả năng hạn chế** | Không có tệp I/O, kết nối mạng hoặc cấu trúc dữ liệu nâng cao | Sử dụng cho việc học tập; chuyển sang ngôn ngữ văn bản cho các dự án thực tế |
| **Hiệu suất** | Phiên dịch, chậm cho các dự án phức tạp | Không được thiết kế cho công việc quan trọng về hiệu suất |
| **Nhận thức về tuổi tác** | Thường được coi là "chỉ dành cho trẻ em" | Scratch là một công cụ học tập, không phải một ngôn ngữ chuyên nghiệp |
---

## Cách thức hoạt động của Scratch
Các chương trình Scratch (được gọi là "dự án") bao gồm **sprites** (ký tự/đối tượng) phản hồi **khối** được gắn với nhau trong tập lệnh.
### Các khái niệm cốt lõi (Được dạy qua các khối)
| Khái niệm | Hạng mục Khối cào | Ví dụ |
|----------|----------------------|----------|
| **Trình tự** | Chuyển động, Ngoại hình | “Tiến 10 bước” rồi “Nói xin chào” |
| **Vòng lặp** | Kiểm soát (màu vàng) | "Lặp lại 10", "Mãi mãi", "Lặp lại cho đến khi" |
| **Có điều kiện** | Kiểm soát (màu vàng) | "Nếu... thì", "Nếu... thì... khác" |
| **Biến** | Biến (màu cam) | "Đặt điểm thành 0", "Thay đổi điểm bằng 1" |
| **Sự kiện** | Sự kiện (màu vàng) | "Khi nhấp vào cờ xanh", "Khi nhấn phím" |
| **Chức năng** | Khối của tôi (tùy chỉnh) | Xác định chuỗi khối có thể tái sử dụng |
| **Danh sách (mảng)** | Biến (màu cam) | "Thêm vào danh sách", "Mục danh sách" |
| **Phát sóng** | Sự kiện | Gửi tin nhắn giữa các sprite |
### Ví dụ: Logic trò chơi đơn giản
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

## Cú pháp & Mẫu nâng cao
### Chặn danh mục chi tiết
Scratch 3.0 sắp xếp các khối thành các danh mục được mã hóa màu:
| Danh mục | Màu sắc | Các loại khối |
|----------|--------|-------------|
| **Chuyển động** | Màu xanh | di chuyển, xoay, đi, lướt, trỏ, thay đổi x/y |
| **Trông** | Màu tím | nói, suy nghĩ, đổi trang phục, thay đổi kích thước, hiển thị/ẩn |
| **Âm thanh** | Hồng | phát âm thanh, dừng âm thanh, thay đổi âm lượng, thay đổi cao độ |
| **Sự kiện** | Vàng | khi nhấp vào cờ, khi nhấn phím, khi nhấp vào sprite, phát sóng |
| **Kiểm soát** | Vàng | chờ, lặp lại, mãi mãi, nếu, nếu-khác, lặp lại cho đến khi, dừng |
| **Cảm biến** | Xanh nhạt | chạm, nhấn phím, chuột, khoảng cách, hỏi/trả lời, hẹn giờ |
| **Người vận hành** | Xanh | hoạt động toán học, hoạt động văn bản, so sánh và/hoặc/không, ngẫu nhiên |
| **Biến** | Cam | đặt/thay đổi biến, liệt kê các thao tác |
| **Khối của tôi** | Đỏ sẫm | định nghĩa khối tùy chỉnh (chức năng) |
### Mẫu khối nâng cao
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

### Khối tùy chỉnh (Chức năng)
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

### Thao tác danh sách (Mảng)
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

### Broadcasting (Giao tiếp giữa các Sprite)
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

## Thiết kế kiến ​​trúc & hệ thống
### Thiết kế hướng sự kiện
Scratch sử dụng kiến ​​trúc hướng sự kiện. Mọi tập lệnh đều bắt đầu bằng một khối sự kiện (khối mũ) và chạy để phản hồi sự kiện đó.
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

### Cấu trúc dự án
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

### Hệ thống nhân bản (Tạo đối tượng)
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

## Cấu hình dự án & xây dựng hệ thống
### Tiện ích mở rộng Scratch
Scratch hỗ trợ các tiện ích mở rộng chính thức và cộng đồng bổ sung các khả năng:
| Gia hạn | Mục đích |
|----------||----------|
| **Bút** | Vẽ đường nét và hình dạng trên sân khấu |
| **Cảm biến video** | Sử dụng webcam để phát hiện chuyển động |
| **Chuyển văn bản thành giọng nói** | Chuyển văn bản thành âm thanh nói |
| **Dịch** | Dịch văn bản giữa các ngôn ngữ |
| **Makey Makey** | Kết nối các đối tượng vật lý làm đầu vào |
| **micro:bit** | Kết nối phần cứng micro:bit của BBC |
| **Động não LEGO** | Điều khiển robot LEGO |
| **Âm nhạc** | Chơi các nốt nhạc và nhạc cụ |
### Định dạng tệp cào
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

### Trình chỉnh sửa ngoại tuyến
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

## Kiểm tra & gỡ lỗi
### Công cụ gỡ lỗi tích hợp
Scratch cung cấp một số công cụ tích hợp để gỡ lỗi dự án:
| Công cụ | Cách sử dụng |
|------|-------------|
| **Chế độ rùa** | Nhấp chuột phải vào một sprite và chọn "hiển thị gỡ lỗi" để xem tọa độ |
| **Màn hình thay đổi** | Nhấp chuột phải vào một biến và chọn "hiển thị" để xem giá trị của nó theo thời gian thực |
| **Liệt kê màn hình** | Xem nội dung danh sách ở chế độ hiển thị thông thường, hàng hoặc cột |
| **Chế độ Turbo** | Giữ phím Shift trong khi nhấp vào cờ xanh để thực hiện nhanh hơn |
| **Chế độ một bước** | Nhấp chuột phải vào cờ xanh cho "bước đơn" (làm chậm quá trình thực thi) |
### Mẫu gỡ lỗi
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

### Các vấn đề thường gặp
| Vấn đề | Nguyên nhân | Giải pháp |
|----------|-------|----------|
| Sprite không phản hồi | Không có khối mũ sự kiện | Thêm "Khi nhấp vào cờ xanh" hoặc sự kiện khác |
| Bản sao không hoạt động | Bản sao được tạo nhưng không hiển thị | Thêm khối "Hiển thị" sau "Khi tôi bắt đầu làm bản sao" |
| Biến được chia sẻ giữa các sprite | Sự nhầm lẫn biến toàn cục và cục bộ | Sử dụng tùy chọn "Chỉ dành cho sprite này" |
| Không nhận được phát sóng | Tên tin nhắn sai | Xác minh tên phát và nhận khớp chính xác |
| Đóng băng vòng lặp vô hạn | “Mãi mãi” không chờ đợi | Thêm các khối "Chờ" nhỏ vào các vòng lặp chặt chẽ |
---

## Khả năng tương tác
### Tiện ích mở rộng phần cứng
Scratch có thể kết nối với phần cứng vật lý thông qua các tiện ích mở rộng:
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

### API tiện ích mở rộng Scratch (Tiện ích mở rộng tùy chỉnh)
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

## Mẫu thiết kế
### Mẫu 1: Phong trào platformer
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

### Mẫu 2: Nền cuộn
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

### Mẫu 3: Sprite Đi theo (Đuổi AI)
```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### Mẫu 4: Hệ thống tồn kho có danh sách
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

### Mẫu 5: Hệ thống hạt với bản sao
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

## Hiệu suất & Tối ưu hóa
### Tối ưu hóa Sprite
| Kỹ thuật | Tác động | Mô tả |
|----------|----------|-------------|
| **Giảm thiểu sự sao chép** | Cao | Mỗi bản sao tiêu thụ bộ nhớ; xóa khi hoàn tất |
| **Giảm trang phục** | Trung bình | Ít công tắc trang phục hơn có nghĩa là chi phí hiển thị ít hơn |
| **Sử dụng "chạy mà không làm mới màn hình"** | Cao | Khối tùy chỉnh không cần làm mới màn hình sẽ chạy nhanh hơn |
| **Giới hạn khối "nói"** | Trung bình | Bong bóng lời thoại gây ra chi phí hiển thị |
| **Tránh "mãi mãi" trong mọi sprite** | Trung bình | Sử dụng các chương trình phát sóng và sự kiện thay vì bỏ phiếu liên tục |
### Quản lý bản sao
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

### Danh sách kiểm tra tối ưu hóa
| Kỹ thuật | Tác động | Mô tả |
|----------|----------|-------------|
| **Chạy mà không cần làm mới màn hình** | Rất Cao | Khối tùy chỉnh bỏ qua kết xuất để tăng tốc độ |
| **Giảm thiểu các bản sao hoạt động** | Cao | Xóa các bản sao ngay khi không còn cần thiết |
| **Sử dụng chương trình phát sóng một cách tiết kiệm** | Trung bình | Quá nhiều chương trình phát sóng trên mỗi khung hình gây ra hiện tượng lag |
| **Đơn giản hóa trang phục** | Trung bình | Hình ảnh nhỏ hơn hiển thị nhanh hơn |
| **Giảm thao tác danh sách** | Trung bình | Tránh quét danh sách lớn mỗi khung hình |
| **Sử dụng khối "chờ"** | Thấp | Ngăn chặn tình trạng ngốn CPU trong các vòng lặp mãi mãi |
---

## Triển khai & Sử dụng trong Thế giới Thực
### Chia sẻ dự án
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

### Cách sử dụng giáo dục trong thế giới thực
| Bối cảnh | Scratch được sử dụng như thế nào | Quy mô |
|----------|-------------------|-------|
| **Trường K-12** | Nhập môn lập trình trong lớp CS | Được sử dụng ở hơn 190 quốc gia |
| **Câu lạc bộ viết mã** | Hội thảo Câu lạc bộ Scratch / CoderDojo | Hơn 3000 câu lạc bộ trên toàn thế giới |
| **Thư viện** | Chương trình lập trình sau giờ học | Hệ thống thư viện công cộng |
| **Giáo dục tại nhà** | Giáo dục lập trình theo nhịp độ riêng | Hàng triệu người học tại nhà |
| **Đại học CS0** | Các khóa học CS giới thiệu không chuyên ngành | Chương trình cầu nối đại học |
| **Khả năng tiếp cận** | Dạy lập trình cho người khiếm thị | Hỗ trợ trình đọc màn hình |
| **Trị liệu** | Phát triển kỹ năng nhận thức và vận động | Trị liệu nghề nghiệp |
### Scratch trong nghiên cứu giáo dục
Nghiên cứu đã chỉ ra rằng Scratch dạy một cách hiệu quả:
- **Tư duy tuần tự**: Chia vấn đề thành các bước theo thứ tự
- **Kỹ năng gỡ lỗi**: Tìm và sửa lỗi logic
- **Biểu hiện sáng tạo**: Kết hợp nghệ thuật, âm nhạc và lập trình
- **Hợp tác**: Phối lại và xây dựng dự án của người khác
- **Kiên trì**: Lặp lại các dự án để cải thiện chúng
---

## Chuyển đổi từ đầu
Sau khi học Scratch, các bước điển hình tiếp theo bao gồm:
| Ngôn ngữ tiếp theo | Tại sao |
|--------------|------|
| **Trăn** | Chuyển đổi tự nhiên nhất — cú pháp dễ đọc, khái niệm logic tương tự |
| **Javascript** | Nếu quan tâm đến web/trò chơi — phản hồi trực quan ngay lập tức |
| **Lua (thông qua Roblox/Love2D)** | Nếu quan tâm đến việc phát triển trò chơi |
| **Nhà phát minh ứng dụng** | Khối trực quan dành cho ứng dụng Android (cùng dòng MIT) |
| **Khối đá** | Thư viện lập trình trực quan của Google (khái niệm tương tự) |
### Ánh xạ khái niệm: Scratch to Python
| Khái niệm cào | Tương đương với Python |
|----------------|-------------------|
| `set [x] to 0`| `x = 0`|
| `change [x] by 1`| `x += 1`|
| `repeat 10`| `for i in range(10):`|
| `forever`| `while True:`|
| `if ... then`| `if ...:`|
| `broadcast [msg]`| Hệ thống gọi hàm hoặc sự kiện |
| `My Blocks`| `def function():`|
| `list`| `list = []`|
| `item 1 of [list]`| `list[0]`(được lập chỉ mục 0!) |
| `length of [list]`| `len(list)`|
---

## Khi nào nên sử dụng Scratch
| Kịch bản | Tại sao lại cào | Thay thế tốt hơn |
|----------|-------------|-------------------|
| Dạy trẻ em (8-16) viết mã | Được thiết kế đặc biệt cho việc này | — |
| Giới thiệu tư duy tính toán | Trực quan, không có lỗi cú pháp | — |
| Hội thảo trường học / câu lạc bộ mã hóa | Miễn phí, dựa trên trình duyệt, không cần thiết lập | — |
| Ý tưởng trò chơi nguyên mẫu một cách trực quan | Lặp lại nhanh | — |
| Phát triển chuyên môn | Không được thiết kế cho việc này | Python, JavaScript, bất kỳ ngôn ngữ văn bản nào |
| Giáo dục CS cấp đại học | Quá đơn giản | Python, Java, C |
---

## Hỏi đáp tổng hợp
**Q1: Scratch có thực sự là một ngôn ngữ lập trình không?**
Trả lời 1: Đúng, Scratch là ngôn ngữ lập trình thực sự, nhưng nó dựa trên hình ảnh chứ không dựa trên văn bản. Nó hỗ trợ tất cả các khái niệm lập trình cơ bản: biến, vòng lặp, điều kiện, hàm (khối tùy chỉnh), danh sách và lập trình hướng sự kiện. Sự khác biệt là bạn kéo và thả các khối thay vì gõ mã. Điều này giúp loại bỏ các lỗi cú pháp và làm cho việc lập trình trở nên dễ tiếp cận đối với những người học nhỏ tuổi.
**Q2: Làm cách nào để tạo các hàm tùy chỉnh (khối tùy chỉnh) trong Scratch?**
A2: Đi tới danh mục "Khối của tôi" và nhấp vào "Tạo khối". Đặt tên cho nó, thêm tham số nếu cần, sau đó xác định hành vi của nó bằng cách thêm các khối bên dưới nó. Các khối tùy chỉnh có thể lấy đầu vào (số, chuỗi, boolean) và có thể gọi các khối tùy chỉnh khác. Điều này cho phép lập trình mô-đun và tái sử dụng mã.
**Q3: Cách tốt nhất để xử lý logic trò chơi phức tạp trong Scratch là gì?**
Câu trả lời 3: Sử dụng các khối tùy chỉnh để sắp xếp logic, phát thông báo để phối hợp sự kiện giữa các họa tiết và sử dụng danh sách để lưu trữ trạng thái trò chơi (điểm số, cấp độ, kho đồ). Đối với AI phức tạp, hãy sử dụng máy trạng thái hữu hạn với các biến theo dõi trạng thái hiện tại. Sao chép các họa tiết cho nhiều kẻ thù và sử dụng "khi tôi bắt đầu làm bản sao" để đưa ra từng hành vi độc lập.
**Q4: Làm cách nào tôi có thể chia sẻ dữ liệu giữa các họa tiết trong Scratch?**
Câu trả lời 4: Sử dụng các biến toàn cục (được tạo mà không có "chỉ dành cho hình ảnh này") cho dữ liệu được chia sẻ như điểm số hoặc trạng thái trò chơi. Sử dụng tin nhắn quảng bá để kích hoạt các sự kiện trên các họa tiết. Để giao tiếp phức tạp hơn, hãy sử dụng danh sách làm cấu trúc dữ liệu dùng chung. Mỗi sprite có thể đọc và sửa đổi các biến và danh sách chung, cho phép phối hợp.
**Q5: Một số kỹ thuật nâng cao trong Scratch là gì?**
A5: Sử dụng khối bút để vẽ và tạo hiệu ứng hình ảnh. Triển khai raycasting cho đồ họa giống 3D. Sử dụng các biến đám mây cho trò chơi nhiều người chơi (yêu cầu trạng thái Scratcher). Tạo thế hệ thủ tục với các số và danh sách ngẫu nhiên. Sử dụng các khối tùy chỉnh với các tham số cho các thuật toán có thể tái sử dụng. Thử nghiệm cảm biến video và thao tác âm thanh cho các dự án tương tác.
---

## Chuỗi tư duy
### Vấn đề 1: Tạo game platformer
**Bước 1: Tìm hiểu vấn đề**
Chúng ta cần tạo một nền tảng trong đó nhân vật có thể di chuyển sang trái/phải, nhảy, tránh chướng ngại vật và thu thập vật phẩm.
**Bước 2: Xác định phương pháp tiếp cận**
- Sử dụng mô phỏng trọng lực với biến “rơi”
- Phát hiện va chạm mặt đất/va chạm bằng cách sử dụng màu sắc hoặc chạm vào sprite
- Lưu trữ dữ liệu cấp độ trong danh sách
- Sử dụng các khối tùy chỉnh cho logic nhảy và chuyển động
**Bước 3: Triển khai giải pháp**```scratch
// Gravity and movement
when green flag clicked
forever
  change y by (y velocity)
  if touching color [brown] then
    set [y velocity v] to [0]
    set [is jumping v] to [0]
  else
    change [y velocity v] by (-1)
  end
  
  if key [right arrow v] pressed then
    change x by (5)
  end
  if key [left arrow v] pressed then
    change x by (-5)
  end
  if key [space v] pressed and not <is jumping = [1]> then
    set [y velocity v] to [10]
    set [is jumping v] to [1]
  end
end
```

**Bước 4: Xác minh và tối ưu hóa**
Thử nghiệm nhảy trên các nền tảng khác nhau. Điều chỉnh trọng lực và độ cao nhảy để có cảm giác chơi game tốt. Thêm hình ảnh động khi chạy và nhảy. Thực hiện các điểm kiểm tra bằng cách sử dụng tin nhắn quảng bá.
---

### Bài toán 2: Tạo trò chơi đố vui có tính năng theo dõi điểm
**Bước 1: Tìm hiểu vấn đề**
Xây dựng trò chơi đố vui đặt câu hỏi, kiểm tra câu trả lời và theo dõi điểm số của người chơi.
**Bước 2: Xác định phương pháp tiếp cận**
- Lưu trữ câu hỏi và câu trả lời trong danh sách song song
- Sử dụng bộ đếm câu hỏi để theo dõi tiến độ
- Sử dụng khối "hỏi và chờ" để nhập liệu
- So sánh đáp án và cập nhật điểm
**Bước 3: Triển khai giải pháp**```scratch
when green flag clicked
set [score v] to [0]
set [question number v] to [1]

repeat (length of [questions v])
  ask (item (question number) of [questions v]) and wait
  if <(answer) = (item (question number) of [answers v])> then
    change [score v] by (1)
    say [Correct!] for (2) secs
  else
    say [Wrong!] for (2) secs
  end
  change [question number v] by (1)
end

say (join [Final score: ] join (score) [/5]) for (4) secs
```

**Bước 4: Xác minh và tối ưu hóa**
Kiểm tra với nhiều câu trả lời khác nhau bao gồm cả các trường hợp đặc biệt. Thêm phản hồi cho câu trả lời sai. Thực hiện tùy chọn thử lại. Thêm hiệu ứng âm thanh và phản hồi trực quan cho câu trả lời đúng/sai.
---

### Bài 3: Vẽ cây Fractal bằng bút
**Bước 1: Tìm hiểu vấn đề**
Tạo cây fractal đệ quy bằng cách sử dụng phần mở rộng pen.
**Bước 2: Xác định phương pháp tiếp cận**
- Sử dụng đệ quy để vẽ nhánh
- Mỗi nhánh chia thành 2 nhánh nhỏ hơn
- Sử dụng các góc ngẫu nhiên để tạo ra sự biến đổi tự nhiên
- Theo dõi độ dài nhánh và giảm dần theo từng cấp độ đệ quy
**Bước 3: Triển khai giải pháp**```scratch
define draw branch (length)
pen down
glide (1) secs to (x:(x position) + (length * cos of direction)) (y:(y position) + (length * sin of direction))
pen up

if <(length) > [5]> then
  turn right (pick random (10) to (45))
  draw branch (length * 0.7)
  turn left (pick random (20) to (90))
  draw branch (length * 0.7)
end

when green flag clicked
erase all
goto x:(0) y:(-150)
point in direction (90)
draw branch (100)
```

**Bước 4: Xác minh và tối ưu hóa**
Điều chỉnh ngưỡng chiều dài cành và phạm vi góc cho cây thẩm mỹ. Thêm lá ở đầu cành bằng cách thay đổi màu sắc. Thực hiện các kiểu cây khác nhau. Lưu bản vẽ dưới dạng hình ảnh.
---

## Bản tóm tắt
Scratch không phải là ngôn ngữ lập trình theo nghĩa truyền thống - nó là một môi trường học tập. Thiên tài của nó là xóa bỏ mọi rào cản giữa một đứa trẻ và niềm vui khi tạo ra thứ gì đó có tính tương tác. Bằng cách tập trung vào các khái niệm hơn là cú pháp, Scratch dạy các nguyên tắc cơ bản về lập trình có thể chuyển sang bất kỳ ngôn ngữ nào. Để giới thiệu chương trình cho những người học trẻ tuổi, Scratch là tiêu chuẩn vàng.