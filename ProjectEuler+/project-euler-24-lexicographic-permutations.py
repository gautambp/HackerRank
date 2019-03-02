# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-24-lexicographic-permutations/problem
from itertools import permutations

for _ in range(int(input())):
    n = int(input())
    for p in permutations('abcdefghijklm'):
        n -= 1
        if n <= 0:
            print(''.join(p))
            break