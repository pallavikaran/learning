/*
The cats form a line grouped by color. Inside each color group the cats order themselves by name. Every cat must have a unique number for its place in the line.
We must assign each cat a unique number while maintaining their color & name ordering.
Return: unique_number, name, color

Cats:
----------------
name	varchar
breed	varchar
weight	float
color	varchar
age	    int

Desired output:
unique_number	name	color
1	            Ashes	Black
2	            Charlie	Black
3	            Molly	Black
4	            Oscar	Black
5	            Smudge	Black
6	            Alfie	Brown
7	            Misty	Brown
8	            Smokey	Brown
9	            Felix	Tortoiseshell
10	            Millie	Tortoiseshell
11	            Puss	Tortoiseshell
12	            Tigger	Tortoiseshell
*/

-- ================================================ SOLUTION 1 =========================================================

SELECT
    ROW_NUMBER() OVER (ORDER BY color, name) AS unique_number,
    name,
    color
FROM
    cats
