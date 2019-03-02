# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/concatenate/problem
import numpy

(n, m, p) = list(map(int,input().split()))
l1 = [None]*n
for i in range(n):
    l1[i] = list(map(int,input().split()))
a = numpy.array(l1)

l2 = [None]*m
for i in range(m):
    l2[i] = list(map(int,input().split()))
b = numpy.array(l2)

print(numpy.concatenate((a,b)))
