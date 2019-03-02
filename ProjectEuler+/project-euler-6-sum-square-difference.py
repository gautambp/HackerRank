# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-6-sum-square-difference/problem
#!/bin/python3

import sys

def solve(n):
    sqr_of_sum = n * (n+1)
    sqr_of_sum >>= 1
    sqr_of_sum = sqr_of_sum*sqr_of_sum
    sum_of_sqr = 0
    for i in range(1, n+1):
        sum_of_sqr += i*i
    print(sqr_of_sum-sum_of_sqr)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    solve(n)