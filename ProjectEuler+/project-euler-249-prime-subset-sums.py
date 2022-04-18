# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-249-prime-subset-sums/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

upper_bound = 7001
prime_ub = 1000000
is_prime_no = [0]*prime_ub
prime_sum = [0]*upper_bound

def is_prime(n):
    for i in range(2, int(n ** 0.5)+1):
        if n%i == 0: return 0
    return 1

def init_prime_nos():
    is_prime_no[2] = is_prime_no[3] = is_prime_no[5] = 1
    for i in range(7, prime_ub, 2):
        is_prime_no[i] = is_prime(i)

def init_prime_sum():
    prime_sum[2] = 1
    prime_sum[3] = 3
    s = set()
    s.add(2)
    s.add(3)
    s.add(5)
    for i in range(4, upper_bound):
        if is_prime_no[i] == 1:
            s = calc_prime_sum(i, s)
            #print('{} {} {}'.format(i, prime_sum[i], s))
        else:
            prime_sum[i] = prime_sum[i-1]

def calc_prime_sum(n, s):
    ps = prime_sum[n-1] + is_prime_no[n]
    s.add(n)
    for val in list(s):
        ps += is_prime_no[val+n]
        s.add(val+n)
    prime_sum[n] = ps
    return s

def init():
    init_prime_nos()
    init_prime_sum()

init()
k = int(input())
l = list(map(int, input().split()))
for i in l:
    print(prime_sum[i-1], end=' ')
