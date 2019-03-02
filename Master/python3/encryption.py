# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/encryption/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s = s.replace(' ', '')
    l = (len(s) ** 0.5)
    r = int(l)
    c = math.ceil(l)
    if r*c < len(s):
        r += 1
    #print('{} {}'.format(r,c))
    sl = ['']*c
    for i in range(len(s)):
        ci = i%c
        sl[ci] += s[i]
    return ' '.join(sl)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
