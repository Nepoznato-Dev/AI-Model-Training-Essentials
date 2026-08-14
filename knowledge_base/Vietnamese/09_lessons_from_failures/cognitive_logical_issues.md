---
# Metadata
title: "Cognitive Biases and Logical Fallacies"
description: "Reasoning errors and cognitive biases"
category: "Lessons from Failures"
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
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cognitive, logical, issues, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "27 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Những thành kiến ​​về nhận thức và những sai lầm logic
Tài liệu này tổng hợp những thành kiến ​​về nhận thức, những sai lầm logic và những lỗi lý luận ảnh hưởng đến cả việc ra quyết định của con người và kết quả đầu ra của hệ thống AI.
---

## Thành kiến ​​về nhận thức
Những thành kiến ​​​​nhận thức là những mô hình sai lệch có hệ thống khỏi tính hợp lý trong phán đoán và ra quyết định. Trong phát triển phần mềm và hệ thống AI, những điều này có thể dẫn đến các quyết định thiết kế kém, yêu cầu sai sót và hành vi sai lệch của mô hình.
### Xu hướng xác nhận
**Nó là gì:** Xu hướng tìm kiếm, diễn giải và nhớ lại thông tin theo cách xác nhận những niềm tin đã có từ trước.
**Ví dụ tồi trong quá trình phát triển:**```python
# Developer believes their algorithm is O(n log n)
def analyze_complexity(code):
    # Only looks for evidence supporting O(n log n)
    sees_divide_and_conquer = True
    sees_recursion = True
    
    # Ignores contradictory evidence
    nested_loop_present = True  # Actually makes it O(n²)
    redundant_computation = True  # Adds extra factor
    
    return "O(n log n)"  # Wrong conclusion
```

**Trong phần đánh giá mã:**```markdown
Developer A (senior): "This looks good, nice work!"
Developer B (junior): "This has several potential issues..."

Team accepts Developer A's review without scrutiny but questions Developer B's feedback excessively.
```

**Giảm thiểu:**
- Tích cực tìm kiếm bằng chứng phủ nhận
- Sử dụng đánh giá mã mù
- Khuyến khích những ý kiến bất đồng
- Ghi lại các giả định một cách rõ ràng
### Xu hướng neo đậu
**Nó là gì:** Dựa quá nhiều vào thông tin đầu tiên gặp phải.
**Ví dụ tồi:**```markdown
Project Manager: "This feature should take about 2 days."
Developer: (Anchored to 2 days, even though realistic estimate is 5 days)
"Okay, I'll try to finish in 2 days."

Result: Rushed work, technical debt, missed deadlines anyway.
```

**Giảm thiểu:**
- Nhận nhiều ước tính độc lập
- Sử dụng kế hoạch poker để ước tính
- Xem xét phạm vi thay vì ước tính điểm
- Dữ liệu lịch sử tham khảo
### Ngụy biện về chi phí chìm
**Nó là gì:** Tiếp tục nỗ lực vì những nguồn lực đã đầu tư trước đó (thời gian, tiền bạc, công sức), ngay cả khi từ bỏ sẽ tốt hơn.
**Ví dụ tồi:**```markdown
"We've already spent 6 months building this custom framework. 
We can't switch to the industry standard now, even though 
it would save us time in the long run."
```

**Giảm thiểu:**
- Đánh giá các quyết định dựa trên giá trị tương lai, không phải đầu tư trong quá khứ
- Thường xuyên đánh giá lại tính khả thi của dự án
- Tạo tâm lý an toàn khi xoay vòng
- Sử dụng tiêu chí khách quan cho các quyết định tiếp tục/dừng
### Heuristic sẵn có
**Nó là gì:** Đánh giá quá cao tầm quan trọng của thông tin có sẵn hoặc thông tin gần đây.
**Ví dụ tồi:**```markdown
"I just read about a SQL injection attack, so we should 
prioritize SQL injection prevention over XSS, even though 
our security audit shows XSS is our bigger risk."
```

