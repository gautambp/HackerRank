# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/lisas-workbook/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    return workbookPage(n, k, arr, 1) 

def workbookPage(n, k, arr, pg):
    if n == 0 or len(arr) == 0: return 0
    if arr[0] <= k:
        sp = (1 if pg <= arr[0] else 0)
        n -= 1
        pg += 1
        return sp + workbookPage(n, k, arr[1:], pg)
    else:
        cnt = 1
        sp = 0
        while cnt <= arr[0]:
            next_cnt = cnt+k
            if next_cnt > arr[0]:
                sp += (1 if pg >= cnt and pg <= arr[0] else 0)
            else:
                sp += (1 if pg >= cnt and pg < next_cnt else 0)
            pg += 1
            cnt += k
        n -= 1
        print('{} {} {}'.format(arr[0], pg, sp))
        return sp + workbookPage(n, k, arr[1:], pg)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
