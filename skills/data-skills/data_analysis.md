# Data Analysis Skill

## Overview

Data analysis is the process of inspecting, cleaning, transforming, and modeling data to discover useful information, draw conclusions, and support decision-making. It combines statistical knowledge, domain expertise, and technical skills to extract actionable insights from raw data.

## When to Use

- Exploring datasets to understand patterns and trends
- Making data-driven business decisions
- Identifying problems or opportunities in operations
- Validating hypotheses through statistical testing
- Creating reports and dashboards for stakeholders
- Building predictive models for forecasting
- Measuring performance against KPIs and metrics
- Conducting A/B tests and experiments

## Core Competencies

### Statistical Analysis
- Descriptive statistics (mean, median, mode, variance, standard deviation)
- Inferential statistics (hypothesis testing, confidence intervals)
- Probability distributions (normal, binomial, Poisson)
- Correlation and regression analysis
- Time series analysis and forecasting
- Bayesian statistics
- Statistical significance and p-values
- Power analysis and sample size determination

### Data Exploration
- Exploratory Data Analysis (EDA) techniques
- Data profiling and quality assessment
- Outlier detection and handling
- Pattern recognition and anomaly detection
- Distribution analysis and visualization
- Feature relationships and interactions
- Data segmentation and grouping

### Data Visualization
- Choosing appropriate chart types for data
- Dashboard design principles
- Interactive visualization creation
- Storytelling with data
- Color theory and visual perception
- Avoiding misleading representations
- Tools: Matplotlib, Seaborn, Plotly, Tableau, Power BI

### Data Cleaning & Preparation
- Handling missing values (imputation, deletion)
- Data type conversion and validation
- Removing duplicates and inconsistencies
- Standardizing formats and units
- Feature engineering and transformation
- Data normalization and scaling
- Encoding categorical variables

### Analytical Thinking
- Problem decomposition and framing
- Critical thinking and skepticism
- Root cause analysis
- Comparative analysis
- Trend analysis and pattern recognition
- Contextual interpretation of results
- Drawing valid conclusions from data

## Design Principles

### CRISP-DM Framework
Cross-Industry Standard Process for Data Mining:
1. **Business Understanding** - Define objectives and requirements
2. **Data Understanding** - Collect and explore initial data
3. **Data Preparation** - Clean and transform data
4. **Modeling** - Apply analytical techniques
5. **Evaluation** - Assess results against objectives
6. **Deployment** - Implement findings

### OSEMN Framework
- **Obtain** - Acquire data from sources
- **Scrub** - Clean and preprocess data
- **Explore** - Analyze and visualize patterns
- **Model** - Apply statistical/ML techniques
- **Interpret** - Draw conclusions and communicate

### FAIR Principles
- **Findable** - Data should be easy to find
- **Accessible** - Data should be retrievable
- **Interoperable** - Data should work with other systems
- **Reusable** - Data should be well-documented for reuse

## Frameworks & Methods

### Analysis Process
1. **Define Question** - Clearly state what you want to learn
2. **Collect Data** - Gather relevant data from sources
3. **Clean Data** - Handle missing values, outliers, errors
4. **Explore Data** - Understand distributions and relationships
5. **Analyze** - Apply statistical methods and models
6. **Interpret** - Draw conclusions and insights
7. **Communicate** - Present findings to stakeholders
8. **Act** - Make decisions based on analysis

### Statistical Methods
- **Descriptive Analysis** - Summarize and describe data
- **Diagnostic Analysis** - Understand why something happened
- **Predictive Analysis** - Forecast future outcomes
- **Prescriptive Analysis** - Recommend actions
- **Causal Analysis** - Determine cause-and-effect relationships

### Documentation Standards
- Analysis notebooks with clear narrative
- Data dictionaries and metadata
- Methodology documentation
- Assumptions and limitations
- Reproducible code and pipelines
- Version control for analyses

## Practical Templates

### Analysis Project Template
```markdown
# Analysis: [Project Name]

## Objective
[Clear statement of what we're trying to learn]

## Hypotheses
- H1: [First hypothesis]
- H2: [Second hypothesis]

## Data Sources
- [Source 1]: [Description and access method]
- [Source 2]: [Description and access method]

## Methodology
[Statistical methods and tools used]

## Key Findings
1. [Finding 1 with supporting data]
2. [Finding 2 with supporting data]

## Recommendations
- [Actionable recommendation 1]
- [Actionable recommendation 2]

## Limitations
- [Limitation 1]
- [Limitation 2]

## Next Steps
[Follow-up analyses or actions needed]
```

