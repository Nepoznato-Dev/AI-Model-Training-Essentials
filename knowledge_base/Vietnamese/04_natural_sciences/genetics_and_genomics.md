---
# Metadata
title: "Genetics and Genomics"
description: "DNA, gene expression, CRISPR, GWAS, sequencing technologies"
category: "Natural Sciences"
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
reviewed_by: "Natural Sciences Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [genetics, genomics, natural-sciences]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Di truyền học và bộ gen
Di truyền học là nghiên cứu về tính di truyền - cách các đặc điểm được truyền từ cha mẹ sang con cái thông qua DNA. Genomics là nghiên cứu về toàn bộ bộ gen: tất cả các gen, các vùng không mã hóa, cách chúng tương tác và cách chúng khác nhau giữa các cá thể và quần thể. Quá trình chuyển đổi từ di truyền sang gen được thúc đẩy bởi công nghệ giải trình tự - chúng tôi đã đi từ nghiên cứu từng gen một đến đọc toàn bộ bộ gen trong vài giờ, tạo ra dữ liệu giúp biến đổi y học, nông nghiệp, pháp y và hiểu biết của chúng ta về quá trình tiến hóa.
---

## Cơ bản về DNA
###Cấu trúc ADN
| Thành phần | Mô tả |
|----------||-------------|
| **Nucleotide** | Khối xây dựng DNA; bao gồm một loại đường (deoxyribose), một nhóm photphat và một bazơ nitơ |
| **Căn cứ** ​​| Adenine (A), Thymine (T), Guanine (G), Cytosine (C) |
| **Ghép nối cơ bản** | A tạo cặp với T (2 liên kết hydro); G cặp với C (3 liên kết hydro) |
| **Chuỗi xoắn kép** | Hai sợi chạy ngược chiều nhau (5' đến 3' và 3' đến 5'); xoắn thành một vòng xoắn |
| **Nhiễm sắc thể** | Một phân tử DNA dài, đơn quấn quanh protein histone; con người có 46 (23 cặp) |
| **Bộ gen** | Bộ DNA hoàn chỉnh trong một sinh vật; bộ gen của con người là ~3,2 tỷ cặp bazơ |
### Giáo điều trung tâm của sinh học phân tử
| Bước | Quy trình | Vị trí | Sản phẩm |
|------|----------|----------|---------|
| **Sao chép** | ADN → ADN | Hạt nhân | Hai phân tử DNA giống hệt nhau |
| **Phiên âm** | ADN → mARN | Hạt nhân | RNA thông tin |
| **Dịch** | mARN → protein | Ribosome (tế bào chất) | Chuỗi polypeptide (protein) |
---

## Biểu hiện gen
### Gen được điều hòa như thế nào
| Cấp độ | Cơ chế | Ví dụ |
|-------|-------------|---------|
| **Biểu sinh** | Quá trình methyl hóa DNA; sửa đổi histone; tái cấu trúc chất nhiễm sắc | Làm im lặng một nhiễm sắc thể X ở nữ giới |
| **Phiên âm** | Các yếu tố phiên mã liên kết các chất xúc tiến/chất tăng cường; kích hoạt hoặc đàn áp | Lac operon ở vi khuẩn; gen đáp ứng hormone |
| **Sau phiên mã** | Nối thay thế; sự ổn định của mRNA; microRNA | Một gen → nhiều biến thể protein |
| **Dịch** | Sự sẵn có của ribosome; quy định yếu tố khởi đầu | Điều hòa sắt thông qua ferritin mRNA |
| **Hậu dịch** | Biến đổi protein (phosphoryl hóa, phổ biến hóa); xuống cấp | Kiểm soát chu kỳ tế bào |
---

