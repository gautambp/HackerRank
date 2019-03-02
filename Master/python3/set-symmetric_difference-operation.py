# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/set-symmetric_difference-operation/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
a = set(map(int, input().split()))
input()
b = set(map(int, input().split()))
print(len(a.symmetric_difference(b)))