# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/bill-division/problem
#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    total = reduce(lambda x, y: x+y, bill)
    a_part = int((total - bill[k])/2)
    if a_part == b:
        print('Bon Appetit')
    else:
        print(b-a_part)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
