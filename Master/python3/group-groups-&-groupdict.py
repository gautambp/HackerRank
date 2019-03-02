# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/group-groups-&-groupdict/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

s = input()
m = re.compile(r'(.)\1*')
found = False
for i in m.finditer(s):
    g = i.group()
    if g.isalnum() and len(g) > 1:
        print(g[0])
        found = True
        break

if not found:
    print(-1)
