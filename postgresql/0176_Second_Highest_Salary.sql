-- Write your PostgreSQL query statement below

-- Approach_1: Window Function
SELECT 
    MAX(salary) AS SecondHighestSalary
FROM (
    SELECT 
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM Employee
) AS ranked
WHERE rnk = 2;

-- Approach_2: With Clause
-- WITH SecondHighest AS (
--     SELECT DISTINCT salary
--     FROM Employee
--     ORDER BY salary DESC
--     LIMIT 1 OFFSET 1
-- )
-- SELECT 
--     MAX(salary) AS SecondHighestSalary
-- FROM SecondHighest;