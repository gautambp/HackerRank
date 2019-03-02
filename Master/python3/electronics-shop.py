# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/electronics-shop/problem
#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    can_buy = False
    max_amt = 0
    for k in keyboards:
        for d in drives:
            s = k+d
            if s <= b and s > max_amt:
                max_amt = s
                can_buy = True
    if can_buy == True:
        return max_amt
    else:
        return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
