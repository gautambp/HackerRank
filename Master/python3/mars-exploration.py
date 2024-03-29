# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/mars-exploration/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    cnt = 0
    for i in range(0, len(s), 3):
        if s[i] != 'S': cnt += 1
        if s[i+1] != 'O': cnt += 1
        if s[i+2] != 'S': cnt += 1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
