-- @author: Gautam Patel
-- Problem Description URL: https://www.hackerrank.com/challenges/weather-observation-station-20/problem
/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
select to_char(median(lat_n),'999.9999') from station;