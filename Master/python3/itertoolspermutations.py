# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/itertoolspermutations/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

(s, sc) = input().split(' ')
ss = set()
for i in permutations(s, int(sc)):
    ss.add(''.join(i))
for i in sorted(ss):
    print(i)

