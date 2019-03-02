# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/capitalize/problem


# Complete the solve function below.
def solve(s):
    result = ''
    parts = s.split(' ')
    for p in parts:
        result = result + p[:1].upper() + p[1:] + ' '
    return result


