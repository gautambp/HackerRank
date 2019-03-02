# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/set-mutations/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
a = set(map(int, input().split()))

for _ in range(int(input())):
    ops = input().split()[0]
    b = set(map(int, input().split()))
    if ops == 'intersection_update':
        a &= b
    elif ops == 'update':
        a |= b
    elif ops == 'symmetric_difference_update':
        a ^= b
    elif ops == 'difference_update':
        a -= b

print(sum(a))
