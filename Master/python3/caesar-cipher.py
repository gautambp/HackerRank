# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/caesar-cipher/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    r = k%26
    result = ''
    for ch in s:
        if ch.isalpha():
            new_ch = ord(ch)+r
            if (ch.isupper() and new_ch > 90) or (ch.islower() and new_ch > 122):
                new_ch -= 26
            result += chr(new_ch)
        else:
            result += ch
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