## Mẫu kế thừa
### Di truyền học Mendel
| Mẫu | Mô tả | Ví dụ |
|----------|-------------|----------|
| **Tính trội nhiễm sắc thể thường** | Một bản sao của alen là đủ | bệnh Huntington; loạn sản |
| **Tính trạng lặn nhiễm sắc thể thường** | Cần có hai bản sao | Bệnh xơ nang; thiếu máu hồng cầu hình liềm |
| **Tính trội liên kết với X** | Gen trên nhiễm sắc thể X; đủ một bản | Hội chứng Rett |
| **Tính trạng lặn liên kết với X** | Gen trên nhiễm sắc thể X; nam giới bị ảnh hưởng nhiều hơn | bệnh máu khó đông; mù màu |
| **Đồng thống trị** | Cả hai alen đều biểu hiện như nhau | Nhóm máu ABO (A và B) |
| **Sự thống trị không hoàn toàn** | Dị hợp tử là trung gian | Hoa hồng từ bố mẹ đỏ và trắng |
| **Đa gen** | Nhiều gen góp phần tạo nên một tính trạng | Chiều cao; màu da; trí thông minh |
| **Đa năng** | Một gen ảnh hưởng đến nhiều tính trạng | Hội chứng Marfan (mô liên kết, mắt, tim) |
---

## Bộ gen
### Các loại gen
| Loại | Tập trung | Ứng dụng |
|------|-------|-------------|
| **Bộ gen cấu trúc** | Cấu trúc 3D của tất cả các protein trong bộ gen | Thiết kế thuốc; kỹ thuật protein |
| **Bộ gen chức năng** | Gen làm gì; tương tác gen; mẫu biểu thức | Tìm hiểu cơ chế bệnh tật |
| **Bộ gen so sánh** | So sánh bộ gen giữa các loài | Mối quan hệ tiến hóa; xác định khu vực bảo tồn |
| **Metanomics** | DNA từ các mẫu môi trường (không nuôi cấy) | Nghiên cứu hệ vi sinh vật; khám phá sinh vật mới |
| **Dược động học** | Gen ảnh hưởng đến phản ứng thuốc như thế nào | Thuốc cá nhân hóa; định lượng thuốc |
| **Dịch tễ học** | Sửa đổi biểu sinh trên toàn bộ gen | Chẩn đoán ung thư; sinh học phát triển |
### Công nghệ giải trình tự DNA
| Thế hệ | Công nghệ | Đọc Chiều Dài | Thông lượng | Tính năng chính |
|----------|————|-------------|-------------|-------------|
| **Thế hệ đầu tiên** | Trình tự Sanger | ~1.000 điểm cơ bản | Thấp | Độ chính xác tiêu chuẩn vàng; được sử dụng để xác nhận |
| **Thế hệ thứ hai** | Illumina (Solexa) | 50–300 điểm cơ bản | Rất cao | Đọc ngắn; nền tảng thống trị; chi phí thấp trên mỗi cơ sở |
| **Thế hệ thứ hai** | Ion Torrent | 200–400 điểm cơ bản | Cao | Dựa trên chất bán dẫn; không có quang học |
| **Thế hệ thứ ba** | PacBio (SMRT) | 10.000–100.000 điểm cơ bản | Trung bình | Đọc dài; giải quyết các vùng lặp đi lặp lại |
| **Thế hệ thứ ba** | Oxford Nanopore | Lên tới hàng triệu bp | Trung bình đến cao | Đọc siêu dài; di động (MinION); thời gian thực |
---

## Biến đổi gen
### Các loại biến thể
| Loại | Mô tả | Tần số |
|------|-------------|----------|
| **SNP** (Đa hình đơn Nucleotide) | Thay đổi cơ sở duy nhất | Phổ biến nhất; ~1 trong 1.000 căn cứ |
| **Chèn/Xóa (indel)** | Bổ sung hoặc loại bỏ căn cứ | Có thể gây đột biến dịch khung |
| **CNV** (Biến thể số bản sao) | Các phân đoạn trùng lặp hoặc bị xóa (1 kb – vài Mb) | Góp phần gây ra bệnh tật và tiến hóa |
| **Biến thể cấu trúc** | Đảo ngược; chuyển vị; sắp xếp lại lớn | Ít phổ biến hơn; có thể gây bệnh |
| **Vệ tinh vi mô (STR)** | Lặp lại song song ngắn (lặp lại 2–6 bp) | Pháp y; xét nghiệm quan hệ cha con |
### GWAS (Nghiên cứu liên kết toàn bộ bộ gen)
| Bước | Mô tả |
|------|-------------|
| **1. Thu thập mẫu** | Các trường hợp (có bệnh) và đối chứng (không có) |
| **2. Kiểu gen** | Sử dụng mảng SNP để tạo kiểu gen cho hàng trăm nghìn biến thể |
| **3. Kiểm tra thống kê** | Kiểm tra từng SNP để tìm mối liên hệ với đặc điểm |
| **4. Lô đất Manhattan** | Trực quan hóa kết quả trên tất cả các nhiễm sắc thể |
| **5. Sao chép** | Xác nhận phát hiện trong các mẫu độc lập |
---

