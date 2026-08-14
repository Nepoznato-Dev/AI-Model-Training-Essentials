---
# Metadata
title: "Management and Project Methodologies"
description: "Leadership, Agile/Scrum/Kanban, OKRs, risk management"
category: "Business and Economics"
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
reviewed_by: "Business & Economics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [management, project, methodologies, business-and-economics]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "12 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Management and Project Methodologies

Managing people and projects is among the most demanding responsibilities in any organisation. Technical skills provide entry, but the ability to lead teams, make decisions, communicate effectively, and deliver results determines whether objectives are achieved. This file covers the frameworks, methodologies, and practical skills that effective managers and project leaders apply.

---

## Leadership Styles

There's no single "right" way to lead. The best style depends on the team, the task, and the context.

| Style | Description | Best When | Risk |
|-------|-------------|----------|------|
| **Autocratic** | Leader makes decisions with minimal input | Crisis; inexperienced team; time pressure | Low morale; dependency on leader |
| **Democratic** | Leader solicits input; team has real influence | Skilled team; complex decisions needing buy-in | Slower decisions; can feel wishy-washy |
| **Laissez-faire** | Leader provides direction; team self-manages | Highly skilled, self-motivated experts | Lack of coordination; unclear accountability |
| **Transformational** | Leader inspires vision and personal growth | Change initiatives; building high-performance culture | Can burn out if not grounded in execution |
| **Servant leadership** | Leader prioritises team's needs and development | Knowledge workers; building trust and loyalty | May be perceived as weak in hierarchical cultures |
| **Situational** | Leader adapts style to team maturity and task | Most real-world situations | Requires high emotional intelligence |

### What Great Managers Actually Do

