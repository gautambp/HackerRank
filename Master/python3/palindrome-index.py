# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/palindrome-index/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def isPalindrome(s):
    s_len = len(s)
    if s_len == 1: return True
    mid_idx = s_len//2
    for i in range(mid_idx):
        if s[i] != s[s_len-1-i]:
            return False
    return True

def palindromeIndex(s):
    s_len = len(s)
    if s_len == 1: return -1
    mid_idx = s_len//2
    for i in range(mid_idx):
        if s[i] != s[s_len-1-i]:
            if isPalindrome(s[:i] + s[i+1:]):
                return i
            if isPalindrome(s[:s_len-1-i] + s[s_len-i:]):
                return s_len-1-i
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
