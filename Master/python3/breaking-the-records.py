# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/breaking-the-records/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min_break = 0
    max_break = 0
    min_score = scores[0]
    max_score = scores[0]
    for i in range(1, len(scores)):
        if scores[i] > max_score:
            max_score = scores[i]
            max_break = max_break + 1
        if scores[i] < min_score:
            min_score = scores[i]
            min_break = min_break + 1
    return (max_break, min_break)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
