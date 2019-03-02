# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
import numpy

numpy.set_printoptions(legacy='1.13')
l = list(map(float,input().split()))
a = numpy.array(l)
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))


