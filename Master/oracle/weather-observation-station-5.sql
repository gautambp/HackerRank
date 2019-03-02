-- @author: Gautam Patel
-- Problem Description URL: https://www.hackerrank.com/challenges/weather-observation-station-5/problem
/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
select city, city_len
from (
select city, length(city) as city_len, min(length(city)) over () as max_len 
from station order by city
) where city_len = max_len and rownum = 1
;
select city, city_len
from (
select city, length(city) as city_len, max(length(city)) over () as max_len 
from station order by city
) where city_len = max_len and rownum = 1
;