**Giảm thiểu:**
- Sử dụng việc ra quyết định dựa trên dữ liệu
- Tư vấn các mô hình mối đe dọa toàn diện
- Nhìn vào tỷ lệ cơ sở và số liệu thống kê
- Tránh sự thiên vị gần đây trong việc ưu tiên
### Hiệu ứng Dunning-Kruger
**Nó là gì:** Những người có năng lực thấp trong một nhiệm vụ đánh giá quá cao khả năng của họ; các chuyên gia có thể đánh giá thấp họ.
**Ví dụ tồi:**```markdown
Junior Developer: "I've completed a Python tutorial. 
I'm ready to architect our entire microservices platform."

Senior Developer: "I've been building distributed systems for 10 years. 
I'm probably missing something important in this design."
```

**Giảm thiểu:**
- Khuyến khích học tập liên tục
- Thực hiện quy trình đánh giá ngang hàng
- Xây dựng các chương trình tư vấn
- Bồi dưỡng tính khiêm tốn và tính tò mò
---

## Sai lầm logic
Ngụy biện logic là những lỗi trong lý luận làm suy yếu giá trị của lập luận. Các mô hình AI có thể tạo ra kết quả đầu ra có chứa những sai lầm này.
### Ad Hominem (Tấn công con người)
**Nó là gì:** Tấn công người đưa ra lập luận chứ không phải chính lập luận đó.
**Ví dụ tồi:**```markdown
"This code review is wrong because the reviewer is a junior developer."
```

**Tại sao nó tệ:** Giá trị của phản hồi phụ thuộc vào nội dung của nó chứ không phải thâm niên của người đánh giá.
### Khiếu nại lên cơ quan có thẩm quyền
**Nó là gì:** Tuyên bố điều gì đó là đúng vì một nhân vật có thẩm quyền đã nói như vậy mà không có bằng chứng.
**Ví dụ tồi:**```markdown
"This architecture must be correct because Google uses it."
```

**Tại sao nó tệ:** Những gì hiệu quả với Google ở ​​quy mô của họ có thể không hiệu quả với trường hợp sử dụng của bạn.
### Sự phân đôi sai lầm (Tư duy đen trắng)
**Nó là gì:** Chỉ trình bày hai tùy chọn khi có nhiều tùy chọn hơn.
**Ví dụ tồi:**```markdown
"We either rewrite everything in Rust or accept that our 
codebase will always be slow and buggy."
```

**Thực tế:** Có nhiều tùy chọn giữa các thái cực này (tối ưu hóa đường dẫn nóng, sử dụng Rust cho các thành phần cụ thể, cải thiện mã Python, v.v.)
### Dốc Trơn Trượt
**Nó là gì:** Lập luận rằng một sự kiện chắc chắn sẽ dẫn đến một chuỗi hậu quả tiêu cực.
**Ví dụ tồi:**```markdown
"If we allow this small technical debt, soon our entire 
codebase will be unmaintainable and the company will fail."
```

**Tại sao nó tệ:** Giả định sự tiến triển không thể tránh khỏi mà không có bằng chứng; bỏ qua các yếu tố giảm nhẹ.
### Lý luận tuần hoàn
**Nó là gì:** Sử dụng kết luận làm tiền đề.
**Ví dụ tồi:**```markdown
"Our code is high quality because we write good code."
```

### Post Hoc Ergo Propter Hoc (Nguyên nhân sai)
**Nó là gì:** Giả sử rằng vì B đi theo A nên A gây ra B.
**Ví dụ tồi:**```markdown
"We deployed the new feature and then saw increased latency. 
The new feature must be causing the latency."
```

**Thực tế:** Mối tương quan không hàm ý quan hệ nhân quả. Các yếu tố khác có thể chịu trách nhiệm.
### Người Rơm
**Nó là gì:** Trình bày sai lập luận của ai đó để dễ bị tấn công hơn.
**Ví dụ tồi:**```markdown
Developer A: "We should add more tests for edge cases."
Developer B: "So you want us to spend all our time writing tests 
and never ship features?"
```

### Ngụy biện về đoàn xe
**Nó là gì:** Lập luận điều gì đó là đúng vì có nhiều người tin vào điều đó.
**Ví dụ tồi:**```markdown
"Everyone is using Kubernetes, so we should too."
```

**Tại sao nó tệ:** Mức độ phổ biến không đảm bảo tính phù hợp cho nhu cầu cụ thể của bạn.
---

