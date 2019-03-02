# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/the-grid-search/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):
    p_idx = 0
    p_pos = None
    for i in range(len(G)):
        pos = G[i].find(P[p_idx])
        #print('{} {} {}'.format(i, p_idx, pos))
        if p_pos:
            if pos < 0 or pos != p_pos:
                return 'NO'
            p_idx += 1
            if p_idx == len(P):
                return 'YES'
        else:
            if pos >= 0:
                p_pos = pos
                p_idx += 1
                if p_idx == len(P):
                    return 'YES'

    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
