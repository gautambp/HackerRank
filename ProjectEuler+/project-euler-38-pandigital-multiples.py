# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-38-pandigital-multiples/problem

def isPandigital(l, k):
    for i in range(1, k+1):
        if l.count(str(i)) != 1: return False
    return True

(n, k) = [int(i) for i in input().strip().split(' ')]

for i in range(2, n):
    m = 1
    l = ''
    while True:
        l = l + str(i*m)
        if len(l) > k:
            break
        elif len(l) == k:
            if isPandigital(l, k):
                print(i)
            break
        m += 1
