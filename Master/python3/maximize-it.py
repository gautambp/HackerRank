# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/maximize-it/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

n = [None]*8
for i in range(8):
    n[i] = [None]*8

s = input().split()
k = int(s[0])
m = int(s[1])

n_len_l = []
for i in range(k):
    s = input().split()[1:]
    n_len_l.append(list(range(len(s))))
    for j in range(len(s)):
        n[i][j] = int(s[j])

max_mod = 0
for i in product(*n_len_l):
    nsqr_sum = 0
    idx = 0
    for j in i:
        nsqr_sum += n[idx][j]*n[idx][j]
        idx += 1
    if nsqr_sum%m > max_mod:
        max_mod = nsqr_sum%m
print(max_mod)
