# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/zeros-and-ones/problem
import numpy
numpy.set_printoptions(legacy='1.13')
s = [int(i) for i in input().split()]
print(numpy.zeros(s, dtype = numpy.int))
print(numpy.ones(s, dtype = numpy.int))
