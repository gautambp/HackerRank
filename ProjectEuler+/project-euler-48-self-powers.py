# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-48-self-powers/problem
m = 10000000000
n = int(input())
s = 0
for i in range(1, n+1):
    s = (s + pow(i, i, m)) % m
print(s)
