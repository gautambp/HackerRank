# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-98-anagramic-squares/problem
# Problem - Anagramic squares
# https://www.hackerrank.com/contests/projecteuler/challenges/euler098/problem
from collections import defaultdict

n = int(input())
lb = int((10 ** (n-1)) ** 0.5)
ub = int((10 ** n) ** 0.5)
d = defaultdict(list)
for i in range(lb, ub):
    i_sqr = i ** 2
    i_sqr_s = str(i_sqr)
    #if len(i_sqr_s) < n: continue
    i_sqr_s = ''.join(sorted(i_sqr_s))
    d[i_sqr_s].append(i_sqr)

largest_set = []
largest_set_size = 0
for k in d.keys():
    v = d[k]
    if len(v) == 1: continue
    if len(v) > largest_set_size:
        largest_set = v
        largest_set_size = len(v)
    elif len(v) == largest_set_size:
        largest_set.extend(v)
largest_set.sort()
print(largest_set[-1])
