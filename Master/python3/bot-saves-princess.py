# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/bot-saves-princess/problem
#!/usr/bin/python
import math;

def displayPathtoPrincess(n,grid):
    p_posx = 0
    p_posy = 0
    m_posx = 0
    m_posy = 0
    for i in range(0, n):
        for j in range(0, n):
            if grid[i][j] == 'p':
                p_posx = i
                p_posy = j
            if grid[i][j] == 'm':
                m_posx = i
                m_posy = j
    x_dir = int((p_posx-m_posx)/abs(p_posx-m_posx))
    y_dir = int((p_posy-m_posy)/abs(p_posy-m_posy))
    for i in range(int(n/2)):
        if x_dir < 0:
            print('UP')
        else:
            print('DOWN')
        if y_dir < 0:
            print('LEFT')
        else:
            print('RIGHT')
            
    
#print all the moves here

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)