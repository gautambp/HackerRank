# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/exceptions/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    s = input().split()
    try:
        a = int(s[0])
        b = int(s[1])
        r = a//b
        print(r)
    except Exception as ze:
        print("Error Code:",ze)
    