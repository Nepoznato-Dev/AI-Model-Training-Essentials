---
# Metadata
title: "Data Visualization"
description: "Chart selection, design principles, storytelling, tools"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, visualization, data-science-and-analytics]
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
# Data Visualization

A well-designed chart can reveal patterns that tables of numbers hide. A poorly designed one can mislead, confuse, or bore. Data visualization is the craft of turning data into visual stories that inform decisions. This file covers chart selection, design principles, common mistakes, and the tools that make it all possible.

---

## Choosing the Right Chart

The most important decision in any visualization is choosing the right chart type for your data and message.

### Chart Selection Guide

| Your Goal | Best Chart Types |
|-----------|-----------------|
| **Compare categories** | Bar chart, grouped bar chart |
| **Show change over time** | Line chart, area chart |
| **Show distribution** | Histogram, box plot, violin plot |
| **Show relationship** | Scatter plot, bubble chart |
| **Show composition** | Stacked bar, pie chart (limited slices), treemap |
| **Show correlation** | Scatter plot, heatmap, pair plot |
| **Show ranking** | Horizontal bar chart |
| **Show geographic patterns** | Choropleth map, dot map |
| **Show part-to-whole over time** | Stacked area chart |

### When to Use Each Chart

| Chart | Strengths | Avoid When |
|-------|-----------|-----------|
| **Bar** | Clear comparisons across categories | Too many categories (>15) |
| **Line** | Trends over time; continuous data | Data isn't sequential |
| **Scatter** | Relationships between two variables | Too many overlapping points |
| **Histogram** | Distribution shape of one variable | Small sample sizes (<20) |
| **Box plot** | Summary statistics + outliers; compare distributions | Audience unfamiliar with them |
| **Heatmap** | Correlation matrices; patterns in 2D data | Too many variables |
| **Pie chart** | Simple composition (2–5 slices) | More than 5 slices; precise comparisons needed |
| **Violin plot** | Distribution density + quartiles | Small audiences unfamiliar with them |
| **Pair plot** | Quick overview of all variable relationships | Many variables (>8) |

---

## Design Principles

### Tufte's Core Ideas

Edward Tufte's principles remain the gold standard for data visualization:

| Principle | Description |
|-----------|-------------|
| **Maximise data-ink ratio** | Every drop of ink should convey data. Remove everything else. |
| **Eliminate chartjunk** | No 3D effects, gratuitous gradients, or decorative elements. |
| **Show the data** | Don't distort, hide, or cherry-pick. Let the data speak. |
| **Small multiples** | Use repeated small charts for comparison across categories. |
| **Sparklines** | Tiny, word-sized charts for inline trend data. |

### Practical Design Rules

| Rule | Why |
|------|-----|
| **Start y-axis at zero** (for bar charts) | Otherwise you exaggerate differences |
| **Label directly** | Put labels on lines/bars instead of using a legend when possible |
| **Use colour purposefully** | Highlight what matters; use grey for context |
| **Keep it simple** | One message per chart; don't overload |
| **Use consistent scales** | When comparing charts, keep axes the same |
| **Order meaningfully** | Sort bars by value (not alphabetically) unless there's a natural order |
| **Provide context** | Add benchmarks, targets, or historical averages |

### Colour Guidelines

| Use Case | Approach |
|----------|----------|
| **Categorical** | Distinct hues (blue, orange, green, red) — max 7–8 categories |
| **Sequential** | Light to dark of one hue (light blue → dark blue) |
| **Diverging** | Two-hue gradient for data with a meaningful midpoint (red ← white → blue) |
| **Accessibility** | Test with colourblind simulators; don't rely on colour alone (add labels or patterns) |

---

## Storytelling with Data

A chart without a narrative is just a picture. Storytelling turns data into insight.

### The Storytelling Framework

1. **Context**: What's the situation? What does the audience already know?
2. **Conflict**: What's the problem, surprise, or tension in the data?
3. **Resolution**: What should the audience do with this insight?

### Practical Tips

| Tip | Description |
|-----|-------------|
| **Lead with the insight** | Title the chart with the takeaway, not the data ("Revenue grew 30%" not "Revenue by Quarter") |
| **Annotate key points** | Add text callouts for important events or turning points |
| **Use progressive disclosure** | Show one chart at a time; build the story step by step |
| **Highlight what matters** | Use colour or size to draw attention to the key data point |
| **Provide a "so what?"** | Every chart should answer a question or prompt an action |

---

## Common Mistakes

| Mistake | Why It's Bad | Fix |
|---------|-------------|-----|
| **Truncated y-axis** | Exaggerates small differences | Start at zero for bar charts |
| **Cherry-picking time range** | Misleads about trends | Show full available range |
| **Too many colours** | Overwhelms the viewer | Limit to 5–7; use grey for context |
| **Dual y-axes** | Implies correlation that may not exist | Use two separate charts |
| **3D charts** | Distorts proportions | Always use 2D |
| **Pie charts with 10+ slices** | Impossible to compare | Use a bar chart instead |
| **Missing labels** | Viewer can't understand the chart | Always label axes, title, and units |
| **Misleading area charts** | Stacked areas distort perception of individual series | Use line charts or small multiples |

---

## Tools

### Python

| Library | Strength |
|---------|----------|
| **matplotlib** | Foundation of Python plotting; fully customisable |
| **seaborn** | Statistical visualisation; beautiful defaults; built on matplotlib |
| **plotly** | Interactive, web-based charts; dashboards |
| **altair** | Declarative grammar of graphics (Vega-Lite) |
| **bokeh** | Interactive visualisation for browsers |

### JavaScript / Web

| Library | Strength |
|---------|----------|
| **D3.js** | Maximum flexibility; steep learning curve |
| **Chart.js** | Simple, responsive charts |
| **Recharts** | React-friendly charting |
| **Observable Plot** | Lightweight, expressive grammar of graphics |

### No-Code / BI Tools

| Tool | Type |
|------|------|
| **Tableau** | Industry-standard visual analytics |
| **Power BI** | Microsoft ecosystem; enterprise BI |
| **Looker** | Google Cloud; data exploration |
| **Metabase** | Open-source; simple setup |
| **Apache Superset** | Open-source; SQL-native |

---

## Dashboard Design

A dashboard is a collection of visualisations that together tell a complete story about a process, system, or business.

### Dashboard Types

| Type | Audience | Purpose |
|------|----------|---------|
| **Strategic** | Executives | High-level KPIs; long-term trends |
| **Operational** | Managers | Real-time monitoring; daily operations |
| **Analytical** | Analysts | Deep exploration; filtering, drill-down |

### Design Checklist

- **Know your audience**: What decisions will they make from this dashboard?
- **5-second rule**: Can the main takeaway be grasped in 5 seconds?
- **Layout**: Most important metrics top-left (where eyes go first).
- **Limit chart types**: 3–4 types max per dashboard for consistency.
- **Interactive by default**: Filters, date range selectors, drill-downs.
- **Performance**: Dashboards that take >5 seconds to load don't get used.
- **Mobile**: Consider responsive design if users need it on the go.

---

## Summary

Good data visualization is about clarity, honesty, and impact. Choose the right chart for your data. Remove everything that doesn't serve the message. Use colour and annotation to guide the viewer. And always, always let the data tell the story — not the other way around.
