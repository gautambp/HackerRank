# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-169-exploring-the-number-of-different-ways-a-number-can-be-expressed-as-a-sum-of-powers-of-2/problem
# Project Euler #169: Exploring the number of different ways a number can be expressed as a sum of powers of 2.
# https://www.hackerrank.com/contests/projecteuler/challenges/euler169/problem

sd_series_d = {0:0, 1:1}

def fn(n):
    if n in sd_series_d:
        return sd_series_d[n]
    if n%2 == 0:
        val = fn(n//2)
        sd_series_d[n] = val
        return val
    else:
        val = fn((n-1)//2)
        val += fn((n+1)//2)
        sd_series_d[n] = val
        return val

n = int(input())
print(fn(n+1))
