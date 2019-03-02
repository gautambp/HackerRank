# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/collectionsordereddict/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

d = OrderedDict()
for _ in range(int(input())):
    s = input()
    pn = s.split()
    ps = pn[len(pn)-1]
    p = int(ps)
    n = s.replace(ps, '').strip()
    if n in d:
        d[n] += p
    else:
        d[n] = p

for k in d:
    print('{} {}'.format(k, d[k]))
