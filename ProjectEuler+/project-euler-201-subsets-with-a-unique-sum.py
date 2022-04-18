# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-201-subsets-with-a-unique-sum/problem
# Project Euler #201: Subsets with a unique sum
# https://www.hackerrank.com/contests/projecteuler/challenges/euler201/problem
from collections import defaultdict

def subset_sum_rec(l, ss, itm_cnt, ssum, f):
    #print('{} {} - {}'.format(itm_cnt, ssum, f))
    if itm_cnt < ss:
        for i in range(len(l)-ss+1):
            idx = f+i
            if idx < len(l):
                yield from subset_sum_rec(l, ss, itm_cnt+1, ssum+l[idx], idx+1)
            else:
                break
    else:
        yield ssum

def get_test():
    return (6, 3, [1, 3, 6, 8, 10, 11])

def get_input():
    s = input().split()
    n, m = int(s[0]), int(s[1])
    l = list(map(int, input().split()))
    return (n, m, l)
    
n, m, s = get_input()
g = subset_sum_rec(s, m, 0, 0, 0)
d = defaultdict(int)
for i in g:
    d[i] += 1

all_sub_sum = 0
for k in d.keys():
    if d[k] == 1:
        all_sub_sum += k
print(all_sub_sum)
