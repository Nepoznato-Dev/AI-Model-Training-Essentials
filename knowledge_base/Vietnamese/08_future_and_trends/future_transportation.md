---
# Metadata
title: "Future Transportation"
description: "EVs, autonomous vehicles, hyperloop"
category: "Future and Trends"
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
reviewed_by: "Future & Trends Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [future, transportation, future-and-trends]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "48 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Giao thông tương lai
## Tổng quan
Đi từ A đến B trông rất khác. Xe tự lái đã có mặt trên đường công cộng. Máy bay điện đang hoàn thành chuyến bay thử nghiệm. Khái niệm Hyperloop hứa hẹn khả năng di chuyển với tốc độ nhanh như tàu hỏa trong ống chân không. Và taxi bay - từng là nội dung của phim hoạt hình - đang được chứng nhận. Đây là trạng thái hoạt động của các công nghệ đang định hình lại cách chúng ta di chuyển.
---

## Xe tự lái
### Nền tảng công nghệ
#### Hệ thống cảm biến
**LiDAR (Phát hiện ánh sáng và phạm vi)**
- Tạo bản đồ đám mây điểm 3D bằng xung laser
- Cung cấp các phép đo khoảng cách chính xác
- Hoạt động trong nhiều điều kiện ánh sáng khác nhau
- Chi phí giảm từ 75.000 USD xuống dưới 1.000 USD/đơn vị
- Nhà cung cấp chính: Velodyne, Luminar, Innoviz, Hesai
**Máy ảnh**
- Hình ảnh trực quan có độ phân giải cao
- Thông tin về màu sắc và kết cấu
- Học sâu để nhận dạng đối tượng
- Chi phí thấp, công nghệ trưởng thành
- Hạn chế về ánh sáng/thời tiết kém
**Rađa**
- Phát hiện tần số vô tuyến
- Đo vận tốc tuyệt vời
- Hoạt động trong mọi điều kiện thời tiết
- Phát hiện tầm xa
- Độ phân giải thấp hơn LiDAR
**Cảm biến siêu âm**
- Phát hiện tầm ngắn (<10 mét)
- Hỗ trợ đỗ xe
- Chi phí thấp
- Phạm vi và độ phân giải hạn chế
#### Nền tảng máy tính
**Máy tính tích hợp**
- NVIDIA DRIVE: Nền tảng điện toán AI hàng đầu
- Mobileye EyeQ: Chuyên gia xử lý thị giác
- Qualcomm Snapdragon Ride: Giải pháp tích hợp
- Chip tùy chỉnh từ Tesla, Waymo
- Yêu cầu xử lý: 100+ TOPS (nghìn tỷ phép tính mỗi giây)
**Ngăn xếp phần mềm**
- Nhận thức: Nhận biết vật thể, làn đường, tín hiệu
- Bản địa hóa: Định vị chính xác (cấp centimet)
- Dự đoán: Dự đoán hành vi của người tham gia giao thông khác
- Quy hoạch: Quy hoạch lộ trình và quỹ đạo
- Điều khiển: Thực hiện lệnh lái xe
#### Khả năng kết nối
**V2X (Từ phương tiện đến mọi thứ)**
- V2V: Giao tiếp giữa xe với xe
- V2I: Giao tiếp giữa phương tiện với cơ sở hạ tầng
- V2P: Giao tiếp giữa xe với người đi bộ
- V2N: Xe tới mạng (đám mây)
- Tiêu chuẩn DSRC so với C-V2X
**Tích hợp 5G**
- Giao tiếp có độ trễ thấp (<10ms)
- Băng thông cao để truyền dữ liệu
- Hỗ trợ điện toán biên
- Cho phép lái xe hợp tác
### Cấp độ tự động hóa
#### Phân loại SAE
**Cấp 0 - Không tự động hóa**
- Kiểm soát hoàn toàn của con người
- Cảnh báo hỗ trợ lái xe cơ bản
**Cấp 1 - Hỗ trợ người lái**
- Lái HOẶC tăng tốc/phanh
- Ví dụ: Kiểm soát hành trình thích ứng, giữ làn đường
**Cấp 2 - Tự động hóa một phần**
- Cả tay lái VÀ tăng tốc/phanh
- Lái xe phải theo dõi liên tục
- Ví dụ: Tesla Autopilot, GM Super Cruise
**Cấp độ 3 - Tự động hóa có điều kiện**
- Hệ thống xử lý mọi hoạt động lái xe trong điều kiện xác định
- Người lái xe có thể bớt chú ý nhưng phải sẵn sàng tiếp quản
- Ví dụ: Honda Legend (Nhật Bản), Mercedes Drive Pilot
**Cấp 4 - Tự động hóa cao**
- Tự chủ hoàn toàn trong lĩnh vực thiết kế vận hành (ODD)
- Không cần sự can thiệp của con người trong ODD
- Có thể có vô lăng để dự phòng
- Ví dụ: Waymo One, Cruise (trước khi tạm dừng)
**Cấp 5 - Tự động hóa hoàn toàn**
- Hoàn toàn tự chủ trong mọi điều kiện
- Không cần vô lăng hoặc bàn đạp
- Chưa được thương mại hóa
### Trạng thái triển khai
#### Dịch vụ Robotaxi
**Waymo Một**
- Hoạt động tại Phoenix, San Francisco, Los Angeles
- Dịch vụ hoàn toàn không có người lái
- Đã hoàn thành hàng triệu km tự lái
- Mở rộng sang các thành phố khác
- Hợp tác với Uber để truy cập nền tảng
**Du thuyền**
- Hoạt động tại San Francisco trước khi bị đình chỉ (2023)
- Sự cố an toàn dẫn đến việc thu hồi đội xe
- Đang thực hiện chương trình tái thiết
- Nêu bật những thách thức về quy định và an toàn
**Người chơi khác**
- **Zoox**: Robotaxi được chế tạo có mục đích, thử nghiệm ở Las Vegas
- **Motional**: Đối tác của Hyundai, hoạt động ở một số thành phố chọn lọc
- **Baidu Apollo Go**: Dịch vụ taxi robot lớn nhất Trung Quốc
- **Pony.ai**: Hoạt động tại Hoa Kỳ và Trung Quốc
####Phương tiện cá nhân
** Xe tự lái hoàn toàn của Tesla (FSD)**
- Hệ thống cấp 2+ yêu cầu người lái giám sát
- Thử nghiệm beta với hàng trăm nghìn người dùng
- Việc đặt tên và tiếp thị gây tranh cãi
- Kiểm tra pháp lý đối với yêu cầu bồi thường
**GM Super Cruise**
- Lái xe trên đường cao tốc rảnh tay
- Hệ thống giám sát lái xe
- Có sẵn trên xe Cadillac và GMC
- Mở rộng thêm nhiều mẫu mã
**Ford BlueCruise**
- Tương tự hệ thống đường cao tốc rảnh tay
- Có sẵn trên F-150 Lightning và Mustang Mach-E
- Cập nhật qua mạng
#### Vận chuyển hàng hóa và hậu cần
**TuĐơn giản**
- Xe bán tải tự hành chạy đường dài
- Tập trung vào vận chuyển hàng hóa từ trung tâm đến trung tâm
- Hợp tác với các công ty logistic
**Cực quang**
- Aurora Driver cho xe tải và xe khách
- Hợp tác với FedEx, Uber Freight
- Định hướng triển khai thương mại
**Plus.ai**
- Công nghệ vận tải tự hành
- Triển khai tại Mỹ, Châu Âu, Châu Á
- Tập trung trang bị thêm các xe tải hiện có
### Thử thách và rào cản
#### Thử thách kỹ thuật
**Vỏ có cạnh**
- Các tình huống hiếm gặp không có trong dữ liệu đào tạo
- Khu vực thi công, tai nạn, phương tiện bất thường
- Thời tiết khắc nghiệt (mưa lớn, tuyết, sương mù)
- Hành vi của con người không thể đoán trước
**Hạn chế của cảm biến**
- Hiệu suất LiDAR trong lượng mưa
- Các vấn đề về ánh sáng chói và ánh sáng yếu của máy ảnh
- Độ phức tạp của cảm biến tổng hợp
- Hiệu chuẩn và bảo trì
**Nhu cầu tính toán**
- Yêu cầu xử lý thời gian thực
- Tiêu thụ điện năng và nhiệt
- Độ tin cậy và nhu cầu dự phòng
- Hạn chế về chi phí đối với phương tiện tiêu dùng
#### Rào cản pháp lý
**Quy định của Liên bang (Hoa Kỳ)**
- Tiêu chuẩn an toàn NHTSA
- Hướng dẫn tự nguyện so với các quy tắc bắt buộc
- Yêu cầu báo cáo sự cố
- Thẩm quyền triệu hồi
**Luật nhà nước**
- Yêu cầu khác nhau theo từng tiểu bang
- Giấy phép thử nghiệm so với phê duyệt triển khai
- Yêu cầu bảo hiểm
- Khung trách nhiệm pháp lý
**Biến thể quốc tế**
- Quy định của UNECE (Châu Âu)
- Phê duyệt theo quốc gia cụ thể
- Những thách thức hoạt động xuyên biên giới
#### Sự chấp nhận của xã hội
**Niềm tin của công chúng**
- Tai nạn cấp cao tác động đến nhận thức
- Hiểu các hạn chế của hệ thống
- Thoải mái với việc từ bỏ quyền kiểm soát
- Bình đẳng trong tiếp cận lợi ích
**Mối quan tâm về lao động**
- Chuyển việc cho lái xe chuyên nghiệp
- Các chương trình đào tạo lại và chuyển tiếp
- Phản hồi của công đoàn
- Gián đoạn kinh tế ở các cộng đồng bị ảnh hưởng
**Câu hỏi đạo đức**
- Tình huống sự cố xe đẩy
- Ra quyết định bằng thuật toán trong các sự cố
- Quyền riêng tư và giám sát dữ liệu
- Bảo mật chống hack
### Triển vọng tương lai
#### Dự đoán dòng thời gian
**2025-2027**
- Mở rộng dịch vụ robotaxi ở các thành phố thuận lợi
- Hệ thống cấp 3 phổ biến hơn ở xe cao cấp
- Tiếp tục cải tiến khả năng Cấp 2+
- Tự động hóa vận chuyển hàng hóa trên các tuyến đường hạn chế
**2028-2030**
- Robotaxis ở hơn 10 thành phố lớn
- Phương tiện cá nhân cấp 4 trong các trường hợp sử dụng cụ thể
- Tiêu chuẩn lái tự động trên đường cao tốc trên xe mới
- Khung pháp lý đang hoàn thiện
**2030++**
- Tính khả dụng rộng rãi ở Cấp độ 4
- Xe tự hành được xây dựng có mục đích chung
- Thị phần đáng kể của xe mới
- Bắt đầu thống trị đội tàu tự hành chung
#### Tác động thị trường
**Quyền sở hữu phương tiện**
- Chuyển từ quyền sở hữu sang tính di động như một dịch vụ
- Giảm sản xuất xe trong thời gian dài
- Thay đổi thiết kế xe (không có người điều khiển)
- Các mô hình kinh doanh mới
**Quy hoạch đô thị**
- Giảm nhu cầu đỗ xe
- Thay đổi mô hình giao thông
- Tiềm năng kích thích nhu cầu
- Tích hợp với phương tiện công cộng
**Hiệu ứng kinh tế**
- Cơ hội thị trường nghìn tỷ đô la
- Sự gián đoạn của ngành bảo hiểm
- Thay đổi giá trị bất động sản
- Năng suất tăng từ thời gian đi lại
---

