# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/array-mathematics/problem
import numpy
numpy.set_printoptions(legacy='1.13')
s = input().split()
n = int(s[0])
m = int(s[1])
l1 = [None]*n
for i in range(n):
    l1[i] = list(map(int,input().split()))
a = numpy.array(l1)
l2 = [None]*n
for i in range(n):
    l2[i] = list(map(int,input().split()))
b = numpy.array(l2)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)
