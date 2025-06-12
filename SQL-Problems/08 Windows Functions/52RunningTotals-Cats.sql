/*
The cats must be ordered by name and will enter an elevator one by one. We would like to know what the running total weight is.
Return: name, running total weight
Order by: name

Cats:
---------------------------
name	varchar
breed	varchar
weight	float
color	varchar
age	    int

Desired output:
name	running_total_weight
-----------------------------
Alfie	5.5
Ashes	10.0
Charlie	14.8
Felix	19.8
Millie	25.2
Misty	30.9
Molly	35.1
Oscar	41.2
Puss	46.3
Smokey	52.4
Smudge	57.3
Tigger	61.1

*/
-- ================================================ SOLUTION 1 =========================================================
-- !!!!!!!!!!!!!! THIS IS RUNNING TOTAL NOT TRUE RUNNING TOTAL, assumes Name is distinct in the given dataset !!!!!!!!!!!!

SELECT
    name,
    SUM(weight) OVER (ORDER BY name) AS running_total_weight
FROM
    cats
ORDER BY name