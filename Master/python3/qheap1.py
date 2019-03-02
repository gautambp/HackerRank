# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/qheap1/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

import heapq

hq = []
is_dirty = True
r = range(int(input()))
for _ in r:
    s = input().split()
    if s[0] == '1':
        n = int(s[1])
        heapq.heappush(hq, n)
    elif s[0] == '2':
        n = int(s[1])
        hq.remove(n)
        is_dirty = True
    elif s[0] == '3':
        if is_dirty:
            heapq.heapify(hq)
        print(hq[0])
        is_dirty = False
