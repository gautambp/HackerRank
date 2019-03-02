# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

a = defaultdict(list)

(n, m) = [int(i) for i in input().split(' ')]
for i in range(n):
    a[input()].append(i+1)
b = [input() for _ in range(m)]
for item in b:
    if item in a:
        for i in a[item]:
            print(i, end=' ')
        print('')
    else:
        print(-1)
