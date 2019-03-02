# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/collectionsnamedtuple/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

n = int(input())
h = input().split()
student = namedtuple('student', h)
m_sum = 0
for _ in range(n):
    s = input().split()
    s1 = student(s[0], s[1], s[2], s[3])
    m_sum += int(s1.MARKS)
print(m_sum/n)

