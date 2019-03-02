# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-7-10001st-prime/problem
ul = 10001
prime_no_l = [None]*ul

def isPrime(n):
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0: return False
    return True
    
def init():
    i = 21
    idx = 8
    prime_no_l[0] = 2
    prime_no_l[1] = 3
    prime_no_l[2] = 5
    prime_no_l[3] = 7
    prime_no_l[4] = 11
    prime_no_l[5] = 13
    prime_no_l[6] = 17
    prime_no_l[7] = 19
    while idx < ul:
        if i%5 != 0:
            if isPrime(i):
                prime_no_l[idx] = i
                idx += 1
        i += 2

init()
for _ in range(int(input())):
    n = int(input())
    print(prime_no_l[n-1])

