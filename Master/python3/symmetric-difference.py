# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/symmetric-difference/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

m = int(input())
m_s = set(map(int,input().split()))
n = int(input())
n_s = set(map(int,input().split()))
l = list(m_s.difference(n_s))
l.extend(n_s.difference(m_s))
for i in sorted(l):
    print(i)
