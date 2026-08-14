---
# Metadata
title: "Signal Processing"
description: "Fourier transforms, FFT, Laplace transforms, Z-transforms, filtering, sampling theorem, windowing, spectral analysis, and wavelets"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial deep-dive into signal processing"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [signal-processing, fourier-transform, fft, laplace-transform, z-transform, filtering, sampling-theorem, wavelets]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "optics_and_waves.md"
  - "numerical_methods.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Xử lý tín hiệu
Xử lý tín hiệu là khoa học phân tích, sửa đổi và tổng hợp tín hiệu - biểu diễn các đại lượng vật lý thay đổi theo thời gian, không gian hoặc tần số. Âm thanh, hình ảnh, video, dữ liệu cảm biến, sóng não, giá cổ phiếu - tất cả đều là tín hiệu. Các công cụ toán học xử lý tín hiệu (biến đổi Fourier, bộ lọc, lý thuyết lấy mẫu) là nền tảng cho học máy, truyền thông, hình ảnh y tế và hầu như mọi lĩnh vực hoạt động với dữ liệu.
---

## Tín hiệu và hệ thống
### Phân loại tín hiệu
| Loại | Mô tả | Ví dụ |
|------|-------------|----------|
| **Thời gian liên tục** | Được xác định cho mọi t ∈ ℝ | Âm thanh điện áp, nhiệt độ |
| **Thời gian rời rạc** | Được xác định tại các chỉ số nguyên n | Âm thanh được lấy mẫu, giá trị pixel |
| **Tương tự** | Liên tục theo thời gian và biên độ | Rãnh ghi vinyl |
| **Kỹ thuật số** | Rời rạc theo thời gian và biên độ lượng tử hóa | Tệp MP3, hình ảnh JPEG |
| **Định kỳ** | x(t + T) = x(t) với mọi t | Sóng hình sin, sóng vuông |
| **Không định kỳ** | Không lặp lại mẫu | Lời nói, âm nhạc |
| **Xác định** | Hoàn toàn có thể dự đoán được | Sóng hình sin |
| **Ngẫu nhiên** | Chứa tính ngẫu nhiên | Tiếng ồn, giá cổ phiếu |
### Thuộc tính hệ thống
| Bất động sản | Định nghĩa | Ví dụ |
|----------|-------------|----------|
| **Tuyến tính** | T[ax₁ + bx₂] = aT[x₁] + bT[x₂] | Bộ lọc thông thấp |
| **Bất biến theo thời gian** | Sự thay đổi đầu vào → sự thay đổi tương tự ở đầu ra | Bất kỳ bộ lọc cố định nào |
| **Nhân quả** | Đầu ra chỉ phụ thuộc vào đầu vào hiện tại và quá khứ | Hệ thống thời gian thực |
| **Ổn định (BIBO)** | Đầu vào bị giới hạn → đầu ra bị giới hạn | Bộ lọc được thiết kế tốt |
| **Không có trí nhớ** | Đầu ra chỉ phụ thuộc vào đầu vào hiện tại | Bộ khuếch đại |
---

