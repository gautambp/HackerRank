# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/counting-sort-1/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    cl = [0]*100
    for i in arr:
        cl[i] += 1
    return cl

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
