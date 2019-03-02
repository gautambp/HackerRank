# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/balanced-brackets/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    l = list()
    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            l.append(ch)
        elif ch == ')' or ch == '}' or ch == ']':
            if len(l) == 0:
                return 'NO'
            l_ch = l.pop()
            if (ch == ')' and l_ch != '(') or (ch == '}' and l_ch != '{') or (ch == ']' and l_ch != '['):
                return 'NO'
    if len(l) == 0:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
