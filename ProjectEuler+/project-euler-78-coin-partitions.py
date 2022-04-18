# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-78-coin-partitions/problem
# Problem - Coin partitions
# https://www.hackerrank.com/contests/projecteuler/challenges/euler078/problem

import sys
sys.setrecursionlimit(3000)

ub = 6*10000+1
m = (10 ** 9) + 7
p_l = [None]*ub
p_l[0] = 1

def pen_num(k):
    return k * (3 * k - 1) // 2

def p(n):
    if n < 0: return 0
    if p_l[n]: return p_l[n]
    cnt = 0
    k = 1
    while True:
        ppk = pen_num(k)
        pnk = pen_num(-k)
        if n-ppk < 0 and n-pnk < 0: break
        if k%2 == 1:
            cnt += p(n-ppk)
            cnt += p(n-pnk)
        else:
            cnt -= p(n-ppk)
            cnt -= p(n-pnk)
        k += 1
    p_l[n] = cnt
    return cnt

for _ in range(int(input())):
    n = int(input())
    i = 1000
    while i < n:
        if p_l[i] == None: p(i)
        i += 1000
    print(p(n)%m)
