# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-37-truncatable-primes/problem
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
        if i in [2, 3, 5, 7, 11, 13, 17, 19]:
            prime_flag_cache[i] = True
        else:
            prime_flag_cache[i] = False
    for i in range(21, 1000001):
        if i%2 == 0 or i%3 == 0 or i%5 == 0 or i%7 == 0 or i%11 == 0 or i%13 == 0 or i%17 == 0 or i%19 == 0:
            prime_flag_cache[i] = False
        else:
            prime_flag_cache[i] = isPrime(i)

left_nos = ['2', '3', '5', '7']
middle_nos = ['1', '3', '7', '9']
right_nos = ['3', '7']

n = int(input())
init()
p_sum = 0
for i in range(11, n):
    if not prime_flag_cache[i]:
        continue
    found = True
    s = str(i)
    if s[0] not in left_nos:
        continue
    last_idx = len(s)-1
    for idx in range(1, len(s)):
        if idx == last_idx and s[idx] not in right_nos:
            found = False
            break
        if idx < last_idx and s[idx] not in middle_nos:
            found = False
            break
        new_n = int(''.join(s[idx:]))
        if not prime_flag_cache[new_n]:
            found = False
            break
        new_n = int(''.join(s[:len(s)-idx]))
        if not prime_flag_cache[new_n]:
            found = False
            break
        
    if found:
        p_sum += i

print(p_sum)        