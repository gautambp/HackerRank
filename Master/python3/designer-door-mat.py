# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/designer-door-mat/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

(ns, ms) = input().split(' ')
n = int(ns)
m = int(ms)
n_half = int(n/2)
m_half = int(m/2)
msg = 'WELCOME'
s = '.|.'
for i in range(n):
    for j in range(m):
        if i == n_half:
            if j < m_half-3 or j > m_half+3:
                print('-', end='')
            else:
                print(msg[j-m_half-4], end='')
        else:
            t = 0
            if i < n_half:
                t = int(((2*i+1)*3)/2)
            else:
                t = int(((2*(n-i-1)+1)*3)/2)
            if j < m_half-t or j > m_half+t:
                print('-', end='')
            else:
                print(s[j%3], end='')
    print('')
