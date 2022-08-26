SELECT CONCAT(first_name,' ', last_name) AS name FROM employees;


SELECT public.departments.department_id
FROM public.employees
JOIN public.departments
ON employees.department_id=departments.department_id


SELECT *
FROM employees
ORDER BY first_name DESC

SELECT CONCAT((first_name, last_name), ' ', salary,' ' , 0.15*salary) AS PF FROM employees ;

SELECT  employee_id,first_name,last_name,salary FROM employees
ORDER BY salary ASC;

SELECT sum(salary) FROM employees;

SELECT min(salary) FROM employees;
SELECT max(salary) FROM employees;
SELECT avg(salary) FROM employees;
SELECT count(salary) FROM employees;

SELECT upper(first_name) FROM employees;

SELECT first_name,last_name,length(employees.last_name) FROM employees;

SELECT first_name from employees WHERE last_name ~ '[0-9]';

SELECT  * FROM table_name ORDER BY COLUMN_NAME ASC LIMIT 10;


SELECT first_name,last_name,salary FROM employees WHERE salary BETWEEN 10000 AND 15000;

SELECT first_name,last_name,hire_date FROM employees WHERE hire_date BETWEEN '01/01/1987' AND '31/12/1987';


SELECT employee_id,lower(first_name),lower(last_name)
FROM employees WHERE first_name LIKE '%c%' AND first_name LIKE '%e%';

SELECT last_name,jobs.job_id,salary
FROM employees
JOIN jobs
ON employees.job_id=jobs.job_id
WHERE job_title != 'Programmers' OR  job_title !='Shipping Clerks' AND
salary != 4500 OR salary != 10000 OR  salary !=15000;

SELECT last_name FROM employees WHERE length(last_name)=6;
SELECT last_name FROM employees WHERE last_name LIKE '__e%';

SELECT job_title
FROM jobs
JOIN employees
ON employees.job_id=jobs.job_id;

SELECT * FROM employees WHERE upper(last_name)='JONES' OR 
upper(last_name)= 'BLAKE' OR
upper(last_name)= 'SCOTT' OR
upper(last_name)= 'KING' OR 
upper(last_name)='FORD';

or SELECT first_name FROM employees WHERE UPPER(last_name) 
in ('JONES' , 'BLAKE' , 'SCOTT' , 'KING' , 'FORD')



