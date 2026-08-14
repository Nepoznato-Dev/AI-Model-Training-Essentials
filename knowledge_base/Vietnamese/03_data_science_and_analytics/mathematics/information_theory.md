<!--
---
# Metadata
title: "Information Theory"
description: "Shannon entropy, differential entropy, joint and mutual information, KL divergence, cross-entropy, channel capacity, source coding, compression, and connections to machine learning loss functions"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "Nepoznato-Dev"
    changes: "Initial deep-dive into information theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [information-theory, entropy, kl-divergence, cross-entropy, mutual-information, channel-capacity, compression, machine-learning]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "statistics_and_probability.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Lý thuyết thông tin
Lý thuyết thông tin, do Claude Shannon sáng lập năm 1948, tự lượng hóa thông tin. Một tin nhắn cho bạn biết bao nhiêu? Bạn có thể nén dữ liệu đến mức nào? Bạn có thể giao tiếp nhanh đến mức nào trên một kênh ồn ào? Những câu hỏi này có câu trả lời toán học chính xác. Ngoài giao tiếp, lý thuyết thông tin đã trở thành nền tảng cho học máy - entropy chéo là hàm mất mát mặc định để phân loại, phân kỳ KL đo lường mức độ tương tự về phân phối và lựa chọn tính năng thúc đẩy thông tin lẫn nhau.
---

##Entropy
**Entropy** đo độ không chắc chắn trung bình hoặc mức độ "bất ngờ" của một biến ngẫu nhiên.
### Shannon Entropy (Rời rạc)
Đối với biến ngẫu nhiên rời rạc X có hàm khối lượng xác suất p(x):
H(X) = −Σₓ p(x) log₂ p(x)
Đơn vị: **bits** (khi sử dụng log₂) hoặc **nats** (khi sử dụng ln).
| Phân phối | Entropy | Trực giác |
|-------------|----------|----------|
| Đồng xu công bằng (p = 0,5, 0,5) | 1 chút | Độ không đảm bảo tối đa cho kết quả nhị phân |
| Xu hướng thiên vị (p = 0,9, 0,1) | 0,469 bit | Ít ngạc nhiên hơn — chủ yếu là đứng đầu |
| Tất định (p = 1, 0) | 0 bit | Không có gì chắc chắn cả |
| Khuôn đẹp (6 mặt) | 2,585 bit | Nhiều kết quả hơn = nhiều sự không chắc chắn hơn |
| Thống nhất trên n kết quả | log₂(n) bit | Entropy tối đa cho n kết quả |
### Thuộc tính của Entropy
| Bất động sản | Tuyên bố |
|----------|----------|
| Không tiêu cực | H(X) ≥ 0 |
| Tối đa | H(X) ≤ log₂(\|X\|) có đẳng thức để phân bố đồng đều |
| Quy tắc dây chuyền | H(X, Y) = H(X) + H(Y \| X) |
| Điều hòa giảm | H(X \| Y) ≤ H(X) |
| Độ lõm | H là hàm lõm của phân bố xác suất |
### Entropy vi phân (Liên tục)
Đối với biến ngẫu nhiên liên tục X có mật độ p(x):
h(X) = −∫ p(x) log p(x) dx
Không giống như entropy rời rạc, entropy vi phân có thể **âm**.
| Phân phối | Entropy vi phân |
|-------------|----------------------|
| Đồng phục trên [a,b] | log(b − a) |
| Bình thường N(μ, σ²) | (1/2) log(2πeσ²) |
| Hàm mũ(λ) | 1 − ln(λ) |
---

## Thông tin chung, có điều kiện và lẫn nhau
### Entropy chung
H(X, Y) = −Σₓ Σᵧ p(x, y) log p(x, y)
Đo tổng độ không chắc chắn của cặp (X, Y).
### Entropy có điều kiện
H(Y | X) = −Σₓ Σᵧ p(x, y) log p(y | x) = H(X, Y) − H(X)
Đo lường độ không chắc chắn còn lại về Y sau khi quan sát X.
### Thông tin lẫn nhau
I(X; Y) = Σₓ Σᵧ p(x, y) log [p(x, y) / (p(x)p(y))]
Đo lường mức độ biết X cho bạn biết về Y (và ngược lại).
| Bất động sản | Tuyên bố |
|----------|----------|
| Không tiêu cực | I(X; Y) ≥ 0 |
| Đối xứng | I(X; Y) = I(Y; X) |
| Mối quan hệ với entropy | I(X; Y) = H(X) − H(X \| Y) = H(Y) − H(Y \| X) |
| Mối quan hệ với khớp | I(X; Y) = H(X) + H(Y) − H(X, Y) |
| Độc lập | I(X; Y) = 0 nếu X và Y độc lập |
| Tự thông tin | I(X; X) = H(X) |
### Trực quan: Biểu đồ Entropy
```
┌─────────────────────────────────────────┐
│            H(X, Y)                      │
│  ┌──────────────┐  ┌──────────────┐    │
│  │   H(X|Y)     │  │   H(Y|X)     │    │
│  │              │I │              │    │
│  │              │( │              │    │
│  │   H(X)−I    │X │   H(Y)−I    │    │
│  │              │; │              │    │
│  │              │Y │              │    │
│  └──────────────┘  └──────────────┘    │
│         H(X)              H(Y)          │
└─────────────────────────────────────────┘
```

