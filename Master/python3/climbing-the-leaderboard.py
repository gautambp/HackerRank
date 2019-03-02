# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def compareInList(l, a, idx_from, idx_to):
    if (a >= l[idx_from]):
        return idx_from
    if (a < l[idx_to]):
        return idx_to+1
    idx_mid = idx_from + int((idx_to - idx_from)/2)
    if a > l[idx_mid]:
        return compareInList(l, a, idx_from, idx_mid)
    elif a < l[idx_mid]:
        return compareInList(l, a, idx_mid+1, idx_to)
    else:
        return idx_mid

def climbingLeaderboard(scores, alice):
    sorted_score = sorted(set(scores), reverse=True)
    s_len = len(sorted_score)
    a_rank = []
    for a in alice:
        rank = compareInList(sorted_score, a, 0, s_len-1)+1
        print(rank)
        a_rank.append(rank)
    return a_rank

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
