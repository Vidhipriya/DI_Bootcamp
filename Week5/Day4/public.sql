CREATE TABLE items(
    smalldesk SMALLINT NOT NULL,
    bigdesk SMALLINT NOT NULL,
    fan SMALLINT NOT NULL,
    
)
INSERT INTO table(smalldesk,bigdesk,fan)
VALUES
    (100),
    (300) ,
    (80);


CREATE TABLE customers(
    name CHAR(100) PRIMARY KEY,
    surname CHAR(100) PRIMARY KEY
)
INSERT INTO table (name,surname)
VALUES
    ("Greg","Jones"),
    ("Sandra" ,"Jones") ,
    ("Scott" , "Scott"),
    ("Trevor" ," Green"),
    ("Melanie" , "Johnson") ;

SELECT items 
FROM public;

SELECT items
FROM public
WHERE items>80



SELECT items
FROM public
WHERE items<300




SELECT customers,surname
FROM public
WHERE surname = 'Smith'


SELECT customers,surname
FROM public
WHERE surname = 'Jones'

SELECT customers,name
FROM public
WHERE name NOT 'Scott'