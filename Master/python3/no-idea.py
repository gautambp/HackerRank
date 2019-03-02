# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/no-idea/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

(m, n) = list(map(int,input().split()))
i_l = list(map(int,input().split()))
a = set(map(int,input().split()))
b = set(map(int,input().split()))
h = 0
for i in i_l:
    if i in a:
        h += 1
    if i in b:
        h -= 1
print(h)