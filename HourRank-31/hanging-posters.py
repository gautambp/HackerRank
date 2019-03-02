# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/HourRank-31/hanging-posters/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER_ARRAY wallPoints
#  3. INTEGER_ARRAY lengths
#

def solve(h, wallPoints, lengths):
    # Write your code here
    max_l = 0
    for w, l in zip(wallPoints, lengths):
        wh = w - 0.25 * l
        if wh > max_l:
            max_l = wh
    if max_l > h:
        return math.ceil(max_l - h)
    else:
        return 0
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    h = int(first_multiple_input[1])

    wallPoints = list(map(int, input().rstrip().split()))

    lengths = list(map(int, input().rstrip().split()))

    answer = solve(h, wallPoints, lengths)

    fptr.write(str(answer) + '\n')

    fptr.close()
