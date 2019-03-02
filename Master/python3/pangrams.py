# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/pangrams/problem
#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the pangrams function below.
def pangrams(s):
    s1 = s.lower()
    for ch in string.ascii_lowercase:
        if s1.find(ch) < 0:
            return 'not pangram'
    return 'pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
