# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/flatland-space-stations/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c_len = len(c)
    c.sort()
    max_d = c[0]
    for i in range(1, c_len):
        #print('{} {}'.format(i, max_d))
        d = (c[i]+c[i-1])//2
        max_d = (d-c[i-1] if d-c[i-1] > max_d else max_d)
        max_d = (c[i]-d-1 if c[i]-d-1 > max_d else max_d)
    if n-c[c_len-1]-1 > max_d:
        max_d = n-c[c_len-1]-1
    return max_d

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
