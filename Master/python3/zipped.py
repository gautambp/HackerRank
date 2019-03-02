# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/zipped/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input().split(' ')
n = int(s[0])
x = int(s[1])
all_sub_marks = [None]*x
for i in range(x):
    all_sub_marks[i] = [float(j) for j in input().split(' ')]

for i in zip(*all_sub_marks):
    print(sum(i)/x)


