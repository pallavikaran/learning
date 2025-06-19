/*
Table: Products
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+
(product_id, change_date) is the primary key (combination of columns with unique values) of this table.
Each row of this table indicates that the price of some product was changed to a new price at some date.

Write a solution to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.
Return the result table in any order.
The result format is in the following example.

Example 1:
Input:
Products table:
+------------+-----------+-------------+
| product_id | new_price | change_date |
+------------+-----------+-------------+
| 1          | 20        | 2019-08-14  |
| 2          | 50        | 2019-08-14  |
| 1          | 30        | 2019-08-15  |
| 1          | 35        | 2019-08-16  |
| 2          | 65        | 2019-08-17  |
| 3          | 20        | 2019-08-18  |
+------------+-----------+-------------+
Output:
+------------+-------+
| product_id | price |
+------------+-------+
| 2          | 50    |
| 1          | 35    |
| 3          | 10    |
+------------+-------+
*/

-- For each product, look for the latest price change on or before 2019-08-16
-- If there's no price change before that date, default to price = 10.
-- ================================================ SOLUTION 1 =========================================================
-- Identify the max date for products that have change_date <= 2019-08-16
-- Get new price for products that have max date <= 2019-08-16
-- Join Products to get all records from (which have dates <= 2019-08-16 with new_price) and 0 for joins that resulted in null

SELECT
    DISTINCT p2.product_id,
    COALESCE(p3.new_price, 10) as price
FROM
    Products p2
LEFT JOIN
(SELECT
    p1.product_id,
    p.new_price
FROM
    Products p
JOIN
    (SELECT
        product_id,
        MAX(change_date) as max_change_date
    FROM Products
    WHERE change_date < '2019-08-17'
    GROUP BY product_id) as p1
ON p.product_id = p1.product_id
WHERE p.change_date = p1.max_change_date) as p3
ON p2.product_id = p3.product_id;

-- ================================================ SOLUTION 2 =========================================================
WITH CTE AS (
  SELECT
    product_id,
    MAX(change_date) as max_change_date
  FROM products
  WHERE change_date<='2019-08-16'
  GROUP BY product_id
)
SELECT
  DISTINCT p.product_id,
  (CASE WHEN c.product_id is null THEN 10 ELSE p.new_price END) as price
FROM
    products p
LEFT JOIN
    cte c
ON p.product_id =  c.product_id
WHERE p.change_date = c.max_change_date OR c.product_id is null

-- ================================================ SOLUTION 3 =========================================================
-- Window Function
WITH prdct_lst AS (
    SELECT
        product_id,
        new_price,
        ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rnk -- to assign rank per product_id ordered by latest change_date
    FROM Products
    WHERE change_date <= '2019-08-16')

SELECT
    dist_products.product_id,
    COALESCE(pl.new_price, 10) as price
FROM
    prdct_lst pl
RIGHT JOIN
    (SELECT DISTINCT product_id FROM Products) as dist_products
ON pl.product_id = dist_products.product_id
AND pl.rnk = 1 -- WHERE pl.rnk = 1 Will exclude products that have no price changes before '2019-08-16', because in those cases pl.rnk is NULL, and NULL = 1 evaluates to FALSE
