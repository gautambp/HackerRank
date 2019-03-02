# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/find-digits/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    result = 0
    d = n
    while True:
        if n < 10:
            if n > 0 and d % n == 0:
                result += 1
            break
        nd = n - 10*int(n/10)
        if nd > 0 and d % nd == 0:
            result += 1
        n = int(n/10)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
