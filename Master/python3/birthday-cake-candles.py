# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    max_val = ar[0];
    for val in ar:
        if val > max_val:
            max_val = val;
    return sum(1 for val in ar if val == max_val);

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
