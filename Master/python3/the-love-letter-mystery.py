# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/the-love-letter-mystery/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    s_len = len(s)
    last_idx = s_len-1
    if s_len == 1: return 0
    cnt = 0
    min_len = s_len//2
    for i in range(min_len):
        if s[i] > s[last_idx-i]:
            cnt += ord(s[i])-ord(s[last_idx-i])
        elif s[i] < s[last_idx-i]:
            cnt += ord(s[last_idx-i])-ord(s[i])
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
