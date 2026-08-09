---
# Metadata
title: "Pair Programming"
description: "Collaborate with another developer in real-time to produce better solutions while sharing knowledge"
category: "Collaboration Skills"
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
    date: "2026-01-15"
    author: "AI Model Training Team"
    changes: "Initial skill creation"

# Review
created: "2026-01-15"
last_modified: "2026-01-15"
review_date: "2026-07-15"
reviewed_by: "Collaboration Skills Team"
next_review: "2027-01-15"

# Classification
tags:
  - pair-programming
  - collaboration
  - knowledge-sharing
  - agile
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "15 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Pair Programming Skill

## Overview
The ability to effectively collaborate with another developer in real-time on the same code, leveraging two minds to produce better solutions while sharing knowledge.

## Core Competencies

### 1. Role Management
- **Driver**: Controls keyboard, focuses on implementation
- **Navigator**: Reviews each line, thinks strategically
- **Role Switching**: Transition smoothly between roles
- **Engagement**: Stay active regardless of role

### 2. Communication
- **Continuous Dialogue**: Explain thinking as you work
- **Active Listening**: Fully consider partner's input
- **Question Asking**: Clarify uncertainties immediately
- **Idea Sharing**: Voice thoughts before fully formed

### 3. Collaboration Techniques
- **Consensus Building**: Agree on approach before coding
- **Conflict Resolution**: Handle disagreements constructively
- **Pacing**: Match partner's speed and style
- **Encouragement**: Support partner's confidence

### 4. Technical Coordination
- **Shared Understanding**: Ensure both know the goal
- **Divide and Conquer**: Know when to pair vs. split
- **Tool Proficiency**: Use collaborative editing tools
- **Flow State**: Maintain productive rhythm together

## Frameworks & Methods

### Pair Programming Styles

#### Ping-Pong (TDD Style)
```
Person A: Write a failing test
Person B: Make the test pass
Person A: Refactor the code
Person B: Write next failing test
... continue pattern, switch drivers each cycle
```

#### Strong-Style Pairing
```
"For an idea to go from your head into the computer, 
it MUST go through someone else's hands."
- Llewellyn Falco

Rule: Driver implements ONLY what Navigator explains
      Switch roles every 15-20 minutes
```

#### Unstructured Pairing
```
- Natural flow based on task needs
- Roles switch organically
- Works well for experienced pairs
- Risk: One person may dominate
```

### Rotation Strategies

#### Time-Based
- Switch every 25 minutes (Pomodoro)
- Switch every hour
- Switch at natural breakpoints

#### Task-Based
- Switch after each feature
- Switch after each test cycle
- Switch when energy dips

#### Hybrid Approach
```
Morning Session (9-12):
- Pair on complex problems together
- Switch every 30-45 minutes

Afternoon Session (1-5):
- Split for independent work
- Reconvene for review/integration
```

## Practical Templates

### Pair Programming Session Template
```markdown
# Pair Programming Session

## Logistics
- Date: 
- Partners: 
- Duration: 
- Location/Tool: 

## Goal
[What are we trying to accomplish?]

## Approach
[High-level strategy we'll use]

## Setup Checklist
- [ ] Development environment ready
- [ ] Code pulled and up to date
- [ ] Tests running locally
- [ ] Distractions minimized
- [ ] Breaks scheduled

## Session Notes
### What We Tried
- 

### What Worked
- 

### What Didn't Work
- 

### Key Decisions Made
1. 
2. 

## Outcome
- [ ] Goal achieved
- [ ] Partial progress (see notes)
- [ ] Blocked (see blockers)

## Blockers/Questions
[List any unresolved issues]

## Next Steps
- [ ] 
- [ ] 

## Follow-up Session
- Scheduled: 
- Focus: 
```

### Working Agreements for Pairing
```markdown
# Pair Programming Agreements

## Communication
- Explain what you're typing as you type it
- Ask questions immediately when confused
- No silent coding for more than 2 minutes
- Use "we" language, not "you/I"

## Decision Making
- Discuss approach before implementing
- Both must agree on major decisions
- If stuck >10 min, take break or ask for help
- It's okay to disagree and try both ways

## Environment
- Driver controls keyboard/mouse
- Navigator can point but not grab
- Font size large enough for both to see
- Same IDE theme/settings if possible

## Breaks
- 5 min break every 25-30 min
- 15 min break every 2 hours
- Stand up and move during breaks
- No screens during breaks

## Respect
- No phones or other distractions
- Be patient with different skill levels
- Acknowledge good ideas from partner
- Thank each other at session end
```

