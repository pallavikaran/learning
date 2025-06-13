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

-- ================================================ SOLUTION 2 =========================================================
-- CTE for user who rated the most movies
WITH user_rating_count AS (
    SELECT
        user_id,
        COUNT(*) AS total_ratings
    FROM MovieRating
    GROUP BY user_id
),
top_user AS (
    SELECT
        user_id
    FROM user_rating_count
    ORDER BY total_ratings DESC, user_id
    LIMIT 1
),

-- CTE for movie with highest average rating in Feb 2020
movie_avg_rating AS (
    SELECT
        movie_id,
        AVG(rating) AS avg_rating
    FROM MovieRating
    WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY movie_id
),
top_movie AS (
    SELECT
        movie_id
    FROM movie_avg_rating
    ORDER BY avg_rating DESC, movie_id
    LIMIT 1
)

-- Final output
SELECT u.name AS results
FROM top_user t
JOIN Users u ON t.user_id = u.user_id

UNION ALL

SELECT m.title AS results
FROM top_movie t
JOIN Movies m ON t.movie_id = m.movie_id

-- ================================================ SOLUTION 3 =========================================================
-- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! This will NOT work foy versions below MYSQL 8 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-- Why? This is invalid — COUNT(*) OVER (...) is a window function, and you're trying to use it inside another window function's ORDER BY clause, which is not allowed.
    -- ROW_NUMBER() OVER (
    --        ORDER BY COUNT(*) OVER (PARTITION BY user_id) DESC, user_id
    --    )

WITH user_rankings AS (
    SELECT
        user_id,
        ROW_NUMBER() OVER (
            ORDER BY COUNT(*) OVER (PARTITION BY user_id) DESC, user_id
        ) AS user_rank
    FROM MovieRating
),

movie_rankings AS (
    SELECT
        movie_id,
        ROW_NUMBER() OVER (
            ORDER BY
                AVG(CASE
                        WHEN created_at BETWEEN '2020-02-01' AND '2020-02-29'
                        THEN rating
                    END
                ) DESC,
                movie_id
        ) AS movie_rank
    FROM MovieRating
)

SELECT u.name AS results
FROM user_rankings ur
JOIN Users u ON ur.user_id = u.user_id
WHERE ur.user_rank = 1

UNION ALL

SELECT m.title AS results
FROM movie_rankings mr
JOIN Movies m ON mr.movie_id = m.movie_id
WHERE mr.movie_rank = 1

-- ================================================ SOLUTION 4 =========================================================
-- Window Function

-- 1. Count ratings per user
WITH total_user_ratings AS (
    SELECT
        user_id,
        COUNT(*) AS total_ratings
    FROM
        MovieRating
    GROUP BY user_id
),
-- 2. Rank users by total ratings
total_user_ratings_ranking AS (
    SELECT
        u.name as user_name,
        ROW_NUMBER() OVER (ORDER BY tur.total_ratings DESC, u.name ASC) as usr_tot_rating_rno
    FROM
        total_user_ratings tur
    JOIN
        Users u
    ON tur.user_id = u.user_id
),
-- 3. Compute average rating in Feb 2020 per movie
avg_movie_ratings AS (
    SELECT
        movie_id,
        AVG(rating) AS avg_ratings
    FROM
        MovieRating
    WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29' -- Both dates are inclusive
    GROUP BY movie_id
),
-- 4. Rank movies by avg ratings
avg_movie_ratings_ranking AS (
    SELECT
        m.title AS movie_title,
        ROW_NUMBER() OVER (ORDER BY avg_mv.avg_ratings DESC, m.title ASC) as movie_avg_rating_rno
    FROM
        avg_movie_ratings avg_mv
    JOIN
        Movies m
    ON m.movie_id = avg_mv.movie_id
)

-- Union total_user_ratings_ranking and avg_movie_ratings_ranking
SELECT
    user_name as results
FROM
    total_user_ratings_ranking
WHERE usr_tot_rating_rno = 1
UNION ALL
SELECT
    movie_title as results
FROM
    avg_movie_ratings_ranking
WHERE movie_avg_rating_rno = 1