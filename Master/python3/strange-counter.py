# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/strange-counter/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    n = t
    b = 0
    bs = 0
    s = 0
    while n>0:
        bs = 3 * (2 ** b)
        n -= bs
        s += bs
        b += 1
    return s-t+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
