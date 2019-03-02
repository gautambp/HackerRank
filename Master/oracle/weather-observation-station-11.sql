-- @author: Gautam Patel
-- Problem Description URL: https://www.hackerrank.com/challenges/weather-observation-station-11/problem
/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
select unique city from station where not (regexp_like(city, '^[aeiou]', 'i') and regexp_like(city, '[aeiou]$', 'i'));