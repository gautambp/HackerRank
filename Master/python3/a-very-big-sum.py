# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/a-very-big-sum/problem
#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    return reduce(lambda x, y: x+y, ar);

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
