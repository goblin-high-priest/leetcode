-- Write your PostgreSQL query statement below
SELECT
    DISTINCT num AS ConsecutiveNums
FROM (
    SELECT
        num,
        LAG(num, 1) OVER (ORDER BY id) AS prev1,
        LAG(num, 2) OVER (ORDER BY id) AS prev2
    FROM
        Logs
)
WHERE num = prev1 AND prev1 = prev2