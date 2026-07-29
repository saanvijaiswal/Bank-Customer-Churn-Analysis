--overall customer churn rate
SELECT COUNT(*) AS total_customers,
SUM(exited) AS churned_customers,
COUNT(*) - SUM(exited) AS retained_customers,
ROUND((SUM(exited)* 100.0) / COUNT(*),2) AS churn_rate_percent
FROM customers;


--profile of avg customer
SELECT ROUND(AVG(age), 1) AS avg_age,
ROUND(AVG(credit_score), 0) AS avg_credit_score,
ROUND(AVG(balance), 2) AS avg_balance,
ROUND(AVG(estimated_salary),2) AS avg_salary
FROM customers;

