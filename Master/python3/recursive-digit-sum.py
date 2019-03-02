# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/recursive-digit-sum/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    def recSuperDigit(d):
        if len(d) == 1: return int(d)
        s = 0
        for i in d:
            s += int(i)
        return recSuperDigit(str(s))
    sd = recSuperDigit(n)
    return recSuperDigit(str(sd * k))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
