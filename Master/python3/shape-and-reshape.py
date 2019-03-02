# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/shape-and-reshape/problem
import numpy

l = list(map(int,input().split()))
a = numpy.array(l)
print(numpy.reshape(a, (3, 3)))