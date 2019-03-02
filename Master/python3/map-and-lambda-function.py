# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/map-and-lambda-function/problem
cube = lambda x: x*x*x # complete the lambda function 

def fibonacci(n):
    l = []
    # return a list of fibonacci numbers
    n1 = 0
    n2 = 1
    f = 0
    while n > 0:
        l.append(n1)
        f = n1 + n2
        n1 = n2
        n2 = f
        n -= 1
    return l

