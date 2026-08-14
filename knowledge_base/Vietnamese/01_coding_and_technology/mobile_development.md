---
# Metadata
title: "Mobile Development"
description: "iOS, Android, React Native, Flutter, mobile architecture"
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
tags: [mobile, development, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Phát triển di động
Phát triển thiết bị di động là hoạt động xây dựng ứng dụng cho điện thoại thông minh và máy tính bảng - chủ yếu dành cho iOS (Apple) và Android (Google). Nó bao gồm mọi thứ, từ thiết kế giao diện người dùng cho màn hình nhỏ đến quản lý thời lượng pin, xử lý tình trạng mất ổn định của mạng và phân phối ứng dụng qua các cửa hàng. Lĩnh vực này đã phát triển đáng kể, với các khung đa nền tảng hiện đang cạnh tranh với sự phát triển gốc trong hầu hết các trường hợp sử dụng.
---

## Cảnh quan di động
| Nền tảng | Nhà phát triển | (Các) ngôn ngữ | Cửa hàng | Thị phần (Toàn cầu) |
|----------|-------------|-------------|-------|----------------------|
| **Android** | Google | Kotlin, Java | Google Play | ~72% |
| **iOS** | Táo | Swift, Mục tiêu-C | Cửa hàng ứng dụng | ~27% |
---

## Phát triển bản địa
###Android
| Khía cạnh | Chi tiết |
|--------|----------|
| **Ngôn ngữ** | Kotlin (chính), Java (cũ) |
| **Khung giao diện người dùng** | Jetpack Compose (hiện đại), bố cục XML (cũ) |
| **Xây dựng hệ thống** | Lớp |
| **IDE** | Studio Android |
| **SDK tối thiểu** | Nhà phát triển lựa chọn; API mục tiêu nhất 24+ (Android 7.0, 2016) |
| **Phân phối** | Cửa hàng Google Play; cửa hàng thay thế ở một số thị trường |
###iOS
| Khía cạnh | Chi tiết |
|--------|----------|
| **Ngôn ngữ** | Swift (chính), Objective-C (cũ) |
| **Khung giao diện người dùng** | SwiftUI (hiện đại), UIKit (trưởng thành) |
| **Xây dựng hệ thống** | Hệ thống xây dựng Xcode |
| **IDE** | Xcode (chỉ macOS) |
| **Phiên bản tối thiểu** | Nhà phát triển lựa chọn; nhắm đến iOS 16+ nhiều nhất |
| **Phân phối** | Apple App Store (tùy chọn duy nhất cho hầu hết các ứng dụng) |
---

## Khung đa nền tảng
Xây dựng một lần, triển khai cho cả iOS và Android.
| Khung | Ngôn ngữ | Kết xuất | Hiệu suất | Tốt nhất cho |
|----------|----------|-------------|-------------|----------|
| **Rung rinh** | Phi tiêu | Động cơ tùy chỉnh (Skia/Cánh quạt) | Gần bản xứ | Giao diện người dùng tùy chỉnh phong phú; cái nhìn nhất quán trên các nền tảng |
| **Phản ứng gốc** | JavaScript/TypeScript | Các thành phần gốc thông qua bridge | Tốt (Kiến trúc mới cải thiện điều này) | Các nhóm có kinh nghiệm về web/JS |
| **Đa nền tảng Kotlin** | Kotlin | Giao diện người dùng gốc trên mỗi nền tảng | Bản địa | Chia sẻ logic kinh doanh; giao diện người dùng gốc |
| **MAUI** (.NET) | C# | Điều khiển gốc | Tốt | Các nhóm .NET; ứng dụng doanh nghiệp |
| **Ionic / Tụ điện** | HTML/CSS/JS | WebView | Hạ | Ứng dụng đơn giản; nhóm web |
### Flutter vs React Native
| Khía cạnh | Rung | Phản ứng bản địa |
|--------|----------|-------------|
| **Ngôn ngữ** | Phi tiêu | JavaScript/TypeScript |
| **Hiển thị giao diện người dùng** | Tự vẽ mọi thứ (nhất quán trên các nền tảng) | Sử dụng các thành phần gốc (giao diện dành riêng cho nền tảng) |
| **Tải lại nóng** | Xuất sắc | Tốt |
| **Hệ sinh thái** | Phát triển nhanh chóng; dựa trên widget | Lớn; hệ sinh thái npm |
| **Đường cong học tập** | Cần học phi tiêu | Dễ dàng hơn cho các nhà phát triển web |
| **Tích hợp nền tảng** | Kênh nền tảng cho mã gốc | Mô-đun gốc qua cầu nối |
| **Hiệu suất** | Xuất sắc; gần bản địa | Tốt; chi phí cầu (giảm nhờ Kiến trúc mới) |
---

## Các mẫu kiến ​​trúc di động
| Mẫu | Mô tả | Khi nào nên sử dụng |
|----------|-------------|-------------|
| **MVC** | Model-View-Controller | Ứng dụng đơn giản; quen thuộc với các nhà phát triển web |
| **MVVM** | Model-View-ViewModel; ràng buộc dữ liệu | Ứng dụng di động hiện đại nhất |
| **MVI** | Model-View-Intent; luồng dữ liệu một chiều | Quản lý nhà nước phức tạp; Rung (với BLoC/Riverpod) |
| **Kiến trúc sạch** | Các lớp có đảo ngược phụ thuộc | Các đội lớn; logic kinh doanh phức tạp |
---

## Mối quan tâm chính về thiết bị di động
### Thiết kế ngoại tuyến đầu tiên
Ứng dụng di động phải hoạt động mà không có internet đáng tin cậy.
| Chiến lược | Mô tả |
|----------|-------------|
| **Cơ sở dữ liệu địa phương** | Lưu trữ dữ liệu trên thiết bị (SQLite, Room, CoreData, Realm) |
| **Chiến lược đồng bộ hóa** | Đồng bộ với máy chủ khi trực tuyến; giải quyết xung đột |
| **Giao diện người dùng lạc quan** | Cập nhật giao diện người dùng ngay lập tức; hòa giải khi máy chủ phản hồi |
| **Bộ nhớ đệm** | Phản hồi API bộ đệm; phục vụ từ bộ nhớ đệm khi ngoại tuyến |
### Hiệu suất
| Mối quan tâm | Giải pháp |
|----------|----------|
| **Thời gian khởi động ứng dụng** | Tải chậm; giảm thiểu công việc khởi tạo |
| **Sử dụng bộ nhớ** | Nén hình ảnh; tránh rò rỉ bộ nhớ; sử dụng các công cụ định hình |
| **Hết pin** | Giảm công việc nền; yêu cầu mạng hàng loạt; sử dụng dịch vụ định vị hiệu quả |
| **Hiệu quả mạng** | Nén tải trọng; sử dụng phân trang; bộ nhớ đệm tích cực |
| **Cuộn danh sách** | Chế độ xem tái chế; sử dụng tính năng tải chậm cho hình ảnh |
### Bảo vệ
| Mối quan tâm | Giải pháp |
|----------|----------|
| **Dữ liệu ở trạng thái nghỉ** | Mã hóa dữ liệu nhạy cảm (Keychain trên iOS, EncryptedSharedPreferences trên Android) |
| **Mạng** | Luôn là HTTPS; ghim chứng chỉ cho các ứng dụng nhạy cảm |
| **Xác thực** | Sinh trắc học (Face ID, vân tay); OAuth; lưu trữ mã thông báo |
| **Làm rối mã** | ProGuard/R8 dành cho Android; mã bit cho iOS |
| **Bẻ khóa/phát hiện root** | Phát hiện các thiết bị bị xâm nhập; giới hạn chức năng |
---

## Vòng đời ứng dụng
| Tiểu bang | Mô tả | Phải làm gì |
|-------|-------------|-------------|
| **Tiền cảnh (hoạt động)** | Người dùng đang tương tác với ứng dụng | Hoạt động bình thường |
| **Bối cảnh** | Ứng dụng không hiển thị nhưng vẫn còn trong bộ nhớ | Tạm dừng hoạt ảnh; lưu trạng thái |
| **Bị đình chỉ** | OS đã đóng băng ứng dụng để tiết kiệm tài nguyên | Không có gì; ứng dụng bị đóng băng |
| **Đã chấm dứt** | Hệ điều hành đã giết ứng dụng để giải phóng bộ nhớ | Khôi phục trạng thái trong lần khởi chạy tiếp theo |
---

## Thông báo đẩy
| Nền tảng | Dịch vụ | Giao thức |
|----------|----------|----------|
| **iOS** | APN (Dịch vụ thông báo đẩy của Apple) | HTTP/2 |
| **Android** | FCM (Nhắn tin qua đám mây Firebase) | HTTP/v1 |
| Loại thông báo | Mô tả |
|-------------------|-------------|
| **Thông báo dữ liệu** | Im lặng; ứng dụng xử lý tải trọng | Cập nhật cơ bản |
| **Hiển thị thông báo** | Hiển thị trong khay thông báo | Cảnh báo người dùng |
| **Thông báo phong phú** | Bao gồm hình ảnh, hành động hoặc giao diện người dùng tùy chỉnh | Tăng cường sự tham gia của người dùng |
---

## Phân phối ứng dụng
| Nền tảng | Cửa hàng | Thời gian xét duyệt | Cắt giảm doanh thu |
|----------|-------|-------------|-------------|
| **iOS** | Cửa hàng ứng dụng | 24-48 giờ | 30% (15% cho doanh nghiệp nhỏ) |
| **Android** | Google Play | Giờ đến ngày | 30% (15% cho 1 triệu USD đầu tiên) |
| **Android (thay thế)** | Cửa hàng Samsung Galaxy, Cửa hàng ứng dụng Amazon, F-Droid | Khác nhau | Khác nhau |
### CI/CD dành cho thiết bị di động
| Công cụ | Mục đích |
|------|----------|
| **Đường nhanh** | Tự động hóa bản dựng, ảnh chụp màn hình, ký và triển khai |
| **Hành động GitHub** | CI/CD với trình chạy macOS cho bản dựng iOS |
| **Bitrise** | CI/CD tập trung vào thiết bị di động |
| **Trung tâm ứng dụng** (Microsoft) | Xây dựng, thử nghiệm, phân phối (đang hoàng hôn; các lựa chọn thay thế đang xuất hiện) |
| **EAS** (Dịch vụ ứng dụng Expo) | Xây dựng đám mây cho React Native/Expo |
---

##Thử nghiệm
| Loại | Công cụ | Mục đích |
|------|-------|---------|
| **Kiểm tra đơn vị** | JUnit, XCTest | Kiểm tra logic kinh doanh |
| **Kiểm tra tiện ích** | Kiểm tra Widget Flutter, Robolectric | Kiểm tra các thành phần UI một cách riêng biệt |
| **Thử nghiệm tích hợp** | Espresso (Android), XCUITest (iOS), Tích hợp Flutter | Kiểm tra tương tác thành phần |
| **Thử nghiệm E2E** | Giải độc, Appium, Maestro | Kiểm tra toàn bộ luồng người dùng trên thiết bị thực/mô phỏng |
| **Kiểm tra hiệu suất** | Trình phân tích tài nguyên Android, Công cụ (iOS) | Đo tốc độ khung hình, bộ nhớ, CPU |
---

## Bản tóm tắt
Phát triển thiết bị di động cung cấp sự lựa chọn giữa gốc (hiệu suất tốt nhất, dành riêng cho nền tảng) và đa nền tảng (cơ sở mã chung, lặp lại nhanh hơn). Flutter và React Native đã phát triển đến mức đa nền tảng là lựa chọn phù hợp cho hầu hết các ứng dụng. Những thách thức cốt lõi vẫn giữ nguyên bất kể khuôn khổ: thiết kế ưu tiên ngoại tuyến, hiệu suất trên phần cứng hạn chế, hiệu quả sử dụng pin, bảo mật trên các thiết bị không đáng tin cậy và điều hướng các quy trình đánh giá cửa hàng ứng dụng. Lĩnh vực này trao thưởng cho các nhà phát triển nghĩ đến trải nghiệm người dùng trước tiên — khởi động nhanh, cuộn mượt mà và xử lý khéo léo khi kết nối kém.