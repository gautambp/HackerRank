# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/array-manipulation/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    a = [0]*(n+1)
    max_val = 0
    for q in queries:
        for i in range(q[0], q[1]+1):
            a[i] += q[2]
            if a[i] > max_val:
                max_val = a[i]
    return max_val    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
