# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-236-luxury-hampers/problem
from fractions import Fraction
from itertools import product

class prod_matches:
    
    def __init__(self, m, n):
        self.m = m
        self.p = [[] for _ in range(n)]
        
    def add_product_vals(self, idx, l):
        for p in l:
            self.p[idx].append(p)
            
    def is_valid_m(self, sum_a, sum_b):
        n = len(self.p)
        for ps in product(*self.p):
            as_sum = 0
            bs_sum = 0
            for i in range(n):
                as_sum += ps[i][0]
                bs_sum += ps[i][1]
            if self.m == calc_m(bs_sum, sum_b, as_sum, sum_a): 
                return True
        return False
    
def get_input():
    n = int(input())
    s = input().split()
    a = [int(s[i]) for i in range(n)]
    s = input().split()
    b = [int(s[i]) for i in range(n)]
    return (n, a, b)

def get_test():
    return (3, [10,8,6], [2,9,9])

def get_smallest_pair_idx(a, b):
    min_p = a[0]*b[0]
    min_p_idx = 0
    for i in range(1, len(a)):
        if a[i]*b[i] < min_p:
            min_p = a[i]*b[i]
            min_p_idx = i
    return min_p_idx

def calc_m(ai, a, bi, b):
    fa = Fraction(ai, a)
    fb = Fraction(bi, b)
    return fb/fa
    
def calc_spoilage(m, a, b):
    l = []
    for a_val in range(1, a+1):
        for b_val in range(1, b+1):
            if m == calc_m(a_val, a, b_val, b):
                l.append((a_val, b_val))
    return l
    
def solve(n, a, b, idx, sum_a, sum_b):
    pml = []
    for a_val in range(1, a[idx]+1):
        for b_val in range(1, b[idx]+1):
            m = calc_m(a_val, a[idx], b_val, b[idx])
            if m > 1:
                pm = prod_matches(m, n)
                is_valid_m = True
                for i in range(n):
                    if i == idx:
                        pm.add_product_vals(i, [(a_val, b_val)])
                    else:
                        sl = calc_spoilage(m, a[i], b[i])
                        if len(sl) == 0:
                            is_valid_m = False
                            break
                        pm.add_product_vals(i, sl)
                if is_valid_m:
                    pml.append(pm)
    return pml
    
n,a,b = get_input()
sum_a = sum(a)
sum_b = sum(b)
idx = get_smallest_pair_idx(a, b)
pml = solve(n, a, b, idx, sum_a, sum_b)
for pm in pml:
    if pm.is_valid_m(sum_a, sum_b):
        print(pm.m)
        break

