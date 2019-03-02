# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/inner-and-outer/problem
import numpy

aLine = input()
l = aLine.split(' ')
a = []
for n in l:
    a.append(int(n))
aLine = input()
l = aLine.split(' ')
b = []
for n in l:
    b.append(int(n))
A = numpy.array(a)
B = numpy.array(b)
print(numpy.inner(A, B))
print(numpy.outer(A, B))

