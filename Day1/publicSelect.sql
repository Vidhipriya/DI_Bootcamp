SELECT items 
FROM public;

SELECT items
FROM public
WHERE items>80;



SELECT items
FROM public
WHERE items<300;




SELECT customers,surname
FROM public
WHERE surname = 'Smith';



SELECT customers,surname
FROM public
WHERE surname = 'Jones';

SELECT customers,name
FROM public
WHERE name NOT 'Scott';

SELECT items FROM public ORDER BY ASC;
SELECT items FROM public WHERE items>80 ORDER BY ASC;

SELECT CONCAT(surname,name) AS full_name
FROM public
BETWEEN 1 AND 3
ORDER BY surname,name DESC NULLS LAST;

SELECT surname,name
FROM public
ORDER BY surname,name DESC NULLS LAST;

