# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/swap-case/problem
def swap_case(s):
    result = ''
    for c in s:
        if c.isupper():
            result += c.lower()
        else:
            result += c.upper()
    return result

