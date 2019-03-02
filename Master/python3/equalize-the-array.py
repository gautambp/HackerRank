# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/equalize-the-array/problem
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the equalizeArray function below.
def equalizeArray(arr):
    max_freq = 0
    freq = Counter(arr)
    for k in freq:
        if freq[k] > max_freq:
            max_freq = freq[k]
    return len(arr)-max_freq

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