Research (notably from Google's Project Oxygen) identified the top behaviours of effective managers:

1. **Is a good coach** — asks questions, helps people think, doesn't just give answers
2. **Empowers the team** — delegates meaningfully; doesn't micromanage
3. **Creates an inclusive environment** — psychological safety; everyone can contribute
4. **Is productive and results-oriented** — keeps the team focused on what matters
5. **Is a good communicator** — listens, shares context, gives clear direction
6. **Supports career development** — talks about growth, not just tasks
7. **Has a clear vision and strategy** — knows where the team is going and why
8. **Has key technical skills** — can advise and understand the work (even if not doing it)

---

## Project Management Methodologies

### Traditional (Waterfall)

| Phase | Activities |
|-------|-----------|
| **Requirements** | Gather and document what needs to be built |
| **Design** | Architecture, specifications, plans |
| **Implementation** | Build the thing |
| **Testing** | Verify it works as specified |
| **Deployment** | Release to production / users |
| **Maintenance** | Fix issues; ongoing support |

**Best for**: Construction, manufacturing, regulated industries where requirements are fixed and changes are expensive.

### Agile

Agile is a mindset, not a methodology. It comes from the [Agile Manifesto](https://agilemanifesto.org/) (2001):

> *Individuals and interactions* over processes and tools
> *Working software* over comprehensive documentation
> *Customer collaboration* over contract negotiation
> *Responding to change* over following a plan

| Agile Principle | What It Means in Practice |
|----------------|--------------------------|
| Deliver working software frequently | Short iterations (1–4 weeks) |
| Welcome changing requirements | Even late in development |
| Business and developers work together | Daily collaboration, not just at start and end |
| Build projects around motivated individuals | Give them the environment and trust they need |
| Face-to-face conversation | Most efficient way to convey information |
| Working software is the primary measure of progress | Not documents, not plans |
| Sustainable pace | Indefinitely; no death marches |
| Continuous attention to technical excellence | Good design and clean code |
| Simplicity | Maximise the work not done |
| Self-organising teams | Best architectures and designs emerge from them |
| Regular reflection and adjustment | Retrospectives; continuous improvement |

### Scrum

Scrum is the most widely used Agile framework.

| Element | Description |
|---------|-------------|
| **Sprint** | Fixed-length iteration (usually 2 weeks) |
| **Product Owner** | Defines and prioritises the backlog; represents stakeholders |
| **Scrum Master** | Facilitates the process; removes impediments; protects the team |
| **Development Team** | Cross-functional, self-organising (5–9 people ideal) |
| **Product Backlog** | Prioritised list of everything that might be needed |
| **Sprint Backlog** | Items selected for the current sprint + the plan to deliver them |
| **Daily Standup** | 15-minute sync: What did I do? What will I do? Any blockers? |
| **Sprint Review** | Demo working software to stakeholders; gather feedback |
| **Sprint Retrospective** | Team reflects on how to improve the process |

### Kanban

Kanban is a flow-based method focused on visualising work and limiting work-in-progress.

| Practice | Description |
|----------|-------------|
| **Visualise the workflow** | Board with columns (To Do → In Progress → Review → Done) |
| **Limit WIP** | Set a maximum number of items in each column |
| **Manage flow** | Measure cycle time; identify and remove bottlenecks |
| **Make policies explicit** | Everyone agrees on what "Done" means for each column |
| **Improve collaboratively** | Use data and feedback to evolve the process |

**Scrum vs Kanban**:

| | Scrum | Kanban |
|---|-------|--------|
| **Cadence** | Fixed sprints (2 weeks) | Continuous flow |
| **Roles** | PO, Scrum Master, Team | No prescribed roles |
| **Change** | No changes mid-sprint | Change anytime |
| **Metrics** | Velocity (story points per sprint) | Cycle time, throughput |
| **Best for** | Product development with regular releases | Support teams; continuous delivery |

---

## OKRs and KPIs

### OKRs (Objectives and Key Results)

OKRs are a goal-setting framework used by Google, Intel, Spotify, and many others.

| Component | Description | Example |
|-----------|-------------|---------|
| **Objective** | Qualitative, ambitious, inspiring | "Become the go-to platform for small business accounting" |
| **Key Result 1** | Measurable; proves the objective is being met | Increase monthly active users from 10K to 50K |
| **Key Result 2** | Measurable | Achieve NPS score of 60+ |
| **Key Result 3** | Measurable | Reduce onboarding time from 30 min to 5 min |

**OKR best practices**:
- Set 3–5 objectives per quarter
- Each objective has 2–5 key results
- Aim for 70% achievement (100% means goals were too easy)
- OKRs are separate from performance reviews
- Transparent: everyone can see everyone else's OKRs

### KPIs (Key Performance Indicators)

| Category | Example KPIs |
|----------|-------------|
| **Financial** | Revenue, gross margin, net profit, EBITDA |
| **Customer** | NPS, CSAT, churn rate, CLV |
| **Product** | DAU/MAU, feature adoption, time to value |
| **Engineering** | Deployment frequency, lead time, MTTR, change failure rate |
| **Marketing** | CAC, ROAS, conversion rate, organic traffic |
| **People** | Employee NPS, retention rate, time to hire |

---

## Stakeholder Management

| Stakeholder Type | What They Care About | How to Engage |
|-----------------|---------------------|---------------|
| **Executive sponsors** | ROI, strategic alignment, risk | Monthly updates; focus on outcomes |
| **End users** | Ease of use, reliability, solving their problem | User research; beta programmes; support channels |
| **Technical teams** | Code quality, architecture, technical debt | Architecture reviews; tech talks; involvement in decisions |
| **External customers** | Delivery timeline, quality, value | Regular demos; clear communication; SLAs |
| **Regulators / Compliance** | Legal requirements, audit trails | Documentation; proactive engagement |

### The Power/Interest Grid

| | Low Interest | High Interest |
|---|-------------|---------------|
| **High Power** | Keep satisfied | Manage closely (key players) |
| **Low Power** | Monitor (minimal effort) | Keep informed |

---

## Communication Frameworks

| Framework | Structure | When to Use |
|-----------|-----------|-------------|
| **PREP** | Point → Reason → Example → Point | Persuasive communication; meetings |
| **STAR** | Situation → Task → Action → Result | Interviews; performance reviews |
| **BLUF** | Bottom Line Up Front | Emails to executives; status updates |
| **SBAR** | Situation → Background → Assessment → Recommendation | Handoffs; incident communication |
| **The 7 Cs** | Clear, Concise, Concrete, Correct, Coherent, Complete, Courteous | General written communication |

### Giving Feedback

| Approach | Description |
|----------|-------------|
| **SBI** (Situation-Behaviour-Impact) | "In yesterday's meeting (situation), you interrupted the client (behaviour), which made them shut down (impact)." |
| **Feedforward** | Focus on future behaviour, not past mistakes. "Next time, try..." |
| **Radical Candour** (Kim Scott) | Care personally + challenge directly. Not too nice (ruinous empathy) and not too harsh (obnoxious aggression). |

---

## Decision-Making Models

| Model | Description | Best For |
|-------|-------------|----------|
| **RAPID** | Recommend, Agree, Perform, Input, Decide — clarifies who does what | Complex decisions with many stakeholders |
| **RACI** | Responsible, Accountable, Consulted, Informed — role clarity | Project tasks and deliverables |
| **Eisenhower Matrix** | Urgent/Important grid — prioritise tasks | Personal productivity; task triage |
| **Decision Matrix** | Score options against weighted criteria | Choosing between alternatives |
| **OODA Loop** | Observe → Orient → Decide → Act — rapid decision cycles | Competitive situations; incident response |
| **Six Thinking Hats** | Look at a decision from 6 perspectives (facts, emotions, risks, benefits, creativity, process) | Group decisions; avoiding groupthink |

### The Eisenhower Matrix

| | Urgent | Not Urgent |
|---|--------|------------|
| **Important** | **Do first** — crises, deadlines, critical problems | **Schedule** — strategic planning, relationship building, learning |
| **Not Important** | **Delegate** — some emails, meetings, interruptions | **Eliminate** — time wasters, busy work, excessive browsing |

---

## Risk Management

| Step | Description |
|------|-------------|
| **1. Identify risks** | Brainstorm what could go wrong (technical, schedule, resource, external) |
| **2. Assess probability and impact** | Rate each risk: High/Medium/Low for both |
| **3. Prioritise** | Focus on high-probability, high-impact risks |
| **4. Plan responses** | Avoid, mitigate, transfer, or accept each risk |
| **5. Monitor** | Review regularly; risks change as the project evolves |

### Risk Response Strategies

| Strategy | Description | Example |
|----------|-------------|---------|
| **Avoid** | Change the plan to eliminate the risk | Use proven technology instead of experimental |
| **Mitigate** | Reduce probability or impact | Add buffer time; hire additional staff |
| **Transfer** | Shift risk to a third party | Insurance; outsourcing; fixed-price contracts |
| **Accept** | Acknowledge and plan for it if it happens | Contingency fund; fallback plan |

---

## Remote Team Management

| Challenge | Solution |
|-----------|----------|
| **Communication gaps** | Default to written; over-communicate context; use async-first tools |
| **Isolation** | Regular 1:1s; virtual social events; occasional in-person meetups |
| **Time zones** | Rotate meeting times; record decisions; minimise synchronous dependencies |
| **Visibility** | Public channels over DMs; written status updates; shared dashboards |
| **Trust** | Measure outcomes, not hours; avoid surveillance software |
| **Onboarding** | Structured buddy system; documented processes; clear first-week goals |

### Effective Meetings

| Meeting Type | Duration | Frequency | Purpose |
|-------------|----------|-----------|---------|
| **Daily standup** | 15 min | Daily | Sync; surface blockers |
| **Sprint planning** | 1–2 hrs | Every sprint | Align on what to build next |
| **Sprint review** | 1 hr | Every sprint | Demo; gather feedback |
| **Retrospective** | 45–60 min | Every sprint | Process improvement |
| **1:1** | 30 min | Weekly/biweekly | Individual support and growth |
| **All-hands** | 30–60 min | Monthly | Company/team updates; Q&A |

**Meeting rules**: Every meeting needs an agenda. Start on time. End on time. Assign action items with owners. If it could be an email, make it an email.

---

## Organisational Structures

| Structure | Description | Pros | Cons |
|-----------|-------------|------|------|
| **Functional** | Organised by specialty (engineering, marketing, sales) | Deep expertise; clear career paths | Silos; slow cross-functional work |
| **Divisional** | Organised by product, market, or geography | Focus; accountability | Duplicated resources; inconsistent practices |
| **Matrix** | People report to both functional and project managers | Flexibility; resource sharing | Conflicting priorities; confusion about who's in charge |
| **Flat / Holacracy** | Minimal hierarchy; self-organised teams | Speed; autonomy; innovation | Unclear decisions; doesn't scale well |
| **Team-topology** (Skelton/Pais) | Stream-aligned teams + platform teams + enabling teams + complicated subsystem teams | Aligns with how work actually flows | Requires thoughtful design; not a silver bullet |

---

## Product Management Basics

Product management is the discipline of deciding what to build, for whom, and why — and ensuring it delivers value.

| Responsibility | Description |
|---------------|-------------|
| **Discovery** | User research, market analysis, competitive intelligence |
| **Strategy** | Product vision, roadmap, prioritisation frameworks |
| **Execution** | Write specs/user stories; work with engineering and design |
| **Launch** | Go-to-market planning; positioning; sales enablement |
| **Iteration** | Analyse metrics; gather feedback; prioritise next improvements |

### Prioritisation Frameworks

| Framework | How It Works |
|-----------|-------------|
| **MoSCoW** | Must have / Should have / Could have / Won't have |
| **RICE** | Reach × Impact × Confidence ÷ Effort |
| **Kano Model** | Classify features as basic, performance, or delight |
| **Value vs Effort matrix** | Plot on 2×2 grid; prioritise high-value, low-effort items |
| **Opportunity Scoring** | Importance minus satisfaction; find underserved needs |

---

## Summary

Management is the practice of achieving objectives through other people. Effective managers combine clear thinking (frameworks, methodologies, metrics) with interpersonal skills (listening, empathy, trust). No methodology replaces good judgment, but good judgment is enhanced by sound frameworks. These should be applied as practical guides rather than rigid doctrines.
