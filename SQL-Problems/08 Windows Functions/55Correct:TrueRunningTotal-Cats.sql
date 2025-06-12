/*
The cats must be ordered by weight descending and will enter an elevator one by one. We would like to know what the running total weight is.
If two cats have the same weight they must enter separately.
Return: name, running total weight
Order by: weight desc

Cats:
----------------------
name	varchar
breed	varchar
weight	float
color	varchar
age	    int


Desired output:
name	running_total_weight
-----------------------------
Smokey	6.1
Oscar	12.2
Misty	17.9
Alfie	23.4
Millie	28.8
Puss	33.9
Felix	38.9
Smudge	43.8
Charlie	48.6
Ashes	53.1
Molly	57.3
Tigger	61.1
*/

-- ================================================ SOLUTION 1 =========================================================
-- !!!!!!!!!!! THIS IS TRUE RUNNING TOTAL NOT RUNNING TOTAL, assumes weight are duplicates in the given dataset !!!!!!!!!!!
-- TRUE RUNNING TOTAL ADD - ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW

SELECT
    name,
    SUM(weight) OVER (ORDER BY weight DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total_weight
FROM
    cats
ORDER BY weight DESC