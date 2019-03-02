-- @author: Gautam Patel
-- Problem Description URL: https://www.hackerrank.com/challenges/weather-observation-station-19/problem
/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.


*/

select to_char(sqrt(power(a-b,2)+power(c-d,2)),'999.9999') from (
select min(lat_n) a, min(long_w) c, max(lat_n) b, max(long_w) d from station
);
