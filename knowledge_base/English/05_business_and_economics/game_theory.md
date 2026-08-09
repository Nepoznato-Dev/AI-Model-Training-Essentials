---
# Metadata
title: "Game Theory and Strategic Thinking"
description: "Nash equilibrium, prisoner's dilemma, mechanism design, auctions"
category: "Business and Economics"
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
reviewed_by: "Business & Economics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [game, theory, business-and-economics]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Game Theory and Strategic Thinking

Game theory is the mathematical study of strategic interactions — situations where your outcome depends not just on what you do, but on what others do. It applies everywhere: business competition, international relations, auctions, negotiations, evolutionary biology, and everyday decisions like choosing a route through traffic. The core insight is that rational actors in strategic situations don't just optimise their own strategy — they anticipate what others will do, and others are doing the same.

---

## Fundamental Concepts

### Key Terminology

| Term | Definition |
|------|-----------|
| **Game** | Any situation with two or more decision-makers (players) whose choices affect each other's outcomes |
| **Player** | A decision-maker in the game |
| **Strategy** | A complete plan of action for every situation that might arise |
| **Payoff** | The outcome a player receives from a particular combination of strategies |
| **Nash equilibrium** | A set of strategies where no player can improve their payoff by unilaterally changing their strategy |
| **Dominant strategy** | A strategy that is best regardless of what other players do |
| **Zero-sum game** | One player's gain is exactly another's loss |
| **Non-zero-sum game** | Players can potentially all gain or all lose |
| **Cooperative game** | Players can form binding agreements |
| **Non-cooperative game** | No binding agreements; each player acts in self-interest |

---

## Classic Games

### Prisoner's Dilemma

Two suspects are arrested. Each can cooperate (stay silent) or defect (confess).

| | B Cooperates | B Defects |
|---|-------------|-----------|
| **A Cooperates** | A: 1 year, B: 1 year | A: 10 years, B: free |
| **A Defects** | A: free, B: 10 years | A: 5 years, B: 5 years |

| Insight | Description |
|---------|-------------|
| **Dominant strategy** | Defect is dominant for both players |
| **Nash equilibrium** | Both defect (5 years each) |
| **Pareto optimal** | Both cooperate (1 year each) |
| **Lesson** | Rational individual decisions can lead to collectively worse outcomes |

### Other Classic Games

| Game | Description | Nash Equilibrium | Lesson |
|------|-------------|-----------------|--------|
| **Chicken (Hawk-Dove)** | Two drivers head toward each other; swerve or go straight | One swerves, one goes straight | Brinkmanship; credibility of commitment |
| **Stag Hunt** | Hunt a stag together (high payoff) or hunt a hare alone (low payoff) | Both stag or both hare | Coordination; trust |
| **Battle of the Sexes** | Two players prefer different outcomes but want to coordinate | Both go to the same event | Multiple equilibria; who moves first has advantage |
| **Ultimatum game** | Proposer divides money; responder accepts or rejects (both get nothing) | Proposer offers minimum; responder accepts | People reject unfair offers (irrational but common) |
| **Public goods game** | Contribute to a shared pool or free-ride | Everyone free-rides | Tragedy of the commons; need for enforcement |

---

## Types of Games

### By Timing

