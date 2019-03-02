# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-62-cubic-permutations/problem
cube_l = {}

def init(n):
    for i in range(3, n):
        val = i ** 3
        sorted_val = ''.join(sorted(str(val), reverse=True))
        if not(sorted_val in cube_l):
            cube_l[sorted_val] = []
        cube_l[sorted_val].append(i)
 
#(n, k) = (10000, 3)
(n, k) = [int(i) for i in input().split(' ')]

init(n)
r = range(1, k)
for c in cube_l.values():
    if len(c) == k:
        min_c = c[0] ** 3
        for i in r:
            val = c[i] ** 3
            if val < min_c: min_c = val
        print(min_c)

