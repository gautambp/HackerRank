# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-27-quadratic-primes/problem

def is_prime(n):
    if n % 2 == 0 or n%3 == 0 or n%5 == 0 or n%7 == 0 or n%11 == 0 or n%13 == 0:
         return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

def init(ub):
    is_prime_nos = [False]*ub
    is_prime_nos[2] = is_prime_nos[3] = is_prime_nos[5] = True
    is_prime_nos[7] = is_prime_nos[11] = is_prime_nos[13] = True
    for i in range(17, ub, 2):
        is_prime_nos[i] = is_prime(i)
    return is_prime_nos

def solve_quad(n, a, b):
    return n**2 + n * a + b

def get_prime_seq_len(a, b):
    n = 0
    while is_prime_nos[solve_quad(n, a, b)]:
        n += 1
    return n

is_prime_nos = init(30000)

N = int(input())
longest_seq = (0, 0, 0)
for a in range(1, N+1, 2):
    if a%2 == 0: continue
    for b in range(1, N+1, 2):
        if not is_prime_nos[b]: continue
        n = get_prime_seq_len(a, b)
        if longest_seq[2] < n:
            longest_seq = (a, b, n)
        n = get_prime_seq_len(-1*a, b)
        if longest_seq[2] < n:
            longest_seq = (-1*a, b, n)
print('{} {}'.format(longest_seq[0], longest_seq[1]))
