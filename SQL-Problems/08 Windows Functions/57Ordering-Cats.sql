/*
We would like to find the fattest cat. Order all our cats by weight.
The two heaviest cats should both be 1st. The next heaviest should be 3rd.

Return: ranking, weight, name
Order by: ranking, name

Cats:
----------------
name	varchar
breed	varchar
weight	float
color	varchar
age	    int

Desired output:
ranking	weight	name
-----------------------
1	    6.1 	Oscar
1	    6.1	    Smokey
3	    5.7	    Misty
4	    5.5	    Alfie
5	    5.4 	Millie
6	    5.1 	Puss
7	    5.0 	Felix
8	    4.9	    Smudge
9	    4.8	    Charlie
10	    4.5	    Ashes
11	    4.2	    Molly
12	    3.8	    Tigger
*/

-- ================================================ SOLUTION 1 =========================================================

SELECT
    RANK() OVER (ORDER BY weight DESC) as ranking,
    weight,
    name
FROM
    cats
ORDER BY ranking, name

