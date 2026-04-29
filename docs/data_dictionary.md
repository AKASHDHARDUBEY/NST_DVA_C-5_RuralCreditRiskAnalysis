

# Data Dictionary: Rural Credit Risk Analysis

This document provides a detailed map of the dataset used in the Capstone 2 project, including the original raw fields and the derived business metrics created during the ETL process.

## Dataset Summary

| Item | Details |
|---|---|
| **Dataset name** | Credit/Loan Dataset - Rural India |
| **Source** | Kaggle |
| **Raw file name** | `RuralCreditData.csv` |
| **Last updated** | April 2026 |
| **Granularity** | One row per individual borrower |

## Column Definitions

| Column Name | Data Type | Description | Example Value | Used In | Cleaning Notes |
|---|---|---|---|---|---|
| **city** | String | The city/district where the borrower resides | Dhanbad | EDA / Tableau | None |
| **age** | Int | Age of the borrower | 22 | EDA / Stats | None |
| **sex** | String | Gender of the borrower | F / M | EDA / Stats | Standardized to Uppercase |
| **social_class** | String | Socio-economic classification | Mochi | EDA / Tableau | Standardized 'Mouchi' $\rightarrow$ 'Mochi' |
| **primary_business** | String | Main source of income/occupation | Tailoring | EDA / Tableau | None |
| **secondary_business** | String | Additional income source | Others | EDA | None |
| **annual_income** | Float | Total earnings per year | 36000 | KPI / Stats | Outliers capped at 95th percentile |
| **monthly_expenses** | Float | Average monthly spending | 5000 | KPI / Stats | Nulls filled with Median |
| **old_dependents** | Int | Number of elderly dependents | 0 | KPI / Stats | None |
| **young_dependents** | Int | Number of child dependents | 2 | KPI / Stats | None |
| **home_ownership** | Int | Whether the borrower owns the home (1=Yes, 0=No) | 1 | EDA / Stats | None |
| **type_of_house** | String | Category of housing (e.g., R, T1) | T1 | EDA | None |
| **occupants_count** | Int | Total number of people living in the house | 4 | EDA | None |
| **house_area** | Float | Total area of the house in sq ft | 70 | EDA / Stats | None |
| **sanitary_avail** | Float | Availability of sanitary facilities (Binary) | 1 | EDA | None |
| **water_avail** | Float | Availability of water facilities (Binary) | 0.5 | EDA | Renamed from `water_availabity` |
| **loan_purpose** | String | Reason for taking the loan | Apparels | Tableau | None |
| **loan_tenure** | Int | Duration of the loan in months | 12 | EDA / Stats | None |
| **loan_installments** | Int | Number of installments paid/due | 12 | EDA | None |
| **loan_amount** | Float | Total principal amount of the loan | 5000 | KPI / Stats | Nulls filled with Median |

## Derived Columns

These columns were created in `02_cleaning.ipynb` to provide deeper business insights.

| Derived Column | Logic / Formula | Business Meaning |
|---|---|---|
| **disposable_income** | `annual_income - (monthly_expenses * 12)` | The actual cash left over for loan repayment. The most critical risk metric. |
| **loan_to_income_ratio**| `(loan_amount / annual_income) * 100` | Percentage of annual income taken as a loan. High ratio = High Risk. |
| **total_dependents** | `old_dependents + young_dependents` | Total family burden, which impacts the borrower's ability to pay. |
| **risk_level** | Logic based on `loan_to_income_ratio` | Categorizes borrowers into Low, Medium, or High risk for the bank. |

## Data Quality Notes

- **Typo Correction:** The raw column `water_availabity` was misspelled and was renamed to `water_availability` for consistency.
- **Label Standardization:** The `social_class` column contained inconsistent entries (`Mochi` and `Mouchi`); these were merged into a single category.
- **Outlier Handling:** `annual_income` contained extreme values that would distort the average; these were capped at the 95th percentile using a clipping method.
- **Missing Data:** Numerical nulls were imputed using the **Median** to avoid the influence of outliers, and categorical nulls were labeled as **'Unknown'**.
- **Sampling:** The original dataset of 40,000 rows was randomly sampled down to 10,000 rows to ensure computational efficiency in Tableau while maintaining statistical representation.

***

