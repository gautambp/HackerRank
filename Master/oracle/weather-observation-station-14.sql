-- @author: Gautam Patel
-- Problem Description URL: https://www.hackerrank.com/challenges/weather-observation-station-14/problem
/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
select trunc(max(lat_n),4) from station where lat_n < 137.2345;