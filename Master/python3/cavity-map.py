# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/cavity-map/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    g_len = len(grid)
    mod_g = [None]*g_len
    for i in range(g_len):
        s = ''
        for j in range(g_len):
            if i == 0 or i == g_len-1 or j == 0 or j == g_len-1:
                s += grid[i][j] 
                continue
            if grid[i][j] > grid[i][j+1] and grid[i][j] > grid[i][j-1] and grid[i][j] > grid[i-1][j] and grid[i][j] > grid[i+1][j]:
                s += 'X'
            else:
                s += grid[i][j]
        mod_g[i] = s
    return mod_g                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
