# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/refindall-&-refinditer/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

#s = 'rabcdeefgyYhFjkIoomnpOeorteeeeet'
#s = 'abaabaabaabaae' 
s = input()
m = re.compile(r'(?=([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm][AEIOUaeiou]{2,}[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]))')
l = m.findall(s)
if len(l) > 0:
    for i in l:
        print(i[1:-1])
else:
    print(-1)
