-- Write your PostgreSQL query statement below
WITH TopThreeSalary AS (
    SELECT
        name,
        departmentId,
        salary,
        DENSE_RANK() OVER (
            PARTITION BY departmentID 
            ORDER BY salary DESC
        ) AS rnk
    FROM 
        Employee
)
SELECT 
    d.name AS Department,
    t.name AS Employee,
    t.salary AS Salary
FROM TopThreeSalary t
JOIN Department d
    ON t.departmentId = d.id
WHERE 
    t.rnk <= 3