# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/viral-advertising/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    total_ppl_liked = 0
    no_ppl = 5
    for i in range(n):
        ppl_liked = math.floor(no_ppl/2)
        total_ppl_liked += ppl_liked
        no_ppl = ppl_liked * 3
    return total_ppl_liked

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
