/*
The cats now want to lose weight according to their breed.
Each cat would like to lose weight to be the equivalent weight of the cat in the same breed weighing just less than it.
Print a list of cats, their breeds, weights and the weight difference between them and the nearest lighter cat of the same breed.

Return: name, breed, weight, weight_to_lose
Order by: weight

Cats:
----------------
name	varchar
breed	varchar
weight	float
color	varchar
age	    int


Desired output:
name	breed	            weight	    weight_to_lose
-------------------------------------------------------
Tigger	British Shorthair	3.8	        0.0
Molly	Persian	            4.2	        0.0
Ashes	Persian	            4.5	        0.3
Charlie	British Shorthair	4.8	        1.0
Smudge	British Shorthair	4.9	        0.1
Felix	Persian	            5.0	        0.5
Puss	Maine Coon	        5.1	        0.0
Millie	Maine Coon	        5.4	        0.3
Alfie	Siamese	            5.5	        0.0
Misty	Maine Coon	        5.7	        0.3
Oscar	Siamese	            6.1	        0.6
Smokey	Maine Coon	        6.1	        0.4
*/

-- ================================================ SOLUTION 1 =========================================================
SELECT
    name,
    breed,
    weight,
COALESCE(weight - LAG(weight, 1) OVER (PARTITION BY breed ORDER BY weight), 0) AS weight_to_lose
FROM
    cats
ORDER BY weight
