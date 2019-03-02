# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-36-double-base-palindromes/problem
upper_limit = 100001
pal_cache = []

def isPalindrome(s):
    len_s = len(s)
    l = int(len_s/2)
    while l >= 0:
        if s[l] != s[len_s-l-1]:
            return False
        l -= 1
    return True

def n2b(n, b):
    if n == 0:
        return 0
    d = []
    while n:
        d.append(int(n % b))
        n = int(n/b)
    return ''.join(map(str,d[::-1]))
        
def init():
    # handle single digit palindromes
    for i in range(1, 10):
        pal_cache.append(i)
    # handle double digit palindromes
    for i in range(11, 100, 11):
        pal_cache.append(i)
    # handle three & four digit palindromes
    for i in range(1, 10):
        for j in range(0, 10):
            p_no = i*100 + j*10 + i
            pal_cache.append(p_no)
            p_no = i*1000 + j*100 + j*10 + i
            pal_cache.append(p_no)
    # handle five & six digit palindromes
    for i in range(1, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                p_no = i*10000 + j*1000 + k*100 + j*10 + i
                pal_cache.append(p_no)
                p_no = i*100000 + j*10000 + k*1000 + k*100 + j*10 + i
                pal_cache.append(p_no)
            
init()

(ns, ks) = input().split(' ')
n = int(ns)
k = int(ks)
pal_sum = 0
for i in range(len(pal_cache)):
    pd = pal_cache[i]
    if pd > n:
        continue
    pk = n2b(pd, k) 
    if isPalindrome(pk):
        pal_sum += pd
print(pal_sum)
