<!--
---
# Metadata
title: "Accessibility and Inclusive Design"
description: "WCAG, inclusive UX, assistive technology, accessible coding"
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
tags: [accessibility, inclusive, design, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Khả năng tiếp cận và thiết kế toàn diện
Khả năng truy cập (thường được viết tắt là a11y) là phương pháp làm cho phần mềm có thể sử dụng được cho mọi người - bao gồm cả những người bị khuyết tật về thị giác, thính giác, vận động, nhận thức và thần kinh. Đó là một yêu cầu pháp lý ở nhiều khu vực pháp lý và là một thông lệ kỹ thuật tiêu chuẩn. Phần mềm có thể truy cập là phần mềm tốt hơn cho mọi người vì các quyết định thiết kế hỗ trợ người dùng khuyết tật — cấu trúc rõ ràng, điều hướng bàn phím, độ tương phản vừa đủ, văn bản dễ đọc — cải thiện trải nghiệm cho tất cả người dùng.
---

## Ai được hưởng lợi từ khả năng tiếp cận?
| Loại khuyết tật | Ví dụ | Công nghệ hỗ trợ |
|----------------|----------|----------------------|
| **Trực quan** | Mù, thị lực kém, mù màu | Trình đọc màn hình (JAWS, NVDA, VoiceOver); kính lúp; chế độ tương phản cao |
| **Thính giác** | Điếc, lãng tai | Chú thích; bảng điểm; cảnh báo trực quan |
| **Động cơ** | Khéo léo hạn chế, tê liệt, run rẩy | Điều hướng chỉ bằng bàn phím; điều khiển bằng giọng nói; chuyển đổi thiết bị; theo dõi mắt |
| **Nhận thức** | Chứng khó đọc, ADHD, chứng tự kỷ, suy giảm trí nhớ | Ngôn ngữ rõ ràng; điều hướng nhất quán; giảm phiền nhiễu |
| **Tạm thời** | Gãy tay, nắng chói chang, môi trường ồn ào | Chỗ ở tương tự như khuyết tật vĩnh viễn |
| **Tình huống** | Ôm con, lái xe, một tay bận rộn | Giao diện giọng nói; mục tiêu cảm ứng lớn |
**Thông tin chi tiết quan trọng**: các tính năng trợ năng được thiết kế cho người dùng khuyết tật sẽ giúp ích cho tất cả mọi người. Đường cắt lề đường (dốc ở vỉa hè) được thiết kế dành cho xe lăn nhưng được sử dụng bởi các bậc cha mẹ có xe đẩy, nhân viên giao hàng bằng xe đẩy và khách du lịch mang theo hành lý.
---

## Khả năng truy cập web (WCAG)
Nguyên tắc truy cập nội dung web (WCAG) là tiêu chuẩn quốc tế về khả năng truy cập web.
### Nguyên tắc WCAG (POUR)
| Nguyên tắc | Yêu cầu |
|----------||-------------|
| **Có thể cảm nhận được** | Thông tin phải được trình bày theo cách người dùng có thể cảm nhận được (văn bản thay thế, chú thích, bố cục có thể điều chỉnh) |
| **Có thể hoạt động** | Giao diện phải có thể điều hướng và sử dụng được (có thể truy cập bàn phím, đủ thời gian, không có nội dung gây giật) |
| **Dễ hiểu** | Thông tin và hoạt động phải dễ hiểu (có thể đọc được, có thể dự đoán được, hỗ trợ đầu vào) |
| **Mạnh mẽ** | Nội dung phải hoạt động với các công nghệ hỗ trợ hiện tại và tương lai |
### Mức độ phù hợp WCAG
| Cấp độ | Yêu cầu | Mục tiêu điển hình |
|-------|-------------|---------------|
| **A** | Mức tối thiểu; 30 tiêu chí thành công | Tối thiểu hợp pháp ở một số khu vực pháp lý |
| **AA** | Giải quyết các rào cản phổ biến nhất | Mục tiêu tiêu chuẩn cho hầu hết các tổ chức |
| **AAA** | Mức cao nhất; không phải nội dung nào cũng có thể đạt được điều đó | Nội dung chuyên ngành; trang web giáo dục |
### Tiêu chí thành công chính (Cấp AA)
| Tiêu chí | Yêu cầu | Làm thế nào để đạt được |
|----------|-------------|--------------|
| **1.1.1 Nội dung phi văn bản** | Tất cả hình ảnh đều có văn bản thay thế |  Thuộc tính `alt`; `aria-label`cho biểu tượng |
| **1.3.1 Thông tin và mối quan hệ** | Cấu trúc được truyền tải theo chương trình | HTML ngữ nghĩa; tiêu đề; danh sách; cột mốc |
| **Độ tương phản 1.4.3 (tối thiểu)** | Văn bản có tỷ lệ tương phản ít nhất là 4,5:1 | Kiểm tra bằng máy kiểm tra độ tương phản; chọn bảng màu dễ tiếp cận |
| **1.4.4 Thay đổi kích thước văn bản** | Văn bản có thể được thay đổi kích thước đến 200% mà không bị mất | Sử dụng đơn vị tương đối (rem, em); thiết kế đáp ứng |
| **Bàn phím 2.1.1** | Tất cả chức năng có sẵn qua bàn phím | Không có bẫy bàn phím; chỉ báo tiêu điểm có thể nhìn thấy |
| **2.4.3 Thứ tự lấy nét** | Thứ tự tập trung duy trì ý nghĩa và khả năng hoạt động | Thứ tự tab hợp lý; Thứ tự DOM khớp với thứ tự trực quan |
| **2.4.7 Có thể nhìn thấy tiêu điểm** | Tiêu điểm bàn phím được chỉ định trực quan | Kiểu CSS `:focus-visible`; không bao giờ`outline: none`mà không thay thế |
| **3.3.2 Nhãn hoặc hướng dẫn** | Đầu vào có nhãn |  Phần tử `<label>`; `aria-label`|
| **4.1.2 Tên, vai trò, giá trị** | Các thành phần giao diện người dùng có tên và vai trò có thể truy cập | thuộc tính ARIA; HTML ngữ nghĩa |
---

## ARIA (Ứng dụng Internet phong phú có thể truy cập)
ARIA thêm thông tin trợ năng vào các phần tử HTML không có ngữ nghĩa tích hợp.
### Vai trò ARIA
| Vai trò | Mục đích | Ví dụ |
|------|----------|----------|
| `button`| Xác định một phần tử là một nút |`<div>`được tạo kiểu như một nút |
| `dialog`| Hộp thoại phương thức hoặc không phương thức | Các thành phần phương thức tùy chỉnh |
| `tablist`/`tab`/`tabpanel`| Giao diện tab | Thành phần tab tùy chỉnh |
| `alert`| Thông báo quan trọng xuất hiện động | Thông báo lỗi |
| `progressbar`| Chỉ báo tiến độ | Đang tải trạng thái |
| `menu`/`menuitem`| Điều hướng menu | Menu thả xuống |
### Thuộc tính ARIA
| Thuộc tính | Mục đích | Ví dụ |
|----------||----------|----------|
| `aria-label`| Tên có thể truy cập khi không có văn bản hiển thị | Nút chỉ có biểu tượng:`aria-label="Search"`|
| `aria-describedby`| Liên kết phần tử với mô tả của nó | Trường biểu mẫu có văn bản trợ giúp |
| `aria-expanded`| Cho biết liệu một phần có được mở rộng hay không | Đàn xếp; thả xuống |
| `aria-hidden`| Ẩn phần tử khỏi công nghệ hỗ trợ | Biểu tượng trang trí |
| `aria-live`| Thông báo thay đổi nội dung động | Cập nhật trực tiếp; thông báo |
| `aria-disabled`| Cho biết phần tử bị vô hiệu hóa | Nút màu xám |
### Quy tắc đầu tiên của ARIA
> **Không sử dụng ARIA nếu thay vào đó bạn có thể sử dụng HTML gốc.**`<button>`đã có thể truy cập được.`<div role="button">`yêu cầu bạn thêm xử lý bàn phím, quản lý tiêu điểm và hỗ trợ trình đọc màn hình theo cách thủ công. Trước tiên hãy sử dụng HTML ngữ nghĩa; ARIA chỉ khi các phần tử gốc không thể thực hiện được công việc.
---

## Điều hướng bàn phím
| Chìa khóa | Hành vi dự kiến ​​|
|------|-------------------|
| **Tab** | Di chuyển tiêu điểm đến phần tử tương tác tiếp theo |
| **Shift + Tab** | Di chuyển tiêu điểm đến phần tử tương tác trước đó |
| **Nhập / Dấu cách** | Kích hoạt phần tử tập trung (nút, liên kết) |
| **Phím mũi tên** | Điều hướng trong các thành phần (menu, tab, nhóm radio) |
| **Thoát** | Đóng hộp thoại, menu hoặc cửa sổ bật lên |
| **Trang chủ / Kết thúc** | Chuyển tới mục đầu tiên/cuối cùng trong danh sách |
### Bẫy bàn phím phổ biến
| Vấn đề | Sửa chữa |
|----------|------|
| Focus vào một thành phần nhưng không thể rời đi | Đảm bảo Tab di chuyển tiêu điểm ra ngoài; xử lý Thoát |
| Modal không bẫy tiêu điểm | Trọng tâm phải xoay vòng trong phương thức; quay lại kích hoạt khi đóng |
| Các thành phần tùy chỉnh không phản hồi với bàn phím | Thêm trình xử lý nhấn phím cho Enter, Space, mũi tên |
---

## Màu sắc và thiết kế hình ảnh
| Hướng dẫn | Yêu cầu |
|----------||-------------|
| **Tỷ lệ tương phản** | 4,5:1 đối với văn bản thông thường; 3:1 cho văn bản lớn (18pt+ hoặc 14pt+ in đậm) |
| **Đừng chỉ dựa vào màu sắc** | Sử dụng biểu tượng, văn bản hoặc mẫu ngoài màu sắc |
| **Chỉ báo lấy nét** | Luôn nhìn thấy được; độ tương phản cao; không bao giờ được gỡ bỏ mà không thay thế |
| **Thay đổi kích thước văn bản** | Bố cục phải hoạt động ở mức thu phóng 200% |
| **Đáp ứng** | Nội dung phải chỉnh lại ở độ rộng 320px (di động) |
### Những cân nhắc về bệnh mù màu
| Loại | Màu sắc bị ảnh hưởng | Mẹo thiết kế |
|------|-------------------|-------------|
| **Deuteranopia** | Đỏ-xanh (phổ biến nhất) | Đừng sử dụng màu đỏ/xanh lá cây để truyền đạt trạng thái; sử dụng biểu tượng + màu sắc |
| **Protanopia** | Đỏ-xanh | Tương tự như trên |
| **Tritanopia** | Xanh-vàng | Đừng sử dụng màu xanh/vàng làm điểm khác biệt duy nhất |
---

## Kiểm tra khả năng truy cập
| Phương pháp | Công cụ | Nó bắt được gì |
|--------|------|----------------|
| **Quét tự động** | rìu, Ngọn hải đăng, WAVE | Thiếu văn bản thay thế; vấn đề tương phản; Lỗi ARIA |
| **Kiểm tra bàn phím** | Hướng dẫn sử dụng: rút chuột, chỉ sử dụng bàn phím | Thứ tự tập trung; bẫy bàn phím; người xử lý bị thiếu |
| **Kiểm tra trình đọc màn hình** | NVDA (miễn phí), VoiceOver (macOS), JAWS | Thiếu nhãn; cấu trúc kém; những thay đổi không báo trước |
| **Thử nghiệm thu phóng** | Thu phóng trình duyệt tới 200%, 400% | vỡ bố cục; văn bản bị cắt bớt; vấn đề tràn |
| **Độ tương phản màu sắc** | Trình kiểm tra độ tương phản WebAIM, plugin Stark | Tỷ lệ tương phản không đủ |
| **Thử nghiệm người dùng** | Kiểm tra với người dùng khuyết tật | Rào cản trong thế giới thực mà các công cụ tự động bỏ qua |
---

## Yêu cầu pháp lý
| Luật | Vùng | Yêu cầu |
|------|--------|-------------|
| **ADA** (Đạo luật về Người khuyết tật Hoa Kỳ) | Mỹ | Trang web của cơ sở lưu trú công cộng phải truy cập được |
| **Mục 508** | Hoa Kỳ (liên bang) | CNTT của các cơ quan liên bang phải có thể truy cập được |
| **EAA** (Đạo luật tiếp cận châu Âu) | EU (2025+) | Sản phẩm và dịch vụ phải đáp ứng yêu cầu về khả năng tiếp cận |
| **EN 301 549** | EU | Tiêu chuẩn kỹ thuật về tiếp cận CNTT |
| **ACA** (Đạo luật về khả năng tiếp cận của Canada) | Canada | Chính phủ và các ngành được quản lý |
| **Đạo luật Bình đẳng 2010** | Vương quốc Anh | Nhà cung cấp dịch vụ phải có những điều chỉnh hợp lý |
---

## Khả năng truy cập di động
| Nền tảng | Hướng dẫn | Công cụ chính |
|----------|--------------|----------|
| **iOS** | Nguyên tắc giao diện con người của Apple (phần Trợ năng) | VoiceOver; Loại động; Điều khiển chuyển mạch |
| **Android** | Hướng dẫn về khả năng truy cập của Android | TalkBack; Chuyển đổi quyền truy cập; Chọn để nói |
| Mối quan tâm về di động | Giải pháp |
|--------------|----------|
| **Mục tiêu chạm** | Tối thiểu 44×44 điểm (iOS) / 48×48 dp (Android) |
| **Hỗ trợ trình đọc màn hình** | Mô tả nội dung; nhãn khả năng tiếp cận |
| **Độ nhạy chuyển động** | Tôn trọng`prefers-reduced-motion`; tránh hoạt ảnh tự động phát |
| **Kích thước văn bản động** | Hỗ trợ kích thước phông chữ hệ thống; sử dụng các đơn vị văn bản có thể mở rộng |
---

## Bản tóm tắt
Khả năng tiếp cận là một nguyên tắc thiết kế sẽ cung cấp thông tin cho mọi quyết định ngay từ đầu chứ không phải một tính năng được thêm vào cuối. Sử dụng HTML ngữ nghĩa. Đảm bảo điều hướng bàn phím hoạt động. Duy trì đủ độ tương phản màu sắc. Cung cấp các lựa chọn thay thế văn bản cho nội dung phi văn bản. Kiểm tra với trình đọc màn hình và người dùng bị khuyết tật. Kết quả là phần mềm hoạt động tốt hơn cho tất cả mọi người — bao gồm cả những người bị suy giảm tạm thời, hạn chế về tình huống, thiết bị cũ hơn, kết nối chậm và nhiều cách sử dụng trong thế giới thực khác với môi trường phát triển được kiểm soát.