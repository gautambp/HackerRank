# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/validating-roman-numerals/problem
th = 'M{0,3}'
h = '(C[MD]|D?C{0,3})'
t = '(X[CL]|L?X{0,3})'
d = '(I[VX]|V?I{0,3})'

regex_pattern = r"%s%s%s%s$" % (th, h, t, d)

