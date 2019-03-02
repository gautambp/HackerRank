# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/alternating-characters-/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    cnt = 0
    last_ch = None
    for ch in s:
        if last_ch == None or last_ch != ch:
            last_ch = ch
        else:
            cnt += 1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
