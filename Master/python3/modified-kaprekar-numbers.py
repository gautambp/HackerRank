# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/modified-kaprekar-numbers/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    found = False
    for i in range(p, q+1):
        i_sqr = i ** 2
        k_no = None
        if i_sqr == i: k_no = i
        elif i_sqr < 10 or i == 10 or i == 100 or i == 1000 or i == 10000 or i == 4879: continue
        elif i_sqr < 100 and i_sqr//10 + i_sqr%10 == i: k_no = i
        elif i_sqr < 1000 and (i_sqr//100 + i_sqr%100 == i or i_sqr//10 + i_sqr%10 == i): k_no = i
        elif i_sqr < 10000 and i_sqr//100 + i_sqr%100 == i: k_no = i
        elif i_sqr < 100000 and (i_sqr//100 + i_sqr%100 == i or i_sqr//1000 + i_sqr%1000 == i): k_no = i
        elif i_sqr < 1000000 and i_sqr//1000 + i_sqr%1000 == i: k_no = i
        elif i_sqr < 10000000 and (i_sqr//1000 + i_sqr%1000 == i or i_sqr//10000 + i_sqr%10000 == i): k_no = i
        elif i_sqr < 100000000 and i_sqr//10000 + i_sqr%10000 == i: k_no = i
        elif i_sqr < 1000000000 and (i_sqr//10000 + i_sqr%10000 == i or i_sqr//100000 + i_sqr%100000 == i): k_no = i
        elif i_sqr < 10000000000 and i_sqr//100000 + i_sqr%100000 == i: k_no = i
        if k_no:
            print(i, end=' ')
            found = True
    if not found:
        print('INVALID RANGE')

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