## Lập luận thất bại trong AI
### Lỗi logic nhiều bước
**Ví dụ tồi:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Yes, Alice must be a programmer.
```

**Tại sao nó xấu:**
- Phạm phải sai lầm khẳng định hệ quả
- Alice có thể viết mã mà không cần phải là lập trình viên
- Cấu trúc logic: (P→Q, Q) ⊬ P
**Lý luận đúng:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Not necessarily. While all programmers write code, not everyone
who writes code is a programmer. Alice could be a student, hobbyist, or
work in another field that involves coding.
```

### Lỗi suy luận toán học
**Ví dụ tồi:**```
User: A bat and ball cost $1.10 together. The bat costs $1 more than the ball.
How much does the ball cost?
Assistant: The ball costs $0.10.
```

**Thực tế:** Nếu quả bóng có giá 0,10 USD và cây gậy có giá thêm 1 USD (1,10 USD) thì tổng số tiền sẽ là 1,20 USD. Câu trả lời đúng là 0,05 USD cho quả bóng và 1,05 USD cho cây gậy.
### Lỗi suy luận nhân quả
**Ví dụ tồi:**```
User: Ice cream sales and drowning rates both increase in summer. Does ice cream cause drowning?
Assistant: Yes, there appears to be a causal relationship.
```

**Thực tế:** Cả hai đều do yếu tố thứ ba (thời tiết nắng nóng) gây ra chứ không phải do nhau.
---

## Chiến lược cải tiến
### Dành cho việc ra quyết định của con người
1. **Đào tạo nhận thức**: Học cách nhận biết những thành kiến phổ biến
2. **Cách sử dụng danh sách kiểm tra**: Sử dụng danh sách kiểm tra quyết định để chống lại những thành kiến
3. **Nhóm đa dạng**: Bao gồm những người có quan điểm khác nhau
4. **Pre-mortems**: Tưởng tượng thất bại và làm ngược lại để xác định nguyên nhân
5. **Tài liệu**: Ghi lại lý do để xem xét sau
### Dành cho hệ thống AI
1. **Gợi ý chuỗi suy nghĩ**: Yêu cầu người mẫu trình bày các bước suy luận
2. **Tự sửa**: Yêu cầu mô hình xem xét và phê bình các câu trả lời của mô hình
3. **Xác minh chính thức**: Sử dụng các công cụ suy luận mang tính biểu tượng cho logic phản biện
4. **Phân tách**: Chia các vấn đề phức tạp thành các bước nhỏ hơn
5. **Công cụ bên ngoài**: Sử dụng máy tính và bộ giải cho các bài toán
6. **Nhiều mẫu**: Tạo nhiều phản hồi và so sánh
---

## Chủ đề liên quan
- **Thất bại AI/LLM**: Xem`ai_llm_failures.md`để biết các vấn đề về ảo giác và lý luận
- **Các nguồn mâu thuẫn**: Xem tài liệu về đánh giá thông tin xung đột
- **Tư duy phản biện**: Áp dụng các khái niệm này để đánh giá các lập luận và bằng chứng
- **Kỹ thuật nhanh chóng**: Xem`../02_artificial_intelligence/prompt_engineering.md`để biết các kỹ thuật giúp giảm lỗi lập luận
---

## Những thành kiến ​​nhận thức bổ sung trong phát triển phần mềm
### Xu hướng hiện trạng
**Nó là gì:** Ưu tiên duy trì trạng thái hiện tại; bất kỳ thay đổi nào được coi là mất mát.
**Ví dụ tồi:**```markdown
Team Lead: "Should we upgrade to Python 3.12? It has performance improvements 
and security fixes."

Developer: "Python 3.8 works fine. Why risk breaking things?"

Reality: Staying on an older version increases technical debt, security risks,
and makes future upgrades harder.
```

**Giảm thiểu:**
- Lượng hóa chi phí không thay đổi
- Đặt lịch nâng cấp thường xuyên
- Tạo môi trường thử nghiệm an toàn
- Xem những thay đổi là cơ hội chứ không phải mối đe dọa
### Xu hướng lạc quan
**Nó là gì:** Đánh giá thấp thời gian, chi phí và rủi ro trong khi đánh giá quá cao lợi ích.
**Ví dụ tồi:**```markdown
Project Plan:
- Development: 2 weeks (realistic: 4 weeks)
- Testing: 3 days (realistic: 1 week)
- Bug fixes: 2 days (realistic: 1-2 weeks)
- Contingency: None

Result: Project takes 3x longer than planned.
```

