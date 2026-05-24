# End-to-End Insurance Risk Analytics & Predictive Modeling

## Project Overview
This project is part of the **10 Academy: Artificial Intelligence Mastery (Week 3 Challenge)**. Working as a Marketing Analytics Engineer for **AlphaCare Insurance Solutions (ACIS)**, the goal is to analyze historical car insurance claim data from South Africa to identify low-risk segments and build a dynamic, risk-based pricing system.

## Business Need
ACIS aims to optimize marketing investments and refine pricing models by moving from intuition-based decisions to data-driven insights. This project focuses on:
- **Loss Ratio:** (TotalClaims / TotalPremium) - Measuring portfolio profitability.
- **Margin:** (TotalPremium - TotalClaims) - Measuring per-policy profit contribution.

---

## Task 1: Exploratory Data Analysis (EDA)
The analysis was performed on a dataset of **10,000 rows** and **21 columns**.

### 1. Data Quality Assessment
- **Missing Values:** The dataset is highly complete with **0 missing values** across all features.
- **Data Types:** Numerical and categorical columns were correctly typed; `TransactionDate` was converted to datetime for trend analysis.
- **Outliers:** Significant outliers were identified in `TotalClaims` (Maximum value of 49,623) and `CustomValueEstimate`.

### 2. Key Insights & Risk Drivers
- **Geographic Trends:** 
    - **Somali** province exhibits the highest risk, with the highest average `TotalPremium` (~2,521) and `TotalClaims` (~1,542).
    - **Amhara** province is the lowest risk segment with the lowest average claim amounts (~1,177).
- **Gender Analysis:** **Females** have a slightly higher Loss Ratio (**44.7%**) compared to **Males** (**43.8%**).
- **Vehicle Type:** **Luxury** vehicles represent a high-risk segment with a Loss Ratio of **80.4%**, while **Sedans** (34.8%) and **Hatchbacks** (37.1%) are significantly more profitable.
- **Vehicle Makes:** Claims are highest for **Mercedes-Benz** and **BMW**, while **Lifan** and **Hyundai** show the lowest claim severity.
- **Correlation:** A strong positive correlation (**0.82**) exists between `RiskScore` and `TotalPremium`, suggesting the current pricing model is heavily weighted on risk scores.

### 3. Visualizations
- **Premium Distribution:** Shows a bimodal distribution, indicating two distinct pricing tiers within the portfolio.
- **Monthly Trends:** Claim frequencies show volatility with a significant dip in April 2025.

---

## Task 2: Data Version Control (DVC)
To ensure reproducibility and meet regulatory audit requirements, DVC was implemented:
- **Initialization:** DVC was initialized and linked to a local remote storage.
- **Tracking:** The `insurance_data.csv` file is tracked by DVC, while Git only tracks the `.dvc` metadata.
- **Versioning:** Enabled easy switching between raw and cleaned data versions without bloating the Git history.

---

## Project Structure
```text
insurance-risk-analytics/
├── .github/workflows/      # CI/CD (GitHub Actions for linting/testing)
├── data/                   # Data directory (tracked by DVC)
├── notebooks/              # Jupyter Notebooks
│   └── 01_eda.ipynb        # Comprehensive EDA & Visualizations
├── src/                    # Reusable source code
│   ├── data_loader.py      # Script to load data
│   └── eda_utils.py        # Utility functions for plotting and analysis
├── .dvc/                   # DVC configuration files
├── .gitignore              # Files to be ignored by Git (including raw data)
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation