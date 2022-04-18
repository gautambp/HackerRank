# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-197-investigating-the-behaviour-of-a-recursively-defined-sequence/problem
# Project Euler #197: Investigating the behaviour of a recursively defined sequence
# https://www.hackerrank.com/contests/projecteuler/challenges/euler197/problem
import math

c = 1 / (10 ** 9)
ub = 151
em = 1/ (10 ** 8)

def fx(b, x):
    val = 2 ** (b - (x ** 2))
    return math.floor(val) * c

def compute_val(u0, b):
    d = {u0:u0}
    u1 = u0
    for _ in range(ub):
        u1 = fx(b, u0)
        if u1 in d:
            return u1+u0
        u0 = u1
        d[u0] = u0
    return 0

s = input().split()
u0, b = float(s[0]), float(s[1])
val = compute_val(u0, b)
print(f'{val:.16f}')
