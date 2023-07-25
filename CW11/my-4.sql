-- 1. Show each film beside its category and release year

SELECT  film.release_year, film.title, category.name AS category
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id;

-- 2. Show films beside its category and release year that its category is 'Action'
-- or 'Comedy' or 'Family'

SELECT film.title, film.release_year , category.name AS category
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name in ('Action', 'Comedy', 'Family');

-- 3. Show each category and number of its films

SELECT category.name AS category, COUNT(*) AS film_count
FROM film_category
JOIN category ON film_category.category_id = category.category_id
GROUP BY category.name;

-- 4. Show records that number of films are between 60 and 68

SELECT category.name AS category, COUNT(*) AS film_count
FROM film_category
JOIN category ON film_category.category_id = category.category_id
GROUP BY category.name
HAVING COUNT(*) BETWEEN 60 AND 68;

-- 5. Show each film beside it's category and its language

SELECT film.title, category.name AS category, language.name AS language
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id
JOIN language ON film.language_id = language.language_id

-- 6. Show customer with its rental duration (return date - rental date), and
-- name of film

SELECT CONCAT(customer.first_name,' ',customer.last_name) AS customer_name, film.title AS film_name,
(rental.return_date - rental.rental_date) AS rental_duration FROM customer
JOIN rental ON customer.customer_id = rental.customer_id
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film ON inventory.film_id = film.film_id;

-- 7. Show each film that its length is greater than average length of movies

SELECT film.title, film.length
FROM film
WHERE film.length > (
  SELECT AVG(length)
  FROM film
);

-- 8. Show film_id, title of each film that its return_date is between
-- '2005-05-29' and '2005-05-30'

SELECT film.film_id, film.title 
FROM film
JOIN inventory ON inventory.film_id = film.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
WHERE rental_date >= '2005-05-29' AND rental_date <= '2005-05-30'