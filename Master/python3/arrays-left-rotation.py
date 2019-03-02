# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/arrays-left-rotation/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    result = []
    a_len = len(a)
    for i in range(a_len):
        idx = i + d
        if idx >= a_len:
            idx -= a_len
        result.append(a[idx])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
