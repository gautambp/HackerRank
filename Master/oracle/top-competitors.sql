-- @author: Gautam Patel
-- Problem Description URL: https://www.hackerrank.com/challenges/top-competitors/problem
/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.

select h.hacker_id, h.name, s.challenge_id, s.score as s_score, d.score as d_score
from hackers h, submissions s, challenges c, difficulty d
where s.hacker_id = h.hacker_id 
    and c.hacker_id = h.hacker_id and s.challenge_id = c.challenge_id 
    and d.difficulty_level = c.difficulty_level

*/
select s.hacker_id, (select name from hackers where hacker_id = s.hacker_id)
from submissions s, challenges c, difficulty d
where s.challenge_id = c.challenge_id
    and d.difficulty_level = c.difficulty_level
    and s.score = d.score
group by s.hacker_id
having count(c.challenge_id) > 1
order by count(c.challenge_id) desc, 1
;