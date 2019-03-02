# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/counting-sort-2/problem
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
    l = []
    for i in range(100):
        j = cl[i]
        while j > 0:
            l.append(i)
            j -= 1
    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
