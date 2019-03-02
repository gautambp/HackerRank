# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/picking-numbers/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    max_size = 0
    for i in range(1, 100):
        size = 0
        for n in a:
            if (n == i or n == (i+1)):
                size += 1
        if size > max_size:
            max_size = size
    return max_size

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
