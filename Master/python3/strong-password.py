# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/strong-password/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    cnt = 0
    if sum([1 for p in password if p.isdigit()]) == 0:
        cnt += 1
    if sum([1 for p in password if p.islower()]) == 0:
        cnt += 1
    if sum([1 for p in password if p.isupper()]) == 0:
        cnt += 1
    if sum([1 for p in password if "!@#$%^&*()-+".find(p) >= 0]) == 0:
        cnt += 1
    return (cnt if n+cnt >= 6 else 6-n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
