-- @author: Gautam Patel
-- Problem Description URL: https://www.hackerrank.com/challenges/occupations/problem
/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
select min(doctor), min(professor), min(singer), min(actor) 
from (
select row_number() over (partition by doctor, professor, singer, actor order by name) as idx,
    case when doctor = 1 then name else NULL end as doctor,
    case when professor = 1 then name else NULL end as professor,
    case when singer = 1 then name else NULL end as singer,
    case when actor = 1 then name else NULL end as actor
from (
    select * from (
        select name, occupation 
        from occupations 
    )
    pivot (
        count(occupation) for occupation in (
            'Doctor' as doctor, 
            'Professor' as professor, 
            'Singer' as singer, 
            'Actor' as actor)
    ) 
) 
) 
group by idx
order by idx
;