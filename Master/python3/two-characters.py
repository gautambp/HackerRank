# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/two-characters/problem
#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby
from collections import Counter

# Complete the alternate function below.
def isStringAlternate(s):
    if len(s) < 2: return False
    e_ch = s[0]
    o_ch = s[1]
    if e_ch == o_ch:
        return False
    for i in range(2,len(s)):
        if i%2 == 0 and e_ch != s[i]:
            return False
        if i%2 == 1 and o_ch != s[i]:
            return False
    return True

def alternate(s):
    matcher = re.compile(r'(.)\1+')
    for m in matcher.finditer(s):
        ch = m.group()[0]
        s = s.replace(ch, '')
    if len(s) == 0 or isStringAlternate(s):
        return len(s)
    c = Counter(s)
    cnt_max = 0
    for k in c.items():
        cnt = alternate(s.replace(k[0], ''))
        if cnt > cnt_max:
            cnt_max = cnt
    return cnt_max 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
