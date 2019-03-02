# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/equal-stacks/problem
#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    h1_sum = sum(h1)
    h2_sum = sum(h2)
    h3_sum = sum(h3)
    while h1_sum != h2_sum or h2_sum != h3_sum:
        if h1_sum >= h2_sum and h1_sum >= h3_sum:
            n = h1.pop(0)
            h1_sum -= n
        elif h2_sum >= h1_sum and h2_sum >= h3_sum:
            n = h2.pop(0)
            h2_sum -= n
        elif h3_sum >= h1_sum and h3_sum >= h2_sum:
            n = h3.pop(0)
            h3_sum -= n
    return h1_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
