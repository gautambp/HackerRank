# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-5-smallest-multiple/problem
#!/bin/python3

import sys

def solve(n):
    result = 1
    l = [k for k in range(2, n+1)]
    while len(l) > 0:
        f = min(l)
        for i in range(len(l)):
            if l[i] % f == 0:
                l[i] /= f
        l = [k for k in l if k > 1]
        result *= f
    print(int(result))

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    solve(n)