# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/insertion-sort---part-2/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for p in range(1, n):
        i = arr[p]
        found = False
        for j in range(p-1, -1, -1):
            if i < arr[j]:
                arr[j+1] = arr[j]
            else:
                arr[j+1] = i
                found = True
            if found: break
        if not found:
            arr[0] = i
        print(' '.join(map(str,arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
