# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-58-spiral-primes/problem
import random

def getSpiralDiagonalNos(n):
    if n == 1: return (1, 1, 1, 1)
    bot_right = n * n
    bot_left = bot_right - n + 1
    top_left = bot_left - n + 1
    top_right = top_left - n + 1
    return (top_right, top_left, bot_left, bot_right)

"""
def isPrime(n):
    if n == 3 or n == 5: return True
    if n%2 == 0 or n%3 == 0: return False
    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6
    return True
"""
def isPrime(n):
    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False
    k = 16
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

r = int(input())
cnt_prime = 0
cnt_total = 1
pr = 100
n = 1
while pr >= r:
    n += 2
    (tr, tl, bl, br) = getSpiralDiagonalNos(n)
    if isPrime(tr): cnt_prime += 1
    if isPrime(tl): cnt_prime += 1
    if isPrime(bl): cnt_prime += 1
    #if isPrime(br): cnt_prime += 1
    cnt_total += 4
    pr = 100 * cnt_prime/cnt_total
print(n)

