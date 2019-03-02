# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e = 100
    s = 0
    done = False
    while not done:
        s += k
        if s >= len(c):
            done = True
            s = s%len(c)
        if c[s] == 1:
            e -= 2
        e -= 1
        print(s)
        print(e)
    return e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
