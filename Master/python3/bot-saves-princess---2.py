# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/bot-saves-princess---2/problem
#

def findPrincessPos(n, grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                return (i, j)
    return (0, 0)
    
def nextMove(n,r,c,grid):
    pr, pc = findPrincessPos(n, grid)
    dr, dc = r-pr, c-pc
    if dc > 0:
        return ("LEFT" if dc > abs(dr) else "UP" if dr > 0 else "DOWN")
    return ("RIGHT" if abs(dc) > abs(dr) else "UP" if dr > 0 else "DOWN")

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))