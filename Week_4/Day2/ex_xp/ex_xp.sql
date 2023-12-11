ex1

CREATE TABLE items (
	id int PRIMARY KEY,
	item varchar (255),
	price decimal (255)
)
INSERT INTO items (id, item, price) 
VALUES 
	(1, 'Small Desk', 100),
	(2, 'Large desk', 300),
	(3, 'Fan', 800)

CREATE TABLE customers (
	id serial,
	Name varchar (255),
	Surname varchar (255)
)

INSERT INTO customers (id, Name, Surname) 
VALUES 
	(1, 'Greg', 'Jones'),
	(2, 'Sandra', 'Jones'),
	(3, 'Scott', 'Scott'),
	(4, 'Trevor', 'Green'),
	(5, 'Melanie', 'Johnson')
	
ALTER TABLE customers RENAME COLUMN NAME TO "first_name"
ALTER TABLE customers RENAME COLUMN surname to "last_name"

SELECT * FROM items WHERE price >= 80
ORDER BY price DESC

SELECT * FROM customers
SELECT first_name, last_name FROM customers ORDER BY first_name
SELECT last_name FROM customers ORDER BY first_name DESC


ex2

1. 
SELECT * FROM customer

2. 
SELECT first_name  || ' ' || last_name AS full_name FROM customer

3. 
SELECT DISTINCT create_date FROM customer

4. 
SELECT * FROM customer ORDER BY first_name DESC

5. 
SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC

6. 
SELECT address, phone, district FROM address WHERE district = 'Texas'

7. 
SELECT * FROM film WHERE film_id = 15 OR film_id = 150

8,9. 
SELECT film_id, title, description, length, rental_rate FROM film WHERE title LIKE '%Date Speed%'

10. 
SELECT * FROM film ORDER BY replacement_cost ASC LIMIT 10

11. 
SELECT * FROM film  where replacement_cost > 9.99
ORDER BY replacement_cost ASC
LIMIT 10

12.
SELECT customers.first_name, customers.last_name, payment.amount, payment.payment_date
FROM customers, payment
WHERE customers.id = payment.customer_id 
ORDER BY customers.id DESC

13.
SELECT * FROM inventory WHERE film_id = null

14. 
SELECT city.city_id, city.city, country.country_id, country.country
FROM city
JOIN country ON city.country_id = country.country_id

15.
SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, p.staff_id 
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY p.staff_id


