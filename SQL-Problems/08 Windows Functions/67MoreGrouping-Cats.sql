/*
The cats want to show their weight by breed. The cats agree that they should show the second lightest cat's weight (so as not to make other cats feel bad)
Print a list of breeds, and the second lightest weight of that breed

Return: breed, imagined_weight
Order by: breed

Cats:
----------------
name	varchar
breed	varchar
weight	float
color	varchar
age	    int

Desired output:
breed	            imagined_weight
-------------------------------------
British Shorthair	4.8
Maine Coon	        5.4
Persian	            4.5
Siamese	            6.1
*/
-- ================================================ SOLUTION 1 =========================================================


SELECT
    DISTINCT breed,
    NTH_VALUE(weight, 2) OVER (PARTITION BY breed ORDER BY weight RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS imagined_weight
FROM
    cats
ORDER BY breed
