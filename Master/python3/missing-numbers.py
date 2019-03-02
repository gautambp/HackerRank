# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/missing-numbers/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    dl = [0]*101
    #b_max = max(brr)
    b_min = min(brr)
    for i in range(len(brr)):
        dl[brr[i]-b_min] += 1
        if i < len(arr):
            dl[arr[i]-b_min] -= 1
    result = []
    for i in range(101):
        if dl[i] > 0:
            result.append(i+b_min)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
