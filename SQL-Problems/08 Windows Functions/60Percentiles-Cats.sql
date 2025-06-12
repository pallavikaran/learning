/*
Each cat would like to know what weight percentile it is in. This requires casting to an integer
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
Tigger	3.8	    8
Molly	4.2	    17
Ashes	4.5	    25
Charlie	4.8	    33
Smudge	4.9	    42
Felix	5.0	    50
Puss	5.1	    58
Millie	5.4	    67
Alfie	5.5	    75
Misty	5.7	    83
Oscar	6.1	    100
Smokey	6.1	    100
*/

-- ================================================ SOLUTION 1 =========================================================
select
    name,
    weight,
    CAST(CUME_DIST() OVER(ORDER BY weight) * 100 AS INTEGER) AS percent -- CUME_DIST ranks between 0 to 1 hence * by 100
FROM
    cats
ORDER BY weight