##Siêu vòng lặp
### Tổng quan về khái niệm
#### Nguyên tắc cơ bản
- Hành khách/pod di chuyển trong ống áp suất thấp
- Lực đẩy từ trường giúp loại bỏ ma sát
- Động cơ điện để tăng tốc
- Gần chân không làm giảm sức cản không khí
- Tốc độ lý thuyết: 600-760 mph (970-1.220 km/h)
#### Lịch sử phát triển
- Khái niệm có từ tàu chân không thế kỷ 19
- Robert Goddard đề xuất vắc-xin (1904)
- Sách trắng "Hyperloop Alpha" của Elon Musk (2013)
- Thiết kế nguồn mở đã thu hút sự quan tâm toàn cầu
- Nhiều công ty được thành lập để phát triển công nghệ
###Thành phần công nghệ
#### Cơ sở hạ tầng đường ống
**Hệ thống chân không**
- Áp suất: ~100 Pascals (0,001 atm)
- Cần bơm liên tục
- Trạm airlock cho hành khách vào
- Phát hiện và quản lý rò rỉ
- Giao thức giảm áp khẩn cấp
**Xây dựng ống**
- Vật liệu thép hoặc composite
- Được nâng lên trên cột hoặc dưới lòng đất
- Quản lý giãn nở nhiệt
- Cân nhắc về địa chấn
- Điểm truy cập bảo trì
**Cân nhắc về lộ trình**
- Ưu tiên đường thẳng (hạn chế rẽ)
- Giới hạn cấp độ cho hiệu quả
- Khó khăn trong việc thu hồi đất
- Đánh giá tác động môi trường
- Khó khăn về hội nhập đô thị
#### Thiết kế nhóm
**Hệ thống bay lên**
- **Hệ thống treo điện từ (EMS)**: Lực hấp dẫn (Transrapid-style)
- **Hệ thống treo điện động (EDS)**: Lực đẩy (maglev Nhật Bản)
- **Từ tính thụ động**: Nam châm vĩnh cửu
- **Vòng bi khí**: Đệm khí nén (cuộc thi đầu tiên của SpaceX)
**Sức đẩy**
- Động cơ điện tuyến tính dạng ống
- Pin tích hợp hoặc bộ thu điện
- Phanh tái sinh
- Cấu hình tăng tốc/giảm tốc
- Hệ thống điện khẩn cấp
**Trải nghiệm của hành khách**
- Cấu hình chỗ ngồi (điển hình 12-40 hành khách)
- Quản lý áp suất cabin
- Giảm thiểu chứng say tàu xe
- Thủ tục lên/xuống xe
- Kế hoạch sơ tán khẩn cấp
### Nỗ lực phát triển
#### Các công ty lớn
**Hyperloop nguyên bản (nay là Hyperloop One)**
- Đã huy động được hơn 450 triệu USD
- Đường thử DevLoop ở Nevada
- Thử nghiệm nhóm toàn diện đạt tốc độ hơn 100 mph
- Tiên phong nỗ lực chứng nhận
- Tập trung vào hàng hóa (2022)
- Công ty đã giải thể hiệu quả (2023)
**Hardt Hyperloop (Hà Lan)**
- Tiêu điểm Châu Âu
- Cơ sở thử nghiệm 30m
- Đang tiến hành thử nghiệm thành phần
- Phương pháp liên kết với các trường đại học
- Ứng dụng vận chuyển hàng hóa đang được khám phá
**Công nghệ Swisspod**
- Sự phát triển của Châu Âu
- Tập trung vào tiêu chuẩn hóa
- Quan hệ đối tác học thuật
- Nghiên cứu tuyến đường khu vực
**Công nghệ vận tải Hyperloop (HTT)**
- Mô hình phát triển Crowdsourced
- Thỏa thuận nghiên cứu với nhiều quốc gia
- Phương pháp cấp phép công nghệ
- Tiến độ chậm hơn so với đối thủ
#### Sự quan tâm của Chính phủ
**Hoa Kỳ**
- Nghiên cứu khả thi cho các tuyến đường khác nhau
- Không có cam kết tài trợ liên bang
- Khung pháp lý chưa xác định
**Liên minh Châu Âu**
- 2,5 tỷ euro được phân bổ cho đường sắt tốc độ cao (không phải cụ thể là hyperloop)
- Một số nước thành viên quan tâm
- Lộ trình chứng nhận đang được phát triển
**Ấn Độ**
- Thỏa thuận Andhra Pradesh (phần lớn bị đình trệ)
- Đã nghiên cứu tuyến đường Mumbai-Pune
- Đầu tư cơ sở hạ tầng quan trọng được quy hoạch chung
**Trung Đông**
- Thỏa thuận thử nghiệm và quan tâm của UAE
- Xem xét dự án NEOM của Ả Rập Saudi
- Sự giàu có về dầu mỏ đang tìm kiếm sự đa dạng hóa
### Thử thách
#### Rào cản kỹ thuật
**Duy trì chân không**
- Ngăn chặn chân không ở quy mô km
- Yêu cầu về công suất bơm
- Quản lý tỷ lệ rò rỉ
- Tác dụng nhiệt lên áp suất
**Giãn nở nhiệt**
- Chiều dài ống thay đổi theo nhiệt độ
- Thiết kế khe co giãn
- Bảo trì căn chỉnh
- Cân nhắc lựa chọn vật liệu
**Hệ thống an toàn**
- Phanh khẩn cấp trong chân không
- Tránh va chạm giữa pod-to-pod
- Kịch bản vi phạm ống
- Chữa cháy trong môi trường có lượng oxy thấp
- Ứng phó khẩn cấp y tế
**Yêu cầu về nguồn**
- Công suất đỉnh cao để tăng tốc
- Lưu trữ năng lượng so với cung cấp liên tục
- Kết nối lưới theo chu kỳ
- Hiệu quả so với các lựa chọn thay thế
#### Khả năng kinh tế
**Chi phí xây dựng**
- Ước tính trên 10-100 triệu USD mỗi km
- Chi phí giải phóng mặt bằng
- Xây dựng trạm
- So sánh với đường sắt cao tốc
**Chi phí hoạt động**
- Năng lượng bảo trì chân không
- Yêu cầu về nhân sự
- Bảo trì hệ thống chuyên dụng
- Chi phí bảo hiểm
**Tiềm năng doanh thu**
- Giá vé so với các lựa chọn thay thế
- Giả định sử dụng công suất
- Kinh tế vận chuyển hàng hóa và hành khách
- Cạnh tranh từ việc cải tiến các lựa chọn thay thế
#### Quy định và pháp lý
**Lộ trình chứng nhận**
- Không có danh mục hiện có cho phương thức vận chuyển này
- Khung pháp lý về hàng không và đường sắt
- Nhu cầu hoà hợp quốc tế
- Phân công trách nhiệm
**Quyền đi đường**
- Yêu cầu tên miền nổi bật
- Giao cắt tài sản tư nhân
- Giấy phép môi trường
- Cộng đồng phản đối
**Tiêu chuẩn an toàn**
- Yêu cầu về khả năng va chạm
- Giao thức ứng phó khẩn cấp
- Chứng nhận người vận hành
- Yêu cầu bảo hiểm
### Bối cảnh cạnh tranh
#### Phương tiện giao thông tốc độ cao thay thế
**Đường sắt cao tốc**
- Công nghệ đã được chứng minh (hoạt động từ năm 1964)
- Tốc độ lên tới 350 km/h (217 mph)
- Xây dựng khuôn khổ pháp lý
- Công suất mỗi xe cao hơn
- Hội nhập đô thị tốt hơn
**Hàng không thông thường**
- Tốc độ 800-900 km/h
- Điểm-điểm không có cơ sở hạ tầng
- Ngành công nghiệp trưởng thành
- Mối quan tâm về môi trường
- ùn tắc sân bay
**Công nghệ mới nổi**
- Máy bay eVTOL phục vụ vận tải khu vực
- Máy bay siêu thanh quay trở lại (Boom, v.v.)
- Cải tiến đường sắt thông thường
### Triển vọng thực tế
#### Gần nhiệm kỳ (2025-2030)
- Tiếp tục thử nghiệm thành phần
- Hệ thống trình diễn hàng hóa có thể
- Phát triển khung pháp lý
- Nguyên mẫu quy mô đầy đủ có giới hạn
####Trung hạn (2030-2040)
- Những tuyến thương mại đầu tiên vượt qua được rào cản kỹ thuật
- Có khả năng chở hàng trước hành khách
- Khu vực chứ không phải liên lục địa
- Chi phí ban đầu cao
#### Dài hạn (2040+)
- Các ứng dụng thích hợp tiềm năng
- Không có khả năng thay thế rộng rãi việc di chuyển bằng đường hàng không
- Có thể tìm thấy thành công trong các hành lang cụ thể
- Các sản phẩm công nghệ phụ có giá trị bất kể
#### Kết quả có khả năng xảy ra nhất
- Hyperloop phải đối mặt với những rào cản kinh tế và kỹ thuật to lớn
- Có thể thành công trong một số ứng dụng hạn chế
- Đường sắt tốc độ cao có nhiều khả năng vận chuyển mặt đất hơn
- Nghiên cứu tiến bộ công nghệ liên quan
---

