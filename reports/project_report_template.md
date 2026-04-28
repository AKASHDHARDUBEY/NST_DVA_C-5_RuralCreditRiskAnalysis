FINAL PROJECT REPORT:
 Rural Credit Risk Analysis & Decision Support System

Course: Data Visualization & Analytics | Capstone 2
Sector: Rural Finance & Banking
Team ID: Group C-5
Institute: Newton School of Technology
Date: April 28, 2026

1. Cover Page

  - Project Title: Rural Credit Risk Analysis & Decision Support System
  - Sector: Finance / Rural Banking
  - Team Members: Akash Dhar Dubey, Abhishek varma, Anirudh Panigrahy
  - GitHub Repository: https://github.com/AKASHDHARDUBEY/NST_DVA_C-5_RuralCreditRiskAnalysis 
  

2. Executive Summary

Problem: Lending institutions in rural India struggle to assess creditworthiness
due to a lack of traditional credit scores, leading to high default risks.

Approach: We developed an end-to-end pipeline using Python for ETL and
statistical analysis, and Tableau for visualization. We transformed a raw
dataset of 40,000 records into a risk-segmented model. 

Key Insights: We identified that "Disposable Income" is a far more accurate predictor of
repayment than "Annual Income." We also found a high concentration of risk in
specific business sectors and high Debt-to-Income ratios (>30%).
 
Key Recommendations: Implementation of a tiered risk-based interest rate system and
mandatory co-signers for borrowers with negative disposable income.
 
3. Sector and Business Context

Sector Overview: Rural banking in India is characterized by a "credit gap."
Borrowers often operate in the informal economy (tailoring, small-scale farming,
etc.) and lack the documentation required for standard credit scoring.

Stakeholder: The primary decision-maker is the Regional Bank Manager or Credit
Officer who must decide whether to approve a loan and at what interest rate.

Business Value: By moving from intuition-based lending to a data-driven risk
framework, the bank can reduce Non-Performing Assets (NPAs) and increase the
safety of its loan portfolio.

4. Problem Statement and Objectives

Formal Definition: To analyze socio-economic proxies of rural borrowers to
identify the primary drivers of loan risk and create a segmentation model that
classifies borrowers into Low, Medium, and High-risk categories.

 Scope: The project covers data extraction from Kaggle, cleaning of raw records, statistical
correlation of risk factors, and the creation of a real-time interactive
dashboard. 

Success Criteria: A functional dashboard that allows a manager to
filter by city or social class and see the associated risk level.

5. Data Description

  - Source: Kaggle (Credit/Loan Dataset - Rural India).
  - Structure: Original dataset contained 40,000 rows and 21 columns.
  - Key Fields: Annual Income, Monthly Expenses, Loan Amount, Social Class,
    Primary Business, and Home Ownership.
  - Quality Issues: The raw data contained misspelled category labels (e.g.,
    "Mouchi" vs "Mochi"), missing values in income fields, and significant
    outliers in annual earnings.

6. Cleaning and Transformation

All transformations were executed in notebooks/02_cleaning.ipynb.

  - Standardization: Merged inconsistent social class labels and standardized
    gender entries to uppercase.
  - Missing Values: Numerical nulls were handled using Median Imputation to
    prevent outlier distortion. Categorical nulls were labeled as "Unknown."
  - Outlier Handling: Annual income was capped at the 95th percentile to prevent
    extreme values from skewing the average.
  - Feature Engineering: Created three critical business metrics:
    1.  Disposable Income (Annual Income - Yearly Expenses)
    2.  Debt-to-Income Ratio (Loan Amount / Annual Income)
    3.  Total Dependents (Old + Young Dependents)





7. KPI Framework

We developed three primary KPIs to measure borrower health:

1.  Disposable Annual Income: Measures the actual cash available for loan
    repayment.
2.  Debt-to-Income (DTI) Ratio: Measures the loan burden relative to earnings.
3.  Risk Level: A categorical segment (Low/Med/High) based on the DTI ratio.
    Logic: Logic is documented in notebooks/05_final_load_prep.ipynb.

8. Exploratory Data Analysis (EDA)


Insight: Loan amounts are clustered around specific product tiers (e.g., 5,000 and 7,500), suggesting a standardized product offering by the bank.


Insight: The  Tailoring sector has the highest loan volume, making the bank
highly exposed to this specific industry.


Insight: A significant number of low-income borrowers are receiving high-value loans, representing "Anomaly" loans that are high-risk.

9. Statistical Analysis

  - Correlation: A heatmap revealed a strong positive correlation between
    Disposable Income and loan capacity.

  - Hypothesis Testing: A T-test was performed to see if gender significantly
    impacted loan amounts. The result was "Statistically Significant" or
    "Not Significant", suggesting the bank's lending is [Fair/Biased].

  - Risk Segmentation: By applying the DTI ratio, we found that [70]% of the
    portfolio falls into the "High Risk" category.




10. Tableau Dashboard Design

Objective: To provide a "Single Source of Truth" for loan officers to evaluate
risk.

  - Executive View: Top-level KPIs (Total Borrowers, Avg Income, Total Loan
    Volume).
  - Operational View: A geographic map of India for regional risk and a sectoral
    bar chart for industry risk.
  - Interactivity: A "Global Filter" for Social Class and a Map-based Filter
    allows the user to drill down into specific cities.


11. Key Insights (Decision Language)

1.  Borrowers with a DTI ratio over 30% show a significantly higher probability
    of default.
2.  Disposable income is a more reliable predictor of repayment than gross
    annual income.
3.  The sector is over-represented in the portfolio, increasing
    systemic risk.
4.  pune has the highest concentration of high-risk loans.


12. Recommendations

1.  Risk-Based Pricing: Implement higher interest rates for the "High Risk"
    segment to offset potential losses.
2.  Collateral Requirements: Require mandatory co-signers for any borrower with
    negative disposable income.
3.  Portfolio Diversification: Reduce loan caps for the [Insert Sector] and
    incentivize loans for emerging rural sectors.

Expected Impact: A projected 10-15% reduction in Non-Performing Assets (NPAs)
within the first year.

13. Limitations and Next Steps

  - Limitations: The dataset is a snapshot; time-series data on actual repayment
    history would improve accuracy.
  - Future Scope: Develop a Predictive Machine Learning model (Logistic
    Regression) to automate the "Risk Level" assignment.

14. Contribution Matrix

| Member     | Dataset | ETL     | EDA     | Stats   | Tableau | Report  | PPT     |
| ---------- |    ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| Akash Dhar Dubey] | Owner   | Support | Support | Owner   | Support | Owner   | Owner   |
| \Anirudh Panigrahy] | Support | Owner   | Support | Support | Owner   | Support | Support |
| \Abhishek varma] | Support | Support | Owner   | Support | Support | Owner   | Support |

