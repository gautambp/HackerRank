# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/quicksort-1---partition/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    p = arr[0]
    lp = []
    ep = []
    gp = []
    for i in arr:
        if i < p: lp.append(i)
        elif i == p: ep.append(i)
        else: gp.append(i)
    return lp + ep + gp 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
