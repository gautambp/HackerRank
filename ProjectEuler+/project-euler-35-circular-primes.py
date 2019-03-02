# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-35-circular-primes/problem
import math

prime_flag_cache = [None]*1000001

def isPrime(n):
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def init():
    prime_flag_cache[0] = False
    for i in range(20):
        if i in [1, 2, 3, 5, 7, 11, 13, 17, 19]:
            prime_flag_cache[i] = True
        else:
            prime_flag_cache[i] = False
    for i in range(21, 1000001):
        if i%2 == 0 or i%3 == 0 or i%5 == 0 or i%7 == 0 or i%11 == 0 or i%13 == 0 or i%17 == 0 or i%19 == 0:
            prime_flag_cache[i] = False
        else:
            prime_flag_cache[i] = isPrime(i)
        
def rotateNum(n):
    l = []
    s = list(str(n))
    last_idx = len(s)-1
    for i in range(last_idx):
        first_ch = s[0]
        for j in range(last_idx):
            s[j] = s[j+1]
        s[last_idx] = first_ch
        l.append(int(''.join(s)))
    return l
        
    
init()
n = int(input())
p_sum = 0
for i in range(2, n):
    if prime_flag_cache[i]:
        all_match = True
        for j in rotateNum(i):
            if not prime_flag_cache[j]:
                all_match = False
                break
        if all_match:
            p_sum += i

print(p_sum)
