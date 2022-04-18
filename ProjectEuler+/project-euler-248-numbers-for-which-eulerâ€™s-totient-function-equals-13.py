# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-248-numbers-for-which-euler’s-totient-function-equals-13/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

m, q = input().split()
b = 6227180929
for _ in range(int(q)):
    i = int(input())
    print(b*i, end=' ')
