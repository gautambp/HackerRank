# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/running-time-of-algorithms/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(l):
    cnt = 0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           cnt += 1
           j -= 1
        l[j+1] = key
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
