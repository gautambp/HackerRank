# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/incorrect-regex/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

for _ in range(int(input())):
    s = input()
    try:
        re.compile(s)
        print(True)
    except Exception as e:
        print(False)

