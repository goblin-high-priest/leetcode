CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    SELECT 
        MAX(r.salary)
    FROM (
        SELECT
            e.salary,
            DENSE_RANK() OVER (ORDER BY e.salary DESC) AS rnk
        FROM 
            Employee e
    ) AS r
    WHERE rnk = N
  );
END;
$$ LANGUAGE plpgsql;