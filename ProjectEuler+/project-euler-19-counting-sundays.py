# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-19-counting-sundays/problem
import datetime as dt
from dateutil.relativedelta import *

def solve(d1, d2):
    cnt = 0
    td = relativedelta(months=1)
    d = dt.date(d1.year, d1.month, 1)
    if d > d1:
        d = d + td
    while d <= d2:
        if d.weekday() == 6:
            cnt += 1
        d = d + td
    return cnt
        
    
q = int(input())
for _ in range(q):
    d1s = input().split(' ')
    d2s = input().split(' ')
    d1 = dt.date(int(d1s[0]), int(d1s[1]), int(d1s[2]))
    d2 = dt.date(int(d2s[0]), int(d2s[1]), int(d2s[2]))
    print(solve(d1, d2))