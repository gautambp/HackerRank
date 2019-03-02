-- @author: Gautam Patel
-- Problem Description URL: https://www.hackerrank.com/challenges/the-report/problem
/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
select 
    case when g.grade < 8 then NULL else s.name end, g.grade, s.marks 
from students s, grades g 
where s.marks between g.min_mark and g.max_mark
order by g.grade desc, s.name;
