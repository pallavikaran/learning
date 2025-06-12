/*
Cats are vain. Each cat would like to pretend it has the lowest weight for its color.
Print cat name, color and the minimum weight of cats with that color.

Return: name, color, lowest_weight_by_color
Order by: color, name

Cats:
----------------
name	varchar
breed	varchar
weight	float
color	varchar
age	    int

Desired output:
name	color	    weight_by_color
--------------------------------
Ashes	Black   	    4.2
Charlie	Black	        4.2
Molly	Black   	    4.2
Oscar	Black	        4.2
Smudge	Black	        4.2
Alfie	Brown	        5.5
Misty	Brown	        5.5
Smokey	Brown	        5.5
Felix	Tortoiseshell	3.8
Millie	Tortoiseshell	3.8
Puss	Tortoiseshell	3.8
Tigger	Tortoiseshell	3.8
*/

-- ================================================ SOLUTION 1 =========================================================

SELECT
    name,
    color,
    NTH_VALUE(weight, 1) OVER (PARTITION BY color ORDER BY weight) AS weight_by_color
FROM
    cats
ORDER BY color, name

