/*
Table: Accounts
+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+
account_id is the primary key (column with unique values) for this table.
Each row contains information about the monthly income for one bank account.

Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:
"Low Salary": All the salaries strictly less than $20000.
"Average Salary": All the salaries in the inclusive range [$20000, $50000].
"High Salary": All the salaries strictly greater than $50000.
The result table must contain all three categories. If there are no accounts in a category, return 0.

Return the result table in any order.
The result format is in the following example.
Example 1:

Input:
Accounts table:
+------------+--------+
| account_id | income |
+------------+--------+
| 3          | 108939 |
| 2          | 12747  |
| 8          | 87709  |
| 6          | 91796  |
+------------+--------+
Output:
+----------------+----------------+
| category       | accounts_count |
+----------------+----------------+
| Low Salary     | 1              |
| Average Salary | 0              |
| High Salary    | 3              |
+----------------+----------------+
Explanation:
Low Salary: Account 2.
Average Salary: No accounts.
High Salary: Accounts 3, 6, and 8.
*/

-- ================================================ SOLUTION 1 =========================================================
-- Categorize each account
WITH cte AS (
    SELECT
        account_id,
        CASE WHEN income < 20000 THEN 'Low Salary'
             WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
             ELSE 'High Salary'
        END as salary_category
    FROM
        Accounts
    ),

-- EDGE CASE - Define all categories explicitly, This is to make sure all categories are populated even if a category is NULL/0/does not exist
    categories AS (
        SELECT 'Low Salary' AS category
        UNION ALL
        SELECT 'Average Salary'
        UNION ALL
        SELECT 'High Salary'
    )

-- RIGHT join to ensure all categories are present and GROUP BY category
SELECT
    categories.category,
    count(cte.account_id) as accounts_count
FROM
    cte
RIGHT JOIN
    categories
ON cte.salary_category = categories.category
GROUP BY categories.category;


-- ================================================ SOLUTION 2 =========================================================

WITH categorized AS (
    SELECT
        account_id,
        income,
        CASE
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income <= 50000 THEN 'Average Salary'
            ELSE 'High Salary'
        END AS category
),
category_counts AS (
    SELECT
        category,
        COUNT(*) OVER (PARTITION BY category) AS accounts_count
    FROM categorized
)

-- Return all categories using UNION ALL with fixed set
SELECT 'Low Salary' AS category,
       COALESCE(MAX(accounts_count), 0) AS accounts_count
FROM
    category_counts
WHERE
    category = 'Low Salary'

UNION ALL

SELECT 'Average Salary',
       COALESCE(MAX(accounts_count), 0)
FROM
    category_counts
WHERE
    category = 'Average Salary'

UNION ALL

SELECT 'High Salary',
       COALESCE(MAX(accounts_count), 0)
FROM
    category_counts
WHERE
    category = 'High Salary';
