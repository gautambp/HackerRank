# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-82-path-sum-three-ways/problem
# Project Euler #82: Path sum: three ways
# https://www.hackerrank.com/contests/projecteuler/challenges/euler082/problem

def get_test():
    g = [
        [131, 673, 234, 103, 18],
        [201, 96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524, 37, 331]
    ]
    return (5, g)

def get_input():
    n = int(input())
    g = [None]*n
    for i in range(n):
        g[i] = list(map(int, input().split()))
    return (n, g)

n, g = get_input()
gsd = [[None]*n for _ in range(n)]
for c in range(n-1, -1, -1):
    for r in range(n-1, -1, -1):
        s = g[r][c]
        if c < n-1:
            if r == n-1:
                s += gsd[r][c+1]
            else:
                s += (gsd[r][c+1] if gsd[r][c+1] < gsd[r+1][c] else gsd[r+1][c])
        gsd[r][c] = s
gsu = [[None]*n for _ in range(n)]
for c in range(n-1, -1, -1):
    for r in range(n):
        s = g[r][c]
        if c < n-1:
            if r == 0:
                s += gsu[r][c+1]
            else:
                s += (gsu[r][c+1] if gsu[r][c+1] < gsu[r-1][c] else gsu[r-1][c])
        gsu[r][c] = s        
gs = [[None]*n for _ in range(n)]
for c in range(n-1, -1, -1):
    for r in range(n):
        s = g[r][c]
        if c < n-1:
            if r == 0:
                s += min(gs[r][c+1], gsd[r+1][c])
            elif r == n-1:
                s += min(gs[r][c+1], gsu[r-1][c])
            else:
                s += min(gs[r][c+1], gsu[r-1][c], gsd[r+1][c])
        gs[r][c] = s        
gs_min = gs[0][0]
for r in range(1, n):
    if gs[r][0] < gs_min:
        gs_min = gs[r][0]
print(gs_min)

