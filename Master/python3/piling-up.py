# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/piling-up/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

for _ in range(int(input())):
    n = int(input())
    d = deque(map(int,input().split()))
    last_no = None
    found = True
    for i in range(n):
        if d[0] > d[len(d)-1]:
            if last_no and d[0] > last_no:
                found = False
                break
            last_no = d.popleft()
        else:
            if last_no and d[len(d)-1] > last_no:
                found = False
                break
            last_no = d.pop()
    if found:
        print('Yes')
    else:
        print('No')

