---
# Metadata
title: "Blockchain and Distributed Systems"
description: "Consensus, smart contracts, DeFi, Byzantine fault tolerance"
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
tags: [blockchain, distributed, systems, coding-and-technology]
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
# Chuỗi khối và hệ thống phân tán
Blockchain là một loại hệ thống phân tán cụ thể — một sổ cái phi tập trung, chỉ bổ sung, trong đó các bản ghi (khối) được liên kết bằng các hàm băm mật mã. Hệ thống phân tán là lĩnh vực rộng hơn giúp nhiều máy tính hoạt động cùng nhau như một. Cả hai khái niệm đều quan trọng để hiểu cơ sở hạ tầng hiện đại, từ tiền điện tử đến cơ sở dữ liệu phân tán đến các thuật toán đồng thuận hỗ trợ các dịch vụ toàn cầu.
---

## Nguyên tắc cơ bản về hệ thống phân tán
### Tại sao lại là hệ thống phân tán?
| Động lực | Mô tả |
|----------||-------------|
| **Khả năng mở rộng** | Thêm nhiều máy để xử lý nhiều tải hơn |
| **Khả năng chịu lỗi** | Hệ thống tiếp tục hoạt động ngay cả khi một số máy bị lỗi |
| **Phân bố địa lý** | Phục vụ người dùng từ các trung tâm dữ liệu lân cận |
| **Chuyên môn** | Các máy khác nhau xử lý các nhiệm vụ khác nhau |
### Các khái niệm chính
| Khái niệm | Mô tả | Thử thách |
|----------|-------------|----------|
| **Đồng thuận** | Bắt tất cả các nút đồng ý về một giá trị | Phân vùng mạng; Lỗi Byzantine |
| **Sao chép** | Sao chép dữ liệu qua nhiều nút | Tính nhất quán và tính sẵn có |
| **Phân vùng (sharding)** | Chia dữ liệu giữa các nút | Điểm nóng; truy vấn chéo |
| **Mô hình nhất quán** | Đảm bảo về những gì độc giả khác nhau nhìn thấy | Tính nhất quán cao thì chậm; tính nhất quán cuối cùng có thể khiến người dùng ngạc nhiên |
| **Định lý CAP** | Bạn chỉ có thể có 2 trong số: Tính nhất quán, Tính khả dụng, Dung sai phân vùng | Trong thực tế, cần có dung sai phân vùng; chọn C hoặc A |
### Định lý CAP
| Lựa chọn | Những gì bạn nhận được | Những gì bạn từ bỏ | Ví dụ |
|--------|-------------|--------|---------|
| **CP** | Tính nhất quán + khả năng chịu phân vùng | Một số nút có thể không có sẵn trong quá trình phân vùng | HBase, MongoDB, Redis |
| **AP** | Có sẵn + khả năng chịu phân vùng | Các lần đọc có thể trả về dữ liệu cũ | Cassandra, DynamoDB, CouchDB |
| **CA** | Nhất quán + có sẵn | Không thể chịu đựng được việc phân vùng mạng | Cơ sở dữ liệu một nút (không thực sự được phân phối) |
---

## Thuật toán đồng thuận
Làm thế nào để các nút phân phối thống nhất về trạng thái của hệ thống?
| Thuật toán | Loại | Dung sai lỗi | Được sử dụng trong |
|----------|------|-------------------|----------|
| **Paxos** | Khả năng chịu lỗi khi va chạm | Lên đến f lỗi với các nút 2f+1 | Google mũm mĩm; lý thuyết nền tảng |
| **Bè** | Khả năng chịu lỗi khi va chạm | Lên đến f lỗi với các nút 2f+1 | etcd, Lãnh sự, TiKV |
| **PBFT** | Khả năng chịu lỗi Byzantine | Lên đến f lỗi với các nút 3f+1 | Vải Hyperledger |
| **Bằng chứng công việc** | Khả năng chịu lỗi Byzantine | Phụ thuộc vào sức mạnh băm | Bitcoin |
| **Bằng chứng cổ phần** | Khả năng chịu lỗi Byzantine | Phụ thuộc vào cổ phần | Ethereum 2.0, Cardano |
### Bè (Giản thể)
| Vai trò | Trách nhiệm |
|------|--------------|
| **Lãnh đạo** | Xử lý mọi yêu cầu của khách hàng; gửi các mục nhật ký cho người theo dõi |
| **Người theo dõi** | Đáp ứng yêu cầu của lãnh đạo; phiếu trong cuộc bầu cử |
| **Ứng viên** | Yêu cầu bỏ phiếu để trở thành lãnh đạo |
1. Tất cả các nút bắt đầu với tư cách là người theo dõi
2. Nếu người theo dõi không nhận được phản hồi từ người lãnh đạo trong thời gian chờ bầu cử, người đó sẽ trở thành ứng cử viên
3. Ứng viên xin phiếu bầu; người có nhiều phiếu bầu nhất sẽ trở thành người đứng đầu
4. Người lãnh đạo sao chép các mục nhật ký cho người theo dõi
5. Khi đa số xác nhận, mục nhập được cam kết
---

