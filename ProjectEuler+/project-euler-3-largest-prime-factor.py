# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-3-largest-prime-factor/problem
#!/bin/python3

import sys

def solve(n):
    i = 2
    while i * i <= n:
        if n % i:
             i += 1
        else:
            n //= i
    print (int(n))

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    solve(n)