/*
Table: Employee
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference column) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.


Table: Department
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of a department and its name.

A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.
Write a solution to find the employees who are high earners in each of the departments.
Return the result table in any order.
The result format is in the following example.

Example 1:
Input:
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
Output:
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Joe      | 85000  |
| IT         | Randy    | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+
Explanation:
In the IT department:
- Max earns the highest unique salary
- Both Randy and Joe earn the second-highest unique salary
- Will earns the third-highest unique salary

In the Sales department:
- Henry earns the highest salary
- Sam earns the second-highest salary
- There is no third-highest salary as there are only two employees

Constraints:
There are no employees with the exact same name, salary and department.
*/

--  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! NOT SOLUTION  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-- This does NOT work
# Write your MySQL query statement below
WITH TopSalaries AS (
    SELECT
        departmentId,
        salary
    FROM
        (SELECT
            DISTINCT departmentId,
            salary
        FROM
            Employee
        ORDER BY departmentId ASC, salary DESC
        ) as distinct_dept_sals
        GROUP BY departmentId, salary
        HAVING COUNT(*) <= 3  -- doesn't do what we want — it just counts salary occurrences (not ranks). So we need a better version
)

SELECT
    d.name as Department,
    e.name as Employee,
    e.salary as Salary
FROM
    Employee e
JOIN
    Department d
ON e.departmentId = d.id
JOIN
    TopSalaries ts
ON d.id = ts.departmentId
AND e.salary = ts.salary

-- ================================================ SOLUTION 1 ======================================================================================
WITH DepartmentTopSalaries AS(
    SELECT
        e1.departmentId,
        e1.salary
    FROM
        Employee e1
    JOIN
        Employee e2
    ON e1.departmentId = e2.departmentId
    AND e1.salary <= e2.salary -- For every (departmentId, salary) in e1, we join it to all e2 rows in the same department where e2.salary >= e1.salary
    -- This creates a group where e1.salary is less than or equal to some number of salaries
    GROUP BY
        e1.departmentId, e1.salary
    HAVING COUNT(DISTINCT e2.salary) <= 3 -- count how many DISTINCT e2.salary values are greater than or equal to e1.salary
    -- If that count is ≤ 3, that means the salary is in the top 3 unique salaries in the department
)

SELECT
    d.name as Department,
    e.name as Employee,
    e.salary as Salary
FROM
    Employee e
JOIN
    Department d
ON e.departmentId = d.id
JOIN
    DepartmentTopSalaries dts
ON dts.departmentId = e.departmentId
AND e.salary = dts.salary

-- ================================================ SOLUTION 2 ======================================================================================

-- distinct salaries greater than the current one is less than 3 — meaning it's in the top 3
WITH TopSalaries AS (
    SELECT e1.departmentId, e1.salary
    FROM Employee e1
    WHERE (
        SELECT COUNT(DISTINCT e2.salary)
        FROM Employee e2
        WHERE e2.departmentId = e1.departmentId
          AND e2.salary > e1.salary
    ) < 3
)

SELECT
    DISTINCT d.name AS Department, -- remove duplicates caused by the join
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
JOIN TopSalaries ts
  ON e.departmentId = ts.departmentId
 AND e.salary = ts.salary

-- ================================================ SOLUTION 3 ======================================================================================
-- Window's function

WITH cte AS(
    SELECT
        departmentId,
        name as Employee,
        salary,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) as rnk_sal
    FROM
        Employee
)

SELECT
    d.name AS Department,
    c.Employee,
    c.Salary
FROM
    cte c
JOIN
    Department d
ON c.departmentId = d.id
WHERE c.rnk_sal <= 3

-- ================================================ SOLUTION 4 ======================================================================================
-- Advance - Return NULL if the table has no records.
-- Window's function + union

WITH cte AS (
    SELECT
        departmentId,
        name AS Employee,
        salary,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rnk_sal
    FROM
        Employee
)

SELECT
    d.name AS Department,
    c.Employee,
    c.Salary
FROM
    cte c
JOIN
    Department d ON c.departmentId = d.id
WHERE
    c.rnk_sal <= 3

UNION ALL

SELECT
    NULL AS Department,
    NULL AS Employee,
    NULL AS Salary
WHERE NOT EXISTS (
    SELECT 1 FROM Employee
)
