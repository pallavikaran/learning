/*
The cats have decided the correct weight is the same as the 4th lightest cat. All cats shall have this weight.
Except in a fit of jealous rage they decide to set the weight of the lightest three to 99.9
Print a list of cats, their weights and their imagined weight

Return: name, weight, imagined_weight
Order by: weight

Cats:
----------------
name	varchar
breed	varchar
weight	float
color	varchar
age	    int

Desired output:
name	weight	imagined_weight
------------------------------------------------
Tigger	3.8	    99.9
Molly	4.2	    99.9
Ashes	4.5	    99.9
Charlie	4.8	    4.8
Smudge	4.9	    4.8
Felix	5.0	    4.8
Puss	5.1	    4.8
Millie	5.4	    4.8
Alfie	5.5	    4.8
Misty	5.7	    4.8
Oscar	6.1	    4.8
Smokey	6.1	    4.8
*/
-- ================================================ SOLUTION 1 =========================================================


SELECT
    name,
    weight,
    COALESCE(
        NTH_VALUE(weight, 4) OVER (ORDER BY weight), 99.9) AS imagined_weight
FROM
    cats
ORDER BY weight


