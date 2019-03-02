# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-69-totient-maximum/problem
for _ in range(int(input())):
    n = int(input())
    if n <= 3:
        print(2)
    elif n < 6:
        print(4)
    else:
        print(6 * (n // 6))
