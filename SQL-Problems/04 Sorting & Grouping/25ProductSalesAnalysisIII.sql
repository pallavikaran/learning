/*
Table: Sales
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to Product table.
Each row records a sale of a product in a given year.
A product may have multiple sales entries in the same year.
Note that the per-unit price.

Write a solution to find all sales that occurred in the first year each product was sold.
For each product_id, identify the earliest year it appears in the Sales table.
Return all sales entries for that product in that year.
Return a table with the following columns: product_id, first_year, quantity, and price.
Return the result in any order.

Example 1:
Input:
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+

Output:
+------------+------------+----------+-------+
| product_id | first_year | quantity | price |
+------------+------------+----------+-------+
| 100        | 2008       | 10       | 5000  |
| 200        | 2011       | 15       | 9000  |
+------------+------------+----------+-------+
*/

-- ================================================ SOLUTION 1 =========================================================
-- Determine the first year each product_id appeared in the Sales table.
-- Join that result back with the original Sales table to get all sales in that first year for each product.

SELECT
    s.product_id,
    fs.first_year,
    s.quantity,
    s.price
FROM Sales s
JOIN (
    SELECT
        product_id,
        MIN(year) as first_year
    FROM Sales
    GROUP BY product_id) as fs
ON s.product_id = fs.product_id
AND s.year = fs.first_year

WITH first_year_per_product AS (
    SELECT
        product_id,
        year,
        quantity,
        price,
        MIN(year) OVER (PARTITION BY product_id) AS first_year
    FROM
        Sales
)
-- ================================================ SOLUTION 2 =========================================================
k
SELECT
    product_id,
    first_year,
    quantity,
    price
FROM
    first_year_per_product
WHERE
    year = first_year