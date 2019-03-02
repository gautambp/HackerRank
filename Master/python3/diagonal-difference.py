# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/diagonal-difference/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    p_sum = 0;
    s_sum = 0;
    arr_len = len(arr);
    for idx in range(arr_len):
        p_sum = p_sum + arr[idx][idx];
        s_sum = s_sum + arr[idx][arr_len-idx-1];
    return abs(p_sum - s_sum);

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
