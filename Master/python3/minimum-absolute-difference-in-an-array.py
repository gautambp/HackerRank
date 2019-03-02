# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = 99999999999
    for i in range(1, len(arr)):
        d = abs(arr[i]-arr[i-1])
        if d < min_diff:
            min_diff = d
    return min_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
