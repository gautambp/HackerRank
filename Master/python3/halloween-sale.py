# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/halloween-sale/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    if s < p: return 0
    di = 0
    g_cnt = 0
    while s >= m:
        if p - di*d > m:
            if s < p-di*d:
                break
            s -= p - di*d
            g_cnt += 1
            di += 1
        else:
            s -= m
            g_cnt += 1
    return g_cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
