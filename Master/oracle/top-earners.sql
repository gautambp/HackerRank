-- @author: Gautam Patel
-- Problem Description URL: https://www.hackerrank.com/challenges/top-earners/problem
/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
select max_salary, count(*)
from (
select e.employee_id, m.max_salary 
from (
select max(months * salary) as max_salary from employee
) m, employee e
where (e.salary * e.months) = m.max_salary
) group by max_salary
;
