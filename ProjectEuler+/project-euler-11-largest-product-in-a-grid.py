# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-11-largest-product-in-a-grid/problem
#!/bin/python3

import sys

def solve(grid):
    g_len = len(grid)
    max_product = None
    for i in range(g_len):
        for j in range(g_len):
            if j <= g_len-4:
                p = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
                if max_product == None:
                    max_product = p
                if max_product < p:
                    max_product = p
            if i <= g_len-4:
                p = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
                if max_product < p:
                    max_product = p
            if i <= g_len-4 and j <= g_len-4:
                p = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
                if max_product < p:
                    max_product = p
                p = grid[i][j+3] * grid[i+1][j+2] * grid[i+2][j+1] * grid[i+3][j]
                if max_product < p:
                    max_product = p
    print(max_product)
            

grid = []
for grid_i in range(20):
	grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
	grid.append(grid_t)
solve(grid)
