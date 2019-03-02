# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/happy-ladybugs/problem
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    if b.find('_') == -1:
        for i in range(1, len(b)-1):
            if b[i] != b[i-1] and b[i] != b[i+1]: 
                return 'NO'
    c = Counter(b)
    for k in c:
        if k != '_' and c[k] == 1:
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
