# Bank-Customer-Churn-Analysis
Customer churn is one of the biggest challenges for banks because acquiring a new customer costs significantly more than retaining an existing one. This project analyzes customer demographics, banking behavior, and account information to identify the key drivers behind customer attrition and uncover opportunities to improve customer retention.

**Why are customers leaving the bank, and what actions can reduce churn?**

The project follows the following workflow:

* Data Cleaning & Validation
* Feature Engineering
* Exploratory Data Analysis (EDA)
* SQL Business Analysis
* Interactive Power BI Dashboard

This project focuses on answering the following business question-


## Dataset

**Source:** Kaggle – Bank Customer Churn Prediction Dataset

The dataset contains customer information including:

* Demographics
* Geography
* Credit Score
* Account Balance
* Tenure
* Number of Products
* Active Membership
* Credit Card Status
* Estimated Salary
* Churn Status



## Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SQLite
* Power BI
* Git & GitHub


## Project Workflow

### 1. Data Cleaning

* Removed unnecessary columns
* Checked missing values
* Verified data quality
* Standardized data types
* Prepared an analysis-ready dataset


### 2. Feature Engineering

Created business-focused features including:

* Age Groups
* Balance Categories
* Customer Segments
* Churn Rate Metrics

These features made customer behavior easier to interpret from a business perspective.

### 3. Exploratory Data Analysis

Analyzed relationships between churn and:

* Age
* Geography
* Balance
* Credit Score
* Active Membership
* Number of Products
* Tenure
* Gender

Visualizations included:

* Histograms
* Count Plots
* Box Plots
* Correlation Heatmap
* Churn Rate Comparisons


### 4. SQL Business Analysis

Built reusable SQLite views for Power BI:

* **vw_executive_kpis**
* **vw_customer_segments**
* **vw_retention_analysis**
* **vw_country_performance**

These views aggregate KPIs and customer segments to support dashboard reporting.


### 5. Power BI Dashboard

The dashboard presents:

* Executive KPIs
* Customer Segmentation
* Retention Analysis
* Country Performance
* Interactive slicers and drill-downs

---

# Key Business Insights

### Age is the strongest churn indicator.

Customers in the 41–50 age group exhibited significantly higher churn rates compared to younger customers, suggesting a need for targeted retention strategies for mid-career customers.

---

### Active customers are much less likely to leave.

Inactive members churn substantially more often than active members, indicating that increasing customer engagement can directly improve retention.

---

### Geography influences customer retention.

Churn varies across different countries, highlighting opportunities for region-specific customer experience and marketing initiatives.

---

### Product ownership impacts loyalty.

Customers with fewer banking products tend to churn more frequently, suggesting that cross-selling additional services could improve long-term retention.

---

### High account balances do not guarantee loyalty.

Customers with larger balances still leave the bank, indicating that financial value alone does not ensure retention and that engagement and service quality also matter.

---

# Business Recommendations

* Develop targeted retention campaigns for high-risk age groups.
* Increase engagement initiatives for inactive customers.
* Promote cross-selling to customers with fewer products.
* Design region-specific retention strategies.
* Monitor churn KPIs through interactive dashboards for continuous decision-making.

This project demonstrates an end-to-end data analytics workflow, transforming raw banking data into business insights using Python, SQL, SQLite, and Power BI. The resulting dashboard enables stakeholders to monitor churn trends, identify at-risk customer segments, and support data-driven retention strategies.
