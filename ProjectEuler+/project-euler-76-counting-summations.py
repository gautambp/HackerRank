# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-76-counting-summations/problem
ub = 1002
mod7 = (10 ** 9) + 7
sc = [0]*ub
sc[0] = 1

for c in range(1, ub-1):
    for m in range(c, ub):
        sc[m] += sc[m-c]

for _ in range(int(input())):
    n = int(input())
    print((sc[n]-1)%mod7)

