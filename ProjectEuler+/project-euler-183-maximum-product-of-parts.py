# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-183-maximum-product-of-parts/problem
# Project Euler #183: Maximum product of parts
# https://www.hackerrank.com/contests/projecteuler/challenges/euler183/problem

import math
from fractions import Fraction

n_max = (10 ** 6) + 1
ub = math.ceil(n_max/math.e)+1

def init_term_flag():
    term_flag_l = [False]*ub
    for i in [2,5,100,1000,10000,100000]:
        n = i
        while n < ub:
            term_flag_l[n] = True
            n *= 2
        n = i
        while n < ub:
            term_flag_l[n] = True
            n *= 5
    return term_flag_l

def is_match(n):
    while n > 2:
        if n%2 == 0:
            n //= 2
        elif n%5 == 0:
            n //= 5
        else:
            return False
    return True

def verify():
    term_flag_l = init_term_flag()
    for i in range(2, ub):
        if is_match(i) != term_flag_l[i]:
            print(f'{i} - {term_flag_l[i]}')

def init_ans():
    ans_l = [None]*n_max
    term_flag_l = init_term_flag()
    sdn = 0
    for i in range(5, n_max):
        ns = round(i/math.e)
        f = Fraction(i, ns)
        if f.denominator == 1 or term_flag_l[f.denominator]:
            sdn -= i
        else:
            sdn += i
        ans_l[i] = sdn
    return ans_l

ans_l = init_ans()
for _ in range(int(input())):
    n = int(input())
    print(ans_l[n])

