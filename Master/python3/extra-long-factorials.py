# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/extra-long-factorials/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    print(fact)

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
