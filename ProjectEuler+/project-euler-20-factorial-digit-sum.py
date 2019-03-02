# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-20-factorial-digit-sum/problem
fact_cache = [None]*1000
fact_sum_cache = [None]*1000

def fact(n):
    if n <= 1:
        return 1
    if fact_cache[n]:
        return fact_cache[n]
    f = n * fact(n-1)
    fact_cache[n] = f
    return f

def fact_sum(n):
    if fact_sum_cache[n]:
        return fact_sum_cache[n]
    f = fact(n)
    s = sum(list(map(int, str(f))))
    fact_sum_cache[n] = s
    return s

q = int(input())
for _ in range(q):
    n = int(input())
    print(fact_sum(n))
