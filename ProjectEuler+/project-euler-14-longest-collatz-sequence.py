# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-14-longest-collatz-sequence/problem
ub = 5*(10 ** 6)+1
chain_length = [None]*ub
max_chain_length = [None]*ub

def getChainLength(num):
    if num < ub and chain_length[num]:
        return chain_length[num]
    c_len = 0
    n = num
    while n > 1:
        if n%2 == 0:
            n >>= 1
        else:
            n = 3*n + 1
        c_len += 1
        if n < ub and chain_length[n]:
            c_len += chain_length[n]
            break
    if num < ub: chain_length[num] = c_len
    return c_len
    
def init(n):
    i = 1
    c_len = 0
    while i < n:
        chain_length[i] = c_len
        i *= 2
        c_len += 1
    
def solve(n):
    init(n)
    max_c_len = 0
    max_n = 0
    for i in range(2, n+1):
        cl = getChainLength(i)
        if cl >= max_c_len:
            max_c_len = cl
            max_n = i
        max_chain_length[i] = max_n
    
q = int(input())
max_n = 0
a = []
for i in range(q):
    n = int(input())
    a.append(n)
    if n > max_n:
        max_n = n

solve(max_n)
for i in a:
    if i==1:
        print(i)
    else:
        print(max_chain_length[i])