---

## KL Phân kỳ
**Sự phân kỳ Kullback-Leibler (KL)** đo lường mức độ khác nhau của một phân phối này với một phân phối khác.
D_KL(P || Q) = Σₓ P(x) log [P(x) / Q(x)]
| Bất động sản | Tuyên bố |
|----------|----------|
| Không tiêu cực | D_KL(P \|\| Q) ≥ 0 (Bất đẳng thức Gibbs) |
| Bản sắc | D_KL(P \|\| Q) = 0 nếu P = Q |
| Bất đối xứng | D_KL(P \|\| Q) ≠ D_KL(Q \|\| P) nói chung |
| Không phải là thước đo | Thất bại đối xứng và bất đẳng thức tam giác |
**Giải thích:** D_KL(P || Q) là số bit bổ sung cần thiết để mã hóa dữ liệu từ P bằng cách sử dụng mã được tối ưu hóa cho Q.
### Mối quan hệ với các đại lượng khác
| Mối quan hệ | Công thức |
|-------------|----------|
| Entropy chéo | H(P, Q) = H(P) + D_KL(P \|\| Q) |
| Thông tin lẫn nhau | I(X; Y) = D_KL(P(X,Y) \|\| P(X)P(Y)) |
| KL có điều kiện | D_KL(P(Y\|X) \|\| Q(Y\|X)) tính trung bình trên X |
---

## Entropy chéo
**Entropy chéo** giữa các phân phối P và Q:
H(P, Q) = −Σₓ P(x) log Q(x) = H(P) + D_KL(P || Q)
### Entropy chéo như một hàm mất mát
Trong phân loại, P là phân phối thực (nhãn được mã hóa một nóng) và Q là phân phối dự đoán của mô hình.
**Entropy chéo nhị phân (BCE):**
L = −[y log(ŷ) + (1−y) log(1−ŷ)]
**Entropy chéo phân loại:**
L = −Σᵢ yᵢ log(ŷᵢ)
| Kịch bản | y (đúng) | ŷ (dự đoán) | Mất mát |
|----------|----------|---------------|------|
| Đúng, tự tin | 1 | 0,95 | 0,051 |
| Đúng, không chắc chắn | 1 | 0,55 | 0,598 |
| Sai, tự tin | 1 | 0,05 | 2,996 |
| Sai, không chắc chắn | 1 | 0,45 | 0,799 |
Giảm thiểu entropy chéo tương đương với việc giảm thiểu phân kỳ KL khỏi phân phối thực - đó là lý do tại sao nó hoạt động tốt như một hàm mất mát.
---

## Dung lượng kênh
###Mô hình kênh truyền thông
```
X → [Channel] → Y
```

- X: biến ngẫu nhiên đầu vào
- Y: biến ngẫu nhiên đầu ra
- Kênh: được xác định bởi xác suất có điều kiện p(y|x)
### Định lý mã hóa kênh ồn ào của Shannon
Đối với kênh có công suất C, nếu tốc độ truyền R< C, there exists a coding scheme that achieves arbitrarily small error probability. If R >C thì không thể liên lạc đáng tin cậy.
**Dung lượng kênh:**
C = max_{p(x)} I(X; Y)
### Ví dụ về kênh quan trọng
| Kênh | Mô tả | Công suất |
|----------|-------------|----------|
| **Đối xứng nhị phân (BSC)** | Lật từng bit với xác suất p | 1 − H(p) bit |
| **Xóa nhị phân (BEC)** | Xóa từng bit với xác suất ε | 1 − ε bit |
| **Gaussian (AWGN)** | Y = X + Z, Z ~ N(0, σ²) | (1/2)log(1 + SNR) bit |
| **Nhị phân không ồn ào** | Truyền tải hoàn hảo | 1 chút |
---

## Mã hóa và nén nguồn
### Định lý mã hóa nguồn
Số bit trung bình cần thiết để mã hóa một nguồn được giới hạn dưới mức entropy của nó:
L ≥ H(X)
Mã tối ưu đạt được L ≈ H(X).
### Mã hóa Huffman
Mã **không có tiền tố** gán mã ngắn hơn cho nhiều ký hiệu có khả năng xảy ra hơn.
| Biểu tượng | Xác suất | Mã Huffman | Chiều dài |
|--------|-------------|-------------|--------|
| A | 0,5 | 0 | 1 |
| B | 0,25 | 10 | 2 |
| C | 0,125 | 110 | 3 |
| D | 0,125 | 111 | 3 |
Độ dài trung bình: 0,5(1) + 0,25(2) + 0,125(3) + 0,125(3) = 1,75 bit/ký hiệu
Entropy: H = 1,75 bit/ký hiệu (tối ưu trong trường hợp này!)
### Nén không tổn hao và nén có tổn hao
| Loại | Nguyên tắc | Ví dụ | Giới hạn |
|------|-------------|----------|-------|
| **Không mất mát** | Loại bỏ dư thừa thống kê | ZIP, PNG, FLAC | Tốc độ Entropy H(X) |
| **Mất mát** | Xóa thông tin được cho là không liên quan | JPEG, MP3, H.264 | Hàm biến dạng tỷ lệ R(D) |
**Lý thuyết biến dạng tốc độ:** Đối với nén tổn hao với độ méo tối đa D, tốc độ tối thiểu là R(D) = min I(X; X̂) tuân theo E[d(X, X̂)] ≤ D.
---

