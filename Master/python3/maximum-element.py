# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/maximum-element/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
l = list()
l_max = None
r = range(int(input()))
for _ in r:
    s = input().split()
    if s[0] == '1':
        n = int(s[1])
        l.append(n)
        if l_max != None and n > l_max:
            l_max = n
    elif s[0] == '2':
        n = l.pop()
        l_max = None
        #if l_max and n >= l_max:
        #    l_max = None
    else:
        if l_max:
            print(l_max)
        else:
            l_max = max(l)
            print(l_max)

