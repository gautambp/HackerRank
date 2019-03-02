# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/bigger-is-greater/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    w_len = len(w)
    idx = w_len-1
    last_ch = w[idx]
    while idx > 0 and w[idx-1] > w[idx]:
        idx -= 1
    print('{} {} {}'.format(w[:idx-1], last_ch, w[idx-1:-1]))
    result = w[:idx-1] + last_ch + w[idx-1:-1]
    if result > w:
        return result
    elif result == w:
        return 'no answer'
    else:
        return result[w_len-1] + result[:-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
