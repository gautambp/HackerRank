# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/append-and-delete/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    op_cnt = 0
    while True:
        if op_cnt > k:
            break
        if s == t:
            break
        if len(s) > len(t):
            s = s[:-1]
            op_cnt += 1
        elif len(s) == len(t):
            s = s[:-1]
            op_cnt += 1
        else:
            if t.startswith(s):
                c = t[len(s)]
                s = s + c
                op_cnt += 1
                # append
            else:
                s = s[:-1]
                op_cnt += 1
    if s == t and op_cnt <= k:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
