# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/validating-phone-numbers/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

#s = '7587406281'
for _ in range(int(input())):
    s = input()
    if len(s) == 10 and re.match(r'[$789][0-9]{9}', s):
        print('YES')
    else:
        print('NO')
