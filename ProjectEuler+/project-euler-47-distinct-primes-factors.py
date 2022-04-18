# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-47-distinct-primes-factors/problem
import math

def prime_factor_count(n):
    p = [1]*(n+1)
    p[0], p[1] = 0, 0
    for i in range(2,n+1):
        if p[i] == 1:
            for idx in range(1,n//i+1):
                p[i*idx]+=1            
            for po in range(2,int(math.log(n,i))+1):
                p[i**po] = 0
    return p

s = input().split()
n, k = int(s[0]), int(s[1])
A = prime_factor_count(n+k)
i = 14
while i <= n: 
    if k == 2 and A[i] == 3 and A[i+1] == 3:
        print(i)
    elif k == 3 and A[i] == 4 and A[i+1] == 4 and A[i+2] == 4:
        print(i)
    elif k == 4 and A[i] == 5 and A[i+1] == 5 and A[i+2] == 5 and A[i+3] == 5:
        print(i)
    i += 1
