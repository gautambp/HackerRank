# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/the-hurdle-race/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    max_h = height[0]
    for i in range(1, len(height)):
        if height[i] > max_h:
            max_h = height[i]
    if k > max_h:
        return 0
    else:
        return max_h - k


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
