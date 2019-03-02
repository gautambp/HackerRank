-- @author: Gautam Patel
-- Problem Description URL: https://www.hackerrank.com/challenges/ollivanders-inventory/problem
/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
select w.id, 
    wp.age, 
    w.coins_needed, w.power 
from wands w, wands_property wp
where w.code = wp.code and wp.is_evil = 0
order by 4 desc, 2 desc 
;