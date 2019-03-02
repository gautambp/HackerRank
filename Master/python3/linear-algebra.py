# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/linear-algebra/problem
import numpy
numpy.set_printoptions(legacy='1.13')
n = int(input())
l = [None]*n
for i in range(n):
    l[i] = list(map(float,input().split()))
a = numpy.array(l)
print(numpy.linalg.det(a))
