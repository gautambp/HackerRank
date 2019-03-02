# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/separate-the-numbers/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    if len(s) == 1:
        print('NO')
    else:
        found = False
        n_len = 1
        while n_len < len(s):
            n1 = int(s[:n_len])
            #print('{} {}'.format(n_len, n1))
            if s[n_len:].startswith(str(n1+1)):
                n = n1+1
                f = n_len
                found = True
                while f < len(s):
                    if not s[f:].startswith(str(n)):
                        found = False
                        break
                    f += len(str(n))
                    n += 1
                if found:
                    break
            n_len += 1
        if found:
            print('{} {}'.format('YES',n1))
        else:
            print('NO')

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