## Biến đổi Fourier
**Biến đổi Fourier** phân tách tín hiệu thành các tần số cấu thành của nó.
### Biến đổi Fourier liên tục
X(f) = ∫_{−∞}^{∞} x(t) e^{−j2πft} dt
Nghịch đảo: x(t) = ∫_{−∞}^{∞} X(f) e^{j2πft} df
### Cặp biến đổi Fourier
| Miền thời gian x(t) | Miền tần số X(f) |
|-------------------|----------------------|
| Xung hình chữ nhật | hàm chân thành |
| hàm chân thành | Xung hình chữ nhật |
| Gaussian e^{−at²} | Gaussian (√(π/a))e^{−π²f²/a} |
| Đồng bằng Dirac δ(t) | 1 (tất cả các tần số) |
| Hàm mũ phức e^{j2πf₀t} | δ(f − f₀) |
| Cosin cos(2πf₀t) | ½[δ(f−f₀) + δ(f+f₀)] |
### Thuộc tính chính
| Bất động sản | Miền thời gian | Miền tần số |
|----------|-------------|--------|
| Tuyến tính | ax₁(t) + bx₂(t) | aX₁(f) + bX₂(f) |
| Chuyển đổi thời gian | x(t − t₀) | X(f)e^{−j2πft₀} |
| Chuyển tần số | x(t)e^{j2πf₀t} | X(f − f₀) |
| Tích chập | x₁(t) ∗ x₂(t) | X₁(f) · X₂(f) |
| Phép nhân | x₁(t) · x₂(t) | X₁(f) ∗ X₂(f) |
| Sự khác biệt | dx/dt | j2πf X(f) |
| Định lý Parseval | ∫\|x(t)\|2 dt | ∫\|X(f)\|2 df |
**Định lý tích chập:** Tích chập theo thời gian = nhân tần số. Đây là thuộc tính quan trọng nhất - nó biến các phép tính tích chập đắt tiền thành các phép nhân rẻ tiền.
### Biến đổi Fourier rời rạc (DFT)
Đối với dãy x[0], x[1], ..., x[N−1]:
X[k] = Σ_{n=0}^{N−1} x[n] e^{−j2πkn/N}, k = 0, 1, ..., N−1
| Bất động sản | Giá trị |
|----------|-------|
| Đầu vào | N mẫu thực hoặc phức tạp |
| Đầu ra | N thùng tần số phức tạp |
| Độ phân giải tần số | f_s/N (trong đó f_s là tốc độ lấy mẫu) |
| Tần số Nyquist | f_s/2 (tần số biểu thị tối đa) |
| Độ phức tạp | Tính toán trực tiếp O(N²) |
### Biến đổi Fourier nhanh (FFT)
**FFT** tính toán DFT theo O(N log N) thay vì O(N²).
| N | Hoạt động O(N²) | O(N log N) Hoạt động | Tăng tốc |
|---|-------------------|----------------------|--------|
| 1.024 | 1.048.576 | 10.240 | 102× |
| 1.048.576 | 1,1 × 10¹² | 20.971.520 | 52.428× |
FFT là một trong những thuật toán quan trọng nhất từng được phát minh. Nó cho phép xử lý âm thanh theo thời gian thực, nén hình ảnh (JPEG), giao tiếp không dây (OFDM) và phân tích quang phổ.
---

## Biến đổi Laplace
**Biến đổi Laplace** mở rộng biến đổi Fourier để xử lý các hệ thống không ổn định và phân tích nhất thời.
F(s) = ∫₀^∞ f(t) e^{−st} dt, trong đó s = σ + jω
### Các phép biến đổi Laplace thông thường
| f(t) | F(s) | Vùng Hội Tụ |
|------|------|----------------------|
| δ(t) (xung) | 1 | Tất cả |
| u(t) (bước) | 1/giây | (Các) Người > 0 |
| e^{−at}u(t) | 1/(s+a) | Re(s) > −a |
| bạn(t) | n!/s^{n+1} | (Các) Người > 0 |
| sin(ωt)u(t) | ω/(s²+ω²) | (Các) Người > 0 |
| cos(ωt)u(t) | s/(s2+ω2) | (Các) Người > 0 |
### Kết nối với biến đổi Fourier
Khi σ = 0 (s = jω), biến đổi Laplace giảm thành biến đổi Fourier. Phép biến đổi Laplace cung cấp một bức tranh hoàn chỉnh hơn bằng cách bao gồm thông tin về sự tăng trưởng/suy giảm (σ).
---

