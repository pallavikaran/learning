/*
Cats are fickle. Each cat would like to lose weight to be the equivalent weight of the cat weighing just less than it.
Print a list of cats, their weights and the weight difference between them and the nearest lighter cat ordered by weight.

Return: name, weight, weight_to_lose
Order by: weight

Cats:
----------------
name	varchar
breed	varchar
weight	float
color	varchar
age	    int

Desired output:
name	weight	weight_to_lose
--------------------------------
Tigger	3.8	    0.0
Molly	4.2	    0.4
Ashes	4.5	    0.3
Charlie	4.8	    0.3
Smudge	4.9	    0.1
Felix	5.0 	0.1
Puss	5.1	    0.1
Millie	5.4	    0.3
Alfie	5.5	    0.1
Misty	5.7	    0.2
Oscar	6.1	    0.4
Smokey	6.1 	0.0
*/

-- ================================================ SOLUTION 1 =========================================================
-- LAG(weight, 1) OVER (ORDER BY weight)
    -- LAG(weight, 1) looks 1 row before the current row (in ORDER BY weight order).
    -- So this gets the weight of the previous (lighter) cat.
    -- If there is no previous cat (i.e., the lightest cat), it returns NULL.

-- weight - LAG(weight)
    -- This calculates how much heavier each cat is than the next lightest one.
    -- For Felix: 5.0 - 4.9 = 0.1
    -- For Puss: 5.1 - 5.0 = 0.1
    -- For Tigger: NULL, because there's no cat lighter than her.

-- COALESCE(..., 0)
    -- Handles the NULL case (first row).
    -- Replaces NULL with 0 to avoid a missing value.

SELECT
    name,
    weight,
    COALESCE(
        weight - LAG(weight, 1) OVER (ORDER BY weight),
        0) AS  weight_to_lose
FROM
cats
ORDER BY weight