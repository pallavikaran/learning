/*
We would like to group our cats by color
Return 3 rows, each row containing a color and a list of cat names
Return: color, names Order by: color DESC

Cats:
----------------
name	varchar
breed	varchar
weight	float
color	varchar
age	    int

Desired output:
color	            names
------------------------------------------------
Tortoiseshell	    Felix,Tigger,Millie,Puss
Brown	            Alfie,Misty,Smokey
Black	            Ashes,Molly,Smudge,Oscar,Charlie
*/

-- ================================================ SOLUTION 1 =========================================================

SELECT
    color,
    ARRAY_AGG(name) AS names
FROM
    cats
GROUP BY
    color
ORDER BY color DESC

