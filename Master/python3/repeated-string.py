# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/repeated-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    cnt = 0
    s_len = len(s)
    for i in range(s_len):
        if s[i] == 'a':
            cnt += int(n/s_len)
            if n%s_len > i:
                cnt += 1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