## Chỉnh sửa gen
###CRISPR-Cas9
| Thành phần | Chức năng |
|----------||----------|
| **RNA hướng dẫn (gRNA)** | ~20 nucleotide; khớp với trình tự DNA mục tiêu |
| **Protein Cas9** | Kéo phân tử; cắt DNA tại vị trí mục tiêu |
| **Chuỗi PAM** | Họa tiết ngắn (NGG) bên cạnh mục tiêu; cần thiết cho ràng buộc Cas9 |
| **HDR** (Sửa chữa theo hướng tương đồng) | Chỉnh sửa chính xác bằng mẫu của nhà tài trợ |
| **NHEJ** (Tham gia kết thúc không tương đồng) | Sửa chữa dễ bị lỗi; tạo phần chèn/xóa (loại trực tiếp) |
###Ứng dụng chỉnh sửa gen
| Ứng dụng | Mô tả |
|-------------|-------------|
| **Điều trị** | Sửa chữa các đột biến gây bệnh (hồng cầu hình liềm; beta-thalassemia) |
| **Nông nghiệp** | cây trồng kháng bệnh; chăn nuôi cải tiến |
| **Nghiên cứu** | Tạo mô hình loại trực tiếp; nghiên cứu chức năng gen |
| **Ổ đĩa gen** | Truyền bá biến đổi gen trong quần thể (ví dụ: muỗi kháng bệnh sốt rét) |
---

## Cân nhắc về đạo đức
| Vấn đề | Mối quan tâm |
|-------|----------|
| **Quyền riêng tư về di truyền** | Ai sở hữu dữ liệu bộ gen của bạn? Người sử dụng lao động hoặc công ty bảo hiểm có thể sử dụng nó không? |
| **Chỉnh sửa gen trong phôi** | Những thay đổi có thể di truyền; những đứa trẻ được thiết kế riêng; tác động ngoài mục tiêu ngoài ý muốn |
| **Phân biệt đối xử về mặt di truyền** | GINA (Mỹ) bảo vệ chống lại một số sự phân biệt đối xử nhưng có những khoảng trống |
| **Sự đồng ý có hiểu biết** | Dữ liệu gen tiết lộ thông tin về người thân chưa đồng ý |
| **Lưu trữ dữ liệu** | Bộ gen lớn (~200 GB thô); những thách thức về bảo mật và lưu trữ lâu dài |
| **Vốn chủ sở hữu** | Y học gen có nguy cơ làm gia tăng sự chênh lệch về sức khỏe nếu chỉ dành cho những người giàu có |
---

## Bản tóm tắt
Di truyền học nghiên cứu cách các gen riêng lẻ hoạt động và được di truyền. Genomics nghiên cứu toàn bộ bộ gen - tất cả các gen, sự tương tác và biến thể của chúng. DNA được phiên mã thành RNA, sau đó được dịch mã thành protein. Sự biểu hiện gen được điều hòa ở nhiều cấp độ: biểu sinh, phiên mã, hậu phiên mã, dịch mã và hậu dịch mã. Sự kế thừa tuân theo các kiểu mẫu (chiếm ưu thế, lặn, đa gen) xác định cách các tính trạng được truyền qua giữa các thế hệ. Các công nghệ giải trình tự hiện đại (Illumina, PacBio, Nanopore) có thể đọc toàn bộ bộ gen một cách nhanh chóng và rẻ. CRISPR-Cas9 cho phép chỉnh sửa gen chính xác với tiềm năng biến đổi trong y học và nông nghiệp. Những thách thức lớn nhất là đạo đức: ai kiểm soát dữ liệu gen, cách điều chỉnh chỉnh sửa gen trong phôi và làm thế nào để đảm bảo y học gen mang lại lợi ích cho tất cả mọi người, không chỉ những người có đặc quyền.