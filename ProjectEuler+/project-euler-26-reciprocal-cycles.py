# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-26-reciprocal-cycles/problem
cyclic_primes = [
        7
        #, 17, 19, 23, 29, 47, 59, 61, 97, 109, 113, 131, 149, 
        #167, 179, 181, 193, 223, 229, 233, 257, 263, 269, 313, 
        #337, 367, 379, 383, 389, 419, 433, 461, 487, 491, 499, 
        #503, 509, 541, 571, 577, 593, 619, 647, 659, 701, 709, 
        #727, 743, 811, 821, 823, 857, 863, 887, 937, 941, 953, 
        #971, 977, 983,
        #1193, 1931, 3119, 3779, 7793, 7937, 9311, 9377 
]

def is_prime(n):
    for i in range(3, int(n ** 0.5), 2):
        if n%i == 0:
            return False
    return True

def find_cycle(n):
    f = [0]*n
    f[1] = 1
    m = 1
    i = 2
    while True:
        m *= 10
        p = m % n
        if p == 0: return 0
        if f[p]: return i-f[p]
        f[p] = i
        i += 1
        m = p
    
def is_cyclic(n):
    nc = find_cycle(n)
    return nc == n-1

def init(ub):
    ans = [0]*(ub+1)
    ans[4] = ans[5] = ans[6] = ans[7] = 3
    ans[8] = ans[9] = ans[10] = 7
    last_ans = 7
    for i in range(11, ub+1):
        ans[i] = last_ans
        if i%2 == 0 or i%3 == 0 or i%5 == 0: continue
        if is_prime(i) and is_cyclic(i):
            last_ans = i
    return ans

ans = init(10000)
for _ in range(int(input())):
    n = int(input())
    print(ans[n])
