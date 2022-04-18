# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-81-path-sum-two-ways/problem
# Project Euler #81: Path sum: two ways
# https://www.hackerrank.com/contests/projecteuler/challenges/euler081/problem

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
gs = [None]*n
for r in range(n-1, -1, -1):
    gs[r] = [None]*n
    for c in range(n-1, -1, -1):
        s = g[r][c]
        if r < n-1 and c < n-1:
            s += (gs[r+1][c] if gs[r+1][c] < gs[r][c+1] else gs[r][c+1])
        elif r < n-1:
            s += gs[r+1][c]
        elif c < n-1:
            s += gs[r][c+1]
        gs[r][c] = s
print(gs[0][0])
