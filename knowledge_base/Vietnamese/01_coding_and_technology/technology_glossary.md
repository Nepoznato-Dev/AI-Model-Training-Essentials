<!--
---
# Metadata
title: "Technology Glossary"
description: "Technical terminology (AI models, hardware, benchmarks)"
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
tags: [technology, glossary, coding-and-technology]
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
# Thuật ngữ công nghệ
Bảng thuật ngữ tham khảo bao gồm các mô hình AI, phần cứng, điểm chuẩn và khái niệm cốt lõi
trong bối cảnh điện toán và AI hiện đại.
---

## Mô hình và trợ lý ngôn ngữ AI
###Trò chuyệnGPT
ChatGPT là chatbot AI được phát triển bởi OpenAI, phát hành lần đầu vào tháng 11 năm 2022.
Nó được hỗ trợ bởi loạt mô hình ngôn ngữ lớn (LLM) GPT. ChatGPT là một
trong số các sản phẩm AI tiêu dùng phát triển nhanh nhất trong lịch sử, đạt 100 triệu
người dùng trong vòng hai tháng kể từ khi ra mắt. Nó hỗ trợ hội thoại dựa trên văn bản, mã
tạo, tóm tắt và viết sáng tạo. Các cấp độ trả phí cung cấp quyền truy cập vào
các mẫu mạnh hơn như GPT-4 và GPT-4o.
### GPT (Generative Pre-training Transformer)
GPT là một nhóm các mô hình ngôn ngữ lớn được tạo bởi OpenAI. Kiến trúc
sử dụng Transformer chỉ giải mã được đào tạo với mục tiêu dự đoán mã thông báo tiếp theo trên
kho văn bản đồ sộ. Các phiên bản chính bao gồm GPT-2 (2019, thông số 1.5B, đáng chú ý
vì công khai "quá nguy hiểm để phát hành"), GPT-3 (2020, thông số 175B, rộng rãi
được sử dụng thông qua API), GPT-3.5 (xương sống của ChatGPT ban đầu) và GPT-4
(2023, đa phương thức, hiệu suất gần bằng trình độ chuyên gia của con người trên nhiều điểm chuẩn).
### Claude
Claude là trợ lý AI được phát triển bởi Anthropic. Nó được đặt theo tên của Claude
Shannon, người sáng lập lý thuyết thông tin. Anthropic được thành lập bởi cựu
Các nhà nghiên cứu của OpenAI và tập trung vào "AI hiến pháp" - một kỹ thuật để tạo ra
mô hình an toàn hơn bằng cách đào tạo họ tuân theo một bộ nguyên tắc. người mẫu Claude
(Claude 1, 2, 3 Haiku / Sonnet / Opus) được biết đến với các cửa sổ ngữ cảnh dài (lên
đến 200.000 token), lý luận sắc thái và giảm sản lượng có hại so với
LLM cơ bản.
### Song Tử
Gemini là nhóm mô hình AI đa phương thức của Google DeepMind, được công bố vào năm
Tháng 12 năm 2023. Song Tử vốn là người đa phương thức - được đào tạo từ đầu
văn bản, hình ảnh, âm thanh và video cùng một lúc, không giống như các mẫu trước đó có
các phương thức được thêm vào thông qua tinh chỉnh. Các phiên bản bao gồm Gemini Nano (trên thiết bị),
Gemini Flash (nhanh, tiết kiệm chi phí) và Gemini Ultra (dung lượng cao nhất).
Gemini hỗ trợ chatbot AI của Google Bard (đã đổi tên thành Gemini) và AI Tìm kiếm của Google
Tổng quan.
###Phi-3-mini
Phi-3-mini là mô hình ngôn ngữ nhỏ (SLM) được Microsoft phát triển với 3.8B
các thông số. Nó được phát hành vào tháng 4 năm 2024. Không giống như hầu hết các mẫu lớn, Phi-3-mini
đã được đào tạo về bộ dữ liệu "chất lượng sách giáo khoa" được quản lý cẩn thận - một kỹ thuật
được tiên phong bởi Microsoft Research — ưu tiên chất lượng dữ liệu hơn khối lượng thô.
Mặc dù nhỏ hơn nhiều so với GPT-4 hay Claude 3 Opus, nhưng các trận đấu Phi-3-mini hay
vượt trội hơn các mô hình lớn hơn nhiều lần về các tiêu chuẩn lý luận như MMLU và
HumanEval. Nó hỗ trợ cửa sổ ngữ cảnh mã thông báo 4k trong biến thể cơ sở của nó và 128k
window trong biến thể ngữ cảnh dài. Phi-3-mini có thể chạy trên một GPU tiêu dùng
hoặc thậm chí trên thiết bị trên điện thoại thông minh hiện đại có đủ RAM.
### Llama (Meta AI)
Llama (Mô hình ngôn ngữ lớn Meta AI) là một nhóm mô hình có trọng lượng mở
được phát hành bởi Meta. Llama 2 (2023) được phát hành để nghiên cứu và sử dụng thương mại
với kích thước khác nhau, từ các thông số 7B đến 70B. Llama 3 (2024) cải tiến
hiệu suất đáng kể, với các model từ 8B đến 70B (và sau này là 400B+).
Vì trọng lượng có thể tải xuống công khai nên mô hình Llama là nền tảng
cho một hệ sinh thái rộng lớn gồm các biến thể được tinh chỉnh (Mistral, Alpaca, Vicuna, v.v.)
và được sử dụng rộng rãi để triển khai AI cục bộ/riêng tư.
###Mistral
Mistral AI là một công ty AI của Pháp chuyên phát triển LLM mở và độc quyền.
Mistral 7B (2023) đã chứng minh rằng mô hình tham số 7B có thể phù hợp với
hiệu suất của các mô hình lớn hơn nhiều bằng cách sử dụng các kỹ thuật hiệu quả như trượt
sự chú ý của cửa sổ và sự chú ý truy vấn được nhóm. Mixtral 8x7B (2023) là hỗn hợp-
mô hình chuyên gia - nó định tuyến từng mã thông báo đến một tập hợp con gồm 8 mạng chuyên gia,
đạt được hiệu suất ở mức GPT-3.5 trong khi rẻ hơn về mặt tính toán.
Các mẫu xe của Mistral hoàn toàn có trọng lượng mở và có thể chạy cục bộ.
---

