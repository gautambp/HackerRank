-- @author: Gautam Patel
-- Problem Description URL: https://www.hackerrank.com/challenges/new-companies/problem
/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
select e.company_code, 
    (select founder from company where company_code = e.company_code),
    count(distinct lead_manager_code), 
    count(distinct senior_manager_code), 
    count(distinct manager_code), 
    count(distinct employee_code) 
from employee e group by e.company_code order by e.company_code;
