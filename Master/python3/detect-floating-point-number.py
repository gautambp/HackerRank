# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/detect-floating-point-number/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    s = input()
    try:
        if s.find('.') >= 0:
            f = float(s)
            print(True)
        else:
            print(False)
    except Exception as e:
        print(False)
