-- @author: Gautam Patel
-- Problem Description URL: https://www.hackerrank.com/challenges/asian-population/problem
select sum(c.population) from city c, country cc where c.countrycode = cc.code and cc.continent = 'Asia';