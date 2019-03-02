# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/insertion-sort---part-1/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    i = arr[n-1]
    found = False
    for j in range(n-2, -1, -1):
        if arr[j] > i:
            arr[j+1] = arr[j]
        else:
            arr[j+1] = i
            found = True
        print(' '.join(map(str,arr)))
        if found: break
    if not found:
        arr[0] = i
        print(' '.join(map(str,arr)))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