## Biến đổi Z
**Biến đổi Z** là tương đương thời gian rời rạc của biến đổi Laplace.
X(z) = Σ_{n=−∞}^{∞} x[n] z^{−n}
### Các phép biến đổi Z phổ biến
| x[n] | X(z) | ROC |
|------|------|------|
| δ[n] | 1 | Tất cả z |
| u[n] (bước) | z/(z−1) | \|z\| > 1 |
| aⁿu[n] | z/(z−a) | \|z\| > \|a\| |
| naⁿu[n] | az/(z−a)² | \|z\| > \|a\| |
| sin(ω₀n)u[n] | z sin(ω₀)/(z²−2z cos(ω₀)+1) | \|z\| > 1 |
### Mối quan hệ với các biến đổi khác
| Chuyển đổi | Tên miền | Biến |
|----------|----------|----------|
| Fourier | Tần số liên tục | f hoặc ω |
| Laplace | Tần số phức tạp | s = σ + jω |
| Biến đổi Z | Tần số phức (rời rạc) | z = e^{sT} |
Đường tròn đơn vị trong mặt phẳng z (|z| = 1) tương ứng với phép biến đổi Fourier.
---

## Bộ lọc
Bộ lọc chọn lọc vượt qua hoặc chặn các thành phần tần số nhất định.
### Loại bộ lọc
| Loại | Vượt qua | Khối | Ứng dụng |
|------|--------|--------|-------------|
| **Thông thấp** | Tần số thấp | Tần số cao | Làm mịn, khử răng cưa |
| **Thông cao** | Tần số cao | Tần số thấp | Phát hiện cạnh, loại bỏ tiếng ồn |
| **Băng thông** | Một dải tần số | Ngoài phạm vi | Lựa chọn kênh (radio) |
| **Dải băng (rãnh)** | Mọi thứ ngoại trừ một phạm vi | Một phạm vi cụ thể | Loại bỏ tiếng ồn trên đường dây điện |
### Bộ lọc FIR và IIR
| Bất động sản | FIR (Phản hồi xung hữu hạn) | IIR (Phản hồi xung vô hạn) |
|----------|----------------------------------------------|--------------------------------|
| Phản ứng xung | Thời lượng hữu hạn | Thời lượng vô hạn |
| Tính ổn định | Luôn ổn định | Có thể không ổn định |
| Giai đoạn | Có thể chính xác tuyến tính | Nói chung pha phi tuyến |
| Phản hồi | Không | Có |
| Tính toán | Cần thêm hệ số | Ít hệ số hơn cho cùng một lần tung ra |
| Thiết kế | Cửa sổ, Công viên-McClellan | Butterworth, Chebyshev, hình elip |
| Hàm chuyển | H(z) = Σ bₖz⁻ᵏ | H(z) = Σ bₖz⁻ᵏ / (1 + Σ aₖz⁻ᵏ) |
### Thông số kỹ thuật thiết kế bộ lọc
| Tham số | Mô tả |
|----------||-------------|
| **Băng thông** | Dải tần có thể vượt qua với tổn thất tối thiểu |
| **Dây chặn** | Dải tần số cần giảm bớt |
| **Tần số cắt** | Ranh giới giữa băng thông và băng chặn |
| **Gợn** | Sự thay đổi độ lợi băng thông (hoặc băng chặn) |
| **Cuộn ra** | Tốc độ suy giảm (dB trên quãng tám hoặc thập kỷ) |
| **Dải chuyển tiếp** | Vùng giữa băng thông và băng chặn |
### Thiết kế bộ lọc phổ biến
| Thiết kế | Đặc điểm | Trường hợp sử dụng |
|--------|-------|----------|
| **Bơ** | Băng thông phẳng tối đa, độ cuộn vừa phải | Mục đích chung |
| **Ch Quashev Loại I** | Gợn sóng trong băng thông, độ dốc cao hơn | Khi việc triển khai trở nên quan trọng |
| **Chebyshev Loại II** | Gợn sóng trong băng chặn, băng thông phẳng | Khi độ phẳng của băng thông có vấn đề |
| **Hình elip (Cauer)** | Gợn sóng ở cả hai, độ dốc lớn nhất | Yêu cầu đặt hàng tối thiểu |
| **Bessel** | Pha tuyến tính (độ trễ nhóm phẳng tối đa) | Bảo toàn dạng sóng |
---

