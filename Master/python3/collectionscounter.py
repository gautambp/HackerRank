# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/collectionscounter/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

x = int(input())
sl = [int(i) for i in input().split(' ')]
m = 0
n = int(input())
for _ in range(n):
    s = input().split(' ')
    ss = int(s[0])
    if ss in sl:
        sl.remove(ss)
        m += int(s[1])
print(m)
