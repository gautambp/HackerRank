# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-55-lychrel-numbers/problem
# Project Euler #55: Lychrel numbers
# https://www.hackerrank.com/contests/projecteuler/challenges/euler055/problem
from collections import defaultdict

conv_no_d = defaultdict(set)
ntop_d = {}

def is_palin(n):
    nstr = str(n)
    n_len = len(nstr)
    last_idx = n_len-1
    for i in range(n_len//2):
        if nstr[i] != nstr[last_idx-i]:
            return False
    return True
    
def get_conv_palin(n, itr):
    if n in ntop_d:
        return ntop_d[n]
    if is_palin(n):
        return n
    if itr >= 60: return None
    new_n = n + int(str(n)[::-1])
    result = get_conv_palin(new_n, itr+1)
    if result:
        ntop_d[n] = result
    return result
    
n = int(input())
for i in range(10, n):
    c = get_conv_palin(i, 0)
    if c:
        conv_no_d[c].add(i)

max_size = 0
max_n = None
for k in conv_no_d.keys():
    if len(conv_no_d[k]) > max_size:
        max_size = len(conv_no_d[k])
        max_n = k
print('{} {}'.format(max_n, max_size))
