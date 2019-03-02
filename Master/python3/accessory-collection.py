# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/accessory-collection/problem
#!/bin/python3

import os
import sys

#
# Complete the acessoryCollection function below.
#
def acessoryCollection(L, A, N, D):
    #
    # Write your code here.
    #
    if D > A:
        return 'SAD'
    total = 0
    for i in range(A, A-N, -1):
        if L <= 0:
            break
        total += i*D
        L = L-1
    return str(total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        LAND = input().split()

        L = int(LAND[0])

        A = int(LAND[1])

        N = int(LAND[2])

        D = int(LAND[3])

        result = acessoryCollection(L, A, N, D)

        fptr.write(result + '\n')

    fptr.close()
