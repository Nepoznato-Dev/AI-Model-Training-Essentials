<!--
---
# Metadata
title: "Embedded Systems and IoT"
description: "Microcontrollers, sensors, RTOS, IoT protocols, edge computing"
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
tags: [embedded, systems, iot, coding-and-technology]
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
# Hệ thống nhúng và IoT
Hệ thống nhúng là các máy tính ẩn bên trong các thiết bị khác - bộ điều khiển động cơ ô tô, bộ điều khiển máy giặt, bộ vi điều khiển trong bộ điều chỉnh nhiệt thông minh. Không giống như các máy tính đa năng, chúng được thiết kế cho các tác vụ cụ thể, thường có những hạn chế chặt chẽ về nguồn điện, bộ nhớ và tốc độ xử lý. Internet of Things (IoT) mở rộng các hệ thống nhúng bằng cách kết nối chúng với mạng, cho phép giám sát, điều khiển và thu thập dữ liệu từ xa. Cùng nhau, chúng đại diện cho hàng tỷ thiết bị điện toán tương tác với thế giới vật chất.
---

## Nguyên tắc cơ bản về hệ thống nhúng
### Điều gì tạo nên sự khác biệt cho tính năng nhúng
| Khía cạnh | Máy tính đa năng | Hệ thống nhúng |
|--------|---------------------------------------|-----------------|
| **Mục đích** | Chạy bất kỳ phần mềm nào | Thực hiện nhiệm vụ cụ thể |
| **Tài nguyên** | CPU, RAM, bộ nhớ dồi dào | Giới hạn (KB đến MB RAM; MHz đến GHz thấp) |
| **Sức mạnh** | Cắm điện hoặc pin lớn | Thường chạy bằng pin hoặc thu năng lượng |
| **HĐH** | Hệ điều hành đầy đủ (Windows, Linux, macOS) | RTOS, kim loại trần hoặc Linux nhúng |
| **Giao diện người dùng** | Giàu có (màn hình, bàn phím, chuột) | Tối thiểu (đèn LED, nút, cảm biến) hoặc không có |
| **Thời gian thực** | Nỗ lực hết mình | Thường khó khăn về thời hạn thời gian thực |
| **Trọn đời** | 3-7 tuổi | 10-25+ năm |
### Vi điều khiển vs Vi xử lý
| Tính năng | Vi điều khiển (MCU) | Bộ vi xử lý (MPU) |
|----------|----------------------|----------------------|
| **Tích hợp** | CPU + RAM + Flash + thiết bị ngoại vi trên một chip | chỉ CPU; RAM và bộ nhớ ngoài |
| **Hiệu suất** | Thấp đến trung bình (dải MHz) | Cao (phạm vi GHz) |
| **Sức mạnh** | Rất thấp (µA đến mA) | Cao hơn (hàng trăm mA đến ampe) |
| **Chi phí** | 0,10 USD - 10 USD | $5 - $100+ |
| **Ví dụ** | STM32, ESP32, Arduino (ATmega), nRF52 | Raspberry Pi (BCM2835), i.MX, Allwinner |
| **Trường hợp sử dụng** | Cảm biến, cơ cấu chấp hành, điều khiển đơn giản | Hiển thị, xử lý phức tạp, Linux |
---

## Nền tảng nhúng phổ biến
| Nền tảng | MCU/MPU | Tính năng chính | Tốt nhất cho |
|----------|----------|-------------|----------|
| **Arduino** | ATmega328P (và những người khác) | Đơn giản; cộng đồng lớn | Học hỏi; tạo mẫu |
| **ESP32** | Espressif lõi kép | Wi-Fi + Bluetooth; chi phí thấp | dự án IoT; thiết bị được kết nối |
| **Mâm xôi Pi Pico** | RP2040 (ARM lõi kép) | Có thể chi trả; Hỗ trợ MicroPython | Giáo dục; dự án sở thích |
| **STM32** | Dòng ARM Cortex-M | Cấp công nghiệp; phạm vi rộng | nhúng chuyên nghiệp; công nghiệp |
| **nRF52/nRF53** | Chất bán dẫn Bắc Âu | Chuyên gia Bluetooth năng lượng thấp | Thiết bị đeo được; đèn hiệu |
| **Pi mâm xôi** | Broadcom BCM (ARM) | Linux đầy đủ; Chân GPIO | Nguyên mẫu; trung tâm truyền thông; tính toán biên nhẹ |
| **BeagleBone** | TI Sitara (CÁNH TAY) | Lõi PRU thời gian thực | Công nghiệp; ứng dụng thời gian thực |
| **ESP32-S3** | Espressif | tăng tốc AI; USB | AI cạnh; ứng dụng tầm nhìn |
---

