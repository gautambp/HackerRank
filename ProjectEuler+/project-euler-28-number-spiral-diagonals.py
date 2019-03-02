# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-28-number-spiral-diagonals/problem

for _ in range(int(input())):
    n = (int(input())-1)//2
    total_sum = ((16 * n**3 + 26 * n)//3 + (10 * n**2 + 1))
    print(int(total_sum) % 1000000007)
