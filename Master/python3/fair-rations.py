# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/fair-rations/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    b_cnt = 0
    for i in range(len(B)):
        print(B)
        if B[i]%2 == 0: continue
        if i == len(B)-1:
            return 'NO'
        B[i] += 1
        B[i+1] += 1
        b_cnt += 2
    return str(b_cnt)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
