-- @author: Gautam Patel
-- Problem Description URL: https://www.hackerrank.com/challenges/draw-the-triangle-2/problem
/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
select rpad('* ', 2*level, '* ') from dual connect by level <= 20 order by 1;