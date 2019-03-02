# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/funny-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    last_idx = len(s)-1
    last_s_ch = s[0]
    last_r_ch = s[last_idx]
    found = True
    for i in range(last_idx+1):
        if abs(ord(s[i])-ord(last_s_ch)) != abs(ord(s[last_idx-i])-ord(last_r_ch)):
            found = False
            break
        last_s_ch = s[i]
        last_r_ch = s[last_idx-i]
    return ('Funny' if found else 'Not Funny')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
