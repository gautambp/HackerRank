# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/min-and-max/problem
import numpy

s = input().split()
n = int(s[0])
m = int(s[1])
l = [None]*n
for i in range(n):
    l[i] = list(map(int,input().split()))
a = numpy.array(l)
print(numpy.max(numpy.min(a, axis=1)))

