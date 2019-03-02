# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-9-special-pythagorean-triplet/problem
pyt_cache = [-1]*3001

def generatePyTriple(n):
    prdct = -1
    for a in range(n-1, 0, -1):
        if 2*a == n: continue
        b = (n*n - 2*n*a) / (2*n - 2*a)
        if b < 0 or b != int(b): continue
        b = int(b)
        c = n - a - b
        if c*c == (a*a + b*b):
            t = a*b*c
            if t > prdct:
                prdct = t
    return prdct
            
def cacheAllPyTriple(ub):
    for n in range(1, ub):
        pyt_cache[n] = generatePyTriple(n)
    
cacheAllPyTriple(3001)
#print(pyt_cache)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(pyt_cache[n])
