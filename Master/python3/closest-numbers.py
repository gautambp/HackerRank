# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/closest-numbers/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    min_diff = 9999999999
    min_diff_l = []
    for i in range(len(arr)-1):
        d = abs(arr[i+1]-arr[i])
        if d < min_diff:
            min_diff = d
            min_diff_l = [arr[i], arr[i+1]]
        elif d == min_diff:
            min_diff_l.append(arr[i])
            min_diff_l.append(arr[i+1])
    return min_diff_l


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
