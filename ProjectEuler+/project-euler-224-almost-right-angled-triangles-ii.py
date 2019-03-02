# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-224-almost-right-angled-triangles-ii/problem

def solve(n):
    cnt = 0
    a = 2
    while True:
        b = (a * a / 2)
        c = ((a * a) + 2) / 2
        if (a + b + c) > n:
            break
        if (a*a + b*b) == (c*c - 1):
            cnt += 1
        a += 2
    return cnt
        
q = int(input())
for i in range(q):
    n = int(input())
    print(solve(n))