**Giảm thiểu:**
- Sử dụng dự báo lớp tham chiếu (so sánh với các dự án tương tự trước đây)
- Thêm bộ đệm dự phòng (20-50%)
- Tiến hành khám nghiệm tử thi
- Theo dõi độ chính xác ước tính theo thời gian
### Thiên kiến ​​sống sót
**Nó là gì:** Tập trung vào những ví dụ thành công trong khi bỏ qua những thất bại.
**Ví dụ tồi:**```markdown
"Look at all these successful startups that didn't do market research!
We don't need market research either."

Reality: Many more startups failed without market research, but they're 
not visible because they didn't survive.
```

**Giảm thiểu:**
- Nghiên cứu cả thành công VÀ thất bại
- Tìm kiếm tỷ lệ cơ sở và số liệu thống kê
- Xem xét dữ liệu vô hình
- Tránh các ví dụ hái anh đào
### Lỗi phân bổ cơ bản
**Nó là gì:** Quy kết hành vi của người khác là do tính cách hơn là do hoàn cảnh.
**Ví dụ tồi:**```markdown
"That developer made a bug because they're careless."

Reality: The bug might be due to unclear requirements, time pressure,
lack of testing infrastructure, or fatigue.
```

**Giảm thiểu:**
- Xem xét các yếu tố tình huống
- Rèn luyện sự đồng cảm
- Tập trung vào hệ thống, không phải cá nhân
- Sử dụng những khám nghiệm tử thi vô tội vạ
### Xu hướng nhận thức muộn màng
**Nó là gì:** Sau khi một sự kiện xảy ra, bạn luôn tin rằng nó có thể đoán trước được.
**Ví dụ tồi:**```markdown
After production outage:
"I knew that deployment was risky. This was totally predictable."

Reality: The outcome wasn't obvious beforehand; hindsight makes it seem clear.
```

**Giảm thiểu:**
- Dự đoán tài liệu trước khi kết quả
- Xem xét bối cảnh quyết định, không chỉ kết quả
- Tránh xa văn hóa “Tôi đã bảo rồi mà”
- Tập trung cải tiến quy trình, không đổ lỗi
---

## Thêm những sai lầm logic
### Kêu gọi sự mới lạ
**Nó là gì:** Giả sử thứ gì đó tốt hơn vì nó mới hơn.
**Ví dụ tồi:**```markdown
"We should rewrite our entire backend in the latest framework. 
It's the newest, so it must be better."

Reality: Newer doesn't mean better for your specific use case.
Mature technologies often have better support and stability.
```

### Kêu gọi truyền thống
**Nó là gì:** Lập luận điều gì đó là đúng bởi vì nó luôn được thực hiện theo cách đó.
**Ví dụ tồi:**```markdown
"We've always deployed on Fridays at 5 PM. We shouldn't change that."

Reality: Just because something is traditional doesn't make it optimal.
(Actually, deploying on Friday at 5 PM is generally considered bad practice!)
```

### Tu Quoque (Kêu gọi đạo đức giả)
**Nó là gì:** Loại bỏ những lời chỉ trích bằng cách chỉ ra sự không nhất quán của người phê bình.
**Ví dụ tồi:**```markdown
Senior Dev: "You should write tests for this code."
Junior Dev: "But you don't write tests for your code either!"

Reality: The validity of the advice is independent of who gives it.
```

### Câu hỏi đã được tải
**Nó là gì:** Đặt câu hỏi chứa đựng một giả định.
**Ví dụ tồi:**```markdown
"Why did you write such terrible code for this module?"

Reality: The question assumes the code is terrible, putting the respondent
on the defensive regardless of actual code quality.
```

### Không có người Scotland đích thực
**Nó là gì:** Tạo ra một ngoại lệ đối với một tuyên bố chung khi bị thách thức.
**Ví dụ tồi:**```markdown
Person A: "No professional developer writes code without tests."
Person B: "But John is a professional developer and doesn't write tests."
Person A: "Well, no TRUE professional developer writes code without tests."

Reality: This redefines the category to exclude counterexamples rather 
than revising the claim.
```

