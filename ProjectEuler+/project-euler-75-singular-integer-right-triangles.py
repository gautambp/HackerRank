# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-75-singular-integer-right-triangles/problem
lb = 12
ub = 1600
pyt_cache = {}
rat_cnt = [0]*5000001

def generatePyTriple(n):
    for a in range(n-1, 0, -1):
        if 2*a == n: continue
        b = (n*n - 2*n*a) / (2*n - 2*a)
        if b < 0 or b != int(b): continue
        b = int(b)
        c = n - a - b
        if c*c == (a*a + b*b):
            s = a+b+c
            k = ((a,b,c) if b>a else (b,a,c))
            if s not in pyt_cache:
                pyt_cache[s] = ((a,b,c) if b>a else (b,a,c))
            else:
                if isinstance(pyt_cache[s], int): 
                    pyt_cache[s] += 1
                elif pyt_cache[s] != k: 
                    pyt_cache[s] = 2
            
def cacheAllPyTriple():
    for n in range(lb, ub):
        generatePyTriple(n)
    cnt = 0
    for i in range(lb, 5000001):
        if i in pyt_cache and isinstance(pyt_cache[i], tuple):
            cnt += 1
        rat_cnt[i] = cnt
    
cacheAllPyTriple()
for _ in range(int(input())):
    n = int(input())
    print(rat_cnt[n])
