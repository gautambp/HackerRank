-- @author: Gautam Patel
-- Problem Description URL: https://www.hackerrank.com/challenges/average-population-of-each-continent/problem
select cc.continent, floor(avg(c.population)) from city c, country cc where c.countrycode = cc.code group by cc.continent;