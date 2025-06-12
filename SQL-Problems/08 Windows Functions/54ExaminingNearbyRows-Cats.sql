/*
The cats would like to see the average of the weight of them, the cat just after them and the cat just before them.
The first and last cats are content to have an average weight of consisting of 2 cats not 3.
Return: name, weight, average_weight
Order by: weight

Cats:
----------------
name	varchar
breed	varchar
weight	float
color	varchar
age	    int

Desired output:
name	weight	average_weight
--------------------------------
Tigger	3.8	    4.0
Molly	4.2	    4.2
Ashes	4.5	    4.5
Charlie	4.8	    4.7
Smudge	4.9	    4.9
Felix	5.0	    5.0
Puss	5.1	    5.2
Millie	5.4	    5.3
Alfie	5.5	    5.5
Misty	5.7	    5.8
Oscar	6.1	    6.0
Smokey	6.1	    6.1

*/

-- ================================================ SOLUTION 1 =========================================================
SELECT
    name,
    weight,
    AVG(weight) OVER (ORDER BY weight ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS average_weight
FROM
    Cats
ORDER BY weight