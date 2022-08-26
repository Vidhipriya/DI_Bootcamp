SELECT * FROM  students;

SELECT last_name,first_name
FROM students;
SELECT last_name,first_name FROM students WHERE id=2;
SELECT last_name,first_name FROM students WHERE last_name='Benichou' AND first_name='Marc';
SELECT last_name,first_name FROM students WHERE last_name='Benichou' OR first_name='Marc';

SELECT first_name FROM students WHERE first_name LIKE'%a%';
SELECT first_name FROM students WHERE first_name LIKE'%a';
SELECT first_name FROM students WHERE lower(first_name) LIKE 'a%';
SELECT first_name FROM students WHERE first_name LIKE '%a_';
SELECT first_name FROM students WHERE id=1 OR id=3;

SELECT first_name,  SUBSTRING(first_name,2,4)  FROM students ;
SELECT first_name FROM students WHERE birth_dates => 1/01/2000 ORDER BY ASC;




