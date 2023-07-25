-- CLASS WORK SQL
-- FILM TABLE

-- PART ONE
SELECT * FROM film
WHERE rental_duration >= 4;

-- PART TWO
SELECT * FROM film
WHERE rental_duration > 2 AND rental_duration < 5;

-- PART THREE
-- ASCENDING TITLE
SELECT * FROM film
ORDER BY title;
-- DESCENDING TITLE
SELECT * FROM film
ORDER BY title desc;

-- ASCENDING RENTAL_DURATION
SELECT * FROM film
ORDER BY rental_duration;
-- DESCENDING RENTAL_DURATION
SELECT * FROM film
ORDER BY rental_duration desc;

-- ASCENDING LAST_UPDATE
SELECT * FROM film
ORDER BY last_update;
-- DESCENDING LAST_UPDATE
SELECT * FROM film
ORDER BY last_update desc;

-- PART FOUR
SELECT ROUND(AVG(length)) AS average_length, 
ROUND(MIN(length)) as minimum_length, 
ROUND(MAX(length)) as maximum_length FROM film;