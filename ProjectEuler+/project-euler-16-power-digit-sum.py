# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-16-power-digit-sum/problem
import math

q = int(input().strip())
for i in range(q):
    n = int(input().strip())
    tp = int(2 ** n)
    tp_sum = 0
    for j in str(tp):
        tp_sum += int(j)
    print(tp_sum)
