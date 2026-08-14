---
# Metadata
title: "Geospatial Analysis"
description: "Coordinate systems, spatial operations, GeoPandas, raster analysis"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [geospatial, analysis, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Phân tích không gian địa lý
Phân tích không gian địa lý là quá trình kiểm tra dữ liệu có thành phần địa lý - tọa độ, địa chỉ, ranh giới hoặc bất kỳ dữ liệu nào gắn liền với một vị trí trên Trái đất. Nó trả lời các câu hỏi như "khách hàng của chúng tôi ở đâu?", "lộ trình tối ưu là gì?" và "việc sử dụng đất thay đổi như thế nào theo thời gian?". Mỗi tập dữ liệu đều có một chiều không gian và việc hiểu nó sẽ mở ra những hiểu biết sâu sắc mà phân tích thống kê thuần túy bỏ lỡ.
---

## Khái niệm cốt lõi
### Hệ tọa độ
| Hệ thống | Mô tả | Trường hợp sử dụng |
|--------|-------------|----------|
| **WGS 84 (EPSG:4326)** | Tiêu chuẩn toàn cầu; vĩ độ/kinh độ tính bằng độ | GPS; hầu hết các bản đồ web; GeoJSON |
| **Web Mercator (EPSG:3857)** | Chiếu quả địa cầu vào một hình trụ; làm biến dạng diện tích ở cực | Google Maps; Hộp bản đồ; hầu hết các dịch vụ gạch web |
| **UTM** (Universal Transverse Mercator) | Chia Trái đất thành 60 khu vực; dựa trên mét | Quân đội; khảo sát; công việc địa phương có độ chính xác cao |
| **Lưới điện quốc gia Anh (EPSG:27700)** | dữ liệu OSGB36; dựa trên mét | Bản đồ Vương quốc Anh |
| **Dự báo địa phương** | Dự đoán tùy chỉnh cho các vùng cụ thể | Giảm thiểu biến dạng cho một khu vực cụ thể |
### Các loại hình học
| Loại | Mô tả | Ví dụ |
|------|-------------|----------|
| **Điểm** | Tọa độ đơn | Một nhà hàng; một cảm biến; một khách hàng |
| **LineString** | Thứ tự điểm | Một con đường; một con sông; một tuyến đường |
| **Đa giác** | Hình dạng khép kín với nội thất | Một đất nước; một cái hồ; một khu vực giao hàng |
| **Đa điểm** | Thu thập điểm | Tất cả các điểm dừng xe buýt trong thành phố |
| **Đa dòng** | Bộ sưu tập các dòng | Tất cả các con đường trong một mạng lưới |
| **Đa giác** | Bộ sưu tập đa giác | Một quần đảo; một đất nước có nhiều đảo |
| **Bộ sưu tập hình học** | Các loại hỗn hợp | Một đất nước với những thành phố, những con đường và những dòng sông |
---

## Định dạng dữ liệu
| Định dạng | Loại | Tính năng chính |
|--------|------|-------------|
| **GeoJSON** | Văn bản (JSON) | Con người có thể đọc được; thân thiện với web; hỗ trợ tất cả các loại hình học |
| **Tập tin hình dạng** | Nhị phân (nhiều tệp) | Định dạng kế thừa từ ESRI; .shp + .shx + .dbf + .prj |
| **KML** | XML | Google Earth; hỗ trợ 3D và thời gian |
| **Gói địa lý** | Dựa trên SQLite | Tệp đơn; hỗ trợ raster và vector; tiêu chuẩn hiện đại |
| **GeoParquet** | Cột (Sàn) | Hiệu quả cho các tập dữ liệu lớn; tích hợp với các công cụ kỹ thuật dữ liệu |
| **WKT / WKB** | Văn bản / Nhị phân | Văn bản nổi tiếng; Nhị phân nổi tiếng; dùng để lưu trữ cơ sở dữ liệu |
| **MVT** | Nhị phân | Gạch Vector Mapbox; để phục vụ dữ liệu bản đồ cho các máy khách web |
---

## Hoạt động không gian
### Hoạt động cơ bản
| Hoạt động | Mô tả | Ví dụ |
|----------|-------------|----------|
| **Khoảng cách** | Tính khoảng cách giữa các hình học | "Tìm tất cả bệnh viện trong phạm vi 10 km" |
| **Bộ đệm** | Tạo một đa giác xung quanh một hình học ở một khoảng cách nhất định | "Hiển thị vùng 500m xung quanh trường học" |
| **Ngã tư** | Tìm vùng chồng chéo giữa các hình học | “Những lô đất nào nằm trong vùng lũ lụt?” |
| **Liên minh** | Hợp nhất các hình học thành một | "Gộp tất cả các thửa đất thành một vùng" |
| **Sự khác biệt** | Trừ một hình học từ một hình học khác | "Khu vực có thể xây dựng không bao gồm khu bảo vệ" |
| **Chứa / Bên trong** | Kiểm tra xem một hình học có nằm trong một hình học khác không | "Những khách hàng nào ở trong khu vực giao hàng này?" |
| **Hàng xóm gần nhất** | Tìm hình học gần nhất | "Trạm cứu hỏa gần nhất là gì?" |
| **Kết nối không gian** | Tham gia các thuộc tính dựa trên mối quan hệ không gian | "Gán từng điểm vào vùng điều tra dân số chứa nó" |
### Lập chỉ mục không gian
| Loại chỉ mục | Mô tả | Trường hợp sử dụng |
|----------|-------------|----------|
| **Cây R** | Hệ thống phân cấp hộp giới hạn; phổ biến nhất | PostGIS; SQLite; mục đích chung |
| **Cây tứ giác** | Phân chia đệ quy thành các góc phần tư | Dữ liệu điểm; công cụ trò chơi |
| **Geohash** | Lưới phân cấp; mã hóa thành chuỗi | Tìm kiếm lân cận; phân mảnh cơ sở dữ liệu |
| **H3** (Uber) | Lưới phân cấp lục giác | Phân tích; đi chung xe; thùng đựng đồng phục |
| **S2** (Google) | Hệ thống phân cấp dựa trên ô trên một hình cầu | Lập chỉ mục không gian quy mô lớn |
---

## Công cụ và Thư viện
| Công cụ / Thư viện | Ngôn ngữ | Mô tả |
|--------------|----------|-------------|
| **PostGIS** | SQL (PostgreSQL) | Tiêu chuẩn vàng cho cơ sở dữ liệu không gian; SQL không gian đầy đủ |
| **QGIS** | Máy tính để bàn (Python/C++) | GIS nguồn mở, miễn phí; hệ sinh thái plugin |
| **GeoPandas** | Python | Gấu trúc + Tạo hình + Fiona; DataFrames không gian |
| **Đẹp đẽ** | Python | Các phép toán hình học; dựa trên GEOS |
| **Folium** | Python | Bản đồ tờ rơi tương tác từ Python |
| **Turf.js** | JavaScript | Phân tích không gian địa lý phía khách hàng |
| **Deck.gl** | JavaScript | Trực quan hóa dữ liệu quy mô lớn trên bản đồ |
| **GDAL** | C++ (có liên kết Python) | Dịch dữ liệu raster và vector; con dao quân đội Thụy Sĩ |
| **Rasterio** | Python | Đọc/ghi dữ liệu raster; dựa trên GDAL |
| **Kepler.gl** | JavaScript | Trực quan hóa không gian địa lý được hỗ trợ bởi WebGL |
---

## Mẫu phân tích không gian địa lý
### Các kiểu phân tích phổ biến
| Mẫu | Mô tả | Trường hợp sử dụng |
|----------|-------------|----------|
| **Phân tích mẫu điểm** | Kiểm tra việc phân phối điểm | Lập bản đồ tội phạm; phát hiện ổ dịch |
| **Phân tích điểm nóng** | Tìm cụm có ý nghĩa thống kê | Địa điểm bán lẻ; tội phạm; dịch tễ học |
| **Phân tích mạng** | Tối ưu hóa tuyến đường; khu dịch vụ | Hậu cần; ứng phó khẩn cấp; tiện ích |
| **Nội suy không gian** | Ước tính giá trị tại các vị trí chưa được lấy mẫu | Chất lượng không khí; tính chất của đất; thời tiết |
| **Phát hiện thay đổi sử dụng đất** | So sánh ảnh vệ tinh theo thời gian | Sự mở rộng đô thị; phá rừng; nông nghiệp |
| **Phân tích sự phù hợp** | Tìm địa điểm đáp ứng nhiều tiêu chí | Lựa chọn địa điểm; quy hoạch bảo tồn |
| **Tự tương quan không gian** | Đo lường mức độ liên quan của các giá trị lân cận | Giá bất động sản; bệnh lây lan |
### Bài toán đơn vị diện tích có thể sửa đổi (MAUP)
| Khía cạnh | Vấn đề |
|--------|----------|
| **Hiệu ứng tỷ lệ** | Kết quả thay đổi tùy thuộc vào quy mô của đơn vị phân tích (các vùng điều tra dân số so với các quận so với các tiểu bang) |
| **Hiệu ứng phân vùng** | Kết quả thay đổi tùy thuộc vào cách vẽ ranh giới, thậm chí ở cùng một tỷ lệ |
| **Ngụ ý** | Đừng bao giờ cho rằng kết quả ở cấp độ tổng hợp này áp dụng ở cấp độ tổng hợp khác; luôn kiểm tra độ nhạy cảm với ranh giới |
---

## Những cân nhắc thực tế
| Mối quan tâm | Hướng dẫn |
|----------|----------|
| **Hệ thống tham chiếu tọa độ** | Luôn kiểm tra CRS; không bao giờ trộn lẫn các phép chiếu trong tính toán; biến đổi trước khi tính khoảng cách |
| **Chính xác** | Độ chính xác của dấu phẩy động quan trọng ở quy mô nhỏ; sử dụng các kiểu dữ liệu thích hợp |
| **Hiệu suất** | Các hoạt động không gian rất tốn kém; sử dụng chỉ số không gian; đơn giản hóa hình học để hiển thị |
| **Cấu trúc liên kết** | Đảm bảo hình học hợp lệ (không tự giao, đa giác khép kín) trước khi phân tích |
| **Tỷ lệ** | Web Mercator làm biến dạng khu vực; không sử dụng nó để tính diện tích |
| **Chất lượng dữ liệu** | Kiểm tra hình học null, các đỉnh trùng lặp, đa giác cúi |
---

## Bản tóm tắt
Phân tích không gian địa lý biến dữ liệu vị trí thành thông tin chi tiết hữu ích. Điểm, đường và đa giác đại diện cho các thực thể trong thế giới thực. Các hoạt động không gian - khoảng cách, vùng đệm, giao lộ, nối - trả lời các câu hỏi về khoảng cách gần, chồng chéo và ngăn chặn. Các công cụ đa dạng, từ PostGIS để phân tích quy mô cơ sở dữ liệu đến GeoPandas cho quy trình làm việc Python cho đến Deck.gl để trực quan hóa web. Những thách thức chính là chọn hệ tọa độ phù hợp, quản lý hiệu suất với bộ dữ liệu lớn và nhận thức được MAUP — thực tế là việc lựa chọn ranh giới tổng hợp sẽ ảnh hưởng đến kết quả của bạn. Cho dù bạn đang tối ưu hóa các tuyến đường phân phối, phân tích sự lây lan của bệnh tật hay lập bản đồ phát triển đô thị, thì phân tích không gian địa lý sẽ cung cấp bối cảnh không gian mà những con số thuần túy không thể nắm bắt được.