# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/circular-array-rotation/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    k_mod = k % len(a)
    result = []
    for i in range(len(queries)):
        idx = queries[i] - k_mod
        if idx < 0:
            idx += len(a)
        result.append(a[idx])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
