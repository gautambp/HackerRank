# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/sales-by-match/problem
#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce
from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    freqs = Counter(ar)
#    freqs = [(item, ar.count(item)) for item in ar]
    #print(freqs)
    result = 0
    for key in freqs:
        result = result + int(freqs[key]/2)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
