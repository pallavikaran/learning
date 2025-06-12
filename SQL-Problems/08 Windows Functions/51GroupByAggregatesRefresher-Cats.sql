/*
You will need to know aggregate functions before attempting the other questions.
We would like to find the total weight of cats grouped by age. But only return those groups with a total weight larger than 12.

Return: age, sum(weight) Order by: age
Show Table Schema
Cats:
---------------------------
name	varchar
breed	varchar
weight	float
color	varchar
age	    int


Desired output:
age	total_weight
2	19.6
4	15.8
5	15.4

*/
-- ================================================ SOLUTION 1 =========================================================

SELECT
    age,
    SUM(weight)
FROM cats
GROUP BY age
HAVING SUM(weight) > 12
ORDER BY age ASC