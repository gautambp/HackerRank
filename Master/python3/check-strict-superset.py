# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/check-strict-superset/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

a = set(map(int,input().split()))
result = True
for _ in range(int(input())):
    b = set(map(int,input().split()))
    result = a.issuperset(b)
    if not result:
        break
print(result)