| Type | Description | Example |
|------|-------------|---------|
| **Simultaneous** | Players move at the same time (or without knowing others' moves) | Rock-paper-scissors; sealed-bid auctions |
| **Sequential** | Players move one after another; later players observe earlier moves | Chess; market entry decisions |
| **Repeated** | Same game played multiple times | Repeated prisoner's dilemma; ongoing business competition |

### By Information

| Type | Description | Example |
|------|-------------|---------|
| **Perfect information** | All players know all previous moves | Chess; checkers |
| **Imperfect information** | Some moves are hidden | Poker; business competition |
| **Complete information** | All players know all payoffs and strategies | Most textbook games |
| **Incomplete information** | Some payoffs or types are unknown | Auctions; negotiations |

---

## Solution Concepts

### Nash Equilibrium

| Aspect | Description |
|--------|-------------|
| **Definition** | No player can improve their payoff by changing their strategy alone |
| **How to find** | For each player, find best response to others' strategies; where they all intersect is the Nash equilibrium |
| **Existence** | Every finite game has at least one Nash equilibrium (possibly in mixed strategies) |
| **Uniqueness** | Games can have multiple Nash equilibria; coordination problems arise |
| **Limitation** | Nash equilibrium doesn't tell you which equilibrium will be selected; doesn't account for fairness |

### Dominant Strategy Equilibrium

| Step | Description |
|------|-------------|
| **1. Identify strategies** | List all available strategies for each player |
| **2. Find dominant strategies** | A strategy that is best regardless of what others do |
| **3. If all players have one** | The combination is the dominant strategy equilibrium |
| **4. If not** | Use iterated elimination of dominated strategies or Nash equilibrium |

### Backward Induction (Sequential Games)

| Step | Description |
|------|-------------|
| **1. Draw the game tree** | Nodes = decision points; branches = actions |
| **2. Start at the end** | Identify the last player's optimal choice at each terminal node |
| **3. Work backwards** | At each earlier node, choose the action that leads to the best outcome |
| **4. Result** | Subgame perfect equilibrium — optimal strategy at every decision point |

---

## Advanced Concepts

### Mixed Strategies

| Concept | Description | Example |
|---------|-------------|---------|
| **Mixed strategy** | Randomising between actions according to probabilities | Rock-paper-scissors: play each with 1/3 probability |
| **Why randomise?** | Prevents opponents from predicting your move | Penalty kicks in football; tax audits |
| **Mixed strategy Nash equilibrium** | Each player is indifferent between their pure strategies | Neither player can exploit the other |

### Repeated Games and Folk Theorem

| Concept | Description |
|---------|-------------|
| **Finitely repeated** | Backward induction unravels cooperation; same as one-shot game | Last-round defection propagates backwards |
| **Infinitely repeated** | Cooperation can be sustained through threats of future punishment | Tit-for-tat; grim trigger strategies |
| **Folk theorem** | Any individually rational payoff can be a Nash equilibrium in an infinitely repeated game | Cooperation is possible if the future matters enough |
| **Discount factor** | How much players value future payoffs; higher = more cooperation | Patient players cooperate more |

### Mechanism Design (Reverse Game Theory)

| Concept | Description |
|---------|-------------|
| **Goal** | Design the rules of a game to achieve a desired outcome |
| **Applications** | Auctions; voting systems; contract design; market design |
| **Revelation principle** | Any outcome achievable by any mechanism can be achieved by a truthful direct mechanism |
| **Example** | Vickrey auction (second-price sealed-bid) — bidding your true value is a dominant strategy |

---

## Applications

### Business

| Application | Game Theory Concept | Insight |
|-------------|-------------------|---------|
| **Price competition** | Prisoner's dilemma | Price wars hurt both firms; tacit collusion in repeated games |
| **Market entry** | Sequential game; commitment | Incumbent's threat to fight entry is only credible if they've invested in capacity |
| **Auctions** | Mechanism design | Second-price auctions elicit true values; spectrum auctions raise billions |
| **Negotiation** | Bargaining game; Nash equilibrium | Split the surplus; first-mover advantage in ultimatum games |
| **Signalling** | Spence's education model | Expensive signals are credible because low-quality types can't afford them |

### International Relations

| Application | Game Theory Concept | Insight |
|-------------|-------------------|---------|
| **Arms races** | Prisoner's dilemma | Both sides would be better off disarming but can't trust each other |
| **Trade wars** | Repeated game | Tit-for-tat: cooperate until the other defects, then retaliate |
| **Climate agreements** | Public goods game | Free-riding is rational; enforcement mechanisms needed |
| **Deterrence** | Chicken; credible commitment | Mutually assured destruction is a Nash equilibrium |

---

## Summary

Game theory studies strategic interactions where your outcome depends on others' actions. The Nash equilibrium — where no player benefits from changing strategy alone — is the central solution concept. Classic games like the prisoner's dilemma show that rational individual decisions can produce collectively bad outcomes. Sequential games are solved by backward induction. Repeated games can sustain cooperation through the threat of future punishment. Mixed strategies involve randomisation to remain unpredictable. Mechanism design reverses the question: instead of predicting outcomes, it designs rules to achieve desired outcomes (as in auctions). Applications span business (pricing, entry, auctions), politics (voting, treaties), biology (evolutionary stable strategies), and everyday life. The fundamental lesson is that strategy is not just about what you do — it's about anticipating what others will do, knowing they're doing the same.
