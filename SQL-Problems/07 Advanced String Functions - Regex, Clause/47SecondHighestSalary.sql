/*
Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.

Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).
The result format is in the following example.

Example 1:
Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
Example 2:

Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
*/

-- ================================================ SOLUTION 1 =========================================================
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! This will NOT work for 3rd, 4th, 5th etc highest salary !!!!!!!!!!!!!!!!!!!!!!!!!!!!

SELECT
    COALESCE(
        (SELECT
            DISTINCT salary as SecondHighestSalary
        FROM
            Employee
        WHERE salary NOT IN (SELECT MAX(salary) as salary FROM Employee)
        ORDER BY salary DESC
        LIMIT 1),
        NULL
    )  AS SecondHighestSalary

-- ================================================ SOLUTION 2 =========================================================
-- Window's function

SELECT
    MAX(salary) as SecondHighestSalary -- MAX(salary) is used to wrap salary if it returns no rows(NULL rows) Example 2
FROM
    (SELECT
        DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk_sal,
        salary
    FROM
        Employee) as rnk
WHERE rnk_sal = 2

-- ================================================ SOLUTION 2 =========================================================
-- Window's function, return 0 instead of null in example 2

SELECT
    COALESCE(salary, 0) as SecondHighestSalary -- Handles rows(NULL rows) to return 0
FROM
    (SELECT
        DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk_sal,
        salary
    FROM
        Employee) as rnk
WHERE rnk_sal = 2