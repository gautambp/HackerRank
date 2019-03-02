-- @author: Gautam Patel
-- Problem Description URL: https://www.hackerrank.com/challenges/african-cities/problem
select c.name from city c, country cc where c.countrycode = cc.code and cc.continent = 'Africa';