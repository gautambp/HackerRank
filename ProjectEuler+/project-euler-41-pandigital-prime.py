# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-41-pandigital-prime/problem
import math
from itertools import permutations

small_prime_l = [2, 3, 5, 7, 11, 13, 17, 19]
non_prime_end_digits = [2, 4, 5, 6, 8]
prime_pandigital_l = []

def is_prime(n):
    #if any(n % i == 0 for i in small_prime_l): return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n%i == 0:
            return False
    return True

def buildNoFromDigits(l):
    m = 1
    no = 0
    len_l = len(l)
    for i in range(len_l):
        no += m * l[len_l-i-1]
        m *= 10
    return no

def init(n):
    l = [i for i in range(n, 0, -1)]
    for i in permutations(l, n):
        if i[n-1] in non_prime_end_digits: continue
        no = buildNoFromDigits(i)
        if is_prime(no):
            prime_pandigital_l.append(no)    

for i in range(9, 1, -1): init(i)

for _ in range(int(input())):
    ul = int(input())
    found = False
    for i in prime_pandigital_l:
        if i <= ul:
            print(i)
            found = True
            break
    if not found:
        print(-1)
