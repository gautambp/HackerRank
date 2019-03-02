# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/iterables-and-iterators/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input())
l = input().split()
k = int(input())
tot_cnt = 0
a_cnt = 0
for i in combinations(l, k):
    tot_cnt += 1
    if 'a' in i:
        a_cnt += 1
print(a_cnt/tot_cnt)
