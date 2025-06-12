/*
We are worried our cats are too fat and need to diet.
We would like to group the cats into quartiles by their weight.

Return: name, weight, weight_quartile
Order by: weight

Cats:
----------------
name	varchar
breed	varchar
weight	float
color	varchar
age	    int

Desired output:
name	weight	weight_quartile
--------------------------------
Tigger	3.8	    1
Molly	4.2	    1
Ashes	4.5	    1
Charlie	4.8	    2
Smudge	4.9	    2
Felix	5.0	    2
Puss	5.1	    3
Millie	5.4	    3
Alfie	5.5	    3
Misty	5.7	    4
Oscar	6.1	    4
Smokey	6.1	    4

*/

-- ================================================ SOLUTION 1 =========================================================
SELECT
    name,
    weight,
    NTILE(4) OVER (ORDER BY weight) AS weight_quartile  -- NTILE(4) divides into 4/ quartiles
FROM
    cats
ORDER BY weight

