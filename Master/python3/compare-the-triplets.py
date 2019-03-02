# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/compare-the-triplets/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    a_score = (a[0] > b[0]) + (a[1] > b[1]) + (a[2] > b[2]);
    b_score = (a[0] < b[0]) + (a[1] < b[1]) + (a[2] < b[2]);
    return [a_score, b_score];

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
