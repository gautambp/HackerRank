# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    cnt = 0
    for d in range(i, j+1):
        ds = str(d)
        ds = ds[::-1]
        rd = int(ds)
        if abs(d - rd) % k == 0:
            cnt += 1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
