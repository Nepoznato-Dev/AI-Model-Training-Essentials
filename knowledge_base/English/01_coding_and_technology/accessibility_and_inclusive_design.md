---
# Metadata
title: "Accessibility and Inclusive Design"
description: "WCAG, inclusive UX, assistive technology, accessible coding"
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
tags: [accessibility, inclusive, design, coding-and-technology]
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

# Accessibility and Inclusive Design

Accessibility (often abbreviated as a11y) is the practice of making software usable by everyone — including people with visual, auditory, motor, cognitive, and neurological disabilities. It's not a nice-to-have; it's a legal requirement in many jurisdictions, a moral obligation, and good engineering. Accessible software is better software for everyone, because the design decisions that help disabled users — clear structure, keyboard navigation, sufficient contrast, readable text — improve the experience for all users.

---

## Who Benefits from Accessibility?

| Disability Type | Examples | Assistive Technology |
|----------------|---------|---------------------|
| **Visual** | Blindness, low vision, colour blindness | Screen readers (JAWS, NVDA, VoiceOver); magnifiers; high-contrast modes |
| **Auditory** | Deafness, hard of hearing | Captions; transcripts; visual alerts |
| **Motor** | Limited dexterity, paralysis, tremor | Keyboard-only navigation; voice control; switch devices; eye tracking |
| **Cognitive** | Dyslexia, ADHD, autism, memory impairments | Clear language; consistent navigation; reduced distractions |
| **Temporary** | Broken arm, bright sunlight, noisy environment | Same accommodations as permanent disabilities |
| **Situational** | Holding a baby, driving, one hand occupied | Voice interfaces; large touch targets |

**Key insight**: accessibility features designed for disabled users help everyone. Curb cuts (ramps at sidewalks) were designed for wheelchairs but are used by parents with strollers, delivery workers with carts, and travellers with luggage.

---

## Web Accessibility (WCAG)

The Web Content Accessibility Guidelines (WCAG) are the international standard for web accessibility.

### WCAG Principles (POUR)

| Principle | Requirement |
|-----------|-------------|
| **Perceivable** | Information must be presentable in ways users can perceive (text alternatives, captions, adaptable layout) |
| **Operable** | Interface must be navigable and usable (keyboard accessible, enough time, no seizure-inducing content) |
| **Understandable** | Information and operation must be comprehensible (readable, predictable, input assistance) |
| **Robust** | Content must work with current and future assistive technologies |

### WCAG Conformance Levels

| Level | Requirements | Typical Target |
|-------|-------------|---------------|
| **A** | Minimum level; 30 success criteria | Legal minimum in some jurisdictions |
| **AA** | Addresses the most common barriers | Standard target for most organisations |
| **AAA** | Highest level; not all content can achieve it | Specialised content; educational sites |

### Key Success Criteria (AA Level)

| Criterion | Requirement | How to Achieve |
|-----------|-------------|---------------|
| **1.1.1 Non-text content** | All images have text alternatives | `alt` attributes; `aria-label` for icons |
| **1.3.1 Info and relationships** | Structure conveyed programmatically | Semantic HTML; headings; lists; landmarks |
| **1.4.3 Contrast (minimum)** | Text has contrast ratio of at least 4.5:1 | Test with contrast checkers; choose accessible colour palettes |
| **1.4.4 Resize text** | Text can be resized to 200% without loss | Use relative units (rem, em); responsive design |
| **2.1.1 Keyboard** | All functionality available via keyboard | No keyboard traps; visible focus indicators |
| **2.4.3 Focus order** | Focus order preserves meaning and operability | Logical tab order; DOM order matches visual order |
| **2.4.7 Focus visible** | Keyboard focus is visually indicated | CSS `:focus-visible` styles; never `outline: none` without replacement |
| **3.3.2 Labels or instructions** | Inputs have labels | `<label>` elements; `aria-label` |
| **4.1.2 Name, role, value** | UI components have accessible names and roles | ARIA attributes; semantic HTML |

---

## ARIA (Accessible Rich Internet Applications)

ARIA adds accessibility information to HTML elements that don't have built-in semantics.

### ARIA Roles

| Role | Purpose | Example |
|------|---------|---------|
| `button` | Identifies an element as a button | A `<div>` styled as a button |
| `dialog` | Modal or non-modal dialog | Custom modal components |
| `tablist` / `tab` / `tabpanel` | Tab interface | Custom tab components |
| `alert` | Important message that appears dynamically | Error notifications |
| `progressbar` | Progress indicator | Loading states |
| `menu` / `menuitem` | Menu navigation | Dropdown menus |

### ARIA Attributes

