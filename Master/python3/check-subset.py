# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/check-subset/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    input()
    a = set(map(int,input().split()))
    input()
    b = set(map(int,input().split()))
    print(a.issubset(b))