## Lý thuyết lấy mẫu
### Định lý lấy mẫu Nyquist-Shannon
Tín hiệu liên tục có thể được tái tạo hoàn hảo từ các mẫu của nó nếu tốc độ lấy mẫu vượt quá hai lần tần số tối đa:
f_s > 2f_max
| Kỳ hạn | Định nghĩa |
|------|-------------|
| **Tốc độ lấy mẫu** (f_s) | Số lượng mẫu mỗi giây |
| **Tỷ lệ Nyquist** | 2f_max (tốc độ lấy mẫu tối thiểu) |
| **Tần số Nyquist** | f_s/2 (tần số biểu thị tối đa) |
| **Bí danh** | Tần số cao giả dạng tần số thấp khi f_s < 2f_max |
### Tỷ lệ lấy mẫu phổ biến
| Ứng dụng | Tỷ lệ | Tần số Nyquist |
|-------------|------|-------------------|
| Bài phát biểu qua điện thoại | 8 kHz | 4 kHz |
| CD âm thanh | 44,1 kHz | 22,05 kHz |
| Âm thanh chuyên nghiệp | 48 kHz | 24 kHz |
| Âm thanh độ phân giải cao | 96 kHz | 48 kHz |
| Video (30 khung hình / giây) | 30 Hz (tạm thời) | 15Hz |
### Khử răng cưa
Trước khi lấy mẫu, **bộ lọc khử răng cưa** (thông thấp) sẽ loại bỏ các tần số trên f_s/2 để tránh hiện tượng răng cưa.
---

## Cửa sổ
Khi phân tích một đoạn tín hiệu hữu hạn, chúng ta ngầm nhân với một cửa sổ hình chữ nhật, gây rò rỉ quang phổ. **Chức năng cửa sổ** giảm hiện tượng rò rỉ này.
### Windows thông thường
| Cửa sổ | Chiều rộng thùy chính | Cấp thùy bên | Trường hợp sử dụng |
|--------|-------|-----------------|----------|
| Hình chữ nhật | Thu hẹp nhất | −13 dB | Khi độ phân giải quan trọng nhất |
| Hann | 2× hình chữ nhật | −31 dB | Mục đích chung |
| Hamming | 2× hình chữ nhật | −41 dB | Giảm thùy bên gần nhất |
| Người da đen | 3× hình chữ nhật | −58 dB | Dải động cao |
| Kaiser | Có thể điều chỉnh | Có thể điều chỉnh (thông qua β) | Khi sự đánh đổi có thể điều chỉnh được |
### Rò rỉ quang phổ
Nhân tín hiệu với một cửa sổ sẽ kết hợp phổ của nó với phổ của cửa sổ. Các búp chính rộng hơn làm giảm độ phân giải tần số; thùy bên dưới làm giảm rò rỉ.
---

## Wavelet
**Wavelets** là các hàm dạng sóng nhỏ, cục bộ được sử dụng để phân tích tín hiệu đa độ phân giải.
### Biến đổi Wavelet
Không giống như biến đổi Fourier (cung cấp thông tin tần số toàn cầu), biến đổi wavelet cung cấp định vị **tần số thời gian**.
| Chuyển đổi | Độ phân giải thời gian | Độ phân giải tần số |
|----------|--------------------------------|----------------------|
| Fourier | Không có (toàn cầu) | Xuất sắc |
| FT thời gian ngắn | Đã sửa (kích thước cửa sổ) | Đã sửa |
| Wavelet | Có thể thay đổi (tốt ở tần số cao) | Có thể thay đổi (tốt ở tần số thấp) |
### Các họ Wavelet chung
| Gia đình | Thuộc tính | Ứng dụng |
|--------|-------------|-------------|
| **Haar** | Đơn giản nhất, không liên tục | Phát hiện cạnh, phân tích nhanh |
| **Daubechies** (dbN) | Hỗ trợ nhỏ gọn, N khoảnh khắc biến mất | Nén, khử nhiễu |
| **Symlets** | Daubechies gần như đối xứng | Giảm méo pha |
| **Coiflets** | Được thiết kế cho điều kiện thời điểm | Xử lý tín hiệu |
| **Morlet** | hình sin cửa sổ Gaussian | Phân tích tần số thời gian |
| **Mũ Mexico** | Đạo hàm bậc hai của Gaussian | Phát hiện tính năng |
### Ứng dụng của Wavelet
| Ứng dụng | Wavelet trợ giúp như thế nào |
|-------------|-------------------|
| Nén hình ảnh (JPEG 2000) | Biểu diễn đa độ phân giải, tốt hơn DCT cho các cạnh |
| Khử nhiễu | Ngưỡng hệ số wavelet nhỏ (tín hiệu có hệ số lớn) |
| Phát hiện tính năng | Phát hiện cạnh, phát hiện nhất thời trong chuỗi thời gian |
| Phân tích ECG | Phát hiện phức hợp QRS, phân loại rối loạn nhịp tim |
| Phân tích địa chấn | Xác định các lớp địa chất, xử lý tín hiệu động đất |
---

