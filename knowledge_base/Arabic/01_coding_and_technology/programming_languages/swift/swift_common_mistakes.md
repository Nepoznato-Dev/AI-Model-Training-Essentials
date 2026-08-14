---
# Metadata
title: "Swift — Common Mistakes & Anti-Patterns"
description: "Comprehensive guide to common pitfalls, traps, and anti-patterns in Swift that catch even experienced developers, with explanations and corrections."
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial common mistakes document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [swift, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "20 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# سويفت - الأخطاء الشائعة والأنماط المضادة
يقوم هذا المستند بفهرسة الأخطاء والفخاخ والأنماط المضادة الأكثر شيوعًا في Swift. يُظهر كل إدخال النهج غير الصحيح، ويشرح سبب فشله، ويقدم الحل الصحيح.
---

## 1. فرض إلغاء التغليف الاختياري
```swift
// ❌ WRONG — crash if nil
let user: User? = fetchUser()
print(user!.name)  // fatal error if user is nil

// ✅ CORRECT — optional binding
if let user = fetchUser() {
    print(user.name)
}

// ✅ CORRECT — guard let for early exit
guard let user = fetchUser() else { return }
print(user.name)

// ✅ CORRECT — optional chaining
let name = fetchUser()?.name
```

---

## 2. الاحتفاظ بالدورات مع عمليات الإغلاق
```swift
// ❌ WRONG — self captured strongly in closure
class ViewController {
    var timer: Timer?
    func startTimer() {
        timer = Timer.scheduledTimer(withTimeInterval: 1, repeats: true) { _ in
            self.updateUI()  // retain cycle!
        }
    }
}

// ✅ CORRECT — capture list with weak self
func startTimer() {
    timer = Timer.scheduledTimer(withTimeInterval: 1, repeats: true) { [weak self] _ in
        self?.updateUI()
    }
}
```

---

## 3. عدم استخدام`enum`مع القيم المرتبطة
```swift
// ❌ WRONG — using strings for state
var state = "loading"
if state == "loading" { ... }
else if state == "loaded" { ... }
else if state == "error" { ... }

// ✅ CORRECT — enum with associated values
enum LoadState {
    case loading
    case loaded(Data)
    case error(Error)
}

switch state {
case .loading: showSpinner()
case .loaded(let data): display(data)
case .error(let err): showError(err)
}
```

---

## 4. سوء فهم أنواع القيم مقابل أنواع المراجع
```swift
// ❌ WRONG — expecting struct mutation in closure
var count = 0
let closure = { count += 1 }  // Error: capture of mutable value

// ❌ WRONG — expecting struct sharing
struct Point { var x: Int; var y: Int }
let a = Point(x: 1, y: 2)
var b = a  // copy, not reference
b.x = 99
print(a.x)  // still 1!
```

---

## 5. النمط المضاد: وحدة تحكم العرض الضخمة
```swift
// ❌ WRONG — view controller doing everything
class ViewController: UIViewController {
    func fetchData() { ... }
    func parseJSON() { ... }
    func updateUI() { ... }
    func validateForm() { ... }
    func sendEmail() { ... }
}

// ✅ CORRECT — delegate to services and coordinators
class ViewController: UIViewController {
    private let viewModel: UserViewModel
    init(viewModel: UserViewModel) { self.viewModel = viewModel }
}
```

---

## 6. عدم استخدام`guard`للخروج المبكر
```swift
// ❌ WRONG — deeply nested if-let
func process(user: User?) {
    if let user = user {
        if let address = user.address {
            if let city = address.city {
                print(city)
            }
        }
    }
}

// ✅ CORRECT — guard for early exit
func process(user: User?) {
    guard let user = user else { return }
    guard let address = user.address else { return }
    guard let city = address.city else { return }
    print(city)
}
```

---

## 7. نسيان`weak`في المندوبين
```swift
// ❌ WRONG — strong delegate reference creates retain cycle
class ViewController: UIViewController {
    var delegate: MyDelegate?  // strong reference
}

// ✅ CORRECT — weak delegate
class ViewController: UIViewController {
    weak var delegate: MyDelegate?
}
```

---

## 8. ارتباك في فهرس السلسلة
```swift
// ❌ WRONG — can't use Int index on String
let greeting = "Hello"
greeting[0]  // Error! String.Index, not Int

// ✅ CORRECT — use String.Index
let first = greeting[greeting.startIndex]
let second = greeting[greeting.index(after: greeting.startIndex)]

// ✅ CORRECT — convert to array if indexing needed
let chars = Array(greeting)
let first = chars[0]
```

---

## 9. عدم استخدام`lazy`للعقارات باهظة الثمن
```swift
// ❌ WRONG — initializing expensive property eagerly
class DataManager {
    let database = ExpensiveDatabase()  // initialized even if never used
}

// ✅ CORRECT — lazy initialization
class DataManager {
    lazy var database = ExpensiveDatabase()  // only created when accessed
}
```

---

## 10. سلامة الخيط مع `@MainActor`
```swift
// ❌ WRONG — updating UI from background
func fetchData() {
    Task {
        let data = await api.getData()
        label.text = data.title  // not on main thread!
    }
}

// ✅ CORRECT — MainActor annotation
@MainActor
func updateUI(title: String) {
    label.text = title
}

// or mark the entire class
@MainActor
class ViewModel: ObservableObject { ... }
```

---

## ملخص
تمنع ميزات الأمان في Swift العديد من الأخطاء ولكنها تقدم مصائدها الخاصة: يؤدي إلغاء التغليف القسري إلى حدوث أعطال، وإخفاء دورات الاحتفاظ في عمليات الإغلاق والتفويضات، وتفاجئ دلالات نوع القيمة المطورين القادمين من لغات النوع المرجعي. طريقة Swift هي: عدم فرض الإلغاء مطلقًا (`!`)، واستخدام`guard`للخروج المبكر، واستخدام`weak`للمفوضين ولقطات الإغلاق، ووضع علامة على رمز واجهة المستخدم باستخدام `@MainActor`، وتقسيم وحدات تحكم العرض الضخمة إلى نماذج وخدمات عرض. نظام كتابة Swift هو صديقك - اعمل معه، وليس ضده.