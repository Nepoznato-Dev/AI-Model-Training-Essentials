# Information Retrieval Skill

## Overview
The ability to efficiently find, evaluate, and synthesize information from various sources to answer questions, solve problems, and make informed decisions.

## Core Competencies

### 1. Search Strategy
- **Keyword Selection**: Identify core concepts and synonyms
- **Query Construction**: Use advanced search operators effectively
- **Source Diversification**: Explore multiple types of sources
- **Iterative Refinement**: Adjust searches based on results

### 2. Source Evaluation
- **Credibility Assessment**: Author expertise, publication reputation
- **Currency Check**: Publication date, relevance to current context
- **Bias Detection**: Identify perspective and potential conflicts
- **Evidence Quality**: Data support, citations, methodology

### 3. Information Synthesis
- **Pattern Recognition**: Identify common themes across sources
- **Contradiction Resolution**: Reconcile conflicting information
- **Gap Identification**: Recognize missing information
- **Knowledge Integration**: Connect new info to existing understanding

### 4. Documentation & Organization
- **Note-Taking**: Capture key points systematically
- **Citation Management**: Track sources for attribution
- **Knowledge Base Building**: Organize findings for future reference
- **Summary Creation**: Distill essential information clearly

## Frameworks & Methods

### CRAAP Test for Source Evaluation
- **Currency**: When was it published? Is it current enough?
- **Relevance**: Does it address your specific question?
- **Authority**: Who created it? What are their credentials?
- **Accuracy**: Is it supported by evidence? Can it be verified?
- **Purpose**: Why does this information exist? (inform, sell, persuade)

### Boolean Search Operators
```
AND       - Both terms must appear: "python" AND "testing"
OR        - Either term appears: "unittest" OR "pytest"
NOT/-     - Exclude term: "java" -"javascript"
"quotes"  - Exact phrase: "machine learning"
site:     - Specific domain: site:github.com
filetype: - Specific format: filetype:pdf
intitle:  - In title: intitle:"best practices"
related:  - Similar sites: related:stackoverflow.com
*         - Wildcard: "how to * in python"
..        - Number range: python 2020..2024
```

### Research Workflow
1. **Define**: Clarify what you need to know
2. **Plan**: Identify potential sources and search terms
3. **Search**: Execute searches across multiple platforms
4. **Evaluate**: Assess credibility and relevance of results
5. **Extract**: Pull out key information
6. **Synthesize**: Combine insights from multiple sources
7. **Verify**: Cross-check critical claims
8. **Document**: Record findings with proper citations

## Practical Templates

### Research Question Framework
```markdown
## Primary Question
[Clear, specific question you're trying to answer]

## Sub-Questions
1. 
2. 
3. 

## Key Concepts & Keywords
- Primary: 
- Secondary: 
- Synonyms: 

## Source Types Needed
- [ ] Academic papers
- [ ] Technical documentation
- [ ] Industry reports
- [ ] Expert opinions
- [ ] Case studies
- [ ] Code examples/repositories

## Success Criteria
How will I know I have enough information?
```

### Source Evaluation Checklist
```markdown
# Source: [Title/URL]

## Credibility
- [ ] Author identified with credentials
- [ ] Published by reputable organization
- [ ] Contact information available
- [ ] About/mission page clear

## Content Quality
- [ ] Claims supported by evidence
- [ ] Citations/references provided
- [ ] Methodology explained (if research)
- [ ] Peer-reviewed (if applicable)

## Currency
- [ ] Publication date: [DATE]
- [ ] Links are functional
- [ ] Information is up-to-date for topic

## Bias Check
- [ ] Purpose is clear (inform vs. sell)
- [ ] Multiple perspectives considered
- [ ] Funding/sponsorship disclosed
- [ ] Language is balanced

## Relevance
- [ ] Directly addresses research question
- [ ] Appropriate depth for needs
- [ ] Target audience matches

## Overall Rating: ⭐⭐⭐⭐⭐ (1-5)
Notes: 
```

