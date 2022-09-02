SELECT * FROM customer;

SELECT first_name, last_name FROM customer AS full_name;

SELECT create_date FROM customer;

SELECT * FROM customer ORDER BY first_name ASC;

SELECT film_id, title, description, release_year FROM film ORDER BY rental_rate ASC;

SELECT address_id,phone FROM address WHERE district='Texas';

SELECT * FROM film_list  WHERE fid=15 OR fid=150;

SELECT * FROM film_list WHERE title='Cider Desire';

SELECT title FROM film_list ORDER BY price DESC LIMIT 10;
SELECT title FROM film_list ORDER BY price DESC LIMIT 10 OFFSET 10;

