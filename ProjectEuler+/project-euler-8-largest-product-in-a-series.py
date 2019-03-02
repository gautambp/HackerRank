# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-8-largest-product-in-a-series/problem
#!/bin/python3

import sys
from itertools import permutations 

def solve(n, k, num):
    nl = list(str(num))
    max_product = 0
    for i in range(len(nl)-k):
        prdct = 1
        for j in range(k):
            prdct *= int(nl[i+j])
        if prdct > max_product:
            max_product = prdct
    print(max_product)

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    solve(n, k, num)