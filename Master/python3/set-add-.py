# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/set-add-/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
s = set()
for _ in range(int(input())):
    s.add(input())
print(len(s))
