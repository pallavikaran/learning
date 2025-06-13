/*
Table: RequestAccepted
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| requester_id   | int     |
| accepter_id    | int     |
| accept_date    | date    |
+----------------+---------+
(requester_id, accepter_id) is the primary key (combination of columns with unique values) for this table.
This table contains the ID of the user who sent the request, the ID of the user who received the request, and the date when the request was accepted.

Write a solution to find the people who have the most friends and the most friends number.
The test cases are generated so that only one person has the most friends.
The result format is in the following example.

Example 1:
Input:
RequestAccepted table:
+--------------+-------------+-------------+
| requester_id | accepter_id | accept_date |
+--------------+-------------+-------------+
| 1            | 2           | 2016/06/03  |
| 1            | 3           | 2016/06/08  |
| 2            | 3           | 2016/06/08  |
| 3            | 4           | 2016/06/09  |
+--------------+-------------+-------------+
Output:
+----+-----+
| id | num |
+----+-----+
| 3  | 3   |
+----+-----+
Explanation:
The person with id 3 is a friend of people 1, 2, and 4, so he has three friends in total, which is the most number than any others.
Follow up: In the real world, multiple people could have the same most number of friends. Could you find all these people in this case?
*/

-- ================================================ SOLUTION 1 ======================================================================
-- count unique friendships each user has, regardless of whether they were the requester or accepter
-- Union requester whose request was accepted WITH accepters who accepted the request
-- Counts unique friends per user

SELECT
    id,
    COUNT(DISTINCT friend_id) as num
FROM
(SELECT
    requester_id as id,
    accepter_id as friend_id
FROM
    RequestAccepted
UNION
SELECT
    accepter_id as id,
    requester_id as friend_id
FROM
    RequestAccepted
) as unique_friendships
GROUP BY id
ORDER BY num DESC
LIMIT 1

-- ================================================ SOLUTION 2 =======================================================================
-- Modified version
-- Counts unique friends per user

SELECT id, COUNT(*) AS num
FROM (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
) AS all_friends
GROUP BY id
ORDER BY num DESC
LIMIT 1

-- ================================================ SOLUTION 3 ==========================================================================
-- Follow up: In the real world, multiple people could have the same most number of friends. Could you find all these people in this case
-- This will return all users tied for the highest friend count, which covers the more general real-world case.
    -- all_friends CTE: Collects all friendships in both directions.
    -- friend_counts CTE: Counts unique friends per user.
    -- max_count CTE: Finds the maximum number of friends any user has.
    -- Final SELECT: Returns all users whose number of friends matches the maximum.

WITH all_friends AS (
    SELECT
        requester_id AS id,
        accepter_id AS friend_id
    FROM
        RequestAccepted
    UNION ALL
    SELECT
        accepter_id AS id,
        requester_id AS friend_id
    FROM
        RequestAccepted
),
friend_counts AS (
    SELECT
        id,
        COUNT(DISTINCT friend_id) AS num
    FROM
        all_friends
    GROUP BY id
),
max_count AS (
    SELECT
        MAX(num) AS max_num
    FROM
        friend_counts
)

SELECT
    id,
    num
FROM
    friend_counts
WHERE
    num = (SELECT max_num FROM max_count)  -- explicitly filters to only include users with the maximum friend count

-- We can't remove LIMIT or the WHERE filter above coz it still does not filter to only users who have the maximum number of friends,
-- it gets all users and their number of friends

-- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! NOT SOLUTION  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-- Window Function
-- You're partitioning by id, which means the RANK() window will be computed separately for each person,
-- so every person gets a rnk = 1 in their own partition

-- Union all requester and accepter IDs into one column to represent a "friend".
WITH all_friends AS (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
),
ranked_friends_cnt AS(
    SELECT
        id,
        COUNT(*) AS num,
        RANK() OVER (PARTITION BY id ORDER BY COUNT(*) DESC) as rnk
    FROM
        all_friends)

SELECT
    id,
    num
FROM
    ranked_friends_cnt
WHERE rnk = 1

-- ================================================ SOLUTION 4 ==========================================================================
-- Window Function
-- GROUP BY OVER USING PARTITION since we are counting the user_id so can't select and count in partition by

-- Union all requester and accepter IDs into one column to represent a "friend".
WITH all_friends AS (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
),
ranked_friends_cnt AS(
    SELECT
        id,
        COUNT(*) AS num,
        RANK() OVER (ORDER BY COUNT(*) DESC) as rnk
    FROM
        all_friends
    GROUP BY id)

SELECT
    id,
    num
FROM
    ranked_friends_cnt
WHERE rnk = 1
