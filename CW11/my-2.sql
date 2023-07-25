-- Find customers that their firstnames start with 'Jen
SELECT * FROM customer 
WHERE first_name LIKE 'jen%';

-- Find customers that their firstnames have with 'er'
SELECT * FROM customer 
WHERE first_name LIKE '%er%';

-- Find customers that their firstnames end with 'l'
SELECT * FROM customer
WHERE first_name LIKE '%l';

-- Find customers that their firstnames don't start with 'Jen'
SELECT * FROM customer
WHERE first_name NOT LIKE 'jen%';