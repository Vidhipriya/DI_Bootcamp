CREATE DATABASE bootcamp;

CREATE TABLE students(
    id SERIAL UNIQUE,
    last_name VARCHAR(100) NOT NULL,
    first_name  VARCHAR(100) NOT NULL,
    birth_date DATE NOT NUll
);

