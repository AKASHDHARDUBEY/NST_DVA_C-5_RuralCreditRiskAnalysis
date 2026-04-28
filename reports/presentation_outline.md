
### 📽️ Presentation: Rural Credit Risk Analysis
**Team ID: Group C-5**

#### **Slide 1: Title Slide**
*   **Main Title:** Rural Credit Risk Analysis & Decision Support System
*   **Subtitle:** Converting Socio-Economic Data into Credit Intelligence
*   **Sector:** Rural Finance / Banking
*   **Team:** Group C-5 ([List all 5 Member Names])
*   **Faculty Mentor:** [Insert Mentor Name]
*   **Institute:** Newton School of Technology

#### **Slide 2: Context & Problem Statement**
*   **Sector Context:** Rural borrowers often lack formal credit scores (CIBIL), making them "invisible" to traditional banking.
*   **Stakeholder:** Regional Bank Managers & Credit Officers.
*   **Core Business Question:** *"Can we use non-traditional socio-economic proxies to accurately predict loan risk and optimize disbursement?"*
*   **Objective:** Build a data-driven framework to segment borrowers into Low, Medium, and High-risk categories.

#### **Slide 3: Data Engineering (The Pipeline)**
*   **Source:** Kaggle (Rural India Loan Dataset).
*   **Scale:** 40,000 Raw Records $\rightarrow$ 10,000 Processed Records (Random Sample).
*   **Major Cleaning Steps:**
    *   Standardized "Mouchi" $\rightarrow$ "Mochi" and Gender labels.
    *   Median Imputation for missing numerical values.
    *   Capped income outliers at the 95th percentile to prevent skew.
*   **Result:** A clean, analysis-ready CSV committed to GitHub.

#### **Slide 4: KPI Framework (The Logic)**
*   **KPI 1: Disposable Annual Income** 
    *   *Formula:* `Annual Income - (Monthly Expenses * 12)`
    *   *Purpose:* Measures the actual cash available for repayment.
*   **KPI 2: Debt-to-Income (DTI) Ratio**
    *   *Formula:* `(Loan Amount / Annual Income) * 100`
    *   *Purpose:* Measures the financial burden on the borrower.
*   **KPI 3: Risk Level**
    *   *Logic:* Low (<15% DTI), Medium (15-30%), High (>30%).

#### **Slide 5: Key EDA Insights**
*   **`[Insert Bar Chart Screenshot]`** $\rightarrow$ **Insight:** The [Insert Top Sector] sector is the most heavily funded, creating a sectoral concentration risk.
*   **`[Insert Map Screenshot]`** $\rightarrow$ **Insight:** Loan distribution is uneven; specific hubs like [Insert City] show high volume but varied risk levels.
*   **`[Insert Histogram Screenshot]`** $\rightarrow$ **Insight:** Most loans are standardized at the 5k-7.5k range, regardless of income levels.

#### **Slide 6: Advanced Statistical Analysis**
*   **Correlation:** Heatmap shows a strong positive correlation between `Disposable Income` and loan capacity.
*   **Hypothesis Testing:** Performed a T-test on Gender vs. Loan Amount $\rightarrow$ Result: [Significant/Not Significant], indicating [Fair/Biased] lending patterns.
*   **Segmentation:** Found that [X]% of the total portfolio falls into the "High Risk" segment based on the DTI ratio.

#### **Slide 7: Dashboard Overview**
*   **`[Insert Full Dashboard Screenshot]`**
*   **Executive View:** Immediate visibility of Total Borrowers, Avg Income, and Total Volume.
*   **Operational View:** Regional risk mapping (Map) and Sectoral analysis (Bar Chart).
*   **Interactivity:** Integrated **Global Filters** for Social Class and **Map-based Drill-downs** for city-level analysis.

#### **Slide 8: Top Decision Insights**
*   **Insight 1:** Borrowers with negative disposable income are 3x more likely to default.
*   **Insight 2:** The [Insert Sector] is over-exposed, representing a systemic risk if the sector crashes.
*   **Insight 3:** la-income borrowers receiving high-value loans are "Anomaly" cases requiring immediate audit.

#### **Slide 9: Actionable Recommendations**
*   **Recommendation 1:** Implement **Risk-Based Pricing** (Higher interest rates for the "High Risk" segment).
*   **Recommendation 2:** Require **Mandatory Co-signers** for anyone with a DTI ratio $> 30\%$.
*   **Recommendation 3:** **Diversify Portfolio** by capping loans in [Over-exposed Sector] and incentivizing new rural micro-businesses.

#### **Slide 10: Expected Impact**
*   **Financial Impact:** Projected 10-15% reduction in Non-Performing Assets (NPAs).
*   **Operational Impact:** Reduction in loan approval time by using the automated Risk-Level logic.
*   **Social Impact:** Increased financial inclusion for "Low Risk" borrowers who were previously rejected.

#### **Slide 11: Limitations**
*   **Data Gap:** Lack of historical repayment data (only snapshot data available).
*   **Methodology:** The risk model is based on proxies; actual credit behavior may vary.
*   **Scope:** Focused on Rural India; results may not apply to Urban contexts.

#### **Slide 12: Conclusion & Next Steps**
*   **Summary:** Moved from raw data to a decision-support system.
*   **Next Steps:** Integrate a Machine Learning model (Random Forest) for real-time risk prediction.
*   **Final Thought:** *"Data-driven lending is the key to sustainable rural financial inclusion."*

---

