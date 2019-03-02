-- @author: Gautam Patel
-- Problem Description URL: https://www.hackerrank.com/challenges/type-of-triangle/problem
/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
select  
    case 
    when (a = b and b = c) then 'Equilateral'
    when (a + b <= c or a + c <= b or b + c <= a) then 'Not A Triangle'
    when (a = b or b = c or a = c) then 'Isosceles'
    when (a != b and b != c and a != c) then 'Scalene'
    else ''
    end
from triangles;
