/*
Table: Movies
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| title         | varchar |
+---------------+---------+
movie_id is the primary key (column with unique values) for this table.
title is the name of the movie.

Table: Users
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.
The column 'name' has unique values.

Table: MovieRating
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| user_id       | int     |
| rating        | int     |
| created_at    | date    |
+---------------+---------+
(movie_id, user_id) is the primary key (column with unique values) for this table.
This table contains the rating of a movie by a user in their review.
created_at is the user's review date.

Write a solution to:
Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.
The result format is in the following example.

Example 1:
Input:
Movies table:
+-------------+--------------+
| movie_id    |  title       |
+-------------+--------------+
| 1           | Avengers     |
| 2           | Frozen 2     |
| 3           | Joker        |
+-------------+--------------+
Users table:
+-------------+--------------+
| user_id     |  name        |
+-------------+--------------+
| 1           | Daniel       |
| 2           | Monica       |
| 3           | Maria        |
| 4           | James        |
+-------------+--------------+
MovieRating table:
+-------------+--------------+--------------+-------------+
| movie_id    | user_id      | rating       | created_at  |
+-------------+--------------+--------------+-------------+
| 1           | 1            | 3            | 2020-01-12  |
| 1           | 2            | 4            | 2020-02-11  |
| 1           | 3            | 2            | 2020-02-12  |
| 1           | 4            | 1            | 2020-01-01  |
| 2           | 1            | 5            | 2020-02-17  |
| 2           | 2            | 2            | 2020-02-01  |
| 2           | 3            | 2            | 2020-03-01  |
| 3           | 1            | 3            | 2020-02-22  |
| 3           | 2            | 4            | 2020-02-25  |
+-------------+--------------+--------------+-------------+
Output:
+--------------+
| results      |
+--------------+
| Daniel       |
| Frozen 2     |
+--------------+
Explanation:
Daniel and Monica have rated 3 movies ("Avengers", "Frozen 2" and "Joker") but Daniel is smaller lexicographically.
Frozen 2 and Joker have a rating average of 3.5 in February but Frozen 2 is smaller lexicographically.
*/


-- "Lexicographically" means dictionary order, similar to alphabetical order, but it also considers the entire string from left to right, one character at a time.
-- "Apple" comes before "Banana" — just like in a dictionary.
-- "Zebra" comes after "Elephant".
-- "Daniel" is lexicographically smaller than "Monica" because "D" comes before "M"
-- Hence order by column asc, no need to do length/char_length

--  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! NOT SOLUTION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-- THIS MIGHT LOOK RIGHT BUT IT IS ******* WRONG *********
-- MySQL does not allow using ORDER BY inside subqueries when using UNION unless wrapped with derived tables or CTEs

WITH cte as (
    SELECT
        mr.*,
        u.name,
        m.title
    FROM
        MovieRating mr
    JOIN
        Users u
    ON mr.user_id = u.user_id
    JOIN
        Movies m
    ON mr.movie_id = m.movie_id
)

(SELECT
    name as results
FROM
    cte
GROUP BY user_id, name
ORDER BY COUNT(*) DESC, name ASC
LIMIT 1)

UNION ALL

(SELECT
    title as results
FROM
    cte
WHERE
    cte.created_at BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY movie_id, title
ORDER BY AVG(rating) DESC, title ASC
LIMIT 1)

-- ================================================ SOLUTION 1 =========================================================
-- This is with CTE and is right

WITH cte AS (
    SELECT
        mr.*,
        u.name,
        m.title
    FROM
        MovieRating mr
    JOIN Users u ON mr.user_id = u.user_id
    JOIN Movies m ON mr.movie_id = m.movie_id
),

-- Get top user by number of ratings
    top_user AS (
        SELECT
            name AS results
        FROM cte
        GROUP BY user_id, name
        ORDER BY COUNT(*) DESC, name ASC
        LIMIT 1
),

-- Get top movie by avg rating in Feb 2020
    top_movie AS (
        SELECT
            title AS results
        FROM cte
        WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
        GROUP BY movie_id, title
        ORDER BY AVG(rating) DESC, title ASC
        LIMIT 1
)

-- Final result
SELECT * FROM top_user
UNION ALL
SELECT * FROM top_movie;