### Sai lầm di truyền
**Nó là gì:** Đánh giá điều gì đó dựa trên nguồn gốc của nó thay vì giá trị hiện tại.
**Ví dụ tồi:**```markdown
"That library came from a small startup, so it can't be enterprise-grade."

Reality: The origin doesn't determine current quality. Evaluate based on
actual characteristics, not source.
```

### Ngụy biện trung gian
**Nó là gì:** Giả sử sự thật luôn nằm ở giữa hai thái cực.
**Ví dụ tồi:**```markdown
Developer A: "We should add comprehensive error handling."
Developer B: "Error handling isn't important, skip it."
Compromise: "Let's add some error handling, but not too much."

Reality: One position might be clearly correct. Compromise isn't always wise.
```

---

## Xu hướng nhận thức trong hệ thống AI
### Xu hướng dữ liệu đào tạo
Các mô hình AI kế thừa những thành kiến ​​có trong dữ liệu đào tạo của chúng.
**Ví dụ:**```markdown
Training data contains: "The doctor said..." (mostly male pronouns)
                       "The nurse said..." (mostly female pronouns)

Model learns: Doctors are typically male, nurses are typically female.

Result: Model exhibits gender bias in profession associations.
```

**Giảm thiểu:**
- Kiểm tra dữ liệu đào tạo về các thành kiến
- Sử dụng kỹ thuật khử nhiễu
- Kiểm tra đầu ra sai lệch
- Thu thập dữ liệu đa dạng
### Xu hướng tự động hóa
**Nó là gì:** Quá phụ thuộc vào hệ thống tự động, ngay cả khi chúng sai.
**Ví dụ:**```markdown
AI suggests code with a subtle bug.
Developer accepts it without review because "the AI is usually right."

Result: Bug makes it to production.
```

**Giảm thiểu:**
- Duy trì sự giám sát của con người
- Khuyến khích đánh giá quan trọng các kết quả đầu ra AI
- Đừng coi AI là không thể sai lầm
- Thực hiện các quy trình đánh giá
### Ảo tưởng về sự hiểu biết
**Nó là gì:** Tin rằng bạn hiểu cách AI hoạt động trong khi bạn thì không.
**Ví dụ:**```markdown
User: "The AI understands what I mean, it's like talking to a person."

Reality: LLMs predict tokens based on patterns, they don't truly 
"understand" in the human sense. This illusion leads to over-trust.
```

**Giảm thiểu:**
- Giáo dục người dùng về những hạn chế của AI
- Minh bạch về cách thức hoạt động của hệ thống
- Tránh nhân cách hóa AI
- Đặt kỳ vọng phù hợp
---

## Nghiên cứu trường hợp
### Case Study 1: Xu hướng xác nhận trong lựa chọn kiến ​​trúc
**Sự cố:** Một nhóm đã chọn kiến ​​trúc vi dịch vụ cho một ứng dụng nhỏ.
**Nguyên nhân cốt lõi:** Trưởng nhóm đã đọc một số bài viết ca ngợi vi dịch vụ và 
chỉ tìm kiếm thông tin xác nhận lựa chọn này, bỏ qua những cảnh báo về sự phức tạp.
**Tác động:**
- Chi phí lớn cho một nhóm gồm 3 nhà phát triển
- Độ phức tạp triển khai tăng gấp 10 lần
- Hiệu suất bị suy giảm do các cuộc gọi mạng
- Dự án chậm 6 tháng
**Bài học:** Đánh giá kiến trúc dựa trên ngữ cảnh cụ thể của bạn, không chỉ 
lời chứng thực tích cực. Hãy xem xét sự đánh đổi một cách rõ ràng.
### Nghiên cứu điển hình 2: Chi phí chìm trong hệ thống cũ
**Sự cố:** Công ty tiếp tục duy trì CRM được xây dựng tùy chỉnh trong 5 năm 
mặc dù có những lựa chọn thay thế tốt hơn.
**Nguyên nhân cốt lõi:** "Chúng tôi đã đầu tư 2 triệu đô la rồi, chúng tôi không thể từ bỏ nó bây giờ."
**Tác động:**
- Chi phí bảo trì hàng năm: 500K$
- Chi phí cơ hội: Không sử dụng được các tính năng hiện đại
- Vấn đề giữ chân nhân tài (các nhà phát triển muốn làm việc với công nghệ hiện đại)
- Tổng chi phí trong 5 năm: 4,5 triệu USD so với 1,5 triệu USD cho giải pháp thay thế SaaS
**Bài học:** Khoản đầu tư trong quá khứ bị đánh chìm. Đưa ra quyết định dựa trên giá trị tương lai.
### Nghiên cứu điển hình 3: Heuristic sẵn có trong bảo mật
**Sự cố:** Nhóm ưu tiên phòng thủ trước một cuộc tấn công được công bố gần đây 
vector trong khi bỏ qua các mối đe dọa có thể xảy ra hơn.
**Nguyên nhân cốt lõi:** Tin tức gần đây đã làm cho một loại mối đe dọa trở nên phổ biến 
trong bộ nhớ, đánh giá rủi ro sai lệch.
**Tác động:**
- Đã chi 100 nghìn đô la để giảm thiểu mối đe dọa có xác suất thấp
- Vi phạm thực tế xảy ra thông qua vectơ bị bỏ qua
- Chi phí phục hồi: $500K+
**Bài học:** Sử dụng mô hình hóa mối đe dọa dựa trên dữ liệu, không phải mức độ ưu tiên dựa trên thời gian gần đây.
---