## Phần cứng GPU và Card đồ họa
### GPU (Bộ xử lý đồ họa)
GPU là bộ xử lý được thiết kế để tính toán song song ồ ạt. Ban đầu
được xây dựng để hiển thị đồ họa 3D, GPU đã trở nên cần thiết cho việc đào tạo AI/ML
và suy luận vì chúng có thể thực hiện hàng ngàn phép tính dấu phẩy động
đồng thời sử dụng hàng ngàn lõi nhỏ. Hai nhà sản xuất GPU chính
cho AI là NVIDIA và AMD.
### Dòng NVIDIA GeForce RTX
Dòng RTX (Ray Tracing Texel eXtreme) là dòng GPU tiêu dùng của NVIDIA. RTX
Thế hệ 30xx (Ampere, 2020) và RTX 40xx (Ada Lovelace, 2022) bao gồm
Lõi Tensor chuyên dụng để tăng tốc hoạt động AI. VRAM (RAM video) là
rất quan trọng để chạy cục bộ các mô hình AI - GPU 8GB có thể xử lý tham số 7B
mô hình lượng tử hóa 4 bit; GPU 24 GB có thể xử lý các mô hình 70B ở 4 bit.
### NVIDIA A-Series và H-Series (Trung tâm dữ liệu)
A100 (Ampere, 2020) và H100 (Hopper, 2022) là AI chuyên nghiệp của NVIDIA
máy gia tốc. H100 có bộ nhớ HBM3 lên tới 80GB và là tiêu chuẩn
phần cứng đằng sau hầu hết các chương trình đào tạo LLM quy mô lớn hiện nay. Những GPU này có giá 25.000 USD–
40.000 USD mỗi thẻ nhưng cung cấp thông lượng AI gấp 10–30× so với thẻ RTX dành cho người tiêu dùng.
### Dòng AMD Radeon RX
Dòng GPU tiêu dùng của AMD. RX 7900 XTX (2022) có 24GB VRAM, chạy được
LLM cục bộ thông qua ROCm (ngăn xếp tính toán GPU của AMD). GPU AMD nhìn chung ít hơn
được hỗ trợ tốt hơn NVIDIA cho các khung AI, mặc dù khả năng hỗ trợ đang được cải thiện.
### Intel Arc
Intel Arc là dòng sản phẩm GPU rời của Intel, ra mắt bắt đầu từ năm 2022. Arc
GPU hỗ trợ XeSS (siêu mẫu của Intel) và có sự hỗ trợ hạn chế nhưng ngày càng tăng
cho các tác vụ suy luận AI thông qua khung OpenVINO và IPEX-LLM.
### ARK Intel (ark.intel.com)
ARK là cơ sở dữ liệu thông số kỹ thuật sản phẩm chính thức của Intel tại ark.intel.com. Nó
cung cấp thông số kỹ thuật chi tiết cho mọi CPU, GPU, FPGA và
Sản phẩm NUC, bao gồm số lượng lõi, tốc độ xung nhịp, TDP, loại bộ nhớ được hỗ trợ,
và các tính năng của tập lệnh. Khi bạn nghe thấy "kiểm tra thông số kỹ thuật của ARK", điều đó có nghĩa là
truy cập cơ sở dữ liệu đó để biết thông tin phần cứng có thẩm quyền.
---