## Ô tô bay (eVTOL)
### eVTOL là gì?
#### Định nghĩa
- Máy bay cất cánh và hạ cánh thẳng đứng bằng điện
- Thường được gọi là "ô tô bay" dù không thể đi trên đường
- Được thiết kế cho di chuyển trên không trong đô thị (UAM)
- Động cơ đẩy bằng điện hoặc hybrid-điện
- Vận hành thí điểm hoặc tự động
#### Thể loại
**Thang máy + Du thuyền**
- Rôto riêng biệt để nâng và đẩy về phía trước
- Hệ thống điều khiển đơn giản hơn
- Ít hiệu quả hơn trong quá trình chuyển đổi
- Ví dụ: Beta Technologies, Tập đoàn Máy bay Điện
** Lực đẩy theo vectơ **
- Rotor nghiêng cho cả thang nâng và hành trình
- Chuyến bay hiệu quả hơn
- Hệ thống cơ khí phức tạp
- Ví dụ: Joby Hàng không, Archer
**Máy bay đa năng**
- Nhiều cánh quạt cố định
- Đơn giản nhất về mặt cơ học
- Phạm vi và tốc độ hạn chế
- Ví dụ: Volocopter, EHang
**Điện lai**
- Động cơ đốt trong tạo ra điện
- Phạm vi mở rộng so với chỉ dùng pin
- Phức tạp hơn, một số khí thải
- Ví dụ: Một số khái niệm lớn hơn
###Các công ty hàng đầu
#### Joby Hàng không
- **Trụ sở chính**: California, Hoa Kỳ
- **Thiết kế**: Cánh quạt nghiêng, 5 hành khách + phi công
- **Phạm vi**: hơn 150 dặm
- **Tốc độ**: 200 mph
- **Trạng thái**: Quy trình chứng nhận loại FAA nâng cao
- **Quan hệ đối tác**: Toyota, Delta Air Lines, Lực lượng Không quân Hoa Kỳ
- **Dòng thời gian**: Mục tiêu dịch vụ thương mại 2025-2026
#### Hàng không Archer
- **Trụ sở chính**: California, Hoa Kỳ
- **Thiết kế**: Máy bay lúc nửa đêm, 4 hành khách + phi công
- **Phạm vi**: 100 dặm
- **Tốc độ**: 150 mph
- **Trạng thái**: Quá trình chứng nhận FAA đang được tiến hành
- **Hợp tác**: United Airlines, Stellantis
- **Dòng thời gian**: Mục tiêu ra mắt thương mại là vào năm 2025
####Volocopter
- **Trụ sở chính**: Đức
- **Thiết kế**: Multicopter, 2 hành khách
- **Phạm vi**: 35 km
- **Tốc độ**: 110 km/h
- **Trạng thái**: Quá trình chứng nhận EASA
- **Quan hệ đối tác**: Quan hệ đối tác khác nhau của thành phố
- **Dòng thời gian**: Nhắm mục tiêu 2026-2025 (Mục tiêu là Thế vận hội Paris)
####EHàng
- **Trụ sở chính**: Trung Quốc
- **Thiết kế**: Máy bay trực thăng tự động
- **Phạm vi**: 30 km
- **Trạng thái**: Đã nhận được chứng nhận CAAC (2023)
- **Hoạt động**: Các chuyến bay thương mại giới hạn ở Trung Quốc
- **Dòng thời gian**: Đã hoạt động với công suất hạn chế
#### Công nghệ Beta
- **Trụ sở chính**: Vermont, Hoa Kỳ
- **Thiết kế**: Cất cánh thông thường (không phải VTOL), điện
- **Tiêu điểm**: Hàng hóa trước, hành khách sau
- **Phạm vi**: 400 dặm
- **Quan hệ đối tác**: UPS, Lực lượng Không quân Hoa Kỳ
#### Những cầu thủ đáng chú ý khác
- **Lilium**: Quạt thông gió chạy bằng phản lực, Đức
- **Vertical Aerospace**: Vương quốc Anh, quan hệ đối tác với Virgin Atlantic
- **Wisk Aero**: Được Boeing hậu thuẫn, tự trị, California
- **Kitty Hawk**: Được hỗ trợ bởi Larry Page, được thu nhỏ lại
### Yêu cầu về cơ sở hạ tầng
#### Vertiport
**Yếu tố thiết kế**
- Sân cất cánh/hạ cánh
- Khu vực chờ hành khách
- Trạm sạc/đổi pin
- Giao diện điều khiển không lưu
- Bảo vệ thời tiết
**Cân nhắc về vị trí**
- Mái nhà của các tòa nhà
- Sân bay trực thăng hiện có
- Các đầu mối giao thông
- Công trình bãi đậu xe
- Tầng trệt ở những khu vực ít mật độ hơn
**Yêu cầu quy định**
- Phê duyệt quy hoạch
- Hạn chế tiếng ồn
- Hạn chế về an toàn
- Đánh giá môi trường
- Sự chấp nhận của cộng đồng
#### Cơ sở hạ tầng sạc
**Yêu cầu về nguồn**
- Sạc công suất cao (100 kW)
- Thời gian thực hiện nhanh (<10 phút)
- Tùy chọn trao đổi pin đang được khám phá
- Thường xuyên cần nâng cấp công suất lưới
- Cơ hội hội nhập năng lượng tái tạo
**Công nghệ pin**
- Dòng điện: Lithium-ion, giới hạn mật độ năng lượng
- Tương lai: Pin thể rắn có thể cải thiện phạm vi hoạt động
- Trọng lượng quan trọng cho các ứng dụng hàng không
- Quản lý nhiệt cần thiết
- Cần có cơ sở hạ tầng tái chế
####Quản lý không lưu
**UTM (Quản lý giao thông không người lái)**
- Khung phát triển của NASA và FAA
- Phối hợp kỹ thuật số của các chuyến bay tầm thấp
- Tích hợp với ATC truyền thống
- Phát hiện và giải quyết xung đột
- Tích hợp thời tiết
**Phát hiện và tránh**
- Cảm biến trên tàu để tránh chướng ngại vật
- Liên lạc với các máy bay khác
- Hệ thống dự phòng khi có sự cố
- Thủ tục khẩn cấp tự động
### Ứng dụng thị trường
#### Vận tải hàng không đô thị
**Dịch vụ taxi hàng không**
- Các chuyến bay điểm-điểm theo yêu cầu
- Đặt phòng dựa trên ứng dụng
- Mục tiêu định giá: Dịch vụ đi chung xe cao cấp lên trực thăng
- Lộ trình ban đầu: Đưa đón sân bay, xuyên thành phố
- Mở rộng sang các mạng rộng hơn
**Sự phát triển về giá dự kiến**
- Ra mắt: $5-10 mỗi hành khách-dặm
- Quy mô: 2-5 USD/hành khách/dặm
- Mục tiêu: Bình đẳng về chia sẻ chuyến đi trên mặt đất trong dài hạn
- Phụ thuộc vào khả năng tự chủ giảm chi phí thí điểm
#### Y tế và cấp cứu
**Vận chuyển y tế**
- Giao nội tạng
- Vật tư y tế khẩn cấp
- Chuyển bệnh nhân giữa các bệnh viện
- Nhanh hơn mặt đất ở khu vực tắc nghẽn
**Ứng phó khẩn cấp**
- Triển khai ứng phó đầu tiên
- Tìm kiếm và cứu hộ
- Hỗ trợ chữa cháy
- Đánh giá thảm họa
#### Ứng dụng vận chuyển hàng hóa
**Giao hàng trọn gói**
- UPS, DHL, FedEx khám phá hàng hóa eVTOL
- Giao hàng nhạy cảm về thời gian
- Truy cập khu vực từ xa
- Đường đi điều tiết đơn giản hơn hành khách
**Chuyên chở liên cơ sở**
- Kho đến kho
- Sản xuất linh kiện
- Vật tư y tế giữa các cơ sở
### Thử thách
#### Kỹ thuật
**Hạn chế về pin**
- Mật độ năng lượng hạn chế phạm vi
- Trọng lượng tác động đến hiệu quả
- Thời gian sạc ảnh hưởng đến việc sử dụng
- Hiệu suất thời tiết lạnh
- Lo ngại về an toàn (chạy trốn nhiệt)
**Tiếng ồn**
- Sự chấp nhận của công chúng phụ thuộc vào mức độ tiếng ồn
- Mục tiêu: <65 dB ở độ cao 100m
- Thiết kế rôto quan trọng
- Tối ưu hóa đường bay
- Có khả năng bị hạn chế hoạt động vào ban đêm
**Thời tiết**
- Điều kiện đóng băng có vấn đề
- Hạn chế của gió
- Yêu cầu về khả năng hiển thị
- Chống sét
- Mục tiêu hoạt động trong mọi thời tiết khó khăn
#### Theo quy định
**Chứng nhận**
- FAA Phần 21.17(b) hạng đặc biệt
- Danh mục EASA SC-VTOL
- Quá trình kéo dài, tốn kém
- Thiết kế mới lạ chưa có tiền lệ
- Cần sự hài hòa quốc tế
**Yêu cầu thí điểm**
- Hiện tại: Yêu cầu có phi công được cấp phép
- Tương lai: Giảm huấn luyện cho máy bay đơn giản hóa
- Ultimate: Hoạt động tự chủ
- Lộ trình chuyển tiếp không rõ ràng
**Phê duyệt hoạt động**
- Phê duyệt tuyến đường
- Chứng chỉ của Vertiport
- Chênh lệch tiếng ồn
- Ngoài tầm nhìn trực quan (BVLOS)
- Các chuyến bay khu vực đông dân cư
#### Thuộc kinh tế
**Chi phí phát triển cao**
- Hàng tỷ USD đầu tư vào toàn ngành
- Thời gian dài để có doanh thu
- Nhiều công ty sẽ thất bại
- Dự kiến hợp nhất
**Kinh tế đơn vị**
- Mục tiêu chi phí máy bay: 1-5 triệu USD
- Tỷ lệ sử dụng quan trọng
- Chi phí bảo trì không chắc chắn
- Chưa rõ chi phí bảo hiểm
- Chi phí thí điểm cho đến khi tự chủ
**Không chắc chắn về quy mô thị trường**
- Dự báo nhu cầu rất khác nhau
- Độ nhạy cảm về giá không rõ ràng
- Cạnh tranh từ vận tải mặt đất
- Vấn đề con gà và quả trứng về cơ sở hạ tầng
### Dòng thời gian và Outlook
#### 2026-2026
- Ra mắt thương mại lần đầu (có giới hạn)
- Thế vận hội Paris trình diễn công nghệ
- Đường bay sớm: sân bay, hành lang cụ thể
- Giá cao, số lượng có hạn
- Sự chú ý của giới truyền thông và sự tò mò của công chúng
#### 2027-2030
- Triển khai mở rộng thành phố
- Giá bắt đầu giảm
- Nhiều đối thủ vào/ra hơn
- Đẩy mạnh xây dựng cơ sở hạ tầng
- Tính năng tự chủ tăng lên
#### 2030+
- Có sẵn phổ biến ở các thành phố lớn
- Giá ngang bằng với vận tải mặt đất cao cấp
- Hoạt động tự chủ bắt đầu
- Tích hợp với các ứng dụng chuyển tuyến công cộng
- Tỷ lệ phương thức đáng kể ở các thành phố tắc nghẽn
####Đánh giá thực tế
- Sẽ thành công ở những niche cụ thể trước tiên
- Không thay thế được hầu hết các phương tiện vận tải mặt đất
- Bổ sung cho các tùy chọn di động hiện có
- Mang lại lợi ích ban đầu cho những người giàu có chấp nhận sớm
- Tiềm năng lâu dài để tiếp cận rộng rãi hơn
---

