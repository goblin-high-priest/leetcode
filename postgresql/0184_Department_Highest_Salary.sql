-- Write your PostgreSQL query statement below
WITH HighestSalary AS (
    SELECT
        MAX(salary) AS max_sal, departmentId
    FROM
        Employee 
    GROUP BY 
        departmentId
)
SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM
    HighestSalary h,
    Department d,
    Employee e
WHERE
    h.departmentId = d.id 
    AND h.max_sal = e.salary
    AND h.departmentId = e.departmentId