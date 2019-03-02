# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/sum-and-prod/problem
import numpy
numpy.set_printoptions(legacy='1.13')
s = input().split()
n = int(s[0])
m = int(s[1])
l = [None]*n
for i in range(n):
    l[i] = list(map(int,input().split()))
a = numpy.array(l)
print(numpy.prod(numpy.sum(a, axis=0)))
