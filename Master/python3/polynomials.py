# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/polynomials/problem
import numpy
numpy.set_printoptions(legacy='1.13')
l = list(map(float,input().split()))
x = float(input())
print(numpy.polyval(l, x))
