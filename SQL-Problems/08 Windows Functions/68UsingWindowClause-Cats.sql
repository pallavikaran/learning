/*
This SQL function can be made simpler by using the WINDOW statement. Please try and use the WINDOW clause.
Each cat would like to see what half, third and quartile they are in for their weight.

Return: name, weight, by_half, thirds, quartile
Order by: weight

Cats:
----------------
name	varchar
breed	varchar
weight	float
color	varchar
age	    int

*/

-- ================================================ SOLUTION 1 =========================================================
-- Without using window

SELECT
name,
weight,
NTILE(2) OVER (ORDER BY weight) AS by_half,
NTILE(3) OVER (ORDER BY weight) AS thirds,
NTILE(4) OVER (ORDER BY weight) AS quart
FROM
cats
ORDER BY weight


-- ================================================ SOLUTION 2 =========================================================
-- Using Window

SELECT
    name,
    weight,
    NTILE(2) OVER ntile_window AS by_half,
    NTILE(3) OVER ntile_window AS thirds,
    NTILE(4) OVER ntile_window AS quart
FROM
    cats
WINDOW NTILE_WINDOW AS (ORDER BY weight)
ORDER BY weight