### Remote Pairing Setup Guide
```markdown
## Tools Required
- Video conferencing (Zoom, Meet)
- Screen sharing or collaborative editor
- Good internet connection
- Headset with microphone

## Recommended Setups

### Option 1: VS Code Live Share
- Install Live Share extension
- Share workspace securely
- Both can edit simultaneously
- Shared terminal and debugging

### Option 2: Tuple/Screen
- Built for remote pair programming
- Low latency screen sharing
- Both can control cursor/keyboard
- High quality video/audio

### Option 3: Cloud IDE (Replit, Gitpod)
- Browser-based development
- No local setup needed
- Built-in collaboration
- Consistent environment

## Best Practices for Remote
- Cameras on for better connection
- Use headphones to prevent echo
- Explicitly state when you're typing
- More frequent check-ins ("Does this make sense?")
- Schedule slightly shorter sessions (focus harder remotely)
```

## Common Pitfalls

### ❌ What to Avoid

#### As Driver
- Coding silently without explanation
- Ignoring navigator's suggestions
- Going too fast for navigator to follow
- Taking over completely when frustrated
- Typing before discussing approach

#### As Navigator
- Checking phone/email
- Letting mind wander
- Criticizing without suggesting alternatives
- Taking over keyboard abruptly
- Being too passive or too controlling

#### General
- Pairing for too long without breaks
- Pairing on trivial tasks (waste of resources)
- Mismatched skill levels without adjustment
- Not switching roles regularly
- Skipping setup and jumping straight in

### ✅ Best Practices

#### Before Session
- Align on goals and expectations
- Ensure environment is ready
- Review relevant context/documentation
- Agree on duration and break schedule

#### During Session
- Talk through your thinking continuously
- Switch roles at planned intervals
- Take regular breaks
- Celebrate small wins together
- Ask "Should we keep pairing or split?"

#### After Session
- Document what was learned
- Note any follow-up items
- Reflect on what worked well
- Schedule next session if needed

## Tools & Resources

### Collaborative Editors
- **VS Code Live Share**: Real-time collaboration
- **JetBrains Code With Me**: IntelliJ family support
- **Teletype for Atom**: GitHub's collaboration tool
- **Cloud9/CodeSpaces**: Cloud-based IDEs

### Screen Sharing
- **Tuple**: Built for pair programming
- **Screen**: Low-latency macOS sharing
- **Zoom/Meet**: General purpose with screen share
- **Discord**: Casual pairing with friends

### Whiteboarding
- **Excalidraw**: Hand-drawn style diagrams
- **Miro**: Infinite canvas collaboration
- **CodePen/JSFiddle**: Quick code sharing
- **Replit**: Collaborative coding in browser

### Learning Resources
- "Pair Programming Illuminated" by Laurie Williams
- Extreme Programming (XP) documentation
- Agile Alliance pairing resources
- YouTube: Pair programming examples

## Example Application

### Scenario: Implementing Authentication Feature

**Pre-Session (15 min)**
```
Partners: Alex (Senior), Jordan (Mid-level)
Goal: Implement JWT-based login endpoint
Approach: TDD with ping-pong style
Duration: 2 hours with breaks
```

**Session Flow:**
```
9:00 - Setup and context sharing
9:15 - Jordan drives, writes first failing test
9:25 - Alex navigates, suggests error handling approach
9:35 - Alex makes test pass
9:45 - Jordan refactors, switches to driver
10:00 - BREAK (10 min)
10:10 - Alex drives, implements token generation
10:25 - Jordan navigates, catches edge case
10:40 - Pair debugs failing test together
10:55 - BREAK (10 min)
11:05 - Jordan drives, adds integration tests
11:20 - Alex navigates, suggests performance optimization
11:35 - Final refactor together
11:45 - Documentation and wrap-up
```

**Outcomes:**
- ✅ Login endpoint complete with tests
- ✅ Jordan learned JWT implementation patterns
- ✅ Alex gained fresh perspective on error handling
- ✅ Two bugs caught during pairing that would have reached production
- ✅ Documentation updated with usage examples

**Retrospective Notes:**
- Ping-pong worked well for knowledge transfer
- Should have started with more context on existing auth system
- Consider pairing again for logout/refresh token features

## Related Skills

- [Code Review](code_review.md) - Asynchronous collaborative code quality
- [Team Collaboration](team_collaboration.md) - Broader team effectiveness
- [Teaching](../behavior-skills/teaching.md) - Knowledge transfer through pairing

## Version Information

---
version: 1.0.0
last_updated: 2026-01-15
reviewed_by: Collaboration Skills Team
next_review: 2026-07-15
---
