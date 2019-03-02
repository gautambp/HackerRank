# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/matrix-layer-rotation-/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    row_size = len(matrix);
    col_size = len(matrix[0]);
    num_loops = 0;
    if row_size < col_size:
        num_loops = int(row_size/2);
    else:
        num_loops = int(col_size/2);
    for l in range(num_loops):
        loop_len = 2 * (((col_size-2*l-1) + (row_size-2*l-1)));
        for rot in range(r % loop_len):
            first_val = matrix[l][l];
            for j in range(l, col_size-l-1):
                matrix[l][j] = matrix[l][j+1];
            for i in range(l, row_size-l-1):
                matrix[i][col_size-l-1] = matrix[i+1][col_size-l-1]
            for j in range(col_size-l-1, l, -1):
                matrix[row_size-l-1][j] = matrix[row_size-l-1][j-1];
            for i in range(row_size-l-1, l+1, -1):
                matrix[i][l] = matrix[i-1][l];
            matrix[l+1][l] = first_val;
    for i in range(row_size):
        is_first = True;
        for j in range(col_size):
            if is_first:
                is_first = False;
            else:
                print(' ', end='');
            print(matrix[i][j], end='');
        print('');

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
