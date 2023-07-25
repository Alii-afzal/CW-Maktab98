-- 1. Show unique districts of address table.
-- a) Limit number of rows
SELECT district FROM address
LIMIT 50;

-- b) Sort rows based on districts
SELECT district FROM address
ORDER BY district ASC LIMIT 100;

-- 2. Count unique districts of address table.
SELECT COUNT(DISTINCT district) FROM address;

-- 3. Count number of addresses for each district
-- a) Sort rows based on districts
SELECT district, COUNT(district) AS address_count 
FROM address 
GROUP BY district 
ORDER BY address_count DESC 
LIMIT 3;

-- 4. Show addresses which are California or Alberta

SELECT *
FROM address
WHERE district IN ('California', 'Alberta');

-- 5. Select address, district which are one of these districts: California, Alberta,
-- Texas, Hamilton

SELECT address, district
FROM address
WHERE district IN ('California', 'Alberta', 'Texas', 'Hamilton');

-- 6. Select addresses that address2 field is empty;

SELECT * FROM address
WHERE address2 IS Null;