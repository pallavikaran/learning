/*
The cats must be ordered first by breed and second by name. They are about to enter an elevator one by one. When all the cats of the same breed have entered they leave.
We would like to know what the running total weight of the cats is.
Return: name, breed, running total weight
Order by: breed, name

Cats:
---------------------------
name	varchar
breed	varchar
weight	float
color	varchar
age	int

Desired output:
name	  breed	                running_total_weight
-------------------------------------------------
Charlie	  British Shorthair	    4.8
Smudge	  British Shorthair	    9.7
Tigger	  British Shorthair	    13.5
Millie	  Maine Coon	        5.4
Misty	  Maine Coon	        11.1
Puss	  Maine Coon	        16.2
Smokey	  Maine Coon	        22.3
Ashes	  Persian	            4.5
Felix	  Persian	            9.5
Molly	  Persian	            13.7
Alfie	  Siamese	            5.5
Oscar	  Siamese	            11.6
*/
-- ================================================ SOLUTION 1 =========================================================
SELECT
    name,
    breed,
    SUM(weight) OVER (PARTITION BY breed ORDER BY name) AS running_total_weight
FROM
    cats
ORDER BY breed, name