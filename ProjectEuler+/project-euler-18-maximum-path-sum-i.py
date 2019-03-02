# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-18-maximum-path-sum-i/problem
def solve(l, r, c):
    if r == len(l)-1:
        return l[r][c]
    if c == len(l)-1:
        return l[r][c]
    t1 = solve(l, r+1, c)
    t2 = solve(l, r+1, c+1)
    if t1 > t2:
        return l[r][c] + t1
    else:
        return l[r][c] + t2

t = int(input())
for _ in range(t):
    s = int(input())
    l = [None]*s
    for i in range(s):
        l[i] = list(map(int, input().split(' ')))
    print(solve(l, 0, 0))