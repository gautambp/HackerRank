# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/minimum-distances/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    d = {}
    for i in range(len(a)):
        if a[i] not in d:
            d[a[i]] = [i]
        else:
            d[a[i]].append(i)
    min_dist = -1
    for k in d:
        l = d[k]
        if len(l) > 1:
            for j in range(len(l)-1):
                if min_dist == -1 or l[j+1] - l[j] < min_dist: 
                    min_dist = l[j+1] - l[j]
    return min_dist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
