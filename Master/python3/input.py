# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/input/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

s = input().split(' ')
e = input()
e = e.replace('x', s[0])
print(int(eval(e)) == int(s[1]))