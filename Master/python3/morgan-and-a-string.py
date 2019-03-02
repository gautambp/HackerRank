# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/morgan-and-a-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

def compare(a, b, a_idx, b_idx):
    if a[a_idx] < b[b_idx]:
        return True;
    elif a[a_idx] > b[b_idx]:
        return False;
    else:
        a_rest = a[a_idx:]+'z';
        b_rest = b[b_idx:]+'z';
        if a_rest < b_rest:
            return True;
        else:
            return False;
    
# Complete the morganAndString function below.
def morganAndString(a, b):
    result = '';
    a_idx = 0;
    b_idx = 0;
    a_len = len(a);
    b_len = len(b);
    while True:
        if a_idx >= a_len:
            result += b[b_idx:];
            break;
        if b_idx >= b_len:
            result += a[a_idx:];
            break;
        if compare(a, b, a_idx, b_idx):
            result += a[a_idx];
            a_idx = a_idx+1;
        else:
            result += b[b_idx];
            b_idx = b_idx+1;
    return result;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        fptr.write(result + '\n')

    fptr.close()
