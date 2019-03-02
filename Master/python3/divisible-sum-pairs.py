# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    pair_count = 0;
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j])%k == 0:
                pair_count = pair_count + 1;
    return pair_count;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
