# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-44-pentagon-numbers/problem
import math

pflag_cache = {}

def getPentagonal(n):
    i = int(n * (3 * n - 1) / 2)
    return i

def isPentagonal(x):
    sx = (24*x+1) ** 0.5
    isx = int(sx)
    if sx - isx != 0:
        return False
    return isx % 6 == 5

(n, k) = [int(i) for i in input().strip().split(' ')]

for i in range(k+1, n+1):
    pn = getPentagonal(i)
    pnk = getPentagonal(i-k)
    pflag_cache[pn] = True
    pflag_cache[pnk] = True
    #print('{} {} {}'.format(i, pn, pnk))
    if pn+pnk in pflag_cache or pn-pnk in pflag_cache:
        print(pn)
    elif isPentagonal(pn+pnk) or isPentagonal(pn-pnk):
        print(pn)
        pflag_cache[pn+pnk] = True
        pflag_cache[pn-pnk] = True