## Kết nối với các trường khác
### Lý thuyết thông tin và Nhiệt động lực học
| Khái niệm | Lý thuyết thông tin | Nhiệt động lực học |
|----------|-------------------|----------------|
| Entropy | Entropy của Shannon H(X) | Entropy Boltzmann S = k_B ln W |
| Entropy tối đa | Phân phối thống nhất | Cân bằng nhiệt |
| KL phân kỳ | Sự khác biệt về phân phối | Chênh lệch năng lượng miễn phí |
| Thông tin lẫn nhau | Thông tin được chia sẻ | Mối tương quan trong hệ thống vật lý |
Các dạng toán học giống hệt nhau - Shannon cố tình mượn thuật ngữ "entropy" từ cơ học thống kê.
### Lý thuyết thông tin và thống kê
| Khái niệm | Ứng dụng |
|----------|-------------|
| Khả năng tối đa | Tương đương với việc giảm thiểu sự phân kỳ KL từ phân phối thực nghiệm sang phân phối mô hình |
| Thông tin ngư dân | Độ cong phân kỳ KL; giới hạn dưới của phương sai ước tính (Cramér-Rao) |
| Độ dài mô tả tối thiểu (MDL) | Lựa chọn mô hình bằng cách giảm thiểu tổng chiều dài mã hóa |
| AIC / BIC | Tiêu chí lựa chọn mô hình dựa trên KL gần đúng |
---

## Mức độ liên quan đến Học máy và Khoa học dữ liệu
| Khái niệm CNTT | Ứng dụng ML |
|----------|----------------|
| Mất entropy chéo | Mất phân loại mặc định (nhị phân và đa lớp) |
| KL phân kỳ | Mất VAE (thuật ngữ chính quy), khớp phân phối, chưng cất |
| Thông tin lẫn nhau | Lựa chọn tính năng (MIFS), học biểu diễn (InfoMax), giải mã |
| Entropy | Tiêu chí phân tách cây quyết định (thu được thông tin), thăm dò trong RL (RL entropy tối đa) |
| Dung lượng kênh | Sự phức tạp trong giao tiếp, hiểu giới hạn khái quát hóa |
| Mã hóa nguồn | Nén dữ liệu để lưu trữ và truyền tải, mã hóa hiệu quả |
| Entropy tối đa | Bộ phân loại MaxEnt, lựa chọn trước trong suy luận Bayes |
| Tỷ lệ biến dạng | Hiểu sự cân bằng trong nén tổn thất, lượng tử hóa trong mạng nơ-ron |
| Thông tin ngư dân | Giảm độ dốc tự nhiên, hiểu độ nhạy của tham số |
| MDL / AIC / BIC | Lựa chọn mô hình, ngăn chặn việc trang bị quá mức |
---

## Bản tóm tắt
| Số lượng | Công thức (rời rạc) | Ý nghĩa |
|----------|-------------------|----------|
| Entropy H(X) | −Σ p(x) log p(x) | Độ không đảm bảo trung bình |
| Entropy chung H(X,Y) | −Σ p(x,y) log p(x,y) | Tổng độ không chắc chắn của cặp |
| Entropy có điều kiện H(Y\|X) | H(X,Y) − H(X) | Sự không chắc chắn còn lại về Y cho X |
| Thông tin lẫn nhau I(X;Y) | H(X) − H(X\|Y) | Thông tin được chia sẻ giữa X và Y |
| Phân kỳ KL D_KL(P\|\|Q) | Σ P(x) log(P(x)/Q(x)) | “Khoảng cách” giữa các lần phân phối |
| Entropy chéo H(P,Q) | −Σ P(x) log Q(x) | Chi phí mã hóa sử dụng phân phối sai |
| Dung lượng kênh C | tối đa I(X;Y) | Tốc độ truyền thông đáng tin cậy tối đa |
Lý thuyết thông tin đưa ra những giới hạn cơ bản về những gì có thể học được, nén lại và truyền đạt. Đối với những người thực hành học máy, nó giải thích tại sao entropy chéo hoạt động như một hàm mất mát, cách đo lường chất lượng của các biểu diễn đã học và cách suy nghĩ về sự cân bằng giữa độ phức tạp của mô hình và mức độ phù hợp của dữ liệu. Những hiểu biết sâu sắc của Shannon từ năm 1948 vẫn có liên quan đến AI hiện đại cũng như liên quan đến viễn thông.