# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
def wrapper(f):
    def fun(l):
        f(map(lambda n: '+91 ' + n[-10:-5] + ' ' + n[-5:], l))

        # complete the function
    return fun