### Statistical Test Selection Guide
| Question Type | Data Type | Recommended Test |
|--------------|-----------|------------------|
| Compare means (2 groups) | Continuous | t-test |
| Compare means (3+ groups) | Continuous | ANOVA |
| Compare proportions | Categorical | Chi-square test |
| Relationship between variables | Continuous | Correlation/Regression |
| Before/after comparison | Paired data | Paired t-test |
| Predict outcome | Mixed | Linear/Logistic Regression |
| Time-based patterns | Time series | ARIMA, Exponential Smoothing |

### Data Quality Checklist
- [ ] Missing values identified and handled
- [ ] Duplicates removed or accounted for
- [ ] Outliers detected and investigated
- [ ] Data types are correct
- [ ] Ranges and constraints validated
- [ ] Consistency across sources verified
- [ ] Temporal integrity checked
- [ ] Business rules validated

## Common Pitfalls

### Correlation vs Causation
**Problem**: Assuming correlation implies causation.
**Solution**: Use controlled experiments, consider confounding variables, apply causal inference methods.

### P-Hacking
**Problem**: Manipulating analysis until finding significant results.
**Solution**: Pre-register hypotheses, adjust for multiple comparisons, report all analyses conducted.

### Selection Bias
**Problem**: Analyzing non-representative samples.
**Solution**: Use random sampling, understand data collection process, acknowledge limitations.

### Overfitting
**Problem**: Models that work on training data but fail on new data.
**Solution**: Use cross-validation, regularization, keep models simple, test on holdout data.

### Ignoring Context
**Problem**: Analyzing numbers without business context.
**Solution**: Collaborate with domain experts, understand business processes, consider external factors.

### Cherry-Picking Data
**Problem**: Selecting only data that supports desired conclusion.
**Solution**: Analyze complete datasets, document exclusions, be transparent about methodology.

## Best Practices

### Do
- Start with clear questions and hypotheses
- Document all assumptions and decisions
- Validate data quality before analysis
- Use version control for code and data
- Create reproducible analyses
- Visualize data at every stage
- Communicate uncertainty and limitations
- Peer review important analyses

### Don't
- Skip data exploration and cleaning
- Ignore missing data or outliers
- Use inappropriate statistical tests
- Overcomplicate models unnecessarily
- Present correlations as causation
- Hide unfavorable results
- Forget to validate findings
- Neglect data privacy and security

## Tools & Resources

### Programming Languages
- **Python** - Pandas, NumPy, SciPy, StatsModels
- **R** - Tidyverse, ggplot2, dplyr, tidyr
- **SQL** - Database querying and aggregation
- **Julia** - High-performance statistical computing

### Visualization Tools
- **Tableau** - Interactive dashboards
- **Power BI** - Business intelligence
- **Looker** - Data exploration platform
- **Matplotlib/Seaborn** - Python visualization
- **ggplot2** - R visualization
- **Plotly** - Interactive graphs

### Notebook Environments
- **Jupyter Notebook** - Interactive Python/R
- **JupyterLab** - Enhanced notebook interface
- **Google Colab** - Cloud-based notebooks
- **Databricks** - Collaborative analytics
- **Observable** - JavaScript data visualization

### Data Sources
- **Kaggle** - Datasets and competitions
- **UCI ML Repository** - Research datasets
- **Government Open Data** - Public datasets
- **APIs** - Real-time data access

## Real-World Examples

### E-commerce Conversion Analysis
```python
# Example: Analyzing conversion funnel
import pandas as pd
import numpy as np

# Load data
sessions = pd.read_csv('sessions.csv')
conversions = pd.read_csv('conversions.csv')

# Calculate conversion rates by channel
conversion_rates = sessions.merge(conversions, on='session_id', how='left')
conversion_rates['converted'] = conversions['conversion_id'].notna()

funnel_analysis = conversion_rates.groupby('traffic_source').agg({
    'session_id': 'count',
    'converted': ['sum', 'mean']
}).round(4)

# Statistical significance test
from scipy import stats
organic = conversion_rates[conversion_rates['traffic_source'] == 'organic']['converted']
paid = conversion_rates[conversion_rates['traffic_source'] == 'paid']['converted']

stat, p_value = stats.ttest_ind(organic, paid)
print(f"P-value: {p_value:.4f}")
```

### Customer Segmentation
Analysis approach:
1. Collect customer behavior data
2. Perform RFM analysis (Recency, Frequency, Monetary)
3. Apply clustering algorithms (K-means, hierarchical)
4. Profile and name segments
5. Develop targeted strategies per segment
6. Measure segment performance over time

