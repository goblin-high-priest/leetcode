-- Write your PostgreSQL query statement below
WITH BannedUsers AS (
    SELECT 
        users_id
    FROM 
        Users
    WHERE 
        banned = 'Yes'
)
SELECT
    request_at AS "Day",
    ROUND(SUM(CASE WHEN status != 'completed' THEN 1 ELSE 0 END) * 1.0 / COUNT(*), 2) AS "Cancellation Rate"
FROM
    Trips
WHERE
    driver_id NOT IN (SELECT users_id FROM BannedUsers)
    AND client_id NOT IN (SELECT users_id FROM BannedUsers)
    AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY
    request_at
ORDER BY
    request_at
