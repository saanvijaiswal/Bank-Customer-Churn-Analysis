--customer distribution 
/*SELECT
    CASE
        WHEN balance = 0 THEN 'No Balance'
        WHEN balance < 50000 THEN 'Low Value'
        WHEN balance < 100000 THEN 'Medium Value'
        WHEN balance < 150000 THEN 'High Value'
        ELSE 'Premium'
    END AS customer_segment,
    COUNT(*) AS total_customers,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM customers), 2) AS percentage
FROM customers
GROUP BY customer_segment
ORDER BY total_customers DESC;
*/

/*
--customer value segment that has highest churn
SELECT
    CASE
        WHEN balance = 0 THEN 'No Balance'
        WHEN balance < 50000 THEN 'Low Value'
        WHEN balance < 100000 THEN 'Medium Value'
        WHEN balance < 150000 THEN 'High Value'
        ELSE 'Premium'
    END AS customer_segment,
    COUNT(*) AS total_customers,
    SUM(exited) AS churned_customers,
    ROUND(SUM(exited) * 100.0 / COUNT(*), 2) AS churn_rate
FROM customers
GROUP BY customer_segment
ORDER BY churn_rate DESC;
*/

--high value/premium customers who churned
SELECT COUNT(*) AS high_value_churned_customers FROM customers WHERE exited = 1 AND balance > (SELECT AVG(balance) FROM customers);


--geography with high number of customers lost
SELECT geography, gender, age, balance, num_products, is_active_member
FROM customers
WHERE exited = 0 AND is_active_member = 0 AND balance > (SELECT AVG(balance) FROM customers)
ORDER BY balance DESC;

--avg balance and salary of high value customers who left
SELECT
    geography,
    COUNT(*) AS high_value_churned_customers,
    ROUND(AVG(balance), 2) AS avg_balance,
    ROUND(AVG(estimated_salary), 2) AS avg_estimated_salary
FROM customers
WHERE exited = 1
  AND balance > (
      SELECT AVG(balance)
      FROM customers
  )
GROUP BY geography
ORDER BY avg_balance DESC;