## Hệ điều hành thời gian thực (RTOS)
RTOS đảm bảo rằng các nhiệm vụ quan trọng sẽ hoàn thành trong một khoảng thời gian xác định.
| RTOS | Giấy phép | Tốt nhất cho |
|------|----------|----------|
| **RTOS miễn phí** | MIT | Phổ biến nhất; hỗ trợ MCU rộng rãi |
| **Zephyr** | Apache 2.0 | Hiện đại; Quỹ Linux; hệ sinh thái đang phát triển |
| **ThreadX (Azure RTOS)** | MIT | Đã xác nhận an toàn; IoT |
| **embOS** | Thương mại | Công nghiệp; được chứng nhận |
| **Chủ đề RT** | Apache 2.0 | hệ sinh thái Trung Quốc; đang phát triển trên toàn cầu |
### RTOS so với kim loại trần
| Khía cạnh | Kim loại trần | RTOS |
|--------|-------------|------|
| **Độ phức tạp** | Đơn giản cho những công việc đơn giản | Cần thiết cho các nhiệm vụ phức tạp, đồng thời |
| **Lên lịch** | Hướng dẫn sử dụng (vòng lặp chính + ngắt) | Lập kế hoạch ưu tiên với các ưu tiên |
| **Khả năng mở rộng** | Khó thêm tính năng | Dễ dàng thêm nhiệm vụ |
| **Bộ nhớ** | Chi phí tối thiểu | Chi phí nhỏ (vài KB) |
---

## Giao thức truyền thông
### Giao thức có dây
| Giao thức | Tốc độ | Khoảng cách | Trường hợp sử dụng |
|----------|-------|----------|----------|
| **UART** | Lên tới 1 Mb/giây | Ngắn (trên tàu) | Bảng điều khiển gỡ lỗi; Mô-đun GPS |
| **SPI** | Lên tới 100 MHz | Ngắn (trên tàu) | Thiết bị ngoại vi tốc độ cao (màn hình, đèn flash) |
| **I²C** | Lên tới 3,4 MHz | Ngắn (trên tàu) | Cảm biến; truyền thông có số lượng pin thấp |
| ** CÓ THỂ ** | Lên tới 1 Mb/giây | Lên tới 1 km | Ô tô; công nghiệp |
| **Ethernet** | 10 Mb/giây - 100 Gb/giây | Lên đến 100 m | Kết nối mạng; công nghiệp (có phần mở rộng) |
| **USB** | Lên tới 40 Gbps (USB4) | Lên đến 5 m | Thiết bị ngoại vi; sạc |
### Giao thức không dây
| Giao thức | Phạm vi | Quyền lực | Tốc độ | Trường hợp sử dụng |
|----------|-------|-------|-------|----------|
| **Wi-Fi** | ~100 m | Cao | Lên đến Wi-Fi 7 (lý thuyết là 46 Gbps) | IoT băng thông cao; phát trực tuyến |
| **Bluetooth cổ điển** | ~100 m | Trung bình | 1-3 Mb/giây | Âm thanh; chuyển tập tin |
| **BLE** (Bluetooth năng lượng thấp) | ~100 m | Rất thấp | 1-2 Mb/giây | Thiết bị đeo được; đèn hiệu; cảm biến |
| **Zigbee** | ~100 m (lưới) | Thấp | 250 kbps | Tự động hóa nhà; cảm biến công nghiệp |
| **Sóng Z** | ~100 m (lưới) | Thấp | 100 kbps | Tự động hóa nhà |
| **LoRa / LoRaWAN** | Lên tới 15 km | Rất thấp | 0,3-50 kbps | Nông nghiệp; tiện ích; cảm biến toàn thành phố |
| **NB-IoT** | Vùng phủ sóng di động | Thấp | 250 kbps | Đo sáng; theo dõi tài sản |
| **Chủ đề / Vấn đề** | ~100 m (lưới) | Thấp | Trung bình | Nhà thông minh (Apple, Google, Amazon) |
| **Di động (4G/5G)** | Toàn cầu | Cao | Cao | Xe được kết nối; giám sát từ xa |
---

## Kiến trúc IoT
### Ngăn xếp IoT
| Lớp | Chức năng | Ví dụ |
|-------|----------|---------|
| **Thiết bị** | Cảm biến, cơ cấu chấp hành, vi điều khiển | ESP32, STM32, Raspberry Pi |
| **Kết nối** | Giao thức mạng | MQTT, HTTP, CoAP, LoRaWAN |
| **Điện toán biên** | Xử lý gần thiết bị | AWS Greengrass, Azure IoT Edge |
| **Nền tảng đám mây** | Nhập, lưu trữ, xử lý dữ liệu | AWS IoT, Azure IoT Hub, Google Cloud IoT |
| **Ứng tuyển** | Trang tổng quan, phân tích, cảnh báo | Grafana, ứng dụng web tùy chỉnh |
### Giao thức truyền thông IoT
| Giao thức | Mẫu | Tốt nhất cho |
|----------|----------|----------|
| **MQTT** | Xuất bản/đăng ký; nhẹ | Hầu hết các ứng dụng IoT; băng thông thấp |
| **HTTP/NGƯỜI NGÀY** | Yêu cầu/phản hồi | Khi sự đơn giản quan trọng; tích hợp web |
| **CoAP** | Yêu cầu/phản hồi; Dựa trên UDP | Thiết bị bị hạn chế; điện năng thấp |
| **AMQP** | Xếp hàng tin nhắn | IoT doanh nghiệp; giao hàng đáng tin cậy |
| **WebSocket** | Hai chiều; kết nối liên tục | Bảng điều khiển thời gian thực; dữ liệu trực tiếp |
### MQTT chi tiết
| Khái niệm | Mô tả |
|----------|-------------|
| **Nhà môi giới** | Máy chủ trung tâm định tuyến tin nhắn (Mosquitto, EMQX, HiveMQ) |
| **Chủ đề** | Địa chỉ phân cấp (ví dụ:`home/living-room/temperature`) |
| **QoS** | 0 (tối đa một lần), 1 (ít nhất một lần), 2 (chính xác một lần) |
| **Tin nhắn được giữ lại** | Tin nhắn cuối cùng về một chủ đề; gửi tới người đăng ký mới |
| **Di chúc cuối cùng** | Thông báo được xuất bản khi máy khách ngắt kết nối đột ngột |
---

