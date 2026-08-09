---
# Metadata
title: "Mobile Development"
description: "iOS, Android, React Native, Flutter, mobile architecture"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [mobile, development, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Mobile Development

Mobile development is the practice of building applications for smartphones and tablets — primarily for iOS (Apple) and Android (Google). It encompasses everything from UI design for small screens to managing battery life, handling network instability, and distributing apps through stores. The field has matured significantly, with cross-platform frameworks now competing with native development for most use cases.

---

## The Mobile Landscape

| Platform | Developer | Language(s) | Store | Market Share (Global) |
|----------|-----------|-------------|-------|----------------------|
| **Android** | Google | Kotlin, Java | Google Play | ~72% |
| **iOS** | Apple | Swift, Objective-C | App Store | ~27% |

---

## Native Development

### Android

| Aspect | Details |
|--------|---------|
| **Language** | Kotlin (primary), Java (legacy) |
| **UI Framework** | Jetpack Compose (modern), XML layouts (legacy) |
| **Build system** | Gradle |
| **IDE** | Android Studio |
| **Min SDK** | Developer chooses; most target API 24+ (Android 7.0, 2016) |
| **Distribution** | Google Play Store; alternative stores in some markets |

### iOS

| Aspect | Details |
|--------|---------|
| **Language** | Swift (primary), Objective-C (legacy) |
| **UI Framework** | SwiftUI (modern), UIKit (mature) |
| **Build system** | Xcode build system |
| **IDE** | Xcode (macOS only) |
| **Min version** | Developer chooses; most target iOS 16+ |
| **Distribution** | Apple App Store (only option for most apps) |

---

## Cross-Platform Frameworks

Build once, deploy to both iOS and Android.

| Framework | Language | Rendering | Performance | Best For |
|-----------|----------|-----------|-------------|----------|
| **Flutter** | Dart | Custom engine (Skia/Impeller) | Near-native | Rich custom UIs; consistent look across platforms |
| **React Native** | JavaScript/TypeScript | Native components via bridge | Good (New Architecture improves this) | Teams with web/JS experience |
| **Kotlin Multiplatform** | Kotlin | Native UI per platform | Native | Sharing business logic; native UI |
| **MAUI** (.NET) | C# | Native controls | Good | .NET teams; enterprise apps |
| **Ionic / Capacitor** | HTML/CSS/JS | WebView | Lower | Simple apps; web teams |

### Flutter vs React Native

| Aspect | Flutter | React Native |
|--------|---------|-------------|
| **Language** | Dart | JavaScript/TypeScript |
| **UI rendering** | Draws everything itself (consistent across platforms) | Uses native components (platform-specific look) |
| **Hot reload** | Excellent | Good |
| **Ecosystem** | Growing rapidly; widget-based | Large; npm ecosystem |
| **Learning curve** | Need to learn Dart | Easier for web developers |
| **Platform integration** | Platform channels for native code | Native modules via bridge |
| **Performance** | Excellent; near-native | Good; bridge overhead (reduced with New Architecture) |

---

## Mobile Architecture Patterns

| Pattern | Description | When to Use |
|---------|-------------|-------------|
| **MVC** | Model-View-Controller | Simple apps; familiar to web developers |
| **MVVM** | Model-View-ViewModel; data binding | Most modern mobile apps |
| **MVI** | Model-View-Intent; unidirectional data flow | Complex state management; Flutter (with BLoC/Riverpod) |
| **Clean Architecture** | Layers with dependency inversion | Large teams; complex business logic |

---

## Key Mobile Concerns

### Offline-First Design

Mobile apps must work without reliable internet.

| Strategy | Description |
|----------|-------------|
| **Local database** | Store data on-device (SQLite, Room, CoreData, Realm) |
| **Sync strategy** | Sync with server when online; resolve conflicts |
| **Optimistic UI** | Update the UI immediately; reconcile when server responds |
| **Cache** | Cache API responses; serve from cache when offline |

### Performance

| Concern | Solution |
|---------|----------|
| **App startup time** | Lazy loading; minimise initialisation work |
| **Memory usage** | Image compression; avoid memory leaks; use profiling tools |
| **Battery drain** | Reduce background work; batch network requests; use efficient location services |
| **Network efficiency** | Compress payloads; use pagination; cache aggressively |
| **List scrolling** | Recycle views; use lazy loading for images |

### Security

| Concern | Solution |
|---------|----------|
| **Data at rest** | Encrypt sensitive data (Keychain on iOS, EncryptedSharedPreferences on Android) |
| **Network** | Always HTTPS; certificate pinning for sensitive apps |
| **Authentication** | Biometrics (Face ID, fingerprint); OAuth; token storage |
| **Code obfuscation** | ProGuard/R8 for Android; bitcode for iOS |
| **Jailbreak/root detection** | Detect compromised devices; limit functionality |

---

## App Lifecycle

| State | Description | What to Do |
|-------|-------------|------------|
| **Foreground (active)** | User is interacting with the app | Normal operation |
| **Background** | App is not visible but still in memory | Pause animations; save state |
| **Suspended** | OS has frozen the app to save resources | Nothing; app is frozen |
| **Terminated** | OS killed the app to free memory | Restore state on next launch |

---

## Push Notifications

| Platform | Service | Protocol |
|----------|---------|----------|
| **iOS** | APNs (Apple Push Notification service) | HTTP/2 |
| **Android** | FCM (Firebase Cloud Messaging) | HTTP/v1 |

| Notification Type | Description |
|-------------------|-------------|
| **Data notification** | Silent; app processes the payload | Background updates |
| **Display notification** | Shows in the notification tray | User alerts |
| **Rich notification** | Includes images, actions, or custom UI | Enhanced user engagement |

---

## App Distribution

| Platform | Store | Review Time | Revenue Cut |
|----------|-------|-------------|-------------|
| **iOS** | App Store | 24-48 hours | 30% (15% for small businesses) |
| **Android** | Google Play | Hours to days | 30% (15% for first $1M) |
| **Android (alternative)** | Samsung Galaxy Store, Amazon Appstore, F-Droid | Varies | Varies |

### CI/CD for Mobile

| Tool | Purpose |
|------|---------|
| **Fastlane** | Automate builds, screenshots, signing, and deployment |
| **GitHub Actions** | CI/CD with macOS runners for iOS builds |
| **Bitrise** | Mobile-focused CI/CD |
| **App Center** (Microsoft) | Build, test, distribute (being sunset; alternatives emerging) |
| **EAS** (Expo Application Services) | Cloud builds for React Native/Expo |

---

## Testing

| Type | Tools | Purpose |
|------|-------|---------|
| **Unit tests** | JUnit, XCTest | Test business logic |
| **Widget tests** | Flutter Widget Test, Robolectric | Test UI components in isolation |
| **Integration tests** | Espresso (Android), XCUITest (iOS), Flutter Integration | Test component interactions |
| **E2E tests** | Detox, Appium, Maestro | Test full user flows on real/simulated devices |
| **Performance tests** | Android Profiler, Instruments (iOS) | Measure frame rate, memory, CPU |

---

## Summary

Mobile development offers a choice between native (best performance, platform-specific) and cross-platform (shared codebase, faster iteration). Flutter and React Native have matured to the point where cross-platform is the right choice for most applications. The core challenges remain the same regardless of framework: offline-first design, performance on limited hardware, battery efficiency, security on untrusted devices, and navigating app store review processes. The field rewards developers who think about the user experience first — fast startup, smooth scrolling, and graceful handling of poor connectivity.
