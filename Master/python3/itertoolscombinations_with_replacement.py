# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/itertoolscombinations_with_replacement/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

aLine = input().split()
s = list(aLine[0])
k = int(aLine[1])
s.sort()
for i in combinations_with_replacement(s, k):
    print(''.join(i))

