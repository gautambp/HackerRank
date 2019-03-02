# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/super-reduced-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby

# Complete the superReducedString function below.
def superReducedString(s):
    old_s = s
    new_s = ''
    while True:
        new_s = ''
        for k, g in groupby(old_s):
            if len(list(g))%2 == 1:
                new_s += k
        if new_s == old_s:
            break
        old_s = new_s
    return (new_s if len(new_s) > 0 else 'Empty String')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
