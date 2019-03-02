# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-13-large-sum/problem
sum = 0
n = int(input())
for i in range(n):
    sum += int(input())
print(str(sum)[:10])
