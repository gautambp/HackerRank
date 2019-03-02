# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/arrays/problem


def arrays(arr):
    # complete this function
    # use numpy.array
    l = list(map(float, reversed(arr)))
    return numpy.array(l)

