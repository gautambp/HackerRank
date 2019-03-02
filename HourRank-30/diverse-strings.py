# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/HourRank-30/diverse-strings/problem
#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def solve(n, k):
    # Write your code here
    if n == 1 and n == k:
        return string.ascii_lowercase[:k]
    kk = k*(k+1)
    if n == kk-1:
        s = string.ascii_lowercase[k-1]
        for i in range(k-1, 0, -1):
            cnt = (k-i+1)
            ss = string.ascii_lowercase[i-1]*cnt
            s = ss + s + ss
        return s
    else:
        return 'NONE'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        res = solve(n, k)

        fptr.write(res + '\n')

    fptr.close()
