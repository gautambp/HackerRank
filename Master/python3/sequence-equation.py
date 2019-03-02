# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/sequence-equation/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    d = {}
    for i in range(len(p)): d[p[i]] = i+1
    l = []
    for i in range(1, len(p)+1):
        l.append(d[d[i]])
    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
