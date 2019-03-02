# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/dynamic-array/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    seqList = [None]*n
    for i in range(n):
        seqList[i] = []
    lastAnswer = 0
    result = []
    for q in queries:
        if q[0] == 1:
            idx = (q[1] ^ lastAnswer) % n
            seqList[idx].append(q[2])
        else:
            idx = (q[1] ^ lastAnswer) % n
            j = q[2]%len(seqList[idx])
            lastAnswer = seqList[idx][j]
            result.append(lastAnswer)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
