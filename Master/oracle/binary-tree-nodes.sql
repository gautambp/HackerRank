-- @author: Gautam Patel
-- Problem Description URL: https://www.hackerrank.com/challenges/binary-tree-nodes/problem
/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
select N, 
    case 
        when P is null then 'Root' 
        when is_parent = 1 then 'Inner' 
        else 'Leaf' 
    end 
from (
select s.N, s.P, (select 1 from BST where P is not null and P = s.N and rownum = 1) as is_parent
from BST s
)
order by N
;