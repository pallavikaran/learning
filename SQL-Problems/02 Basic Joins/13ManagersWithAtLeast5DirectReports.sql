/*
Table: Employee
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.

Write a solution to find managers with at least five direct reports.
Return the result table in any order.
The result format is in the following example.

Example 1:
Input:
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
Output:
+------+
| name |
+------+
| John |
+------+
*/


/*
JOIN

+-----+-------+------------+--------+
| e1.id  |  e1.name | e2.id |e2.name|
+--------|----------|-------|-------+
| 101    | John     | 102   | Dan   |
| 101    | John     | 103   | James |
| 101    | John     | 104   | Amy   |
| 101    | John     | 105   | Anne  |
| 101    | John     | 106   | Ron   |
+-----+-------+------------+--------+
*/
-- ================================================ SOLUTION 1 =========================================================

-- grouping by the manager HAVING to get only managers who have more than 4 reports.
SELECT
  e1.name
FROM
    Employee e1
JOIN
    Employee e2
ON e1.id = e2.managerId
GROUP BY e1.id, e1.name
HAVING COUNT(e2.id) > 4;

-- ================================================ SOLUTION 2 =========================================================

-- count how many employees each manager has
SELECT
    e1.name
FROM
    Employee e1
JOIN
    Employee e2
ON e1.id = e2.managerId
GROUP BY e2.managerId
HAVING COUNT(e2.managerId) > 4

