# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/forming-a-magic-square/problem
#!/bin/python3

import math
import os
import random
import re
import sys

def generateMagicSquare():
    s = [None]*8
    s[0] = [[8,1,6],[3,5,7],[4,9,2]]
    s[1] = [[6,1,8],[7,5,3],[2,9,4]]
    s[2] = [[4,9,2],[3,5,7],[8,1,6]]
    s[3] = [[2,9,4],[7,5,3],[6,1,8]]
    s[4] = [[8,3,4],[1,5,9],[6,7,2]]
    s[5] = [[4,3,8],[9,5,1],[2,7,6]]
    s[6] = [[6,7,2],[1,5,9],[8,3,4]]
    s[7] = [[2,7,6],[9,5,1],[4,3,8]]
    for i in range(8):
        yield s[i]

def diff(s1, s2):
    d = 0
    for i in range(3):
        for j in range(3):
            d += abs(s1[i][j]-s2[i][j])
    return d

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    c_min = None
    for ms in generateMagicSquare():
        c = diff(s, ms)
        if c_min == None or c < c_min:
            c_min = c
    return c_min

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