## Điểm chuẩn hiệu suất AI
### MMLU (Hiểu ngôn ngữ đa nhiệm lớn)
MMLU là điểm chuẩn kiểm tra kiến thức LLM trên 57 môn học bao gồm
toán học, lịch sử, luật, y học và khoa học máy tính. Nó bao gồm
câu hỏi trắc nghiệm được rút ra từ các kỳ thi thực tế cấp đại học. Điểm số của
70% là trình độ đại học của con người; GPT-4 và Claude 3 đạt điểm trên 86%.
Phi-3-mini đạt khoảng 70% mặc dù kích thước nhỏ.
### Đánh giá con người
HumanEval là điểm chuẩn của OpenAI để tạo mã. Nó bao gồm 164 Python
vấn đề lập trình với các trường hợp kiểm thử tự động. Các mô hình được đo trên
pass@k - xác suất để ít nhất một trong k giải pháp được tạo vượt qua tất cả
các bài kiểm tra. Điểm GPT-4 ~87% (pass@1); một mô hình 7B được điều chỉnh tốt có thể đạt ~ 50–60%.
### Xin chào Swag
HellaSwag là một tiêu chuẩn lý luận thông thường. Người mẫu được đưa ra một câu
mô tả một hoạt động trần tục và phải chọn sự tiếp tục có khả năng nhất từ
bốn lựa chọn. Các lựa chọn sai được thiết kế đặc biệt để hợp lý nhưng
sai một cách tinh tế. Nó kiểm tra xem một mô hình có hiểu biết cơ bản về vật lý hay không
và các tình huống xã hội.
### ARC (Thử thách suy luận AI2)
ARC là điểm chuẩn của Viện AI Allen. Nó bao gồm các trường cấp
câu hỏi khoa học, được chia thành bộ "Dễ" và "Thử thách". Bộ thử thách
chứa các câu hỏi về các phương pháp dựa trên truy xuất và các mô hình thống kê đơn giản
đấu tranh, đòi hỏi phải suy luận nhiều bước.
---