## Điện toán biên
Xử lý dữ liệu gần nguồn thay vì gửi mọi thứ lên đám mây.
| Lợi ích | Mô tả |
|----------|-------------|
| **Giảm độ trễ** | Không có chuyến đi khứ hồi lên đám mây; quyết định ngay lập tức |
| **Tiết kiệm băng thông** | Chỉ gửi bản tóm tắt hoặc điểm bất thường |
| **Quyền riêng tư** | Dữ liệu nhạy cảm được giữ nguyên tại chỗ |
| **Độ tin cậy** | Hoạt động khi internet bị hỏng |
| Nền tảng | Mô tả |
|----------|-------------|
| **AWS Greengrass** | Chạy các hàm Lambda trên các thiết bị biên |
| **Azure IoT Edge** | Chạy container trên các thiết bị biên |
| **NVIDIA Jetson** | AI biên được tăng tốc GPU (Orin, Nano) |
| **Pi mâm xôi** | Điện toán biên nhẹ |
---

## Cập nhật chương trình cơ sở (OTA)
Các bản cập nhật qua mạng cho phép bạn sửa lỗi và thêm tính năng cho các thiết bị được triển khai.
| Mối quan tâm | Giải pháp |
|----------|----------|
| **Độ tin cậy** | Đèn flash ngân hàng kép; quay trở lại khi thất bại |
| **An ninh** | Hình ảnh có chữ ký; chuyển mã hóa |
| **Kích thước** | Cập nhật Delta (chỉ thay đổi các phần) |
| **Kết nối** | Xếp hàng cập nhật khi thiết bị trực tuyến |
---

## Hệ thống nhúng quan trọng về an toàn
| Tên miền | Tiêu chuẩn | Ví dụ |
|--------|-------------|---------|
| **Ô tô** | ISO 26262 (ASIL A-D) | Điều khiển động cơ, phanh, túi khí |
| **Y tế** | IEC 62304 | Máy điều hòa nhịp tim, bơm truyền dịch |
| **Hàng không vũ trụ** | DO-178C (DAL A-E) | Điều khiển chuyến bay, dẫn đường |
| **Công nghiệp** | IEC 61508 (SIL 1-4) | PLC, bộ điều khiển an toàn |
| **Đường sắt** | EN 50128 (SIL 1-4) | Tín hiệu, điều khiển tàu |
---

## Công cụ và phát triển
| Công cụ | Mục đích |
|------|----------|
| **Nền tảngIO** | Phát triển nhúng đa nền tảng (Arduino, ESP32, STM32) |
| **STM32CubeIDE** | IDE chính thức của ST cho STM32 |
| **IDE Arduino** | Phát triển đơn giản cho Arduino và các bo mạch tương thích |
| **ESP-IDF** | SDK chính thức của Espressif dành cho ESP32 |
| **SDK Zephyr** | Hệ thống xây dựng phía Tây cho Zephyr RTOS |
| **OpenOCD** | Gỡ lỗi trên chip |
| **Máy phân tích logic** | Gỡ lỗi giao thức SPI, I²C, UART |
| **Wireshark** | Phân tích giao thức mạng |
---

## Bản tóm tắt
Hệ thống nhúng và IoT đại diện cho sự giao thoa giữa phần mềm và thế giới vật lý. Từ bộ vi điều khiển điều khiển động cơ đến mạng cảm biến kết nối với đám mây, chúng đòi hỏi tư duy khác với việc phát triển ứng dụng hoặc web: nguồn lực hạn chế, yêu cầu về thời gian thực, tuổi thọ dài và hậu quả của lỗi trong thế giới vật lý. Hệ sinh thái đã phát triển vượt bậc — các khung như ESP-IDF và Zephyr giúp việc phát triển chuyên nghiệp có thể tiếp cận được, trong khi các nền tảng như AWS IoT và Azure IoT Hub xử lý phía đám mây. Các kỹ năng chính là hiểu giao diện phần cứng, giao thức truyền thông, quản lý năng lượng và kỷ luật viết phần mềm phải chạy đáng tin cậy trong nhiều năm mà không cần can thiệp.