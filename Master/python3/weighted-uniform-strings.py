# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/weighted-uniform-strings/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    l = set()
    last_val = 0
    last_ch = None
    for ch in s:
        val = ord(ch)-96
        if last_ch == None or last_ch != ch:
            last_ch = ch
            last_val = 0
        else:
            last_val += val
        l.add(val + last_val)
    result = []
    for q in queries:
        result.append('Yes' if q in l else 'No')
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
