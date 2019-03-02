# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/camelcase/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    return 1+sum([1 for i in s if i.isupper()])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