| Attribute | Purpose | Example |
|-----------|---------|---------|
| `aria-label` | Accessible name when no visible text | Icon-only button: `aria-label="Search"` |
| `aria-describedby` | Links element to its description | Form field with help text |
| `aria-expanded` | Indicates if a section is expanded | Accordion; dropdown |
| `aria-hidden` | Hides element from assistive technology | Decorative icons |
| `aria-live` | Announces dynamic content changes | Live updates; notifications |
| `aria-disabled` | Indicates element is disabled | Greyed-out buttons |

### The First Rule of ARIA

> **Don't use ARIA if you can use native HTML instead.** A `<button>` is already accessible. A `<div role="button">` requires you to manually add keyboard handling, focus management, and screen reader support. Use semantic HTML first; ARIA only when native elements can't do the job.

---

## Keyboard Navigation

| Key | Expected Behaviour |
|-----|-------------------|
| **Tab** | Move focus to the next interactive element |
| **Shift + Tab** | Move focus to the previous interactive element |
| **Enter / Space** | Activate the focused element (button, link) |
| **Arrow keys** | Navigate within components (menus, tabs, radio groups) |
| **Escape** | Close a dialog, menu, or popover |
| **Home / End** | Jump to first / last item in a list |

### Common Keyboard Traps

| Problem | Fix |
|---------|-----|
| Focus enters a component but can't leave | Ensure Tab moves focus out; handle Escape |
| Modal doesn't trap focus | Focus should cycle within the modal; return to trigger on close |
| Custom components don't respond to keyboard | Add keydown handlers for Enter, Space, arrows |

---

## Colour and Visual Design

| Guideline | Requirement |
|-----------|-------------|
| **Contrast ratio** | 4.5:1 for normal text; 3:1 for large text (18pt+ or 14pt+ bold) |
| **Don't rely on colour alone** | Use icons, text, or patterns in addition to colour |
| **Focus indicators** | Always visible; high contrast; never removed without replacement |
| **Text resizing** | Layout must work at 200% zoom |
| **Responsive** | Content must reflow at 320px width (mobile) |

### Colour Blindness Considerations

| Type | Affected Colours | Design Tip |
|------|-----------------|------------|
| **Deuteranopia** | Red-green (most common) | Don't use red/green to convey status; use icons + colour |
| **Protanopia** | Red-green | Same as above |
| **Tritanopia** | Blue-yellow | Don't use blue/yellow as sole differentiator |

---

## Testing Accessibility

| Method | Tool | What It Catches |
|--------|------|----------------|
| **Automated scanning** | axe, Lighthouse, WAVE | Missing alt text; contrast issues; ARIA errors |
| **Keyboard testing** | Manual: unplug mouse, use only keyboard | Focus order; keyboard traps; missing handlers |
| **Screen reader testing** | NVDA (free), VoiceOver (macOS), JAWS | Missing labels; poor structure; unannounced changes |
| **Zoom testing** | Browser zoom to 200%, 400% | Layout breakage; clipped text; overflow issues |
| **Colour contrast** | WebAIM contrast checker, Stark plugin | Insufficient contrast ratios |
| **User testing** | Test with disabled users | Real-world barriers that automated tools miss |

---

## Legal Requirements

| Law | Region | Requirements |
|-----|--------|-------------|
| **ADA** (Americans with Disabilities Act) | USA | Websites of public accommodations must be accessible |
| **Section 508** | USA (federal) | Federal agencies' ICT must be accessible |
| **EAA** (European Accessibility Act) | EU (2025+) | Products and services must meet accessibility requirements |
| **EN 301 549** | EU | Technical standard for ICT accessibility |
| **ACA** (Accessibility Canada Act) | Canada | Government and regulated industries |
| **Equality Act 2010** | UK | Service providers must make reasonable adjustments |

---

## Mobile Accessibility

| Platform | Guidelines | Key Tools |
|----------|-----------|-----------|
| **iOS** | Apple Human Interface Guidelines (Accessibility section) | VoiceOver; Dynamic Type; Switch Control |
| **Android** | Android Accessibility guidelines | TalkBack; Switch Access; Select to Speak |

| Mobile Concern | Solution |
|---------------|----------|
| **Touch targets** | Minimum 44×44 points (iOS) / 48×48 dp (Android) |
| **Screen reader support** | Content descriptions; accessibility labels |
| **Motion sensitivity** | Respect `prefers-reduced-motion`; avoid auto-playing animations |
| **Dynamic text sizing** | Support system font sizes; use scalable text units |

---

## Summary

Accessibility is not a feature you add at the end — it's a design principle that should inform every decision from the start. Use semantic HTML. Ensure keyboard navigation works. Maintain sufficient colour contrast. Provide text alternatives for non-text content. Test with screen readers and real disabled users. The result is software that works better for everyone — not just those with disabilities, but also those with temporary impairments, situational limitations, older devices, slow connections, and the thousand other ways that real-world usage differs from the developer's idealised environment.
