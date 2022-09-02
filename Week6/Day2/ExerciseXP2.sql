SELECT * FROM customer;

SELECT first_name, last_name AS full_name;

SELECT create_date FROM customer;

SELECT * FROM customer ORDER BY DESC;

SELECT film_id, title, description, release_year FROM public ORDER BY rental_rate ASC;

SELECT address_id,phone FROM address WHERE district='Texas';

SELECT * FROM film WHERE film_id=15 OR film_id=15;

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

SELECT public.customer.customer_id,public.payment.payment_id
FROM  public.customer
INNER JOIN public.payment
ON public.payment.payment_id=public.customer.customer_id;
ORDER BY customer.customer_id ASC

SELECT public.inventory.film_id 
FROM public.inventory 
INNER JOIN public.film
ON public.inventory.film_id=public.film.film_id 
WHERE film.film_id not in (inventory.film_id);

-- DAY3
SELECT name FROM language;

SElECT title,description,language
FROM film
INNER JOIN language
ON language.language_id=film.language_id

SElECT title,description,language
FROM film
LEFT JOIN language
ON language.language_id=film.language_id

SElECT title,description,language
FROM film
RIGHT JOIN language
ON language.language_id=film.language_id

CREATE TABLE IF NOT EXISTS new_film(
    id SERIAL UNIQUE,
    name VARCHAR(100) UNIQUE
);
INSERT INTO new_film(name)
VALUES('Bridge to Terabithia'),('Finding Nemo');
DROP TABLE customer_review;

CREATE TABLE customer_review(
review_id SERIAL PRIMARY KEY NOT NULL,
film_id INTEGER,
FOREIGN KEY(film_id) REFERENCES new_film(id) ON DELETE CASCADE,
language_id INTEGER,
FOREIGN KEY(language_id) REFERENCES language(language_id),
title VARCHAR(100),
score INTEGER NOT NULL,
review_text VARCHAR(1000000),
last_update date NOT NULL);

INSERT INTO customer_review(title,score,review_text,last_update,film_id,language_id)
VALUES('Bridge to Terabithia',10,'Excellent movie','11/02/21',1,1);

SELECT * FROM customer_review;
DELETE FROM new_film WHERE id=1;





 
SELECT title FROM film WHERE description='%sumo%' UNION
SElECT title FROM film WHERE first_name ='%penelope%'
SELECT title FROM film WHERE RENTAL='%R%'

UPDATE film 
SET language_id=2
WHERE film_id=100;





DROP TABLE customer_review;

SELECT COUNT(*) 
FROM rental 
WHERE return_date ISNULL ;



SELECT film.title
FROM film 
JOIN film_actor
ON film_actor.film_id=film.film_id
JOIN actor
ON film_actor.actor_id=actor.actor_id
WHERE lower(description) LIKE '%sumo%' 
AND actor.first_name='Penelope'
AND actor.last_name='Monroe';

SELECT film.title
FROM film 
JOIN film_actor
ON film_actor.film_id=film.film_id
JOIN actor
ON film_actor.actor_id=actor.actor_id
WHERE length<60 
AND rating='R';

SELECT film.title
FROM film 
JOIN inventory
ON film.film_id=inventory.film_id
JOIN rental
ON rental.inventory_id=inventory.inventory_id
JOIN customer
ON customer.customer_id=rental.customer_id
WHERE lower(title) LIKE ('%boat%') OR lower(description) LIKE ('%boat%')
AND customer.first_name='Matthew' AND customer.last_name='Mahan'
ORDER BY film.replacement_cost DESC LIMIT 1;












-- EXERCISEXPGOLD1
SELECT title 
FROM film
JOIN inventory
ON film.film_id=inventory.film_id
JOIN rental
ON inventory.inventory_id=rental.inventory_id
WHERE rental_date=NULL;


SELECT title 
FROM film 
JOIN film_category
ON film.film_id=film_category.film_id
JOIN category 
ON film_category.category_id=category.category_id
WHERE lower(category.name)='Action' 
UNION
SELECT title 
FROM film 
JOIN film_actor
ON film.film_id=film_actor.film_id
JOIN actor
ON film_actor.actor_id=actor.actor_id
WHERE lower(first_name)='Joe' AND lower(last_name)='Swank';

-- EXERCISEXPGOLD2
SELECT * 
FROM address
JOIN store 
ON address.address_id=store.store_id
JOIN city
ON address.city_id=city.city_id
JOIN country
ON country.country_id=city.country_id