# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-1-multiples-of-3-and-5/problem
#!/bin/python3

import sys

def solve(n):
    total = 0
    n3 = int(n/3)
    s = 3 * n3 * (n3 + 1)
    s = s >> 1
    total += s
    n5 = int(n/5)
    s = 5 * n5 * (n5 + 1)
    s = s >> 1
    total += s
    n15 = int(n/15)
    s = 15 * n15 * (n15 + 1)
    s = s >> 1
    total -= s
    print(total)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    solve(n-1)