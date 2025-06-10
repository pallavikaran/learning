/*
Table: Triangle
+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
In SQL, (x, y, z) is the primary key column for this table.
Each row of this table contains the lengths of three line segments.

Report for every three line segments whether they can form a triangle.
Return the result table in any order.
The result format is in the following example.

Example 1:
Input:
Triangle table:
+----+----+----+
| x  | y  | z  |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+
Output:
+----+----+----+----------+
| x  | y  | z  | triangle |
+----+----+----+----------+
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
+----+----+----+----------+
*/

-- ================================================ SOLUTION 1 =========================================================
-- For three sides x, y, z to form a triangle:
-- x + y > z
-- x + z > y
-- y + z > x

-- x + y = z OR x + z = y OR z + y = x is NOT a degenerate triangle (where one side equals the sum of the other two), not for valid triangles

SELECT
    x,
    y,
    z,
    (CASE WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
    ELSE 'No'
    END) as triangle
FROM
    Triangle

