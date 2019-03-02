# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/the-captains-room-/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

k = int(input())
l = list(map(int,input().split()))
g = len(l) // k
c = collections.Counter(l)
for i in c:
    if c[i] == 1:
        print(i)
        break
