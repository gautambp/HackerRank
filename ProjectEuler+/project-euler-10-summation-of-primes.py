# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-10-summation-of-primes/problem
ul = 1000001
prime_no_l = [0]*ul

def isPrime(n):
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0: return False
    return True
    
def init():
    prime_no_l[2] = 2
    prime_no_l[3] = 5
    prime_no_l[4] = 5
    prime_no_l[5] = 10
    prime_no_l[6] = 10
    for i in range(7, ul):
        prime_no_l[i] = prime_no_l[i-1]
        if i%2 != 0 and i%3 != 0 and i%5 != 0 and isPrime(i):
            prime_no_l[i] += i            

init()
for _ in range(int(input())):
    n = int(input())
    print(prime_no_l[n])