## Bài tập thực hành
### Bài tập phát hiện sai lệch
Xem lại các quyết định gần đây và hỏi:
1. Chúng ta đã đưa ra những giả định gì?
2. Bằng chứng nào sẽ mâu thuẫn với kết luận của chúng tôi?
3. Chúng ta đã cân nhắc nhiều lựa chọn hay tập trung vào ý tưởng đầu tiên chưa?
4. Chúng ta tiếp tục vì giá trị tương lai hay vì khoản đầu tư trong quá khứ?
5. Chúng ta sẽ đề xuất điều gì nếu người khác hỏi chúng ta?
### Phát hiện lỗi sai logic
Thực hành xác định những sai lầm trong các cuộc thảo luận hàng ngày:
```markdown
Statement: "If we don't adopt AI now, we'll be left behind forever."

Analysis: This is a slippery slope fallacy. It assumes inevitable 
progression to being "left behind" without evidence. Also presents 
a false dichotomy (adopt AI or be left behind).
```

### Kỹ thuật khám nghiệm tử thi
Trước khi bắt đầu một dự án:
1. Hãy tưởng tượng đó là 6 tháng tới
2. Dự án thất bại ngoạn mục
3. Viết câu chuyện vì sao thất bại
4. Làm việc ngược lại để ngăn chặn những kiểu lỗi đó
Điều này phản ánh sự thiên vị lạc quan và kinh nghiệm sẵn có.
---

## Công cụ và Khung
### Mẫu nhật ký quyết định
```markdown
Date: [When]
Decision: [What we decided]
Context: [Situation and constraints]
Options Considered: [Alternatives evaluated]
Expected Outcome: [What we think will happen]
Confidence Level: [How sure we are]
Review Date: [When to revisit]

[Later] Actual Outcome: [What actually happened]
Lessons Learned: [What we'd do differently]
```

### Danh sách kiểm tra thiên vị
Trước khi đưa ra những quyết định quan trọng:
- [ ] Chúng ta đã tìm kiếm bằng chứng bác bỏ chưa?
- [ ] Chúng ta có đang bám chặt vào những thông tin ban đầu không?
- [ ] Chi phí chìm có ảnh hưởng đến chúng ta không?
- [ ] Chúng ta có quá tự tin vào ước tính của mình không?
- [ ] Chúng ta đã xem xét lãi suất cơ bản chưa?
- [ ] Có phải chúng ta đang mắc phải sai lệch về tình trạng sẵn có/mới?
- [ ] Liệu chúng ta có lựa chọn tương tự nếu bắt đầu mới không?
###Bài tập của đội đỏ
Phân công người tranh luận phản đối quyết định đề xuất:
- Vai trò của họ là tìm ra sai sót
- Họ phải trình bày những quan điểm thay thế
- Thực hành nhóm phản ứng lại những lời chỉ trích một cách xây dựng
- Lập hồ sơ các vấn đề được nêu ra và giải quyết
Điều này phản ánh sự thiên vị xác nhận và suy nghĩ nhóm.