## Hàng không điện
### Phân khúc thị trường
#### Máy bay khu vực (Sắp tới nhất)
**Định nghĩa**
- Máy bay 9-100 chỗ
- Lộ trình: 200-800 dặm
- Hiện tại có động cơ phản lực cánh quạt hoặc máy bay phản lực nhỏ
- Tần suất cao, thời gian ngắn
**Tại sao lại dùng điện trước?**
- Các tuyến đường ngắn hơn phù hợp với khả năng của pin
- Rào cản chứng nhận thấp hơn so với máy bay lớn
- Cấu trúc tuyến đường hiện có
- Lợi ích môi trường dễ thấy nhất
- Kinh tế làm việc với công nghệ hiện tại
**Dự án trọng điểm**
- **Heart Aerospace ES-30**: 30 chỗ, phạm vi chạy điện 200 km
- **Eviation Alice**: 9 chỗ, theo đuổi chứng chỉ
- **MagniX**: Chuyển đổi động cơ điện
- **Universal Hydrogen**: Chuyển đổi pin nhiên liệu hydro
#### Hàng không tổng hợp
**Máy bay huấn luyện**
- Pipistrel Velis Electro: Máy bay điện được chứng nhận đầu tiên
- Chi phí vận hành thấp lý tưởng cho việc đào tạo
- Chuyến bay ngắn phù hợp với dung lượng pin
- Hoạt động yên tĩnh mang lại lợi ích cho các trường bay
- Tăng cường áp dụng trên toàn thế giới
**Máy bay cá nhân**
- Chuyển đổi điện của thiết kế hiện có
- Thiết kế mới dành riêng cho điện
- Phạm vi lo lắng giới hạn việc áp dụng
- Chi phí cao hơn so với thông thường
- Sự chấp nhận dẫn đầu thị trường
#### Máy bay thương mại cỡ lớn (Dài hạn)
**Thách thức kỹ thuật**
- Trọng lượng pin hạn chế cho các tuyến đường dài
- Khoảng cách mật độ năng lượng: nhiên liệu máy bay ~ 40x pin
- Độ phức tạp của chứng nhận tăng theo quy mô
- Yêu cầu về cơ sở hạ tầng sân bay
- Kinh tế chưa được chứng minh ở quy mô
**Phương pháp tiếp cận kết hợp**
- Turbogelectric: Tua bin tạo ra điện cho động cơ
- Lai song song: Cả động cơ tua-bin và động cơ điện
- Series hybrid: Tua bin sạc pin trong chuyến bay
- Công nghệ cầu nối trong khi pin được cải thiện
**Tùy chọn hydro**
- Đốt cháy hydro: Động cơ phản lực cải tiến
- Pin nhiên liệu hydro: Động cơ điện
- Những thách thức về lưu trữ hydro lỏng
- Cần có cơ sở hạ tầng hydro sân bay
- Không có carbon nếu hydro xanh
### Sự phát triển công nghệ
#### Công nghệ pin
**Trạng thái hiện tại**
- Lithium-ion chiếm ưu thế
- Mật độ năng lượng: ~250 Wh/kg (cấp độ tế bào)
- Mức đóng gói: ~160-180 Wh/kg
- Nhiên liệu phản lực tương đương: ~12.000 Wh/kg
- Khoảng cách phải đóng lại để hàng không điện khả thi
**Quỹ đạo cải tiến**
- Cải thiện hàng năm: 5-8% trong lịch sử
- Pin thể rắn: tiềm năng cải thiện gấp 2-3 lần
- Lithium-lưu huỳnh: Cải thiện gấp 5 lần về mặt lý thuyết
- Lithium-air: Giới hạn lý thuyết thậm chí còn cao hơn
- Mốc thời gian: Những cải tiến có ý nghĩa đến năm 2030
**Yêu cầu dành riêng cho ngành hàng không**
- An toàn tối đa (ngăn ngừa thoát nhiệt)
- Hoạt động ở dải nhiệt độ rộng
- Tốc độ phóng điện cao khi cất cánh
- Vòng đời cho hoạt động hàng ngày
- Tái chế và bền vững
####Động cơ điện
**Ưu điểm**
- Hiệu suất cao hơn động cơ đốt trong (>90% so với ~35%)
- Ít bộ phận chuyển động hơn, bảo trì thấp hơn
- Cung cấp mô-men xoắn ngay lập tức
- Khả năng đẩy phân phối
- Có thể mở rộng theo kích cỡ
**Sự phát triển**
- Cải thiện mật độ năng lượng
- Hệ thống điện cao thế (800V+)
- Tối ưu hóa hệ thống làm mát
- Tích hợp với cánh quạt/quạt
- Dự phòng để đảm bảo an toàn
#### Hiệu suất khí động học
**Tầm quan trọng**
- Mỗi mức tăng hiệu quả đều mở rộng phạm vi
- Lợi ích tổng hợp của động cơ điện
- Quan trọng để làm cho kinh tế hoạt động
**Phương pháp tiếp cận**
- Cánh chảy tầng
- Thiết kế thân cánh pha trộn
- Nhập lớp ranh giới
- Cấu trúc biến hình
- Công nghệ giảm lực cản
### Sáng kiến ​​ngành
#### Chương trình Airbus
**Sáng kiến ZEROe**
- Ba máy bay ý tưởng cho mục nhập năm 2035
- Quạt phản lực đốt bằng hydro
- Tua bin nhiên liệu hydro
- Hỗn hợp hydro thân cánh
- Phát triển hệ sinh thái toàn diện
**Quạt điện tử X**
- Trình diễn hybrid-điện (đã hoàn thiện)
- Bài học kinh nghiệm áp dụng cho các chương trình sau
- Phương pháp tích hợp đã được xác thực
#### Nỗ lực của Boeing
**Trình diễn chuyến bay bền vững**
- Cánh giằng giàn Transonic
- Tùy chọn động cơ hybrid-điện
- Quan hệ đối tác của NASA
- Tập trung vào hiệu quả bên cạnh điện khí hóa
**Mua lại và đầu tư**
- Wisk Aero (eVTOL tự trị)
- Khởi động động cơ điện khác nhau
- Chương trình nghiên cứu nội bộ
#### Người khởi nghiệp và người đổi mới
**Hàng không vũ trụ trái tim (Thụy Điển)**
- ES-30: Máy bay khu vực 30 chỗ
- Đặt hàng của United Airlines
- Lãi suất SAS, Finnair
- Mục tiêu: Năm 2028 đưa vào sử dụng
**Chuyến bay (Israel/Mỹ)**
- Alice: Máy bay thương gia 9 chỗ
- Hoàn thành chuyến bay đầu tiên (2022)
- Quá trình chứng nhận đang diễn ra
- Khách hàng đầu tiên của DHL
**Wright Electric (Anh)**
- Chuyển đổi BAe 146 thành điện
- Mục tiêu cuối cùng là 100 chỗ
- Hợp tác EasyJet
- Tập trung vào các tuyến đường ngắn
### Nhu cầu về cơ sở hạ tầng
####Điện khí hóa sân bay
**Cơ sở hạ tầng sạc**
- Bộ sạc công suất cao (quy mô MW cho máy bay lớn hơn)
- Nhiều điểm sạc trên mỗi cổng
- Nâng cấp công suất lưới
- Tích hợp năng lượng tái tạo
- Đầu nối tiêu chuẩn hóa
**Cân nhắc về lưới**
- Quản lý nhu cầu cao điểm
- Lưu trữ năng lượng tại chỗ
- Sản xuất năng lượng mặt trời/gió tại sân bay
- Thuật toán sạc thông minh
- Yêu cầu về nguồn điện dự phòng
#### Cơ sở bảo trì
**Yêu cầu kỹ năng mới**
- Chuyên môn hệ thống điện cao thế
- Bảo trì và kiểm tra ắc quy
- Bảo dưỡng động cơ điện
- Phần mềm và điện tử
- Cần có chương trình đào tạo
**Sửa đổi cơ sở**
- Hệ thống an toàn điện
- Bảo quản và xử lý pin
- Thiết bị chẩn đoán
- Chữa cháy khi cháy ắc quy
### Môi trường pháp lý
#### Lộ trình Chứng nhận
**Phương pháp tiếp cận của FAA**
- Phần 23 được cải tiến để chứng nhận dễ dàng hơn
- Lớp đặc biệt cho cấu hình mới
- Chứng nhận dựa trên rủi ro
- Tham gia sớm vào ngành
- Điều phối quốc tế
**Phương pháp tiếp cận EASA**
- Điều kiện đặc biệt cho VTOL
- Phương pháp chứng nhận tiến bộ
- Văn phòng đổi mới dành cho người mới tham gia
- Tích hợp các cân nhắc về môi trường
**Tiêu chuẩn an toàn**
- Mức độ an toàn tương đương với thông thường
- Yêu cầu an toàn về pin
- Kỳ vọng dự phòng hệ thống
- Xác nhận thủ tục khẩn cấp
#### Quy định về môi trường
**Tiêu chuẩn khí thải**
- Hiện tại: Tiêu chuẩn CO2 cho máy bay mới
- Tương lai: Ưu đãi không phát thải
- Lợi ích chất lượng không khí địa phương
- Quy định về tiếng ồn có lợi cho điện
**Giá cacbon**
- EU ETS bao gồm hàng không
- Chương trình bù đắp quốc tế CORSIA
- Có thể miễn trừ máy bay điện
- Lợi ích kinh tế tăng theo giá carbon
### Phân tích kinh tế
#### So sánh chi phí vận hành
**Ưu điểm về điện**
- Chi phí nhiên liệu: Điện rẻ hơn nhiên liệu máy bay
- Bảo trì: Ít bộ phận chuyển động hơn
- Tuổi thọ động cơ: Khoảng thời gian giữa các lần đại tu dài hơn
- Tiếng ồn: Giảm phí tại các sân bay nhạy cảm với tiếng ồn
**Thử thách về điện**
- Giá mua lại: Ban đầu cao hơn
- Thay pin: Chi phí lớn
- Thời gian sạc: Giảm thời gian sử dụng
- Giới hạn phạm vi: Hạn chế về tuyến đường
- Giá trị còn lại: Không chắc chắn
#### Trường hợp kinh doanh theo phân khúc
**Huấn luyện bay: Trường hợp chắc chắn**
- Khả năng chịu chi phí mua lại thấp
- Chuyến bay ngắn phù hợp với khả năng
- Tiết kiệm chi phí vận hành đáng kể
- Hiện tại đã xảy ra rồi
**Hàng không khu vực: Trường hợp mới nổi**
- Tổng chi phí sở hữu gần ngang bằng
- Cải thiện sự phù hợp của tuyến đường bằng pin
- Sự chấp nhận của hành khách ngày càng tăng
- Hãng hàng không lãi suất chính hãng
**Thương mại lớn: Tương lai xa**
- Kinh tế không phù hợp với công nghệ hiện tại
- Đòi hỏi công nghệ pin đột phá
- Giải pháp lai tạm thời có nhiều khả năng hơn
- Hydro có thể cạnh tranh
### Dự đoán dòng thời gian
#### 2026-2027
- Máy bay huấn luyện điện thông dụng
- Máy bay khu vực chạy điện đầu tiên được chứng nhận
- eVTOL ra mắt song song
- Các chuyến bay trình diễn các khái niệm lớn hơn
- Thí điểm cơ sở hạ tầng tại các sân bay chọn lọc
#### 2028-2032
- Máy bay điện khu vực phục vụ thương mại
- Nhiều nhà sản xuất cạnh tranh
- Mở rộng cơ sở hạ tầng sạc
- Trình diễn máy bay lai điện lớn hơn
- Chi phí ngang bằng ở một số phân khúc
#### 2033-2040
- Điện lưới chính cho các tuyến khu vực
- Hydro-điện cho các tuyến đường dài hơn
- Máy bay phản lực thông thường ngày càng được thay thế
- Chuyển đổi cơ sở hạ tầng sân bay lớn
- Giảm phát thải đáng kể
#### 2040+
- Điện chiếm ưu thế cho quãng đường ngắn/trung bình
- Hydro cho chặng đường dài
- Máy bay phản lực thông thường chiếm thiểu số trong đội bay
- Có thể có lượng khí thải hàng không gần bằng không
- Tích hợp đầy đủ hệ sinh thái hàng không bền vững
### Thách thức và Rủi ro
####Rủi ro công nghệ
- Pin phát triển chậm hơn dự kiến
- Sự cố an toàn gây trở ngại cho việc áp dụng
- Sự chậm trễ chứng nhận
- Thiếu sót về hiệu suất
#### Rủi ro thị trường
- Giá nhiên liệu vẫn ở mức thấp
- Định giá carbon chưa đủ
- Sức cản của hành khách
- Độ trễ đầu tư cơ sở hạ tầng
#### Rủi ro cạnh tranh
- Cải thiện nhiên liệu hàng không bền vững (SAF)
- Quá trình đốt cháy trực tiếp hydro thành công
- Cải tiến hiệu quả thông thường
- Chuyển đổi phương thức sang đường sắt cho các tuyến ngắn
---

