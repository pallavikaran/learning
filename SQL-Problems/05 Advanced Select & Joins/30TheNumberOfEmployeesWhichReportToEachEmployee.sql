/*
Table: Employees
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| reports_to  | int      |
| age         | int      |
+-------------+----------+
employee_id is the column with unique values for this table.
This table contains information about the employees and the id of the manager they report to. Some employees do not report to anyone (reports_to is null).
For this problem, we will consider a manager an employee who has at least 1 other employee reporting to them.

Write a solution to report the ids and the names of all managers, the number of employees who report directly to them, and the average age of the reports rounded to the nearest integer.
Return the result table ordered by employee_id.
The result format is in the following example.

Example 1:
Input:
Employees table:
+-------------+---------+------------+-----+
| employee_id | name    | reports_to | age |
+-------------+---------+------------+-----+
| 9           | Hercy   | null       | 43  |
| 6           | Alice   | 9          | 41  |
| 4           | Bob     | 9          | 36  |
| 2           | Winston | null       | 37  |
+-------------+---------+------------+-----+
Output:
+-------------+-------+---------------+-------------+
| employee_id | name  | reports_count | average_age |
+-------------+-------+---------------+-------------+
| 9           | Hercy | 2             | 39          |
+-------------+-------+---------------+-------------+
Explanation: Hercy has 2 people report directly to him, Alice and Bob. Their average age is (41+36)/2 = 38.5, which is 39 after rounding it to the nearest integer.
Example 2:

Input:
Employees table:
+-------------+---------+------------+-----+
| employee_id | name    | reports_to | age |
|-------------|---------|------------|-----|
| 1           | Michael | null       | 45  |
| 2           | Alice   | 1          | 38  |
| 3           | Bob     | 1          | 42  |
| 4           | Charlie | 2          | 34  |
| 5           | David   | 2          | 40  |
| 6           | Eve     | 3          | 37  |
| 7           | Frank   | null       | 50  |
| 8           | Grace   | null       | 48  |
+-------------+---------+------------+-----+
Output:
+-------------+---------+---------------+-------------+
| employee_id | name    | reports_count | average_age |
| ----------- | ------- | ------------- | ----------- |
| 1           | Michael | 2             | 40          |
| 2           | Alice   | 2             | 37          |
| 3           | Bob     | 1             | 37          |
+-------------+---------+---------------+-------------+
*/
-- ================================================ SOLUTION 1 =========================================================

-- Count how many direct reports they have
-- Compute the average age of those reports (rounded to nearest integer)
-- Return the manager’s ID and name, count of direct reports, and average age

-- ** Joining manager to employee ** coz you need to get list of managers

SELECT
    e.employee_id,
    e.name,
    COUNT(m.employee_id) AS reports_count,
    ROUND(AVG(m.age)) AS average_age
FROM
    Employees e
JOIN
    Employees m
ON m.reports_to = e.employee_id
GROUP BY e.employee_id, e.name
ORDER BY e.employee_id

-- ================================================ SOLUTION 2 =========================================================
-- Window Function

-- Grouping employees by reports_to (i.e. their manager)
-- Using window functions to count and average the direct reports for each manager.
WITH report_data AS(
    SELECT
        reports_to AS manager_id,
        COUNT(reports_to) OVER (PARTITION BY reports_to) AS reports_count,
        ROUND(AVG(age) OVER (PARTITION BY reports_to)) AS average_age
    FROM
        Employees
    WHERE
        reports_to IS NOT NULL
),
deduped_report_data AS (
    SELECT
        DISTINCT manager_id,
        reports_count,
        average_age
    FROM report_data
)
-- Joining back with the original table to get the manager's name.

SELECT
    e.employee_id,
    e.name,
    d.reports_count,
    d.average_age
FROM
    deduped_report_data d
JOIN
    Employees e
ON d.manager_id = e.employee_id
ORDER BY e.employee_id