## Mức độ liên quan đến Học máy và Khoa học dữ liệu
| Khái niệm xử lý tín hiệu | Ứng dụng |
|--------------------------|-------------|
| Biến đổi Fourier | Tính năng quang phổ cho âm thanh ML, phân tích miền tần số của chuỗi thời gian |
| FFT | Tích chập nhanh trong CNN (tích chập quang phổ), tương quan hiệu quả |
| Định lý tích chập | Hiểu cách hoạt động của CNN (chúng là các bộ lọc đã học) |
| Bộ lọc | Tiền xử lý (làm mịn, khử nhiễu), trích xuất đặc trưng |
| Định lý lấy mẫu | Tìm hiểu sự rời rạc, chọn tốc độ cảm biến, tránh hiện tượng răng cưa |
| Cửa sổ | STFT cho ML âm thanh (sơ đồ phổ), phân tích tần số thời gian |
| Wavelet | Trích xuất tính năng cho chuỗi thời gian, nén, khử nhiễu |
| Biến đổi Laplace/Z | Lý thuyết điều khiển robot, hiểu tính ổn định của hệ thống |
| Phân tích quang phổ | phân tích EEG/fMRI, theo dõi độ rung, bảo trì dự đoán |
| Tỷ lệ Nyquist | Chọn tốc độ thu thập dữ liệu phù hợp cho đường ống ML |
---

## Bản tóm tắt
| Công cụ | Tên miền | Thông tin chi tiết chính |
|------|--------|-------------|
| Biến đổi Fourier | Thời gian → Tần suất | Tín hiệu là tổng của các hình sin |
| Biến đổi Laplace | Thời gian → Tần số phức tạp | Xử lý quá độ và ổn định |
| Biến đổi Z | Thời gian rời rạc → Phức tạp | Phân tích và thiết kế bộ lọc kỹ thuật số |
| FFT | Tính toán DFT hiệu quả | O(N log N) thay vì O(N2) |
| Bộ lọc | Lựa chọn tần số | Truyền những gì bạn cần, chặn những gì bạn không |
| Định lý lấy mẫu | Liên tục ↔ rời rạc | Lấy mẫu đủ nhanh, không mất gì |
| Cửa sổ | Đánh đổi tần số thời gian | Độ phân giải cân bằng và rò rỉ |
| Wavelet | Phân tích đa độ phân giải | Địa phương cả về thời gian và tần suất |
Xử lý tín hiệu cung cấp nền tảng toán học để hiểu, phân tích và thao tác dữ liệu. Mọi quy trình học máy hoạt động với dữ liệu chuỗi thời gian, âm thanh, hình ảnh hoặc cảm biến đều sử dụng các khái niệm xử lý tín hiệu. Đặc biệt, phép biến đổi Fourier được cho là công cụ toán học quan trọng nhất sau phép tính đối với bất kỳ nhà khoa học dữ liệu nào.