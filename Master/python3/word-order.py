# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/word-order/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
l = []
for _ in range(int(input())):
    l.append(input())

c = Counter(l)
print(len(set(l)))
for k in c:
    print(c[k], end=' ')
print('')