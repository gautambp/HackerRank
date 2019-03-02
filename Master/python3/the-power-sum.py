# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/the-power-sum/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the powerSum function below.
def powerSum(X, N):
    def recPowerSum(x, k):
        if k ** N < x:
            return recPowerSum(x, k+1) + recPowerSum(x-(k ** N), k+1)
        elif k ** N == x:
            return 1
        else:
            return 0
    return recPowerSum(X, 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
