--creating views to import into power bi
CREATE VIEW vw_executive_kpis AS 
SELECT
    COUNT(*) AS total_customers, 
    SUM(exited) AS churned_customers,
    COUNT(*) - SUM(exited) AS retained_customers,
    ROUND(100.0 * SUM(exited) / COUNT(*), 2) AS churn_rate,
    ROUND(AVG(age), 2) AS avg_age,
    ROUND(AVG(balance), 2) AS avg_balance,
    ROUND(AVG(credit_score), 2) AS avg_credit_score,
    ROUND(AVG(estimated_salary), 2) AS avg_estimated_salary
FROM customers;

CREATE VIEW vw_customer_segments AS
SELECT
    geography,
    age,
    balance,
    estimated_salary,
    num_products,
    exited,
    CASE
        WHEN balance = 0 THEN 'No Value'
        WHEN balance < 50000 THEN 'Low Value'
        WHEN balance < 100000 THEN 'Medium Value'
        WHEN balance < 150000 THEN 'High Value'
        ELSE 'Premium'
    END AS value_segment
FROM customers;

CREATE VIEW vw_retention_analysis AS
SELECT
    geography,
    gender,
    age,
    balance,
    estimated_salary,
    num_products,
    is_active_member,
    CASE
        WHEN exited = 1 THEN 'Churned'
        ELSE 'Retained'
    END AS customer_status
FROM customers;

CREATE VIEW vw_country_performance AS
SELECT
    geography,
    COUNT(*) AS total_customers,
    SUM(exited) AS churned_customers,
    ROUND(100.0 * SUM(exited) / COUNT(*), 2) AS churn_rate,
    ROUND(AVG(balance), 2) AS avg_balance,
    ROUND(AVG(estimated_salary), 2) AS avg_estimated_salary
FROM customers
GROUP BY geography;