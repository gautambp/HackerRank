# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/drawing-book-/problem
#!/bin/python3

import os
import sys
import math

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    front = int(p/2)
    back = int((n-p)/2)
    if n%2 == 0:
        back = math.ceil((n-p)/2)
    if front < back:
        return front
    else:
        return back

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
