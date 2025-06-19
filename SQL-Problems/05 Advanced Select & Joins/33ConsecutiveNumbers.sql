/*
Table: Logs
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column starting from 1.

Find all numbers that appear at least three times consecutively.
Return the result table in any order.
The result format is in the following example.

Example 1:
Input:
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output:
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears consecutively for at least three times.
*/

-- ================================================ SOLUTION 1 =========================================================
SELECT
    DISTINCT l1.num as ConsecutiveNums
FROM
    Logs l1, Logs l2, Logs l3
WHERE l1.id = l2.id + 1 AND l2.id = l3.id + 1
AND l1.num = l2.num
AND l1.num = l3.num

-- ================================================ SOLUTION 2 =========================================================
-- Window Function

WITH cte AS (
    SELECT
        id,
        LEAD(num) OVER (ORDER BY id ASC) AS lead_no,
        num,
        LAG(num) OVER (ORDER BY id ASC) AS lag_no
    FROM
        Logs)

SELECT
    DISTINCT num AS ConsecutiveNums
FROM
    cte
WHERE lead_no = num
AND num = lag_no
