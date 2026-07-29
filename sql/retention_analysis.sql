-- countries that have lost highest acc balance 
SELECT
    geography,
    COUNT(*) AS churned_customers,
    ROUND(SUM(balance), 2) AS total_balance_lost,
    RANK() OVER (
        ORDER BY SUM(balance) DESC
    ) AS balance_loss_rank
FROM customers
WHERE exited = 1
GROUP BY geography;

--comparison of avg salary & avg balance who stayed and left
SELECT
    CASE
        WHEN exited = 1 THEN 'Churned'
        ELSE 'Retained'
    END AS customer_status,
    COUNT(*) AS customers,
    ROUND(AVG(balance), 2) AS avg_balance,
    ROUND(AVG(estimated_salary), 2) AS avg_estimated_salary
FROM customers
GROUP BY customer_status;

--classify customers into value segments
SELECT 
    CASE 
        WHEN balance = 0 THEN 'No Value'
        WHEN balance < 50000 THEN 'Low Value'
        WHEN balance < 100000 THEN 'Medium Value'
        WHEN balance < 150000 THEN 'High Value'
        ELSE 'Premium'
    END AS value_segment,
    COUNT(*) AS customer_count
FROM customers GROUP BY value_segment ORDER BY customer_count DESC;


--segment with highest churn
SELECT
    CASE
        WHEN balance = 0 THEN 'No Value'
        WHEN balance < 50000 THEN 'Low Value'
        WHEN balance < 100000 THEN 'Medium Value'
        WHEN balance < 150000 THEN 'High Value'
        ELSE 'Premium'
    END AS value_segment,
    COUNT(*) AS churned_customers
FROM customers
WHERE exited = 1
GROUP BY value_segment
ORDER BY churned_customers DESC;

--customers who churn are above avg or below avg
SELECT 
    CASE    
        WHEN estimated_salary > (
            SELECT AVG(estimated_salary) FROM customers) THEN 'Above average'
            ELSE 'Below average'
    END AS sal_group,
    COUNT(*) AS churned_customers 
FROM customers WHERE exited = 1 GROUP BY sal_group;

