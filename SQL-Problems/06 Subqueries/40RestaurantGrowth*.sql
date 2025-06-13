/*
Table: Customer
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| name          | varchar |
| visited_on    | date    |
| amount        | int     |
+---------------+---------+
In SQL,(customer_id, visited_on) is the primary key for this table.
This table contains data about customer transactions in a restaurant.
visited_on is the date on which the customer with ID (customer_id) has visited the restaurant.
amount is the total paid by a customer.

You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).
Compute the moving average of how much the customer paid in a seven days window (i.e., current day + 6 days before). average_amount should be rounded to two decimal places.
Return the result table ordered by visited_on in ascending order.
The result format is in the following example.

Example 1:
Input:
Customer table:
+-------------+--------------+--------------+-------------+
| customer_id | name         | visited_on   | amount      |
+-------------+--------------+--------------+-------------+
| 1           | Jhon         | 2019-01-01   | 100         |
| 2           | Daniel       | 2019-01-02   | 110         |
| 3           | Jade         | 2019-01-03   | 120         |
| 4           | Khaled       | 2019-01-04   | 130         |
| 5           | Winston      | 2019-01-05   | 110         |
| 6           | Elvis        | 2019-01-06   | 140         |
| 7           | Anna         | 2019-01-07   | 150         |
| 8           | Maria        | 2019-01-08   | 80          |
| 9           | Jaze         | 2019-01-09   | 110         |
| 1           | Jhon         | 2019-01-10   | 130         |
| 3           | Jade         | 2019-01-10   | 150         |
+-------------+--------------+--------------+-------------+
Output:
+--------------+--------------+----------------+
| visited_on   | amount       | average_amount |
+--------------+--------------+----------------+
| 2019-01-07   | 860          | 122.86         |
| 2019-01-08   | 840          | 120            |
| 2019-01-09   | 840          | 120            |
| 2019-01-10   | 1000         | 142.86         |
+--------------+--------------+----------------+
Explanation:
1st moving average from 2019-01-01 to 2019-01-07 has an average_amount of (100 + 110 + 120 + 130 + 110 + 140 + 150)/7 = 122.86
2nd moving average from 2019-01-02 to 2019-01-08 has an average_amount of (110 + 120 + 130 + 110 + 140 + 150 + 80)/7 = 120
3rd moving average from 2019-01-03 to 2019-01-09 has an average_amount of (120 + 130 + 110 + 140 + 150 + 80 + 110)/7 = 120
4th moving average from 2019-01-04 to 2019-01-10 has an average_amount of (130 + 110 + 140 + 150 + 80 + 110 + 130 + 150)/7 = 142.86
*/
-- ================================================ SOLUTION 1 =========================================================
-- There are 2 parts to this problem
    -- Step 1: finding total cost FOR EACH DAY
    -- Step 2: filtering days that have EXACTLY last 7 days transactions in the table
        -- then finding last 7 day's total of all dates from Step 1
        -- computing avg on above
    -- order by date

-- Aggregate daily totals first - grouping all transactions by visited_on (i.e., per day), to get the per day total spending
WITH total_amount as (
    SELECT
        visited_on, -- current day
        SUM(amount) as amount -- total of all for that visited_on day
    FROM
        Customer
    GROUP BY visited_on
)

-- Create 7-day rolling window, this has avg amount of last 7 days based on daily total spending and NOT individual customer transactions
-- For each date t1.visited_on, we find all rows t2.visited_on that fall in the 7-day window ending on d1.visited_on

SELECT
    t1.visited_on, -- current day
    SUM(t2.amount) as amount, -- total of the 7-day window
    ROUND(
        AVG(t2.amount), 2 -- average over 7 days
    ) as average_amount
FROM
    total_amount t1
JOIN
    total_amount t2
ON t2.visited_on BETWEEN DATE_SUB(t1.visited_on, INTERVAL 6 DAY) AND t1.visited_on
GROUP BY
    t1.visited_on
HAVING
    COUNT(t1.visited_on) = 7  -- ensures full 7 days exist (excludes visited_on for which moving dates are < 7 or > 7)
ORDER BY t1.visited_on ASC

-- ================================================ SOLUTION 2 =========================================================
-- WINDOW FUNCTION
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Does NOT work for below MYSQL 8 version !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

-- Aggregate the total amount per day
WITH daily_amounts AS(
    SELECT
        visited_on,
        SUM(amount) AS total_daily_amount
    FROM
        Customer
    GROUP BY visited_on
),
-- Use a window function over a 7-day window (current day + previous 6 days) ON aggregate the total amount per day
moving_avg AS (
    SELECT
        visited_on,
        SUM(total_daily_amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT) AS tot_amt_per_seven_days,
        ROUND(
            AVG(total_daily_amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT),
            2) AS avg_amt_per_seven_days
    FROM
        daily_amounts
)
-- Return only rows where a full 7-day window is possible (i.e., start from the 7th day)

SELECT
    visited_on,
    tot_amt_per_seven_days AS amount,
    avg_amt_per_seven_days AS average_amount
FROM
    moving_avg
WHERE
    visited_on >= (SELECT MIN(visited_on) FROM daily_amounts) + INTERVAL 6 DAY
ORDER BY visited_on

-- ================================================ SOLUTION 3 =========================================================
-- ALTERNATIVE TO SOLUTION 2

SELECT
    total_amount_1.visited_on,
    SUM(total_amount_2.total_daily_amount) AS amount,
    ROUND(AVG(total_amount_2.total_daily_amount), 2) AS average_amount
FROM (
    -- total_amount_1 is the anchor date (current day)
    SELECT
        visited_on,
        SUM(amount) AS total_daily_amount
    FROM
        Customer
    GROUP BY
        visited_on
) total_amount_1
JOIN (
    -- total_amount_2 brings in totals from the 6 previous days + current day
    SELECT
        visited_on,
        SUM(amount) AS total_daily_amount
    FROM
        Customer
    GROUP BY
        visited_on
) total_amount_2
-- simulate the 7-day window on total_amount_2
ON d2.visited_on BETWEEN DATE_SUB(total_amount_1.visited_on, INTERVAL 6 DAY) AND total_amount_1.visited_on
GROUP BY
    total_amount_1.visited_on
HAVING COUNT(*) = 7 -- ensures we only return rows with a complete 7-day window
ORDER BY total_amount_1.visited_on