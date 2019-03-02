# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/beautiful-triplets/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    a_len = len(arr)
    seq_cnt = 0
    for i in range(a_len-2):
        for j in range(i+1, a_len-1):
            if arr[j] - arr[i] == d:
                for k in range(j+1, a_len):
                    if arr[k] - arr[j] == d:
                        seq_cnt += 1
    return seq_cnt



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
