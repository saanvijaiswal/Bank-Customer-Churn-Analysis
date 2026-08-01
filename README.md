# Bank-Customer-Churn-Analysis
Customer churn is one of the biggest challenges for banks because acquiring a new customer costs significantly more than retaining an existing one. This project analyzes customer demographics, banking behavior, and account information to identify the key drivers behind customer attrition and uncover opportunities to improve customer retention.

**Why are customers leaving the bank, and what actions can reduce churn?**

The project follows the following workflow:

* Data Cleaning & Validation -> Python
* Feature Engineering -> Python
* Exploratory Data Analysis (EDA) -> Python
* SQL Business Analysis -> SQLite
* Interactive Power BI Dashboard -> Power BI

## Dataset

**Source:** Kaggle – Bank Customer Churn Prediction Dataset

The dataset contains 10,000 customer records including:

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

Correlation Matrix-
<img width="1536" height="752" alt="image" src="https://github.com/user-attachments/assets/b4c48895-2982-42bd-b242-d656c26f2cbc" />

Age Distribution Box Plot
<img width="1255" height="835" alt="image" src="https://github.com/user-attachments/assets/0498496c-9c17-465a-aff6-30eff753c2bc" />


### 4. SQL Business Analysis

Built reusable SQLite views for Power BI:

* **vw_executive_kpis**
* **vw_customer_segments**
* **vw_retention_analysis**
* **vw_country_performance**

These views aggregate KPIs and customer segments to support dashboard reporting.
Along with that, further analysis uncovered a few interesting insights-
**Were the churned customers above-average or below-average customers? Our analysis shows that the majority of them were above average.**
<img width="397" height="170" alt="image" src="https://github.com/user-attachments/assets/b52e072f-83f3-4732-9c44-56be6a8149e0" />

**Total Balance lost by countries ranked**
<img width="715" height="177" alt="image" src="https://github.com/user-attachments/assets/bb6f8b29-f917-4b62-a82f-42c2e448dd73" />



### 5. Power BI Dashboard

The dashboard presents:

* Executive KPIs
* Customer Segmentation
* Retention Analysis
* Country Performance
* Interactive slicers and drill-downs

Customer Value Page
<img width="1167" height="642" alt="image" src="https://github.com/user-attachments/assets/709ffd10-9373-489d-90ad-5c995d581c2d" />

Executive Overview Page
<img width="1162" height="652" alt="image" src="https://github.com/user-attachments/assets/c0f11a93-a16e-4f2c-a7ec-51fa91e60aec" />

Retention Analysis Page
<img width="1172" height="652" alt="image" src="https://github.com/user-attachments/assets/55725c05-9716-497a-930f-3a9e2a90e22c" />


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
