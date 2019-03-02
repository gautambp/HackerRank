# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/ginorts/problem
import string
odd_digits = ['1', '3', '5', '7', '9']
even_digits = ['2', '4', '6', '8', '0']
def comparator(x):
    if x in string.ascii_lowercase:
        return ord(x.upper())
    elif x in string.ascii_uppercase:
        return ord(x.lower())
    else:
        if x in odd_digits:
            return 123+ord(x)-5
        else:
            return 123+ord(x)+5

s = input()
print(''.join(sorted(s, key=comparator)))
