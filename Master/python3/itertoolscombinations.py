# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/itertoolscombinations/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

(s, n) = input().split(' ')
for j in range(1,int(n)+1):
    for i in combinations(sorted(s), j):
        print(''.join(i))
