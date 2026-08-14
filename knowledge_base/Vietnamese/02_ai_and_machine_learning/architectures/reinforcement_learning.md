<!--
---
# Metadata
title: "Reinforcement Learning"
description: "MDPs, Q-learning, policy gradients, RLHF, multi-agent systems"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to architectures/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [reinforcement, learning, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Học tăng cường
Học tăng cường (RL) là cách máy học cách đưa ra các chuỗi quyết định bằng cách thử và sai. Không giống như học có giám sát, trong đó câu trả lời đúng được cung cấp cho mọi ví dụ, RL chỉ cung cấp cho tác nhân một tín hiệu khen thưởng — và tác nhân phải tìm ra hành động nào dẫn đến kết quả tốt nhất theo thời gian. Đó là cách tiếp cận đằng sau AlphaGo, điều khiển bằng robot, AI chơi trò chơi và – quan trọng – RLHF, kỹ thuật được sử dụng để điều chỉnh các mô hình ngôn ngữ lớn hiện đại phù hợp với sở thích của con người.
---

## Khái niệm cốt lõi
RL đóng khung việc ra quyết định như một vòng lặp giữa **tác nhân** và **môi trường**.
| Thành phần | Vai trò | Ví dụ |
|----------|------|----------|
| **Đại lý** | Người ra quyết định | Chương trình cờ vua, robot, mô hình ngôn ngữ |
| **Môi trường** | Thế giới mà tác nhân tương tác với | Bàn cờ, nhà kho, cuộc trò chuyện |
| **Tiểu bang** | Tình hình hiện tại | Vị trí bảng, bài đọc cảm biến robot, lịch sử trò chuyện |
| **Hành động** | Đại lý có thể làm gì | Di chuyển một quân, rẽ trái, tạo mã thông báo |
| **Phần thưởng** | Tín hiệu phản hồi (số vô hướng) | +1 cho chiến thắng, -1 cho va chạm, điểm ưa thích của con người |
| **Chính sách** | Chiến lược ánh xạ trạng thái thành hành động | "Nếu vua bị đe dọa, hãy di chuyển" |
| **Hàm giá trị** | Phần thưởng tích lũy dự kiến ​​từ một bang | "Vị trí bảng này có giá trị khoảng +3 điểm" |
### Vòng lặp RL
```
Agent observes State → chooses Action → Environment returns new State + Reward
        ↑                                                                         |
        └─────────────────────────────────────────────────────────────────────────┘
```

Mục tiêu của đại lý là tối đa hóa **phần thưởng tích lũy** theo thời gian, không chỉ phần thưởng ngay lập tức. Đây là điều làm cho RL khác biệt cơ bản với học tập có giám sát.
---

## Những điểm khác biệt chính so với các Mô hình học tập khác
| Khía cạnh | Học tập có giám sát | Học tập không giám sát | Học tăng cường |
|--------|-------------------|----------------------|----------------------|
| **Tín hiệu** | Nhãn chính xác cho mọi ví dụ | Không có nhãn; tìm cấu trúc | Phần thưởng vô hướng, thường bị trì hoãn |
| **Phản hồi** | Ngay lập tức | Không có | Trì hoãn và thưa thớt |
| **Trình tự** | Mỗi ví dụ là độc lập | Mỗi ví dụ là độc lập | Hành động ảnh hưởng đến trạng thái trong tương lai |
| **Mục tiêu** | Giảm thiểu lỗi dự đoán | Khám phá các mẫu | Tối đa hóa phần thưởng tích lũy |
---

## Quy trình Quyết định Markov (MDP)
MDP là khung toán học cho RL. Họ cho rằng tương lai chỉ phụ thuộc vào trạng thái hiện tại chứ không phụ thuộc vào lịch sử bạn đến đó bằng cách nào (**thuộc tính Markov**).
| Thành phần | Ký hiệu | Ý nghĩa |
|----------|----------|----------|
| **Tiểu bang** | S | Tất cả các tình huống có thể xảy ra mà tác nhân có thể gặp phải |
| **Hành động** | A | Tất cả những điều đại lý có thể làm |
| **Chức năng chuyển tiếp** | P(s' \| s, a) | Xác suất đạt trạng thái s' sau khi thực hiện hành động a ở trạng thái s |
| **Chức năng thưởng** | R(s, a, s') | Phần thưởng nhận được khi chuyển đổi |
| **Hệ số chiết khấu** | γ (gamma) | Đánh giá phần thưởng trong tương lai bao nhiêu so với phần thưởng trước mắt (0 đến 1) |
**Trả lại** (tổng phần thưởng được chiết khấu) là:
```
G = R₁ + γR₂ + γ²R₃ + ...
```

Hệ số chiết khấu cao (γ gần bằng 1) nghĩa là đại lý có tầm nhìn xa. Một cái thấp có nghĩa là nó thiển cận.
---

## Thuật toán RL cổ điển
### Phương pháp dựa trên giá trị
Những điều này tìm hiểu mức độ tốt của từng trạng thái (hoặc cặp trạng thái-hành động).
| Thuật toán | Ý tưởng chính | Hạn chế |
|----------|----------|-------------|
| **Q-Học** | Tìm hiểu bảng giá trị Q: Q(trạng thái, hành động) = phần thưởng mong đợi | Không mở rộng sang không gian trạng thái lớn |
| **Mạng Q sâu (DQN)** | Sử dụng mạng thần kinh để ước tính giá trị Q | Chỉ xử lý các hành động rời rạc; có thể không ổn định |
| **DQN kép** | Khắc phục sai lệch đánh giá quá cao của Q-learning | Vẫn bị giới hạn ở các hành động rời rạc |
Quy tắc cập nhật Q-learning:
```
Q(s, a) ← Q(s, a) + α [r + γ max Q(s', a') - Q(s, a)]
```

### Phương pháp dựa trên chính sách
Những điều này trực tiếp tìm hiểu chính sách (chiến lược) mà không ước tính giá trị.
| Thuật toán | Ý tưởng chính | Lợi thế |
|----------|----------|----------|
| **CỦNG CỐ** | Độ dốc chính sách của Monte Carlo; cập nhật chính sách theo hướng mang lại kết quả tốt | Đơn giản; hoạt động với các hành động liên tục |
| **PPO** (Tối ưu hóa chính sách gần nhất) | Cắt bớt các cập nhật chính sách để ngăn chặn những thay đổi lớn, gây mất ổn định | Ổn định; được sử dụng rộng rãi; mặc định tốt |
| **TRPO** | Phương pháp vùng tin cậy để cập nhật chính sách | Nguyên tắc hơn PPO; khó thực hiện hơn |
### Phương pháp diễn viên-phê bình
Kết hợp ưu điểm tốt nhất của cả hai: **actor** (chính sách) và **critic** (hàm giá trị).
| Thuật toán | Ý tưởng chính |
|----------||----------|
| **A2C / A3C** | Ưu điểm Diễn viên-Nhà phê bình; sử dụng ước tính lợi thế để giảm phương sai |
| **SAC** (Nhà phê bình-diễn viên mềm) | Tối đa hóa phần thưởng trong khi duy trì hoạt động khám phá (chính quy hóa entropy) |
| **TD3** (DDPG bị trễ đôi) | Giải quyết vấn đề đánh giá quá cao trong không gian hành động liên tục |
---

## RLHF: Học tập tăng cường từ phản hồi của con người
RLHF là kỹ thuật giúp ChatGPT trở nên khả thi. Nó thu hẹp khoảng cách giữa một mô hình có thể dự đoán văn bản và một mô hình tạo ra kết quả mà con người thực sự thấy hữu ích.
### Ba Bước
| Bước | Điều gì xảy ra | Đầu ra |
|------|-------------|--------|
| **1. Tinh chỉnh có giám sát (SFT)** | Tinh chỉnh mô hình được đào tạo trước trên các ví dụ do con người viết chất lượng cao | Một mô hình làm theo hướng dẫn khá tốt |
| **2. Đào tạo mô hình phần thưởng** | Con người so sánh các cặp kết quả đầu ra của mô hình; đào tạo một mô hình để dự đoán sở thích của con người | Mô hình khen thưởng chấm điểm chất lượng đầu ra |
| **3. Tối ưu hóa RL** | Sử dụng PPO để tinh chỉnh mô hình SFT nhằm tối đa hóa điểm số của mô hình khen thưởng | Một mô hình phù hợp với sở thích của con người |
### Tại sao RLHF lại quan trọng
Không có RLHF, một mô hình ngôn ngữ giống như một học sinh đã đọc mọi cuốn sách nhưng không biết cách cư xử trong một cuộc trò chuyện. Nó có thể tạo ra văn bản, nhưng văn bản đó có thể không hữu ích, độc hại hoặc hoàn toàn không hiểu ý chính. RLHF dạy mô hình *những gì con người muốn* — không chỉ văn bản trông như thế nào.
### Các biến thể và lựa chọn thay thế
| Phương pháp | Mô tả | Lợi thế |
|--------|-------------|----------|
| **DPO** (Tối ưu hóa tùy chọn trực tiếp) | Bỏ qua mô hình khen thưởng; trực tiếp tối ưu hóa chính sách từ sở thích của con người | Đơn giản hơn; không có mô hình khen thưởng riêng để đào tạo |
| **RLAIF** | Sử dụng AI (chứ không phải con người) để tạo nhãn ưu tiên | Rẻ hơn ghi nhãn của con người |
| **AI hiến pháp** | Sử dụng một bộ nguyên tắc để hướng dẫn hành vi của người mẫu mà không cần nhãn hiệu của con người | Có khả năng mở rộng hơn; Cách tiếp cận của nhân loại |
| **GRPO** (Tối ưu hóa chính sách tương đối của nhóm) | So sánh kết quả đầu ra trong một nhóm thay vì so với một mô hình riêng biệt | Được sử dụng trong DeepSeek-R1; giảm nhu cầu về mạng lưới giá trị |
---

## Thăm dò và Khai thác
Đây là sự căng thẳng trung tâm trong RL. **Khai thác** có nghĩa là chọn những hành động mà bạn biết là có hiệu quả. **Khám phá** có nghĩa là thử những điều mới để khám phá các chiến lược có khả năng tốt hơn.
| Chiến lược | Nó hoạt động như thế nào | Đánh đổi |
|----------|-------------|----------|
| **ε-tham lam** | Chọn hành động tốt nhất trong hầu hết thời gian; hành động ngẫu nhiên với xác suất ε | Đơn giản nhưng không hiệu quả |
| **Khám phá Boltzmann** | Chọn hành động theo xác suất dựa trên giá trị ước tính của chúng | Mượt mà hơn ε-tham lam |
| **UCB** (Giới hạn độ tin cậy trên) | Thích những hành động có độ không chắc chắn cao (lạc quan khi đối mặt với sự không chắc chắn) | Đảm bảo lý thuyết tốt |
| **Chính quy hóa Entropy** | Thêm phần thưởng khi truy cập các trạng thái khác nhau (được sử dụng trong SAC, PPO) | Khuyến khích khám phá tự nhiên |
---

## Học tăng cường đa tác nhân
Khi nhiều tác nhân học đồng thời, động lực trở nên phức tạp hơn nhiều.
| Kịch bản | Thử thách | Ví dụ |
|----------|-------------|----------|
| **Hợp tác xã** | Đại lý phải phối hợp; phân công tín chỉ khó | Đội bóng robot; mạng cảm biến phân tán |
| **Cạnh tranh** | Đối thủ thích nghi; môi trường không cố định | Trò chơi AI (poker, StarCraft); an ninh mạng |
| **Hỗn hợp** | Một số đại lý hợp tác, số khác cạnh tranh | Thị trường đấu giá; hệ thống giao thông |
| Thuật toán | Mô tả |
|----------||-------------|
| **MADDPG** | Phiên bản đa tác nhân của DDPG; nhà phê bình tập trung, các tác nhân phi tập trung |
| **MAPPO** | PPO đa tác nhân; được sử dụng rộng rãi trong thực tế |
| **Tự chơi** | Các đặc vụ huấn luyện chống lại các bản sao của chính họ (AlphaGo, AlphaStar) |
---

## Chuyển từ Sim sang Real
Việc huấn luyện robot trong thế giới thực rất chậm và nguy hiểm. Thay vào đó, các đặc vụ được đào tạo trong mô phỏng và chuyển sang thực tế.
| Thử thách | Giải pháp |
|----------||----------|
| **Khoảng cách thực tế** (mô phỏng ≠ thế giới thực) | Ngẫu nhiên hóa miền: thay đổi các thông số vật lý trong quá trình đào tạo |
| **Mẫu không hiệu quả** | Sử dụng RL dựa trên mô hình hoặc huấn luyện trên các mô phỏng song song lớn |
| **An toàn** | RL bị ràng buộc: xử phạt các hành động không an toàn trong quá trình đào tạo |
| **Khả năng quan sát một phần** | Đào tạo với cảm biến ồn ào và quan sát bị trì hoãn |
Các công ty như Boston Dynamics và Tesla sử dụng mô phỏng một cách rộng rãi, nhưng khoảng cách giữa hiệu suất mô phỏng và hiệu suất vật lý vẫn là một trong những thách thức lớn nhất của lĩnh vực này.
---

## Công cụ và Khung
| Công cụ | Mục đích | Tốt nhất cho |
|------|----------|----------|
| **Đường cơ sở ổn định3** | Triển khai Python sạch PPO, SAC, TD3, DQN | Học tập và tạo mẫu |
| **RLlib** | Thư viện RL có thể mở rộng được xây dựng trên Ray | Đào tạo phân tán quy mô lớn |
| **CleanRL** | Triển khai một tệp cho nghiên cứu | Tìm hiểu sâu về thuật toán |
| **Phòng tập thể dục (OpenAI)** | Giao diện môi trường được chuẩn hóa | Xác định vấn đề RL |
| **Phòng tập thể dục Isaac / Phòng thí nghiệm Isaac** | Mô phỏng vật lý được tăng tốc GPU | Robotics, mô phỏng như thật |
| **TRL** (Thư viện RL máy biến áp) | RLHF, DPO, PPO cho các mô hình ngôn ngữ | Căn chỉnh LLM |
| **OpenRLHF** | Khung RLHF phân tán | Đào tạo mô hình lớn với RLHF |
---

## Lời khuyên thiết thực
- **Bắt đầu với PPO.** Đây là thuật toán có mục đích chung đáng tin cậy nhất. Nếu bạn không chắc chắn nên sử dụng cái gì thì PPO là mặc định.
- **Bình thường hóa phần thưởng của bạn.** Việc chia tỷ lệ phần thưởng ảnh hưởng đáng kể đến sự ổn định trong quá trình luyện tập.
- **Sử dụng môi trường được vector hóa.** Chạy song song nhiều môi trường (ví dụ: 8–64) giúp ổn định ước tính độ dốc và tăng tốc đáng kể quá trình đào tạo.
- **Giám sát cả phần thưởng và entropy.** Nếu entropy giảm xuống 0, tác nhân của bạn đã ngừng khám phá và có thể bị kẹt ở mức tối ưu cục bộ.
- **Định hình phần thưởng là một nghệ thuật.** Thiết kế chức năng phần thưởng phù hợp thường là phần khó nhất. Phần thưởng thưa thớt (chỉ ở cuối) khiến việc học trở nên cực kỳ chậm. Phần thưởng dày đặc, có hình thức phù hợp hướng dẫn tác nhân nhưng có thể gây ra hành vi ngoài ý muốn.
- **RLHF rất mong manh.** Những thay đổi nhỏ đối với mô hình phần thưởng hoặc siêu tham số PPO có thể gây ra sự sụt giảm lớn về chất lượng. DPO là giải pháp thay thế ổn định hơn nếu bạn không cần đường dẫn RLHF đầy đủ.
---

## Bản tóm tắt
Học tăng cường là nghiên cứu về cách các tác nhân học cách đưa ra quyết định thông qua tương tác. Nó bao gồm từ các thuật toán cổ điển như Q-learning đến các phương pháp RL sâu hiện đại như PPO và SAC, đồng thời củng cố một số tiến bộ quan trọng nhất gần đây trong AI — từ chơi trò chơi đến căn chỉnh mô hình ngôn ngữ. Thử thách cốt lõi vẫn như cũ: làm cách nào để bạn học được hành vi tối ưu khi phản hồi bị trì hoãn, thưa thớt và ồn ào? Câu trả lời - thử và sai, được hướng dẫn bởi toán học thông minh - hóa ra lại là một trong những ý tưởng mạnh mẽ nhất trong trí tuệ nhân tạo.