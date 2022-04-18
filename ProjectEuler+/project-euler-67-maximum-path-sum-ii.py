# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-67-maximum-path-sum-ii/problem
# Problem - Maximum path sum II
# https://www.hackerrank.com/contests/projecteuler/challenges/euler067/problem

def solve(l, r, sl):
    if r < 0: return sl[0]
    lr = len(l[r])
    new_sl = [0]*lr
    for i in range(lr):
        new_sl[i] = max(l[r][i] + sl[i], l[r][i] + sl[i+1])
    return solve(l, r-1, new_sl) 

for _ in range(int(input())):
    n = int(input())
    l = [None]*n
    for i in range(n):
        l[i] = []
        s = input().split(' ')
        for j in range(i+1):
            l[i].append(int(s[j]))
    print(solve(l, n-2, l[n-1]))
