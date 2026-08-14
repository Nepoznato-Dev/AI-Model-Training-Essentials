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
# সুইফট — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্ন
এই নথিটি সুইফটের সবচেয়ে সাধারণ ভুল, ফাঁদ এবং অ্যান্টি-প্যাটার্নের ক্যাটালগ করে। প্রতিটি এন্ট্রি ভুল পদ্ধতি দেখায়, ব্যাখ্যা করে কেন এটি ব্যর্থ হয় এবং সঠিক সমাধান প্রদান করে।
---

## 1. জোর করে মোড়ক খুলে ফেলার বিকল্প
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

## 2. বন্ধের সাথে সাইকেল ধরে রাখুন
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

## 3. সংযুক্ত মানগুলির সাথে`enum`ব্যবহার না করা৷
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

## 4. ভুল বোঝাবুঝি মান প্রকার বনাম রেফারেন্স প্রকার
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

## 5. অ্যান্টি-প্যাটার্ন: ম্যাসিভ ভিউ কন্ট্রোলার
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

## 6. প্রাথমিক প্রস্থানের জন্য`guard`ব্যবহার করছেন না
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

## 7. প্রতিনিধিদের মধ্যে`weak`ভুলে যাওয়া
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

## 8. স্ট্রিং ইনডেক্স কনফিউশন
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

## 9. ব্যয়বহুল সম্পত্তির জন্য`lazy`ব্যবহার করছেন না
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

## 10.`@MainActor`সহ থ্রেড নিরাপত্তা
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

## সারাংশ
সুইফ্টের নিরাপত্তা বৈশিষ্ট্যগুলি অনেক বাগ প্রতিরোধ করে কিন্তু তাদের নিজস্ব ফাঁদ চালু করে: জোর করে খুলে ফেলার ফলে ক্র্যাশ হয়, চক্রগুলি বন্ধ এবং প্রতিনিধিদের মধ্যে লুকিয়ে রাখে এবং রেফারেন্স-টাইপ ভাষা থেকে আগত মান টাইপ শব্দার্থবিদ্যা বিকাশকারীদের অবাক করে দেয়। সুইফ্ট উপায় হল: কখনই জোর করে খুলবেন না (`!`), তাড়াতাড়ি প্রস্থানের জন্য`guard`ব্যবহার করুন, প্রতিনিধিদের জন্য`weak`ব্যবহার করুন এবং ক্লোজার ক্যাপচার করুন,`@MainActor`দিয়ে UI কোড চিহ্নিত করুন, এবং ভিউ মডেল এবং পরিষেবাগুলিতে বিশাল ভিউ কন্ট্রোলার ভেঙে দিন৷ সুইফটের টাইপ সিস্টেম আপনার বন্ধু - এটির সাথে কাজ করুন, এটির বিরুদ্ধে নয়।