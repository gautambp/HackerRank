# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-42-coded-triangle-numbers/problem
import math

def getTriangularNo(tn):
    if tn < 0: return -1
    s = math.sqrt(tn * 8 + 1)
    if int(s) == s:
        return int((int(s)-1)/2)
    return -1

for _ in range(int(input())):
    tn = int(input())
    print(getTriangularNo(tn))
