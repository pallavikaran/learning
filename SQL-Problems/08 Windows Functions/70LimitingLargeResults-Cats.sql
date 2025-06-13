/*
We would like to find the average weight of cats grouped by breed.
Also, in the same query find the average weight of cats grouped by breed whose age is over 1
Return: breed, average_weight, average_old_weight Order by: breed

Cats:
----------------
name	varchar
breed	varchar
weight	float
color	varchar
age	    int

Desired output:
breed	            average_weight	average_old_weight
---------------------------------------------------
British Shorthair	4.5	            4.5
Maine Coon	        5.6	            5.6
Persian	            4.6	            4.8
Siamese	            5.8	            5.5
*/

-- ================================================ SOLUTION 1 =========================================================

SELECT
    breed,
    AVG(weight) AS average_weight,
    AVG(weight) FILTER (WHERE age > 1) AS average_old_weight
FROM
    cats
GROUP BY
    breed
ORDER BY breed