### Research Notes Template
```markdown
# Research Notes: [Topic]
Date: [YYYY-MM-DD]

## Key Findings

### Finding 1: [Headline]
**Source:** [Citation]
**Summary:** 
**Quote:** "..."
**My Analysis:** 

### Finding 2: [Headline]
**Source:** [Citation]
**Summary:** 
**Quote:** "..."
**My Analysis:** 

## Contradictions/Uncertainties
- 

## Knowledge Gaps
- 

## Action Items
- [ ] Follow up on...
- [ ] Verify...
- [ ] Explore...

## Bibliography
1. 
2. 
3. 
```

## Common Pitfalls

### ❌ What to Avoid
- Relying on single source of truth
- Accepting top search results without evaluation
- Confirmation bias (seeking only supporting evidence)
- Not checking publication dates
- Ignoring primary sources
- Poor note-taking leading to lost citations
- Overwhelm from too many sources
- Surface-level reading without deep analysis
- Not considering opposing viewpoints
- Hoarding information without synthesis

### ✅ Best Practices
- Start with overview sources, then go deeper
- Triangulate information across 3+ sources
- Check original sources of cited claims
- Use incognito mode to avoid filter bubbles
- Set time limits to prevent rabbit holes
- Take breaks during intensive research
- Save/search in organized folders
- Write summaries in your own words
- Note confidence level of each finding
- Know when "good enough" is sufficient

## Tools & Resources

### Search Engines & Databases
- **Google Scholar**: Academic papers
- **PubMed**: Medical/life sciences
- **IEEE Xplore**: Engineering/technology
- **arXiv**: Pre-print scientific papers
- **GitHub**: Code and technical implementations
- **Stack Overflow**: Programming Q&A

### Reference Management
- **Zotero**: Free citation manager
- **Mendeley**: Reference + PDF management
- **Notion/Obsidian**: Knowledge base building
- **Evernote/OneNote**: Note organization

### Browser Extensions
- **Unpaywall**: Access open-access papers
- **PubMed Helper**: Quick PubMed access
- **Google Scholar Button**: Quick citations
- **Raindrop.io**: Bookmark management

### AI-Assisted Research
- **Consensus**: AI research paper search
- **Elicit**: AI research assistant
- **Scite.ai**: Smart citation analysis
- **Semantic Scholar**: AI-powered search

## Example Application

### Scenario: Researching "Best Database for Real-Time Analytics"

**Step 1: Define Scope**
- Need: Database for processing streaming data
- Constraints: <100ms latency, handle 10K events/sec
- Context: E-commerce clickstream analysis

**Step 2: Initial Search**
```
"real-time analytics database" comparison
"time-series database" benchmark 2024
"streaming data" database performance
```

**Step 3: Source Types**
- Vendor documentation (TimescaleDB, InfluxDB, ClickHouse)
- Independent benchmarks (DB-Engines, Datadog blogs)
- Case studies (companies with similar use cases)
- Reddit/HackerNews discussions (practical experiences)

**Step 4: Evaluation Matrix**
| Database | Latency | Throughput | Cost | Community | Learning Curve |
|----------|---------|------------|------|-----------|----------------|
| A        |         |            |      |           |                |
| B        |         |            |      |           |                |

**Step 5: Synthesis**
- Common recommendation: TimescaleDB for PostgreSQL compatibility
- Trade-off: ClickHouse faster but steeper learning curve
- Consensus: Start with managed service, optimize later

**Step 6: Decision Document**
Create summary with recommendation, alternatives considered, and implementation plan.

## Success Indicators
- Confident decision-making with clear rationale
- Ability to explain trade-offs considered
- Sources readily available for verification
- Efficient research time (not over-researching)
- Findings validated by experts/outcomes
- Knowledge reusable for future questions
- Others can follow your research trail
