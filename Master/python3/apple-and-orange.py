# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/apple-and-orange/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    a_cnt = 0
    o_cnt = 0
    for i in apples:
        if (a+i >= s) and (a+i <= t):
            a_cnt += 1
    for i in oranges:
        if (b+i <= t) and (b+i >= s):
            o_cnt += 1
    print(a_cnt)
    print(o_cnt)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
