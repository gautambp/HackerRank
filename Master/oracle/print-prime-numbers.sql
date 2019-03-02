-- @author: Gautam Patel
-- Problem Description URL: https://www.hackerrank.com/challenges/print-prime-numbers/problem
/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

select listagg(prime_number, '&') within group (order by prime_number)
from (
select a.n as prime_number
from (
SELECT ROWNUM n
FROM ALL_OBJECTS
WHERE ROWNUM <= 1000
) a, (
SELECT ROWNUM n
FROM ALL_OBJECTS
WHERE ROWNUM <= 1000
) b
where b.n <= a.n
group by a.n
having count(case a.n/b.n when trunc(a.n/b.n) then 'prime' end) = 2
)
;
