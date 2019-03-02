# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-34-digit-factorials/problem
fact_cache = [None]*10

def init():
    fact_cache[0] = 1
    fact_cache[1] = 1
    fact = 1
    for i in range(2, 10):
        fact *= i
        fact_cache[i] = fact
        
init()
n = int(input())
total = 0
for i in range(10, n+1):
    sum = 0
    for j in str(i):
        sum += fact_cache[int(j)]
    if sum % i == 0:
        #print('{} {}'.format(i, sum))
        total += i
print(total)
