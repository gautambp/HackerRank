# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-24-lexicographic-permutations/problem
import math

s = 13
fact = [math.factorial(i) for i in range(s+1)]
ch_l = [chr(ord('a')+i) for i in range(s)]

for _ in range(int(input())):   
    n = int(input())-1
    ch = ch_l.copy()
    l = [None]*s
    for i in range(1,s):
        l[i-1] = ch[( n // fact[s-i] )]
        ch.remove(l[i-1])
        n = n%fact[s-i]
    l[-1] = ch[0]
    print(''.join(l))
