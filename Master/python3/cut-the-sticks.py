# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/cut-the-sticks/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    print(arr)
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [1]
    min_val = 1001
    for i in arr:
        if i < min_val:
            min_val = i
    mod_arr = list(filter(lambda a: a > 0, map(lambda x: x - min_val, arr)))
    l = cutTheSticks(mod_arr)
    return [len(arr), *l] 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
