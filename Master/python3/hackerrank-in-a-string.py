# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    t = 'hackerrank'
    t_idx = 0
    s_pos = 0
    while s_pos < len(s) and t_idx < len(t):
        f = s.find(t[t_idx], s_pos)
        if f < 0:
            return 'NO'
        t_idx += 1
        s_pos = f+1
    if t_idx < len(t): return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
