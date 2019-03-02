# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/game-of-two-stacks/problem
#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#
def twoStacks(x, a, b):
    #
    # Write your code here.
    #
    a_idx = 0
    b_idx = 0
    ab_sum = 0
    while ab_sum < x:
        if a_idx >= len(a) and b_idx >= len(b):
            break
        elif a_idx >= len(a):
            ab_sum += b[b_idx]
            b_idx += 1
        elif b_idx >= len(b):
            ab_sum += a[a_idx]
            a_idx += 1
        elif a[a_idx] >= b[b_idx]:
            ab_sum += b[b_idx]
            b_idx += 1
        else:
            ab_sum += a[a_idx]
            a_idx += 1

    return a_idx+b_idx-1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