## Phần kết luận
Tương lai của giao thông vận tải hứa hẹn những thay đổi mạnh mẽ trên tất cả các phương thức:
### Chủ đề chung
**Điện khí hóa**
- Pin cho phép khả năng mới
- Lợi ích môi trường thúc đẩy việc áp dụng
- Lợi thế về chi phí vận hành
- Cần chuyển đổi cơ sở hạ tầng
**Tự động hóa**
- Loại bỏ người vận hành nếu có thể
- Tiềm năng cải thiện an toàn
- Lo ngại gián đoạn lao động
- Cần có sự điều chỉnh về mặt pháp lý
**Kết nối**
- Phương tiện giao thông liên lạc với nhau và cơ sở hạ tầng
- Tối ưu hóa lưu lượng truy cập
- Đã kích hoạt mô hình dịch vụ mới
- An ninh mạng rất quan trọng
**Mô hình dịch vụ**
- Chuyển từ quyền sở hữu sang tính di động như một dịch vụ
- Truy cập theo yêu cầu
- Nền tảng đa phương thức tích hợp
- Sự phát triển giá cả theo hướng khả năng chi trả
### Cơ hội hội nhập
**Hành trình đa phương thức**
- Sự kết hợp liền mạch của các phương thức vận tải
- Ứng dụng duy nhất để lập kế hoạch và thanh toán
- Tích hợp vật lý tại các trung tâm
- Lịch trình phối hợp
**Cơ sở hạ tầng dùng chung**
- Vertiport tại các trạm trung chuyển
- Trạm sạc phục vụ nhiều loại xe
- Chia sẻ dữ liệu giữa các chế độ
- Quy hoạch đô thị đồng bộ
### Yếu tố thành công
**Sự trưởng thành của công nghệ**
- Tiếp tục cải tiến pin
- AI và cảm biến tiến bộ
- Mở rộng quy mô sản xuất
- Chứng minh độ tin cậy
**Hiện đại hóa quy định**
- Các khuôn khổ thích ứng cho sự đổi mới
- An toàn không cản trở tiến độ
- Hài hòa quốc tế
- Lộ trình cấp chứng chỉ rõ ràng
**Đầu tư cơ sở hạ tầng**
- Vốn công và vốn tư nhân
- Hiện đại hóa lưới điện
- Xây dựng cơ sở vật chất
- Triển khai hệ thống số
**Sự chấp nhận của xã hội**
- Xây dựng niềm tin của công chúng
- Công bằng trong việc tiếp cận các lợi ích
- Giải quyết vấn đề dịch chuyển lao động
- Công lý môi trường
**Khả năng kinh tế**
- Đạt được khả năng cạnh tranh về chi phí
- Mô hình kinh doanh bền vững
- Tính kinh tế nhờ quy mô
- Các ngoại tác tích cực được đánh giá cao
Cuộc cách mạng giao thông vận tải đã được tiến hành. Mặc dù các mốc thời gian vẫn chưa chắc chắn và có những thách thức đáng kể, nhưng phương hướng đã rõ ràng: khả năng di chuyển sạch hơn, an toàn hơn, hiệu quả hơn và dễ tiếp cận hơn cho tất cả mọi người.