### A/B Test Analysis
Key considerations:
- Proper sample size calculation
- Random assignment verification
- Run test for sufficient duration
- Check for novelty effects
- Analyze primary and secondary metrics
- Segment results for deeper insights
- Calculate confidence intervals

## Metrics for Success

### Analysis Quality Metrics
- Stakeholder satisfaction score > 4/5
- Recommendation implementation rate > 60%
- Analysis reproducibility rate = 100%
- Peer review pass rate > 90%

### Business Impact Metrics
- Revenue impact from insights (tracked quarterly)
- Cost savings identified and realized
- Decision speed improvement
- Risk mitigation value

### Technical Metrics
- Data accuracy > 99%
- Analysis completion within SLA
- Code coverage > 80%
- Documentation completeness > 95%

## Practice Exercises

### Beginner
1. Analyze a sales dataset to find top products and trends
2. Create visualizations showing monthly revenue patterns
3. Calculate descriptive statistics for customer demographics
4. Build a simple dashboard in Excel or Tableau

### Intermediate
1. Perform cohort analysis on user retention data
2. Conduct A/B test analysis with statistical significance
3. Build a regression model to predict outcomes
4. Create an interactive dashboard with filters

### Advanced
1. Analyze time series data with seasonality and trends
2. Perform customer segmentation using clustering
3. Design and analyze a multi-variate experiment
4. Build an end-to-end analytics pipeline with automation

## Getting Started

### Learning Path
1. **Fundamentals**: Learn statistics basics and Excel
2. **Programming**: Master Python or R for analysis
3. **Visualization**: Study data visualization principles
4. **SQL**: Learn database querying for data extraction
5. **Domain Knowledge**: Understand your industry deeply
6. **Communication**: Practice presenting insights clearly

### Recommended Resources
- Books: "Storytelling with Data" by Cole Nussbaumer Knaflic
- Books: "Practical Statistics for Data Scientists" by Bruce & Gedeck
- Courses: Coursera "Data Science Specialization"
- Practice: Kaggle competitions and datasets
- Communities: r/datascience, Towards Data Science

### First Project
Analyze personal spending or fitness data:
- Export data from your bank or fitness app
- Clean and explore the dataset
- Identify patterns and trends
- Create visualizations
- Write up key insights and recommendations

## Quick Reference Card

### Common Statistical Tests
- **t-test**: Compare two means
- **ANOVA**: Compare 3+ means
- **Chi-square**: Test independence of categorical variables
- **Pearson correlation**: Linear relationship between continuous variables
- **Spearman correlation**: Monotonic relationship (rank-based)
- **Linear regression**: Predict continuous outcome
- **Logistic regression**: Predict binary outcome

### Data Visualization Types
- **Trends over time**: Line chart
- **Comparisons**: Bar chart, column chart
- **Proportions**: Pie chart (limited categories), stacked bar
- **Relationships**: Scatter plot, bubble chart
- **Distributions**: Histogram, box plot, violin plot
- **Flows**: Sankey diagram, funnel chart
- **Geographic**: Map, choropleth

### Key Formulas
- Mean: μ = Σx / n
- Standard Deviation: σ = √(Σ(x - μ)² / n)
- Correlation: r = Σ((x - x̄)(y - ȳ)) / √(Σ(x - x̄)² × Σ(y - ȳ)²)
- Confidence Interval: x̄ ± z × (σ / √n)

### Red Flags in Analysis
- Sample size too small
- Non-random sampling
- Missing data > 20%
- Extreme outliers not investigated
- Multiple comparisons without adjustment
- Results contradict domain knowledge

## Mastery Tips

1. **Ask Better Questions**: The quality of insights depends on the quality of questions
2. **Know Your Data**: Spend time understanding data collection and limitations
3. **Visualize Early**: Create plots before formal analysis to spot issues
4. **Embrace Uncertainty**: Always quantify and communicate uncertainty
5. **Tell Stories**: Frame insights as narratives that drive action
6. **Stay Curious**: Dig deeper when results are surprising
7. **Collaborate**: Work with domain experts and other analysts
8. **Keep Learning**: Statistics and tools evolve continuously

## Related Skills

- **Database Design** - Structuring data for analysis
- **Data Engineering** - Building data pipelines
- **Machine Learning** - Predictive modeling techniques
- **Business Intelligence** - Reporting and dashboards
- **Statistics** - Mathematical foundation for analysis
- **Data Visualization** - Communicating insights visually
- **Critical Thinking** - Evaluating evidence and arguments

---

*This skill document is part of the Skills Repository. For more skills, visit the main repository.*
