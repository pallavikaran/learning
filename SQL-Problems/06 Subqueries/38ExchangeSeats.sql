/*
Table: Seat
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key (unique value) column for this table.
Each row of this table indicates the name and the ID of a student.
The ID sequence always starts from 1 and increments continuously.

Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped
Return the result table ordered by id in ascending order.
The result format is in the following example.

Example 1:
Input:
Seat table:
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | Emerson |
| 4  | Green   |
| 5  | Jeames  |
+----+---------+
Output:
+----+---------+
| id | student |
+----+---------+
| 1  | Doris   |
| 2  | Abbot   |
| 3  | Green   |
| 4  | Emerson |
| 5  | Jeames  |
+----+---------+
Explanation:
Note that if the number of students is odd, there is no need to change the last one's seat.
*/

-- ================================================ SOLUTION 1 =========================================================

-- CASE-based transformation
-- when id is odd, id % 2 = 1, then return id + 1
-- when id is even, id % 2 = 0, then return id - 1
-- student names will adjust based on updated id
-- order result by asc ids

SELECT
    CASE WHEN id % 2 = 1 AND id + 1 <= (SELECT MAX(id) FROM Seat) THEN id + 1
         WHEN id % 2 = 0 THEN id - 1
         ELSE id
    END as id,
    student
FROM
    Seat
ORDER BY id ASC

-- ================================================ SOLUTION 2 =========================================================
-- SELF JOIN
-- joining the Seat table to itself (s1 and s2).
-- For each row in s1, we look for its neighbor:
-- If the id is odd(s1.id % 2 = 1), we try to join it with the next (id + 1).
-- If the id is evens1.id % 2 = 0), we try to join it with the previous (id - 1).
-- Then we select s2.student (the swapped one), and fallback to s1.student if no match is found (e.g., the last row in an odd-sized table) using COALESCE.
-- Final result is ordered by the original s1.id to preserve the sequence.

SELECT
    s1.id,
    COALESCE(s2.student, s1.student) as student
FROM
    Seat s1
LEFT JOIN
    Seat s2
ON (s1.id % 2 = 1 AND s2.id = s1.id + 1) -- odd
    OR
   (s1.id % 2 = 0 AND s2.id = s1.id - 1) -- even
ORDER BY s1.id ASC
