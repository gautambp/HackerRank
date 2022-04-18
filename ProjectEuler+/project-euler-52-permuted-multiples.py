# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-52-permuted-multiples/problem

s = input().split()
n, k = int(s[0]), int(s[1])
for i in range(1000,n+1):
    si = str(i)
    ski = str(i*k)
    if len(si) < len(ski): continue
    ssi = sorted(si)
    found = True
    for kk in range(2, k+1):
        if ssi != sorted(str(i*kk)):
            found = False
            break
    if found:
        for kk in range(1, k+1):
            print(kk*i, end=' ')
        print()
