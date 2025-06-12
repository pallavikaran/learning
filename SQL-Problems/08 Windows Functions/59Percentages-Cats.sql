/*
Each cat would like to know what percentage of other cats weigh less than it
Return: name, weight, percent
Order by: weight

Cats:
----------------
name	varchar
breed	varchar
weight	float
color	varchar
age	    int

Desired output:
name	weight	percent
-------------------------
Tigger	3.8	    0.0
Molly	4.2	    9.1
Ashes	4.5	    18.2
Charlie	4.8	    27.3
Smudge	4.9	    36.4
Felix	5.0	    45.5
Puss	5.1	    54.5
Millie	5.4	    63.6
Alfie	5.5	    72.7
Misty	5.7	    81.8
Oscar	6.1	    90.9
Smokey	6.1	    90.9
*/
-- ================================================ SOLUTION 1 =========================================================

SELECT
    name,
    weight,
    PERCENT_RANK() OVER (ORDER BY weight) * 100 AS percent -- PERCENT_RANK ranks between 0 to 1 hence * by 100
FROM
    cats
ORDER BY weight


