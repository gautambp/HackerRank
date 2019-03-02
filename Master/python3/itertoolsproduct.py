# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/itertoolsproduct/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

aLine = input()
A = []
for i in aLine.split(' '):
    A.append(int(i))

aLine = input()
B = []
for i in aLine.split(' '):
    B.append(int(i))

for i in product(A, B):
    print(i, end=' ')

