# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/transpose-and-flatten/problem
import numpy

(n, m) = list(map(int,input().split()))
l1 = [None]*n
for i in range(n):
    l1[i] = list(map(int,input().split()))
a = numpy.array(l1)
print(numpy.transpose(a))
print(a.flatten())
