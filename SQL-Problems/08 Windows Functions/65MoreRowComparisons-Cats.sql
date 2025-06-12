/*
Each cat would like to see the next heaviest cat's weight when grouped by breed. If there is no heavier cat print 'fattest cat'
Print a list of cats, their weights and either the next heaviest cat's weight or 'fattest cat'

Return: name, weight, breed, next_heaviest
Order by: weight

Cats:
----------------
name	varchar
breed	varchar
weight	float
color	varchar
age	    int


Desired output:
name	weight	    breed	        next_heaviest
------------------------------------------------
Tigger	3.8	    British Shorthair	4.8
Molly	4.2	    Persian	            4.5
Ashes	4.5	    Persian	            5
Charlie	4.8	    British Shorthair	4.9
Smudge	4.9	    British Shorthair	fattest cat
Felix	5.0	    Persian	            fattest cat
Puss	5.1	    Maine Coon	        5.4
Millie	5.4	    Maine Coon	        5.7
Alfie	5.5 	Siamese	            6.1
Misty	5.7	    Maine Coon	        6.1
Oscar	6.1	    Siamese	            fattest cat
Smokey	6.1	    Maine Coon	        fattest cat
*/

-- ================================================ SOLUTION 1 =========================================================

SELECT
    name,
    weight,
    breed,
    COALESCE(
        CAST(
            LEAD(weight, 1) OVER (PARTITION BY breed ORDER BY weight ASC)
        AS VARCHAR),
    'fattest cat') AS next_heaviest
FROM
    cats
ORDER BY weight