# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-25-n-digit-fibonacci-number/problem
fib_digit_cache = {}

def initFibDigitCache():
    f1 = 1
    f2 = 1
    d_size = 10
    i = 3
    while True:
        f = f1 + f2
        f1 = f2
        f2 = f
        if f >= d_size:
            idx = len(str(d_size))
            fib_digit_cache[idx] = i
            d_size *= 10
            if idx >= 5000:
                break
        i += 1

initFibDigitCache()
for _ in range(int(input())):
    idx = int(input())
    print(fib_digit_cache[idx])