## Chuỗi khối
### Blockchain hoạt động như thế nào
| Thành phần | Mô tả |
|----------||-------------|
| **Chặn** | Một loạt giao dịch + siêu dữ liệu + hàm băm của khối trước đó |
| **Băm** | Dấu vân tay mật mã của nội dung khối |
| **Chuỗi** | Mỗi khối tham chiếu hàm băm của khối trước đó, tạo ra một chuỗi bất biến |
| **Đồng thuận** | Những người tham gia mạng đồng ý về những khối cần thêm |
| **Cây Merkle** | Cây băm tóm tắt tất cả các giao dịch trong một khối |
### Tại sao Blockchain khó bị giả mạo
1. Mỗi khối chứa hàm băm của khối trước đó
2. Thay đổi bất kỳ giao dịch nào cũng sẽ thay đổi hàm băm của khối
3. Hàm băm thay đổi sẽ phá vỡ chuỗi — tất cả các khối tiếp theo trở nên không hợp lệ
4. Kẻ tấn công sẽ cần khai thác lại tất cả các khối tiếp theo VÀ kiểm soát >50% mạng
### Các loại Blockchain
| Loại | Truy cập | Trình xác thực | Ví dụ |
|------|--------|-------------|---------|
| **Công khai (không được phép)** | Bất cứ ai cũng có thể đọc và viết | Đồng thuận mở (PoW, PoS) | Bitcoin, Ethereum |
| **Riêng tư (được phép)** | Hạn chế truy cập | Trình xác thực đã biết | Sổ cái, Corda |
| **Tập đoàn** | Được quản lý bởi một nhóm tổ chức | Người xác thực được chọn | R3 Corda cho ngân hàng |
### Hợp đồng thông minh
Mã tự thực thi được lưu trữ trên blockchain chạy khi đáp ứng các điều kiện xác định trước.
| Nền tảng | Ngôn ngữ | Tính năng đáng chú ý |
|----------|----------|--------|
| **Ethereum** | Vững chắc, Vyper | Hệ sinh thái hợp đồng thông minh lớn nhất |
| **Solana** | Rỉ sét, C | Thông lượng cao; phí thấp |
| **Cardano** | Haskell (Plutus) | Đánh giá ngang hàng; xác minh chính thức |
| **Siêu sổ cái** | Đi, Java, JavaScript | Doanh nghiệp; được phép |
---

## Tiền điện tử
| Tiền tệ | Đồng thuận | Cung cấp | Sử dụng Chính |
|----------|----------|--------|-------------|
| **Bitcoin** | Bằng chứng công việc | 21 triệu (giới hạn) | Lưu trữ giá trị; vàng kỹ thuật số |
| **Ethereum** | Bằng chứng cổ phần | Không có nắp cứng | Hợp đồng thông minh; DeFi; NFT |
| **Solana** | Bằng chứng cổ phần + Bằng chứng lịch sử | Không có nắp cứng | Giao dịch tốc độ cao |
| **Cardano** | Bằng chứng về cổ phần (Ouroboros) | 45 tỷ (có trần) | Phương pháp học thuật; tính bền vững |
---

