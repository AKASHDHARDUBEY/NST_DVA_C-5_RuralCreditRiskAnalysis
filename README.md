# 📊 Rural Credit Risk Analysis & Decision Support System
### NST DVA Capstone 2 | Group C-5

> **Newton School of Technology | Data Visualization & Analytics**
> A professional industry simulation converting raw rural financial data into actionable business intelligence using Python and Tableau.

---

## 📌 Project Overview
This project addresses the challenge of financial inclusion in rural India. Because many rural borrowers lack traditional credit scores, lending institutions struggle to assess risk accurately. 

Our team developed an end-to-end analytical pipeline to identify socio-economic markers—such as disposable income, home ownership, and business sector—that correlate with creditworthiness. The final output is an interactive Tableau dashboard designed for bank managers to make data-driven loan approval decisions.

## 🎯 Business Problem Statement
**The Challenge:** Traditional credit scoring is unavailable for a large portion of the rural population, leading to either high default rates or unfair loan rejections.

**Core Business Question:** Which non-traditional socio-economic factors are the strongest predictors of loan risk, and how can we segment borrowers to optimize the loan disbursement process?

**Decision Supported:** This project enables stakeholders to move from "intuition-based" lending to "evidence-based" lending by using a tiered risk-approval framework based on the **Debt-to-Income Ratio** and **Disposable Income**.

## 🛠️ Technical Stack
- **Language:** Python 3.11+
- **ETL & Analysis:** Pandas, NumPy, SciPy (Statistical Testing)
- **Visualization:** Tableau Public (Interactive Dashboard)
- **Version Control:** GitHub (Structured branching and PR workflow)
- **Environment:** Jupyter Notebooks / VS Code

## ⚙️ Data Pipeline (ETL)
The project follows a rigorous industry-standard ETL process to ensure data integrity:
1. **Extraction:** Ingested raw data (`RuralCreditData.csv`) from Kaggle.
2. **Transformation:** 
   - **Standardization:** Fixed inconsistent labels (e.g., merged 'Mouchi' into 'Mochi').
   - **Data Quality:** Handled missing values via Median Imputation and capped income outliers at the 95th percentile.
   - **Feature Engineering:** Created high-value business metrics: `Disposable Income`, `Debt-to-Income Ratio`, and `Risk Level`.
3. **Loading:** Randomly sampled the dataset to 10,000 rows to optimize performance for the Tableau Public cloud environment.

## 📁 Repository Structure
```text
NST_DVA_C-5_RuralCreditRiskAnalysis/
├── data/
│   ├── raw/                
│   └── processed/          
├── notebooks/
│   ├── 01_extraction.ipynb      
│   ├── 02_cleaning.ipynb       
│   ├── 03_eda.ipynb             
│   ├── 04_statistical_analysis.ipynb 
│   └── 05_final_load_prep.ipynb 
├── scripts/
│   ├── etl_pipeline.py          
│   └── __init__.py              
├── tableau/
│   ├── screenshots/            
│   └── dashboard_links.md     
├── docs/
│   └── data_dictionary.md      
└── reports/
    ├── project_report.pdf       
    └── presentation.pdf         


👥 Team C-5 & Contribution Matrix
Name	   Role	Key         Contribution	                      GitHub Profile
[AKASH DHAR DUBEY]	Project Lead	Problem Framing & Statistical Analysis	[@AKASHDHARDUBEY]
[Anirudh Panigrahy]	ETL Engineer	Data Cleaning & Pipeline Automation	[@Anirudh-020505]
[Abhishek varma]	Data Analyst	EDA & Insight Generation	[@it-is-Abhishek]

📈 Key Findings & Recommendations
Major Insights

Income Correlation: There is a strong positive correlation between Disposable Income and loan repayment capacity.
Risk Markers: Borrowers with a Debt-to-Income Ratio exceeding 30% are categorized as "High Risk."
Sectoral Trends: The  sector has the highest loan volume, but exhibits higher volatility in repayment.
Geographic Insight: Loan disbursement is heavily concentrated in specific rural hubs, suggesting an opportunity for expansion.

Actionable Recommendations
Tiered Interest Rates: Implement a risk-based pricing model where borrowers in the "High Risk" segment are charged a higher interest rate to offset potential defaults.
Collateral Requirement: Require mandatory co-signers or physical collateral for loans where Disposable Income is negative.
Sector Diversification: Reduce exposure to the [Insert Top Sector] and incentivize loans for emerging rural micro-businesses.

🔗 Final Deliverables

Project Report: Available in /reports/project_report.pdf
Data Dictionary: Available in /docs/data_dictionary.md
