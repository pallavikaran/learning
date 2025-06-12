/*
For cats age means seniority, we would like to rank the cats by age (oldest first).
However we would like their ranking to be sequentially increasing.

Return: ranking, name, age
Order by: ranking, name

Cats:
----------------
name	varchar
breed	varchar
weight	float
color	varchar
age	    int

Desired output:
r	name	age
----------------
1	Alfie	5
1	Ashes	5
1	Millie	5
2	Charlie	4
2	Smokey	4
2	Smudge	4
3	Felix	2
3	Misty	2
3	Puss	2
3	Tigger	2
4	Molly	1
4	Oscar	1
*/

-- ================================================ SOLUTION 1 =========================================================

SELECT
    DENSE_RANK() OVER (ORDER BY AGE DESC) AS r,
    name,
    age
FROM
    cats
ORDER BY r, name

