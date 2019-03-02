# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/chocolate-feast-/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    def chocFeastWrapper(w):
        if w < m:
            return 0
        ch = w // m
        w = w % m
        w += ch
        return ch + chocFeastWrapper(w)
    ch = n // c
    return ch + chocFeastWrapper(ch)        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
