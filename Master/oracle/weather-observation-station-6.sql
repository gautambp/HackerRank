-- @author: Gautam Patel
-- Problem Description URL: https://www.hackerrank.com/challenges/weather-observation-station-6/problem
/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT DISTINCT city FROM station 
WHERE (
city LIKE 'A%' or city LIKE 'a%' or
city LIKE 'E%' or city LIKE 'e%' or
city LIKE 'I%' or city LIKE 'i%' or
city LIKE 'O%' or city LIKE 'o%' or
city LIKE 'U%' or city LIKE 'u%')
;