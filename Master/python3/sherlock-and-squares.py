# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/sherlock-and-squares/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    result = 0
    a_low = int(math.sqrt(a))
    b_high = int(math.sqrt(b))+1
    for i in range(a_low, b_high):
        i_sqr = i*i
        if i_sqr >= a and i_sqr <= b:
            result += 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
