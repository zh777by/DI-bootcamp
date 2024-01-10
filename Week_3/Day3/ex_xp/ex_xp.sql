-- ex1

1.
SELECT name FROM language

2.
SELECT film.title, film.description, language.name
FROM film
INNER JOIN language 
ON film.language_id = language.language_id;

3.
SELECT film.title, film.description, language.name
FROM film
LEFT JOIN language 
ON film.language_id = language.language_id;

4.
CREATE TABLE new_film (
	film_id serial PRIMARY KEY,
	film_name varchar(255)
)

INSERT INTO new_film (film_name)
VALUES ('Predator'), ('Terminator'), ('Protector')
	
select * from new_film

5.
CREATE TABLE customer_review (
    review_id serial PRIMARY KEY,
    film_id INT REFERENCES new_film(film_id) ON DELETE CASCADE,
    language_id INT REFERENCES language(language_id),
    title varchar(255),
    score INT CHECK (score >= 1 AND score <= 10),
    review_text text,
    last_update timestamp DEFAULT CURRENT_TIMESTAMP
);

6.
INSERT INTO customer_review (film_id, language_id, review_text)
VALUES (
    (SELECT film_id FROM new_film WHERE film_name = 'Protector'),
    (SELECT language_id FROM language WHERE name = 'English'),
    'Protector is an exciting film with great actions.'
);


INSERT INTO customer_review (film_id, language_id, review_text)
VALUES (
    (SELECT film_id FROM new_film WHERE film_name = 'Terminator'),
    (SELECT language_id FROM language WHERE name = 'English'),
    'Terminator is a classic sci-fi movie!'
);

SELECT * FROM customer_review

7.
DELETE FROM new_film WHERE film_name = 'Protector'


-- ex2

1.
UPDATE film
SET language_id = 3
WHERE language_id = 2 AND film_id IN (1, 5)

select language_id from film order by language_id desc

2. 

-- customer_address_id_fkey references to address_id address table

3.

DROP TABLE customer_review

4.
SELECT COUNT(*) AS row_count FROM rental
WHERE rental_date = null

5.

SELECT * FROM film
ORDER BY rental_rate DESC
LIMIT 30

6.1
SELECT * FROM film
WHERE description LIKE '%The film is about a sumo wrestler, and one of the actors is Penelope Monroe%' 

6.2
SELECT * FROM film
WHERE rating = 'R' AND length < 60

6.3
SELECT * FROM customer WHERE first_name = 'Matthew' AND last_name = 'Mahan'
SELECT * FROM payment WHERE amount = 3.99
SELECT * FROM rental WHERE return_date BETWEEN '2005-07-28' AND '2005-08-01'AND customer_id = 144

SELECT customer.first_name, customer.last_name, rental.return_date, rental.customer_id
FROM customer
INNER JOIN rental
ON customer.customer_id = rental.rental_id
WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan'
WHERE rental.return_date BETWEEN '2005-07-28' AND '2005-08-01'


6.4
SELECT film.title, film.description, customer.first_name, customer.last_name 
FROM film
INNER JOIN customer
ON customer.customer_id = film.film_id
WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan'









	
	
	
	