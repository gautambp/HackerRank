# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/collectionsdeque/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

d = deque()
for _ in range(int(input())):
    ops = input().split()
    if ops[0] == 'append':
        d.append(int(ops[1]))
    elif ops[0] == 'appendleft':
        d.appendleft(int(ops[1]))
    elif ops[0] == 'pop':
        d.pop()
    elif ops[0] == 'popleft':
        d.popleft()
print(*d, sep=' ')
