# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/gemstones/problem
#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the gemstones function below.
def gemstones(arr):
    g_cnt = 0
    for i in string.ascii_lowercase:
        found = True
        for s in arr:
            if s.find(i) == -1:
                found = False
                break
        if found:
            g_cnt += 1
    return g_cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
