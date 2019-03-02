# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-43-sub-string-divisibility/problem
from itertools import permutations

def isDivisible(l, i1, i2, i3, d):
    no = 100*l[i1]+10*l[i2]+l[i3]
    return no%d == 0

def joinDigits(l):
    no = 0
    m = 1
    l_len = len(l)
    for i in range(l_len):
        no += m * l[l_len-i-1]
        m *= 10
    return no
    
n = 3
d = [2, 3, 5, 7, 11, 13, 17]
n = int(input())
l = [i for i in range(n+1)]
sum = 0
for i in permutations(l, n+1):
    match = True
    for j in range(1, n-1):
        if not isDivisible(i, j, j+1, j+2, d[j-1]):
            match = False
            break
    #print('{} - {}'.format(i, match))
    if match:
        sum += joinDigits(i)
print(sum)

