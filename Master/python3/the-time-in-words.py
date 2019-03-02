# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/the-time-in-words/problem
#!/bin/python3

import math
import os
import random
import re
import sys

d = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'quarter',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'half',
    40:'fourty',
    50:'fifty'
}
# Complete the timeInWords function below.
def timeInWords(h, m):
    if m == 0:
        return d[h] + ' o\' clock'
    else:
        if m == 30:
            return 'half past ' + d[h]
        elif m == 15:
            return d[m] + ' past ' + d[h]
        elif m < 30:
            ms = (d[m] if m <= 20 else d[10*(m//10)] + ' ' + d[m%10])
            return ms + ' minute' + ('s' if m > 1 else '') + ' past ' + d[h]
        else:
            m = 60-m
            h += 1
            if m == 15:
                return d[m] + ' to ' + d[h]
            else:
                ms = (d[m] if m <= 20 else d[10*(m//10)] + ' ' + d[m%10])
                return ms + ' minute' + ('s' if m > 1 else '') + ' to ' + d[h]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
