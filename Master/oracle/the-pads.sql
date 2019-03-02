-- @author: Gautam Patel
-- Problem Description URL: https://www.hackerrank.com/challenges/the-pads/problem
/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
select name || '(' || substr(occupation, 0, 1) || ')' from occupations order by name;
select 'There are a total of ' || occ_cnt || ' ' || lower(occupation) || 's.'
from (
    select occupation, count(*) occ_cnt from occupations group by occupation
)
order by occ_cnt, occupation;