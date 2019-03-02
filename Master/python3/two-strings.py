# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/two-strings/problem
#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    for ch in string.ascii_lowercase:
        if s1.find(ch) >= 0 and s2.find(ch) >= 0:
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
