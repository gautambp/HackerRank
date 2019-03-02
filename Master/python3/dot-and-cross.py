# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/dot-and-cross/problem
import numpy
numpy.set_printoptions(legacy='1.13')
n = int(input())
l = [None]*n
for i in range(n):
    l[i] = list(map(int,input().split()))
A = numpy.array(l)
l2 = [None]*n
for i in range(n):
    l2[i] = list(map(int,input().split()))
B = numpy.array(l2)

print(numpy.dot(A, B))
