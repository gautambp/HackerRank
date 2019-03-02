# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/HourRank-29/customized-chess-board/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(board):
    b_len = len(board)
    for i in range(b_len-1):
        for j in range(b_len-1):
            if (board[i][j] + board[i+1][j] != 1 or board[i][j] + board[i][j+1] != 1):
                return 'No'
    return 'Yes'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        board = []

        for _ in range(n):
            board.append(list(map(int, input().rstrip().split())))

        result = solve(board)

        fptr.write(result + '\n')

    fptr.close()
