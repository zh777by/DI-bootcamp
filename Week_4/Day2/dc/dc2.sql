dc2

CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
)

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar')

CREATE TABLE SecondTab (
    id integer 
)

INSERT INTO SecondTab VALUES
(5),
(NULL)

SELECT * FROM FirstTab
SELECT * FROM SecondTab

SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id IS NULL)
-- The query counts the number of rows in FirstTab where the id is not NULL in the SecondTab. If the result is 0, it means that all rows in FirstTab have corresponding NULL values in the id column of SecondTab. If the result is greater than 0, it means that there are rows in FirstTab where the id does not have a corresponding NULL value in SecondTab.

SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
-- The query counts the number of rows in FirstTab where the id is not equal to 5 in the SecondTab. If the result is 0, it means that all rows in FirstTab have corresponding values of 5 in the id column of SecondTab. If the result is greater than 0, it means that there are rows in FirstTab where the id does not have a corresponding value of 5 in SecondTab.

SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
-- The query counts the number of rows in FirstTab where the id does not have a corresponding value in the id column of SecondTab. If the result is 0, it means that all rows in FirstTab have corresponding values in the id column of SecondTab. If the result is greater than 0, it means that there are rows in FirstTab where the id does not have a corresponding value in SecondTab.

SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
-- The query counts the number of rows in FirstTab where the id does not have a corresponding non-NULL value in the id column of SecondTab. If the result is 0, it means that all rows in FirstTab have corresponding non-NULL values in the id column of SecondTab. If the result is greater than 0, it means that there are rows in FirstTab where the id does not have a corresponding non-NULL value in SecondTab.