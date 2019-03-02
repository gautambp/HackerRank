# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-2-even-fibonacci-numbers/problem
#!/bin/python3

import sys

def solve(n, t1, t2, total):
    while True:
        t = t1 + t2
        if t > n:
            return (t1, t2, total)
        if t%2 == 0:
            total += t
        t1 = t2
        t2 = t

t = int(input().strip())
t1 = 1
t2 = 1
last_total = 0
last_n = 0
for a0 in range(t):
    n = int(input().strip())
    if (n < last_n):
        t1 = 1
        t2 = 1
        last_total = 0
    (t1, t2, total) = solve(n, t1, t2, last_total)
    print(total)
    last_n = n
    last_total = total