## Cơ sở dữ liệu phân tán
| Cơ sở dữ liệu | Kiến trúc | Tính nhất quán | Tốt nhất cho |
|----------|-------------|-------------|----------|
| **Cassandra** | Cột rộng; ngang hàng | Có thể điều chỉnh (cuối cùng đến đại biểu) | Thông lượng ghi cao; chuỗi thời gian |
| **MongoDB** | Tài liệu; bộ bản sao | Cuối cùng (với tùy chọn nhất quán nhân quả) | Lược đồ linh hoạt; phát triển nhanh chóng |
| **GiánDB** | SQL phân tán; Raft đồng thuận | Mạnh mẽ | SQL phân tán; triển khai toàn cầu |
| **TiDB** | SQL phân tán; Bè (thông qua TiKV) | Mạnh mẽ | Tương thích với MySQL; chia tỷ lệ ngang |
| **DynamoDB** | Khóa-giá trị; được quản lý | Cuối cùng (hoặc mạnh mẽ với số lần đọc nhất quán) | Không có máy chủ; Tích hợp AWS |
| **Cờ lê** | SQL phân tán; Paxos | Mạnh mẽ | Đám mây của Google; tính nhất quán toàn cầu |
---

## Mẫu hệ thống phân tán
| Mẫu | Mô tả | Trường hợp sử dụng |
|----------|-------------|----------|
| **Bầu cử lãnh đạo** | Chọn một nút để phối hợp | Trưởng bè; Người giữ vườn thú |
| **Sao chép** | Sao chép dữ liệu để dự phòng và chia tỷ lệ đọc | Bản sao cơ sở dữ liệu; CDN |
| **Sharding** | Phân vùng dữ liệu theo phạm vi khóa hoặc hàm băm | Cơ sở dữ liệu quy mô lớn |
| **MapReduce** | Phân chia tính toán giữa các nút; kết quả tổng hợp | Xử lý dữ liệu lớn |
| **Giao thức tin đồn** | Các nút chia sẻ trạng thái định kỳ với các nút ngang hàng ngẫu nhiên | Thành viên cụm; phát hiện lỗi |
| **Cam kết hai giai đoạn** | Phối hợp các giao dịch trên nhiều nút | Cơ sở dữ liệu phân tán |
| **Mẫu Saga** | Chuỗi giao dịch nội địa kèm hành động đền bù | Giao dịch vi dịch vụ |
| **Ngắt mạch** | Dừng gọi một dịch vụ bị lỗi; thất bại nhanh chóng | Khả năng phục hồi; ngăn ngừa sự cố xếp tầng |
---

## Những thách thức trong hệ thống phân tán
| Thử thách | Mô tả | Giảm nhẹ |
|----------|-------------|-------------|
| **Phân vùng mạng** | Các nút không thể giao tiếp | đánh đổi CAP; thử lại với thời gian lùi |
| **Đồng hồ lệch** | Các nút khác nhau có đồng hồ khác nhau | Sử dụng đồng hồ logic; NTP; tránh dựa vào thời gian trên đồng hồ treo tường |
| **Lỗi Byzantine** | Các nút nói dối hoặc hành xử tùy tiện | sự đồng thuận của BFT; chuỗi khối |
| **Chia não** | Cả hai nút đều nghĩ rằng họ là người dẫn đầu | Đấu kiếm; quyết định dựa trên số đại biểu |
| **Lỗi xếp tầng** | Thất bại này gây ra thất bại khác | Bộ ngắt mạch; vách ngăn; xuống cấp duyên dáng |
| **Tính nhất quán của dữ liệu** | Giữ các bản sao được đồng bộ hóa | Mô hình nhất quán; giải quyết xung đột |
---

## Bản tóm tắt
Hệ thống phân tán là cách phần mềm hiện đại mở rộng quy mô, khắc phục lỗi và phục vụ người dùng trên toàn cầu. Các thuật toán đồng thuận (Raft, Paxos) đảm bảo các nút đồng ý. Chuỗi khối thêm xác minh và phân cấp mật mã để tạo sổ cái không cần tin cậy. Cơ sở dữ liệu phân tán (Cassandra, CockroachDB, DynamoDB) xử lý dữ liệu trên quy mô lớn. Sự cân bằng cơ bản - được định lý CAP nắm bắt - là giữa tính nhất quán và tính khả dụng khi mạng không đáng tin cậy. Hiểu những khái niệm này là điều cần thiết để xây dựng các hệ thống hoạt động ở quy mô internet.