# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/eye-and-identity/problem
import numpy
numpy.set_printoptions(legacy='1.13')
s = input().split()
n = int(s[0])
m = int(s[1])
print(numpy.eye(n, m))
