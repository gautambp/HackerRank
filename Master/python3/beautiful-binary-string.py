# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/beautiful-binary-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    cnt = 0
    n = len(b)
    p = b.find('010')
    while p >= 0:
        if p+4 < n and b[p+3] == '1' and b[p+4] == '0':
            b = b[:p+2] + '1' + b[p+3:]
            cnt += 1
        else:
            b = b[:p+1] + '0' + b[p+2:]
            cnt += 1
        print(b)
        p = b.find('010')
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