## Các khái niệm AI/ML cốt lõi
### RAG (Thế hệ tăng cường truy xuất)
RAG là một kỹ thuật kết hợp hệ thống truy xuất (thường là vectơ
cơ sở dữ liệu) với một mô hình ngôn ngữ. Thay vì chỉ dựa vào mô hình
kiến thức tham số, trước tiên RAG lấy các tài liệu liên quan từ bên ngoài
cơ sở tri thức và sau đó đưa chúng vào ngữ cảnh của mô hình. Điều này cho phép
mô hình để trả lời các câu hỏi về thông tin cập nhật hoặc thông tin cụ thể theo tên miền
mà không cần đào tạo lại. Potato.ai sử dụng một dạng RAG — nó lấy từ KB của nó
và bao gồm các kết quả trong ngữ cảnh trước khi tạo phản hồi.
### Tinh chỉnh
Tinh chỉnh là quá trình tiếp tục huấn luyện một mô hình đã được huấn luyện trước trên một
tập dữ liệu nhỏ hơn, theo miền cụ thể. Điều này điều chỉnh trọng số của mô hình cho phù hợp
nhiệm vụ hoặc lĩnh vực cụ thể. Ví dụ: LLM cơ sở có thể được tinh chỉnh trên
hồ sơ y tế để tạo ra một trợ lý hỏi đáp y tế. Tinh chỉnh là
tốn kém về mặt tính toán nhưng rẻ hơn nhiều so với việc đào tạo từ đầu.
### Lượng tử hóa
Lượng tử hóa làm giảm độ chính xác về số của trọng số mô hình (ví dụ: từ 32-bit
float thành số nguyên 4 bit). Điều này làm giảm đáng kể dung lượng bộ nhớ — model 7B
ở độ chính xác 16 bit yêu cầu ~ 14GB VRAM; cùng một mô hình ở 4-bit (định dạng GGUF)
yêu cầu ~ 4GB. Lượng tử hóa thường gây ra độ chính xác nhỏ nhưng có thể chấp nhận được
xuống cấp và là kỹ thuật chính cho phép các mô hình lớn chạy trên thiết bị tiêu dùng
phần cứng hoặc thậm chí cả thiết bị di động.
### Cửa sổ ngữ cảnh
Cửa sổ ngữ cảnh là số lượng mã thông báo tối đa mà một mô hình có thể xử lý cùng một lúc,
bao gồm cả lời nhắc và phản hồi được tạo ra. GPT-3.5 có 4.096 mã thông báo
cửa sổ; GPT-4 Turbo và Claude 3 hỗ trợ 128.000 token; Song Tử 1.5 Pro
hỗ trợ 1.000.000 token. Cửa sổ ngữ cảnh lớn hơn cho phép mô hình "nhìn thấy"
giống một cuộc trò chuyện hoặc tài liệu cùng một lúc hơn, cải thiện tính mạch lạc trong thời gian dài
trao đổi.
### RLHF (Học tập tăng cường từ phản hồi của con người)
RLHF là kỹ thuật đào tạo chuyển đổi mô hình ngôn ngữ cơ sở (mà
chỉ cần dự đoán mã thông báo tiếp theo) vào một trợ lý làm theo hướng dẫn và
cư xử hữu ích. Đầu ra của mô hình chấm điểm của người đánh giá là con người, mô hình phần thưởng được đào tạo
theo sở thích của họ và mô hình ngôn ngữ sau đó được tối ưu hóa theo điều này
mô hình khen thưởng bằng cách sử dụng học tập tăng cường. ChatGPT, Claude và Gemini đều sử dụng
các biến thể của RLHF hoặc các kỹ thuật căn chỉnh tương tự (ví dụ: AI Hiến pháp,
Tối ưu hóa tùy chọn trực tiếp).
### Kiến trúc máy biến áp
Transformer là kiến trúc mạng nơ-ron làm nền tảng cho tất cả các LLM hiện đại.
Được giới thiệu trong bài báo năm 2017 "Sự chú ý là tất cả những gì bạn cần" của Vaswani và cộng sự, nó
sử dụng cơ chế tự chú ý để xử lý song song tất cả các mã thông báo thay vì
một cách tuần tự. Máy biến áp chỉ có bộ mã hóa (BERT) được sử dụng để hiểu các nhiệm vụ;
Máy biến áp chỉ có bộ giải mã (GPT, Llama, Mistral) được sử dụng cho các tác vụ tạo;
Máy biến áp mã hóa-giải mã (T5, BART) được sử dụng để dịch và tóm tắt.
### Cơ sở dữ liệu nhúng và vectơ
Phần nhúng là các biểu diễn số dày đặc của văn bản (hoặc hình ảnh) được tạo bởi
một mạng lưới thần kinh. Các văn bản tương tự về mặt ngữ nghĩa có các phần nhúng gần giống nhau
không gian vectơ. Cơ sở dữ liệu vectơ (ChromaDB, Pinecone, Weaviate, Qdrant)
các phần nhúng này và hỗ trợ tìm kiếm lân cận gần nhất nhanh chóng. Họ là
xương sống lưu trữ của hệ thống RAG, bao gồm cả lớp bộ nhớ lạnh của Potato.ai.