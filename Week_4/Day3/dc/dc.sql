-- dc_d3
-- part_1

select * from CustomerDC
select * from CustomerProfile

CREATE TABLE CustomerDC (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL
);

CREATE TABLE CustomerProfile (
    id SERIAL PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT false,
    customer_id INT UNIQUE,
    FOREIGN KEY (customer_id) REFERENCES CustomerDC(id)
);

INSERT INTO CustomerDC (first_name, last_name) 
VALUES 
	('John', 'Doe'),
	('Jerome', 'Lalu'),
	('Lea', 'Rive')
	

INSERT INTO CustomerProfile (isLoggedIn, customer_id)
VALUES (true, (SELECT id FROM CustomerDC WHERE first_name = 'John' AND last_name = 'Doe'))

INSERT INTO CustomerProfile (isLoggedIn, customer_id)
VALUES (false, (SELECT id FROM CustomerDC WHERE first_name = 'Jerome' AND last_name = 'Lalu'))

SELECT c.first_name
FROM CustomerDC c
JOIN CustomerProfile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = true

SELECT c.first_name, COALESCE(cp.isLoggedIn, false) AS isLoggedIn
FROM CustomerDC c
LEFT JOIN CustomerProfile cp ON c.id = cp.customer_id

SELECT COUNT(c.id) AS num_customers_not_logged_in
FROM CustomerDC c
LEFT JOIN CustomerProfile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn IS NULL OR cp.isLoggedIn = false


-- Part_2
1.
CREATE TABLE Book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL
)

2.
INSERT INTO Book (title, author) 
VALUES
    ('Alice In Wonderland', 'Lewis Carroll'),
    ('Harry Potter', 'J.K Rowling'),
    ('To Kill a Mockingbird', 'Harper Lee')
	
3.
CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    age INT CHECK (age <= 15)
)

4.
INSERT INTO Student (name, age) 
VALUES
    ('John', 12),
    ('Lera', 11),
    ('Patrick', 10),
    ('Bob', 14)
	
5.
CREATE TABLE Library (
    book_fk_id INT,
    student_fk_id INT,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id),
    FOREIGN KEY (book_fk_id) REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (student_fk_id) REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
)

6.
INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
    (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM Student WHERE name = 'John'),
    '2022-02-15'
)

-- Insert record for Bob borrowing To kill a mockingbird on 03/03/2021
INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
    (SELECT book_id FROM Book WHERE title = 'To kill a mockingbird'),
    (SELECT student_id FROM Student WHERE name = 'Bob'),
    '2021-03-03'
)

INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
    (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM Student WHERE name = 'Lera'),
    '2021-05-23'
)

INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
    (SELECT book_id FROM Book WHERE title = 'Harry Potter'),
    (SELECT student_id FROM Student WHERE name = 'Bob'),
    '2021-08-12'
)

7.
SELECT * FROM Library

SELECT s.name AS student_name, b.title AS book_title
FROM Library l
JOIN Student s ON l.student_fk_id = s.student_id
JOIN Book b ON l.book_fk_id = b.book_id

SELECT AVG(s.age) AS average_age
FROM Library l
JOIN Student s ON l.student_fk_id = s.student_id
JOIN Book b ON l.book_fk_id = b.book_id
WHERE b.title = 'Alice In Wonderland'

DELETE FROM Student WHERE name = 'Lera'







