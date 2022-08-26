CREATE TABLE items(
    smalldesk SMALLINT NOT NULL,
    bigdesk SMALLINT NOT NULL,
    fan SMALLINT NOT NULL);

CREATE TABLE customers(
    id SERIAL PRIMARY KEY, 
    first_name CHAR(100) NOT NULL,
    surname CHAR(100) NOT NULL);