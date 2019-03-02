# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/string-construction-/problem
#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the stringConstruction function below.
def stringConstruction(s):
    c = 0
    for ch in string.ascii_lowercase:
        if s.find(ch) >= 0:
            c += 1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
