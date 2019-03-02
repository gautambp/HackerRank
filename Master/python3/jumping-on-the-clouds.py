# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    cnt = 0
    c_len = len(c)
    idx = 0
    while idx <= c_len-1:
        if idx+2 < c_len and c[idx+2] == 0:
            cnt += 1
            idx += 2
        elif idx+1 < c_len and c[idx+1] == 0:
            cnt += 1
            idx += 1
        else:
            idx += 1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
