# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/angry-professor/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    s_cnt = list(filter(lambda x: x<=0, a))
    if len(s_cnt) >= k:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
